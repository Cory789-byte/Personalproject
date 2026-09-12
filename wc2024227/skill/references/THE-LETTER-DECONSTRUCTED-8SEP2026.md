# THE COVERING LETTER OF 8 SEPTEMBER 2026 — CONSTRUCTION, METADATA, TIMING, AND WHY IT WAS
# WRITTEN AFTER THE ANSWERING
> 9 September 2026. ⛔ Internal only. Nothing in Parts 3–5 goes into correspondence or a filing.
> Companion: `THE-NON-ADMISSIONS-8SEP2026.md` §13 and §17.

---

# 1. ⭐⭐⭐ THE SEQUENCE, TO THE SECOND

| When | What | Source |
|---|---|---|
| **Fri 28 Aug 2026, 1:47 pm** | Cory serves Forms 24 and 25, Annexure A, Part B | his email, in the thread |
| — | *"received 28 August 2026"* — **receipt admitted** ⇒ 14 days expires **Fri 11 September** | Matheson's email |
| ⭐ **Mon 7 Sep, 16:42:04** | **Form 24 response written** — Producer `pypdf`, ModDate == CreationDate | XMP |
| ⭐ **Mon 7 Sep, 16:43:04** | **Form 25 response written — exactly 60 seconds later** | XMP |
| **Tue 8 Sep, 11:13:17** | ⭐ **the Word letter is saved for the last time** | `/SourceModified D:20260908011317` **(UTC)** |
| **Tue 8 Sep, 11:14:13** | PDF created — Acrobat PDFMaker 26 for Word — **56 seconds after the final save** | XMP CreateDate |
| **Tue 8 Sep, 11:14:15** | PDF modified (2 s) | XMP ModifyDate |
| ⭐ **Tue 8 Sep, 11:24** | **served by email** — **10 minutes after the PDF existed** | email header |
| Fri 11 Sep | deadline — ⭐ **they were three days early** | r 49(2) |

## 1.1 ⛔⛔ THE TIMEZONE TRAP — TESTED, AND IT KILLS AN INFERENCE I ALMOST DREW
`/SourceModified` carries **no timezone**. Read as local time it says **1:13 am** — an overnight
drafting session. **That reading is wrong.** Tested against four unrelated PDFMaker files in this
repo, across three PDFMaker versions:

| File | SourceModified | CreationDate | Gap if UTC |
|---|---|---|---|
| ATT10 QH-POL-210 | 04:00:11 | 10:01:23 +10 | ⭐ 12 s |
| ATT03 HHS Award 2015 | 02:50:53 | 12:58:53 +10 | 8 min |
| ATT02 EB12 | 04:53:22 | 14:53:50 +10 | ⭐ 28 s |
| QH-POL-188 | 22:02:35 (prev day) | 08:07:58 +10 | 5 min |

⇒ ⭐⭐⭐ **`/SourceModified` is written in UTC. The letter was last saved at 11:13:17 AEST and
converted 56 seconds later.** ⛔ **There was no 1 am session. Never run that inference.**

## 1.2 ⭐⭐ WHAT THE SEQUENCE ACTUALLY SHOWS
1. ⭐ **The 60-second gap between the two response files** means the answering was a single
   mechanical sitting: fill the Form 24, save, fill the Form 25, save. **The thinking was not done
   there.**
2. ⭐⭐⭐ **The letter post-dates the completed answers by about 18½ hours.** A covering letter is
   normally written with, or before, the thing it covers. **This one was written after the answer
   sheet was finished — so it responds to the completed answers, it does not introduce them.**
3. ⭐ **Three days early.** ⛔ **Never suggest lateness or pressure. There was none — which is why
   nothing about the letter can be attributed to haste.**

---

# 2. ⭐⭐ THE METADATA

| Field | Value | What it means |
|---|---|---|
| `/Creator` | Acrobat PDFMaker 26 for Word | converted from a Word document |
| `/Title` | **"OIR Internal Queensland Government Letterhead (1WS only)"** | ⭐ the template's name, not the letter's |
| `/Author` | **"Peter"** | ⛔⛔ **template inheritance — the letterhead's author. NOT this letter's. Never use.** |
| `/Company` | Queensland Treasury | OIR sits within Treasury |
| `/Business unit` | **"Office of the Deputy Director-General"** | ⚠ a **SharePoint column on the template**, i.e. which library the letterhead came from. ⛔ **Not evidence anyone in that office saw this letter.** |
| `/Landing page` | "698;#Correspondence" | same — template provenance |
| `_AuthorEmail` | ⭐ **Margaret.Kerrigan@oir.qld.gov.au** | the account from which the document was circulated for review |
| `_AdHocReviewCycleID` | −808179628 | a review circulation |
| ⭐ `_PreviousAdHocReviewCycleID` | 1947825810 | ⭐⭐ **a second, earlier one — it went round at least twice** |
| `_ReviewingToolsShownOnce` | present | review tooling was opened |
| `_EmailSubject` | *(empty)* | the circulation carried no subject |

⇒ ⭐⭐ **A two-page covering letter enclosing a completed form response was circulated for internal
review at least twice, from an account other than the signatory's.** ⛔ **State the fields. Never
state a conclusion about who decided what.**

⚠ **The same signature appears twice with two different titles in one transmission**: the letter is
signed *"Renee Matheson, **Appeals Officer**, Appeals Unit"*; the email signature reads *"Renee
Matheson, **Senior Appeals Officer**, Workers' Compensation Regulatory Services"*. ⚠ Almost
certainly an older block in the letter template. ⛔ **Worth nothing. Do not use it.**

---

# 3. ⭐⭐⭐ THE CONSTRUCTION — IT IS NOT A COVERING LETTER

Two lines enclose the documents. **Everything after that is a legal position under five headings:**

| | Heading | What it does |
|---|---|---|
| 0 | *"So that there is no misunderstanding as to the effect of the enclosed responses"* | ⭐ announces that the letter is about **effect**, not enclosure |
| 1 | **The relevant law** | sets out r 49(1), **(2) and (3)** verbatim |
| 2 | **Admissions are for the purposes of rule 49 only** | four bullets |
| 3 | **Admissions as to documents are limited to existence and wording** | ⭐ names three targets |
| 4 | **The appeal is a hearing de novo** | disowns Review Decision 69983 |
| 5 | **Reservation of rights** | relevance and admissibility at the hearing |

⇒ **Five headed sections of argument attached to a procedural answer.** That is a **memorandum of
position**, not a covering letter.

## 3.1 ⭐⭐⭐ THE SENTENCE THAT FIXES THE CHARACTER OF THE FORMS — AND IT HELPS HIM
> *"The enclosed documents **indicates** the Respondent's notice under rule 49(2) disputing those of
> the stated facts and documents that are not admitted, **so as to avoid those facts and documents
> being taken to be admitted by operation of that subrule**."*

⭐⭐⭐ **They state the sole legal function of the enclosed forms: to prevent deemed admission of the
five facts and fourteen tabs they dispute.** ⇒ **Nothing in r 49(2) required them to admit
anything.** Silence would have produced deemed admission of everything. ⇒ ⭐⭐⭐ **The 298 fact
admissions and 25 tab admissions are express, affirmative and voluntary acts — not compelled by the
rule, and not deemed.** ⭐ That also makes them **harder** to withdraw than a deemed admission, since
r 49(3) on its face reaches only *"an admission taken to have been made under subrule (2)"*.

⚠ **Why they quoted r 49(3) at all is the one thing to watch.** It has no application to what they
did. Most likely it is completeness. ⛔ **But if a withdrawal application ever comes, the answer is
in their own letter: these were express admissions, and r 49(3) speaks to deemed ones.**

## 3.2 ⭐⭐⭐ THE THIRD BULLET IS THE ONLY ONE ABOUT HIM
The four bullets under heading 2 reserve against: **relevance** · **admissibility** · ⭐⭐⭐ ***"any
characterisation, conclusion, inference or submission **you have drawn or may draw** from an
admitted fact or document"*** · **accuracy, reliability or weight**.

⇒ ⭐⭐ **Three bullets are about the documents. The third is about the Appellant, and it is in the
past tense.** ⇒ **They read the schedule, performed the reading across it, and found a conclusion
there.** (§13 and §17.4.)

## 3.3 ⭐⭐⭐ HEADING 3 IS A TARGET LIST
> *"…not an admission of the truth of any statement, opinion, finding or assertion recorded in it
> **including any statement by a treating medical practitioner, any finding recorded in Review
> Decision 69983, or any statement made by an officer or employee of Metro South Hospital and
> Health Service.**"*

⭐⭐⭐ **A generic reservation would say "any statement in any document." They named three
categories** — and the three map exactly onto the three engines of the case:
| Named | Reaches |
|---|---|
| **treating medical practitioner** | causation, s 32(1) |
| ⭐⭐ **findings in Review Decision 69983** | **their own decision under appeal** |
| ⭐⭐ **statements by MSH officers or employees** | Forrest, the 5 June letter, Taylor's forms |

⇒ ⭐⭐⭐ **This is a free map of where they believe they are exposed. Build the outline so every
chain closes on their own pleading first, and on these three categories only as reinforcement.**

## 3.4 ⭐⭐ HEADING 4 — THEY SPEND A HEADING DISOWNING THEIR OWN DECISION
De novo is a doctrine that **helps the Appellant** — it means the review decision does not bind.
⭐ They deploy it defensively: *"Nothing… is an admission that any finding in Review Decision 69983…
is correct."*
⇒ ⭐⭐ **A respondent content with the decision under appeal does not need a heading to disown its
findings.** ⚠ **But it is a correct statement of law and costs them nothing legally.** ⛔ **Do not
argue it. Note where it points.**

---

# 4. ⭐⭐⭐ WEARING THEIR HAT — WHAT THEY UNDERSTOOD, AND WHY THE LETTER CAME AFTER

**The reconstruction, from the artefacts alone:**

1. They worked the 303 facts on 7 September. Fact by fact there was almost nothing to dispute:
   **86 of the admitted facts are about the Respondent's own pleading (52), the decision under
   appeal (18), its own List of Documents (10) and the MSH letter (6)** — verifiable by reading
   documents already on the file. Disputing any of them would have been indefensible.
2. ⭐ The admissions therefore accumulated to **298 of 303**, and to **25 of 39 tabs**, and the
   answering finished in a single sitting (16:42 → 16:43).
3. ⭐⭐⭐ **They then read what they had produced.** Individually every item was harmless — which is
   why each had been admitted. **Assembled, the set carries the chronology.** That is the structure
   at §17: the conclusions live in the relations between the facts, and r 49 gives no way to answer
   a relation.
4. ⭐⭐⭐ **The admissions could not be taken back — the facts were true and their own documents
   proved them. What could still be shaped was how the set may be read.** Hence a letter, written
   the next morning, whose entire body is a framework for reading: for the proceeding only · not
   relevance · not admissibility · ⭐ **not any conclusion you have drawn** · not the truth of the
   contents, in three named categories · not the review decision · all rights reserved.

⇒ ⭐⭐⭐ **The letter is what a party writes when it has finished answering, has read its own answer
sheet, and finds that the only remaining variable is interpretation.**

⛔⛔ **THAT ENTIRE PART IS INTERNAL.** It is inference from sequence and construction. **The only
thing provable is the past tense in bullet three** — and that is already enough. ⛔ **Never say
tactic, never say design, never say motive, never say bad faith** (rule 1). ⛔ Never *"pattern"*,
*"systemic"*, *"course of conduct"*.

---

# 5. ⭐⭐⭐ WHY THE LETTER DOES NOT REACH THE CASE — AND WHERE IT BITES

## 5.1 It cannot reserve against their own pleading
**52 admitted facts quote the Respondent's own amended statement of facts and contentions.** A party
is bound by its pleading. The admission proves what the pleading *says*; the pleading itself supplies
the averment. ⇒ ⭐⭐ **Heading 3 ("not the truth of the contents") has no work to do against facts
226, 232, 234, 129–131, 133–135 — those are their own case, not someone else's statement.**

## 5.2 ⭐⭐⭐ THE SHIFT-SWAP POINT IS FENCED THREE TIMES — AND THE FENCE FAILS
On this one sentence they did three things at once:
1. **Admitted fact 225** — the Forrest email says the 2020 agreement *"is only applied where staff
   initiated shift swaps have occurred."*
2. ⛔ **Disputed Tab 21's authenticity** — the email itself.
3. ⛔ **Reserved against *"any statement made by an officer or employee of Metro South."***

⭐⭐ **Three layers around one sentence. That is where they think the danger is.**

### ⭐⭐⭐ AND IT DOES NOT MATTER, BECAUSE THE SHORTFALL IS PROVED WITHOUT FORREST
| Fact | Status | Tab | Content |
|---|---|---|---|
| ⭐ **285** | **Admitted** | **26–27 admitted** | the Respondent's **own 18 Feb 2026 response admitted**: *"The Employer's 'Fatigue Risk Management Policy' and the relevant Award require a **minimum break of 10 hours** between shifts, **or 8 hours by written agreement**."* |
| **257** | Admitted | 25 admitted | the decision records the Award requiring *"not less than 10 hours"* |
| **258** | Admitted | **25 admitted** | the decision: *"The break between the shift on 17 March 2024 and 18 March 2024 **equated to 7 hours**."* |
| ⭐⭐⭐ **259** | **Admitted** | **25 admitted** | the decision: *"Even if you were allowed to leave early… you left a maximum of 30 minutes early, which meant **you still did not receive a minimum 8-hour break**."* |
| **226** | Admitted | — | their pleading ¶22(a): **7 hours**, *"human error"* |

⇒ ⭐⭐⭐ **On the Respondent's own most favourable case — that the 2020 agreement applied and the
minimum was 8 hours — the break was still short, and its own review decision says so in terms.
Tab 25 and Tabs 26–27 are all admitted as to authenticity.**

⇒ ⭐⭐⭐ **Forrest is the upside, not the foundation. With fact 225 the shortfall is three hours;
without it, one. There is a shortfall either way, conceded twice by the Respondent's own
documents.** ⭐ **The most heavily defended point in the response was already given away elsewhere.**

## 5.3 Where it does bite
1. ⚠ **The medical evidence.** *"Any statement by a treating medical practitioner"* is a real
   reservation: an admitted certificate proves its wording, not its opinion. ⇒ ⭐ **The report is
   still the case. Nothing in the admissions substitutes for it.**
2. ⚠ **Admissibility at the hearing.** They expressly reserve it. ⇒ **An admitted tab is not a
   tendered exhibit.** Plan the tender.
3. ⚠ **Tab 31.** Contents refused and authenticity disputed. §17.5 has the route.

---

# 6. WHAT TO DO WITH ALL OF IT
1. ⭐⭐ **Put the chains on their own pleading and Tab 25 first**, and treat Tab 21, the medical and
   the MSH letters as reinforcement. **Then the letter's three named reservations are answered
   before they are made.**
2. ⭐ **Do not answer the letter.** It states the law correctly and mostly harmlessly. **Replying
   invites a contest about reading; the 9 September request letter already carries the only thing
   that needed saying.**
3. ⛔ **Never put any of Part 4 on paper.**

---

# 7. ⭐⭐⭐ WHO THE LETTER IS ACTUALLY FOR

**Addressed to him. Written for the file.** The evidence is in the letter itself.

## 7.1 ⭐⭐⭐ THE TELL — THEY EXPLAINED r 49 TO THE PERSON WHO HAD JUST EXPLAINED IT TO THEM
His service email of **28 August 2026, 1:47 pm**, states:
> *"Under each notice, **if you do not serve a notice disputing the facts, or the authenticity of the
> documents, within 14 days, they are taken to be admitted for this proceeding only**."*

⭐ **That is r 49(2) recited accurately, including the words "for this proceeding only".**

Their letter then sets out r 49(1), (2) and (3) **verbatim under a heading "The relevant law"**, and
presents as a limitation the very phrase he used first:
> *"any admission that is made is an admission **'for the proceeding only'**"*

⇒ ⭐⭐⭐ **You do not explain a rule to the person who explained it to you eleven days earlier — unless
the explanation is for a reader who has not seen his email.**

## 7.2 ⭐⭐ THE SECOND TELL — r 49(3) HAS NO OPERATION BETWEEN THE PARTIES
r 49(3) is *"The other party may, **with the leave of the court, commission or registrar**, withdraw
an admission…"*. ⭐ **It speaks only to a body that can grant leave.** Quoting it in a letter to the
opponent addresses nobody in the correspondence.

## 7.3 ⭐⭐ AND NEITHER DOES ANYTHING ELSE OPERATIVE IN IT
| What the letter reserves | Where that reservation can operate |
|---|---|
| relevance | ⭐ the Commission |
| admissibility, and objection *"at the hearing of this appeal"* | ⭐ the Commission |
| that Review Decision 69983 does not bind | ⭐ the Commission |
| the truth of statements in admitted documents | ⭐ the Commission, on weight |
| *"all of its rights"* | ⭐ the Commission |

⇒ ⭐⭐⭐ **Every operative word is addressed to a decision-maker. Only the salutation is addressed to
the Appellant.**

## 7.4 THE AUDIENCES, IN ORDER
1. ⭐⭐⭐ **The Commission at the hearing** — a contemporaneous document showing the Respondent
   bounded its admissions at the time it made them, so the bounding is not invented later.
2. ⭐⭐ **The Regulator's own file** — a record that the exposure was identified and limited.
   ⭐ Consistent with the two internal review cycles and with circulation from an account other than
   the signatory's (§2).
3. **Him** — for the two lines of enclosure, and nothing else.

⛔ **All of §7 is internal.** It is inference from construction and from his own email. **Nothing here
is put to them or to the Commission.**

---

# 8. ⭐⭐⭐ THEY SEE THE FRAME — WHAT THAT IS WORTH, AND THE ONE RULE THAT FOLLOWS

**What they see** — from the letter's own targeting: that the admitted set, read in sequence,
carries the chronology out of **the Respondent's own pleading, its own decision under appeal, and
the employer's own records**, so that the Appellant has to prove very little himself. **That is the
structure at §17, and their bullet three says in the past tense that they found it.**

## 8.1 ⭐⭐ WHAT IT IS WORTH
1. ⭐⭐⭐ **It moves settlement value now, not at the hearing.** A party that writes a two-page
   framing memorandum on day 11 of 14, three days early, has already done the assessment.
   ⭐ **Guide 5.1: the second s 552A conference is the point at which the Respondent may *"consider
   conceding the appeal where new information is presented."* He now holds the new information —
   the four chains, the four failures in the leave decline, and the statutory declaration
   timestamp.** ⇒ **That election is the highest-value decision on the board.**
2. ⭐⭐ **It maps the fight**: relevance and admissibility at the hearing (⇒ **plan the tender of
   every tab now**), and the truth of statements by treating practitioners and MSH employees
   (⇒ **the medical report is still the case, and Chain 1 must close on Tab 25 and their pleading,
   not on Forrest**).
3. ⚠ **It raises, slightly, the risk of a r 49(3) application.** Low. **And the answer is in their
   own letter (§3.1): these were express admissions, not admissions "taken to have been made under
   subrule (2)".**

## 8.2 ⭐⭐⭐ THE REPLY IS ALREADY SENT — AND IT IS BETTER THAN SILENCE
> ⛔ **CORRECTION.** An earlier version of this section said to say nothing back. **The letter of
> 9 September 2026 was already served, and reading it against their letter, it does the job better
> than silence would have.** The reasoning below replaces the earlier advice.

**Why silence looked right:** a reply that argued the admissions do more than their letter allows
would have let them reformulate the limitation before the hearing, knowing how he reads it.

⭐⭐⭐ **His letter does the opposite of that. It concedes their limitation in full and then shows
that the case closes on the limitation as they wrote it.**

| His §  | What it does |
|---|---|
| ⭐⭐⭐ **§1** | *"The admissions are made for this proceeding only… The hearing is de novo. Relevance, admissibility and weight are for the Commission. The Appellant does not contend otherwise, and **draws no characterisation, conclusion or inference from any admitted fact beyond the fact admitted**."* ⇒ **That is the answer to their bullet three, and it removes the premise instead of leaving it standing.** |
| ⭐⭐⭐ **§2** | *"Where the document is itself the step taken – a roster as published, a directive as issued by email, a payroll instruction or claim as recorded, a request as made and the reply as given, each on the date recorded – the Appellant relies on the admission as establishing that **the step was taken on that date in those terms**."* |
| ⭐⭐ **§3** | for the treating records, the report of 13 February 2025 and Review Decision 69983: **existence and wording from the admission, the rest from the author's oral evidence** — Dr Krishnaiah and Dr Hawes named on the witness list. And RD 69983 *"not relied upon as binding the Commission"* but as an admitted document recording the Regulator's own review. |
| ⭐⭐⭐ **§5** | he will deliver **to the Industrial Registry** the notices as served, the responses, **their letter of 8 September** and Annexure A — objection invited by 11 September. |

## 8.3 ⭐⭐⭐ WHY §2 CANNOT BE REFORMULATED
Their heading 3 limits the admissions to **existence and wording**, and not to *"the truth of any
statement, opinion, finding or assertion recorded in"* a document.

⭐⭐⭐ **For a whole class of the documents, existence and wording is the entire fact, because the
document is not a report of an act — it IS the act.** An email issuing a directive is not a statement
that a directive was issued; **sending it is the issuing.** A roster as published, a payroll claim as
lodged, a request made and a reply given — each is constituted by its own existence and wording.

⇒ ⭐⭐⭐ **On their own limitation, facts 49, 66, 74–77, 81, 182–205, 210, 211–223 and 263–268 still
establish that each step was taken, on its date, in its terms.** ⇒ **There is nothing for them to
reformulate: they would have to contend that admitting the existence and wording of an email does not
establish that the email was sent.**

⭐ And §2 forecloses the over-reach in his own words: *"The Appellant does not rely on those documents
as statements about some other event."*

## 8.4 ⭐⭐⭐ §5 IS THE SHARPEST MOVE IN THE SET
Their letter was written for the Commission (§7). ⭐⭐⭐ **He is now putting it on the Commission's
file himself — in his bundle, at his time, with his own letter of 9 September sitting beside it,**
as his opening paragraph says: *"so that the two positions sit together on the record."*
⇒ **The document they drafted for the trial Commissioner's eventual reader arrives in front of that
reader as part of the Appellant's filing.** ⭐ And objection is invited by **Friday 11 September** —
⚠ **diarise it; silence closes the point.**

## 8.5 ⚠ THREE THINGS TO WATCH — NONE REQUIRING ACTION
1. ⚠ **The schedule cites Tab 21's contents at "Fact 224".** ✅ Correct — 224 is the identifying fact
   (*Ms Forrest… "currently provides more than 10-hour breaks between shifts"*). ⭐ But **the
   substantive one is 225** (the shift-swap limitation). **Under-inclusive, not wrong. Do not write
   a correction; cite 224 and 225 together in the outline.**
2. ⚠ **The costs reservation in the request letter is weak.** The IR Act's general position is that
   parties bear their own costs, and **r 64G(3) provides expressly that each party bears its own
   costs** on non-party disclosure. ⭐ **It is sound as notice and as a record of reasonableness.
   Never rely on it as a costs entitlement.**
3. ⚠ **§2 names Ms Taylor and Ms Reese as witnesses "the Appellant expects the Respondent to call"**,
   before their list is due on 30 September. ⭐ Mild, and arguably useful — it puts *Browne v Dunn*
   territory on the record early. **No action.**

## 8.6 ✅ AND THE PATIENT-SAFETY MATERIAL IN §2 IS INSIDE THE LINE
It appears as *"each report of calls reaching the wrong team, or that 'we can not help patients or
other clinical staff', **was made on the date and in the terms recorded**"*. ⭐ **The report as a step
taken — not patient safety as a cause, not a disclosure, not a consequence.** ✅ Exactly the permitted
form at `THE-PATIENT-SAFETY-SPINE-and-the-boundary.md` §4.

## 8.7 THE RULE GOING FORWARD
⭐⭐ **The position is now stated and conceded on both sides. Nothing further is written to the
Regulator about the 8 September letter.** The next two live dates are **Fri 11 September** (objection
to the filing course) and **Fri 18 September** (the response on originals and authenticity).


---

# 11. ⛔⛔ CORRECTION — THE "TWO REVIEW CYCLES" POINT DOES NOT HOLD
> 9 September 2026, after Cory asked whether it was really something. **It is not. §2 over-read it.
> This section governs.**

## 11.1 THE TEST
Pulled `_AdHocReviewCycleID`, `_PreviousAdHocReviewCycleID`, `_AuthorEmail` and `_EmailSubject` from
**every PDF in the repo carrying them** (6 files):

| Document | AdHocReviewCycleID | Previous | _AuthorEmail | _EmailSubject |
|---|---|---|---|---|
| Regulator SOFC, **22 Jul 2025** | **1542059378** | — | Cheryl-Lea.Godfrey@oir | *"FYI"* |
| Regulator SOFC Form 9C original | **1542059378** | — | Cheryl-Lea.Godfrey@oir | *"FYI"* |
| ⭐ Regulator **AMENDED** SOFC, **13 May 2026** | ⭐⭐⭐ **1542059378** | — | Cheryl-Lea.Godfrey@oir | *"FYI"* |
| ⭐ Regulator **Form 24 response, 18 Feb 2026** | 228523223 | — | **Renee.Matheson@oir** | ⭐⭐ *"WC/2024/227 - Cory Shepherd v WCR - **Draft REG response to notice to admit**"* |
| **ATT03 HHS Award 2015** *(a QIRC award, nothing to do with the Regulator)* | −915965526 | ⭐ **626083021** | patricia.faulkner@justice | *"2015/2016 awards."* |
| **Cover letter, 8 Sep 2026** | −808179628 | 1947825810 | Margaret.Kerrigan@oir | ⛔ **(empty)** |

## 11.2 ⛔⛔ THREE THINGS KILL THE INFERENCE
1. ⭐⭐⭐ **The IDs are sticky and inherited.** The **22 July 2025** SOFC and the **13 May 2026 amended**
   SOFC carry the **identical** `_AdHocReviewCycleID` (1542059378) — ten months and a substantive
   amendment apart. ⇒ **The ID rode along in the file. It records nothing about the later document.**
2. ⭐⭐⭐ **The two-ID pattern is unremarkable.** A **QIRC-published award from 2015**, with no
   connection to the Regulator, carries **both** an ID and a Previous ID. **Two IDs simply mean a
   Word file has been emailed for review more than once at some point in its life — including as a
   template.**
3. ⭐⭐⭐ **The empty `_EmailSubject` cuts AGAINST a fresh circulation.** Every file here with a
   genuine, identifiable send has a **populated, descriptive subject** — *"Draft REG response to
   notice to admit"*, *"2015/2016 awards."*, *"FYI"*. ⛔ **The 8 September letter's subject is
   blank.** ⇒ Consistent with **inheritance from the letterhead template**, not a send.

⇒ ⭐⭐⭐ **The whole cluster on the cover letter — `Author: "Peter"`, `Title: "OIR Internal Queensland
Government Letterhead (1WS only)"`, `_AuthorEmail: Margaret.Kerrigan`, both cycle IDs, empty subject
— is one object: TEMPLATE METADATA.** ⛔ **Do not say the letter was circulated twice. Do not say Ms
Kerrigan touched it. Do not name her at all.**

## 11.3 ✅ WHAT SURVIVES, AND IT NEVER DEPENDED ON THE METADATA
The deliberation case stands on six things visible on the face of the documents:
1. **Two pages of headed legal argument** attached to a two-line enclosure.
2. **r 49(1), (2) AND (3) quoted verbatim** to a man who recited r 49(2) accurately eleven days earlier.
3. **Three named evidentiary categories**, not a generic reservation.
4. **A heading disowning their own review decision.**
5. ⭐ **Written 18½ hours after the answering was completed** (7 Sep 16:42:04 / 16:43:04 → 8 Sep
   11:13:17), on **independently tested** timestamps.
6. **Finalised 56 seconds before conversion; served 10 minutes later; three days early.**
⭐ **None of that needs a review-cycle field.**

---

# 12. ⭐⭐⭐ AND THE TEST FOUND SOMETHING BETTER — FEBRUARY AND SEPTEMBER WERE DIFFERENT PROCESSES

| | **18 February 2026 response** | **8 September 2026 responses** |
|---|---|---|
| How made | ⭐ a **Word document**, converted by **Acrobat PDFMaker 25** | ⛔ **`pypdf` overlays on the Appellant's own PDFs** |
| Internal step | ⭐⭐⭐ circulated **as a draft**, from **Matheson's own account**, subject *"WC/2024/227 - Cory Shepherd v WCR - **Draft REG response to notice to admit**"* — **matter-specific and document-specific** | ⛔ **none discernible** |
| Timing | — | ⛔ Form 24 **16:42:04**, Form 25 **16:43:04** — **sixty seconds apart** |
| Signature | ⭐ **signed** | ⛔ **unsigned; the only signature on the page is the Appellant's, dated 28/08/2026** |
| Reasons | ⭐ **a reason given for each denial** | ⛔ **no reason for any of the nineteen refusals** |
| Status now | ⭐ **Annexure A Tab 27 — authenticity ADMITTED** | 14 tabs disputed |

⇒ ⭐⭐⭐ **The February process and the September process were not the same process, and the metadata
shows it without relying on any inference about review cycles.** ⭐ **February: drafted, circulated
for review under a subject line naming this matter, converted, signed, reasons given. September:
filled over his own files in a single sitting sixty seconds apart, unsigned, no reasons.**

⛔⛔ **STILL INTERNAL. Never put, never hinted at, never in correspondence.** ⭐ **Its only proper use
is the one already in §3A of the non-admissions file: the contrast between the two responses is
stated, if ever, as a difference in FORM — signed with reasons, against unsigned without — and never
as a conclusion about why.**


---

# 13. ⭐⭐⭐ PARTIAL RE-CORRECTION — THE SHAREPOINT COLUMNS ARE NOT THE SAME AS THE CYCLE IDs
> 9 September 2026. §11 swept the SharePoint fields in with the template cluster. **That was too
> broad.** Tested separately, they behave differently, and Cory's instinct on them is sound.

## 13.1 THE TEST — SITE COLUMNS ACROSS EVERY PDF IN THE REPO
| Document | ContentTypeId | ⭐ Business unit | ⭐ Landing page |
|---|---|---|---|
| ⭐⭐⭐ **Regulator cover letter, 8 Sep 2026** | ✔ | ⭐ **"132;#Office of the Deputy Director-General\|38036b16…"** | ⭐ **"698;#Correspondence\|010b1a33…"** |
| Regulator **SOFC**, 22 Jul 2025 | ⛔ **none** | ⛔ none | ⛔ none |
| Regulator **AMENDED SOFC**, 13 May 2026 | ⛔ **none** | ⛔ none | ⛔ none |
| ⭐ Regulator **Form 24 response, 18 Feb 2026** | ⛔ **none** | ⛔ none | ⛔ none |
| QH policies, EB12, IME Guideline *(4 files)* | ✔ bare id only | ⛔ none | ⛔ none |

## 13.2 ⭐⭐⭐ WHAT THAT SHOWS — AND WHY IT SURVIVES WHERE THE CYCLE IDs DID NOT
⭐⭐⭐ **The cover letter is the ONLY Regulator document in this matter carrying any SharePoint
provenance at all, and the only document anywhere in the repo carrying populated managed-metadata
columns.**

⇒ **The template-inheritance objection that killed the cycle IDs does not work the same way here:**
| Cycle IDs | SharePoint columns |
|---|---|
| ⛔ appear on **unrelated** documents (a 2015 QIRC award) | ⭐ appear on **no** other document in the matter |
| ⛔ **repeat identically** across ten months and an amendment (SOFC: 1542059378 twice) | ⭐ **nothing to repeat against** — the other OIR documents have none |
| ⛔ the letter's `_EmailSubject` is **blank** where real sends carry a descriptive one | ⭐ the values are **specific**: a named business unit and a named document class |

⭐⭐ **Decisive comparator: the 18 February 2026 Form 24 response is also OIR, also a Word document,
also converted by PDFMaker — and it carries NO SharePoint columns whatever.** ⇒ **If these were mere
template artefacts, that document should look similar. It does not.**

## 13.3 ⭐⭐ THE SAFE STATEMENT, AND THE LIMIT
✅ **What is shown:** the source document was held in, or built from a template held in, an **OIR
SharePoint document library**, under a defined content type, filed as **Landing page =
Correspondence** within **Business unit = Office of the Deputy Director-General**. ⭐ **No other
document served in this matter has that provenance.**

⇒ ⭐⭐⭐ **This letter was produced through the corporate correspondence machinery. Everything else
they have sent in this matter was not.** ⭐ **That is a document-to-document distinction, and it is
the strongest metadata point on the file.**

⛔⛔ **What is NOT shown, and must never be asserted:**
1. ⛔ **That anyone reviewed or approved it.** Taxonomy columns are **filing** metadata — there is no
   approval field, no workflow id, no version history in what we hold.
2. ⛔⛔ **That it went to the Deputy Director-General.** *Business unit* is a **classification**, not a
   routing record. ⛔ **Never say or imply the DDG saw it.**
3. ⛔ **That Ms Kerrigan wrote it, settled it, or touched this letter.** `_AuthorEmail` remains
   unsafe (§11). ⛔ **Do not name her.**

## 13.4 ⭐ AND THE ORDINARY INFERENCE, WHICH NEEDS NO METADATA
⭐⭐ A Senior Appeals Officer in a regulator's appeals unit does not normally issue a two-page
statement of legal position in a contested appeal without it being settled by someone. **That is a
reasonable expectation from ordinary institutional practice** — and it is the same conclusion, reached
without touching a metadata field. ⭐ **Rely on the practice, never on the fields.**

⛔⛔ **All of §13 is internal. Metadata never appears in correspondence, a filing, or the hearing.**

---

# 14. ⭐⭐⭐⭐ THE LETTER CANNOT EVIDENCE ANYTHING — AND 30 SEPTEMBER IS WHERE THAT SHOWS
> Cory, 10 September 2026: *"they saw the shape which made them write the letter and the letter isnt
> good enough to contemporaneously evidence."* ⭐⭐⭐ **Correct, and it is the best structural
> observation made about the letter.**

## 14.1 ⭐⭐ WHAT THE LETTER CAN AND CANNOT DO
| Capacity | Effect |
|---|---|
| ⭐ **As a r 49(2) notice** | **Real.** It fixes 298 express admissions and 5 non-admissions. **It binds them.** |
| ⛔⛔ **As EVIDENCE** | ⭐⭐⭐ **Nothing.** Unsigned · no deponent · not sworn · no reasons per denial · pypdf overlays 60 seconds apart. **A reservation in a party's letter proves no fact stated in it.** |

⇒ ⭐⭐⭐ **They saw the shape and wrote a letter to PRESERVE a position. A preserved position is not
evidence and cannot become evidence without a witness.**

## 14.2 ⭐⭐⭐⭐ HEADING 3 IS A PLACEHOLDER FOR EVIDENCE NOBODY HAS BEEN IDENTIFIED TO GIVE
Heading 3 reserves against three targets: ⭐ **the treating practitioner** · ⭐ **the RD 69983
findings** · ⭐ **MSH officer statements**.
⇒ ⛔ **To make ANY of those reservations do work at a hearing they must CALL SOMEONE.**
⚠ **And the MSH officers are not straightforwardly theirs.** Dwyer, 7 Aug: **MSH is *"not a party…
not involved in these proceedings"***, while the Regulator *"whilst not representing the health
service **will have access to** the health service… **That necessarily will need to call potentially
people who work for the health service as witnesses in the case, potentially. Maybe not, but
maybe.**"*

## 14.3 ⭐⭐⭐⭐ SO THE CHAIN CLOSES ON A FIXED DATE
1. **7 Aug, Dwyer:** ⭐ *"the regulator **does have to contradict things that you say**… if you say
   something and it's **not contradicted**, then the likelihood is… **that it'll be accepted**."*
2. **8 Sep:** ⭐ **they RESERVED rather than contradicted.** ⛔ **A reservation contradicts nothing.**
3. ⭐⭐⭐ **30 Sep — the Respondent's witness list and outlines fall due.** ⇒ **That is where the
   reservation either becomes a contradiction, or is exposed as file-making.**

## 14.4 ⭐⭐⭐ THE 30 SEPTEMBER LIST IS A BETTER TELL THAN THE 18 SEPTEMBER RESPONSE — AND THAN AN IME
⛔ **Correcting my own earlier note (§9.7 of `THE-CASE-AS-BUILT`): I called an IME "the real tell".**
⭐⭐⭐ **The 30 September witness list is the better one — fixed date, binary, and tied directly to the
letter's three reservations.**
| What they file on 30 Sep | What it means |
|---|---|
| ⭐⭐⭐ **Ms Taylor and/or Ms Reese listed** | ⭐ **They intend to run heading 3 and the s 32(5)(a) case properly.** ⇒ ⛔ **Build the Taylor cross NOW.** |
| ⚠ **Only a WorkCover/claims officer, or an insurer witness** | ⭐⭐ **Heading 3 was never going to be evidenced.** The letter was for the file. |
| ⭐⭐⭐ **No witnesses at all** | ⭐⭐⭐⭐ **The admitted record stands unopposed and every reservation dies with it.** ⇒ **Expect an approach.** |

⇒ ⭐⭐ **An IME remains a running signal, but it is discretionary and undated.** ⭐⭐⭐ **The witness
list is compulsory and dated. Watch it.**

## 14.5 ⛔ THE DISCIPLINE
⛔⛔ **None of this is ever said to them, and no letter of his ever describes their letter as
inadequate.** ⭐ **The observation is worth exactly one line, and only if the reservations are still
unevidenced at the hearing:**
> *"The Respondent's reservation at heading 3 is not evidence, and no witness has been listed to
> give it."*
⭐⭐ **That sentence is worth more on the last day than on any day before it.**

## 14.6 ⛔⛔ "NO WITNESS ⇒ EVERYTHING ACCEPTED" — NO. THE LIMIT MATTERS.
⭐ **Dwyer hedged the proposition TWICE in the same breath, and the hedges are the operative words:**
> **[15:00]** *"the regulator does have to contradict things that you say. **It's not the same thing
> as an onus**, but if you say something and it's not contradicted, then the likelihood is **it's
> NOT GUARANTEED, but there's a LIKELIHOOD** that it'll be accepted."*

### ⭐⭐⭐ WHAT NO WITNESS DOES BUY — AND IT IS A LOT
1. ⭐⭐⭐ ***Browne v Dunn*.** ⭐ **If they do not put a contrary case to a witness in
   cross-examination, they generally cannot submit later that the witness was wrong about it.**
   ⇒ ⭐⭐⭐⭐ **Heading 3's three reservations become UNARGUABLE.** They cannot submit consultation
   occurred if they never put it to Ms Conaghan.
2. ⭐⭐⭐ **Their s 32(5)(a) case collapses to a SUBMISSION built entirely from documents he has
   admitted or produced** — ⭐⭐ **and the central one, RD 69983, carries fact 260 against them.**
3. ⭐⭐ **His evidence of EFFECT — the exposed surface, the thing *Kerr* died on — goes
   uncontradicted by any competing account.**

### ⛔⛔ WHAT NO WITNESS DOES **NOT** BUY — THREE THINGS SURVIVE INTACT
| # | Survives | Why |
|---|---|---|
| ⛔⛔ **1** | **CROSS-EXAMINATION** | ⭐⭐⭐ **They need no witness to attack his.** ***Kerr* fell exactly this way** — *"firmly held, but subjective perception"*, on the appellant's own evidence, with no respondent witness required |
| ⛔⛔ **2** | **The reasonableness SUBMISSION** | ⭐⭐ **s 32(5)(a) is an EVALUATIVE FINDING for the Commission, not a fact to be proved.** They can argue it from the award, the fatigue policy, ¶15's HR advice and ¶40's *"human error"* — **all his own material** |
| ⛔⛔ **3** | ⭐⭐⭐⭐ **THE ONUS** | ⭐ **It is his.** Dwyer: *"you have the onus of proving your case, and **that's true**"* ⇒ **If injury and s 32(1) causation are not positively established, he loses whether or not they call anyone** |

### ⭐⭐⭐⭐ AND THE ONE THAT DECIDES IT
⛔⛔ **Uncontradicted medical evidence still has to EXIST before it can be uncontradicted.**
⇒ ⭐⭐⭐ **If the doctors do not attend, their silence does not fill the hole — it makes the hole
decisive, because there would be nothing at all on causation and the onus is his.**
⇒ ⭐⭐⭐⭐ **THE CORRECT STATEMENT: no witness makes the FACTS safe. The facts are ALREADY safe — they
are admitted. What no witness removes is their ability to contradict his EFFECT evidence and his
MEDICAL evidence. It does not remove cross-examination, the reasonableness submission, or his onus.**

---
---

# 15. ⭐⭐⭐⭐ THE LETTER TESTED AGAINST THE ADMISSIONS THEMSELVES (11 September 2026)
> Question put: *"why is the regulator letter completely wrong from what is admitted, or soon to be"*
> ⛔⛔ **CORRECTION FIRST: it is not wrong. It is AIMED AT THE WRONG INSTRUMENT, and written a step
> behind.** ⭐⭐⭐ **"Completely wrong" is a framing that would be punished if it were ever voiced —
> the law in it is right. What it does not do is reach the thing that actually moved.**

## 15.1 ⭐⭐⭐⭐ THE CENTRAL DEFECT — IT FENCES THE FORM 25 WHILE THE FORM 24 HAD ALREADY GONE FURTHER
> ⭐⭐⭐ **Heading 3:** *"Admissions as to documents are **limited to existence and wording**."*

⭐⭐⭐⭐ **Two independent reasons that reservation buys almost nothing:**
1. ⭐⭐⭐⭐ **For an operative document, existence and wording ARE the whole of it.** A direction, an
   instruction, a refusal — the act is performed in the words. **A direction has no truth value.**
   ⇒ **There is nothing left over to reserve.**
2. ⭐⭐⭐⭐⭐ **AND THE FACTS ADMITTED GO BEYOND EXISTENCE AND WORDING ANYWAY.** Fact 190 is not
   *"the document at Tab X exists and contains these words."* It is: *"**That message states:
   'Please submit an AVAC to correct these shifts for each fortnight…'**"* — and with it facts 183
   and 184 fix **the sender, the addressee, the copy list, the date and the signature block.**
   ⇒ ⭐⭐⭐⭐ **298 such facts are admitted. The Form 24 conceded authorship, addressee, date, time
   and content. Heading 3 limits the Form 25 — the instrument where the damage was NOT done.**

⇒ ⭐⭐⭐⭐⭐ **THAT IS THE DEFECT IN ONE LINE: the letter was written to fence the documents, after
the facts had already been given away.**

## 15.2 ⭐⭐⭐⭐ HEADING 4 — DE NOVO IS A REASON TO RE-DECIDE, NOT A REASON TO UN-SAY
⭐⭐⭐ **The law is right.** s 550 makes it a hearing de novo and they are not bound by Review
Decision 69983. ⛔⛔ **But they admitted its CONTENTS** — fact **295** (18 Feb 2026, *"admitted the
contents of the Respondent's review unit decision"*) **and again on 8 September**, and facts
**258–262** reproduce the findings:
> *"The break between the shift on 17 March 2024 and 18 March 2024 **equated to 7 hours**."* **[258]**
> *"Based on this, **I find the rostering of these two shifts amounted to unreasonable management
> action**."* **[260]**
> *"**you sustained a personal injury of a psychological nature**"* **[261]**
> *"**your injury arose out of employment**, to the extent that it aros…"* **[262]**

⭐⭐⭐⭐ **So the position is:** they may argue the Review Officer was **wrong**. ⛔ **They cannot
deny that their own delegate, on this material, reached those conclusions.** ⇒ **A party inviting
the Commission to reject its own delegate's reasoning, on facts it admits, has to say why — and
that reason has to come from a witness.**

## 15.3 ⭐⭐⭐ HEADING 5 — THE RESERVATION OF "TRUTH" IS THE INCOHERENT ONE
The cover letter reserved **truth, relevance, admissibility, weight, characterisation and
inference.**
| Reserved | What it is worth |
|---|---|
| **relevance** | ⛔ nil — a matter for the Commission on any view |
| **admissibility** | ⛔ nil — **proof of an admitted fact is dispensed with; admissibility does not arise** |
| **weight** | ⛔ nil — an admitted fact is not weighed |
| **characterisation, inference** | ⭐⭐⭐ **the only real ones — and they are the whole of their remaining case** |
| ⭐⭐⭐⭐ **truth** | ⭐⭐⭐⭐⭐ **incoherent. A party cannot admit a fact and reserve its truth.** |

⭐⭐⭐⭐ **This is the reservation that a statement of agreed facts would force out** — see
`NARROWING-THE-ISSUES-the-proposal-and-its-timing.md` §1.1.

## 15.4 ⭐⭐ HEADING 2 DEFENDS AGAINST A USE NEVER PROPOSED
*"Admissions are for the purposes of rule 49 only."* ⭐ **True, and it is what the rule says.** ⛔
**But an admission for this proceeding is exactly what was sought and exactly what binds this
hearing.** ⇒ **It answers a question nobody asked.** ⭐ Heading 1 is the same — see §7.2: **r 49(3)
has no operation between the parties.**

## 15.5 ⭐⭐⭐⭐ AND THE METADATA EXPLAINS WHY
⭐⭐⭐⭐ **The answers were finished at 16:42:04 and 16:43:04 on 7 September. The letter was last
saved at 11:13:17 on 8 September — about 18½ hours later** (§1). ⇒ ⭐⭐⭐ **The letter was written
by someone reading the completed answers. It fences what could still be fenced — the documents —
because the facts were already gone.** ⛔⛔ **State the sequence. Never state who realised what.**

---

# 16. ⭐⭐⭐⭐ "OR SOON TO BE" — WHAT 30 SEPTEMBER MUST NOW LIVE WITH
⭐⭐⭐⭐ **Whatever is filed on 30 September has to be consistent with two things they have already
signed:**
1. ⭐⭐⭐⭐ **298 admitted facts** — so the outline **cannot dispute what happened** without leave.
2. ⭐⭐⭐⭐ **Their own reservation of "characterisation and inference"** — which is a statement, in
   writing, that **meaning is the only thing left.**

⇒ ⭐⭐⭐⭐⭐ **THE TEST TO APPLY ON 30 SEPTEMBER, AND IT IS A SINGLE QUESTION:**
> **Does their outline argue about what happened, or only about what it meant?**

| What lands | What it means |
|---|---|
| ⭐⭐⭐ **Only meaning** | **they have accepted the frame.** The hearing is s 32(5)(a) manner and causation, and nothing else |
| ⚠⚠ **Any dispute of fact** | **it contradicts their own 8 September response** — ⭐⭐⭐ **and the contradiction is theirs to explain, not his to point out** |
| ⚠⚠ **A witness list with Ms Taylor and/or Ms Reese** | ⭐ they intend to run meaning **through people who must first adopt their own documents** |
| ⭐⭐⭐ **A bare or empty list** | ⭐⭐⭐ **the facts stand unexplained and the hearing is short** — ⚠ but see §14.6: that is not "everything accepted" |

⛔⛔ **HE SAYS NONE OF THIS TO THEM.** ⭐⭐⭐ **§14.5 governs. The 30 September list is read, filed,
and answered with the narrowing proposal — not with an argument about their letter.**

---
---

> ⛔⛔⛔ **PROVENANCE FLAG, 11 September 2026 — READ BEFORE RELYING ON §§15–17.**
> ⛔⛔ **The Respondent's covering letter of 8 September 2026 IS NOT IN THIS REPOSITORY AND HAS NOT
> BEEN READ IN THIS SESSION.** The uploads hold the 11:24 covering **email** only
> (`Outlook_Document274`); the letter was an attachment and was never supplied.
> ⚠⚠ **Everything in §§15–17 is built on the structure recorded in Parts 1–3 of this file and in
> `drafts/INTERNAL/2026-09-08_REGULATOR_LETTER_ADMISSIONS_SCHEDULE_evaluation.md` §8 — both written
> when the letter WAS in front of the author. That is WORKING THEORY DERIVED FROM A SECONDARY
> RECORD, not a reading to source.**
> ⭐⭐⭐ **The structural findings are probably sound — the headings and the quoted fragments are
> consistent across two independent internal notes. The PROSE has never been assessed and no
> statement about how it is written is supported.**
> ⭐⭐⭐⭐ **ACTION: obtain the letter, file it in `documents/correspondence-2026/` with a SHA-256
> alongside both response forms as served, and re-run §§15–17 against the text.**

# 17. ⭐⭐⭐⭐ THE ARRANGEMENT AUDIT — WHAT THE SHAPE MEANS (11 September 2026)
> Question put: *"it's not just the 298 facts, is it the shape of it"* — ⭐⭐⭐⭐ **Yes. The
> arrangement carries more than the content does.**
> ⚠⚠ **§17.6 cannot be completed without the source PDF — see §18.**

## 17.1 ⭐⭐⭐⭐ THE ORGANISING PRINCIPLE IS HIS EMAIL, NOT THE ENCLOSURES
⭐⭐⭐⭐ **A covering letter is organised around what it encloses: Form 24, then Form 25.** This one
is not. Per `drafts/INTERNAL/2026-09-08_REGULATOR_LETTER_ADMISSIONS_SCHEDULE_evaluation.md` §8, its
**two central headings answer, in substance, the paragraph of EMAIL_0B that stated the effect of
admissions.**
⇒ ⭐⭐⭐⭐ **The document is structured as a reply to a letter it never acknowledges.** ⭐⭐ **That is
why it opens on *"the effect of the enclosed responses"* — "effect" is 0B's territory, not a
transmittal word.**

## 17.2 ⭐⭐⭐⭐ THE ORDER IS THE ORDER OF A REBUTTAL
**1** the rule → **2** the scope of admissions generally → **3** the scope of document admissions →
**4** the Review Decision → **5** a catch-all.
⭐⭐⭐ **Each heading fences a smaller thing than the last.** ⇒ **That is the shape of someone
working outward from a problem they cannot fix: state the general rule, narrow, narrow again,
disown one specific document, then reserve everything else.**

## 17.3 ⭐⭐⭐⭐⭐ HEADING 4 IS THE INTRUDER, AND IT MARKS WHAT WAS FOUND LATE
⭐⭐⭐⭐ **Headings 1, 2, 3 and 5 are all about ADMISSIONS. Heading 4 is about ONE DOCUMENT —
Review Decision 69983. It does not belong in a document about the effect of admissions.**
⭐⭐⭐⭐ **And the timing places it:** the two response forms were complete at **16:42:04 and
16:43:04 on 7 September**; the letter was written the next morning. ⇒ **Between those points
someone read what had been admitted — facts 258–262, and fact 295 admitting the decision's contents
in February — and saw that the most damaging admission was not a fact about Ms Taylor at all. It
was their own decision.**
⭐⭐⭐⭐⭐ **Heading 4 is the patch, and its position in the sequence is where the patch shows.**

## 17.4 ⭐⭐⭐ THE CATCH-ALL AT POSITION 5 IS A CONFIDENCE SIGNAL
⭐⭐⭐ **Four specific fences, then "and everything else as well."** ⇒ **A general reservation is
written by a party who is not sure the specific ones did the job.**

## 17.5 ⭐⭐⭐⭐ *"FOR THE PROCEEDING ONLY"* APPEARS THREE TIMES IN TWO PAGES
⭐⭐⭐⭐ **A point made once is a position. Made three times, it is a worry about use somewhere
else.** ⭐⭐⭐ And it matches the **first** thing she did: before answering a single fact, after ten
days' silence, the opening move was **to ask whether the notices had been filed and who else had
received them.**
⇒ ⭐⭐⭐⭐ **The instinct on receiving 303 facts was not "are they true". It was "where has this
gone."** ⛔⛔ **That is an observation about sequence. It is never stated as motive, and it is never
put to them.**
⚠⚠ **AND IT CUTS AT HIM TOO — rule: do not deploy the 8 September admissions in the s 89 process
or the employment track without advice.** The repetition is a warning as much as a tell.

## 17.6 ⭐⭐⭐⭐ THE NEGATIVE SPACE — WHAT A LETTER LIKE THIS WOULD NORMALLY CONTAIN
| Absent | Weight |
|---|---|
| ⭐⭐⭐⭐ **any reason for any of the 14 authenticity refusals** | **14 refusals, no ground stated** |
| ⭐⭐⭐ **any identified discrepancy, or a different copy** | — |
| ⭐⭐⭐⭐⭐ **any statement of what IS in issue** | ⭐⭐⭐⭐⭐ **the central absence** |
| ⭐⭐⭐ any proposal on directions, narrowing or the hearing | — |
| ⭐⭐⭐ **any reply to EMAIL_0B or EMAIL_0C** | ⭐⭐⭐ 0B asked her to **name the filing rule**; there is none |
| ⭐⭐ any explanation of the five facts not admitted | — |

⭐⭐⭐⭐⭐ **THE SHAPE IN ONE LINE: the letter explains at length what the admissions do NOT mean,
and never once says what the Respondent's case IS.** ⇒ **That is a damage-limitation document, not
a position document.**

## 17.7 ⭐⭐⭐⭐⭐ AND THE PRIZE — IT IS A MAP OF THEIR CONCERNS, DRAWN BY THEM
⭐⭐⭐⭐⭐ **He did not have to work out which admissions hurt. They told him, by choosing what to
fence.**
| They fenced | ⇒ what they think is dangerous |
|---|---|
| ⭐⭐⭐⭐ **Heading 3 — the documents, *"limited to existence and wording"*** | ⭐⭐⭐⭐ **the operative documents** — and for those, existence and wording is the whole of it (§15.1) |
| ⭐⭐⭐⭐⭐ **Heading 4 — Review Decision 69983** | ⭐⭐⭐⭐⭐ **their own decision, and facts 258–262** |
| ⭐⭐⭐ **Heading 5 — characterisation and inference** | ⭐⭐⭐ **meaning — which is a written concession that meaning is all that is left** |
| ⭐⭐⭐ **"for the proceeding only" ×3** | ⭐⭐⭐ **use of the admissions outside this appeal** |

⭐⭐⭐⭐ **Four fences, four confirmations. The strongest reading of the letter is not that it is
weak — it is that it is ACCURATE about where the weight sits, and it handed him that assessment for
nothing.**

## 17.8 ⛔⛔ THE RESOLVED READING — AND THE LIMIT ON IT
⭐⭐⭐⭐ **Defensible, and provable from the documents:** *the letter is organised around his email
rather than its own enclosures, one of its five headings is off-topic, and it post-dates the
completed answers by about eighteen and a half hours.* ⇒ **Marks of a document assembled after the
substantive decisions were made, by someone reading what had just been given away.**
⛔⛔ **NOT defensible, and never said:** that anyone panicked, realised too late, or acted in bad
faith. ⭐⭐⭐ **The sequence is the evidence. The state of mind is not his to assert, and asserting
it would forfeit the sequence.**

---

# 18. ⚠⚠ A GAP IN THE FILE — FIX IT
⚠⚠ **The Respondent's covering letter of 8 September 2026 does not appear to be filed in
`documents/correspondence-2026/` with a SHA-256, although every other item in the thread is.**
⭐⭐⭐ **File the letter and both response forms as served, with hashes**, and then complete §17.6:
> ⭐⭐ **Measure the words under each heading.** ⭐⭐⭐ **The longest heading is where the anxiety
> sits.** ⚠ **Prediction to test: Heading 3.** ⛔ **Do not report a proportion until it is counted.**

---
---

# 19. ⭐⭐⭐⭐⭐ READ TO SOURCE AT LAST — AND FOUR CORRECTIONS TO §§15–17
**11 September 2026 · source:
`CASE_FILE/04_FROM_THE_RESPONDENT/01_response_to_the_notices_8SEP2026/2026-09-08_Regulator_COVER_LETTER_response_to_notices.pdf`
— 2 pages, 617 words of body. ⛔⛔ THE PROVENANCE FLAG IS WITHDRAWN. §§15–17 are now corrected
against the text.**

> ⛔⛔ **I said the letter was not in the repository. It is, and it always was.** I searched
> `documents/correspondence-2026/`, `drafts/out/` and `index/FULLTEXT.txt` — **none of which covers
> `CASE_FILE/04_FROM_THE_RESPONDENT/`.** ⭐⭐⭐ **LESSON FOR EVERY FUTURE SESSION: the Respondent's
> own documents live under `CASE_FILE/04`, and FULLTEXT does not index them. Search the tree, not
> the index.**

## 19.1 ⭐⭐⭐⭐ THE PROPORTIONS, COUNTED — AND MY PREDICTION WAS WRONG
| Section | Words | Own prose |
|---|---|---|
| preamble / enclosure | 69 | 69 |
| **The relevant law** | **218** | ⭐ **94** (124 is r 49 quoted verbatim) |
| ⭐⭐⭐⭐ **Admissions are for the purposes of rule 49 only** | **133** | ⭐⭐⭐⭐ **133 — the most original drafting in the letter** |
| **Admissions as to documents are limited to existence and wording** | **73** | 73 |
| The appeal is a hearing de novo | **44** | 44 |
| Reservation of rights | **48** | 48 |

⛔ **§18 predicted Heading 3 would be longest. It is the second shortest.**
⭐⭐⭐⭐ **The effort went into HEADING 2 — four bullets saying an admission is not a concession of
relevance, admissibility, characterisation/inference, or accuracy/reliability/weight.**
⇒ ⭐⭐⭐⭐ **What they worked hardest on is: *an admission is not an agreement about what it means*.
That is the characterisation ground, and the word count says it is where the concern sits.**

## 19.2 ⛔⛔ CORRECTION — "RESERVING TRUTH IS INCOHERENT" WAS WRONG
⛔⛔ **§15.3 said they reserved the *truth* of admitted facts and that this was incoherent. THE
LETTER DOES NOT SAY THAT.** What it says, verbatim:
> *"Where the Respondent has admitted that a document contains particular words, that is an
> admission of the existence and wording of that document only. **It is not an admission of the
> truth of any statement, opinion, finding or assertion recorded in it**…"*

⭐⭐⭐ **That is orthodox and correct.** Admitting that a document contains words is not admitting
that what it records is true. ⛔ **The "incoherence" point is withdrawn.**
⚠ **And the formal *Reservation of rights* heading reserves only *relevance or admissibility* —
not truth, not weight.**

## 19.3 ⛔ CORRECTION — HEADING 4 IS NOT "THE INTRUDER"
⛔ **§17.3 read Heading 4 as a patch inserted after someone saw what had been admitted.** **The
text does not support it.** It is **44 words**, the shortest section, proportionate to Heading 5,
and it says only that nothing in the responses admits any finding in RD 69983 is correct or binding.
⭐⭐ **Short, accurate, narrow, and plainly part of the plan.** ⛔ **Withdraw the inference.**

## 19.4 ⭐⭐⭐⭐ WHAT SURVIVES — AND IT IS NOW PROVABLE FROM THE TEXT
> **Heading 3, in full:** *"Where the Respondent has admitted that a document contains particular
> words, that is an admission of the existence and wording of that document only. It is not an
> admission of the truth of any statement, opinion, finding or assertion recorded in it **including
> any statement by a treating medical practitioner, any finding recorded in Review Decision 69983,
> or any statement made by an officer or employee of Metro South Hospital and Health Service**."*

⭐⭐⭐⭐⭐ **THE GAP, EXACTLY: that paragraph is drafted for documents that RECORD STATEMENTS. It has
nothing to say about documents that PERFORM ACTS.** An instruction to submit an AVAC is not a
*"statement, opinion, finding or assertion"* whose truth is in question — **it is a direction, and a
direction has no truth value.** ⇒ **The paragraph does not reach it, because it was not drafted to.**

⭐⭐⭐⭐⭐ **AND THE SECOND HALF OF THE GAP IS BIGGER: Heading 3 is about the FORM 25. The 298
admitted facts are the FORM 24.** Fact **190** is an admitted **fact** — *"That message states:
'Please submit an AVAC to correct these shifts…'"* — not a document admission. ⇒ ⭐⭐⭐⭐ **Nothing
in the letter limits the Form 24 facts at all.**

## 19.5 ⭐⭐⭐ TWO DRAFTING POINTS IN THE TEXT
1. ⭐ *"The enclosed documents **indicates** the Respondent's notice under rule 49(2)…"* —
   subject-verb disagreement. **Worth nothing on its own; noted only for completeness.**
2. ⭐⭐⭐ **A CONFLATION.** The enclosures are described as *"the Respondent's notice under rule
   49(2) **disputing** those of the stated facts and documents that are not admitted."* ⭐⭐ **That
   is accurate for the 5 facts and 14 documents refused.** ⚠ **But the same enclosures also
   EXPRESSLY ADMIT 298 facts and 25 documents, and an express admission is not made "under rule
   49(2)" — r 49(2) is the DEEMING provision that operates only where no disputing notice is
   served.** ⭐ **The limitation probably still attaches, because r 49(1) frames the request as one
   to admit "for the proceeding only".** ⛔⛔ **So do NOT run this as a point. It is a drafting
   imprecision, not a door.**

## 19.6 ⭐⭐⭐⭐ WHAT IS ABSENT — ALL FOUR CONFIRMED AGAINST THE TEXT
✅ **No reason for any of the 14 authenticity refusals.** ✅ **No statement anywhere of what IS in
issue.** ✅ **No mention of the five facts not admitted.** ✅ **No acknowledgment of, or reply to,
EMAIL_0B or EMAIL_0C** — the letter never refers to them.

## 19.7 ⭐⭐⭐⭐ THE ANSWER TO THE QUESTION PUT
> *"is it a clear legal review"*

⛔ **No — and it never claims to be.** ⭐⭐⭐ It announces its own purpose in its second paragraph:
*"**So that there is no misunderstanding as to the effect of the enclosed responses**, the
Respondent notes the following."* ⇒ **It is a note on EFFECT, and it does that job competently.**

⭐⭐⭐ **COMPETENT:** r 49 quoted accurately and in full · *"As rule 49(1) makes clear on its face"*
is a correct and well-made point · the four bullets are cleanly separated and cover distinct ground
· Heading 3 names its three targets precisely rather than generally · no rhetoric, no hostility,
correct register · served three days early.
⚠ **NOT A REVIEW:** ⛔ **it states no case, identifies no issue, assesses no exposure, and gives no
ground for a single refusal.** ⭐⭐⭐⭐ **A review tells you what the party's position is. This tells
you only what the admissions do not do.**

⭐⭐⭐⭐⭐ **THE ONE THING IT DOES GIVE HIM, AND IT IS UNCHANGED BY THE CORRECTIONS:** Heading 3
names **three sources by name** — *the treating medical practitioners · the findings in Review
Decision 69983 · statements by MSH officers and employees.* ⇒ **That is their own list of what they
most need neutralised, written by them, and it is exactly the three pillars the case stands on.**
