---
name: bwc-evidence-processor
description: >
  Body-worn camera and audio/video evidence processor for defence teams.
  Extracts audio from MP4/MOV/MKV/WAV, transcribes with Whisper producing
  word-level timestamps, emits SRT/VTT subtitles, and builds a timestamped
  evidence matrix that cross-references transcript segments against
  configurable keyword banks (OPM clauses, Form 24 admissions, sworn-statement
  contradictions, QPP/Form 29 breach markers, PID/CO/WC matter identifiers).
  All generated output is labelled machine-generated, unverified and includes
  a mandatory human-verification column.
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
inputs:
  - path: local path to an MP4/MOV/MKV/WAV/MP3/M4A file
  - matter_config: optional path to a JSON file with matter-specific keywords
  - output_dir: directory to write transcript, SRT, and evidence matrix
outputs:
  - <basename>.srt - machine-generated subtitle track
  - <basename>.vtt - WebVTT subtitle track
  - <basename>.transcript.json - word-level timestamps
  - <basename>.evidence_matrix.csv - Scott-schedule-compatible matrix
  - <basename>.viewing_log.md - forensic viewing log
  - <basename>.contradictions.csv - conflicts with sworn-statement corpus
---

# BWC Evidence Processor

## Purpose

This skill assists defence teams preparing audio/video evidence for review.
It is NOT a certified transcription service. Every output file is stamped
`MACHINE-GENERATED - UNVERIFIED` and every row in the evidence matrix carries
an empty `human_verified` column that must be signed off by counsel or an
instructing solicitor before tender.

## When to use

Use this skill when:

- A user references body-worn camera footage, MP4/MOV evidence, or similar
- A user asks for subtitles, an SRT, or a transcript of an audio/video file
- A user asks for an evidence matrix, forensic viewing log, or contradiction
  register
- A user references sworn-statement cross-referencing against video/audio

Do NOT use this skill:

- For producing court-tendered certified transcripts (direct the user to a
  NAATI-accredited transcriber)
- When the source file cannot be verified as lawfully disclosed evidence

## How to run

The primary entry point is `scripts/process_video.py`:

```bash
python scripts/process_video.py \
    --input /path/to/evidence.mp4 \
    --output-dir /path/to/output \
    --matter-config keywords/matter_generic.json \
    --model small.en \
    --sworn-corpus /path/to/statements.txt
```

Arguments:

- `--input` (required): absolute path to the source media file
- `--output-dir` (required): directory for generated artefacts
- `--matter-config` (optional): matter-specific keyword bank JSON
- `--model` (optional): Whisper model size (`tiny.en`, `base.en`, `small.en`,
  `medium.en`, default `small.en`)
- `--sworn-corpus` (optional): plain-text file of sworn statements for
  contradiction analysis
- `--language` (optional): ISO language code, default `en`

## Dependencies

System:

- `ffmpeg` (for audio extraction)

Python (see `requirements.txt`):

- `faster-whisper>=1.0.0`
- `srt>=3.5.0`
- `webvtt-py>=0.5.0`
- `rapidfuzz>=3.9.0`

Install:

```bash
pip install -r requirements.txt
# Debian/Ubuntu:
sudo apt-get install -y ffmpeg
```

## Evidentiary caution

Whisper timestamp accuracy is typically within 200ms but can drift on long
silences or overlapping speech. Counsel must verify any passage intended for
cross-examination against the original media. The skill's output format makes
this explicit; do not strip the `MACHINE-GENERATED - UNVERIFIED` banner.

## Keyword banks

See `keywords/` for the configurable phrase banks. `matter_generic.json` is
the starter template; create per-matter copies (e.g. `matter_CO-25-2722.json`)
and pass via `--matter-config`. Never commit matter-specific files containing
client data to a shared repository.
