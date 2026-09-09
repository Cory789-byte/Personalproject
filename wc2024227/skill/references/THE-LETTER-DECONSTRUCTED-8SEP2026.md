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
