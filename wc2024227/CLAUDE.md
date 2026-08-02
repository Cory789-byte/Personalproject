# CLAUDE.md — WC/2024/227 Working Project

This is the Claude Code project context for Cory Shepherd's QIRC workers' compensation appeal **WC/2024/227** (Shepherd v Workers' Compensation Regulator, s 550(4) WCRA, Commissioner Dwyer). Claude Code reads this file automatically at session start. Save this project to OneDrive and open the folder in Claude Code to work on the matter.

## Read these first, every session

0⭐. **`CURRENT.md`** — ⛔ **READ FIRST.** States which layer is live and which "FINAL" documents are
   superseded. Several files in `drafts/` are titled FINAL and are final **for their own date only**.
   The live package is `drafts/SEND_31JUL/` → `drafts/out/`, sending **Monday 3 August 2026**;
   the send map is `drafts/SEND_31JUL/MASTER_SEND_PACK.md`.
0. **`MASTER.md`** — the consolidated single pull-from point (state of play, findings, disciplines, open items, document index). Start here.
0a. **`corpus/FULL_CORPUS.md`** — ⭐ **the whole correspondence record in one searchable file**: 154 messages, 2020–2026, full text, chronological, each cited to its pack and page. **Grep this before opening any PDF.** Companion index at `corpus/MESSAGE_INDEX.tsv`; cautions at `corpus/README.md` — times are **UTC (+10 for AEST)**, and **nothing is quoted into a filing from the corpus**, only from the source PDF.
1. **This file** — standing context + the discipline rules below.
2. **`skill/SKILL.md`** and the relevant **`skill/sub-skills/*.md`** — the routed working method (drafting, evidence, disclosure mechanics, settlement, parallel tracks).
3. **`skill/references/confirmed-record.md`** — verified facts ONLY. Never rely on memory for a pinpoint; confirm here or in the source PDF.
4. **`working-notes.md`** — the live running log. Append to it as work happens.

## What this project is for

Running the WorkCover appeal at counsel standard, self-represented. The immediate live task is the **Rule 64G application** (deadline 12 June 2026). The standing posture: compel the records that sit only in Metro South HHS's systems, restrained and procedural, then build the case and settle on the enlarged record.

## The discipline rules (non-negotiable — full detail in skill/SKILL.md)

1. Conspiracy/collusion framing never reaches paper — use the *asymmetry*, held in reserve.
2. The word "fraud" never appears in the WC track — PID/reprisal track only.
3. Items 8–9 anchor ONLY to Stressor 1(a) (erratic presence) + the "roster was equitable" denial — never the reprisal or fraud.
4. File first, ask second. Communications to the Regulator wait until after filing+service, written only, never phone.
5. Neutral/procedural tone — Dwyer must discover MSH's problems himself.
6. Restraint as posture — concede what's available; it makes the rest grantable.
7. Severity = whole course of conduct — evidence-in-chief/medical/closing, not the 64G.
8. Parallel tracks sequenced BEHIND the WC settlement.
9. Settlement releases the COMPENSATION CLAIM ONLY — watch the deed scope.

## The cardinal habit

Keep **confirmed-against-source** strictly separate from **working-theory**. A memory reconstruction is a lead to verify, not authority. Before any pinpoint/date/quote enters a filing, open the source document.

## How to work in this project (Claude Code)

- **Source documents** live in `documents/` (you populate this from OneDrive — the actual PDFs: Form 9A, Form 24, the MSH objection, the Regulator's 11 June disclosure, the medical records, the rosters, the payroll). Claude reads them from there.
- **Drafts and outputs** go in `drafts/`. The current 64G build is the v5 application + draft order.
- **Append every session's work to `working-notes.md`** — what was done, what was verified, what's next. This is the continuity layer between sessions.
- When you finish a session, update `working-notes.md` and the "Current status" in `skill/SKILL.md`.

## Current status (UPDATE EACH SESSION)

**As at 2026-08-02. ⭐ See `CURRENT.md` for the live layer — the 3 August package is FINAL:
six documents, 26pp, five emails, zero placeholders, routing settled (Hughes on nothing, HR on
the Taylor email only, CE letter solo). Full-picture read + two addenda at
`skill/references/FULL-PICTURE-READ-1AUG.md` (employment 42%/63% favourable; appeal 68%).**

### ⚠️ Source-integrity rules added 1 Aug 2026
- ⛔ **ATT09 (QH-IMP-401-5) has NO TEXT LAYER** and no OCR is installed. **Never quote it from
  memory.** Render with `pdftoppm -r 150 -png` and read the page. Verified extracts are at
  `documents/instruments/ATT09_VERIFIED_EXTRACTS.md`.
- ⛔ **EB12 cl 3.9.1 is a Schedule 3 (Variable Working Hours) clause, not a main-body clause.** Do
  not cite it for work-now-grieve-later. For grievances: **cl 1.12.1 → Award cl 7.2**, plus
  **Schedule 2**, which lists **E12** and **E13** as preserved HR policies.
- ⛔ **ATT20 (AD Act) is current only to 19 May 2025** — the positive duty is not in it.
- ⚠️ **Grep PDFs only after `pdftotext`.** Grepping a PDF as a binary silently misses compressed
  text and produces false negatives.

- **64G / Form 29 — ✅ FILED AND SEALED 23 June 2026** (confirmed by Cory 31 July 2026), served on MSH 24–25 June. MSH's objection (ref K-LM26/729, 5 June 2026, signed Noelle Cridland CE; enquiries Myla Ruttan, Principal Lawyer) is on file, mined, and mirrored at `evidence-index/sources-text/`. **Mention 7 August 2026 before Dwyer; MSH required to attend.** Posture at the mention: ordinary procedural machinery — volunteer nothing about the employment dispute.
- **Settlement:** Calderbank #2 served **1 July 2026 at 12:16**, addressed to Matheson *and* the OIR appeals registry (service proof filed at `documents/2026-07-01_Cory_Calderbank2_covering_email_SERVICE_PROOF.pdf`); rejected 16 July 2026. Without-prejudice "material development" letter to Matheson **sent** 30–31 July.
- **Employment track — now the live front.** Excluded from the workplace since 3 July 2026: five weeks, no wages, accrued leave debited, medical costs self-funded. Six-plus position shifts; no instrument ever identified. **31 July 2026, 11:43 — Request for Medical Information (nine questions to Dr Ma), signed Scott Hughes, Director Corporate Services.** Response package built and ready at `drafts/SEND_31JUL/`.
- **Union:** Together Queensland — Heath Moran (background), Emily Petering (industrial officer). Not engaged on the appeal by their own demarcation; engaged on roster, pay and leave.
- Matter correspondence + the OneDrive "01 FINISHED APPEAL" folder ingested into `evidence-index/`. Full picture + de novo demolition in `skill/references/case-theory-synthesis.md` §15. Evidence source = Gmail + M365/OneDrive connectors (NOT the Trustandcollectiveco Outlook).

### Immediate tasks
1. ⭐ **MON 3 AUG — SEND.** Petering email first (the 13 July appeal-window question), then the
   four MSH emails per `drafts/SEND_31JUL/EMAILS_TO_PASTE_3AUG.txt`. Save every sent item as PDF
   into `documents/`.
2. **This week:** Dr Ma certificate covering from 3 July (obtain and HOLD); runway plan; the
   Appeals directive + s 102 directive; ask Cory whether the bounced 3 Oct 2025 email was ever
   re-sent successfully; his written account of 7am 24 Feb 2025.
2a. **Clocks:** Tue 4 Aug Stage 1 due · Mon 10 Aug refer Stage 2 (one line, does not
   self-execute) · Mon 17 Aug Stage 2 ends · ⭐ Mon 24 Aug cl 10.3.6 deemed refusal · ~8 Sep AD
   Act limitation (date with Petering) · appointments: rebook within 3 business days of MSH
   confirming the question set, or at day 7 of silence regardless.
3. **7 August 2026** — 64G mention before Dwyer.
4. Psychiatrist: **Report A** (MSH-funded — current capacity, functional restrictions, adjustments only) and **Report B** (appeal — causation and chronology) from one shared attendance. Scopes stay separate; Report A is silent on aetiology, as declared to MSH.
5. Obtain: the clinical note for 24 October 2024 *with consultation time*; the delivery email/timestamp for Review Decision 69983; the psychiatrist referral document and its date.
6. Verify the last shift actually worked before 2 July 2026 (the 2 July origin document implies the stoppage may predate it).

## Tooling notes

- The 64G was built with a Node script + the docx toolchain. If rebuilding in Claude Code, keep pagination spacing as-is (document is at its page ceiling).
- Filing: email to qirc.registry@qirc.qld.gov.au, business hours, under 30pp (PD 3/2021), cover line referencing K-LM26/729 and the 22 May direction.
