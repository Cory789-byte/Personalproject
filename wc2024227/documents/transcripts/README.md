# Mention of 7 August 2026 — transcripts. READ THIS BEFORE QUOTING ANYTHING.

## Which file to use

| File | Use it for | Status |
|---|---|---|
| `MENTION_7AUG2026_TRANSCRIPT_diarised_CORRECTED.pdf` | **reading** | ⭐ canonical narrative copy |
| `TRANSCRIPT_diarised_prosody.md` | reading with prosody (F0, intensity, rate, pauses) | ⭐ corrections now marked **inline in the body** |
| `MENTION_7AUG2026_segments.jsonl` | **machine search, timestamps, interval arithmetic** | ⭐ corrections now **applied to the `speaker` field** |
| `diarise_inferential.py` | how the labels were produced | tool |
| ⭐⭐ `MENTION-7AUG2026-FIX-LEDGER.md` | **every fix ever made to the mention — transcript and reading — in one place, recomputed from the data** | ⭐ start here |

## ⛔⛔ The rule that exists because it was broken

**On 15 September 2026 a line was attributed to the bench that the Appellant had actually spoken.**
The corrected attribution had been settled on 12 September and recorded in the corrections table —
but the table was at the top of the file and the *body* still carried the machine label, and the
`.jsonl` had not been patched at all. The analysis was done off the raw `.jsonl`.

⇒ **Every one of the ten corrections is now applied in both the `.jsonl` and the prosody body.**
⇒ ⛔ **Never attribute a short line — "Yeah", "Yes", "No", "All right" — from machine output alone.**
The documented failure mode is: *a short acknowledgement inside a long run is given to whoever holds
the floor.* All ten corrections are of exactly that kind.

## What was corrected — final, applied 15 September 2026

**⭐ Forty-four segments were reattributed and four were split.** No segment is now unattributed.
**Final counts: DWYER IC 853 · MR SHEPHERD 210 · MS MATHESON 9 across 1,072 rows.**
⚠ **The figure was 38 here until 15 September, when it was recomputed against the data and found wrong** —
it had been carried forward from an intermediate commit. The full verified ledger, with the reproducible
diff that produces it, is `MENTION-7AUG2026-FIX-LEDGER.md`.
⚠ *(superseded — see the line above; the flip-shape audit of 15 Sep added segs 64, 482, 483 and split 63 and 483.)*

**A. The 12 September review** — 437 (30:12) DWYER → **MR SHEPHERD**, ⭐ *Certain, confirmed first-hand
by the Appellant*; 623, 1009 → DWYER IC; 627, 628 (40:40) and 1008 → **MS MATHESON**; 908 confirmed
unchanged.
⚠ **440, 620, 673, 792 already carried `MR SHEPHERD` in this `.jsonl`.** They were corrections to the
**other** machine baseline — the diarisation pass behind the PDF. ⛔ **There are two machine baselines in
this matter. Always say which one a correction is against.**

**B. Six confirmed by the Appellant, who was present, on 15 September 2026**

| Seg | Time | Was | Now | The line |
|---|---|---|---|---|
| 396–399 | 27:44 | MR SHEPHERD | **DWYER IC** | *"She's erratic physical presence and imposes unassessed unilateral directives."* — the bench reading the stressor aloud |
| 231–232 | 17:45 | *(no diariser cluster on 232)* | **MR SHEPHERD, confirmed** | *"There has been some emails to involve the quality of the staff…"* ⚠ both already carried this label; the confirmation supports a label the machine could not |
| 863 | 53:14 | DWYER IC (merged) | **split** | *"holidays?"* → DWYER IC · *"There's probably a few"* → MR SHEPHERD |
| 864 | 53:18 | DWYER IC (merged) | **split** | *"things yes."* → MR SHEPHERD · *"Well probably or is because disclosure is about what you know"* → DWYER IC |
| 893 | 54:47 | MR SHEPHERD | **DWYER IC** | *"roster for the relevant period"* |
| 429 | 29:37 | MR SHEPHERD | *confirmed, unchanged* | *"we're now not even contacting them by their numbers"* — **the Appellant's line** |
| 633–635 | 41:01 | MR SHEPHERD | **MS MATHESON** | *"I do believe that I have received those, Commissioner, and disclosed them. I would have to triple check to be…"* — 635 continues her own sentence, and the bench answers it with *"That's okay. That's all right."* |
| 183 | 14:20 | DWYER IC | *confirmed, unchanged* | *"And I don't want you to do that now, which is what you're launching into."* |

⚠ Segments 863 and 864 each contained **two speakers in one segment**. They were split and the
boundary timestamp interpolated; the surrounding timings are unchanged.

**C. Twenty-six resolved by question-and-answer structure** *(the count read "Nineteen" until 15 Sep; the ids listed here have always been 26)* — a judge does not ask and answer his own
question. 227, 247, 249, 537, 588, 614, 616, 706, 707, 708, 730, 779, 819 → **MR SHEPHERD**;
375, 523, 533, 552, 554, 562, 613, 669, 671, 700, 834, 914, 919 → **DWYER IC**.

## ⛔ Seg 437 — why it matters

At 30:12, after the bench redirected him, **the Appellant said "Yeah, I actually understand what
you're getting at."** He was signalling that he had taken the method the bench had just set out —
that evidence which is not contradicted is likely to be accepted, so the case could be proved
without the documents. The machine gave the line to the bench, which inverted its meaning. The
action that follows is continuous with the line as correctly attributed: the disclosure application
withdrawn 10 August, the notice to admit 303 facts served 28 August, 298 admitted on 8 September.

## ⚠ Standing cautions

- **None of these transcripts is certified.** Overall speaker accuracy measured at **90%** on 30
  hand-checked anchor turns. Transcription confidence is high (mean log-probability −0.180).
- ⛔ **Order the certified transcript before any passage is quoted externally** — in a filing, a
  letter, or to the Commission. These files are for internal analysis only.
- `small.en` output is **less** accurate than the `large-v3` set here and contains at least two
  hallucinations — see `skill/references/TRANSCRIPT-ACCURACY-comparison.md`.
- Residual errors are concentrated in **one- and two-word interjections and overlapping speech**.
  Long turns and question-and-answer exchanges are reliable.
- ⚠⚠ **Residual risk, measured 15 September.** The diariser's own cluster contradicts the label on
  **45 segments** (down from 75 — **32 of the 41 fixes came out of that set**), and **50 segments have
  no cluster at all**. ⭐ Two fixes were applied *against* the cluster (segs 399, 864) because the
  Appellant confirmed them — **a person who was in the room outranks the machine**. **0 of 1,068 long
  turns** show any conflict, so every substantive analysis is unaffected. **Others may remain.** Any
  short interjection still has to be checked against who was asked the question before it is relied on.

---

## ⭐⭐ Split-segment ids

A split child's id is **`100000 + parent id`**. Any id ≥ 100000 is the second half of a segment the
diariser had merged across a speaker change; subtract 100000 for its parent. Current children:
**100063, 100483, 100863, 100864**. ⚠ The earlier scheme (8631/8641) collided with real segment ids
and was withdrawn.

## ⭐ Read the per-word confidences before relying on a phrase

Every word carries a probability in the `p` field of its `words` entry. The fabricated-quotation
error of 15 September sat on a word the model scored at **0.02** while every word around it scored
0.97–1.00. **The file was flagging its own guess and nobody read the flag.**
