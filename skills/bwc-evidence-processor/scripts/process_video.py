"""End-to-end orchestrator: media file -> transcript, SRT/VTT, evidence matrix."""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "BWC Evidence Processor - machine-generated, unverified. "
            "Counsel must verify outputs before tender."
        )
    )
    parser.add_argument("--input", required=True, help="Path to media file")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--matter-config", default=None)
    parser.add_argument("--sworn-corpus", default=None)
    parser.add_argument("--model", default="small.en")
    parser.add_argument("--language", default="en")
    parser.add_argument("--device", default="auto")
    args = parser.parse_args()

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from extract_audio import extract_audio
    from transcribe import transcribe, save_transcript_json
    from generate_srt import write_srt, write_vtt
    from evidence_map import (
        KeywordBank,
        build_contradictions,
        build_evidence_matrix,
        build_viewing_log,
    )

    source = Path(args.input).expanduser().resolve()
    out_dir = Path(args.output_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = source.stem

    print(f"[1/5] Extracting audio from {source.name}")
    with tempfile.TemporaryDirectory() as tmp:
        wav = extract_audio(source, Path(tmp) / f"{stem}.wav")

        print(f"[2/5] Transcribing with Whisper model {args.model}")
        segments = transcribe(wav, args.model, args.language, args.device)
        transcript = out_dir / f"{stem}.transcript.json"
        save_transcript_json(segments, transcript)

    print("[3/5] Rendering SRT and VTT")
    write_srt(transcript, out_dir / f"{stem}.srt")
    write_vtt(transcript, out_dir / f"{stem}.vtt")

    print("[4/5] Building evidence matrix and viewing log")
    bank = KeywordBank.load(
        Path(args.matter_config) if args.matter_config else None
    )
    build_evidence_matrix(transcript, bank, out_dir / f"{stem}.evidence_matrix.csv")
    build_viewing_log(transcript, out_dir / f"{stem}.viewing_log.md", source.name)

    print("[5/5] Building contradictions register")
    build_contradictions(
        transcript,
        Path(args.sworn_corpus) if args.sworn_corpus else None,
        out_dir / f"{stem}.contradictions.csv",
    )

    print(f"\nDone. Artefacts written to {out_dir}")
    print("REMINDER: All outputs are MACHINE-GENERATED - UNVERIFIED.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
