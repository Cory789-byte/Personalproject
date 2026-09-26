# ECAPA diarisation + Praat prosody — pipeline

Adds the two layers the rest of this skill does not have: **who spoke**
(acoustic, not lexical) and **how they spoke** (f0, intensity, rate, pauses).

Same method as the WC/2024/227 mention run, so outputs of the two matters
are directly comparable. Field names match `MENTION_7AUG2026_segments.jsonl`.

## Shortcut: reuse an existing transcript

Whisper is **not** re-run. `load_segments.py` takes a transcript you already
have — Whisper/faster-whisper JSON, this skill's `<stem>.transcript.json`,
or a `.srt` — and normalises it to `segments.jsonl`. Everything downstream
works from those segment boundaries.

## Run

```bash
S=skills/bwc-evidence-processor/scripts

# 1. existing transcript -> segments
python3 $S/load_segments.py interview.srt segments.jsonl

# 2. Praat prosody per segment  (~1-2 min per audio hour)
python3 $S/prosody.py interview.wav segments.jsonl segments.pros.jsonl

# 3. ECAPA-TDNN diarisation  (~10-15 min per audio hour, CPU)
python3 $S/diarise_ecapa.py interview.wav segments.jsonl diar --speakers 2 3 4

# 4. merged transcript
python3 $S/build_diarised_prosody.py segments.pros.jsonl diar OUT.md \
    --variant k3_cmn_ward --names "SPK0=BICKERY,SPK1=DAVIES,SPK2=SHEPHERD"
```

`prosody.py` accepts `--start/--end` so a long file can be processed in
windows and the outputs concatenated.

## Method notes

* **Embeddings** SpeechBrain `spkrec-ecapa-voxceleb`, 192-dim, CPU.
* **Channel compensation** global mean subtracted, then length-normalised.
  Without this, clustering separates *recording conditions*, not speakers.
* **Several clusterings are reported side by side** (agglomerative on raw
  and compensated embeddings, Ward, k-means, spectral) at each requested
  speaker count. Agreement across variants is the evidence that a partition
  is real; a split only one variant finds is not.
* **Segments under `--min-dur` (default 0.60 s) are not embedded.** Short
  interjections inside another speaker's turn are the weakest case for
  automated attribution and are left unassigned rather than guessed.
* **Prosodic markers are speaker-relative**, computed against that
  speaker's own median f0 and own quartiles for range, rate and intensity.
  Absolute Hz and dB never compare across speakers — different voices,
  different microphones, different distances to the microphone.

## Limits — read before relying on any of it

* Speaker labels are **machine inference, not participant evidence**. A
  person who was in the room correcting a label outranks the model.
* Prosody computed on a **transcode** is analysis, not evidence; the
  original recording remains primary. Prefer lossless (WAV/FLAC) input.
* Intensity in dB is **not calibrated** to any absolute level. It supports
  within-speaker comparison in one recording and nothing else.
* Diarisation degrades on overlapping speech; overlaps commonly land in
  whichever speaker dominates the segment.

Verified end to end on synthetic two-speaker audio: Praat recovered the
synthesised f0 to 0.2 Hz (115.1/195.2 against 115/195) and all four
clustering variants recovered the true speaker split exactly.
