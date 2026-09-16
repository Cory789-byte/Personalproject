# WC/2024/227 — MENTION OF 7 AUGUST 2026 — TRANSCRIPT FILE SET

**There is exactly one transcript.** Everything else here is the provenance and verification
behind it. Nothing in this directory duplicates anything else.

| File | What it is | Keep? |
|---|---|---|
| **`TRANSCRIPT_diarised_prosody.md`** | ⭐ **THE TRANSCRIPT.** The single canonical record. Amendment log (A1, A2), full diarised text with prosody, and reader's notes N1–N4 behind a hard rule | **Yes — this is the artefact** |
| `TRANSCRIPT_diarised_prosody.pdf` | Rendered copy of the above, for reading and sending | Yes — regenerate whenever the .md changes |
| `MENTION_7AUG2026_segments.jsonl` | 1,068 Whisper segments with **per-word probabilities**. The evidence behind every confidence claim | **Yes — delete this and no confidence figure is checkable** |
| `WORD_CONFIDENCE_AUDIT.md` | Word-level confidence analysis and the re-decode results | Yes |
| `REDECODE_six_windows_report.json` | Raw output of the six-window re-decode, both passes, per-word | Yes — the raw evidence |
| `DIARISATION_ecapa_clusters.json` | Cluster labels from all five clustering methods | Yes — makes the 93.8% checkable |
| `DIARISATION_ecapa_segment_index.json` | Maps cluster rows → segment indices | Yes — needed to read the above |
| `diarise_inferential.py` | The **original** diarisation method (Resemblyzer + Viterbi) | Yes — reproduces the labels in the transcript |
| `diarise_ecapa.py` | The **independent** ECAPA-TDNN diarisation | Yes — reproduces the 93.8% corroboration |
| `redecode_disputed.py` | Targeted re-decode of the disputed windows | Yes — reproduces N1–N4 |

## What is NOT here

- ⛔ **The audio.** `PRF0466309_20260807_QIRC-OIR_Brisbane…mp3`, 31,007,232 bytes,
  md5 `b4f1e1fd31d24d18e4d22fba388e00e0`, 3,875.9 s. **Deliberately not committed** — it is a
  recording of a proceeding and is not carried in git history. It lives in the owner's own storage.
- ⛔ **The superseded small.en transcript.** Not in this repository and not to be reintroduced; its
  rendering of [16:29] is wrong (see reader's note N1).
- ⛔ **A certified transcript.** **None exists.** Request ATR0282381 to QTranscripts was for **audio
  only**; the notification of 18 August 2026 is a request record, not a transcript.

## Status of the record, as at 16 September 2026

- **Two amendments.** A1 (correction, participant-confirmed, **independently corroborated** by ECAPA)
  and A2 (confirmation, participant-confirmed, used as the ground-truth calibration point).
- **Six windows re-decoded from the audio** at beam 10, two passes each. Four confirmations;
  two words removed as never spoken (*"Absolutely."*, *"Yeah,"*); one operator hypothesis refuted.
- **Independently re-diarised.** ECAPA-TDNN agrees with the transcript on **93.8%** of 1,018 embedded
  segments.
- ⛔ **Still uncertified machine output.** Order the certified transcript before quoting externally.
