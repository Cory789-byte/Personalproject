# WC/2024/227 — "THE ROOM WENT QUIET"

> ## ⚠⚠ SUPERSEDED IN PART — 18 September 2026
> This file was built on **9.3 minutes of published extract**. The full 64.6-minute audio has since
> been analysed and **two of its headline claims are retracted**:
> - §7's "the ten quietest seconds of the entire recording are all inside this one" is **FALSE**.
>   None of them is. The ten quietest seconds are at 16:36, 33:33, 19:15, 18:32, 27:17 and 25:26.
> - §1's "rank 1 of 29 gaps, 22.2 dB below the median, 10.4 dB below the next quietest" is **WRONG**.
>   On all 267 gaps it ranks **5**, at −63.5 dBFS against a median of −49.0 (a 14.5 dB difference),
>   and the next quietest gap is −64.2 dBFS.
>
> **What survives** is §5's narrower claim, now properly grounded: among the **40 gaps of 2 s or
> more the silence ranks 1 of 40 by level**; every longer gap is 6–13 dB noisier and every quieter
> gap is under 1.4 s. The room reaches that floor elsewhere — but only for half a second at a time.
>
> See `2026-09-18_FULL_RUN_corrections.md`. Read the sections below against that file.

## Tested against the waveform. The room claim is confirmed. The Dwyer claim is partly confirmed.

Method: `faster_whisper.audio.decode_audio` at 16 kHz over the two published extracts
(29:17→32:02 and 58:02→end). Noise floor measured as RMS dBFS over each inter-turn gap with
100 ms trimmed from each end to exclude speech tails. Segment intensities are the Praat
`db_mean` values already in the segment file.

---

## 1. The room — confirmed, and by a wide margin

The 5.74-second gap at **29:39.88 → 29:45.62** measures **−62.2 dBFS**.

| | dBFS |
|---|---|
| median inter-turn gap (n = 29, both extracts) | −40.0 |
| 10th percentile | −47.9 |
| **next quietest single gap** | **−51.8** |
| **the 5.74 s gap** | **−62.2** |

- **22.2 dB below the median gap** — z = **−2.97**, **rank 1 of 29**.
- **10.4 dB below the next quietest gap in the sample.** It is not the tail of the distribution.
  It is separated from it.
- 22 dB is roughly a **13-fold** reduction in sound pressure.

Every other gap in this hearing carries room tone — paper, chairs, movement, breathing, plant.
This one does not.

### Time course (250 ms steps from the end of his last word)

| offset | dBFS |
|---|---|
| +0.00 s | −49.8 |
| **+0.25 s** | **−61.4** |
| +0.50 s | −63.1 |
| +0.75 s → +4.75 s | **−61.7 to −64.4, held** |
| +5.00 s | −59.5 (rising — the Commissioner draws breath) |

**The floor drops 11.6 dB within a quarter of a second and holds for five and a half seconds.**
That is not a speaker pausing. That is a room stopping.

---

## 2. Dwyer — real, but modest, and it does not last

His first words back, at **29:45.62**, are **61.8 dB — 4.2 dB below his own baseline** of 66.0 dB.

But measured against his own habit of retaking the floor (n = 100 re-entries after a Shepherd turn,
median 65.7 dB, sd 3.7):

- 61.8 dB is **−3.9 dB, z = −1.06, rank 12 of 100.** Quieter than usual. **Not unique** — he has
  eleven quieter re-entries, including 53.6 dB at 45:26 and 54.4 dB at 16:56.

There is a weak but real general effect: **longer silence → quieter re-entry**, r = −0.205,
p = 0.043. And a long silence before him is itself rare — only **4 of 98** re-entries follow a gap
of 3 s or more, and one of those is the 25.58 s pause at 25:27 while the Form 29 file is handled.

### What follows is the part memory does not keep

| time | dB vs his baseline | |
|---|---|---|
| 29:45.62 | **−4.2** | *"It's going to move on for a moment, okay?"* |
| 29:52.04 | +1.7 | |
| 29:56.00 | **+3.9** | *"And ultimately what I'm proposing is…"* |
| 30:14.96 | **+9.0** | *"If we can't get to that,"* — over the top of the interjection |

He is back above his own baseline within **6.4 seconds** and at **+9.0 dB within 30**. The 30-second
windows at 29:30 and 30:00 rank **112th and 107th of 120** by loudness — among the **loudest** of
the hearing, not the quietest.

⇒ The quiet re-entry is a **recovery beat**, not a retreat. What it precedes is the escalation
already recorded in `2026-09-16_THE_ARC_prosodic_control_7Aug2026.md`.

---

## 3. Note on the arc file

With amendment A1 applied (30:12.98 re-attributed to MR SHEPHERD), the intensity maximum in this
passage belongs to **30:14.96** at 75.0 dB / +9.0 dB, not to 30:12.98.

---

## 5. What is actually *in* the other gaps — added 17 September 2026

The level comparison in §1 says the silence is quieter. This section says **what the difference is
made of**. Each gap was measured for discrete events: 20 ms frame levels, counting every frame more
than 8 dB above that gap's own floor — the signature of paper, a chair, a footfall, a cough.

| | other gaps (n = 28) | the 5.74 s |
|---|---|---|
| level | median **−39.8 dBFS** | **−62.2** |
| discrete events | median **4.71 /s** (range 0 – 20.65) | **0.72 /s** |

### ⚠ Correction to an over-broad reading

**It is not true that every other pause contains a discrete event. 8 of the 28 contain none.**
But every one of those eight is **short — 0.42 s to 1.36 s** — and they sit at −29.7 to −37.5 dBFS,
25 to 30 dB **above** the silence. They are not quiet; they are full of continuous room noise
(ventilation, hum, murmur) and simply too brief to contain a discrete event.

The correct statement is narrower and stronger:

> **No other gap in the sample is both long and quiet.**

| gaps ≥ 1.2 s, excluding the silence | n = 9 |
|---|---|
| level range | −51.8 to −31.3 dBFS |
| **median** | **−43.5 dBFS** |
| **the 5.74 s silence** | **−62.2 dBFS** |

Every gap that lasts is noisy. Every gap that is quiet is too short to mean anything. One gap is
six times longer than the typical pause **and** 19 dB below the quietest comparable one.

### The events inside the silence are not the room

The gap registers 4 frame-groups above its floor. They are not people:

| offset | level | what it is |
|---|---|---|
| +0.00 → +0.14 s | −45.0 to −53.5 dBFS | **the decay tail of his own last word, *"numbers"***, ringing out |
| **+0.16 → +5.04 s** | **nothing above the floor** | **4.88 seconds with no event of any kind** |
| +5.06 s | −55.3 dBFS | **the Commissioner drawing breath** (matches the level rise at +5.00 s in §1) |

Between the end of his voice and the start of the Commissioner's breath there are **4.88 seconds in
which the room produces nothing measurable at all.** Floor −63.5 dBFS, flat.

That is the finding: not that the room was quieter than usual, but that for almost five seconds it
generated **no sound other than the building**.

---

## 6. The respondents — what is audible, and what cannot be established

### On the record

**MS MATHESON is the entire respondent presence in 65 minutes: three turns, 17 words.**

| time | level | vs Dwyer | vs Shepherd | |
|---|---|---|---|---|
| 17:35.36 | **48.5 dB** | **−17.5** | −13.7 | *"Yes, Commissioner. We've disclosed all we have currently."* |
| 22:29.58 | 63.2 dB | −2.8 | +1.0 | *"Only just now."* |
| 40:36.74 | **54.1 dB** | **−11.9** | −8.1 | *"The request for conducting an email,"* |

Word share of the spoken record: **Dwyer 8,313 · Shepherd 1,331 · Matheson 17 — 0.18%.**

Two of her three turns are **11.9 and 17.5 dB below the Commissioner** — far off-mic, consistent
with the far end of the bar table. She is audible, but only just, and only when addressed directly.

### ⚠ Retraction — voice detection inside the short gaps

Two attempts were made to detect unattributed voices (murmuring, whispering at the respondents'
end) inside the inter-turn gaps. **Both failed and neither result is relied on.**

1. **Frame-normalised autocorrelation** returned "voice-like" for **25 of 25 gaps, including the
   5.74 s silence at −62.2 dBFS.** Per-frame normalisation destroyed the level information and made
   the noise floor read as periodic. Discarded.
2. **Level-gated autocorrelation with an f0-stability requirement** passed its sanity check on known
   speech (Shepherd 77 voiced frames, stability 0.92; Dwyer 79 frames, 0.95) but still returned
   "VOICE" for 16 of 25 gaps. The gaps are 0.50–1.78 s and sit **between** speech segments; a 100 ms
   trim at each end does not remove the decay of the preceding word or the onset of the next. The
   instrument cannot separate a third person's murmur from the speech either side of it.

**No claim is made about who, if anyone, can be heard in the short gaps.** Establishing that needs
either a longer trim than these gaps can afford or a multi-channel recording, and this is a
single-channel mix.

### What does stand

Whatever is or is not in the other gaps, **the 5.74 s silence contains nothing above its own
floor for 4.88 consecutive seconds** (§5). Ms Matheson's quietest recorded turn sits 17.5 dB below
the Commissioner and was still transcribed. A sound at that level, made anywhere in that room during
the silence, would have registered plainly above a −63.5 dBFS floor.

Nothing did.

---

## 7. Ranked against every second of the recording — added 17 September 2026

The earlier sections compare the silence against other **gaps**. This compares it against
**everything**: every 1-second window at a 0.25 s hop across all 556 s of available audio, with
2 s dropped at each file edge to exclude MP3 encoder padding (which produced two spurious
−63 dBFS windows at the head of the first extract in an earlier pass).

**n = 2,184 windows.**

### The ten quietest seconds in the entire recording

| rank | level | time |
|---|---|---|
| 1 | **−64.4 dBFS** | 29:41.25 |
| 2 | −64.1 | 29:41.50 |
| 3 | −64.0 | 29:41.75 |
| 4 | −63.9 | 29:40.75 |
| 5 | −63.7 | 29:41.00 |
| 6 | −63.6 | 29:40.50 |
| 7 | −63.4 | 29:42.00 |
| 8 | −63.3 | 29:43.75 |
| 9 | −63.2 | 29:40.25 |
| 10 | −63.2 | 29:42.50 |

**All ten are inside the 5.74 seconds.**

### The separation

| | |
|---|---|
| quietest second inside the silence | **−64.4 dBFS** |
| quietest second **anywhere else** in 556 s | **−53.5 dBFS** |
| **gap** | **10.9 dB** |
| median second of the hearing | −31.7 dBFS |
| **the silence vs the median second** | **32.6 dB down** |

- **0 of 2,159** windows elsewhere are quieter than even the *loudest* second of the silence.
- Against the median second: **43× lower sound pressure, 1,832× less acoustic energy.**
- Against the next-quietest second in the whole recording: **3.5× lower sound pressure.**

It is not the quietest moment by a margin. It is the quietest moment by a **category**: the ten
quietest seconds of the hearing are consecutive, and they are all the same five seconds.

---

## 8. Limits

The noise-floor baseline is drawn from 29 gaps inside the two published extracts, not from all
65 minutes; a full-hearing sample could move the median, though a 10.4 dB separation from the next
quietest gap is unlikely to close. MP3 encoding at the extract stage can suppress very low-level
content, which would bias the measured floor **downward** — the absolute figure of −62.2 dBFS should
be treated as a floor estimate, while the **relative** comparison against 28 other gaps encoded
identically is sound.
