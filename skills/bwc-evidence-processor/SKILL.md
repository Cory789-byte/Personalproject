---
name: bwc-evidence-processor
description: >
  Deep forensic processor for body-worn camera and audio/video evidence,
  built for defence teams. Produces a full analytical stack per file:
  integrity and tamper flags, word-level transcripts, subtitles, evidence
  matrix against configurable keyword banks, contradictions register against
  sworn statement corpus, procedural compliance findings (cautions, rights,
  arrest grounds, search authority, post-invocation questioning, inducements,
  leading questions), bias and power-dynamics analysis (role inference,
  talk-time, interruption detection, aggressive/dehumanising/presumptive/
  confirmation-bias lexicon density, one-sided framing), and a master
  markdown report consolidating everything.

  Every artefact is labelled MACHINE-GENERATED - UNVERIFIED. The skill
  SURFACES concerns for counsel to verify; it does not make legal
  determinations.
triggers:
  - body-worn camera
  - BWC footage
  - subtitle generation
  - MP4 evidence
  - OneDrive evidence link
  - video evidence mapping
  - evidence matrix
  - forensic viewing log
  - transcript cross-reference
  - procedural compliance
  - abuse of process
  - police misconduct review
  - interrogation analysis
  - caution compliance
  - right to silence
  - use of force review
inputs:
  - input: local path to MP4 / MOV / MKV / WAV / MP3 / M4A / WebM
  - matter_config: optional JSON with matter-specific keywords and annexure map
  - sworn_corpus: optional plain-text sworn statement corpus for contradictions
  - ocr: optional flag to OCR burnt-in timestamps on keyframes
outputs:
  - <stem>.integrity.json    file hash, ffprobe metadata, scene cuts, anomalies
  - <stem>.transcript.json   word-level Whisper transcript
  - <stem>.srt / .vtt        machine-generated subtitle tracks
  - <stem>.evidence_matrix.csv
  - <stem>.viewing_log.md
  - <stem>.contradictions.csv
  - <stem>.compliance.csv    cautions, rights, arrest grounds, inducements
  - <stem>.bias.csv          per-segment bias/role/question metrics
  - <stem>.bias_summary.json aggregate bias + interruption list
  - <stem>.word_review.csv   one row per word with confidence + flags
  - <stem>.master_report.md  consolidated human-readable report
---

# BWC Evidence Processor

## Purpose

Defence-side analytical pipeline for police body-worn-camera footage and
related audio/video exhibits. It produces the artefacts a solicitor or
barrister needs to run a granular cross-examination: a certified-adjacent
transcript, a scene-cut / integrity report, per-utterance procedural-
compliance flags, a role-attributed bias analysis, and a word-by-word
review sheet with confidence scores.

This is NOT a court-certified transcript. Every artefact carries a
`MACHINE-GENERATED - UNVERIFIED` banner and a mandatory `human_verified`
column. Counsel must verify every flag against the underlying footage.

## When to use

- Review of BWC / in-car / station-camera / covert audio
- Drafting cross-examination on caution timing, arrest grounds, search
  authority, detention limits
- Identifying inducements (promises / threats), leading questions,
  questioning after invocation of rights
- Producing a Scott-schedule-compatible evidence matrix for a brief
- Detecting integrity anomalies in disclosed footage (container edits,
  re-encoding, unusual scene cuts, black/freeze intervals)

## When NOT to use

- Producing a court-tendered transcript (use a NAATI-accredited transcriber)
- Any matter where the source file is not a lawfully disclosed exhibit
- As the sole basis for any allegation of misconduct or abuse of process

## How to run

```bash
python scripts/process_video.py \
    --input /path/to/bwc.mp4 \
    --output-dir /path/to/out \
    --matter-config keywords/matter_generic.json \
    --sworn-corpus /path/to/sworn.txt \
    --model small.en \
    --ocr
```

Options:

- `--input` (required): local media path
- `--output-dir` (required): artefact destination
- `--matter-config` (optional): per-matter keyword bank JSON
- `--sworn-corpus` (optional): plain-text sworn statements for contradictions
- `--model` (optional): Whisper size — `tiny.en`, `base.en`, `small.en`,
  `medium.en`, `large-v3` (default `small.en`)
- `--language` (optional): ISO language code, default `en`
- `--device` (optional): `cpu`, `cuda`, `auto` (default `auto`)
- `--ocr`: enable OCR of burnt-in timestamps on keyframes (needs tesseract)
- `--skip-integrity`, `--skip-transcription`: skip stages
- `--transcript`: reuse an existing transcript JSON

## Dependencies

System:

- `ffmpeg`, `ffprobe` (required)
- `tesseract` (optional — only for OCR)

Python:

- `faster-whisper>=1.0.0`
- `rapidfuzz>=3.9.0`
- `pytesseract` and `Pillow` (optional, for `--ocr`)

## Analytical modules

| Module | Produces |
|--------|----------|
| `frame_analysis.py` | hash, ffprobe metadata, scene cuts, black/freeze intervals, anomaly flags, optional keyframe OCR |
| `extract_audio.py` | 16 kHz mono WAV via ffmpeg |
| `transcribe.py` | word-level Whisper transcript JSON |
| `generate_srt.py` | SRT + WebVTT subtitle files |
| `evidence_map.py` | evidence matrix, contradictions register, viewing log |
| `procedural_compliance.py` | missing/late caution, right-to-counsel, post-invocation questioning, arrest without grounds, search without warrant/consent, inducements, leading questions |
| `bias_analysis.py` | role inference, talk-time, Q/A ratio, aggressive/dehumanising/presumptive/confirmation-bias/one-sided lexicon hits, interruption detection |
| `word_review.py` | one-row-per-word CSV with confidence, gap, flagged categories |
| `master_report.py` | consolidated markdown master report |

## Forensic hygiene

- All outputs: `MACHINE-GENERATED - UNVERIFIED`
- Every CSV: `human_verified` column (empty by default)
- Speaker role inference is heuristic — verify against footage
- Whisper timestamps drift on overlapping speech and long silences — verify
  any passage intended for cross-examination
- `integrity.json` SHA-256 must be compared against the hash on the
  disclosure receipt to confirm chain of custody

## Matter configuration

Never commit a matter file containing client identifiers to a shared repo.
`.gitignore` blocks `matter_*.json` except `matter_generic.json` and
`matter_template.json`. Create per-matter files locally.
