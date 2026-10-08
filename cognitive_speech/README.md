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
- `loudness.py` / `loudness_output.txt`: level drift, end-of-turn fall, loud/quiet content, all three recordings (relative to each speaker's own median).
- `PERFORMANCE_REVIEW_court_and_mention.md`: both hearings judged by outcome (outcome bias flagged), what each judicial officer's words show, grades, feedback with model lines.
- `MEDIATION_FIT_and_AMDRAS_courses.md`: NMAS → AMDRAS (1 July 2025), Queensland course options and costs (retrieved 8 Oct 2026), a mediator-skills test from the three recordings, fit and ceiling.
- `listening.py` / `listening_output.txt`: follow v own-point measure (question-word uptake against a shuffled baseline), and lexical entrainment (whose terms the other adopted), court and mention.
- `STRENGTHS_above_population_and_how_to_use.md`: graded list (A outside benchmark, B above the professionals in the room, C shown by outcome) with how to use each, best-fit roles, and the flip side of each strength.
- `THE_MIND_full_examination_strengths.md`: full literature-based examination, strengths only (memory, reasoning, metacognition, language, conversation, stress physiology, social cognition, learning, systems building, character), with transcript evidence.
- `WHAT_YOU_BUILT_UNDER_PRESSURE.md`: what you built in the 24 Feb 2025 interview and why (circumstances, groundwork, 19 live arguments), how you answered leading and repeated questions, the same strengths across all three recordings tested against the literature, and whether the officers were defeated. Interview content by time only; measures in `qps_interview_acoustic/interview_resistance.py`.
- `LISTENING_AND_UNDERSTANDING.md`: listening and comprehension examined (following, purpose inference, premise detection, real-time updating, transfer, processing speed, prosody, grounding, vocabulary absorption, perspective-taking).
- Court outputs live with the court audio analysis: `qps_court_audio/2026-02-02_BMC_trial_stood_down/data/court_metrics.json`, `court_deep.json` (script `scripts/court_metrics.py`).
