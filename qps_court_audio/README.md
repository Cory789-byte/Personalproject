# QPS track: court audio analyses

> ⛔ **QPS track / personal file only.** Nothing here is voiced, cited or attached in WC/2024/227 or the
> employment track (discipline rule 10). Machine-generated and unverified; private analysis only.
> Court audio files are **never committed**: they are recordings of proceedings and stay in the owner's storage.

| Folder | Hearing | Contents |
|---|---|---|
| `2026-02-02_BMC_trial_stood_down/` | Brisbane Magistrates Court, 2 Feb 2026, QPS prosecution; trial stood down | `TRANSCRIPT_diarised_prosody.md` (diarised, prosody-marked, amendment log), `ANALYSIS.md` (what was said, structure, voices, comparison with the 2025 interview and the 2026 mention, §5 spoken not read), `data/` (incl. `court_metrics.json`, `court_deep.json`), `scripts/` (incl. `court_metrics.py`) |

Method matches the 7 Aug 2026 mention and the QPS interview: faster-whisper large-v3 with per-word
probabilities; ECAPA-TDNN speaker clustering; Praat (parselmouth) pitch and intensity per segment;
markers relative to each speaker's own medians. Re-run from `scripts/` with the audio file path.
