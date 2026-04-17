"""Transcribe an audio file using faster-whisper with word-level timestamps."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class Word:
    start: float
    end: float
    text: str
    probability: float


@dataclass
class Segment:
    index: int
    start: float
    end: float
    text: str
    words: list[Word]


def transcribe(
    audio_path: Path,
    model_size: str = "small.en",
    language: str = "en",
    device: str = "auto",
) -> list[Segment]:
    from faster_whisper import WhisperModel

    compute_type = "int8" if device in ("cpu", "auto") else "float16"
    model = WhisperModel(model_size, device=device, compute_type=compute_type)

    raw_segments, _info = model.transcribe(
        str(audio_path),
        language=language,
        word_timestamps=True,
        vad_filter=True,
        beam_size=5,
    )

    segments: list[Segment] = []
    for i, seg in enumerate(raw_segments):
        words = [
            Word(
                start=float(w.start),
                end=float(w.end),
                text=w.word,
                probability=float(getattr(w, "probability", 0.0)),
            )
            for w in (seg.words or [])
        ]
        segments.append(
            Segment(
                index=i,
                start=float(seg.start),
                end=float(seg.end),
                text=seg.text.strip(),
                words=words,
            )
        )
    return segments


def save_transcript_json(segments: Iterable[Segment], dest: Path) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "header": "MACHINE-GENERATED - UNVERIFIED",
        "segments": [asdict(s) for s in segments],
    }
    dest.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    return dest


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model", default="small.en")
    parser.add_argument("--language", default="en")
    args = parser.parse_args()

    segs = transcribe(Path(args.input), args.model, args.language)
    save_transcript_json(segs, Path(args.output))
    print(f"{len(segs)} segments written to {args.output}")
