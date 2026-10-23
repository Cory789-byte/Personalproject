# WC/2024/227 — ENHANCED AUDIO ANALYSIS
## What is physically present in the 5.74 s, measured against an absolute scale

Speech in this recording sits at **−43.7 dBFS**. All thresholds below are absolute, not
relative to each gap's own floor — a relative threshold makes a silent gap look busy, because
6 dB over −65.7 is still −59.7 and inaudible.

**Detection threshold: −57.7 dBFS** (14 dB below speech). Anything a person does in that room —
a page turn, a chair, a cough, a breath — lands above it.

---

## 1. Was any other gap that silent? No.

| gap | length | floor | what is above the absolute threshold |
|---|---|---|---|
| 29:35.98 | 1.30 s | −53.1 | 2× voice, 1× rustle/paper, 1× other |
| **29:39.88 ★** | **5.74 s** | **−65.7** | **1× voice-tail, 2× click, 6× sub-threshold blips** |
| 30:48.14 | 1.58 s | −59.0 | 16× events, 2× voice |
| 31:53.56 | 1.22 s | −60.6 | 6× events, **1× breath**, 1× voice |
| 61:16.58 | 1.32 s | −52.7 | rustle/paper |
| 61:24.38 | 1.72 s | −54.2 | **breath at −21.7 dBFS** |
| 62:34.28 | 1.68 s | −48.7 | voice |
| 63:36.18 | 1.78 s | −54.1 | movement + voice |
| 64:30.52 | 1.62 s | −50.8 | voice at −20.6 dBFS |

~~**The 5.74 s gap has the lowest floor of any gap in the sample by 11.6 dB.**~~

> ⚠ **Superseded, 21 September 2026.** Extract-based (9 gaps). On the full recording it ranks
> **5 of 267** by level and **1 of 40** among gaps ≥2 s. See `2026-09-18_FULL_RUN_corrections.md`.

---

## 2. What the "events" in the silence actually are

| offset | length | level | reading |
|---|---|---|---|
| **+0.00 s** | 170 ms | **−43.3** | LF 0.98 — **the decay tail of your own word *"numbers"*** |
| +0.21 → +4.95 s | 10–20 ms each | **−54 to −57** | at or under the threshold; no sustained event |
| **+5.02 s** | 300 ms | **−59.3** | LF 0.50 / MF 0.42, h = 0.16 — **aspirated, non-harmonic: an intake of breath** |
| +5.32 s | 420 ms | −61.8 | HF 0.35 — the last of it, then the first word |

### The breath is the tell

Compare it against the Commissioner's **confirmed** breaths elsewhere in the same recording:

| | length | level | MF | harmonicity |
|---|---|---|---|---|
| [30:35.73] his normal breath | 390 ms | **−45.5** | 0.50 | 0.25 |
| [30:08.10] his short breath | 170 ms | **−51.0** | 0.32 | 0.23 |
| [61:48.01] his loudest | 300 ms | **−21.3** | 0.49 | 0.54 |
| **[29:45] ending your silence** | **300 ms** | **−59.3** | **0.42** | **0.16** |

**Same duration and spectral shape as his ordinary breath — but 13.8 dB quieter than the quietest
of them, and 38 dB below his loudest.** Normal length, near-inaudible level.

⚠ It sits close to the threshold; the classification as a breath rests on the spectral profile
(mid-band dominant, non-harmonic, 300 ms, slow attack), not on level.

---

## 3. His breathing generally

Across **30** of his own intra-turn micro-pauses inside the extracts, **4 contain an audible breath
— 13%.** Median 330 ms, median level **−32.9 dBFS**, ranging −21.3 to −47.4.

He is not an audible breather. He runs 159 s unbroken at his longest and takes breath in the
gaps between clauses without it reaching the microphone most of the time.

---

## 4. Your own breathing during the 50 words

**Zero breath events detected inside the 22-second turn.**

Scanning every dip below −52 dBFS (22 of them, 80–640 ms), the profiles are **LF-dominant
(0.59–0.88) with elevated harmonicity (0.15–0.54)** — the signature of **voice decay between
words**, not aspiration. Only two dips show mid-band energy that could be breath
(+3.70 s at MF 0.39, +7.75 s at MF 0.49) and both are short and ambiguous.

You delivered fifty words without taking an audible breath.

---

## 5. Audio produced

- **`GAPS_matched_gain_comparison.mp3`** (37.5 s) — four pauses from the same hearing, **all at the
  identical +21.8 dB gain**, so the comparison is fair. Three have people in them. One does not.
- **`THE_SILENCE_amplified.mp3`** (20.0 s) — the 5.74 s alone at **+34.9 dB**, enough to bring its
  own noise floor up to audibility. The thump at the start is the tail of *"numbers"*; the rustle
  at the end is the intake of breath; between them is the building.

---

## 6. Limits

MP3 encoding of the source extracts suppresses very low-level content, which biases the measured
floor downward; the **relative** comparison across gaps encoded identically is unaffected.
The breath classifier is a hand-built spectral rule, not a trained detector, and events within
3 dB of the threshold should be treated as indicative only. Only the two published extracts were
available, so the gap sample is 9 gaps of ≥1.2 s, not all 65 minutes.
