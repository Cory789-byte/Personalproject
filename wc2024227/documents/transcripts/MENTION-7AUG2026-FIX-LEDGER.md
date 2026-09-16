# THE MENTION OF 7 AUGUST 2026 — EVERY FIX, IN ONE PLACE

**WC/2024/227 · Shepherd v Workers' Compensation Regulator · Commissioner Dwyer · 65 minutes.**
Compiled 15 September 2026. **Internal only.** Nothing in this file is quoted externally.

---

## 0. What this file is, and how its numbers were produced

Two different kinds of fix have been made to the mention, and until now they lived in nine
different files. This is the single ledger of both:

- **Part 1 — fixes to the transcript itself.** Who said which line.
- **Part 2 — fixes to the *reading* of the mention.** What the hour meant.

⭐ **Every figure in Part 1 was recomputed for this file, not copied from any summary.** The method
was to take the transcript as it stood **before any correction** — git commit `71e7169`, the last
state of `MENTION_7AUG2026_segments.jsonl` prior to 15 September — and diff its `speaker` field
against the file as it stands now, segment by segment. That is reproducible:

```bash
git show 71e7169:wc2024227/documents/transcripts/MENTION_7AUG2026_segments.jsonl > /tmp/base.jsonl
# then compare the speaker field of each id against the current file
```

⛔⛔ **Doing that surfaced three errors in the transcripts README itself, which are corrected in
§3 below.** The README's own summary of the fixes had drifted from the fixes. That is the exact
failure this whole exercise exists to stop, and it had happened again inside the fix record.

### The headline numbers, verified

| | Before | After |
|---|---|---|
| Rows in the file | 1,068 | **1,072** (four merged segments split) |
| DWYER IC | 846 | **853** |
| MR SHEPHERD | 219 | **210** |
| MS MATHESON | 3 | **9** |
| Segments reattributed | — | ⭐ **44** |
| Segments split into two speakers | — | **4** (63, 483, 863, 864) |
| Rows where the diariser's own cluster contradicts the label | **75** | **44** |
| Rows with no diariser cluster at all | 50 | 50 |

⇒ **Nothing but the `speaker` field changed, except at 863 and 864.** No text and no timestamp was
altered anywhere else in the file: verified by diffing `text`, `start` and `end` across all 1,068
original rows — only 863 and 864 differ, and only because they were split.

---

# PART 1 — THE TRANSCRIPT FIXES

## 1. The reattributions, in time order

⚠ **This table is the first 41, applied 15 September.** Three more (segs 64, 482, 483) were added the
same day by the flip-shape audit at **Part 3**, taking the total to **44**. They are listed at §17.

Generated directly from the diff. **Segment 437 is the one that matters most** and is explained in
§2.

| # | Seg | Time | Machine label | Corrected to | The line | Basis |
|---|---|---|---|---|---|---|
| 1 | 227 | 17:16.10 | DWYER IC | **MR SHEPHERD** | *I've just asked MSH. I thought that's who holds the documents.* | question-and-answer structure |
| 2 | 247 | 19:01.66 | DWYER IC | **MR SHEPHERD** | *I have asked the regulator to produce what they have.* | question-and-answer structure |
| 3 | 249 | 19:09.12 | DWYER IC | **MR SHEPHERD** | *Not those specific things, no.* | question-and-answer structure |
| 4 | 375 | 26:52.54 | MR SHEPHERD | **DWYER IC** | *Unassessed unilateral directives.* | question-and-answer structure |
| 5 | 396 | 27:44.52 | MR SHEPHERD | **DWYER IC** | *She's erratic physical* | Appellant confirmed |
| 6 | 397 | 27:46.28 | MR SHEPHERD | **DWYER IC** | *presence and* | Appellant confirmed |
| 7 | 398 | 27:48.44 | MR SHEPHERD | **DWYER IC** | *imposes unassessed unilateral* | Appellant confirmed |
| 8 | 399 | 27:50.16 | MR SHEPHERD | **DWYER IC** | *directives.* | Appellant confirmed |
| 9 | **437** | 30:12.98 | DWYER IC | **MR SHEPHERD** | *I actually understand what you're getting at.* | 12 Sep review |
| 10 | 523 | 35:28.86 | MR SHEPHERD | **DWYER IC** | *What have they disclosed to you?* | question-and-answer structure |
| 11 | 533 | 36:02.34 | MR SHEPHERD | **DWYER IC** | *Or not?* | question-and-answer structure |
| 12 | 537 | 36:10.36 | DWYER IC | **MR SHEPHERD** | *Yes, she tore it.* | question-and-answer structure |
| 13 | 552 | 36:53.32 | MR SHEPHERD | **DWYER IC** | *Do you still have a copy of that?* | question-and-answer structure |
| 14 | 554 | 36:55.72 | MR SHEPHERD | **DWYER IC** | *So that's in your documentary case.* | question-and-answer structure |
| 15 | 562 | 37:26.56 | MR SHEPHERD | **DWYER IC** | *for that stressor.* | question-and-answer structure |
| 16 | 588 | 38:59.58 | DWYER IC | **MR SHEPHERD** | *No, that's reform 29.* | question-and-answer structure |
| 17 | 613 | 40:16.64 | MR SHEPHERD | **DWYER IC** | *Is it in the form of an email?* | question-and-answer structure |
| 18 | 614 | 40:18.44 | DWYER IC | **MR SHEPHERD** | *Yes, but I've no longer got those.* | question-and-answer structure |
| 19 | 616 | 40:21.68 | DWYER IC | **MR SHEPHERD** | *I was restricted in my...* | question-and-answer structure |
| 20 | 623 | 40:30.64 | MR SHEPHERD | **DWYER IC** | *All right.* | 12 Sep review |
| 21 | 627 | 40:40.42 | MR SHEPHERD | **MS MATHESON** | *I do believe we have those,* | 12 Sep review |
| 22 | 628 | 40:41.72 | MR SHEPHERD | **MS MATHESON** | *and I do believe we've disclosed them.* | 12 Sep review |
| 23 | 633 | 41:01.20 | MR SHEPHERD | **MS MATHESON** | *I do believe that I have received those, Commissioner,* | Appellant confirmed |
| 24 | 634 | 41:03.50 | MR SHEPHERD | **MS MATHESON** | *and disclosed them.* | Appellant confirmed |
| 25 | 635 | 41:04.58 | MR SHEPHERD | **MS MATHESON** | *I would have to triple check to be...* | continues a confirmed sentence |
| 26 | 669 | 42:54.24 | MR SHEPHERD | **DWYER IC** | *Okay, but you don't know...* | question-and-answer structure |
| 27 | 671 | 42:56.50 | MR SHEPHERD | **DWYER IC** | *...to a certainty.* | question-and-answer structure |
| 28 | 700 | 44:36.32 | MR SHEPHERD | **DWYER IC** | *OK, you've got that letter?* | question-and-answer structure |
| 29 | 706 | 44:45.76 | DWYER IC | **MR SHEPHERD** | *Yeah, just that we've followed up with the health service,* | question-and-answer structure |
| 30 | 707 | 44:49.20 | DWYER IC | **MR SHEPHERD** | *or we've followed up with the manager,* | question-and-answer structure |
| 31 | 708 | 44:50.70 | DWYER IC | **MR SHEPHERD** | *and, yeah, it was just ongoing.* | question-and-answer structure |
| 32 | 730 | 45:56.16 | DWYER IC | **MR SHEPHERD** | *We didn't have one.* | question-and-answer structure |
| 33 | 779 | 49:15.48 | DWYER IC | **MR SHEPHERD** | *Well, they just said that we emailed the health service.* | question-and-answer structure |
| 34 | 819 | 51:14.94 | DWYER IC | **MR SHEPHERD** | *I haven't raised it with the QARC or anything.* | question-and-answer structure |
| 35 | 834 | 51:46.68 | MR SHEPHERD | **DWYER IC** | *In what?* | question-and-answer structure |
| 36 | 864 | 53:18.96 | DWYER IC | **MR SHEPHERD** | *things yes.* | Appellant confirmed |
| 37 | 893 | 54:47.86 | MR SHEPHERD | **DWYER IC** | *roster for the relevant period* | Appellant confirmed |
| 38 | 914 | 56:01.22 | MR SHEPHERD | **DWYER IC** | *All right.* | question-and-answer structure |
| 39 | 919 | 56:12.36 | MR SHEPHERD | **DWYER IC** | *Has our discussion* | question-and-answer structure |
| 40 | 1008 | 61:37.14 | MR SHEPHERD | **MS MATHESON** | *No.* | 12 Sep review |
| 41 | 1009 | 61:38.36 | MR SHEPHERD | **DWYER IC** | *All right.* | 12 Sep review |

**By basis:** question-and-answer structure **26** · Appellant confirmed first-hand **8** ·
12 September review **6** · continuation of a confirmed sentence **1**. Total **41**.

**By direction:** → MR SHEPHERD **16** · → DWYER IC **19** · → MS MATHESON **6**.

## 1A. The two segments that contained two speakers

The diariser had merged a question and its answer into one row. Each was split and the boundary
timestamp interpolated; the surrounding timings are untouched.

| Row | Time | Speaker | Text |
|---|---|---|---|
| 863 | 53:14.74–53:15.64 | DWYER IC | *"holidays?"* |
| **8631** *(new)* | 53:15.64–53:18.96 | **MR SHEPHERD** | *"There's probably a few"* |
| 864 | 53:18.96–53:19.96 | **MR SHEPHERD** | *"things yes."* |
| **8641** *(new)* | 53:19.96–53:22.68 | **DWYER IC** | *"Well probably or is because disclosure is about what you know"* |

⚠ The two new rows carry ids **8631** and **8641** — deliberately out of the 0–1067 range so a
split row can never be mistaken for an original segment.

## 1B. Segments examined and left alone

Being checked and found correct is a result, and it is recorded so nobody re-opens them.

| Seg | Time | Stands as | Why it was checked |
|---|---|---|---|
| **183** | 14:20 | DWYER IC | *"And I don't want you to do that now, which is what you're launching into."* — **Appellant confirmed it as the bench.** Cluster `spk=1` at only 0.5 confidence, so it was flagged |
| **429** | 29:37 | MR SHEPHERD | *"we're now not even contacting them by their numbers"* — the closing link of the clinical chain. **Appellant confirmed it as his.** It sits inside a Dwyer run, which is the classic misattribution shape |
| **908** | 55:53 | DWYER IC | *"Okay."* — no cluster at all; reviewed 12 September and left |
| **231, 232** | 17:45 | MR SHEPHERD | *"There has been some emails to involve the quality of the staff… consider that."* — **Appellant confirmed both as his.** 232 has no diariser cluster. ⚠ See §3(c): these were never mislabelled in the data |
| **440, 620, 673, 792** | various | MR SHEPHERD | Short affirmatives. ⚠ See §3(b): corrected in the PDF rendering, already correct in the data |
| **863** *(head)* | 53:14 | DWYER IC | The question survives the split unchanged |

---

## 2. ⛔⛔ Segment 437 — the fix that changed the meaning of the hour

**At 30:12.98, after the bench had redirected him, the line is:**

> ⭐⭐ **MR SHEPHERD: *"I actually understand what you're getting at."***

The machine gave it to the bench. **It is the Appellant's**, and he confirmed it first-hand as
someone who was in the room. The corrections table in
`MENTION_7AUG2026_TRANSCRIPT_diarised_CORRECTED.pdf` had already recorded it on 12 September at
confidence **Certain**. The diariser's own cluster field agreed the whole time: `spk=0`
(the Appellant's cluster) at `conf=1.0`, sitting inside a run of `spk=1`.

**Why the error mattered.** Attributed to the bench, the line reads as a judge summarising himself.
Attributed correctly, it is **the appellant accepting a method on the record** — the method stated
forty seconds earlier:

> *"if you give evidence that you were sent unassessed directives … and the regulator doesn't
> contradict it, doesn't cross-examine you, doesn't produce documents for you to comment on …
> that's a problem for them, not for you."*

⇒ **That is the turning point of the mention, and it is his move, not the bench's.** What follows
is continuous with it: the 64G and the outstanding Form 29 items withdrawn **10 August**; the notice
to admit 303 facts served **28 August**; **298 admitted and none denied, 8 September**; the footing
letter of **9 September** relying on the admissions as acts, so the steps are proved without a
witness. He accepted the method at 30:13 and executed it over five weeks.

⛔ **How the error was made, stated plainly.** The corrected attribution had been settled on
12 September and written into the PDF's corrections table — but the table was at the top of the file
and the *body* still carried the machine label, and the `.jsonl` had not been patched at all. The
analysis was run off the raw `.jsonl`. **The fix existed and was not read.**

---

## 3. ⛔ Three errors found in the transcripts README while compiling this

The README is the rule file. It carried numbers that the data does not support. All three are now
corrected there, and they are recorded here so the correction is traceable.

**(a) "Thirty-eight segments were reattributed" — wrong. The verified figure is 41.**
The count appears to have been carried forward from an intermediate commit (`3607f63`, 35 segments)
plus the three Matheson segments added at `69b4364`, and never recomputed against the file.

**(b) "440, 620, 673, 792 → MR SHEPHERD" — these were never mislabelled in the data.**
All four already carried `MR SHEPHERD` in the raw `.jsonl`. They were corrections to a **different
machine baseline** — the diarisation pass behind the PDF, produced by `diarise_inferential.py`,
which labelled some segments differently from the `.jsonl`. ⭐ **There are two machine baselines in
this matter, not one.** A "correction" recorded against the PDF is not necessarily a correction to
the data, and vice versa. That distinction was never stated, and it is why (a) drifted.

**(c) "231–232: unattributed → MR SHEPHERD" — they were not unattributed.**
Both carried `MR SHEPHERD` as their label. What 232 lacks is a diariser **cluster** (`spk=-1`).
The README conflated *no cluster* with *no label*. The Appellant's confirmation still matters — it
converts a label the machine could not support into a fact — but no reattribution occurred.

⚠ **And "nineteen resolved by question-and-answer structure" understates it: the figure is 26.**

---

## 4. The residual risk, measured

The fixes did not make the transcript safe. They made it measurably safer, and the remainder is
now quantified rather than guessed.

| | Count | What it means |
|---|---|---|
| Rows where the diariser's cluster still contradicts the label | **45** | was 75. **32 of the 41 fixes came out of that set** |
| Rows with no diariser cluster at all | **50** | the machine expressed no view; the label is inference only |
| Rows where a fix was applied *against* the cluster | **2** — segs 399 and 864 | ⭐ deliberate. Both are Appellant-confirmed. **A person who was in the room outranks the machine** |
| Long turns where content markers conflict with the label | **0 of 1,068** | ⇒ every substantive analysis of who said what at length is unaffected |

⇒ **43 of the original 75 disagreements plus 2 new ones = 45.** The arithmetic closes; nothing is
unexplained.

⛔⛔ **The standing rule, which exists because it was broken:** *never attribute a short line —
"Yeah", "Yes", "No", "All right" — from machine output alone.* The documented failure mode is that
**a short acknowledgement inside a long run is given to whoever holds the floor.** Almost every fix
in §1 is exactly that shape.

⛔ **None of these transcripts is certified.** Speaker accuracy measured at 90% on 30 hand-checked
anchor turns. **Order the certified transcript before any passage is quoted in a filing, a letter,
or to the Commission.**

---

# PART 2 — THE FIXES TO THE READING OF THE MENTION

Ten corrections to what the hour was understood to mean. Each is stated as: what was said, what is
right, and what it changed.

## 5. ⛔⛔ A fabricated quotation — the worst of them [corrected 15 Sep]

**What was said.** That the bench said the health service would *"engage HopgoodGanim"*. Quoted
twice, as the bench's own words.

**What is right.** ⛔ **The transcript contains no firm name.** The audio at **31:34** renders:

> *"because I'd imagine the health service will probably want to engage **aged ground law** and
> they'll bring their lawyers along and I'll allow that"*

An unclear phrase was pattern-matched to a firm name that already existed elsewhere in the
repository, and written as a direct quotation.

**What it changed.** The name is marked **unestablished** in both files. ⚠ The collateral risk was
real: `HOPGOODGANIM-QUESTION.md` concerns that firm's position on **WorkCover Queensland's** panel —
the insurer side, not Metro South. Importing the name into the bench's mouth would have joined two
unrelated threads on a mis-hearing. ⭐ And no external firm ever acted: Metro South ran the objection
**in-house throughout** (Ms Ruttan, Principal Lawyer, Health Law).

⇒ **New standing rule, second limb of the HopgoodGanim rule:** *ask, never allege* — **and never put
a name in anyone's mouth from an unclear recording.**

## 6. ⛔⛔ The clinical moment was read as one adverse event. It is a registration arc [corrected 15 Sep]

**What was said.** That the 5.74-second pause at 29:46, and the redirect that followed, were the
bench shutting the patient-safety material down.

**What is right.** The arc starts two minutes *before* the pause and runs to the end of the hour:

| Time | What happens |
|---|---|
| **27:33** | ⭐ **Permission granted, unprompted:** *"If you think it's in a patient safety environment, **you can raise that**. Anyway, let's not get into the case."* |
| 29:37 | The Appellant's clinical chain — *"we're now not even contacting them by their numbers"* |
| **29:46** | **the 5.74 s silence** |
| 29:46 | *"I'm concerned at the direction this is going in, Mr Shepherd"* — ⭐ concern about **direction**, not about subject |
| **30:13** | ⭐⭐ **MR SHEPHERD: *"I actually understand what you're getting at."*** (§2) |
| 30:27–30:58 | ⭐ Work put on the other side: *"the party should work very hard at formulating a bundle of documents that **might satisfy you**"* · *"you've got a bit of work to do down there at the bar table"* |
| 57:45 | ⭐ *"and **you may be right** about all of that"* |
| 62:28 | ⭐ *"you might be **on to something there**"* |
| 63:07 | ⭐⭐ *"that particular point is **the one area** I think in all of what we've been through that there might be something to look at"* |

⇒ **What was stopped was re-arguing the case orally at a mention, mid-way through a disclosure
application — not the concept.** A judge who had dismissed the material does not return to it four
times.

## 7. ⛔ The mention was read as tuition. It was a case-management address with both opponents present [corrected 15 Sep]

**What was said.** That the hour was the bench teaching an unrepresented appellant.

**What is right.** **Ms Matheson was in the room, on the record, and answered from the bar table**
(*"Yes, Commissioner. We've disclosed all we have currently."*). Metro South was required to attend.
Everything said was heard by the people who decide whether to defend.

| What Dwyer said | Who it was really for |
|---|---|
| *"the presence or existence of an injury … is usually not so much in dispute … **as you do in this particular case**"* | the Regulator: the diagnosis is not a live contest |
| *"the real crux … how certain events … **were significant contributors**"* | the Regulator: this is the only ground you have |
| *"if you say something and **it's not contradicted** … there's a likelihood that it'll be accepted"* (twice) | the Regulator: silence costs you |
| *"**I would have thought the regulator will call Ms Taylor**"* | the Regulator: name your witnesses |
| *"**I would have thought the regulator would be all over that**"* | the Regulator: chase the material yourself |
| *"resolved sooner rather than later … for **the people of Queensland who are resourcing these proceedings**"* | a publicly funded respondent: cost |

⭐ **And the firmness toward the Appellant did work in that room.** A member who pressed only the
Regulator would look partisan and his signals would carry no weight.

⇒ Measured against *"I would have thought the regulator would be all over that"*: five weeks later
the Regulator admitted 298 facts, denied none, served no expert report, and **could not confirm its
witnesses**.

## 8. ⛔ "The material thing was the injury" — a half-answer. He was injured **and** sacked [corrected 15 Sep]

**What was said.** That the material consequence making ordinary non-compliance examinable was the
injury itself.

**What is right.** Dwyer's own test names two examples:

> *"it's only a problem if **somebody gets sacked** or somebody gets killed … And it's only then
> when these things get a light shone on them and they become relevant."*

**Both are facts of this matter.** Employment ceased **9 October 2024** by an abandonment-of-
employment letter, backdated to the day after the WorkCover decision, later overturned, with
**reinstatement to his employment with an effective date of 20 September 2024**. The materiality
threshold is met **literally, not by analogy**.

⚠ **And the sharp part.** Dwyer read him at the mention as carrying *"a broader grievance …
that systemically, the place in which you worked had a number of failings"* — because the pleaded
case is the 2024 stressors and the dismissal is deliberately kept out of them. **The discipline that
keeps the dismissal out of causation is the same thing that let the bench read him as a
grievance-holder.** That is a real cost of the discipline, and it should be known rather than
discovered.

⛔ **The discipline does not change.** The dismissal post-dates the 18 June 2024 onset, cannot bear
on causation, and pressed as a stressor invites characterisation as management action under
s 32(5)(a). It belongs to aggravation and prognosis. TD/2024/110 stays out of WC filings; deed terms
are never discussed. ⭐ **And it does not need pleading** — the Respondent's own Form 24 response at
row 36 quotes Dr Krishnaiah's reference to *"disputed unfair dismissal proceedings"*.

## 9. ⛔ The costs warning — who it was actually addressed to [corrected 15 Sep]

**What was said.** Loosely, that the bench warned "the parties" about costs.

**What is right.** **Two sentences, two addressees, and the pronouns settle it.**

- **To the room** [30:57]: *"you've got a bit of work to do down there at the bar table"* —
  collective, about negotiating a bundle.
- **The costs passage** [31:01–32:00] — **second person singular, seven times, all to him**:
  *"if **you** can't be disavowed … whether **you're** entitled … unreasonable for **you** to
  require the health service … **if you want it to be** … a lot of items in **your** list …
  **if you want it, you can have it**."*

⇒ **Not one second-person reference in the costs passage is to the Regulator or to Metro South.**
The bar-table remark was to the room; **the costs warning was to him alone.**

**And what the rules actually provide:**

| Provision | Effect |
|---|---|
| **r 64G(3)** — *"each party to an application to decide an objection must bear the party's own costs"* | ⭐ **the default on a 64G is own costs.** A non-party's fees in resisting are, by default, its own |
| **r 64I(1)** — *"Subject to rule 64G(3), the party must pay the non-party's reasonable expenses of producing a document"* | the real exposure — but **expenses of production**, and only **if production is ordered**, i.e. only if he wins |
| **WCRA s 558(3)** | the substantive appeal, not the interlocutory |

⇒ The chain as delivered was *they will engage lawyers, therefore cost consequences*. Under
r 64G(3) that does not follow by default. ⚠ **This is not a criticism** — the tribunal *may* order
otherwise, and an unsuccessful applicant who has put a non-party to thousands of documents' work is
precisely the discretionary case. The warning was of a **real discretionary risk, stated at the top
of its range, without the default beside it**, to a litigant in person, at the moment he was being
steered off the application.

## 10. ⛔ Matheson was not "left out" of the 64G. She had no formal role in it [corrected 15 Sep]

**What was said.** That the bench left the Regulator out of a hearing she had been ordered to attend.

**What is right.** The application was **the Appellant's against a non-party**. Metro South was the
objector; the Regulator had no formal role in it at all. **She was the audience, not an omission.**
The structural read that follows: **r 64F stayed the notice for 66 days and the objection was never
determined** — the bench had held since mid-June that it could not be decided on the papers, yet
listed a mention rather than a hearing, parked the application at 2 minutes 29, and never returned
to it. **The objector and the respondent together spoke under 1% of a hearing listed on the
objector's own objection.**

## 11. ⛔ A history-list note is not a diagnosis [corrected 15 Sep]

**What was said.** That the Regulator's February 2026 denial about **26 October 2022** anxiety/ADHD
entries put a pre-existing psychiatric condition genuinely in issue.

**What is right.** They are **past-medical-history list entries** carried on Dr Zhao's **referral
letter of 16 May 2024**. Not a diagnosis, not a consultation record, not a treatment episode.
"Anxiety" as a history notation is not a psychiatric disorder; ADHD is neurodevelopmental, not
depression. The injury is **Major Depressive Disorder with anxious distress**.

**The same record answers it three times, all served 9 September:** (i) **16 Nov 2023** —
*"no psychological illness such as depression or psychosis"*, poor sleep attributed to **shift
work**; (ii) the 16 May 2024 referral itself lists medications, **none an antidepressant or
anxiolytic**; (iii) **Dr Hawes, 1 July 2024** — *"there was no pre-existing factor or condition"*,
maintained in all later certificates.

⭐⭐ **And their own conduct runs against them:** the Regulator's Form 29 to the practice was scoped
**01/01/2023–01/08/2024**. The 2022 entries were **never within that scope**. They inferred a
condition from a list they never obtained.

⛔ **What is unchanged, and it is the point:** ¶1.2 of the live Form 9A tags *"clean psychiatric
baseline"* as *"(Admitted Fact: Form 24, Para 34)"*. **The defect is the assertion of admission, not
the merits of the baseline.** See §14.

## 12. ⛔ Paper handed up — he asked leave first [corrected from the audio]

**What was said.** That he handed up paper unprompted, thirty seconds after the bench complained
about volume.

**What is right.** [22:11] ***"Can I give you these two pieces of paper?"*** → [22:13] Dwyer:
***"Hand it up, please."***

⇒ ⭐ **He sought leave and it was granted** — not an appellant compounding an overload complaint,
but one asking permission and receiving it. Seg **314** carries `MR SHEPHERD` in the data; ⚠ the
PDF's diarisation had given [22:11] to Dwyer. Another instance of the two-baseline problem at §3(b).

## 13. ⛔ 29:17 is not five items side by side [corrected 13 Sep]

**What was said.** That the clinical passage was five coordinated units delivered in one breath.

**What is right.** One structure: **context → consequence.** The context (the manager not present;
the contact list not updated) was set in the preceding exchange; the five clauses are that context's
consequence spelled out. **The surface syntax is chained; the logic underneath is nested.**

⇒ The chaining is in the delivery, not the thinking — the same finding as *concept faster than
sentence*. **For the box:** state the premise aloud before the consequences every time, even when it
was said a moment ago. *A listener without the premise hears a list. A listener with it hears a
cause.*

## 14. ⛔ Three claims about the mention that overstate themselves, corrected and held

1. **Dwyer did not say this case would be hard to prove.** He said causation is *"the real crux"* in
   cases of this type, and that the diagnosis here is not much in dispute. He was locating the
   contest for **both** sides. What he doubted was whether an unrepresented appellant would tell the
   relevant from the irrelevant — **and that prediction was defied.**
2. **The admissions prove the acts. They do not prove causation.** 298 admitted facts establish that
   steps were taken on dates in terms. The bridge to the condition is medical and is **not closed**:
   Krishnaiah declined to provide a report on 5 September, no expert report has been served, and
   element (d) runs on the treating records plus oral evidence. The schedule sets the bridge up; the
   witness box finishes it.
3. **Nothing has been found by anybody.** *"Undismissable on the served record"* is not a result.
   The s 32(5)(a) exclusion remains the Respondent's to run.

⚠ **And two further limits held throughout.** A mention is not a ruling; these were indications given
while explaining process. **Under Appeal Guide 7.1 the Member who chairs the conference does not hear
the appeal**, and Dwyer has said nothing about the merits.

---

## 15. Rules that exist because of these fixes

1. ⛔ **Never attribute a short line from machine output alone.** Check who was asked the question.
2. ⛔ **Never put a name in anyone's mouth from an unclear recording.** (Second limb of *ask, never
   allege*.)
3. ⛔ **There are two machine baselines** — the `.jsonl` and the PDF's diarisation pass. Say which
   one a correction is against.
4. ⛔ **A correction at the top of a file does not fix the body of the file, or any other file.**
   Propagate it everywhere, or it will be read back as fact.
5. ⛔ **Recompute a count before repeating it.** Three of the numbers in the fix record were carried
   forward from an intermediate state and were wrong (§3).
6. ⛔ **Order the certified transcript before anything is quoted externally.**

---

## 16. ⚠ What is still open

- **The certified transcript.** ATR0282381 is audio-only and stalled. Everything here is machine
  output.
- **45 rows** where the diariser's cluster still contradicts the label, and **50** with no cluster.
  All short turns. Not reviewed individually.
- **[09:06], the answer to the AI question.** Rendered *"Just to the end, I do it all myself"*; the
  first clause is unrecoverable. ⚠ Worth having right from the certified transcript — candour to the
  Commission is not a thing to be wrong about by accident.
- **Ms Ruttan** does not register acoustically at all. Addressed once at seg 1010 (*"And Ms.
  Rutland, any?"*, name mis-transcribed); **no answer is on the tape.** The 0% share appears correct
  but is unconfirmed.
- **The appearance announcements are not on the recording** — it begins mid-sentence inside Dwyer's
  opening remarks. Speaker identities are inferred, not taken from the parties naming themselves.
- ⛔⛔ **The Second Amended Form 9A remains unserved** (§11). The live 8 April 2026 pleading carries
  five false *"Admitted Fact"* tags. The fix exists at
  `drafts/out/FORM9A_SECOND_AMENDED_FOR_FILING.pdf`. **Their outlines are due 30 September.**

---

# PART 3 — THE FLIP-SHAPE AUDIT

> **The question put on 15 September: are the reattributions a full flip of the speakers?**
> Answered from the data, not from impression.

## 17. ⭐ The answer: full flip per segment, **not** a full flip of the transcript

**Per segment — yes.** Every one of the 44 is a complete reassignment: the line moves wholly from
one mouth to another. There is no partial or hedged attribution anywhere in the file.

**Across the transcript — no, and the measurements say so plainly:**

| Test | Result | What it rules out |
|---|---|---|
| Worst 20-segment window | **7 of 20 flipped** (35%) | never a majority anywhere |
| Worst 5-minute block | **14.7%** (40–45 min) | no wholesale inverted region |
| Blocks with **zero** flips | **0–5, 5–10, 10–15, 20–25 min** | the first 25 minutes are almost untouched |
| Consecutive runs flipped together | **31 runs; 25 of them a single segment** | not block drift |
| True adjacent swap pairs (a question and its answer exchanged) | ⭐ **1** — segs 613/614 | the machine was not systematically trading turns |
| Median length of a flipped segment | **5 words** (file median 8); **24 of 41 were ≤5 words** | it is the short-turn failure, as documented |

⇒ ⭐⭐ **The error was never "the speakers are swapped". It was "a short line inside a long run went
to whoever held the floor" — 21 of the 41 sat exactly there.** That is why the fixes are scattered
and short, and why every long turn survived untouched (**0 conflicts in 1,068 long turns**).

**But there is one true thing in the full-flip reading, and it should be held:** the flips are
**directionally clustered by region**, which is not random noise.

| Block | Flips | Direction |
|---|---|---|
| 15–20 min | 3 | ⭐ **all** DWYER → SHEPHERD |
| 25–30 min | 5 | ⭐ **all** SHEPHERD → DWYER |
| 40–45 min | 15 | fully mixed — **and the only block with a third speaker in it** |

⇒ The diariser locks onto the wrong cluster for a stretch and then recovers. **40–45 minutes is the
disordered zone** — it is where Ms Matheson speaks, and the diariser has **no Matheson cluster at
all**, so her six segments were dealt out to the other two.

## 18. ⭐⭐ The audit found three more, and two are now fixed

Running the same test over the regions that were **never reviewed** turned up four candidates of
exactly the 437 shape. Two are certain on the structural basis already used for 26 other segments —
*a judge does not ask and answer his own question* — and are **applied**. Two turn on a sentence
that spans a speaker change and **need confirmation**.

### ✅ APPLIED — 06:39, segment 63 split and segment 64 reattributed

The bench asked the question and the machine gave him the answer as well:

| Was | Now |
|---|---|
| DWYER: *"…Do you have any questions or difficulties understanding all of that **at the moment? No, I mean, you're telling me, so I'm not experienced in it, but I just did what I understood.**"* | DWYER: *"…at the moment?"* → ⭐ **SHEPHERD: *"No, I mean, you're telling me, so I'm not experienced in it, but I just did what I understood."*** → DWYER: *"That's okay. I want to stress… I'm not being critical of you, Mr Shepherd"* |

⭐ **No judge says "I'm not experienced in it".** And there is a **1.12-second silence** between
*"moment?"* and *"No,"* — the longest gap in the passage, and the split boundary.
⚠ **This is the Appellant's first answer of the hearing on the record**, and it was attributed to the
bench.

### ✅ APPLIED — 32:24, segment 482 reattributed and 483 split

| Was | Now |
|---|---|
| DWYER: *"have, have you had"* → SHEPHERD: *"constructive discussions with / **them?** We have not / not like a constructive discussion"* | DWYER: *"have, have you had **constructive discussions with them?**"* → ⭐ **SHEPHERD: *"We have not, not like a constructive discussion."*** |

The question had been broken across two speakers mid-clause.

### ⚠ OPEN — two that need the Appellant's confirmation

**(a) Segment 69, at 07:09 — ⭐⭐ the mirror image of segment 437.**

> 68 **DWYER**: *"…how this impacts the efficient conduct of the proceedings."*
> 69 **labelled MR SHEPHERD**: *"I understand, I think I understand, what you think you are trying to achieve **and I'm not**"*
> 70 **DWYER**: *"**saying you are entirely wrong** and the thing with disclosure is that if…"*

⛔ *"and I'm not"* + *"saying you are entirely wrong"* is **one clause spanning 69 into 70**. A clause
cannot change speaker mid-way. So either **all of 69 is the bench**, or the boundary sits **inside**
69 (*"I understand, I think I understand"* his, the rest the bench's). The cluster says DWYER at 0.64.

⭐⭐ **Why this one matters more than its length.** Segment 437 — the fix that changed the meaning of
the hour — is *"I actually understand what you're getting at"*, and the error there ran **Shepherd
→ wrongly labelled Dwyer**. Segment 69 is the same phrase family running **the other way**. If 69 is
the bench, then the *"I understand"* register belongs to both men and 437 stops being distinctive.
**If 69 is his, he said it twice — at minute 7 and at minute 30 — and the second time it was
accepted.** ⛔ Not resolvable from the machine. It needs the man who was in the room.

**(b) Segment 72, at 07:25.**

> 71 **DWYER**: *"…someone's willing to give you some documents you've asked for **and they**"*
> 72 **labelled MR SHEPHERD**: *"**don't have any problem with it** that's fine I don't have a problem with that"*

Same defect: *"and they"* + *"don't have any problem with it"* is one clause across the boundary. The
first half must be the bench. *"I don't have a problem with that"* may be either.

## 19. ⛔ A correction to the fix record itself — the word-level confidences were there all along

`THE-MENTION-THEORY-OF-MIND-15SEP2026.md` §8.1 records that the *"aged ground law"* segment
*"carries a good overall transcription score (avg_logprob −0.155) but **no word-level
probabilities**"*. **That is wrong. Every word in the file carries one**, in the `p` field of the
`words` array. Reading them changes what can be said about that passage:

| Word | Confidence |
|---|---|
| …want to **engage** | 1.00 |
| ⛔⛔ **aged** | ⭐⭐ **0.02** |
| **ground** | 0.78 |
| **law** | 0.84 |
| and they'll bring their **lawyers** along | 0.97 – 1.00 |

⇒ ⭐⭐⭐ **The model itself was 98% unsure of that word, and every word around it is near-certain.**
The transcript was flagging its own guess, at the exact point where a firm name would sit, and
nobody looked at the flag before a name was written into the bench's mouth.

⛔ **This does not reopen the name — it closes it harder.** A 0.02 rendering is not evidence of what
was said; it is evidence that **the audio there cannot be read**. The firm, if one was named, remains
**unestablished**, and only the certified transcript can settle it.

⭐ **The rule this yields:** *before relying on any phrase that carries weight, read the per-word `p`
values.* They were free, they were in the file, and they would have stopped the error on their own.

## 20. Housekeeping — the split-id scheme, made collision-proof

The first two splits took ids **8631** and **8641** (parent + "1"). ⚠ That scheme **collides**: under
it segment 63 would produce id 631, which is an existing segment. All split children are therefore
renumbered on one rule:

> ⭐ **a split child's id is `100000 + parent id`.** Any id ≥ 100000 is the second half of a split
> segment; subtract 100000 for its parent.

| Parent | Child | Time | Speaker |
|---|---|---|---|
| 63 | **100063** | 06:40.80 | MR SHEPHERD |
| 483 | **100483** | 32:27.38 | MR SHEPHERD |
| 863 | **100863** *(was 8631)* | 53:15.64 | MR SHEPHERD |
| 864 | **100864** *(was 8641)* | 53:19.96 | DWYER IC |

## 21. Where the remaining risk now sits

The audit moved the residual from a guess to a map. **44 rows** still carry a cluster that
contradicts their label — but the cluster is demonstrably unreliable, so that is an **upper bound on
risk, not a count of errors**: seg 188 (*"What do you mean by that, Mr Sheppard?"*) is flagged, and
is obviously the bench.

| Block | Flagged rows | Reviewed? |
|---|---|---|
| **30–35 min** | ⚠ **9 of 81** | ⛔ **no** — and this is the block containing segment 437 |
| **5–15 min** | ⚠ **13 of 151** | ⛔ **no** — it produced both fixes at §18 and both open items |
| 40–45 min | **1 of 102** | ✅ yes — reviewed hard, now the cleanest block in the file |

⇒ ⭐ **The next review, if one is done, is 5–15 minutes and 30–35 minutes.** The 5–15 block has
already yielded two applied fixes and two open questions from a single pass, which is the highest
error density found anywhere.
