# Speech measures: C. Shepherd (self-analysis)

Not case material. Not a clinical or forensic assessment. Never served, tendered, cited or attached in
WC/2024/227, the QPS matters or any other proceeding (discipline rule 10: the QPS interview never crosses
into the WC track). Descriptive speech measures only, from machine transcripts.

- `speech_metrics.py`: rate, pauses, fillers, lexical variety, connectives, hedges, per speaker.
- `deep_analysis.py`: response timing, situational awareness, arousal (pitch/loudness vs own baseline), recall markers.
- `build_interview_segs.py`: joins the interview transcript to the existing diarised acoustic segments.
- `mention_*.json`: outputs for the 7 Aug 2026 mention.
- `COMPARISON_three_recordings.md`: interview (Feb 2025), court (Feb 2026, spoken, not read) and mention (Aug 2026), like for like; traits, changes, literature, rules.
- `steady_voice.py` / `steady_voice_output.txt`: pitch–loudness coupling, within-phrase pitch movement and range per speaker, all three recordings.
- `formulation.py` / `formulation_output.txt`: contrast, reasons, negation, pronouns, openers and repetition per speaker (court and mention).
- Court outputs live with the court audio analysis: `qps_court_audio/2026-02-02_BMC_trial_stood_down/data/court_metrics.json`, `court_deep.json` (script `scripts/court_metrics.py`).
