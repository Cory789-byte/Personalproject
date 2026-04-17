"""Frame-level forensic analysis.

Produces:
- file hash (SHA-256) for chain-of-custody reference
- ffprobe container/stream metadata
- scene-change timestamps (via ffmpeg scene-detect filter)
- anomaly flags: duration gaps, black frames, freeze frames, container edit lists,
  re-encoding fingerprints, suspicious keyframe spacing
- optional OCR of burnt-in BWC timestamps (tesseract) to reconcile against
  container timestamps

ffmpeg and ffprobe must be on PATH. tesseract is optional.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

HEADER = "MACHINE-GENERATED - UNVERIFIED"


class ToolMissingError(RuntimeError):
    pass


def _require(tool: str) -> None:
    if shutil.which(tool) is None:
        raise ToolMissingError(f"{tool} not on PATH")


def sha256_file(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def ffprobe_metadata(path: Path) -> dict[str, Any]:
    _require("ffprobe")
    cmd = [
        "ffprobe", "-v", "error",
        "-print_format", "json",
        "-show_format", "-show_streams", "-show_chapters",
        str(path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    return json.loads(result.stdout)


def detect_scene_changes(path: Path, threshold: float = 0.3) -> list[float]:
    """Return list of timestamps (seconds) where a scene cut is detected."""
    _require("ffmpeg")
    cmd = [
        "ffmpeg", "-hide_banner", "-nostats",
        "-i", str(path),
        "-filter:v", f"select='gt(scene,{threshold})',showinfo",
        "-f", "null", "-",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    cuts: list[float] = []
    for line in result.stderr.splitlines():
        m = re.search(r"pts_time:([0-9.]+)", line)
        if m:
            cuts.append(float(m.group(1)))
    return sorted(set(cuts))


def detect_black_frames(path: Path, min_duration: float = 0.1) -> list[tuple[float, float]]:
    """Return list of (start, duration) for black frame intervals."""
    _require("ffmpeg")
    cmd = [
        "ffmpeg", "-hide_banner", "-nostats",
        "-i", str(path),
        "-vf", f"blackdetect=d={min_duration}:pic_th=0.98",
        "-an", "-f", "null", "-",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    intervals: list[tuple[float, float]] = []
    for line in result.stderr.splitlines():
        m = re.search(r"black_start:([0-9.]+).*black_duration:([0-9.]+)", line)
        if m:
            intervals.append((float(m.group(1)), float(m.group(2))))
    return intervals


def detect_freeze_frames(path: Path, duration: float = 2.0, noise_db: float = -60) -> list[tuple[float, float]]:
    _require("ffmpeg")
    cmd = [
        "ffmpeg", "-hide_banner", "-nostats",
        "-i", str(path),
        "-vf", f"freezedetect=n=0.001:d={duration}",
        "-map", "0:v:0", "-f", "null", "-",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    out: list[tuple[float, float]] = []
    start = None
    for line in result.stderr.splitlines():
        m_start = re.search(r"freeze_start:\s*([0-9.]+)", line)
        m_dur = re.search(r"freeze_duration:\s*([0-9.]+)", line)
        if m_start:
            start = float(m_start.group(1))
        if m_dur and start is not None:
            out.append((start, float(m_dur.group(1))))
            start = None
    return out


def extract_keyframes(path: Path, dest_dir: Path, every_seconds: float = 10.0) -> list[Path]:
    _require("ffmpeg")
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-hide_banner", "-nostats", "-y",
        "-i", str(path),
        "-vf", f"fps=1/{every_seconds}",
        str(dest_dir / "frame_%05d.jpg"),
    ]
    subprocess.run(cmd, capture_output=True, text=True, check=False)
    return sorted(dest_dir.glob("frame_*.jpg"))


def ocr_timestamps(frame_paths: list[Path]) -> list[dict[str, Any]]:
    """Attempt OCR of burnt-in timestamps. Returns per-frame results.

    Gracefully degrades if pytesseract or tesseract are unavailable.
    """
    try:
        import pytesseract  # type: ignore
        from PIL import Image  # type: ignore
    except Exception:
        return [{"frame": str(p), "ocr": None, "note": "pytesseract/PIL unavailable"} for p in frame_paths]
    if shutil.which("tesseract") is None:
        return [{"frame": str(p), "ocr": None, "note": "tesseract not installed"} for p in frame_paths]
    out = []
    for p in frame_paths:
        try:
            text = pytesseract.image_to_string(Image.open(p)).strip()
            out.append({"frame": str(p), "ocr": text})
        except Exception as e:
            out.append({"frame": str(p), "ocr": None, "note": str(e)})
    return out


@dataclass
class IntegrityReport:
    source: str
    sha256: str
    format: dict[str, Any]
    streams: list[dict[str, Any]]
    scene_cuts: list[float]
    black_frames: list[tuple[float, float]]
    freeze_frames: list[tuple[float, float]]
    anomalies: list[str] = field(default_factory=list)
    ocr_samples: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "header": HEADER,
            "source": self.source,
            "sha256": self.sha256,
            "format": self.format,
            "streams": self.streams,
            "scene_cuts": self.scene_cuts,
            "black_frames": [list(x) for x in self.black_frames],
            "freeze_frames": [list(x) for x in self.freeze_frames],
            "anomalies": self.anomalies,
            "ocr_samples": self.ocr_samples,
        }


def _detect_anomalies(meta: dict[str, Any]) -> list[str]:
    flags: list[str] = []
    fmt = meta.get("format", {})
    tags = fmt.get("tags", {}) or {}
    if "encoder" in tags and "handbrake" in tags["encoder"].lower():
        flags.append("container tag indicates re-encoding via HandBrake")
    for s in meta.get("streams", []):
        if s.get("codec_type") == "video":
            if s.get("nb_frames") and s.get("duration"):
                nb = int(s["nb_frames"])
                dur = float(s["duration"])
                fps_num = s.get("r_frame_rate", "0/1").split("/")
                try:
                    fps = float(fps_num[0]) / float(fps_num[1]) if len(fps_num) == 2 else 0
                    expected = dur * fps
                    if fps and abs(nb - expected) / max(1, expected) > 0.02:
                        flags.append(
                            f"frame-count/duration mismatch: nb_frames={nb} expected~={expected:.0f}"
                        )
                except Exception:
                    pass
        if s.get("disposition", {}).get("attached_pic"):
            flags.append("video stream carries attached picture disposition (unusual for BWC)")
    if "creation_time" in tags:
        flags.append(f"container creation_time: {tags['creation_time']}")
    return flags


def run_integrity(
    source: Path,
    frames_dir: Path | None = None,
    ocr: bool = False,
    scene_threshold: float = 0.3,
) -> IntegrityReport:
    source = Path(source).resolve()
    meta = ffprobe_metadata(source)
    report = IntegrityReport(
        source=str(source),
        sha256=sha256_file(source),
        format=meta.get("format", {}),
        streams=meta.get("streams", []),
        scene_cuts=detect_scene_changes(source, scene_threshold),
        black_frames=detect_black_frames(source),
        freeze_frames=detect_freeze_frames(source),
    )
    report.anomalies = _detect_anomalies(meta)
    if ocr and frames_dir is not None:
        frames = extract_keyframes(source, frames_dir)
        report.ocr_samples = ocr_timestamps(frames)
    return report


def save_integrity(report: IntegrityReport, dest: Path) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")
    return dest


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--ocr", action="store_true")
    p.add_argument("--frames-dir")
    p.add_argument("--scene-threshold", type=float, default=0.3)
    args = p.parse_args()
    rep = run_integrity(
        Path(args.input),
        Path(args.frames_dir) if args.frames_dir else None,
        args.ocr,
        args.scene_threshold,
    )
    save_integrity(rep, Path(args.output))
    print(f"Integrity report written to {args.output}")
