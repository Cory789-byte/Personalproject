"""Extract single frames from video at exact timestamps, optionally
cropping and up-scaling for OCR. Designed for forensic zoom-in on
on-screen evidence like mail, documents, ID cards, licence plates.

Usage (CLI):

    python scripts/frame_extract.py \
        --video "C:/Evidence/.../Exhibit.mp4" \
        --timestamp 00:01:23.5 \
        --output C:/Evidence/.../output/frames/mail.png \
        --crop 400,300,200,150 \
        --zoom 3 \
        --ocr

Timestamp accepts either seconds (e.g. 83.5) or HH:MM:SS[.ms].

Crop is an integer tuple (x,y,w,h) in source pixels. Omit for the
full frame. Use --crop-pct instead if you want percentages.

Library:

    from frame_extract import extract_frame, ocr_frame, extract_and_ocr
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _path_helper import ensure_tools_on_path, locate  # noqa: E402

ensure_tools_on_path()


HEADER = "MACHINE-GENERATED - UNVERIFIED"


def parse_timestamp(value: str | float | int) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    v = str(value).strip()
    # HH:MM:SS[.ms]
    m = re.match(r"^(\d+):([0-5]?\d):([0-5]?\d(?:\.\d+)?)$", v)
    if m:
        h, mi, s = m.groups()
        return int(h) * 3600 + int(mi) * 60 + float(s)
    # MM:SS[.ms]
    m = re.match(r"^([0-5]?\d):([0-5]?\d(?:\.\d+)?)$", v)
    if m:
        mi, s = m.groups()
        return int(mi) * 60 + float(s)
    # seconds
    return float(v)


def extract_frame(
    video: Path,
    timestamp: float | str,
    dest: Path,
    crop: tuple[int, int, int, int] | None = None,
    crop_pct: tuple[float, float, float, float] | None = None,
    zoom: float = 1.0,
    sharpen: bool = True,
) -> Path:
    """Pull a single frame. Returns the destination path.

    crop: (x, y, w, h) in pixels (source coords). Applied before zoom.
    crop_pct: (x_pct, y_pct, w_pct, h_pct) in 0-1 range. Requires probing
              frame dimensions first.
    zoom: 2.0 = double size (lanczos). Useful for OCR legibility.
    sharpen: apply unsharp mask after zoom.
    """
    if locate("ffmpeg") is None:
        raise RuntimeError("ffmpeg not on PATH")

    ts = parse_timestamp(timestamp)
    video = Path(video).resolve()
    dest = Path(dest).resolve()
    dest.parent.mkdir(parents=True, exist_ok=True)

    if not video.is_file():
        raise FileNotFoundError(video)

    if crop_pct is not None and crop is None:
        w, h = _video_wh(video)
        xp, yp, wp, hp = crop_pct
        crop = (int(w * xp), int(h * yp), int(w * wp), int(h * hp))

    filters: list[str] = []
    if crop:
        x, y, cw, ch = crop
        filters.append(f"crop={cw}:{ch}:{x}:{y}")
    if zoom and zoom != 1.0:
        filters.append(f"scale=iw*{zoom}:ih*{zoom}:flags=lanczos")
    if sharpen:
        filters.append("unsharp=5:5:1.0:5:5:0.0")

    cmd = [
        "ffmpeg", "-hide_banner", "-nostats", "-y",
        "-ss", str(ts),
        "-i", str(video),
        "-frames:v", "1",
        "-update", "1",
    ]
    if filters:
        cmd += ["-vf", ",".join(filters)]
    cmd.append(str(dest))

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"ffmpeg failed (exit {result.returncode}):\n{result.stderr[-1500:]}"
        )
    if not dest.is_file() or dest.stat().st_size == 0:
        raise RuntimeError("ffmpeg did not produce an output frame")
    return dest


def _video_wh(video: Path) -> tuple[int, int]:
    if locate("ffprobe") is None:
        raise RuntimeError("ffprobe not on PATH")
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height",
         "-of", "csv=p=0:s=x", str(video)],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        raise RuntimeError(out.stderr)
    w, h = out.stdout.strip().split("x")
    return int(w), int(h)


def ocr_frame(image: Path, config: str = "--psm 6") -> str:
    try:
        import pytesseract  # type: ignore
        from PIL import Image  # type: ignore
    except Exception as e:
        raise RuntimeError(f"pytesseract / Pillow not installed: {e}")
    if locate("tesseract") is None:
        raise RuntimeError("tesseract not on PATH (install from UB-Mannheim)")
    return pytesseract.image_to_string(Image.open(image), config=config).strip()


def extract_and_ocr(
    video: Path,
    timestamp: float | str,
    dest: Path,
    crop: tuple[int, int, int, int] | None = None,
    crop_pct: tuple[float, float, float, float] | None = None,
    zoom: float = 2.0,
    psm: int = 6,
) -> tuple[Path, str]:
    extract_frame(video, timestamp, dest, crop=crop, crop_pct=crop_pct, zoom=zoom)
    text = ocr_frame(dest, config=f"--psm {psm}")
    sidecar = dest.with_suffix(".ocr.txt")
    sidecar.write_text(
        f"# {HEADER}\nsource: {video}\ntimestamp_seconds: {parse_timestamp(timestamp)}\n"
        f"crop: {crop or crop_pct or '-'}\nzoom: {zoom}\n\n{text}\n",
        encoding="utf-8",
    )
    return dest, text


def _parse_crop(s: str) -> tuple[int, int, int, int]:
    parts = [int(p.strip()) for p in s.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("--crop must be four ints: x,y,w,h")
    return tuple(parts)  # type: ignore


def _parse_crop_pct(s: str) -> tuple[float, float, float, float]:
    parts = [float(p.strip()) for p in s.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("--crop-pct must be four floats: x,y,w,h (0-1)")
    return tuple(parts)  # type: ignore


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--video", required=True)
    p.add_argument("--timestamp", required=True,
                   help="seconds or HH:MM:SS[.ms]")
    p.add_argument("--output", required=True, help="destination PNG/JPG")
    p.add_argument("--crop", type=_parse_crop, default=None,
                   help="x,y,w,h in source pixels")
    p.add_argument("--crop-pct", type=_parse_crop_pct, default=None,
                   help="x,y,w,h in 0..1 fractions")
    p.add_argument("--zoom", type=float, default=1.0)
    p.add_argument("--no-sharpen", action="store_true")
    p.add_argument("--ocr", action="store_true")
    p.add_argument("--psm", type=int, default=6)
    args = p.parse_args()

    if args.ocr:
        dest, text = extract_and_ocr(
            Path(args.video), args.timestamp, Path(args.output),
            crop=args.crop, crop_pct=args.crop_pct,
            zoom=args.zoom or 1.0, psm=args.psm,
        )
        print(f"Frame:   {dest}")
        print(f"OCR:     {dest.with_suffix('.ocr.txt')}")
        print("----- OCR text -----")
        print(text or "(empty)")
    else:
        dest = extract_frame(
            Path(args.video), args.timestamp, Path(args.output),
            crop=args.crop, crop_pct=args.crop_pct,
            zoom=args.zoom or 1.0, sharpen=not args.no_sharpen,
        )
        print(f"Frame: {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
