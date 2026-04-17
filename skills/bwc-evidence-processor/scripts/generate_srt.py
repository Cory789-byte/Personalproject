"""Render SRT and WebVTT subtitle files from transcript segments."""

from __future__ import annotations

import json
from pathlib import Path

HEADER = "MACHINE-GENERATED - UNVERIFIED"


def _load_segments(transcript_json: Path) -> list[dict]:
    data = json.loads(Path(transcript_json).read_text())
    return data["segments"]


def _srt_ts(seconds: float) -> str:
    ms = int(round(max(0.0, float(seconds)) * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _vtt_ts(seconds: float) -> str:
    ms = int(round(max(0.0, float(seconds)) * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def write_srt(transcript_json: Path, dest: Path) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    segments = _load_segments(transcript_json)

    blocks = [
        f"1\n{_srt_ts(0)} --> {_srt_ts(2)}\n[{HEADER}]\n"
    ]
    for i, seg in enumerate(segments, start=2):
        blocks.append(
            f"{i}\n{_srt_ts(seg['start'])} --> {_srt_ts(seg['end'])}\n"
            f"{seg['text']}\n"
        )
    dest.write_text("\n".join(blocks))
    return dest


def write_vtt(transcript_json: Path, dest: Path) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    segments = _load_segments(transcript_json)

    lines = ["WEBVTT", f"NOTE {HEADER}", ""]
    for seg in segments:
        lines.append(f"{_vtt_ts(seg['start'])} --> {_vtt_ts(seg['end'])}")
        lines.append(seg["text"])
        lines.append("")
    dest.write_text("\n".join(lines))
    return dest


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript", required=True)
    parser.add_argument("--srt")
    parser.add_argument("--vtt")
    args = parser.parse_args()

    if args.srt:
        write_srt(Path(args.transcript), Path(args.srt))
    if args.vtt:
        write_vtt(Path(args.transcript), Path(args.vtt))
