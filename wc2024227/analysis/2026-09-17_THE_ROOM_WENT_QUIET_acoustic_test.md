# WC/2024/227 — "THE ROOM WENT QUIET"
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

## 4. Limits

The noise-floor baseline is drawn from 29 gaps inside the two published extracts, not from all
65 minutes; a full-hearing sample could move the median, though a 10.4 dB separation from the next
quietest gap is unlikely to close. MP3 encoding at the extract stage can suppress very low-level
content, which would bias the measured floor **downward** — the absolute figure of −62.2 dBFS should
be treated as a floor estimate, while the **relative** comparison against 28 other gaps encoded
identically is sound.
