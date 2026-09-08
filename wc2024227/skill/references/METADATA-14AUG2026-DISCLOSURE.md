# FORENSIC METADATA — the Regulator's disclosure of 14 August 2026
> Extracted 14 Aug 2026 with **exiftool 12.76**, **pikepdf 10.11.0**, **qpdf**, **poppler**.
> Six files: the amended Form 23 List of Documents, the four sealed Form 29 NNPDs, and the
> covering email. Everything in Parts 1–3 is extracted fact; assessment is confined to Part 4.

---

## PART 1 — THE AMENDED LIST OF DOCUMENTS (Form 23)
`2026-08-14_Regulator_AMENDED_List_of_Documents_Form23.pdf` · 596 kB · 7pp · PDF 1.6 · linearized

| Field | Value |
|---|---|
| **Author** (Info + XMP dc:creator) | ⭐⭐ **Kerstin Bednarek** |
| Company | *(blank)* |
| ⭐⭐ **Created** (source Word doc) | **D:20180706 — 6 July 2018** |
| ⭐⭐ **LastSaved** (source Word doc) | **D:20181003 — 3 October 2018** |
| PDF CreateDate | 2026-08-14 **10:17:07** +10:00 |
| PDF ModifyDate | 2026-08-14 **10:17:14** +10:00 *(7 seconds — clean single-pass export)* |
| Creator / CreatorTool | **Acrobat PDFMaker 26 for Word** |
| Producer | **Adobe PDF Library 26.1.29** |
| Custom properties | `Tag_NewReviewCycle` *(empty)* · XMP-xmpMM **Subject: 269** |
| DocumentID / InstanceID | uuid:f64828fd-3289-4a3c-bd2a-4d8347d5cfc2 / uuid:bfe4a3bc-80d9-4cce-85c5-767c123d2a8a |
| Structure | **2 × %%EOF and 2 × startxref — the normal artefact of LINEARIZATION, not an incremental update.** qpdf reports only standard linearization hint-table warnings. **No hidden revision, no deleted content** |

## PART 2 — THE FOUR SEALED FORM 29 NOTICES
All four produced by one device. **No author, company or custom fields — scanner output only.**

| File | Title | Created | Pages |
|---|---|---|---|
| Mind & Memory | `SKM_C65825070415170` | **2025-07-04 15:17:08 +09:30** | 6 |
| Our Medical Ashmore | `SKM_C65825070415171` | **2025-07-04 15:17:20 +09:30** | 6 |
| Qld Health | `SKM_C65825070415172` | **2025-07-04 15:17:31 +09:30** | 6 |
| Qld Health (COVID leave) | `SKM_C65826042716390` | **2026-04-27 16:39:15 +09:30** | 6 |

- **Producer:** KONICA MINOLTA bizhub C658 · **Creator/CreatorTool:** KM_C658 · XMP Toolkit: Adobe XMP Core 5.2 (2010)
- ⭐ **The 2025 three were scanned in one continuous batch** — twelve seconds apart, sequential
  file numbers 170 → 171 → 172, at **15:17 on 4 July 2025**.
- ⭐ **Same physical device ten months apart.** All four DocumentIDs share the device prefix
  `6b3d8e09`.
- ⭐⭐ **THE TIMESTAMPS ARE SELF-CORROBORATING.** The DocumentID encodes the scan time in hex:
  `6b3d8e09 **07e9 04 0f** …` = year **0x07E9 = 2025**, day **04**, hour **0x0F = 15**;
  `6b3d8e09 **07ea 1b 10** …` = year **0x07EA = 2026**, day **0x1B = 27**, hour **0x10 = 16**.
  Both match their stated CreateDate exactly. **No indication of altered timestamps.**
- ⚠ **Timezone +09:30 on all four** — ACST (Adelaide/Darwin), not Brisbane's +10:00. ⛔ Most likely
  a misconfigured device clock. **Weak signal. Note; do not build on it.**
- Structurally clean: single %%EOF, qpdf reports no syntax or stream errors.

## PART 3 — THE COVERING EMAIL
`2026-08-14_1028_Matheson_amended_LOD_and_NNPDs_covering_email.pdf` — **Producer: Microsoft: Print
To PDF · Author: Cory Shepherd · Title: "Mail - Cory Shepherd - Outlook"** ⇒ **his own print**, not
a Regulator artefact. Created 2026-08-14 10:37:12, ten minutes after Matheson's 10:28 email.

---

## PART 4 — ⭐⭐⭐ THE ASSESSMENT: TODAY'S DISCLOSURE SUPPLIED THE CONTROL SAMPLE

**Four classes of document from the Regulator's side can now be compared directly:**

| | Author | Company | Matter-specific custom fields |
|---|---|---|---|
| **WCRS Attachment, 18 Aug 2022** | Microsoft Office User | **DJAG** · `Angela.Sense@oir.qld.gov.au` | SharePoint `ContentTypeId`, `BusinessUnit` |
| ⭐ **Amended LOD, 14 Aug 2026** | **Kerstin Bednarek** *(from a 2018 source doc)* | *(blank)* | ⭐ **NONE.** One empty tag and a numeric subject |
| **Form 29 notices ×4** | *(none)* | *(none)* | *(none — scanner output)* |
| ⛔ **Review Decision 69983, 24 Oct 2024** | **HopgoodGanim Lawyers** | **HopgoodGanim Lawyers** | ⛔⛔ **SIX, ALL POPULATED WITH THIS MATTER**: matter 2440758 · doc 29218845v1 · user hendry8286 · addressee *"Worker applicant - Mr Cory Shepherd"* · description *"Reasons for decision - WCR reject"* · date 09.10.2024 |

⭐⭐⭐ **THE FINDING.** The amended LOD is a textbook stale-template artefact from the Regulator's
own output: an **author name from 2018**, a **source document created and last saved in 2018**, and
**no matter-specific data of any kind**. It is exactly what the "stale template" explanation
predicts a document should look like.

⇒ **The Review Decision does not look like that.** The stale-template explanation was excluded on
8 August by reasoning; **today's disclosure has now independently demonstrated what a genuine stale
template in this agency's documents actually looks like — and it is not the Review Decision.**

⭐ The control sample arrived from the Regulator's own hand, unprompted.

## 4.1 ⚠ THE COUNTERPOINT THAT MUST BE STATED FAIRLY
**Acrobat PDFMaker is the Regulator's own toolchain.** The LOD is PDFMaker **26**; the Regulator's
SOFC of 13 May 2026 is PDFMaker **26**; the Review Decision of Oct 2024 is PDFMaker **24** — normal
version progression across two years. ⇒ ⭐ **The Word→PDF toolchain is NOT a discriminator and
must never be argued as one.** The only discriminator is the **populated DMS field set**.

## 4.2 ⛔⛔ THE RULE, RESTATED — IT NOW APPLIES TO A SECOND NAME
**Kerstin Bednarek is almost certainly the person who created the Form 23 template in 2018.** The
2018 creation and last-saved dates make that plain, and the document contains no matter-specific
data connecting her to anything.
⛔ **DO NOT research, name, or pursue her — for exactly the reasons already recorded for
`hendry8286`.** System identifiers and template artefacts: yes. A person's name: never.

## 4.3 WHAT IS **NOT** ESTABLISHED
- Nothing about who prepared the Review Decision's reasoning.
- Nothing about whom HopgoodGanim acted for.
- Nothing improper by anyone.
- The +09:30 timezone means nothing on its own.

## 4.4 INTEGRITY
**Every file disclosed today is forensically clean.** No incremental updates, no hidden layers, no
deleted content, no altered timestamps, no encryption. The scan timestamps are corroborated by
their own embedded identifiers. **The Regulator's disclosure is what it appears to be.**

---

## PART 5 — WHAT THIS CHANGES FOR THE LETTER
**Nothing in the letter needs to change.** But the answers now have a benchmark:
1. If the reply says the Author field is a template artefact, the LOD is the example that shows
   what that looks like — and the Review Decision does not match it.
2. The letter already asks the right question at 3(d): **what the fields refer to.** The control
   sample means an unsatisfactory answer will be visible as unsatisfactory.
⛔ **Do not put this comparison in the letter.** It is analysis, not enquiry, and it converts a
question into an argument.
