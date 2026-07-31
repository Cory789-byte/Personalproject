# MASTER — WC/2024/227 Shepherd · consolidated 31 July 2026

> **Single pull-from point.** Everything below is either verified against a source in this repo or
> marked otherwise. Grading: **[D]** proved by document · **[A]** rests on Cory's account ·
> **[D/A]** document exists, identity or significance rests on his account · **[W]** witness.
> Deeper detail lives in the reference files indexed at §9.

---

## 1. WHERE THINGS STAND

| Track | Status |
|---|---|
| **64G / Form 29** | ✅ **FILED AND SEALED 23 June 2026**, served 24–25 June. **Mention 7 August 2026 before Commissioner Dwyer**, MSH required to attend. Posture: ordinary procedural machinery — volunteer nothing about the employment dispute |
| **Settlement** | Calderbank #2 served **1 July 2026, 12:16** to Matheson **and** the OIR appeals registry (service proof filed). **Rejected 16 July.** Without-prejudice "material development" letter to Matheson **sent 31 July 10:46** (filed) |
| **Employment — the live front** | Excluded since **3 July 2026**. Five weeks. No wages, leave debited, medical costs self-funded. Six shifting bases, **no instrument ever identified**. **31 July 11:43 — Request for Medical Information, nine questions, signed Scott Hughes, Director Corporate Services** |
| **Response** | ✅ **BUILT AND READY** — `drafts/SEND_31JUL/`, 11 pp. Two `[DATE]` fields to fill; one description to confirm |
| **Instruments** | ATT19–21 downloaded and verified from legislation.qld.gov.au 31 July: **PS Act 2022** (current 1 Jul 2026), **AD Act 1991** (19 May 2025 — DV still not a s 7 attribute), **IP Act 2009** (current 1 Jul 2026 — **QPPs**) |
| **Union** | Together — **Heath Moran** (background, and copied on the Oct 2025 complaint), **Emily Petering** (industrial officer). Engaged on roster/pay/leave only; not the appeal, by their demarcation |
| **Appeal substance** | Injury **18 June 2024**. Rejected on the **s 32(5) exclusion** (reasonable management action), *not* on s 32(1). Regulator's SOFC nevertheless contests causation on appeal |

---

## 2. THE 31 JULY RESPONSE PACKAGE

**Location:** `drafts/SEND_31JUL/` · built PDF at `drafts/out/RFMI_Response_and_Allocation_MSH-INJ-5795.pdf`

| File | What it is |
|---|---|
| `RFMI_RESPONSE_EMAIL.txt` | Covering email — To `lbh_InjuryManagement@health.qld.gov.au`, cc `LBH.HRTeam1` |
| `RFMI_Response_and_Allocation_MSH-INJ-5795.pdf` | **11 pp, A4, metadata scrubbed. 11 parts + summary** |
| `NOTE_FOR_DR_MA.txt` | Context note for the GP — **not sent to MSH** |
| `SEND_CHECKLIST_31JUL.md` | Pre-send checklist |
| `build_alloc_pdf.py` | Rebuild: `python3 wc2024227/drafts/SEND_31JUL/build_alloc_pdf.py` from repo root |
| `SUPERSEDED_single-letter-draft.txt` | ❌ do not send |

**Outstanding before send:** `[DATE]` in the header (response date); `[DATE]` at Part 6 (date of the
earlier email raising delegation/conflict); confirm the "formal complaint in February 2026"
description at Part 5.2.

### The allocation — the document's spine

| Q | Subject | Allocated to |
|---|---|---|
| 1(a) | Date of first diagnosis | **Answered openly — 24 October 2024**; clinical context from the psychiatrist |
| 1(b) | Clinical basis for the causal link | **Withdrawal requested** — the only one |
| 1(c) | Self-report v clinical assessment; reports held | Consented — Dr Ma, his own file. *Answer: the specialist reports he holds* |
| 1(d) | Foreseeable risk; controls | Psychiatrist; Dr Ma from the specialist documentation |
| **2** | Lawful directions; performance/conduct | **Health Service** — threshold question |
| **3** | Fitness under existing reporting arrangements | **Health Service** — risk assessment |
| 4 | Restrictions, duration, review | Dr Ma |
| 5 | Meaning of "complaint handling" | Health Service (already answered), then Dr Ma |
| **6** | Requirements without modification | **Health Service** — identify the genuine occupational requirements |
| 7 | Working memory, functional | Psychiatrist |
| 8 | Tasks/environments that exacerbate | Psychiatrist; Dr Ma from the specialist documentation |
| **9** | If unable to accommodate, safe return? | **Health Service** — the onus is theirs |

⭐ **Four of nine are not medical questions.** Seven are already answered by the ECC.

**Two structural additions made 31 July:**
- **Part 6.1 — the separation of functions**, proposed as the management of the conflict: medical
  information held **exclusively by Injury Management**; the **decision made outside Corporate
  Services**; **implementation retained** within it. *"The officer steps out of the decision, not out
  of the workplace."* Anchored to the ECC's own AC4(c) recommendation.
- **Part 11 — the substantive position**: asks MSH to confirm the position is still held, **whether
  the shifts are being worked by another employee** (tied expressly to Q9 — if the work is being
  done, it is available), and what has been communicated in the workplace about the absence.

---

## 3. THE JULY 2026 FINDINGS

### 3.1 The purpose inversion — MSH's own words
> "your recently completed Employee Capabilities Checklist … **which was provided to us to
> facilitate a Return to Work Plan**." — Hughes, 31 July 2026

**2 Jul** Taylor requires the ECC, return "cannot be facilitated" without it, deadline 2:00pm 3 Jul →
**3 Jul 14:32** provided, certifying **fit with restrictions** → **~15:30** held out (**~58 minutes**)
→ shifts charged to accrued leave. The document required so he could work became the basis for
refusing work.

### 3.2 The restriction and MSH's own process are identical
- **ECC:** complaints "to be logged and redirected to management/the dedicated complaints area, not
  actioned, resolved or absorbed by Mr Shepherd"
- **MSH 31 Jul:** "immediate escalation and management by the Health Service Client Liaison Officer
  and/or Manager, Switchboard Services"
- **Role Description (their Attachment 2):** no complaint-handling responsibility

⇒ Five weeks of unpaid exclusion over a restriction asking MSH to keep doing what it says it does.

### 3.3 The ECC already answers 7 of the 9 questions
Q1(d) ← AC3/AC4 · Q4 ← AC2 ("3–6 months… 8-weekly review"; review date **28 Aug 2026**) · Q5 ← the
restriction verbatim · Q6 ← "**Usual switchboard operational duties remain suitable**" · Q7 ←
"Working memory affected under stress (**treating psychiatrist report 13-Feb-2025**)" · Q8 ← AC1 ·
Q2 ← "**Understanding instructions: Normal**", "**Carrying out instructions accurately: Normal**"

Also on its face: "**(continuation of existing arrangement)**"; "the pattern Mr Shepherd has in fact
**worked and tolerated over the past twelve months without deterioration**"; AC4(c) recommends
"return-to-work coordination and correspondence **through the Injury Management team, Human
Resources**".

### 3.4 Legal defects in the request
- **No power cited.** G03 is a policy; WHS ss 17/19 are **duties**. The source is the reasonable-direction power, limited by **reasonableness**
- **G03 cl 3** limits supporting information to what is "**necessary**… to either identify required workplace adjustments and/or assess the suitability of proposed adjustments"
- **G03 cl 2**: unjustifiable hardship "tested against **the whole organisation, not a division or unit**"; "**the onus is on Queensland Health, as the employer, to prove an adjustment is unreasonable**"
- **Q6 applies the wrong test** — G03 and AD Act s 34 ask about genuine occupational requirements **with** adjustment
- **AD Act s 124(1)/(3)** — asking for information on which discrimination might be based; **onus on MSH** to prove it was "reasonably required"
- **WHS ss 47–49** — no consultation. s 49(e)(iii) covers "procedures for **monitoring the health of workers**"
- **QH-IMP-401-5 §2.2** — suitable duties "wherever reasonably practicable"; ongoing connection to the workplace; "regular, transparent and timely communication… **whether at work or off work**"; inform the worker of the **dispute resolution process**. None occurred
- **G03 cl 1.1.1 / WRS §2.3** — rehabilitation applies with "**no claim or entitlement to compensation**" and to "**either a work or non-work-related** injury/illness" ⇒ kills the 15 July position

### 3.5 The asymmetry of time
**2 Jul** Taylor sets a deadline of 2:00pm next day — **met**. **3 Jul** excluded within the hour.
**Five weeks**: no instrument, no date, six positions, "unable to guarantee" (30 Jul). **31 Jul**
Hughes sets seven days **with a consequence attached**.
⇒ Response asks what decision is meant and under what instrument, and for **a date in return**.

### 3.6 The bleeding stopped 30 July
15 Jul was the last freely-given position. **29 Jul** basis changed to WHS. **30 Jul** holding reply
— they stopped answering. **31 Jul** a formal process. Trigger: his own 28 and 30 July letters.
⇒ From assertion to inquiry. Assume few further admissions from HR.

### 3.7 Drafting evidence — the RFMI was not legally settled
Institutional third person and pinpoint rule citations in the **5 June objection** (Ruttan contact)
vs first person, loose citation, "cab be found out their website", "Mr Shepherds", "fulfill", and
**he/their pronoun drift between adjacent questions** in the RFMI. Decisive: **Ruttan drafted Item 20
of the objection, which addresses PID 24-ESU-1130 by reference number** — she cannot have approved
"the Health Service is not aware of any concerns being raised".
⇒ Template architecture + rushed HR execution, no legal review. **The four admissions of 31 July are
on the record before anyone competent read it.**

### 3.8 ⭐ THE PRODUCTION TIMINGS — established from PDF metadata and recovered revisions

| Time (AEST, Fri 31 Jul 2026) | Event |
|---|---|
| **10:46** | Cory's WP letter sent to Matheson |
| **11:10:27** | GP letter (5 pp) exported from Word |
| **11:11:02** | Employee letter (2 pp) exported — **35 sec later** |
| **11:11:27** | Employee letter signed — **25 sec after creation** |
| **11:11:42** | GP letter signed — **75 sec after creation** |
| **11:43** | Both transmitted |

- The signature is a **stored image**: 1000 × 398 px @ 624 dpi (1.60 × 0.64 in), applied via Adobe
  Fill & Sign. **Identical dimensions and byte size in both letters.**
- **All three saved revisions of each letter recovered** (truncation at each `%%EOF`). **Text
  identical throughout** — nothing hidden, nothing altered. ⚠️ Any suggestion of alteration is
  **closed. Do not advance it.**
- ⚠️ An export timestamp fixes **finalisation**, not drafting. The Word original — never produced —
  is the only artefact carrying the author, revision history and save chain.

### 3.9 ⭐ 14 ERRORS ACROSS 7 PAGES — the letters were not read before signing
Two in one five-word phrase (*"cab be found out their website"*); *"Mr Shepherds"*; *"fulfill"*;
*"The purposes… is"*; *"the below question"* followed by four; **wrong policy number — "G3" for
"G03"**; letterhead *"Logan and Beaudesert"* vs signature block *"Logan Beaudesert"* on one page;
and **pronoun drift between adjacent questions** (Q3 "their" → Q4 "his" → Q7 "their").
⇒ **You cannot read a 5-page, 9-question letter in 75 seconds.** Three independent lines — the
errors, the timings, the substantive failures — converge on the same conclusion.

### 3.10 ⭐ WHAT POWER WAS MSH ACTUALLY USING? — the answer splits
**Their stated basis, entire:** *"HR Policy G3: Reasonable Adjustment, and sections 17 and 19 of the
Work Health and Safety Act 2011."*

- **For the information request** — G03 can bear it. Their theory is articulable and Forrest stated
  it on 7 July: they say they cannot understand the unresolved matters, so cannot assess the risk.
- **For the exclusion — nothing was used at all.** G03 cl 1.1 says adjustments let employees
  *"continue work during their recovery"*. WHS ss 17 and 19 are **duties on MSH**, not powers over a
  worker. Neither supports exclusion or leave debiting.
- ❌ **PS Act 2022 s 104 — the only statutory power to compel a medical examination — was NEVER
  CITED.** Its **s 103** gateway needs absence or unsatisfactory performance: no performance issue
  has ever been put, and **the absence is MSH's own act**. **s 105** (the only statutory link to
  leave in that division) operates only where an s 104(b) requirement is not complied with.

⇒ **The six shifting bases exist because each was an attempt to find, after the fact, an authority
for something already done.**

### 3.11 ⭐ NEW — IP ACT: QPP 3.3 (verified from the Act, current 1 July 2026)
The Act now applies **Queensland Privacy Principles** (sch 3) — the old IPP/NPP split is superseded.
> **QPP 3.3** An agency **must not collect sensitive information** unless (a) the individual
> **consents** **and** the information is **reasonably necessary for, or directly related to**, one
> or more of the agency's functions; or (b) QPP 3.4 applies.
> **sch 5:** sensitive information includes **health information**; health information includes
> "the individual's **health at any time**" and "**a disability** of the individual at any time".

⇒ **Consent is a statutory precondition, and it may be scoped.** Declining option 2 and consenting
question-by-question is the operation of QPP 3.3, **not obstruction**.
⇒ **Third independent necessity test**, alongside **G03 cl 3** and **AD Act s 124(3)** (onus on MSH
to prove information was "reasonably required").
⚠️ Also: the employee letter says the information will *"**primarily** be used"* for the stated
purpose — conceding undisclosed secondary uses, against QPP 3.3.

### 3.12 "UNRESOLVED MATTERS" — answered from the Code MSH must apply
MSH says it *"does not have sufficient information to understand the nature of these matters"*.
But **"unresolved" is a status, not a mystery**: matters were raised, not determined, and no outcome
was advised. **MSH holds the record of both.**
And **G03 cl 1** obliges MSH to apply the **Psychosocial Code 2022** to this very process — a Code
which defines **poor organisational justice** as "a lack of procedural fairness…, informational
fairness (keeping relevant people informed), or interpersonal fairness", arising from "**inconsistent
application of procedures across workers or over time**" and "**failing to follow agreed policies,
guidelines and procedures**".
⇒ Now in the response at **Part 4.2** — with no reference to patient safety, the PID, or the subject
matter of any complaint.

### 3.13 ⛔ THE 31 JULY TIMING INFERENCE — CLOSED
Cory's WP letter to Matheson went **10:46**; the first RFMI export was **11:10:27** — **24 minutes**.
**But MSH's holding reply of 30 July at 14:33 said the request was "progressing for delegate
approval."** The document existed ~20 hours before the email. **Record as closed on causation.**
His working theory (that the email collapsed the review step) is recorded as **WT-2026-07-31** in
`working-theories.md`, with the evidence both ways.
⚠️ Closing this one **protects** the still-open 1 Jul → 2 Jul sequence: a set of inferences in which
one has been tested and abandoned reads as observation, not habit.

### 3.14 ⭐ THE COMPLETE CITATION RECORD — two instruments in five weeks
Full-text extraction of every MSH item, 2–31 July 2026. Detail at
`skill/references/msh-citations-complete-list.md`.

| Date | Author | Instruments cited **by MSH** |
|---|---|---|
| 2 Jul | Taylor *(the origin direction)* | **NONE** |
| 7 Jul | Forrest | **NONE** — "work health and safety legislation", unnamed |
| 15 Jul | Harrison *(pay refused)* | **NONE** |
| 29 Jul | Harrison | **WHS Act 2011** — first correct formulation |
| 30 Jul | Harrison *(holding reply)* | **NONE** — the EB12/Award/QH-POL text in that PDF is **Cory's own 28 July letter quoted beneath** |
| 31 Jul | Harrison *(covering email)* | **NONE** |
| 31 Jul | **Hughes — both letters** | **HR Policy G3 [sic: G03]** + **WHS Act ss 17, 19** |

**Complete deduplicated list:** WHS Act 2011 (ss 17, 19); HR Policy G3/G03. Plus, in **form
boilerplate only** — Information Privacy Act *(year omitted on the consent form)*, WCRA 2003, HED
01/16, HED 12/21 + HR Policy B70, and an unnamed "Metro South Health privacy policy". *(2025:
Directive 03/20, HR Policy C73, HR Policy E4.)*

⇒ **The WHS Act appears the day after Cory's 28 July letter. G03 appears two days after that, and
only for the information request — never for the exclusion.** Not cited once by anyone: **PS Act
ss 103–105**, EB12, the Award, **QH-IMP-401-5** (MSH's own standard for this process), QH-POL-231 /
Directive 12/24, the Psychosocial Code, WHS ss 47–49, AD Act ss 34/124, Code of Conduct cl 1.2.
⇒ **Independent corroboration of §3.10 on MSH's own documents: for the exclusion, nothing was used.**

---

## 4. THE 2025 HUGHES/TAYLOR HISTORY

Full compilation: `skill/references/hughes-taylor-evidence-compilation.md`

### The three findings resting entirely on MSH's own documents
1. **Hughes held a court form naming Cory the AGGRIEVED** (sent 12 Mar 2025 05:43, acknowledged 08:38 "Noted thanks") **and sixteen days later wrote he "may be deemed as the perpetrator"** — the police application having been **withdrawn and the TPO vacated 25 Feb 2025**, 31 days earlier
2. **Hughes wrote that meetings "have not taken place due to you not being in the workplace"** when the 27 Aug meeting was cancelled at 09:15 — **two hours and two minutes** after Cory offered documents at 07:13 — because "**Scott is unwell today and not in the office**"
3. **Hughes signed the 31 Jul 2026 RFMI premised on MSH being "not aware of any concerns"** eight weeks after its Chief Executive signed an objection engaging PID 24-ESU-1130 by reference number

### The measured intervals
| Interval | Between |
|---|---|
| **31 days** | withdrawal/TPO vacated → "perpetrator" |
| **16 days** | receipt of the aggrieved form → "perpetrator" |
| **17 days** | return to work (31 Mar 2025) → counting begins (17 Apr) |
| **2h 02m** | offer of documents → meeting cancelled |
| **~58 min** | ECC provided → held out |

### April 2025 — placement, appointment, and both reversed
Returned **31 Mar 2025** (MSH knew by 28 Mar). By **8 Apr** located in the **security office** during
a "**Cory Shepherd Reinstatement process**" with **Jacqui Roberts, A/Director HR Business
Partnering**. A full-time appointment was made in his position. **Together was involved; Cory was
not.** **Roberts caused him to be restored to Switchboard; the appointment was revoked entirely and
that employee returned to their previous role.**

⇒ **A reversal is an admission by conduct.** Properly made placements and appointments do not need
undoing. And **the correction generated records even though the original did not** — MyHR movements
for both employees, payroll showing hours revert, rosters, any written direction from Roberts.

### The counting
**34 alleged process failures**, 17 Apr – 17 Aug 2025, each dated and attachment-referenced. Several
recorded by MSH as **court-related**. A fatigue-leave request **declined** "on the grounds that the
'fatigue' experienced was due to personal circumstances and not work related".
⇒ Disclosure **12 Mar**; first counted occasion **17 Apr**. **They had the context in writing five
weeks before the conduct they counted.**
⚠️ The 34 occasions are a genuine vulnerability. Warn-then-count is orthodox. The honest position is
that there were attendance problems, and that the employer's response to a disclosed crisis was to
count its consequences.

### The complaint
**4 Oct 2025** — formal written request for review to **Jacquie Roberts, A/Director HR Business
Partnering**, concerning the process "initiated by my Director, Mr. Scott Hughes", **copied to Heath
Moran (Together)**. No documented response.

⇒ **Hughes is the subject of a documented complaint by the employee whose capacity and return he is
now determining.** One sentence recording this is in Part 6 of the response.

### The repeated defect — action without a documented basis
| | Apr 2025 | Jul 2026 |
|---|---|---|
| Action | Placed outside Switchboard | Excluded, 5 weeks |
| Basis | None — no advertisement, no authorisation, no movement record **[A, establishable by nil return]** | **No instrument, no delegate**, after three written requests **[D]** |
| Directorate | Corporate Services | Corporate Services |
| Officers | Taylor, Hughes **[A]** | Taylor (2 Jul), Hughes (31 Jul) **[D]** |

---

## 5. STANDING DISCIPLINES

1. ❌ **Never connect 1 July and 2 July** (Calderbank → Taylor's ECC direction) in any correspondence. Record the sequence; assert nothing. Same for 30/31 July
2. ❌ **Never allege a threat.** Ask what decision is meant and under what instrument
3. ❌ **Never allege "unsanctioned" or "acting alone."** A Director signed — that is authorisation. The argument is **acted with authority and without power**
4. ❌ **Never say "privileged"** about anything going to MSH. Report A is **medical-in-confidence**. Report B (appeal) is privileged
5. ❌ **Keep the DFV history, court material and attendance record out of MSH correspondence.** Union and reserved general-protections file only
6. ❌ **Keep "Chloe's friend" out of any document.** Converts a documented sequence into an allegation of motive
7. ❌ **Do not approach colleagues for statements** while excluded — characterisable as inappropriate contact and exposes them. The union can
8. ✅ **State facts, ask questions.** An assertion can be denied; a fact plus a question can only be answered or visibly avoided
9. ✅ **Concede everything conceivable.** Objecting to one question out of nine is what makes the objection unanswerable
10. ❌ **Never allege the documents were altered.** All revisions recovered; text identical. That line is closed
11. ❌ **Never raise the typographical errors with MSH.** Petty, and it forfeits the register doing the work. Only the substantive failures are deployed, argued on the instrument
12. ❌ **Never invite MSH to narrow its own costs undertaking.** State the billing arrangement; do not ask them to confirm it
13. ⚠️ **Do not conflate a rushed finalisation with a rushed decision.** The metadata proves the first only; the drafting errors independently prove no review

### Banked — deployed only on a specific trigger
- **QH-IMP-401-5 §2.1** — "not take action to avoid the workers compensation process as per section 46A of the act" → appeal track only
- **IME Guideline §4.1** — "a chief executive **cannot direct an employee not to attend the workplace** for the purpose of requiring an employee to submit to a medical examination" → only if MSH moves to an IME
- **PS Act s 103 gateway failure** — same trigger. No performance issue was ever put; the absence is MSH's own act
- **MSH's four weeks of silence** on the missing medical certificate → only if they ever raise it

---

## 6. THE TWO-REPORT STRUCTURE

**One attendance, two reports.**
- **Report A — MSH-funded.** Current capacity, functional restrictions, adjustments. **No opinion on cause or origin, even in passing.** Assume it reaches the Regulator: MSH receives the Regulator's decisions (Review Decision 69983 is cc'd to MSH), is inside the proceeding via the 5 June objection, and a medical report about Cory has reached this proceeding once already. The scope limit is a **filter, not a shield** — it makes the report useless to them, not invisible
- **Report B — the appeal.** Causation and chronology. Commissioned by Cory, **litigation privilege**, his to serve or not

⚠️ **The 24 October 2024 collision.** Diagnosis and the Review Decision reasons share a date. The
appointment was that day; the decision arrived after. Same-day, so **time proves it, not date** — the
delivery email timestamp and the consultation time. Brief the psychiatrist on the chronology
**18 June 2024 → 24 October 2024** (~4 months).

---

## 7. OPEN ITEMS

**Clock on them**
- **7 August 2026** — 64G mention before Dwyer
- Two `[DATE]` fields + the Feb 2026 description, then send the response
- Limitation period for a **non-dismissal general protections application** — the 2025 events are
  9–16 months old. Union question, this week

**Documents to obtain**
- ⚠️ **Directive 03/20** (DFV support) — **still unread.** Not locatable by path on forgov;
  `health.qld.gov.au` returns **403**. The whole March 2025 DFVL point rests on it
- **Directive 04/24** (IMEs), **HR Policy C73**, **HR Policy E4** — same problem
- **MyHR movement records, April 2025** — Cory's restoration to Switchboard **and** the other
  employee's revocation; payroll, rosters, any written direction from Roberts
- **Rosters / AVAC / payroll 3–31 July 2026** — whether the shifts are being worked
- **Together's file** — the April 2025 revocation, and the 4 Oct 2025 complaint
- **Texts from Hughes** — full threads, sender verified against **0499973195**, timestamps intact
- Clinical note **24 Oct 2024** with consultation time; delivery email for **Review Decision 69983**
  with timestamp; the psychiatrist referral and date
- Org chart showing **Security under Corporate Services**
- The separate **medical certificate** the ECC form requires

**Resolved today — do not re-open**
- ✅ **AD Act**: DV is **not** a protected attribute. Confirmed against the in-force version
- ✅ **IP Act**: framework is now **QPPs**, not IPPs/NPPs. QPP 3.3 verified
- ✅ **PS Act ss 103–105**: verified verbatim, current 1 July 2026
- ✅ **Document alteration**: all revisions recovered, text identical. **Closed**
- ✅ **The 31 July timing inference**: closed on causation by MSH's own 30 July holding reply

**Unresolved facts**
- The **last shift actually worked** before 2 July 2026
- Any response from Roberts to the 4 Oct 2025 complaint
- Whether an **RRTWC** was ever notified (WRS §2.3)
- Whether MSH's Word originals of the 31 July letters exist — the only artefact carrying the author
  and revision history

## 8. KEY DOCUMENT LOCATIONS

**July 2026:** `documents/2026-07-*` — the Calderbank service proof (1 Jul), Taylor's ECC direction
(2 Jul), Forrest (7 Jul), Harrison discretion (15 Jul), Matheson rejection (16 Jul), the 28 Jul
letter, the EAF/WHS reply (29 Jul), the holding reply (30 Jul), and the full **RFMI bundle** (31 Jul:
covering email, both Hughes letters, ECC, Role Description)

**2025 history:** `documents/2025-hughes-history/` — Attachments A–F, the Roberts reinstatement chain,
the 4 Oct complaint

**Instruments:** `documents/instruments/ATT02–ATT18` — EB12, Award, Psychosocial Code, QH-IMP-401-5,
QH-POL-210/G03, Directive 12/24, AO3 Role Description, QPS Code of Conduct, AD Act, WHS Act, IME
Guideline

⚠️ **Image-only PDFs** (ECC, QH-IMP-401-5): no text extraction. Render with
`pdftoppm -png -r 110 <file> <prefix>` then read the images. `pdfimages` fragments some files —
use `pdftoppm`.

---

## 9. REFERENCE FILES

| File | Contents |
|---|---|
| `skill/references/hughes-taylor-evidence-compilation.md` | **The evidence schedule** — 31+ propositions graded, 7 contradictions, 13 admissions, propositions not established, gaps, chronology with intervals, evidence classes |
| `skill/references/hughes-2025-history-forensic.md` | Forensic analysis of the eight 2025 documents |
| `skill/references/RFMI-compliance-test.md` | The 31 July request tested against every governing instrument |
| `skill/references/31JUL-error-and-rush-assessment.md` | **14 errors, 5 substantive failures matched to the instruments, and the production timings** |
| `skill/references/metadata-register-31JUL2026.md` | **Full metadata, recovered revisions, signature-image analysis, and the limits of what metadata can show** |
| `skill/references/what-power-did-MSH-use.md` | **The instruments tested against the acts taken — and where nothing was used at all** |
| `skill/references/msh-document-quality-comparison.md` | Seven MSH documents ranked by development and error density |
| `skill/references/msh-citations-complete-list.md` | **Every policy and Act MSH has cited, by document and date — and the nine instruments never cited once** |
| `skill/references/personal-liability-hughes-taylor.md` | **Whether acting for the Health Service protects Hughes and Taylor — IR Act ss 282(6), 285, 296, 305–307, 310(3), 571; PS Act s 269; PID Act ss 40–45; AD Act ss 122–123, 129–133; WHS ss 27, 104–107** |
| `skill/references/hughes-taylor-evidence-compilation.md` | *(see above)* |
| `skill/references/working-theories.md` | Hypotheses with confidence — incl. **WT-2026-07-31** |
| `skill/references/letter-foundation-verified.md` | ✅/⚠️/❌ register of propositions |
| `skill/references/public-entity-obligations.md` | The four layers of obligation |
| `skill/references/medical-causation-framework.md` | Krishnaiah brief; the pre-existing-anxiety rebuttal |
| `skill/references/9C-contradiction-matrix.md` | Contradictions in the Regulator's SOFC |
| `skill/references/discretion-logic-research.md` | Why the 15 July "discretion" is misconceived |
| `working-notes.md` | The running log — append here each session |
| `CLAUDE.md`, `skill/SKILL.md` | Project context and method; status blocks current as at 31 Jul 2026 |
