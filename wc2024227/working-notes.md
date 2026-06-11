# Working Notes — WC/2024/227

Running log. APPEND newest entries at the top. Each entry: date | what was done | what was verified against source | what's next.

---

## 2026-06-11 — Session: matter folder integrated into git (Personalproject repo)

**Done:**
- Whole project (CLAUDE.md, skill + sub-skills + references, working-notes) committed to the private `Personalproject` repo under `wc2024227/`, on PR #9 branch (`claude/workcover-matter-repo-krg8qg`). Primary documents filed in `documents/`; index in `wc2024227/README.md`. Matter thread doc (`source_documents/WC2024227_MATTER_THREAD.md`) updated to the verified record.
- Textual pre-filing checks run on the uploaded `WC2024227_Form4_Rule64G_Application2.docx`: it is an EARLIER draft, not v5 — contains the uncorrected "Respondent carries the onus" framing, no Section G, `[street address]`/`[telephone]` unfilled. (Good: no "1 July 2024" Hawes reference, no case-law citations, no "fraud".)

- Full metadata + content-date extraction across the 11 June bundle and the MSH Item 11 production → `documents/METADATA_REGISTER.md`; confirmed facts migrated to `confirmed-record.md`. Headlines: bundle is 10 pp (revision-1 `/Count` = 4, expanded in the 11 June 10:56 re-save); six-minute PID routing now on the face of pp 7–8; exact leave-form 15480560 history timestamps captured; Item 11 prints authored by Ruttan (29 May / 2 June), myHR report from native .xlsx, PRNs 15397775/15605601 absent; new unknown name "Estelle Bain" (Item 11 myHR session banner); 22 May direction text recovered (MSH non-attendance at the mention; objections due 5 June 4 PM).
- Matheson 11 June cover-email screenshot filed (`documents/2026-06-11_Matheson_disclosure_cover_email_screenshot.jpg`). A second uploaded screenshot (Ryan Yaun email, 21/08/2025, DVO struck out / "another officer from Southport... incorrectly used my original Police occurrence") is QPS-track — filed in the QPS repo side (`source_documents/`), NOT this matter, per parallel-tracks discipline.

**Verified against source this session:**
- Application2.docx structure (6 sections + Schedule A) and the onus wording — read from the document itself.
- All metadata-register entries — extracted directly from the files in `documents/` (raw Info dict + XMP + rendered pages).

**NOT yet verified / OPEN:**
- The v5 FINAL filing files are NOT in this repo — they were in a prior session's `/mnt/user-data/outputs/`. **Recover or rebuild before the 12 June deadline — do not file from Application2.docx.**
- The four pre-filing verifications from the filing checklist still require the Form 24 response document (not in this upload batch).

**Batch 2 + Form 24 (same session, later):**
- Integrated: 4 directions orders (3 Jun / 16 Jul / 22 Aug 2025, 7 Apr 2026), Notice of Listing 22 May 2026, the 25–27 Feb 2026 stamped filings (supplementary Form 4 + affidavits; Form 4 Disclosure + affidavit), **Review Decision 69983 in full** (factor-4 unreasonableness; *Delaney* global evaluation; 8-hour agreement signed 17 June 2020), Saines costs agreement (26 Nov 2024), Form 35 (withdrawal of Saines/Conrad), listing .msg chain (Form 24 served 11 Feb, receipt 12 Feb; mention 26→27 Feb at Matheson's request, r 49(2) reserved), Quatrix screenshots, April-2025 switchboard stats xlsx (load profile — hold, do not serve), mailbox export manifests (provenance), **and the Form 24 response itself (dated 18/02/2026; PDF author "Stephen Gray")** — the pinpoint-verification source is now in-repo.
- Procedural spine in confirmed-record.md substantially extended (review decision → 22 May 2026 mention).
- **⚠ Representation-timeline tension flagged in confirmed-record:** Form 35 (Saines/Conrad) carries a 22 Aug 2025 export timestamp and the 22 Aug 2025 order responds to the Appellant's OWN 21 Aug correspondence — vs the record's previous "self-rep since ~9 Feb 2026". Resolve before anything relies on it.

**Batch 3 (same session, later still):**
- Integrated the 14 July 2025 Quatrix production (QH Payroll 24 pp; witness-conferencing **Tammy Reese** 50 pp; FRMS part 47 pp) → `documents/disclosure-2025-07/` — contradiction-matrix source now local. Original Regulator Form 9C SOFC (6 pp). **Hawes Work Capacity Certificate images** — resolves the "1 July 2024" mystery: that is the certificate's *first seen for this injury* date; signed 8 Sept 2024 ✓. ESU PID complaint form (E5 Att 1). **TD/2024/110** reinstatement application (stamped 25 Oct 2024, v Queensland Health Logan Hospital) → `related-matters/` — separate matter, parallel track. "Chloe Work" text-message evidence (incl. 4 Apr 2023 roster board). Dups skipped (3 Jun order copy; 22 Aug order alt scan; sainsindex = AFDO-2 copy; .bin = .jpg).

**Batch 4 (same session):**
- Integrated: the **v5 Rule 64G Draft Order** (docx+pdf, verified against the documents-and-64g.md spec — consistent, recites the application dated 11 June 2026); **Cory's Form 29 as sealed 22/04/2026** (15 pp, Registry seal); the **Amended Form 9A SOFC** (the three-stressor pleading incl. 1(a) erratic presence and the Mahaffey argument); Exhibit B4 (original Form 9C Statement of Reasons); QIRC appeal guides (reference). Second copy of the 11 June disclosure verified byte-identical, skipped.
- v5 APPLICATION FINAL still missing from every batch — only the draft order has surfaced.

**v5R rebuild (same session, final):**
- Application REBUILT as v5R (original v5 FINAL never recovered): `drafts/WC2024-227_Rule64G_FILING_v5R_FINAL.pdf` (7 pp A4) + editable docx. No case law (re-confirmed by Cory). Validated 33/33 — every Form 24 pinpoint machine-checked against the in-repo response; stress-test in `drafts/VALIDATION_REPORT_v5R.md`. Draft order unchanged (original v5 output). Skill files updated for chat use (status, file locations, theories §2–3).

**Next:**
- 12 June, before lodgement: the three eyeball checks in VALIDATION_REPORT_v5R.md (Schedule A vs sealed Form 29; C2–C4 vs the 5 June letter; confirm phone/address). Then lodge to qirc.registry@qirc.qld.gov.au referencing K-LM26/729 + the 22 May direction; serve Regulator + MSH; TQ courtesy note; silence. Index email to Matheson the day after service.
- Post-order: contradiction matrix from the Reese witness-conferencing bundle (now in `disclosure-2025-07/`); IP access-log request (operator 105777, "Renee Dawson", "Estelle Bain"); July 2025 diff.

---

## [DATE] — Session: 64G build v5 + skill creation

**Done:**
- Built Rule 64G application v5: stripped ALL case law (per instruction); added full-scale Section G (the 11 June disclosure — records exist / production frictionless / breadth confirmed); corrected onus to Appellant; Annexure C trimmed to the single headed McGinley page. Validated to zero defects, 7 body pages + Annexure C.
- Read the actual Form 24 response in full and corrected the reconstructed schedule (see confirmed-record.md). KEY: medical records obtained under a Form 29 Registry-signed 4 July 2025 (¶23); IRO finding admitted as DOCUMENT, relevance reserved to Commission (¶34); Hawes certificate dated 8 Sept 2024 not 1 July (¶33); pay disparity DENIED with "roster was equitable" (¶39).
- Built this project + the wc227-matter skill (router + 5 sub-skills + 3 reference files).

**Verified against source this session:**
- Form 24 full response document (read in full).
- Regulator 11 June disclosure PDF metadata (container 6 May; McGinley email never addressed to Cory).
- PID complaint form (13 May 2024) + ESU closing letter (Loader, 24 Dec 2024).
- July 2025 Quatrix/extension emails; Feb 2026 filing; 2 March 2026 Notice of Listing.

**NOT yet verified (do before filing):**
- Form 24 pinpoint NUMBERS as cited in the 64G against the source (numbering offset from ¶34).
- That Section D frames the IRO point as persuasive not binding.
- That no "1 July 2024" Hawes reference survives anywhere in the build.
- No conflicting live 9 Feb 2026 direction.

**Next:**
- File the 64G (12 June). Fill address/phone. Lodge to Registry. Serve. TQ courtesy note. Silence.
- Day after service: index email to Matheson (Form 29 / 64D questions).
- Post-order: contradiction matrix from the 52MB witness bundle; IP access-log request; July 2025 diff.

---
