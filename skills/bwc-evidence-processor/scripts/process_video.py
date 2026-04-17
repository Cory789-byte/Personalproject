"""End-to-end orchestrator for BWC evidence processing.

Pipeline:
  1. File integrity (SHA-256, ffprobe, scene cuts, black/freeze frames,
     optional OCR of burnt-in timestamps)
  2. Audio extraction (ffmpeg -> 16 kHz mono WAV)
  3. Transcription (faster-whisper, word-level timestamps)
  4. Subtitle rendering (SRT + VTT)
  5. Evidence matrix against configurable keyword banks
  6. Forensic viewing log
  7. Contradictions register against sworn corpus
  8. Procedural compliance findings (cautions, rights, arrest grounds, etc.)
  9. Bias / power-dynamics analysis + interruption detection
 10. Word-by-word review CSV
 11. Master markdown report consolidating everything

Every artefact is labelled MACHINE-GENERATED - UNVERIFIED. The orchestrator
skips stages that require unavailable tools and reports what was skipped.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
import traceback
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "BWC Evidence Processor - machine-generated, unverified. "
            "Counsel must verify outputs before tender."
        )
    )
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--matter-config", default=None)
    parser.add_argument("--sworn-corpus", default=None)
    parser.add_argument("--model", default="small.en")
    parser.add_argument("--language", default="en")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--ocr", action="store_true",
                        help="OCR burnt-in timestamps on extracted keyframes")
    parser.add_argument("--skip-integrity", action="store_true")
    parser.add_argument("--skip-transcription", action="store_true")
    parser.add_argument("--transcript", default=None,
                        help="Use an existing transcript JSON and skip stages 1-3")
    args = parser.parse_args()

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from generate_srt import write_srt, write_vtt
    from evidence_map import (
        KeywordBank, build_contradictions, build_evidence_matrix,
        build_viewing_log,
    )
    from procedural_compliance import check as compliance_check, save_findings
    from bias_analysis import score_segments, save_bias_csv, save_bias_summary
    from word_review import build as build_word_review
    from master_report import render as render_master

    source = Path(args.input).expanduser().resolve()
    out_dir = Path(args.output_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = source.stem
    transcript_path = out_dir / f"{stem}.transcript.json"
    skipped: list[str] = []

    if args.transcript:
        transcript_path = Path(args.transcript).resolve()
        print(f"[=] Using existing transcript {transcript_path}")
    else:
        if not args.skip_integrity:
            print("[1] Integrity report")
            try:
                from frame_analysis import run_integrity, save_integrity
                frames_dir = out_dir / f"{stem}_frames" if args.ocr else None
                rep = run_integrity(source, frames_dir, args.ocr)
                save_integrity(rep, out_dir / f"{stem}.integrity.json")
            except Exception as e:
                skipped.append(f"integrity: {e}")
                traceback.print_exc()

        if not args.skip_transcription:
            print("[2] Extracting audio")
            try:
                from extract_audio import extract_audio
                from transcribe import transcribe, save_transcript_json
                with tempfile.TemporaryDirectory() as tmp:
                    wav = extract_audio(source, Path(tmp) / f"{stem}.wav")
                    print(f"[3] Transcribing ({args.model})")
                    segs = transcribe(wav, args.model, args.language, args.device)
                    save_transcript_json(segs, transcript_path)
            except Exception as e:
                skipped.append(f"transcription: {e}")
                traceback.print_exc()

    if not transcript_path.is_file():
        print("No transcript available - skipping transcript-dependent stages.")
        print("Skipped:", skipped)
        return 1

    print("[4] Rendering subtitles")
    write_srt(transcript_path, out_dir / f"{stem}.srt")
    write_vtt(transcript_path, out_dir / f"{stem}.vtt")

    print("[5] Evidence matrix")
    bank = KeywordBank.load(Path(args.matter_config) if args.matter_config else None)
    build_evidence_matrix(transcript_path, bank, out_dir / f"{stem}.evidence_matrix.csv")

    print("[6] Viewing log")
    build_viewing_log(transcript_path, out_dir / f"{stem}.viewing_log.md", source.name)

    print("[7] Contradictions register")
    build_contradictions(
        transcript_path,
        Path(args.sworn_corpus) if args.sworn_corpus else None,
        out_dir / f"{stem}.contradictions.csv",
    )

    print("[8] Procedural compliance")
    import json
    data = json.loads(transcript_path.read_text(encoding="utf-8"))
    findings = compliance_check(data["segments"])
    save_findings(findings, out_dir / f"{stem}.compliance.csv")

    print("[9] Bias analysis")
    scored = score_segments(data["segments"])
    save_bias_csv(scored, out_dir / f"{stem}.bias.csv")
    save_bias_summary(scored, out_dir / f"{stem}.bias_summary.json")

    print("[10] Word-by-word review")
    build_word_review(transcript_path, out_dir / f"{stem}.word_review.csv")

    print("[11] Master report")
    render_master(out_dir, stem, source.name)

    print(f"\nDone. Artefacts in {out_dir}")
    if skipped:
        print("Skipped stages:")
        for s in skipped:
            print(f"  - {s}")
    print("REMINDER: All outputs are MACHINE-GENERATED - UNVERIFIED.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
