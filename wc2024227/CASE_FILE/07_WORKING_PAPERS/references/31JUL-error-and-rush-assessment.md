# ASSESSMENT — the 31 July 2026 documents: every error, matched to the instrument, and the rush

> The two letters signed by Mr Scott Hughes, Director Corporate Services, sent 11:43 AEST
> 31 July 2026. Every error quoted from source. Every substantive error matched to the provision it
> contradicts. All timings from PDF metadata and recovered revisions.
> **Purpose: to establish that these documents were not reviewed before they were sent.**

---

## PART A — THE RUSH, ESTABLISHED

### A1. The production sequence

| Time (AEST, Fri 31 Jul 2026) | Event | Source |
|---|---|---|
| **11:10:27** | GP letter (5 pp, 9 questions) exported from Word | `xmp:CreateDate` |
| **11:11:02** | Employee letter (2 pp) exported from Word | `xmp:CreateDate` |
| **11:11:27** | Employee letter signed — **25 sec after creation** | recovered revision 3 |
| **11:11:42** | GP letter signed — **75 sec after creation** | recovered revision 3 |
| **11:43** | Both transmitted | covering email |

**Both letters exported 35 seconds apart. Both signed within 75 seconds. Sent 32 minutes later.**

### A2. The signature was applied without the document being read

Revision recovery (truncation at each of the 3 `%%EOF` markers) establishes:
- **rev1 → rev2** = +185 bytes, adds `/StructTreeRoot`, **text identical**. Standard Word output —
  the unsigned Role Description does exactly the same.
- **rev2 → rev3** = **+99,121 bytes** (employee) / **+101,021** (GP); adds `/OCProperties` and
  **`/ADBE_FillSignInfo`** (Adobe Fill & Sign); **text identical**.
- What rev3 added: a **1000 × 398 px JPEG at 624 dpi** with transparency mask — **1.60 in × 0.64 in**
  — placed on the signature page. **Identical dimensions and byte size in both files: the same
  stored signature image.**

⇒ **You cannot read a five-page letter putting nine questions to a doctor in 75 seconds. You cannot
read a two-page letter in 25 seconds.** The signature was applied to documents that were not read at
the point of signing.

### A3. And nothing was corrected afterwards
Text identical across all three revisions of both letters. Nothing was amended between creation,
signing and transmission. **The errors below were in the version signed and in the version sent.**

### A4. What the metadata does NOT establish
A Word→PDF export timestamp fixes **finalisation**, not drafting. The Word document may have existed
earlier. ⇒ **The rush established is a rush to finalise and send. The errors below independently
establish that no proofread occurred at any stage.**

---

## PART B — EVERY ERROR

### B1. EMPLOYEE LETTER (2 pp)

| # | Error | Quoted |
|---|---|---|
| 1 | **Two errors in five words** | *"More information about the support TELUS Health can provide **cab be found out their** website"* — "can be found on their" |
| 2 | Missing preposition | *"If you have any questions in relation ⌀ this correspondence"* — "in relation **to**" |
| 3 | Wrong preposition | *"to support the implementation **for** appropriate controls"* — "implementation **of**" |
| 4 | **Wrong policy number** | *"Human Resources (HR) Policy **G3**: Reasonable Adjustment"* — the policy is **G03** (its own header: "Human Resources Policy G03 (QH-POL-210)") |
| 5 | Internal inconsistency | Letterhead: *"**Logan and Beaudesert** Health Service"*. Signature block: *"**Logan Beaudesert** Health Service"* — same page |
| 6 | Missing punctuation | *"your role Administration Officer (AO), Switchboard Operations…"*; *"Michelle Harrison Injury Management Consultant"* |
| 7 | Awkward date form | *"completed by Dr Day Hong Ma **on the 3 July 2026**"* |
| 8 | ⚠️ **Undisclosed secondary purpose** | *"This information will **primarily** be used for the purposes of better understanding your condition"* — "primarily" implies other uses, none stated. **See C5** |
| 9 | Voice/signature seam | Written in the first person of the **Injury Management Consultant** — *"**I** am seeking"*, *"**I** require"*, *"**I** will make a decision"* — and signed by **Hughes** |

### B2. GP LETTER (5 pp)

| # | Error | Quoted |
|---|---|---|
| 10 | Subject–verb disagreement | *"**The purposes** of this request **is** to better understand…"* |
| 11 | Missing apostrophe | *"Your report states **Mr Shepherds** 'working memory is affected under stress'"* (Q7) |
| 12 | **US spelling** in a Queensland Government letter | *"is Mr Shepherd able to **fulfill** the full inherent requirements"* (Q6) |
| 13 | Singular/plural mismatch | *"Could you please clarify **the below question**"* — followed by four sub-questions (a)–(d) |
| 14 | ⭐ **TEMPLATE DRIFT — the decisive marker** | **Q3:** *"whether Mr Shepherd is medically fit to return to **their** substantive role… reporting to **their** current line manager"* · **Q4:** *"If Mr Shepherd is not able to return to **his** substantive role"* · **Q7(a):** *"how this may affect **their** capacity to perform **their** substantive duties"* |

⇒ **He becomes they and back again between adjacent questions.** A gender-neutral template
find-and-replaced in part. **This is the single clearest proof that the question set was not read
through before it was sent to an external clinician.**

---

## PART C — THE SUBSTANTIVE ERRORS, MATCHED TO THE INSTRUMENT

### C1. Q6 applies a test that does not exist under the policy the same letter cites
> **Their question:** *"In your medical opinion is Mr Shepherd able to fulfill the full inherent
> requirements of his Role… **without restrictions or modifications to duties**?"*

| Instrument | What it actually requires |
|---|---|
| **G03, purpose** | "to assist employees… to meet the **genuine occupational requirements** of their role **by applying principles of reasonable adjustment**" |
| **G03 cl 3** | adjustments "should support the employee to undertake the **genuine occupational requirements** of their role" |
| **AD Act s 34** | reasonable terms where capacity is restricted — with adjustment, subject to unjustifiable hardship (ss 5, 35) |
| **IME Guideline** | information on capacity "to carry out the **genuine occupational requirements** of their role" |

⇒ **Four instruments, one test — and it is not the test asked.** "Without restrictions or
modifications" is the incapacity formulation. **They cited G03 in the same document and asked the
opposite of what G03 asks.**

### C2. Q9 reverses the onus their own policy places on them
> **Their question:** *"**If we are not able to accommodate** the restrictions you have
> recommended, is Mr Shepherd able to safely return to the workplace?"*

> **G03 cl 2:** unjustifiable hardship "is tested against **the whole organisation, not a division or
> unit within the organisation**… **the onus is on Queensland Health, as the employer, to prove an
> adjustment is unreasonable, not on the person to prove that it is reasonable.**"

⇒ Three errors in one question: it presupposes an inability never assessed; it asks the doctor to
discharge **MSH's** onus; and it is framed at unit rather than organisation level.

### C3. Q3 asks a clinician to discharge MSH's statutory duty
> **Their question:** *"whether Mr Shepherd is medically fit to return to their substantive role
> **under the existing reporting arrangements**"*

| Instrument | Where the duty sits |
|---|---|
| **WHS s 19(1)–(2)** | The **PCBU** must ensure health and safety of workers **and of other persons** |
| **Psychosocial Code 2022** | Psychosocial hazards are **features of the work**, identified and controlled by the PCBU |
| **G03 cl 1** | "proper consideration **must** be given to the [Code]… to ensure the **process**… identifies and manages psychosocial hazards and risks" |
| **EB12 cl 7.2.1** | supplies the risk-assessment mechanism |

⇒ A workplace risk assessment was asked of a general practitioner.

### C4. Q2 rests on a statement that is false on MSH's own record
> **Their premise:** *"As the Health Service **is not aware of any concerns being raised** for
> appropriate management"*

> **MSH's own objection, 5 June 2026, signed by the Chief Executive, Item 20:** *"the reference
> cited in the Notice being '**PID24-ESU-1130**' commenced in November 2024…"*

⇒ **Eight weeks earlier the Health Service addressed his public interest disclosure by reference
number, over the Chief Executive's signature.** Also on the record: the patient safety report; the
complaint of 4 October 2025 to the A/Director HR Business Partnering; two years of correspondence;
and WC/2024/227 itself.

### C5. "Primarily" — an undisclosed secondary purpose, against a statutory prohibition
> *"This information will **primarily** be used for the purposes of better understanding your
> condition and to support the implementation for appropriate controls"*

> **IP Act 2009, QPP 3.3** (sch 3; current 1 July 2026): "An agency **must not collect sensitive
> information** about an individual unless— (a) the individual **consents** and the information is
> **reasonably necessary for, or directly related to**, 1 or more of the agency's functions or
> activities…"
> **sch 5:** sensitive information includes "**health information**"; health information includes
> "the individual's **health at any time**" and "**a disability** of the individual at any time".

⇒ Collection of sensitive information must be tied to a stated function. **"Primarily" concedes
uses that are not stated.**

### C6. No power was ever identified
G03 is a **policy**. WHS ss 17 and 19 are **duties on MSH**. Neither confers a power to exclude a
worker, compel information, or debit leave.
**PS Act 2022 s 104** — the only statutory power to require a medical examination — **was never
cited**, and its **s 103** gateway requires absence or unsatisfactory performance: no performance
issue has ever been put, and **the absence is MSH's own act**. **s 105**, the only statutory link in
that division to leave, operates solely where an s 104(b) requirement is not complied with —
never invoked.

---

## PART D — THE CONCLUSION

**Fourteen identified errors across seven pages**, including two errors in a single five-word phrase,
a wrong policy number, an internal inconsistency on the same page, and pronoun drift between adjacent
questions.

**Five substantive failures**, each contradicting an instrument the letters themselves cite or are
governed by: the wrong test under G03, the reversed onus under G03 cl 2, a statutory duty put to a
GP, a false premise contradicted by their own Chief Executive's objection, and an undisclosed
secondary purpose against QPP 3.3.

**And the physical evidence:** exported at 11:10:27 and 11:11:02, signed with a stored image 25 and
75 seconds later, transmitted at 11:43, with the text unchanged throughout.

⇒ **These documents were not reviewed before they were sent.** The errors prove no proofread at any
stage; the timings prove the signature was applied to an unread document; and the substantive
failures prove that nobody checked the letters against the instruments they cite.

⚠️ **USE.** Errors 1–14 are for the union brief and the reserved tracks — raising typographical
errors in correspondence reads as petty and forfeits the register currently working. **Only C1, C2,
C3, C4 and C6 are deployed in the response, and each is argued on the instrument, never as a
mistake.** C5 is raised only as a neutral question about the handling of health information.
