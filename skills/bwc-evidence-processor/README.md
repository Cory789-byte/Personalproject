# bwc-evidence-processor

Claude Code skill for defence-side body-worn-camera and audio/video evidence
processing. See `SKILL.md` for activation triggers and full usage.

## Install

```bash
pip install -r requirements.txt
sudo apt-get install -y ffmpeg   # Debian/Ubuntu
```

To register as a user skill in Claude Code, copy this directory to
`/mnt/skills/user/bwc-evidence-processor/` (web) or the equivalent user-skills
directory for your Claude Code installation.

## Run

```bash
python scripts/process_video.py \
    --input  /path/to/bwc.mp4 \
    --output-dir /path/to/out \
    --matter-config keywords/matter_generic.json \
    --model small.en
```

Artefacts produced in the output directory:

| File | Purpose |
|------|---------|
| `<name>.transcript.json` | Word-level timestamps, JSON |
| `<name>.srt` | SRT subtitle track (machine-generated) |
| `<name>.vtt` | WebVTT subtitle track |
| `<name>.evidence_matrix.csv` | Scott-schedule-compatible matrix |
| `<name>.viewing_log.md` | Forensic viewing log |
| `<name>.contradictions.csv` | Partial-match divergences vs. sworn corpus |

## Tests

Offline tests that do not require ffmpeg or Whisper:

```bash
python -m unittest discover -s tests
```

## Evidentiary status

Every artefact carries a `MACHINE-GENERATED - UNVERIFIED` banner. The skill
is an aide-mémoire, not a certified transcript. Counsel must verify any
passage before tender.

## OneDrive / SharePoint sources

This skill operates on local files only. For SharePoint-hosted evidence,
download the file via the Microsoft 365 connector in a live Claude Code
session and pass the local path to `--input`.
