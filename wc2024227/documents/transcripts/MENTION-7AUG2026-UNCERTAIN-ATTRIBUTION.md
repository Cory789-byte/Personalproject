# THE MENTION OF 7 AUGUST 2026 — SEGMENTS THAT CANNOT BE SAFELY ATTRIBUTED

**WC/2024/227 · 15 September 2026 · ⛔ INTERNAL ONLY. Nothing here is quoted externally.**

⭐⭐ **This file deliberately carries no speaker names for the 83 segments below.** Each is given as
a pair of percentages instead. Where the estimate lands between 40% and 59% it is marked
**🔴 NO CALL** and must be treated as genuinely unknown — not as a weak lean.

⛔ **Rule:** none of these 83 lines is relied on, quoted, or reasoned from as anybody's words
until it is confirmed by a person who was in the room or by the certified transcript.

---

## 1. How the percentages were produced — and how good they are

Four signals were tested against held-out data. **Two survived. Two were rejected, and the
rejections matter as much as the acceptances.**

| Signal | Tested how | Result | Used? |
|---|---|---|---|
| **Diariser cluster** (`spk`) | 294 held-out long turns | ⭐ **97.3% correct** | ✅ **yes — the strongest signal by far** |
| **Turn-change after a question** | 397 adjacent long-turn pairs | ⭐ speaker changes **54%** of the time after a segment ending in `?`, against a **9%** baseline — a **6× lift** | ✅ yes, as the prior |
| **Pitch** (F0 median) | 566 long turns | ⛔ **Cohen's d = 0.03.** Dwyer 137.5 Hz, Shepherd 137.2 Hz. **The two men have the same voice pitch.** | ❌ **no — useless** |
| **Loudness** (mean dB) | trained on half, tested on half | Separates them (d = 1.09, Dwyer 65.6 dB v Shepherd 62.1 dB — mic distance, not voice) but scored **86.4%**, *worse* than the 88.4% you get from the base rate alone. **It actively hurt.** | ❌ **no — tested and rejected** |

### ⚠ The reliability figure that carries the most weight, and how weak it is

The cluster is **97.3% on long turns** — but every one of the 44 known errors was a **short** turn,
so long-turn accuracy is the wrong number to apply here. Short-turn accuracy can only be measured
against independent ground truth, and there is very little of it:

| Sample | Cluster correct | Use |
|---|---|---|
| 294 held-out **long** turns | **97.3%** | applies to turns over 10 words |
| 26 structurally-resolved short turns | 100% | ⛔ **discarded — circular.** Most were *found* by looking at cluster disagreement |
| ⭐ **13 independently confirmed short turns** (the Appellant's own first-hand confirmations, plus segments resolved by reading the words) | ⚠ **9/13 = 69%** | ✅ **this is the figure used for turns of 5 words or fewer** |

⚠⚠ **n = 13.** That is a thin basis for a reliability constant, and it is the weakest joint in the
model. It was chosen over the flattering 100% because that sample is contaminated and this one is
not. The cluster was wrong on four of those thirteen — including on two split-segment heads and on
segment 429, a line the Appellant confirmed as his own.

### The model, stated in full so it can be attacked

```
P(Dwyer) ∝ prior × cluster_likelihood

prior            = 0.91 if the previous segment does not end in '?' and was Dwyer's
                   0.54 if it does end in '?' and was Dwyer's       (measured: 54% / 9%)
                   mirrored where the previous segment was the Appellant's
cluster reliability = 0.70  for turns of <=5 words     (measured, n=13)
                      0.85  for 6-10 words             (interpolated - NOT measured)
                      0.97  for >10 words              (measured, n=294)
pitch, loudness  = excluded (see table above)
```

⛔ **Three things the percentages are not.**
1. **They are not measurements of who spoke.** They are the output of a two-signal model.
2. **They inherit the previous segment's label**, which in a few cases is itself uncertain. Errors
   can therefore chain.
3. ⛔⛔ **The model cannot represent Ms Matheson at all** — the diariser produced no cluster for
   her, which is why her six segments were dealt out to the other two men in the first place. Any
   segment inside her known speaking windows carries a **⚠ M** flag below and the two percentages
   there should be read as *conditional on it being one of the two men*.

---

## 2. 🔴 The 15 genuine no-calls — the model cannot separate these

| Time | Estimate | Words | Why unclear | The line |
|---|---|---|---|---|
| **14:48.62** | **D 46% / S 54%** | 1 | no cluster | *Exactly.* |
| **16:55.94** | **D 46% / S 54%** | 1 | no cluster | *Correct.* |
| **22:51.96** | **D 46% / S 54%** | 1 | no cluster | *Yes.* |
| **23:26.28** | **D 46% / S 54%** | 1 | no cluster | *10.* |
| **23:29.16** | **D 46% / S 54%** | 1 | no cluster | *10.* |
| **26:56.34** | **D 46% / S 54%** | 1 | no cluster | *Yep.* |
| **35:26.56** | **D 46% / S 54%** | 1 | no cluster | *Yes.* |
| **40:28.28** | **D 46% / S 54%** | 1 | no cluster | *Yes.* |
| **40:29.94** | **D 46% / S 54%** | 4 | no cluster | *No, I do not.* |
| **42:25.34** | **D 46% / S 54%** | 2 | no cluster | *Correct, yes.* |
| **44:37.86** | **D 46% / S 54%** | 1 | no cluster | *Yep.* |
| **45:25.16** | **D 46% / S 54%** | 1 | no cluster | *Exactly.* |
| **49:53.18** | **D 46% / S 54%** | 1 | no cluster | *Yeah.* |
| **55:59.66** | **D 46% / S 54%** | 1 | no cluster | *Yeah.* |
| **64:33.38** | **D 46% / S 54%** | 2 | no cluster | *All right.* |

⇒ ⛔ **These are the ones to put to the certified transcript first.** Nothing in the analysis
files should rest on any of them.

---

## 2A. ⛔⛔ Where the words settle what the model cannot — read this before trusting any number

The model has **no access to meaning**. It knows cluster identity and turn position. It does not
know who would say a thing. Three examples from this very register show how far that can go, and
they are why the percentages are a triage tool and not an answer.

| Time | Model says | What the words say |
|---|---|---|
| **03:19** *"Section 32.5, reasonable management action taken in a reasonable way."* | ⛔ **SHEPHERD 76%** | **The bench**, reciting the statutory exclusion in the opening framework. An appellant does not read the Act to the Commissioner in the third minute. **The model is simply wrong here** |
| **14:35** *"What do you mean by that, Mr Sheppard?"* | DWYER 64% | ⭐ **Certain — the bench.** The segment names the person being addressed. **Removed from the register on that ground**, not on its percentage |
| **32:19** *"disclosure for documents that you say…"* | 🔴 no call | **The bench.** *"documents that **you** say"* is addressed to the appellant, and it sits mid-sentence inside a Dwyer run |

⇒ ⭐⭐ **Where a segment names a person in the room, content decides and the model is ignored.**
⇒ ⛔ **Everywhere else a low percentage is a reason to check, never a reason to reattribute.**
**The percentages rank the work. They do not do it.**

---

## 3. The full register — 83 segments, in time order

`[nc]` the diariser produced **no cluster** for this segment · `[xc]` it produced a cluster that
**contradicts** the label currently in the file · `⚠ M` inside a window where Ms Matheson is known
to have spoken · `?→` the preceding segment ends in a question, which raises the chance the
speaker changed here to 54%.

### 0–5 minutes

**03:19.08** &nbsp; 🟡 — **DWYER 24% · SHEPHERD 76%**
<sub>[xc] · 11w · file currently says DWYER IC</sub>

> Section 32.5, reasonable management action taken in a reasonable way.

### 5–10 minutes

**07:06.28** &nbsp; 🟠 — **DWYER 64% · SHEPHERD 36%**
<sub>[xc] · 9w · file currently says DWYER IC</sub>

> how this impacts the efficient conduct of the proceedings.

**07:09.36** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[xc] · gap 0.9s · 17w · file currently says MR SHEPHERD</sub>

> I understand, I think I understand, what you think you are trying to achieve and I'm not

**07:25.32** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[xc] · 15w · file currently says MR SHEPHERD</sub>

> don't have any problem with it that's fine I don't have a problem with that

**08:49.54** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Okay.

**09:10.06** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · gap 1.3s · 1w · file currently says MR SHEPHERD</sub>

> well

**09:18.16** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> days

**09:19.50** &nbsp; 🟡 — **DWYER 19% · SHEPHERD 81%**
<sub>[xc] · gap 1.0s · 1w · file currently says MR SHEPHERD</sub>

> and

**09:26.12** &nbsp; 🟡 — **DWYER 81% · SHEPHERD 19%**
<sub>[xc] · 5w · file currently says DWYER IC</sub>

> AI or what's not AI

### 10–15 minutes

**10:24.68** &nbsp; 🟡 — **DWYER 24% · SHEPHERD 76%**
<sub>[xc] · 18w · file currently says DWYER IC</sub>

> is always the best. People make the mistake. I've got to have a big case because then it

**10:32.36** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[xc] · 10w · file currently says MR SHEPHERD</sub>

> I mean for me it happened over a whole year

**14:02.88** &nbsp; 🟠 — **DWYER 36% · SHEPHERD 64%**
<sub>[xc] · 7w · file currently says MR SHEPHERD</sub>

> would show that, you know, people would...

**14:06.16** &nbsp; 🟠 — **DWYER 36% · SHEPHERD 64%**
<sub>[xc] · 6w · file currently says MR SHEPHERD</sub>

> I think I attached one attachment

**14:12.20** &nbsp; 🟡 — **DWYER 19% · SHEPHERD 81%**
<sub>[xc] · 5w · file currently says MR SHEPHERD</sub>

> No, hang on a sec.

**14:13.36** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Sorry.

**14:48.62** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · gap 0.5s · 1w · file currently says MR SHEPHERD</sub>

> Exactly.

### 15–20 minutes

**16:55.94** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 1w · file currently says MR SHEPHERD</sub>

> Correct.

**18:31.00** &nbsp; 🟡 — **DWYER 19% · SHEPHERD 81%**
<sub>[xc] · 1w · file currently says MR SHEPHERD</sub>

> Okay.

**19:31.60** &nbsp; 🟡 — **DWYER 81% · SHEPHERD 19%**
<sub>[xc] · 4w · file currently says DWYER IC</sub>

> Maybe not, but maybe.

**19:50.36** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Okay.

### 20–25 minutes

**22:51.96** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 1w · file currently says MR SHEPHERD</sub>

> Yes.

**22:59.68** &nbsp; 🟡 — **DWYER 13% · SHEPHERD 87%**
<sub>[xc] · ?→ · 6w · file currently says DWYER IC</sub>

> So just say email directives, basically.

**23:26.28** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 1w · file currently says MR SHEPHERD</sub>

> 10.

**23:29.16** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 1w · file currently says MR SHEPHERD</sub>

> 10.

**23:44.52** &nbsp; 🟡 — **DWYER 19% · SHEPHERD 81%**
<sub>[xc] · gap 0.8s · 4w · file currently says MR SHEPHERD</sub>

> or let's say Outlook,

### 25–30 minutes

**26:30.40** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Yeah.

**26:30.92** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Okay.

**26:54.36** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Okay.

**26:56.34** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 1w · file currently says MR SHEPHERD</sub>

> Yep.

**27:59.66** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[xc] · 14w · file currently says MR SHEPHERD</sub>

> effective immediately we're going to do this, effective immediately we're going to do that.

### 30–35 minutes

**30:19.46** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Yeah.

**32:02.78** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[xc] · 4w · file currently says MR SHEPHERD</sub>

> I think I can

**32:14.98** &nbsp; 🟡 — **DWYER 81% · SHEPHERD 19%**
<sub>[xc] · 5w · file currently says DWYER IC</sub>

> regulator about what they can

**32:16.88** &nbsp; 🟠 — **DWYER 64% · SHEPHERD 36%**
<sub>[xc] · 6w · file currently says DWYER IC</sub>

> and can't facilitate in respect of

**32:19.04** &nbsp; 🟠 — **DWYER 64% · SHEPHERD 36%**
<sub>[xc] · 6w · file currently says DWYER IC</sub>

> disclosure for documents that you say

**32:21.10** &nbsp; 🟡 — **DWYER 81% · SHEPHERD 19%**
<sub>[xc] · 5w · file currently says DWYER IC</sub>

> they could have or should

**32:43.46** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[xc] · gap 2.4s · 57w · file currently says DWYER IC</sub>

> I don't know whether it's a generational thing, but back in my day we used to pick up the phone and we would talk to people and we'd say, hey, and just because you're an opponent to somebody in litigation doesn't mean you can't have a constructive civil conversation with them, right? Even if you're self-represented.

**33:24.44** &nbsp; 🟡 — **DWYER 24% · SHEPHERD 76%**
<sub>[xc] · 12w · file currently says DWYER IC</sub>

> in terms of your response to the objection in relation to it,

**33:28.96** &nbsp; 🟡 — **DWYER 81% · SHEPHERD 19%**
<sub>[xc] · 5w · file currently says DWYER IC</sub>

> and your application as well.

**34:38.54** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · gap 1.5s · 1w · file currently says MR SHEPHERD</sub>

> Anyway.

### 35–40 minutes

**35:26.56** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 1w · file currently says MR SHEPHERD</sub>

> Yes.

**35:27.48** &nbsp; 🟡 — **DWYER 19% · SHEPHERD 81%**
<sub>[xc] · 4w · file currently says MR SHEPHERD</sub>

> She took them out.

**35:44.20** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · gap 0.5s · 1w · file currently says DWYER IC</sub>

> Okay.

**36:52.92** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Yep.

**37:16.98** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[xc] · 20w · file currently says MR SHEPHERD</sub>

> do that in an email or a letter? I wrote that to an email and that was our email correspondence

**37:22.04** &nbsp; 🟡 — **DWYER 76% · SHEPHERD 24%**
<sub>[xc] · 17w · file currently says MR SHEPHERD</sub>

> back of course. Yes, I got that. And you've got that? Yeah. Done. You've got your documents

**39:08.54** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Yeah.

### 40–45 minutes

**40:28.28** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 1w · file currently says MR SHEPHERD</sub>

> Yes.

**40:29.94** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 4w · file currently says MR SHEPHERD</sub>

> No, I do not.

**41:53.82** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Yep.

**42:25.34** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 2w · file currently says MR SHEPHERD</sub>

> Correct, yes.

**42:47.56** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Okay.

**42:53.60** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Yeah.

**42:59.54** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Yeah.

**43:36.16** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[xc] · 17w · file currently says MR SHEPHERD</sub>

> union delegate, in an email I presume? Yeah, even in when I went for, when I went

**44:37.86** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 1w · file currently says MR SHEPHERD</sub>

> Yep.

### 45–50 minutes

**45:25.16** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 1w · file currently says MR SHEPHERD</sub>

> Exactly.

**45:25.74** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Okay.

**47:22.10** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · gap 0.5s · 1w · file currently says MR SHEPHERD</sub>

> Okay.

**47:35.76** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[xc] · ?→ · gap 0.8s · 15w · file currently says DWYER IC</sub>

> you've got all of that? I just haven't got what the manager did with that

**47:43.02** &nbsp; 🟡 — **DWYER 24% · SHEPHERD 76%**
<sub>[xc] · 15w · file currently says DWYER IC</sub>

> that they did anything with it? Well I think they didn't do anything with it

**48:36.74** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Correct.

**48:37.38** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Okay.

**48:57.04** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[xc] · 16w · file currently says MR SHEPHERD</sub>

> I got this letter from the union, and the letter says the management is blocking me.

**49:37.50** &nbsp; 🟡 — **DWYER 19% · SHEPHERD 81%**
<sub>[xc] · 4w · file currently says MR SHEPHERD</sub>

> I can't remember the...

**49:40.20** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · gap 0.5s · 3w · file currently says DWYER IC</sub>

> Yes or no?

**49:53.18** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 1w · file currently says MR SHEPHERD</sub>

> Yeah.

### 50–55 minutes

**53:00.52** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Yes.

**53:01.26** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Okay.

**54:04.94** &nbsp; 🟡 — **DWYER 24% · SHEPHERD 76%**
<sub>[xc] · 16w · file currently says DWYER IC</sub>

> So I recall that we don't need to go over that too because I've recalled that.

### 55–60 minutes

**55:53.54** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 1w · file currently says DWYER IC</sub>

> Okay.

**55:59.66** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · gap 0.6s · 1w · file currently says MR SHEPHERD</sub>

> Yeah.

**56:00.22** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Okay.

**56:04.54** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[xc] · gap 2.6s · 13w · file currently says MR SHEPHERD</sub>

> Are there any documents in relation to any of that that you think...

**56:08.36** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Okay.

**56:08.72** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 2w · file currently says MR SHEPHERD</sub>

> All right.

**56:33.36** &nbsp; 🟡 — **DWYER 10% · SHEPHERD 90%**
<sub>[nc] · 1w · file currently says MR SHEPHERD</sub>

> Yeah.

**59:53.24** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[xc] · 15w · file currently says MR SHEPHERD</sub>

> both as a commissioner and as a practitioner, appearing against them on many occasions as

### 60–65 minutes

**61:23.96** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · gap 1.1s · 1w · file currently says MR SHEPHERD</sub>

> Okay?

**61:42.92** &nbsp; 🟠 — **DWYER 27% · SHEPHERD 73%**
<sub>[xc] · ?→ · ⚠ M · gap 1.1s · 3w · file currently says DWYER IC</sub>

> Okay, all right.

**64:27.20** &nbsp; 🟡 — **DWYER 81% · SHEPHERD 19%**
<sub>[xc] · gap 1.0s · 3w · file currently says DWYER IC</sub>

> OK? All right.

**64:28.94** &nbsp; 🟡 — **DWYER 90% · SHEPHERD 10%**
<sub>[nc] · 2w · file currently says MR SHEPHERD</sub>

> All right.

**64:33.38** &nbsp; 🔴 NO CALL — **DWYER 46% · SHEPHERD 54%**
<sub>[nc] · ?→ · 2w · file currently says MR SHEPHERD</sub>

> All right.

---

## 4. Distribution

| Band | Segments |
|---|---|
| DWYER, 90% (capped) | **25** |
| DWYER, 75–89% | **7** |
| DWYER, 60–74% | **3** |
| 🔴 NO CALL (40–59%) | **15** |
| SHEPHERD, 60–74% | **3** |
| SHEPHERD, 75–89% | **12** |
| SHEPHERD, 90% (capped) | **18** |
| **total** | **83** |

**46 of the 83** have no diariser cluster at all; the
remaining **37** have one that contradicts the label in the file.

⚠ **Calibration, measured on held-out data:** in the 80%+ band the model was right about **87–90%**
of the time. **In the 50–60% band it was right 42–48% of the time — worse than a coin toss.**
That is why the middle band is marked NO CALL rather than given a lean.

---

## 5. What this register is for

1. ⛔ **A stop list.** No line here is quoted or reasoned from as anyone's words.
2. ⭐ **An order of work for the certified transcript.** Section 2 first, then the 90%+ Shepherd
   entries — those are lines the file currently gives to the bench.
3. ⭐ **A list to put to the Appellant**, who was in the room. His confirmation outranks every
   number in this file, as it already has on thirteen segments.

⚠ **None of these transcripts is certified.** Order the certified transcript before any passage is
quoted in a filing, a letter, or to the Commission.
