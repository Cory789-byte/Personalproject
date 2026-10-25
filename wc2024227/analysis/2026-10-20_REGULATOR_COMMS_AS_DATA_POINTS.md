# The Regulator's communications as data points: words and structure, 23 communications (20 Oct 2026)

> Internal. Prediction only. Small numbers; read the pattern, not any single count.
> - **Script:** `analysis/stylometry/regulator_features.py`.
> - **Data:** `regulator_comms_features.csv`.
> - **Output:** `regulator_features_output.txt`.

**Data.** Every Regulator communication held in full, July 2025 to 20 Oct 2026: 22 emails and the 8 Sep
letter.
- **Split:** 11 before the notices to admit (28 Aug), 12 after.
- **Word features:** counted by fixed rules (in the script).
- **Structural features:** coded by stated rules (in the script):
  - gives something;
  - asks;
  - defers;
  - latency;
  - compose time.

## Findings

| Feature | Before (n=11) | After (n=12) | Note |
|---|---|---|---|
| "Defend" statement ("we will be defending the appeal"; "position remains to defend") | **3** | **0** | All three earlier ones were at decision points (Calderbank #1, Calderbank #2, the WP letter). p ≈ 0.09 |
| Apology | **4** | **0** | p ≈ 0.04 |
| Either of the two above | 7 | 0 | p ≈ 0.001, but the grouping was chosen after looking |
| Legal reservation or legal idiom | 0 | **3** | 8 Sep letter, 12 Oct Registry email, 16 Oct |
| Warmth ("thank", "thankfully", "appreciate", "assistance") | 3 | 5 | 4 of the last 5 emails |
| Dated promise ("respond by… as requested") | 0 | 1 | First ever, 20 Oct |
| Defers an answer | 1 | 4 | Becomes a routine move |
| Gives something | 6 | 9 | Give first |
| **Merits words** ("reasonable", "management action", s 32, causation, stressor) | **0** | **0** | **0 of 23.** Before, the defence was asserted only by pointer ("as outlined in our SOFC"). With the pointer gone, nothing in their correspondence asserts a defence |
| "Exit" words ("review its position", "consent orders", "without admission") | 0 | 0 | Not yet |
| Median latency (days) | 10 | 9 | **No change across the phase.** The speed-up is in the last week only: 6 days, then 17 h 40 min |

**The position slot.** This is the sentence where they say where they stand.

| Date | Content of the slot |
|---|---|
| 18 Feb | "we will be defending the appeal" |
| 16 Jul | "position remains to defend… as outlined in our Statement of Facts and Contentions" |
| 14 Aug | the same, with "As mentioned previously" |
| 8 Sep | admissions "for the purposes of rule 49 only"; de novo; "reserves the right" |
| 24 Sep | "reserves its right to amend this list" |
| 12 Oct | "would be better placed to be discussed at the conference in lieu of ordered in directions, in the first instance" |
| 16 Oct | the reservation re-attached |
| 20 Oct | "respond by Friday 30 October 2026 as requested" |

The decision points still occur. Since the admissions, the slot has been filled by a reservation, a deferral
or a dated promise, never by "defend".

**Compose time** (new emails only):
- typed live: 101–549 s;
- pasted: 20 s (24 Sep) and 10 s (12 Oct), both decision emails;
- left open for 97 minutes: the witness list.

**Correction.** "Faster since the admissions" overstated it. The median latency is unchanged. The speed-up
began about 16 Oct.

## The 30 Oct reply as data point 24: what to code and what each value means

| Feature | Expected | If different |
|---|---|---|
| Arrives by 4 pm Fri 30 Oct | yes (85–90%) | Late means the routine broke; something is being decided above her |
| "Defend" statement or the formula | absent (about 85%) | **Present means the fight is back** |
| Reservation | present (about 85%) | Absent is unusual and leans toward an exit |
| Legal idiom inside her frame | present (60–70%) | Counsel settled it, so it is a decision email |
| Gives something (228–231, tender) | yes (about 70%) | Nothing given means a holding reply |
| Defers (s 32(1), leave, ¶27 to the conference) | yes (about 60%) | Fewer deferrals means the decision is being made |
| **Merits words: first appearance in 24** | see the right-hand column | Agreeing ("s 32(1) not in issue") narrows the case. Asserting ("the management action was reasonable"; "¶27 relies on…") means a fight |
| **Exit words: first appearance** | about 10% | **Decisive:** "review its position", "consent orders", "without admission" |
