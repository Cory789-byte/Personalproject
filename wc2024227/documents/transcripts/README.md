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

## What was corrected (applied 15 September 2026)

| Seg | Time | Machine label | Corrected to | Confidence |
|---|---|---|---|---|
| **437** | 30:12 | DWYER IC | **MR SHEPHERD** | ⭐ **Certain** — confirmed first-hand by the Appellant, who was present |
| 440 | 30:19 | DWYER IC | MR SHEPHERD | High |
| 620 | 40:28 | DWYER IC | MR SHEPHERD | High |
| 623 | 40:30 | MR SHEPHERD | **DWYER IC** | High |
| 627 | 40:40 | MR SHEPHERD | **MS MATHESON** | High |
| 628 | 40:41 | MR SHEPHERD | **MS MATHESON** | High |
| 673 | 42:59 | DWYER IC | MR SHEPHERD | High |
| 792 | 49:53 | DWYER IC | MR SHEPHERD | High |
| 1008 | 61:37 | MR SHEPHERD | **MS MATHESON** | High |
| 1009 | 61:38 | MR SHEPHERD | **DWYER IC** | High |
| 908 | 55:53 | DWYER IC | *no change* | Confirmed |
| 231–232 | 17:45 | MR SHEPHERD | ⚠ **DISPUTED — probably MS MATHESON** | ⚠ **Uncertain — do not attribute** |

**The corrections are written straight into the `speaker` field and the old labels are gone.** The
data files now contain the correct attribution and nothing else — no residual machine label that a
search could hit, and no per-segment correction metadata. The table above is the record of what was
changed; the same table appears in `TRANSCRIPT_diarised_prosody.md` and in the corrected PDF.

⚠ **Segs 231–232 are set to `SPEAKER UNRESOLVED`,** not to Ms Matheson. That correction is rated
Uncertain, so the wrong label was removed without inventing a right one. Do not attribute that line
to anyone without the certified transcript.

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
