"""Extract a 16kHz mono WAV track from a source media file using ffmpeg."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


class FFmpegMissingError(RuntimeError):
    pass


class AudioExtractionError(RuntimeError):
    pass


def extract_audio(source: Path, dest: Path) -> Path:
    if shutil.which("ffmpeg") is None:
        raise FFmpegMissingError(
            "ffmpeg not found on PATH. Install it (Debian/Ubuntu: "
            "`sudo apt-get install -y ffmpeg`)."
        )

    source = Path(source).expanduser().resolve()
    dest = Path(dest).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(source)

    dest.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(source),
        "-vn",
        "-ac", "1",
        "-ar", "16000",
        "-c:a", "pcm_s16le",
        str(dest),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise AudioExtractionError(result.stderr.strip()[-2000:])
    return dest


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    out = extract_audio(Path(args.input), Path(args.output))
    print(out)
