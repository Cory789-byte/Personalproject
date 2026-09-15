# Mention of 7 August 2026 — transcripts. READ THIS BEFORE QUOTING ANYTHING.

## Which file to use

| File | Use it for | Status |
|---|---|---|
| `MENTION_7AUG2026_TRANSCRIPT_diarised_CORRECTED.pdf` | **reading** | ⭐ canonical narrative copy |
| `TRANSCRIPT_diarised_prosody.md` | reading with prosody (F0, intensity, rate, pauses) | ⭐ corrections now marked **inline in the body** |
| `MENTION_7AUG2026_segments.jsonl` | **machine search, timestamps, interval arithmetic** | ⭐ corrections now **applied to the `speaker` field** |
| `diarise_inferential.py` | how the labels were produced | tool |

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

**Thirty-eight segments were reattributed and two were split.** No segment is now unattributed.
Final counts: **DWYER IC 852 · MR SHEPHERD 209 · MS MATHESON 9** across 1,070 segments.

**A. The ten from the 12 September review** — 437 (30:12) DWYER → **MR SHEPHERD**, ⭐ *Certain,
confirmed first-hand by the Appellant*; 440, 620, 673, 792 → MR SHEPHERD; 623, 1009 → DWYER IC;
627, 628 (40:40) and 1008 → **MS MATHESON**; 908 confirmed unchanged.

**B. Six confirmed by the Appellant, who was present, on 15 September 2026**

| Seg | Time | Was | Now | The line |
|---|---|---|---|---|
| 396–399 | 27:44 | MR SHEPHERD | **DWYER IC** | *"She's erratic physical presence and imposes unassessed unilateral directives."* — the bench reading the stressor aloud |
| 231–232 | 17:45 | unattributed | **MR SHEPHERD** | *"There has been some emails to involve the quality of the staff…"* |
| 863 | 53:14 | DWYER IC (merged) | **split** | *"holidays?"* → DWYER IC · *"There's probably a few"* → MR SHEPHERD |
| 864 | 53:18 | DWYER IC (merged) | **split** | *"things yes."* → MR SHEPHERD · *"Well probably or is because disclosure is about what you know"* → DWYER IC |
| 893 | 54:47 | MR SHEPHERD | **DWYER IC** | *"roster for the relevant period"* |
| 429 | 29:37 | MR SHEPHERD | *confirmed, unchanged* | *"we're now not even contacting them by their numbers"* — **the Appellant's line** |
| 633–635 | 41:01 | MR SHEPHERD | **MS MATHESON** | *"I do believe that I have received those, Commissioner, and disclosed them. I would have to triple check to be…"* — 635 continues her own sentence, and the bench answers it with *"That's okay. That's all right."* |
| 183 | 14:20 | DWYER IC | *confirmed, unchanged* | *"And I don't want you to do that now, which is what you're launching into."* |

⚠ Segments 863 and 864 each contained **two speakers in one segment**. They were split and the
boundary timestamp interpolated; the surrounding timings are unchanged.

**C. Nineteen resolved by question-and-answer structure** — a judge does not ask and answer his own
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
- ⚠⚠ **Only eleven segments were ever re-examined.** Across the file there are roughly **75 segments
  where the diariser's own speaker cluster disagrees with the label**, plus ~50 with no cluster at
  all. The ten corrections applied here are the reviewed ones. **Others may remain.** Any short
  interjection still has to be checked against who was asked the question before it is relied on.
