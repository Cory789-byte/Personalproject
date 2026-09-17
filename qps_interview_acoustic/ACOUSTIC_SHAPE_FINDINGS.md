# WHAT THE ACOUSTIC SHAPE SHOWS — Bickery record-of-interview

**File** `Exhibit__1_BICKERY_BWCF_-_SHEPHERD_interview_at_SOUWH.wav` · 1 h 06 m 16 s
**SHA-256** `f832c3af5eecd356ec82d07ed3a9ce91febe1451c3c4d0c11d10c9c41ec0923e`

> ⚠ **MACHINE-GENERATED — UNVERIFIED.** No transcript was available: there are
> **no words** in this analysis. Speaker labels C0/C1 are unsupervised acoustic
> clusters, not named people. Surfaces measurements for counsel to verify.

## 1. Event structure

| | |
|---|---|
| Speech | 50.5 min of 66.3 min (76%) |
| Turns | 302 (146 C0 / 156 C1) · 240 turn changes |
| Longest single turn | **157.8 s — C0, at 08:41.5 → 11:19.3** |
| Silences ≥10 s | 11, of which **9 fall in the first 8 minutes** |
| Longest silence | 26.78 s, before 03:46.8 |

The first ~8 minutes are sparse and punctuated by 10–27 s silences, then a
158-second uninterrupted turn by C0 at the 9-minute mark, after which the
exchange becomes continuous. That is the shape of set-up, then a formal
scripted passage, then questioning.

## 2. Two parties, and which is which

| | C0 | C1 |
|---|---|---|
| Turns | 146 | 156 |
| Mean turn | **13.67 s** | 7.81 s |
| Median turn | 9.00 s | **4.84 s** |
| Longest turn | 157.8 s | 66.1 s |
| Talk time | **33.3 min (62.8%)** | 20.3 min (37.2%) |
| f0 median | 131.2 Hz | 98.8 Hz |
| f0 sd within cluster | 18.6 Hz | 15.8 Hz |
| dB median | 62.6 | 64.5 |

**Response latency**

| Transition | n | median | latched (<0.3 s) |
|---|---|---|---|
| C0 → C1 | 120 | **0.94 s** | 12% |
| C1 → C0 | 117 | **0.63 s** | **20%** |

⇒ Near-equal turn *counts* but C0 holds the floor **1.6× longer**; C0 comes
back faster and latches more often; C1 answers in short turns and takes
half a second longer to begin.

**Inference (not established):** C0 is the interviewing party, C1 the person
interviewed. Supporting this: the 157.8 s scripted-length monologue at the
9-minute mark belongs to C0; the latency asymmetry is the standard
questioner/respondent pattern; and C0's wider within-cluster f0 spread is
consistent with **two officers merged into one cluster** (a third speaker did
not resolve — silhouette falls from +0.197 at k=2 to +0.168 at k=3).

**Breaking silence.** After gaps ≥5 s, C1 resumes **26** times against C0's
**10** — and 16 of those are C1 resuming after C1's own pause.

## 3. The one strong trend

**C1's speaking level declines across the hour. C0's does not.**

Artefact-free speech only (f0 70–200 Hz, voiced fraction ≥0.25, beep-overlapping
segments removed — 616 of 766 segments):

| Speaker | slope | total | r | p |
|---|---|---|---|---|
| C0 | +0.16 dB/10 min | +1.1 dB | +0.085 | 0.12 (ns) |
| **C1** | **−0.71 dB/10 min** | **−4.6 dB** | **−0.437** | **1.8 × 10⁻¹⁴** |

C1 by block: 66.5 → 65.0 → 64.2 → 65.2 → 63.3 → 63.4 → **60.8 dB**.
Survives dropping the first and last ten minutes (−0.49 dB/10 min, p = 6.5 × 10⁻⁴).

**C1's pitch does not rise** — 96–104 Hz across every block, a total spread of
1.3 semitones. Falling level with flat pitch is **not** arousal; arousal raises
both together.

⚠ **Two explanations fit equally and the audio cannot separate them:**
1. **Behavioural** — declining vocal effort over an hour.
2. **Geometric** — this is a body-worn camera. The wearer's level is fixed
   relative to their own microphone; everyone else's varies with distance and
   angle. C0 being flat while C1 declines is *exactly* what a wearer-versus-
   other-party geometry produces if the parties' relative position drifted.

Any claim that the interviewee became withdrawn must confront explanation 2.

## 4. Corrections made during analysis

* The loudest segment in the file (**79.6 dB at 48:28.6**) is **the 177 Hz grid
  beep**, not a person. Excluded.
* Segments reading f0 **258–432 Hz** (+15 to +25 st above a male baseline) are
  **not raised voices**. Spectral testing gives peaks at **706–730 Hz with
  tone-like flatness (0.02–0.09)**, i.e. a second device tone, and noise
  transients — Praat pitch-tracking errors, not speech.
* ⇒ **There is no acoustic evidence of shouting, raised voice or distress
  vocalisation anywhere in this recording.**

## 5. A second, unidentified tone

Distinct from the 120 s grid beep: a **~706–730 Hz** tonal event at **04:10.1,
48:04.8 and 48:12.4**. Origin unknown. Not periodic on any grid found.

## 6. What cannot be known from this file

* **Which cluster is which person.** Needs participant confirmation or a
  reference sample of a known voice.
* **Whether C0 is one officer or two.**
* **Any content.** No transcript, so no words, no speech rate, no question
  forms, no caution wording, no compliance analysis.
* Whether the level decline is behavioural or positional (§3).

---

## 7. Semitone measures (added 17 Sep 2026) — and a correction to the range metric

**Semitone** = logarithmic pitch interval. `st = 12 × log₂(f₂/f₁)`; 12 st = one
octave. Used because equal Hz steps are not equal perceptual steps: +20 Hz from
100 Hz is 3.2 st, the same +20 Hz from 300 Hz is 1.1 st. All level figures below
are measured against **that speaker's own median**, never across speakers.

### ⚠ Correction — `f0_range_st`

The first run defined the range as **min-to-max of the raw pitch track**. That is
extremely outlier-sensitive: a single octave-tracking error or one creaky frame
inflates it by an octave or more. It reported medians of **21.59 st (C0)** and
**20.40 st (C1)** — nearly two octaves within one phrase, which is not real speech.

`prosody.py` now reports a **robust 5th–95th percentile span** as `f0_range_st`
and retains the raw extremes as `f0_range_raw_st` / `f0_min_raw` / `f0_max_raw`.

| | robust p5–p95 | raw min–max (discarded) |
|---|---|---|
| C0 | **10.39 st** (IQR 7.10–13.31) | 21.59 st |
| C1 | **10.28 st** (IQR 4.73–14.71) | 20.40 st |

⚠ **Cross-recording comparison is NOT currently safe.** The WC/2024/227 mention
figures (Dwyer 7.61 st, Shepherd 5.24 st) came from a different pipeline whose
range definition is unverified. The mention audio must be re-run through this
code before the two are compared.

### Findings

**Voice separation.** C0 131.3 Hz, C1 98.7 Hz — **4.94 semitones apart**.

**Within-phrase movement is the same for both.** C0 10.39 st vs C1 10.28 st,
difference +0.11 st, Mann-Whitney **p = 0.23 (not significant)**. Expressiveness
does not distinguish these speakers.

**C1 has almost no downward pitch range.**

| | ≥ +2 st above own baseline | ≤ −2 st below | ratio | p5 |
|---|---|---|---|---|
| C0 | 16.0% | 13.9% | **1.1 : 1** | −3.13 st |
| **C1** | 16.8% | **1.1%** | **15.7 : 1** | **−1.51 st** |

Both lift above baseline equally often; only C0 descends below it. C1 speaks from
the **floor of his own range** throughout. Two readings fit: a genuinely held-low
delivery, or modal-register floor with creak below it being filtered out as
unvoiced. Both describe a low, held voice.

**Pitch range does not narrow over the hour.** C0 −0.15 st/10 min (p = 0.34);
C1 −0.02 st/10 min (p = 0.94). Both flat.

⇒ C1's **4.6 dB intensity decline** (p = 1.8 × 10⁻¹⁴) occurs **without any loss of
pitch modulation**. Quieter, but not flatter. That is a different state from
monotone withdrawal — subject always to the body-worn-camera geometry
alternative recorded at §3.
