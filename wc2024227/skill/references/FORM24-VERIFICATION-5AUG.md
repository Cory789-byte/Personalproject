# FORM 24 — FULL VERIFICATION OF EXHIBITS AND CLAIMS
> 5 August 2026. Every one of the 50 Notice paragraphs read from the **rendered pages**, and
> checked against the Respondent's Response and `confirmed-record.md`.
> ⚠ Contains references to sensitive medical material. Internal only.

---

## ⛔ 1. INTEGRITY WARNING — THE TEXT LAYER IS INCOMPLETE

`2026-02-18_Form24_Response_and_email_communication.pdf` has a text layer that **omits every
exhibit reference, every date, and every quoted phrase** in the Notice.

`pdftotext` returns: `In the Review Decision dated ( , p. 27)…`
The page actually reads: **`In the Review Decision dated 24 October 2024 (Exhibit B1, p. 27)…`**

No AcroForm, no field values — the missing runs simply do not extract. **Any analysis of the
Form 24 done from `pdftotext` output is incomplete and will silently miss every exhibit.**

⇒ **RULE: render the Form 24 with `pdftoppm -r 150 -png` and read the pages.** Same class of
problem as ATT09 (CLAUDE.md source-integrity rules). Add the Form 24 to that list.

## ⚠ 2. THE NOTICE AS FILED IS UNSIGNED AND UNDATED

Page 6: **Signature blank · Print name blank · Title of office held blank · Date blank.**
Page 1: **Matter Number blank · Respondent field blank · "To:" field blank**, and the radio
button is marked **● respondent** ("the respondent … proposes to prove the facts") when the
facts are the Appellant's.

⇒ Either the repo holds a working copy rather than the served version, or the form went out
incomplete. **The Respondent's paragraph-by-paragraph Response of 18 Feb 2026 cures any doubt
about service** — you do not answer 44 paragraphs of something you never received — but
locate the executed copy.

## 3. THE EXHIBIT REGISTER (recovered from the rendered pages)

| Exhibit | What it is | Cited at Notice ¶ |
|---|---|---|
| **A1** | Work Capacity Certificate, Dr Peter Hawes | 36 |
| **A4** | Dr Ravikumar Krishnaiah — MDD diagnosis 13 Feb 2025; **p. 5** the premature-exposure opinion | 38, 39 |
| **A5** | Medical records from "Our Medical Ashmore"; **p. 48, 50, 52, 53**; p. 52 = the De Silva Nanayakkara entry of 16 Nov 2023 | 23, 24, 26–29, 33, 34 |
| **B1** | Review Decision 24 Oct 2024 — **p. 16** causation finding · **p. 27** unreasonable-management-action finding | 2, 37, 50 |
| **C2** | Roster, 17–18 March 2024 | 1 |
| **D1** | Employee Payslip Comparison | 42, 43 |
| **D2** | AVAC submitted 28 May 2024 | 41 |
| **E1** | Email bundle — **p. 10** Taylor→Reese 6 Jun 2023 4:05pm · **p. 20** Reese 7 Aug 2023 | 5, 10, 14 |
| **E2** | Payroll bundle — **p. 236** Taylor 21 May 2024 12:33pm · **p. 237** Grant instruction 3 May 2024 | 40, 46, 47 |
| **E3** | ESU PID determination, 24 Dec 2024 | 20 |
| **E5** | Reese retraction email 15 May 2024; Taylor's comparator email 9 May 2024 | 21, 22 |
| **F1** | Fatigue Risk Management Policy | 3 |
| **F2** | QH-POL-248 Union Encouragement Policy | 17 |
| **F3** | Delegate-intent notification, 11 Aug 2023 | 18 |
| **H1** | Service on former solicitors 22 Jul 2025; Matheson email 14 Jul 2025 | 30, 32 |
| **I2** | Carolyn Jeffrey statement — **also cited for the communication-book removal at ¶6** ⚠ same exhibit, two different subjects; confirm I2's contents | 6, 13, 15 |

⛔ **THE NUMBERED EXHIBIT BUNDLE IS NOT IN THE REPO under these labels.** Underlying content
exists for some (Hawes certificate images, Review Decision 69983, the ESU PID form) but the
A/B/C/D/E/F/H/I bundle as served is not filed. **Locate it before the hearing** — every
pinpoint above depends on it.

## 4. ARITHMETIC — CHECKED

| ¶ | Claim | Check |
|---|---|---|
| 41 | AVAC delay of **25 days** | 3 May → 28 May 2024 = **25 ✓** |
| 47–48 | Instruction held **18 days** before the 21 May email | 3 May → 21 May = **18 ✓** |
| 44 | Disparity **$5,411.46** | 18,169.14 − 12,757.68 = **5,411.46 ✓** |
| 44 | "approximately **42%**" | 5,411.46 ÷ 12,757.68 = **42.4%** ✓ as a proportion of *his own* gross. ⚠ **AMBIGUOUS** — as a proportion of the comparator's it is **29.8%**. A reader may take "42%" to mean he received 42% less than the comparator, which is wrong. **Say "he received $5,411.46 less, being 42% of his own gross for the period"** |

## ⛔ 5. CLAIMS THAT DO NOT SURVIVE — DO NOT REPEAT THESE

**¶25 — "breach of Rule 64E".** ⛔ **FAILS.** Per the Subdivision 7A verification in
`confirmed-record.md` (checked verbatim against sl-2011-0237): **r 64D(1)(a)** requires service
on a person *"other than a party"* — Cory **is** a party and is carved out. There was no duty
to serve him, and **r 64E is an objection right, not a service duty**. **Never plead a service
breach or "unlawfully obtained".** The remedy is **r 64E(2)** — leave to object at any time,
on grounds **(e) confidential nature** and **(f) effect on any person** — plus s 580 and
relevance/prejudice.

**¶23 — "full medical history".** DENIED, and correctly: there **is** a Form 29 for the medical
records, **signed by a Senior Registry Officer on 4 July 2025**, received before 16 July 2025.

**¶24 — "system-generated footer".** Does not survive. There is **no footer**; page one states
the records were printed 8 July 2025.

**¶36 — the Hawes certificate "dated 1 July 2024".** ⛔ **THE NOTICE IS WRONG ON THE DATE.**
The Respondent corrects it: **signed 8 September 2024**. Fix every citation that says 1 July.

**¶35 — "not in possession of any contemporaneous medical evidence prior to 2024 that
contradicts".** ⚠ **CONTESTED, and this is the live risk.** The Regulator asserts the records
show **anxiety and ADHD history from 26 October 2022, "missing from Exhibit A5"**. That cuts
directly at the clean-baseline proposition at ¶¶33–35. **Do not run the clean baseline as
though it is unanswered.**

**¶15 — the yelling particular.** ⚠ **HEARSAY.** Jeffrey **did not witness it**; she was told
by Cory. Her email of 18 July 2024 is admitted as saying what it says (¶13), but the
underlying event is not corroborated by an eyewitness.

**¶31 — distress and breakdown of representation.** Not admitted, "matters within the
Appellant's knowledge". Requires his own evidence.

**¶32 — Matheson's 14 July 2025 email.** Admitted as sent, and admitted to have been sent in
error to him rather than his solicitors — **but the Respondent says the medical records "were
not in the possession of the Regulator at the time"**. The non-disclosure inference at ¶32
therefore does not hold on the Respondent's account.

## 6. PARAGRAPHS WITH NO EXHIBIT AT ALL

**4, 7, 8, 9, 11, 12, 16, 19, 25, 31, 35, 44, 45, 48, 49.**

Of those, **11, 12, 16, 45, 48 and 49 are characterisation or argument rather than fact** —
a pop-culture inference, a "social clique lens", what "constitutes unprofessional conduct",
what "demonstrates a lack of diligence". A notice to admit facts should contain facts, and the
Respondent declined each of them on exactly that basis. **Lesson for any future Form 24: plead
only what a document proves.**

⭐ Note the exception: **¶8 has no exhibit and was still ADMITTED** — the patient-safety
criticality. That admission is the strongest single sentence in the Form 24 and it was obtained
without any document at all.

## 7. WHAT SURVIVED, AND IS WORTH MOST

| ¶ | Fact | Status |
|---|---|---|
| 1, 3 | The 7-hour break; the 10-hour minimum | **ADMITTED** |
| 5 | Reese: "a rostering error … accidentally made by Chloe with regards to night shifts" | **ADMITTED** |
| 6 | Taylor removed the communication-book page | **ADMITTED** (not the handwriting) |
| **8** | ⭐ **Switchboard contact-detail accuracy is critical to clinical handover and patient safety** | ⭐ **ADMITTED** |
| 17 | QH-POL-248 requires a "positive, supportive role" | **ADMITTED** |
| 20 | ⭐ The ESU determined the complaint a **PID** | ⭐ **ADMITTED** |
| 21 | Reese directed retraction, 48 hours after the PID | **ADMITTED** — causation contested |
| 25 | No Form 29 served on him before the records were obtained | **ADMITTED** — but no breach follows |
| 37 | Review Decision: "employment was a significant contributing factor" | **CONTENTS ADMITTED**, relevance reserved |
| 40, 41 | The payroll instruction; the 25-day AVAC delay | **ADMITTED** |
| 46 | Taylor's 21 May "waiting payroll confirmation" email | **ADMITTED** |
