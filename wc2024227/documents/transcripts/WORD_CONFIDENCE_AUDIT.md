# WORD-LEVEL CONFIDENCE AUDIT — THE SEGMENTS IN ISSUE

**16 September 2026.** Measured from `MENTION_7AUG2026_segments.jsonl` (the word-level output of the
original large-v3 run). ⛔ **No re-decode has been performed** — the audio is not in this repository.
See `redecode_disputed.py` for the ready-to-run targeted re-decode.

**Baseline for the whole hearing:** 9,693 words. **2.2%** below p=0.50; **3.6%** between 0.50 and 0.75.
Anything at or near those rates is normal; the interest is in individual words, not zone averages.

---

## ⛔ THE HEADLINE HYPOTHESIS WAS TESTED AND REFUTED — 16 September 2026

This file originally proposed that **"spread" (p=0.23) at 46:48.54 was a mis-recognition of
"suppressed"**, on the grounds that it was by far the weakest word in the passage and that "an
appointment is not actively spread". **The audio was obtained and the window re-decoded. The
hypothesis fails on both grounds.**

### The re-decode, five conditions

| Decode | Prompt primed "suppressed"? | Word returned | p |
|---|---|---|---|
| Original run (Aug, beam 5) | — | `spread,` | 0.23 |
| Re-decode, context pass | **yes** (domain prompt **and** Dwyer saying it 3× in-window) | `spread.` | 0.32 |
| Re-decode, no-context pass | **yes** (domain prompt) | `suppressed,` | 0.46 |
| Clean, neutral prompt | no | ⛔ **hallucinated** — *"Subtitles by the Amara.org community"* | — |
| **Clean, NO prompt at all** | **no** | **`spread,`** | **0.20** |

⇒ **Three of four valid passes return "spread", including the only genuinely unprimed one.** The
single "suppressed" reading came from the pass most primed toward it — **by the operator's own domain
prompt, which contained the phrase "actively suppressed"**. That was a methodological error in the
first re-decode and it is disclosed here.

### The semantic argument was also wrong

The subject of the clause is **the correspondence**, not the appointment. The fuller passage recovered
by the unprimed decode reads:

> *"It's more so the correspondence you got from the union. **The correspondence I also got from the
> manager**, but it wasn't actively **spread**, it was actively avoided, but would be more likely."*

Correspondence can straightforwardly be *spread*. The original objection mis-identified the subject.

### ⚠ Two method notes worth keeping

1. **Never put a disputed word into the decoder's prompt.** It contaminated the pass that produced
   the only contrary reading.
2. **An under-specified prompt is worse than none.** The "neutral prompt" condition **hallucinated**
   a stock YouTube-subtitle string on this audio. Low-information prompts on quiet, distant-mic audio
   invite fabrication. **Any empty or odd result must be inspected raw before it is read as a finding.**

⇒ **The transcript was right. "spread" stands.** Low probability here reflects a quietly spoken word
on a distant microphone, not an error.

## WHAT IS VERBATIM-CERTAIN, AND CAN BE QUOTED

| Passage | Per-word probabilities | Status |
|---|---|---|
| **[16:29] "I guess I did request"** | I 0.76 · **guess 0.96** · I 0.91 · **did 0.97** · **request 1.00** | ✅ **Settles N1 by measurement.** small.en's *"I didn't request"* is wrong at word level, not merely on aggregate. **Never cite small.en for this line.** |
| **[23:52] "So my filters were effective immediately"** | So 0.87 · my 0.92 · **filters 1.00** · were 1.00 · effective 0.99 · immediately 1.00 | ✅ The criterion specification is certain. **§99 rests on measured ground.** |
| **[46:10] "I don't know if I can prove it as much"** | **every word 1.00** | ✅ The concession is certain. Ten words, none below 1.00 — the cleanest passage audited. |
| **[29:31] "they're not sent to someone having a cardiac arrest"** | they're 0.97 · everything else **1.00** | ✅ The nine words are certain. |
| **[50:54] "a documented 42% pay disparity"** | documented 1.00 · **42 1.00** · % 0.97 · pay 1.00 · disparity 1.00 | ✅ **The figure itself is certain.** |
| **[51:50] "or your colleagues generally?"** | colleague 1.00 · your 1.00 · **colleagues 1.00** · **generally 1.00** | ✅ The class slide at N4 is certain. |

---

## TWO SECONDARY FLAGS

### "week" at 51:26.70 — p = 0.44

> *"That's what me and my colleagues over a six **week** [period]"* — That's 0.98 · ·what 0.50 ·
> ·me 0.75 · and 1.00 · my 1.00 · colleagues 1.00 · over 0.99 · a 0.98 · six 0.94 · **⚠week 0.44**

⚠ **The 42% is computed over a stated period, and the period's unit is the low-confidence word.**
The figure is certain; the denominator is not. **Verify the period against the payslips before the
42% is stated anywhere with a period attached.**

### "Yeah," at 30:12.98 — p = 0.37 — and this *supports* amendment A1

> *"**Yeah,** I actually understand what you're getting at."*
> ⚠Yeah, **0.37** · I 1.00 · actually 1.00 · understand 0.99 · what 0.97 · you're 0.96 · getting 0.97 · ·at. 0.67

⭐ The substance of the amended line is near-certain; **the only weak element is the lead-in
interjection** — precisely the class the transcript's own Method section identifies as the weakest
for automated attribution, and precisely why the speaker label was wrong. **The measurement is
consistent with A1 rather than against it.** The words are safe to quote; the attribution rests on
participant confirmation, as A1 records.

---

## ZONE SUMMARY

| Zone | Segments | Words | Mean avg_logprob | <0.50 | 0.50–0.75 |
|---|---|---|---|---|---|
| N1 16:29 | 5 | 68 | −0.207 | 4.4% | 0.0% |
| N2 filters | 12 | 100 | −0.222 | 3.0% | 7.0% |
| 29:17 nine words | 13 | 100 | **−0.151** | **1.0%** | 3.0% |
| A1 zone | 14 | 138 | −0.177 | 2.9% | 4.3% |
| N3 suppressed | 22 | 207 | **−0.128** | 1.9% | 2.4% |
| N4 comparator | 24 | 153 | −0.153 | 2.6% | 3.9% |
| **whole hearing** | 1,068 | 9,693 | −0.180 | **2.2%** | **3.6%** |

⇒ **No disputed zone is anomalously bad.** N3 and the nine words are *better* than the hearing
average. The problems are individual words, not degraded passages — which is why a targeted
re-decode of six short windows is the right tool and a whole-file re-run is not.

---

## WHAT A RE-DECODE WOULD ADD, AND WHAT IT WOULD NOT

`redecode_disputed.py` targets the six windows with beam 10 / best_of 10, **temperature 0 with no
fallback**, VAD off, ±6 s padding, a domain-primed prompt, and **two passes compared** (with and
without prior-text conditioning). Disagreement between passes is treated as the signal.

⛔ **It still produces machine output.** For any word carrying legal weight — "spread"/"suppressed"
above all — **listen to the audio at the timestamp**, then record the outcome in the AMENDMENT LOG
with a confidence class. That is what makes it a participant correction rather than a second guess.
