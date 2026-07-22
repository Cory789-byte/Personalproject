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

**v5 ORIGINAL recovered + assessed + cleaned (12 June, pre-lodgement):**
- The original v5 application docx + FILING_v5_FINAL.pdf + 12-June draft order revision all surfaced. Assessed against the MSH response engagement and the skill: the original v5 is the RICHER document (written with the 5 June letter in hand — item-by-item grounds, MSH's own Item 19 narrowing, the Item 20 PID-reference-number explanation). Pinpoints verified: v5 cites Form 24 NOTICE numbering consistently, matching the response's own "With respect to paragraph N" usage — all pinpoints check against the response text.
- Three fixes applied → v5.1: (1) `[street address]` filled (15 Edmond Street, Coomera, per sealed Form 29); (2) IRO citation qualified "contents admitted, relevance reserved to the Commission" (checklist item 2); (3) equitable-roster anchor added to Annexure B Item 8 (¶¶42–45: "the roster was equitable" — verified verbatim in the response).
- Metadata scrubbed: docx props emptied (creator/lastModifiedBy/app/custom removed); zip timestamps neutralised; assembled PDF carries NO Title/Author/Creator/Producer; original Annexure C page (p8) reused. The 12-June draft order PDF verified already clean (no author/creator/producer/XMP).
- **LODGE: `drafts/WC2024227_Rule64G_FILING_v5.1_FINAL_CLEAN.pdf` + `drafts/WC2024227_Rule64G_Draft_Order_12June_CLEAN.pdf`.** v5R (the rebuild) stands down as backup. Remaining before sending: eyeball Schedule A vs the sealed Form 29; confirm phone 0417 400 227.

**Signed reproduction (12 June, final):**
- Cory's Samsung-signed copy found to have DROPPED the three italic statute names (Samsung re-render bug): gaps at "Industrial Relations (Tribunals) Rules 2011", "Workers' Compensation and Rehabilitation Act 2003" (D-section), and "Public Interest Disclosure Act 2010" (Schedule A terms) — the "mistake and spaces" Cory spotted. Signature extracted as pure strokes (the Samsung overlay was a separate transparent image) and embedded into the CLEAN docx; rebuilt A4; all three dropout points verified fixed; signature renders on the line above the name. Metadata empty. **Lodgement file replaced: `lodgement/WC2024227_Form_4_Application_Rule_64G.pdf` is now the SIGNED clean version (8 pp).** Signed master: `drafts/WC2024227_Application_v5.1_signed_master.docx`.

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

## 2026-06-27 — Cloud evidence ingest + Review Decision forensics

**Review Decision (Squires, 24 Oct 2024) forensic pass** — analysis only, hearing/strategy track:
- The conclusion is load-bearing on a counting error: doctor (via comms report) gave FOUR
  causative factors; she listed four; the conclusion counts "two of THREE" — Factor 1 (rules/
  union) silently dropped at the substantiation gate, against the evidence (union policy held +
  union forwarded the delegate forms; EB11 s 1.9 never obtained). Restore it → 2-of-4 (tie/worse).
- Pay/Covid mislabelled "blemished but resolved": the duty is timely correct payment, so the
  delay/3× Covid declines ARE the breach, not cured by the fix; also Factor 1 (rule non-adherence),
  not just Factor 3. Tally: 1 breach conceded (10-hr break), ≥7 actual across 5 instruments.
- Frame stays "error not bias" + de novo cures the thin record — NOT on the 64G.

**Evidence ingest — OneDrive `01 FINISHED APPEAL`** (via M365 connector; user-supplied .lnk path).
Built `evidence-index/` (README + 01-FINISHED-APPEAL manifest + sources-text/ mirror). Findings:
- Folder is clean WC (no QPS/DV co-mingling). Mostly already in repo: MSH 5 June letter is
  BYTE-IDENTICAL to documents/2026-06-05_MSH_Objection_KLM26-729_Cridland.pdf; Regulator SOFC +
  Outline already present. New = 4 Correspondance/corro PDFs but ALL image-only (no text layer) →
  content not extractable via connector; indexed as pointers (Factor 3 pay, Factor 4/FRMS, Item 10
  redaction/disparate-treatment). Need OCR/originals to ingest content.
- Saved greppable text mirror of the MSH letter. Confirms an internal contradiction: Item 3(c)
  "no consequential changes" vs Item 5 "organisational change related to the reporting lines for
  Switchboard" — already trapped by Draft Order Schedule C Item 3(c).
- NOTE: connected M365 OneDrive heavily co-mingles the QPS/DV/Alexia Negro criminal matter +
  third-party data — EXCLUDED from the index per discipline; never bulk-ingest that store.

**Next:** OCR the 4 image PDFs (or drop originals into documents/) to ingest content; then promote
verified facts to confirmed-record. Optional: de novo hearing note (denominator collapse + union
limb + pay-timeliness/Covid), kept clear of the 64G.

## 2026-06-27 (cont.) — Email correspondence ingested + LIVE STATUS UPDATE

Ingested WC/2024/227 procedural email correspondence from the coryshepherd1@hotmail.com
mailbox (Gmail connector) → `evidence-index/communications-register.md` (timeline + cadence
analysis + orders + quarantine of the reprisal/collateral emails). Key STATUS changes vs the
skill's record (which assumed filing ~12 June):
- **64G application FILED & SEALED 23 June 2026** (Form 4 + Form 20), circulated by Registry
  24 June (= the last QIRC email). The 12 June attempt was REJECTED by Registry 14 June on
  format; refiled corrected 23 June. Served on MSH (Ruttan) 24 June.
- **NEXT LISTING: 7 August 2026 before Dwyer — Myla Ruttan / MSH REQUIRED TO ATTEND** (notice
  15 June). This is the 64G/objection hearing.
- Signal: MSH minimal & appearance-averse (no-show at the 22 May mention, Commissioner noted
  it; now compelled to attend). Matheson diligent, rejected Calderbank #1 (18 Feb: "defending
  the appeal") yet made the 11 June adverse disclosure — the seam holds.
- **Calderbank #1 was Feb 2026, flatly rejected on the thin record.** The current Calderbank
  question is therefore a RENEWED offer — hold until post-7-Aug production per settlement.aml.
- Connected M365 (CoryShepherd@Trustandcollectiveco) Outlook is a near-empty admin mailbox —
  NOT where the legal mail lives. The legal correspondence is in the hotmail/Gmail account.

## 2026-06-27 — FULL-PICTURE ASSESSMENT (6-agent workflow + adversarial red-team)

Grades: merits 7 (unreasonableness limb ~70-80%, but OVERALL ~50-65%); disclosure/64G 8
(~80-85% some production, likely VARIED); settlement 8 (acceptance ~10-20% now / ~60-80%
post-production); risk 6; procedural 7. Modal path = settle post-production.

THE ONE THING THAT COULD LOSE IT = MEDICAL CAUSATION (red-team, verified):
- Hawes WCC (08.09.2024) diagnoses "anxiety, stress" — NOT MDD as the north star/CB draft say
  — and mechanism is "bosses victimising him," roster mentioned NOWHERE.
- Regulator operative SOFC (13.05.2026) para 22(f) expressly DENIES causation; pleads
  pre-injury anxiety/ADHD; seeks COSTS vs the self-rep. Onus on Cory (Davis v Blackwood);
  Mahaffey needs the 7-hr break a SIGNIFICANT contributor. Psychiatrist report does not exist.
  Causation currently points the WRONG way. Everything funnels through it.

CORRECTIONS (I/we were overconfident this session):
- "Denominator collapse" is NOT a counting error: Squires gave a REASONED non-substantiation
  of Factor 1 (union delegate = union's responsibility; recruitment complied). It's a merits
  fight to OVERTURN at hearing, can be lost — not arithmetic. (Underlying critique survives.)
- It's an 8-HOUR minimum, not 10: Review Officer found the breach on "award AND the 8-hr
  agreement" (assumed 8-hr applied, still breach). Regulator pleads "7 rather than 8." Fixed
  in Calderbank draft para 6.
- MDD vs "anxiety, stress" discrepancy — resolve in the medical evidence.

ACTION ITEMS (new, surfaced by red-team — none previously flagged):
1. 64G TIMELINESS: operative app sealed 23 June = 18 days after the 5 June objection; r 64G(1)
   wants 7 days. 12 June attempt bounced for format. Relation-back/leave is DISCRETIONARY.
   Verify it's properly on foot before 7 Aug.
2. ITEM 8 WITHDRAWN in the operative filing ("duplicates Item 9") — but Item 8 (AD/Entra
   sign-in) was the load-bearing ABSENCE proof. Confirm intended; confirm CS-1..CS-4 vetted.
3. s 42 PID LIMITATION CLOCK — still uncomputed; events ~2 yrs old; may already be barred.
   Compute TODAY, independent of WC timing. Deferral premise is asserted, not proven.
4. Calderbank draft 10hr->8hr — DONE.

## 2026-06-27 — Ingested "Qirc REG Filed forms" (operative filed instruments)

Ingested the filed-forms OneDrive folder. New greppable sources: Regulator SOFC (13.05.2026),
Amended 9A (07.04.2026), the 23 June Form-4 covering email. Manifest: evidence-index/QIRC-REG-FILED-FORMS.md.
Quarantined the E1-LTR collateral bundle (reprisal/PID) — off the WC track.

ASSESSMENT UPDATES (the filed forms resolve 3 of the 4 red-team action items):
1. 64G TIMELINESS — SUBSTANTIALLY DE-RISKED. Covering email: "the corrected re-filing... of the
   application made on 12 June 2026." 5 June objection + 7 days = 12 June = day 7 = ON TIME. The
   23 June seal is a format re-file of an on-time app, relation-back framing on the record. (Still
   Commission's discretion to accept relation-back, not automatic.)
2. ITEM 8 — CONFIRMED WITHDRAWN. Operative Draft Order v2 presses 1,2,3(a),3(b),9,10,19. Item 8
   (AD/Entra sign-in) OUT; Item 9 (building access, MSH's hardest objection) is the only presence proof.
3. MDD DIAGNOSIS EXISTS (Krishnaiah; 9A injury = MDD DSM-5 296.23) — red-team's "no psychiatrist"
   overstated. BUT Regulator SOFC ¶9 does NOT admit it; no medical yet ties injury to the ROSTER.
4. s 42 LIMITATION — still uncomputed (not addressed by these docs). STILL OPEN.

SOFC (operative defence) confirms the hard line: ¶8 pre-injury anxiety history (attacks clean baseline);
¶10 admits Hawes SAYS "victimising" but denies it as fact; ¶16 "Ms Reese was UNAWARE of the PID" (defeats
the reprisal causal link); ¶22(a) 7-hr "rather than 8-hr... human error, not intentional or repeated",
22(b) "could refuse shifts at anytime", 22(e) signed June 2020 8-hr agreement, 22(f) "NOT causative";
¶24(b) cl 18.10 Award denies fatigue leave (no overtime); decision sought incl. COSTS against the self-rep.
NOTE: the 9A itself overstates "10-hour minimum (Form 24 Para 3)" — same error as the Calderbank (now fixed);
live minimum is contested/8-hr.

## 2026-06-27 — PID/REPRISAL TRACK research + integration (PARALLEL TRACK — off the WC track)

New file: skill/references/pid-reprisal-track.md. Pulled the PID materials from OneDrive (ESU
outcome letter 24-ESU-1130, 24 Dec 2024; ESU complaint; reprisal narrative) and integrated with
the statutory framework.

PID determined a PID 24 Dec 2024 (Janelle Loader, ESU) on the 30 Aug 2024 CCC complaint (referred
to MSH 22 Nov 2024); plus the 13 May 2024 ESU complaint also a PID. Reprisal protection = ss 40-42
PID Act. s 42 = reprisal IS A TORT, damages incl. exemplary, District/Supreme Court, WCRA does NOT
apply (so the tort survives a WC settlement unless a deed releases it).

LIMITATION — the standing "verify soon" action item, now COMPUTED (research, not formal advice):
- 3-YEAR limitation (Limitation of Actions Act s 11, personal injury) is OPEN — cause accrued
  ~mid-2024 (reprisal 15 May / injury 18 June / termination 8 Oct 2024) → runs to ~May-Oct 2027.
  NOT time-barred. (Red-team's "possibly already fatal" was too pessimistic on the core clock.)
- PIPA Part 1 Notice of Claim (if PIPA applies) = 9 months from the incident → ~Feb 2025 / Jul 2025
  = LIKELY ALREADY PASSED. Late notice possible with reasonable excuse (PIPA s 9A); late != barred.
- Whether PIPA applies to a PID reprisal psych-injury claim is genuinely arguable — needs a
  SPECIALIST. Action: get personal-injuries/whistleblower advice NOW; give any PIPA notice promptly.
- The psychiatrist causation report serves BOTH tracks (reprisal needs the same injury causation).
- DEED RESERVATION (ss 40-42 + MSH) is non-negotiable in any WC settlement (rule 9) — already in
  the Calderbank para 3.

## 2026-07-01 — Calderbank #2 SENT + a COSTS CORRECTION I owe the record
Cory SENT a renewed, counsel-grade Calderbank on 1 July 2026 (open 21 days, ~22 July), to the
Regulator only. Text: evidence-index/sources-text/Calderbank_SENT_2026-07-01.txt. Assessment:
- STRONGER than the held template: full legal argument (inaction/omissions -> s 32(5)(a) not engaged,
  Read/Allwood; the onus fork; single-stressor Hochen/Mahaffey/Adams; Delaney/Carr), built on the
  ADMITTED record + MSH concessions + the Review Officer's UMA finding — so the "thin record" objection
  to a pre-production offer is largely answered (it doesn't need production to argue).
- SCOPE HELD where it matters: the s 40-42 reprisal tort is NOT released; only the narrow medical-info-
  handling complaint (6.2(d), SEVERABLE) is. WATCH: 6.2(c) offers to DISCONTINUE the 64G (severable) =
  the disclosure/citable-decision escape; conscious call if the Regulator accepts core + (c).
- CAUSATION stronger than the red-team assessed: a Krishnaiah PSYCHIATRIST REPORT EXISTS (Exhibit A4,
  dated 13 Feb 2025; diagnosed 24 Oct 2024; referred by Hawes Sept 2024). Not "no psychiatrist."
- **COSTS CORRECTION (I was WRONG earlier):** WC APPEALS are NOT the general QIRC own-costs default.
  s 558(3) WCRA gives the Commission a costs discretion and costs "ordinarily follow the event" (Canton
  v WCR [2019] QIRC 145 [33], applying Latoudis v Casey), on the s 191 scale, with up to 1.5x uplift
  (s 191(3)). So the Calderbank has REAL teeth — a self-rep who briefs counsel + expert and wins can
  recover those costs, and unreasonable rejection triggers uplift. Update settlement.md L21 accordingly.
- POSTURE: offer live to ~22 July. If accepted -> resolved. If rejected/lapsed -> proceed to 7 Aug with
  the costs reservation banked. Discipline: written only, no chasing; say NO to any "release everything"
  counter (reprisal tort stays reserved).

## 2026-07-03 — Employee Capability Checklist (Dr Day Hong Ma, 3.7.26) ingested + PDF built
Built metadata-scrubbed 5pp A4 PDF from Cory's 6 photos (deduped the double scan of p1) →
documents/medical/Employee_Capability_Checklist_CShepherd_03-07-2026.pdf. For the LBH Injury
Management team (lbh_injurymanagement@health.qld.gov.au per the form). Key content: MDD w/ anxious
distress ongoing; modified duties 6x8h shifts/fortnight (max 2 weekday day/aft + 2 night + 2 weekend),
"continuation of the reduced pattern sustained since 2025"; fit from 3 July 2026; review 28 Aug 2026;
NO complaint-handling duties; predictable rostering + MIN 10-HOUR BREAK "consistent with the Award and
fatigue risk management standards"; stressors named = complaint handling, being blamed for others'
failures, rostering/fatigue practices, unresolved line-management matters; cites the treating
psychiatrist report 13-Feb-2025; meds fluoxetine 60mg + lisdexamfetamine (Vyvanse) 30mg, quetiapine
ceased. CLAIM IMPACT: proves ongoing injury/partial incapacity (quantum continuity), corroborates the
pleaded stressors + the 10-hr control, reinforces the Krishnaiah chain; DOUBLE-EDGE = Vyvanse feeds the
Regulator's pre-existing ADHD/anxiety causation attack (SOFC ¶8); goes into MSH's records via Injury
Management (clean — no collateral content).

## 2026-07-07 — MSH HR (Forrest) letter: RTW withheld, 7-day information demand — EVIDENCE-GRADE
Lyndelle Forrest (Senior Consultant HR, LBH) 7 July 10:54am: ECC "reviewed and carefully
considered" BUT return withheld pending "further information" within 7 CALENDAR DAYS (→ 14 July):
(1) further info re the psych injury + A COPY OF THE KRISHNAIAH REPORT (13 Feb 2025) — the
litigation causation centrepiece, requested through the HR/RTW channel while MSH (non-party)
fights the 64G and the Regulator's SOFC ¶9 does not admit the diagnosis; (2) "clarify" the
complaint-handling restriction; (3) "clarify" rostering/10-hr concerns — claims "not aware of
breaching this provision", "not received any Workload Concerns"; (4) "unclear what matters you are
being held accountable for... not aware of any concerns being raised" — from the institution served
with the appeal, amended SOFC, Form 24, Form 29 and the sealed 64G.

**BANKED (quietly — do NOT flag to them): the 8-HOUR AGREEMENT ADMISSION.** Forrest in writing:
the 17 June 2020 8-hr agreement "is ONLY APPLIED WHERE STAFF INITIATED SHIFT SWAPS HAVE OCCURRED."
The 17-18 March 2024 shifts were rostered by the manager, NOT a staff-initiated swap → on MSH's own
statement the 8-hr agreement did NOT apply → the applicable minimum was 10 hours → undercuts the
Regulator's SOFC ¶22(e) reliance and the employer's Sept-2024 "agreement remained current" position.
Contradicts their own prior account; goes to the contradiction matrix / hearing, never to this thread.

Also: rolling return date (Fri "review Mon, answer Tue COB" → Tue = 7 more days of questions);
gatekeeper escalated from Injury Management Consultant to Senior HR Consultant; leave still being
docked. Cory's "held out while they decide what to do about my submissions" theory materially
strengthened. Response strategy: cooperative-in-form, boundaried-in-substance (practitioner-channel
clarification w/ consent; DECLINE the psychiatrist report via HR; litigation matters → Metro South
Legal; renew the paid-time request). Letter saved: documents/2026-07-07_MSH_HR_Forrest_ECC_further_information.pdf

## 2026-07-10/13 — Harrison reply: hold-out continues, pay dodged, QSuper deflection (WRONG premise)
Cory sent his RTW reply 10 July 8:35am (variant: DIRECT consent for Health Service to contact Dr Ma,
capacity-limited; "will not provide further particulars" re WC matters; report declined; paid-time
request renewed). Harrison (IM Consultant) replied:
- Hold-out CONTINUES ("unable to safely support or accommodate a Graduated RTW Plan") pending
  "further medical clarification" from Dr Ma. No timeframe ("as soon as practicable").
- PAY REQUEST NOT ANSWERED — deflected: "you currently have an active open QSuper Income Protection
  claim... contact your claim manager James Zappia at QSuper and inform them that WE ARE UNABLE TO
  SUPPORT A RETURN TO WORK at this time."
- **PREMISE WRONG (per Cory): the IP claim/fund is CLOSED** (QSuper is ART since 2022; the ART claim
  has since closed — cf. May 2026 Mind&Memory emails "waiting on confirmation from ART"). So the
  employer's proposed income path is ILLUSORY: certified fit + willing + employer-directed absence +
  leave exhausted + NO income from any source.
- Also conceptually broken: IP responds to INCAPACITY; he is certified FIT — the loss is caused by the
  employer's refusal to roster, not incapacity. CAUTION: he must NOT lodge an incapacity-based IP claim
  while certified fit (inconsistent-statements trap).
- RECORD GAINS: (1) Harrison's own words "we are unable to support a return to work at this time" =
  written admission the barrier is the employer; (2) she formally names "the WorkCover matter" — the
  HR/legal silo is now CLOSED on the record; (3) they accept the Dr Ma clarification channel.
- ACTIONS: brief Dr Ma urgently (they will write; scope = capacity+adjustments; key point = pattern
  unchanged 12 months, safe to return; respond fast); union (Together) NOW; correct the QSuper premise
  in writing + renew pay request + ask basis-in-writing if refused; optionally obtain ART written
  confirmation the claim is closed (artifact proving the deflection illusory).
- REFINEMENT (Cory): the QSuper/ART IP benefit was only ever a PARTIAL TOP-UP premised on partial
  incapacity while WORKING the reduced hours (topping up 0.6 earnings toward pre-injury income) —
  never wage replacement for a total employer-directed absence. He is NOT totally incapacitated
  (certified fit). So the Harrison deflection fails 3 ways: claim closed; benefit design = partial
  top-up only; no incapacity basis exists. Reply para 1 updated accordingly.
- WORDING CORRECTION (Cory): the precise point is the SUPPORTING DOCUMENTATION would only support a
  PARTIAL payment — the ECC certifies fitness for the reduced pattern, so no medical evidence exists
  that could ground total-incapacity income support; the total loss flows from the employer's
  non-rostering. Reply para 1 recast on that basis (documentation-driven, not benefit-history).

## 2026-07-13 — Harrison writes to QSuper/ART claim manager (James Zappia) — EVIDENCE-GRADE
Harrison phoned then emailed Zappia (Cory in receipt of copy): "we are unable to facilitate Cory's
return to work in accordance with the restrictions outlined in the attached ECC" — the ECC ATTACHED
(his medical document shared with the fund; claim per Cory is CLOSED — verify what authority/consent
covered that disclosure). They will send Dr Ma a "Request for Medical Information" "over the coming
days," expressly probing "the reduction in hours from Cory's substantive position," and note Ma's
28 Aug review date — pacing risk: drift toward ~8 weeks held out unpaid.
KEY READS: (1) third written admission the barrier is MSH, now published to an independent third
party; (2) LITIGATION TENSION BANKED: MSH now asserts it "cannot safely support" the very pattern
it ran for 12 months (and that Forrest's letter said was already accommodated by existing practice)
— irreconcilable with both their own prior letter and the reasonableness narrative; (3) POLICY
OPPORTUNITY: many group IP policies treat "partial capacity + employer unable to provide suitable
duties" as a payable benefit — MSH's written "cannot accommodate" + the fit-for-reduced-pattern ECC
is the classic evidentiary pair; Cory to ask Zappia (truthfully framed: NOT incapacity — employer
non-accommodation) whether the policy responds + what MSH provided; (4) privacy check: how was the
ECC's disclosure to the fund authorised, claim being closed.
ACTIONS: send the 4-point email if not yet sent (unchanged — still fully apt); short follow-up re
the Zappia email (confirm what was shared + authority; press a date for the Ma request + copy to
Cory; reject 28-Aug pacing; renew pay); Cory to contact Zappia himself in writing; brief Ma hard
(the hours-reduction probe is coming; hold the certified line; copy Cory); union URGENT.
- PRIVACY POINT (calibrated): the ECC disclosure to Zappia is ARGUABLY unauthorised (claim closed;
  ECC provided for RTW not insurance) but MSH has 3 candidate answers (old claim authority; good-faith
  timing; related-purpose limb). The follow-up email's "what authority" question extracts their
  position first — do NOT characterise a breach before their answer. TIMING TO PIN: did Cory's
  "claim is closed" correction land BEFORE Harrison's 13 July call/email to Zappia? If yes, good-faith
  dies. Escalation ladder (banked, rule 8): MSH privacy officer → OIC Qld.
- **CALDERBANK 6.2(d) INTERACTION FLAG:** the severable release ("the State of Queensland and its
  entities"... "manner in which his medical and personal information was obtained and disseminated")
  could arguably catch the NEW 13 July QSuper disclosure if accepted post-13-July. If acceptance
  arrives incl. 6.2(d), CONSCIOUSLY decide: carve out the QSuper disclosure or release it. Not by accident.
- HEADERS NOW VISIBLE (Zappia email, Mon 13 July 4:20pm): To james.zappia@ART.COM.AU (Australian
  Retirement Trust — confirms QSuper→ART); Cc notes@solv.com.au AND CORY (disclosure was transparent,
  not covert — softens optics, doesn't create authority); Subject carries claim ref "[CLM-317073]"
  — the fund retains a claim record; status per Cory = closed. TIMING: thread order suggests Cory's
  four-point correction ("claim is now closed") was sent BEFORE Harrison's 4:20pm disclosure —
  CONFIRM the sent timestamp; if confirmed, the good-faith timing defence dies (disclosure made
  after written notice the claim was closed).
- SENT four-point email: point 3's fence got garbled in sending — "This offer is made to my
  substantive Switchboard position" (the words "without prejudice" dropped). Substance survives
  ("interim... as an alternative... to which I remain ready to return") but the new reply must
  restore the full "made without prejudice to" formula.

## 2026-07-13 — ART/QSuper claim file history surfaces (CLM-317073, Party 195438787) — GOLD + CAUTIONS
Cory produced the fund correspondence history:
- Dec 2024 (Louise Ings, ART claims mgr): monthly IP claim management; fund file already holds the
  litigation narrative (Form 12 reinstatement + deed negotiation, Form 9 appeal, lawyer); Krishnaiah
  + psychologist (Helen Morris) + GP treating team documented; fund sought medical reports.
- "Hey Louise" follow-up email (date TBC — confirm if SENT and when): **"I have returned to work and
  against medical advice... approximately 50-60% of my hours over the year... I basically RETURNED DUE
  TO NOT WANTING TO LOSE MY JOB. Most days are a struggle."** Asked the super to STOP paying him +
  how WC acceptance would pay back into super.
- April 2026 (Gavin, QSuper Resolutions, ref cf15866300-446968946): Cory complained re his MEDICAL
  INFORMATION causing harm (a SECOND medical-info grievance — against the FUND, separate from MSH);
  and an **OVERPAYMENT** exists which Cory accepts "needs to be addressed" (IP benefits paid while
  working). Claim since closed.
KEY INTEGRATIONS:
1. **The contemporaneous fear record ALREADY EXISTS**: "returned due to not wanting to lose my job"
   written to a third-party financial institution, dated, in their file — corroborates the fear-driven
   premature return post-Oct-2024 termination. Severity + reprisal-detriment evidence. PRESERVE AS IS.
2. **Two-period reconciliation (critical discipline)**: 2025 = returned early AGAINST medical advice
   out of fear; 2026 = the same pattern now MEDICALLY CERTIFIED (ECC: "sustained since 2025 without
   deterioration"). Never blend the two framings: today's correspondence says "certified fit" ONLY.
   If the fund file ever surfaces (summons), the reconciliation is coherent and actually strengthens
   severity/causation (worked hurt for a year because they'd fired him once).
3. **Overpayment ↔ WC interplay**: WC acceptance arrears would likely offset/repay the IP overpayment
   (standard offset mechanics + he already asked "how WC would pay back into the super"). The
   Calderbank resolution CLEANS UP the fund debt — settlement mechanics note: part of arrears may
   flow to ART, not to pocket.
4. Zappia letter to be REVISED: reference the Ings history, the stop-payment request, the overpayment
   resolution; framing stays "closed at my request on RTW; employer now refuses to roster; what does
   the policy provide; confirm what MSH sent."
5. The fund is NOT "the State/its entities" → the April fund complaint sits OUTSIDE Calderbank 6.2(d).
CONFIRM WITH CORY: (a) was "Hey Louise" sent + date; (b) status of the Gavin resolution/overpayment;
(c) the four-point-vs-Harrison-disclosure timestamp (still outstanding).

## 2026-07-13 — Carolyn Jeffrey text (17:21): "have you been dismissed... Chloe is saying she will
have a full time line available?" — EVIDENCE-GRADE, handle with care
Colleague (and existing WC witness — her two 2024 statements are in the Review Decision record)
texts Cory unprompted: "Hi Cory have you been dismissed is that why Chloe is saying she will have a
full time line available?" Screenshot preserved: documents/evidence/2026-07_Carolyn_Jeffrey_text_
dismissed_fulltime_line.jpg (confirm exact date of the 17:21 message).
READS: (1) while HR holds him out "pending assessment," the LINE MANAGER is telling the team a
full-time line will be available — the team infers dismissal. Corroborates the "held out while they
decide what to do" theory; possible backfill of his substantive line. (2) CAUTION: hearsay of
Chloe's words; innocent readings exist (temporary coverage of his shifts; another vacancy).
(3) The workplace-believes-he's-dismissed fact is itself: reputational harm + PID-detriment-adjacent
+ external corroboration that his fear of re-termination is reasonable (a colleague spontaneously
asks it). (4) Chloe making roster/line statements about him while RTW comms are supposed to run
through Injury Management.
ACTIONS: reply to Carolyn calm/minimal (correct the rumour: NOT dismissed, certified fit, awaiting
HR; ask naturally what exactly was said/when); PROTECT CAROLYN — do not name her in any
correspondence; route the position-status question through TOGETHER (union asks about
backfill/vacancy plans without sourcing); **MONITOR SmartJobs/QH recruitment for Logan Switchboard
AO3 full-time postings** — an advertisement converts hearsay into documentary proof; do NOT confront
HR/Chloe directly yet.

## 2026-07-14 — QSuper/ART correspondence bundle ingested (30pp, assembled 14 July) — DATES LOCKED
Saved: documents/2026-07-14_QSuper_IP_RTW_Correspondence_Bundle.pdf. Contents & key extractions:
1. Ings thread 4–29 Oct 2024 (claim assessment).
2. **"Hey Louise" = 13 MARCH 2026** (RTW against medical advice; request to CEASE benefit).
3. **21 MARCH 2026 11:30am, to Jennifer Chen cc Ings — THE FEAR RECORD, verbatim:** "During the
   workcover I was actually dismissed from my employment and then reinstated at Queensland Health,
   I returned to work against medical advice because I was DEEPLY AFRAID OF LOSING MY JOB AGAIN.
   I tried to keep going and manage the hours, but I was not coping, and the level of overwhelm...
   ultimately resulted in A CAR CRASH ON THE MOTORWAY." Also "~55% reduction in my pay."
   → Answers the "did I write it" question: YES, with "again", dated, in ART's file, 4 months
   before the July lockout.
4. **Ings (Senior Claims Mgr) in writing:** benefit was paid as FULL benefit on a "Totally and
   Temporarily Disabled" basis; RTW → reassessment to "Partially and Temporarily Disabled";
   overpayment "will need to be recouped" + fund requested payslips, RTW medical docs, WC status.
5. Overpayment response + medical-info complaint (13 Apr 2026, Chen/Ings); Gavin reply 13 Apr.
6. Four-point ECC email = **13 July 2026 4:39PM**; Harrison QSuper deflection = 13 July 15:53;
   Harrison→Zappia = 13 July 16:20.

**TIMING CORRECTION (against my earlier hope): Harrison's Zappia disclosure (16:20) PRECEDED
Cory's "claim is closed" correction (16:39) by 19 minutes.** The "disclosed after being told"
angle is DEAD — drop it. The neutral what-authority question stands (already sent in that form).
**"CLOSED" NUANCE:** benefits ceased at Cory's request (13 Mar) but the claim file remains open
for OVERPAYMENT recoupment — expect MSH/fund to say "not closed"; his substantive point (no income
support available from that source) survives regardless. Zappia letter should say "benefits ceased
at my request; I understand the claim is closed subject to the overpayment resolution."
**TENSION TO MANAGE:** Mar 2026 "I was not coping" + the (2025) motorway crash vs Jul 2026 ECC
"sustained without deterioration" — the psychiatrist report must OWN the whole arc (fear-driven
premature return → crash/struggle → stabilisation → certified pattern). Also the crash = severity/
consequence evidence (MVA 2025 exhibit exists in the archive) but invites an intervening-event
argument — handle via the medical evidence, never volunteered in correspondence.
**CREDIBILITY ASSET:** the bundle shows Cory self-reported his RTW, asked payments to STOP, and
cooperated on recoupment — the opposite of a malingerer; powerful against any exaggeration attack.

## 2026-07-14 — Docs 122/123/124 cross-referenced against the master timeline — NO CONTRADICTIONS
1. **Doc 123 — Form 29 service on Matheson (AP1), Wed 22 Apr 2026 16:52** — expressly invoking
   r 64C(4): served on the Affected Party BEFORE the Nominated Party, 7-day objection window stated.
   CONFIRMS the register (22 Apr seal + service) and DOCUMENTS the service-sequence compliance —
   the clean answer to any procedural attack on the Form 29 at the 7 Aug hearing.
2. **Doc 124 — Postmaster delivery receipt, 64G service on Ruttan, Thu 25 June 08:31 (AEST).**
   Reconciles with the Gmail-ingest receipts stamped 24 June 22:31 (UTC) = 25 June 08:31 AEST —
   SAME EVENT, timezone rendering. Service on MSH proven delivered.
3. **Doc 122 — the Chloe "ECC/Leave Type" thread, closing with Cory 3 July 15:18**: annual-leave-
   not-unpaid-sick request for the past period + "certifies me fit to resume from 3 July...
   confirm I'm right to attend." **NEVER ANSWERED by Chloe (11+ days)** — add to the unanswered
   ledger: (a) 3 Jul annual-leave request [Chloe]; (b) pay for employer-directed period ×5 [IM/HR];
   (c) interim duties offer [IM/HR]; (d) QSuper what-authority question [IM]; (e) 3-business-day
   Ma-request ask [IM].
4. **THE 3 JULY MICRO-TIMELINE (now minute-stamped):** 14:32 ECC lodged with IM → 14:35 Chloe told
   → 14:49 Chloe: "sick leave / sick leave no pay" → 14:50 Harrison: resend p2 → 15:06/15:09 p2
   resent → 15:18 Cory to Chloe: certified fit, ready, annual leave please → 15:30 Harrison: held
   out until review, shifts "paid out of your available sick leave." **58 MINUTES between the fit
   certificate arriving and the decision to hold him out and charge his leave** — the "review"
   posture was adopted before any review was possible.

## 2026-07-14 — HR personnel/roles map + structural signals (from signature blocks & distribution lists)
Taylor (Switchboard Mgr, line) → Harrison (Injury Mgmt Consultant, "LBHS HR Team 1" — the case
admin) → Forrest (SENIOR Consultant HR — appeared ONCE, for the 7 July four-demand set-piece, then
file returned to Harrison) → Griffin (MSH HR — ON THE QIRC DISTRIBUTION LIST, receives all listing
notices; procedurally fluent: re-routed Ruttan's April extension app + effected service) → Thorburn
(ED Clinical Governance Risk & Legal — routed the Form 29 to the Chief People & Partnerships Officer
in April). SIGNALS: (1) escalation gradient — senior signs the demand letter, junior runs the file =
set-piece fingerprint; WHS-flavoured drafting; (2) HR-as-a-unit cannot claim ignorance — Griffin on
the Commission's list + CPPO holding the Form 29 since April makes Forrest's "not aware of any
concerns" false WITHIN her own unit; (3) IM sits INSIDE HR — the RTW desk and any future exit desk
are the same shop; (4) URGENCY ASYMMETRY — lockout in 58 min, fund contact in the last hour of a
Monday (16:20, past stated 4pm finish) vs 11+ days of silence on pay/leave/RFI = pacing is policy;
(5) Solv case MSH-INJ-5795 is a self-contained extractable file containing their own adverse letters.
WATCH: who signs the RFI to Ma (new name/unit = escalation; "Workforce Relations" appearing = exit
machinery); distribution-list creep; Forrest reappearing. Discipline: roles/structure analysis only —
NO personal dossiers on staff (vexatious-frame risk; the structural read is the useful one).

## 2026-07-14 — Settlement-date Monte Carlo (50k runs, 6 pathways)
P(consent resolution) ≈ 85%. Conditional median deal date 18 AUG 2026 (IQR 6 Aug – 3 Oct).
Monthly (unconditional): Jul 16% | AUG 31% | Sep 14% | Oct 18% | Nov+ 5% | never 15%.
Pathways: accept-in-window 13% | engage-pre-lapse 17% | mention-driven 17% | POST-PRODUCTION 33%
(single likeliest pathway, landing ~end Sept) | hearing-door 5% | no settlement 15%.
TWIN PEAKS: mid-Aug (post-mention fortnight) and late Sept/early Oct (post-production renewal).
Money lag: orders +1-2 wks after deal; payments +2-6 wks after orders. Movers: any Matheson
engagement before 22 Jul (shifts left); the 7 Aug room; the updated Krishnaiah report (accelerates
every pathway). Priors = calibrated judgment from the record, not measured rates.

## 2026-07-14 — External second opinion (sanitised brief → Grok) cross-checked
Brief was de-identified; banked evidence EXCLUDED by design → external numbers are a FLOOR.
Grok: consent-resolution 68-74% (vs our 86%); in-window acceptance 11%; no-settle 22-26%.
RECONCILED BAND: ~78-84% consent, in-window ~14%, no-settle ~16-18%; median date CI widened ±2wks.
LANDED: (1) timetable-compression risk at the 7 Aug mention (not "bifurcation" — mechanism wrong,
worry right) → Krishnaiah report before timetables; at mention ask sequencing = production before
evidence directions. (2) Priors humility. VALIDATED: produce-or-swear "judicially palatable";
expiry-before-mention "strategically optimal"; staged-production fallback already in the application.
REJECTED: WPSATC costs-threat letter to MSH cc insurer (torches restraint posture, merges channels);
lay supplementary statement on causation (expert's job — the report); GP subpoena (procedurally
confused). ADAPTED: obtain Dr Ma's clinical notes for key dates (esp. 3 July consult) voluntarily —
evidence preservation, added to list. DECLINED: offer auto-extension 7 days post-orders (gives the
Regulator a free look at the mention outcome at the old price; lapse-then-renew keeps option value).
No repo access was granted at any point; assessment ran on the pasted brief only.

## 2026-07-15 — Harrison reply (13:10, to Cory AND Zappia, cc Solv) — THE DISCRETION LETTER
Saved: documents/2026-07-15_Harrison_reply_pay_refused_discretion.pdf. Answers everything, badly:
1. DISCLOSURE: only the 13 July email+ECC went to ART; calls confined to RTW-support + claim status.
   AUTHORITY CLAIMED: the declaration/authorisation at "page 7 of your Income Protection Application"
   (permits QSUPER TO REQUEST from the employer — note the direction-of-flow gap: this was employer-
   initiated push on a closed claim; arguable, banked, NOT worth fighting now).
2. RFI TO MA: "unable to commit to a timeframe" — after telling the fund "over the coming days."
   The gate to his return now has NO CLOCK. Open-ended lockout formalised in writing.
3. PAY: REFUSED — "we are not responsible for your payments whilst on this claim... sits with your
   QSuper Claim Manager"; demands HE provide written proof of closure. THE BASIS-IN-WRITING HAS
   ARRIVED and it is FALSIFIABLE: rests entirely on a claim that pays nothing. CHECKMATE PATH:
   ART written closure confirmation (Zappia letter Q1) → forward to Harrison → basis evaporates →
   pay or a fresh artifact refusing a disproven basis.
4. INTERIM DUTIES: REFUSED "in any capacity" pending the un-timetabled RFI. Fit worker, no duties
   anywhere in a hospital-and-health-service, indefinitely.
5. **THE DISCRETION PARAGRAPH (lawyered; the month's biggest own goal):** WCRA rehab/suitable-duties
   obligations "apply to workers with ACCEPTED claims... does not extend to employees being managed
   through HEALTH MANAGEMENT PROCESSES or those receiving QSuper IP benefits... remains at the
   discretion of the Employer."
   (a) NAMES THE TRACK: "Health Management processes" = the QH pathway that can end in ill-health
       retirement — the exit-pathway watch item CONFIRMED as the operating frame (probability up).
   (b) OWN GOAL: they formally state his lack of rehabilitation rights flows from the CLAIM REJECTION
       UNDER APPEAL — i.e., the July lockout is a direct consequence of the wrongful rejection.
       Quantifies acceptance stakes: acceptance converts him from discretionary exclusion to statutory
       rehab/suitable-duties rights. STRENGTHENS the Calderbank/settlement narrative + severity.
   (c) LEGALLY INCOMPLETE: WCRA silence ≠ pure discretion — AD Act reasonable-adjustment duties
       (impairment), WHS duty of care, general protections, and QH's OWN health-management/RTW
       policies all constrain "discretion." Refusing ANY duties to a worker with certified capacity,
       indefinitely, without timeframe = the union brief writes itself; AD Act angle flagged for Together.
6. Reply now addressed to Cory AND Zappia jointly — employer keeping the fund looped into employment
   correspondence.
ACTIONS: NO reply-war with Harrison (they've answered; arguing = badgering). (1) Zappia/ART letter
NOW if not sent — the written closure confirmation is the pin; on receipt forward to Harrison + renew
pay in one line. (2) TOGETHER — this letter IS the exhibit (fit worker, no duties in any capacity, no
timeframe, "discretion," Health Management naming). (3) Brief Ma to turn the RFI fast whenever it
lands. (4) Exit-pathway watch: escalated from ~35-40% toward ~45-50% on the "Health Management" naming.

## 2026-07-15 — FULL RE-READ of the Harrison chain — the "what are they clarifying" question is ANSWERED IN THE LETTER
Close re-read of documents/2026-07-15_Harrison_reply_pay_refused_discretion.pdf (whole chain incl.
the embedded 13 Jul Harrison→Zappia email). New findings beyond the first-pass log:
1. **THE RFI'S SUBJECT IS STATED — and it is the CONDITION, not the restrictions.** Interim-duties
   paragraph: further medical information is required "to understand the NATURE OF THE MATTERS
   identified by Dr Ma and to assess whether they present any PSYCHOSOCIAL HAZARDS OR RISKS that may
   affect your proposed return to work IN ANY CAPACITY." That is the reading-3 discriminator we said
   to watch for, present in advance: the clarification goes to the underlying psychiatric condition
   ("nature of the matters"), framed as a potential workplace HAZARD. THE INVERSION: he raised
   psychosocial hazards (fatigue/governance); his own condition is now cast as the psychosocial
   hazard justifying blanket exclusion. Same WHS-flavoured drafting fingerprint as the Forrest
   7 July letter (continuity of hand).
2. **DECISION-BEFORE-EVIDENCE sequencing:** the 13 Jul Zappia email states "we are UNABLE to
   facilitate Cory's return" FIRST, then says clarification will be sought — conclusion announced to
   the fund before the evidence-gathering begins. Undermines the innocent-caution reading.
3. **One concrete RFI topic exists but was told to the FUND, not Cory:** "the reduction in hours from
   Cory's substantive position" (Zappia email). So the ECC's reduced-hours restriction is the one
   named operational issue; to Cory the scope is the open-ended "nature of the matters."
4. **Identity assignment:** Cory processed as "a QSuper Claimant request[ing] to return to duties" —
   not an employee with a fit certificate. "Safe and SUSTAINABLE return" = health-management
   vocabulary.
5. **Pay premise wording:** "as WE HAVE BEEN PROVIDED INFORMATION that you do hold a current QSuper
   Income Protection Claim" — passive, unattributed, and maintained AFTER Cory's 13 Jul 16:39 closed-
   claim advice (his own statement disregarded in favour of unnamed "information"). Falsifiable
   premise stands; checkmate path unchanged (ART written closure confirmation).
6. **Direction-of-flow gap in their own words:** consent para says the p7 authorisation "permits
   QSUPER TO REQUEST relevant information FROM your employer" — but the 13 Jul disclosure was an
   employer-initiated push after Harrison phoned Zappia ("Thank you for taking the time to speak with
   me"). Their stated authority describes the opposite flow. BANKED (not worth fighting now).
7. **Unanswered ledger updated:** pay = now ANSWERED (refused, basis in writing); interim duties =
   ANSWERED (refused "at this stage"). STILL UNANSWERED/REFUSED: (a) the 3-business-day RFI ask
   (refused — "unable to commit"); (b) "advise the timeframe within which my RTW will be decided once
   Ma's response is received" (IGNORED entirely); (c) the 28-Aug pacing point (met with SILENCE — no
   assurance the process won't run to the review date); (d) Chloe annual-leave request (11+ days).
8. **Signal tally / track assessment:** health-management-track signals now: track named; condition-
   as-hazard framing; "in any capacity"; "nature of the matters" RFI scope; "sustainable"; no
   timeframe + silence on 28-Aug pacing; decision-before-evidence to the fund; claimant identity
   assignment; channels merged (Zappia joint-addressee, Solv cc). Innocent-caution residue: the
   reduced-hours topic is a genuine operational specific; consent explanation procedurally coherent;
   "endeavour... expeditiously." NET: exit/health-management operating frame FIRMED — hold at the
   top of the 45-50% band; do not raise further until a hard step (IME direction, PSA ill-health
   citation, Workforce Relations appearance, show-cause).
9. **AD Act sharpening for the union brief:** blanket exclusion "in any capacity" based on
   unparticularised risk from an impairment, against a treating doctor's fit-with-restrictions
   certificate and with no timeframe, is the classic reasonable-adjustment failure pattern. The
   condition-as-hazard framing makes the discrimination angle CRISPER, not weaker.
Actions unchanged and sharpened: (1) Together NOW — before the RFI lands (step-zero representation);
(2) Zappia/ART written closure confirmation; (3) Ma briefing must anticipate CONDITION-scope
questions — answer within consent scope, restrictions-and-capacity focus, copy Cory, fast turn;
(4) NO reply-war with Harrison.

## 2026-07-15 — Cory's articulation of the INVERSION + two new evidence leads (provenance needed)
Cory's own framing (verbatim substance): ~2 years before the injury he raised psychosocial risks —
pay, fatigue, the environment, and DELAYED MANAGEMENT UPDATES OF PHONE NUMBERS (routing changes fed
through a "second information manager" instead of real-time updates, with access to that information
RESTRICTED FROM THE SWITCHBOARD ITSELF); the employer now inverts the psychosocial-hazard framework
against him post-injury, while he has had to SELF-MANAGE his psychological risk in a workplace that
treats Switchboard as "picks up a phone, answers it, transfers it" and a manager (Taylor) who is
erratic and referred to switchboard employees as **"bums on a seat."**
TWO NEW LEADS needing provenance before use anywhere:
1. **"Bums on a seat" (Taylor):** when said, to whom, witnesses, any writing (email/comm book/minutes)?
   If memory-only → Cory writes a dated statement NOW (who/when/where/who heard it). If documented →
   locate in archive. USE: Stressor 1(a) colour + the institutional-attitude thread (severity /
   evidence-in-chief / Krishnaiah context). NEVER in correspondence.
2. **Phone-number/directory update failure:** routing/contact changes held by a second information
   manager, not pushed real-time to Switchboard; access restricted. Fits Stressor 1(a) "bottlenecked
   emergency workflows / delayed urgent pathology results" and the CS-1 misrouting-misdiagnosis
   pattern (info needed to route life-safety calls withheld from the desk that routes them). CHECK:
   is this in the master complaint email / 7 Aug 2023 grievance / comm book / CS-3?
THE INVERSION, dated: 2023–24 he named the hazards (grievance 7 Aug 2023 dismissed same day; comm-book
entry removed 6 June 2023; PID 13 May 2024) → duties to manage psychosocial hazards sat with MSH and
went unperformed (the course-of-INACTION theory in miniature) → injury 18 June 2024 → JULY 2026: the
employer's first enthusiastic documented use of psychosocial-hazard vocabulary is AGAINST the injured
worker (his condition as the hazard), not the hazards he named. Placement: Krishnaiah report arc +
evidence-in-chief + union brief + closing. NOT to Harrison; NOT the 64G.
Self-management thread: he carried the psychosocial risk himself (fear-driven 2025 return against
advice → crash; 21 Mar 2026 fear record; certified-fit-and-excluded July 2026) — severity +
credibility, pairs with the "opposite of a malingerer" QSuper-bundle finding.

## 2026-07-15 — "Bums on a seat" PROVENANCE (from Cory): said to TRISH; Taylor made to APOLOGISE via JACKIE (HR)
Cory's account: the "bums on a seat" remark was said by Chloe Taylor TO TRISH (switchboard colleague);
Taylor WAS MADE TO APOLOGISE, the apology RELAYED THROUGH JACKIE in HR.
WHY THIS UPGRADES THE LEAD: (1) an HR-mediated apology = the incident was COMPLAINED OF, HANDLED, and
likely FILE-NOTED inside HR — MSH's own records probably confirm both the remark and the apology;
(2) an apology is an implied ADMISSION the remark was made; (3) TWO named corroborators exist — Trish
(recipient/witness) and Jackie (HR handler); (4) yet another datapoint that the HR unit KNEW of
switchboard-culture concerns (compounds the Forrest "not aware of any concerns" problem).
STILL TO PIN: Trish's surname; Jackie's surname/role in HR; approximate DATE; apology written or
verbal; how Cory learned of it (did he hear the remark himself, or via Trish?); whether Trish would
confirm if asked.
USE/DISCIPLINE: evidence-in-chief + witness-statement territory (Trish as potential witness) +
severity/attitude thread. The 64G is FILED — do NOT expand it for this. If ever compelled, it's a
later, separate consideration; first preference is a willing witness. WITNESS APPROACH RULES: casual,
factual, zero pressure, no coaching — "do you remember the bums-on-a-seat comment and the apology?
would you be comfortable putting what you remember in a short statement?" Nothing about this in ANY
correspondence with MSH/HR.

## 2026-07-15 — STATUS CORRECTION (from Cory): he is NOT a "return to work" case — he was WORKING
Cory's correction (adopt everywhere): he has been WORKING for the past year (2025 return → continuous
service; QSuper benefits ceased at his request Mar 2026 BECAUSE he was working; rostered and working
right up to 3 July 2026 14:32). The reduced shifts over that year were HIS OWN self-managed adjustment
to an unresolved, mismanaged psychosocial environment — not an absence. On 3 July he submitted updated
medical restrictions (the ECC) as a WORKING employee; MSH responded by REMOVING him from the roster.
WHY "RETURN TO WORK" IS THEIR LOAD-BEARING MISLABEL (Harrison to Zappia: "a QSuper Claimant requests
to return to duties"; to Cory: "your proposed return to work"):
1. Recasts the lockout as the DEFAULT STATE (absent worker seeking entry) instead of what happened
   (working employee ejected in 58 minutes). The onus flips with the label.
2. Feeds the PS Act s 103 health-management gateway ("absent from duty") — but the ONLY absence is
   12 days old and WHOLLY EMPLOYER-CREATED. Before 3 July: no absence, just a working employee.
   Gateway even more fragile than previously noted.
3. Positions the ECC as an APPLICATION for a privilege rather than routine updated medical info from
   a serving employee. In substance the situation is a SUSPENSION WITHOUT PAY with no power invoked.
4. It was also said to the FUND — factually wrong twice over (claim closed + not "returning") — banked
   with the other fund-communication inaccuracies.
LANGUAGE DISCIPLINE (all future drafts/analysis): never "return to work" — use "resume my rostered
shifts" / "continue working" / "reinstatement to the roster." Cory's own sent emails already mostly
hold this line ("held out of work since 3 July while certified fit").
DOUBLE EDGE — handle with care: "I dropped shifts to manage the psychosocial environment" is TRUE and
powerful (worker performing the employer's unperformed WHS duty; the restrictions measure THEIR
unmanaged hazard, not his incapacity) BUT stated carelessly it hands MSH "he says the workplace harms
him" for the incapacity file. Correct articulation (union brief/evidence only, never correspondence):
the hazards are the employer's and remain unmanaged; his adjusted hours were a reasonable interim
CONTROL he implemented himself; the lawful fix is managing the hazard, not removing the worker. In
correspondence the only position is: CERTIFIED FIT WITH RESTRICTIONS, working until excluded.
Consistency bonus: the year of self-adjusted partial hours ↔ partial QSuper benefits ↔ payslip-driven
partial-payment position — one coherent, documented story of a worker managing honestly.

## 2026-07-16 — TOGETHER IS ENGAGED (Heath Moran thread, 14–15 July) — URGENT INDUSTRIAL REFERRAL
Saved: documents/2026-07-15_Together_Heath-Moran_thread_urgent-industrial-referral.pdf.
The union action item is DONE — Cory had already made contact on 14 July (before my repeated urging
resolved; he was ahead of the plan). Thread:
1. **14 Jul 10:50 Cory → Heath Moran (Organiser, South Team, 0414 225 851):** raises (a) TAYLOR HAS
   TOLD OTHERS A FULL-TIME POSITION IS COMING SOON in his line of work — asks his status re it (the
   SmartJobs watch item + the Carolyn Jeffrey "dismissed full-time line" text now CORROBORATED as a
   live vacancy rumor, on record with the union BEFORE any ad); (b) the ECC requirement is NOVEL —
   not required on his previous resumption after the 2024 dismissal/reinstatement, despite 12 months
   performing the role on self-managed reduced hours (DIFFERENTIAL-TREATMENT datapoint); (c) directed
   out until ECC complete → completed → STILL excluded; (d) his contemporaneous stated belief the
   exclusion may connect to the WC appeal/systemic patient-safety risks/reprisal (adverse-action
   belief now on record with the union, dated 14 July).
2. **14 Jul 16:04 Heath → Cory: "this is VERY SERIOUS... URGENT REFERRAL to our industrial team...
   if you've been put on an ECC, completed it and are still being told you cannot return, I need to
   make sure an industrial officer looks over this BEFORE ANYTHING IS ACTIONED."** Plus the gold:
   **"your ongoing concerns for the hazards in switchboard... this is a RECURRING THEME RAISED BY
   MEMBERS"** — the union already holds a switchboard-hazard file; Cory is corroborated, not alone.
3. **14 Jul 17:03 Cory → Heath:** handed over appeal submissions (expressly: to identify the
   unassessed psychosocial risks, NOT to run the appeal; not to be shared). Stated "no grievances
   with Ms Taylor personally" (good restraint). Form 20 affidavit describes role/workplace. Will
   send the ECC + HR's refusal.
4. **15 Jul 15:27 Heath → Cory:** "significant material... I'll have time to go through these on
   FRIDAY [17 July]... won't comment until reviewed... then I'll get back with my thoughts."
CONSEQUENCES FOR THE PLAN:
- **THE RECORD-CORRECTION LETTER TO HARRISON IS ON HOLD** — Heath expressly asked that nothing be
  actioned before an industrial officer reviews. The draft (drafts/2026-07-15_Harrison_record-
  correction_union-cc_DRAFT.md) + the discretion-logic research note become the UNION BRIEF handover.
- Union advice expected ~Fri 17 – early week of 20 July — landing RIGHT AT the Calderbank window
  close (22 Jul 4pm). Separate tracks; no conflict; if the industrial officer proposes anything
  touching the WC track, sequence carefully.
- ONE addition should go to Heath before Friday (single attachment, two lines): the 15 July Harrison
  discretion letter — it is THE exhibit (pay refused, no duties in any capacity, no timeframe,
  "discretion," "Health Management processes"). Also the ECC if not yet sent (he flagged he would).
- "He knows who i am" (Cory): Heath/Together recognise him and the switchboard issue — consistent
  with "recurring theme raised by members" + the 2024 unfair-dismissal history.
- NEW LEAD: the full-time-position rumor (Taylor, pre-advertisement) — if the exclusion runs while a
  full-time switchboard role is advertised/filled, the adverse-action inference sharpens materially.
  WATCH SmartJobs daily.

## 2026-07-16 — CALDERBANK #2 REJECTED (Matheson, 15:54) — the expected posture; the door-line noted
Saved: documents/2026-07-16_Matheson_Calderbank2_rejection.pdf. Full text of the operative part:
"I refer to your email and attached correspondence dated 1 July 2026 and note its contents. The
Respondent's position remains to defend the appeal as outlined in our Statement of Facts and
Contentions. Should our position change at any point, we will advise you as soon as possible."
ANALYSIS:
1. **Day 15 of 21** (offer lapses 22 Jul 4pm). Terse, no reasons, no counter, no request to confer —
   despite Cory's cover expressly inviting clarification/conference. Compare Calderbank #1 rejection
   (18 Feb): "does not accept your offer, and we will be defending the appeal." Same family, BUT:
2. **THE DOOR LINE:** "Should our position change at any point, we will advise you as soon as
   possible." Unnecessary in a flat rejection; it (a) acknowledges the position MAY change, (b)
   promises proactive notice, (c) reads as written-for-the-file by a party aware the offer will be
   produced on costs. Consistent with defend-as-instructed NOW + revalue at the known decision
   nodes (7 Aug mention; production). NOT an engagement signal; a keep-options-open signal.
3. **COSTS ARTIFACT BANKED:** a bare no-reasons rejection of a detailed 8-part offer (own-review
   adverse finding, ultra vires, Form 24 admissions itemised) is strong material for the
   unreasonable-rejection limb if the outcome ≥ offer: costs from 16 Jul/lapse, s 191(3) uplift ask,
   model-litigant point (no engagement, no counter, no conference despite invitation). Preserve the
   email + attachments chain intact.
4. **MODEL UPDATE (v3):** in-window acceptance (was 13%) and engage-pre-lapse (was 17%) are DEAD
   (~0-2% residual before 22 Jul). Mass redistributes: mention-driven ~20% | post-production ~36-38%
   (now clearly dominant, landing ~late Sept/early Oct) | MSH-folds-pre-mention ~10% | hearing-door
   ~6% | no consent resolution ~18-22%. P(consent resolution overall) ~74-80% (from 78-84 —
   modest haircut; rejection-before-mention was substantially priced). Median deal date shifts RIGHT:
   ~mid-late SEPTEMBER (post-production peak), secondary peak mid-Aug (post-mention). Money
   likelier Oct than Aug now.
5. **NO REPLY to Matheson.** Nothing to say; arguing re-opens nothing and cheapens the costs record.
   Let the offer LAPSE 22 Jul (lapse-then-renew keeps option value; auto-extension already declined).
   Renewal consideration point = post-production (or post-mention if the room shifts).
6. **CRITICAL PATH unchanged and now singular:** the 7 Aug mention (produce-or-swear) + the updated
   Krishnaiah report. Every settlement pathway that remains runs THROUGH production. The union/
   lockout front is unaffected (separate track) — and every extra lockout week keeps compounding
   the severity narrative that prices the eventual deal.

## 2026-07-16 — Rejection LATENCY signal (Cory's catch): 24 hours (Feb) vs 15 days (July)
Calderbank #1: rejected NEXT DAY (18 Feb) — "does not accept your offer, and we will be defending
the appeal." Calderbank #2: rejected day 15 of 21 — "position remains to defend... should our
position change at any point, we will advise you as soon as possible."
READ: (1) a one-line answer doesn't take 15 days to WRITE — it takes 15 days to AUTHORISE:
consistent with referral up/advice (counsel briefed for 7 Aug; possibly consultation with MSH given
term 6.2(c) directly affects MSH) before instructions came back "hold the line." The Feb rejection
was reflexive; this one was considered. (2) They ANSWERED rather than letting it lapse silently
(lapse was free and 6 days away) — affirmative rejection + door line = managing the costs record,
which itself concedes the offer has costs teeth. (3) WORDING DELTA: Feb categorical ("we will be
defending") → July conditional ("position REMAINS... SHOULD our position change... as soon as
possible") — from fighting words to holding words. Direction of travel across the two rejections is
the signal, not either letter alone. CAUTION: latency partly explainable by leave/July workload/
using the window; door line could be house politeness. Treat as a LEAN (posture = hold until the
7 Aug mention + production, with a pre-authorised path back to the table), not proof. Consistent
with v3 model (post-mention/post-production pathways dominant).

## 2026-07-16 — Integrating THE UNION'S OWN VIEW of the switchboard psychosocial hazard (strategy)
Heath's written line ("hazards in switchboard... a recurring theme raised by members") = independent
institutional confirmation the hazard is COLLECTIVE, not personal. Integration map:
1. **Industrial/WHS track (primary, union acts in ITS name):** Together can demand the psychosocial
   risk assessment that never happened — as a COLLECTIVE issue (HSR involvement; WHS Act right-of-
   entry powers; escalation to WHSQ, whose inspectors can compel assessment under the 2022
   psychosocial Code/Reg). Depersonalises: "Cory's condition" becomes "the switchboard's conditions."
2. **Anti-exit shield:** an ill-health/IME move against a member whose hazard complaints the union
   has formalised collectively becomes far costlier — the "he is the hazard" individualisation
   collapses against a union-endorsed collective frame. IF the union formally engages on the hazard,
   exit-pathway watch drops ~45-50% → ~30-35%.
3. **Appeal (careful, indirect only):** the union's VIEW is not admissible opinion, but (a) member
   witnesses could corroborate Stressor 1(a) conditions voluntarily (ask Heath IF members would
   assist — never fish in the union's confidential file); (b) evidence other members raised the same
   hazards = management knowledge + notoriety, counters individualisation at hearing; (c) supports
   severity/course-of-inaction narrative. Nothing union-sourced goes to the Regulator/QIRC without
   deliberate decision; the 64G stays untouched.
4. **Settlement pricing:** union WHS engagement raises MSH's systemic exposure (WHSQ attention,
   collective grievance, publicity risk of a public hearing) → nudges MSH-folds + post-production
   settlement pathways up; doesn't change the Regulator's legal analysis but raises the
   embarrassment cost of defending MSH's file in public.
DISCIPLINES: the union campaigns on the HAZARD, not on Cory's case (privacy + appeal restraint);
Cory never states "the union agrees with me" in correspondence to MSH (it's Heath's card to play,
in Together's name, with more force); the ask to Heath after Friday = "would the union consider
raising the switchboard psychosocial risk assessment as a collective issue" — a question, his call.

## 2026-07-16 — "Call the union as a witness?" — NO (analysed); the narrow exception; better vehicles
Cory asked whether to call the union (Heath) as a witness in WC/2024/227. CONCLUSION: no.
1. **Temporal mismatch:** the appeal turns on Jun 2023–Jun 2024 conduct + 18 Jun 2024 onset. Heath's
   involvement began 14 JULY 2026. He has zero first-hand knowledge of the injury-period conditions.
2. **Hearsay of near-zero weight:** "a recurring theme raised by members" in the box = unnamed
   members, unspecified dates/content. Cross by Willson: which members? when? did any complaint
   predate June 2024? were you even the organiser then? Evidence evaporates in four questions —
   QIRC's relaxed evidence rules go to admissibility, not weight.
3. **Confidentiality wall:** Heath cannot and will not name members or disclose their complaints;
   a guarded witness protecting confidences reads worse than no witness.
4. **STRATEGIC COST (decisive):** putting the union in Cory's witness list re-personalises the
   collective frame — the exact inversion we're running the other way. It also drags Together into
   the litigation as HIS instrument, constraining their freedom to act collectively (WHS demand,
   WHSQ) and cooling the relationship at the moment the industrial team is engaging.
5. **THE SAME PROBATIVE CONTENT ARRIVES BETTER AS:** (a) MEMBER witnesses with first-hand 2023-24
   knowledge (Trish, Carolyn, others the union may encourage VOLUNTARILY); (b) DOCUMENTS — other
   members' complaints/grievances TO MSH are MSH records (management knowledge proved from their own
   files); union-held 2023-24 correspondence if any exists; (c) Cory's own contemporaneous records.
6. **NARROW EXCEPTION:** a Together official with FIRST-HAND 2023-24 involvement — especially the
   Stressor 1(g) delegate-suppression (April 2023 delegate interest; QH-POL-248; 13 months) — would
   be a percipient FACT witness who happens to be union. ASK HEATH (after Friday): does Together
   hold any 2023-24 records touching Logan switchboard / Cory's delegate expression? Documents
   first; testimony only if a specific person saw specific pleaded facts.
7. **July 2026 events (lockout) are NOT before the QIRC in this appeal** — union witnesses about the
   lockout belong to a future general-protections/reprisal proceeding, where they are standard.

## 2026-07-16 — Addendum: the UNCHANGED-ENVIRONMENT BRIDGE (union-derived hearing evidence, upgraded)
Cory pressed the union-as-witness value at a substantive hearing. The push surfaced a real upgrade:
IF Together's collective action produces a FORMAL 2026 psychosocial risk assessment of the
switchboard (or WHSQ findings), that document CAN reach back to the injury period — because **MSH's
own 5 June 2026 letter confirms no consequential changes to switchboard practices (Item 3(c)) and
no FRMS applied until after 30 June 2024 (Items 4-5)**. Unchanged environment = a 2026 assessment
of the same conditions that existed in 2023-24. A union-triggered assessment finding hazards would
arrive at hearing as a DOCUMENT (tendered, objective, regulator-adjacent), not as Heath's opinion —
immune to the which-members/when cross that kills the testimonial version. The union's collective
WHS push is therefore ALSO an evidence-generation engine for the hearing, not just industrial
pressure. Sequencing unchanged: union acts in its own name; Cory never commissions it as a
litigation exercise (collateral-purpose optics); if the document comes to exist, tender-decision
made then with the timeline bridge (5 June letter) alongside. Heath-in-the-box position unchanged
(no first-hand 2023-24 knowledge); the two Friday asks stand: (1) 2023-24 Together records re
switchboard/delegate interest; (2) willing member witnesses.

## 2026-07-16 — Union involvement in WC appeals: the ROLES map (Cory's question — what's different here)
Cory correctly notes unions routinely involve themselves in WC reviews/appeals. The distinction is
ROLE, not involvement:
1. **REPRESENTATIVE/ADVOCATE** — the standard union role: industrial advocates appear for members
   at QIRC (IR Act agent-representation), and unions refer/fund members to their legal panel for WC
   appeals. THIS role is open NOW and is the high-value ask: Together-funded solicitor/counsel for
   the 7 Aug mention + hearing would transform resources and the costs equation (Calderbank already
   foreshadows counsel + instructing solicitor).
2. **FUNDER** — union legal-assistance schemes for work-related matters; ask Friday what Together
   provides for WC appeals at hearing stage.
3. **FACILITATOR/SUPPORTER** — member witnesses, records, collective WHS action (the engine already
   mapped), RTW/industrial pressure on the lockout.
4. **WITNESS** — the only role analysed and rejected (no first-hand 2023-24 knowledge; hearsay;
   confidentiality wall).
KEY RULE: **advocate and witness are incompatible** — a union that represents Cory cannot also
testify for him; choosing the witness box forfeits the far more valuable advocacy seat.
STAGE NOTE: review-stage union involvement (helping lodge/argue the review) is standard but that
stage passed (Oct 2024, pre-union). Arriving at appeal stage, the union's natural entries are
representation/funding + the industrial flank. TRANSITION CAUTION if representation is offered:
carriage handover mid-stream (64G filed, mention 7 Aug, Calderbank lapsing 22 Jul) needs care —
strategy is built and validated; union lawyers reviewing/adopting it ≠ restarting it. Friday asks
now THREE: (1) legal assistance/representation for the appeal; (2) collective WHS action on the
switchboard hazard; (3) 2023-24 records + willing member witnesses.

## 2026-07-16 — Together's demarcation: NO involvement at appeal stage (per Cory) — plan adjusted
Cory reports the union's position is not to get involved at the WC APPEAL stage (standard
demarcation for many unions: assist claim/review, refer appeals out). Effect on the Friday asks:
- Ask #1 (representation/funding for the appeal) — likely OFF the table; do not re-pitch it.
  RESOURCE PLAN UNCHANGED: counsel at own cost per the existing plan; recoverable on the s 558(3)/
  Calderbank costs track (offer already foreshadows counsel + solicitor; rejection 16 Jul banked).
- Ask #2 (collective WHS action on the switchboard hazard) — UNAFFECTED and now THE primary ask:
  it is industrial/WHS work squarely inside what unions DO do, and it's where Heath already
  escalated urgently. The lockout/pay fight is likewise industrial, not appeal-stage.
- Ask #3 (2023-24 records + willing member witnesses) — still fine: facilitation is not appeal-
  stage REPRESENTATION; member witnesses are voluntary individuals; a records question is modest.
CORY'S "UNIQUE MATTER" INSTINCT — channel, don't pitch: the exception-maker for a union is never
one member's appeal; it is the COLLECTIVE frame (whole switchboard, recurring member theme,
unassessed psychosocial hazard, patient-safety dimension, the full-time-position/casualisation
angle). The file he handed Heath IS that pitch. Let the industrial team read it Friday and reach
"this is bigger than one member" themselves — a conclusion they form is one they act on. Division
of labour locked: UNION = lockout/pay/WHS collective flank; CORY = the appeal (built strategy,
counsel plan); the flanks reinforce (union action raises MSH systemic exposure → settlement
pressure; appeal acceptance dissolves the lockout's stated basis).

## 2026-07-16 — Simulation: the INDUSTRIAL OFFICER'S Friday read (Form 29 + Form 20 + Form 4/64G +
## MSH objection + Heath's member-theme knowledge + the patient-safety dimension)
Composite the officer assembles: (1) a LIFE-SAFETY desk (Code Blue/MET routing) run without fatigue
governance — ADMITTED in MSH's own 5 June objection (no FRMS applied, Item 4; implemented only
after 30 Jun 2024, Item 5; no consequential change, 3(c)); (2) a member who used EVERY proper
channel (comm book → same-day-dismissed grievance → PID → suppressed delegate interest) and whose
channel-records are the exact documents MSH resists producing (the Form 29/64G fight itself
becomes evidence of the culture); (3) RECORD-KEEPING failures on a safety desk — comm-book page
removed by the manager (admitted), paging records not retained, management texts off-system;
(4) injury after the 7-hr break with the Regulator's OWN review finding unreasonable management
action; (5) the arc AFTER raising issues: abandonment dismissal on certificates → reinstated →
Jul 2026 certified-fit lockout, leave-docked, no timeframe, "Health Management processes" named —
reprisal-shaped to any industrial eye; (6) Heath's overlay: RECURRING member theme + full-time
role discussed with casuals while the full-timer is excluded (casualisation lens); (7) PATIENT
dimension: misrouted codes/delayed urgent pathology = the hazard extends past members to patients —
the public-interest frame unions escalate on; (8) the member himself: counsel-grade filed forms,
disciplined tone, organised file = low-cost, high-credibility intervention. EXPECTED CONCLUSIONS:
individual matter (pay/lockout) quickly winnable; collective matter (unassessed psychosocial hazard
on a life-safety desk) justifies collective WHS action; urgency from the reprisal pattern; the
employer's own documents carry the case. EXPECTED CAUTION: don't cut across the live QIRC appeal —
coordination conversation likely. Watch: this simulation is a PREDICTION, not their view — update
against what actually comes back after Friday.

## 2026-07-16 — Simulation COMPLETED: the officer's read WITH Form 24 (admissions) + the PID letter
Adding Form 24/responses + the PID outcome letter to the Friday bundle transforms the file's NATURE:
(1) ALLEGATION → ADMISSION: the opposing government party formally admits the spine — 7-hr break
(¶1); comm-book removal "I took it out last week" (¶14); same-day grievance dismissal (¶5); PID
determination (¶20); 48-hr retraction direction (¶21); delegate interest (¶18) vs QH-POL-248 (¶17);
payroll "IMMEDIATELY" + 25-day delay (¶¶40-41); clean 16 Nov 2023 baseline (¶34); Krishnaiah MDD
diagnosis (¶38) + deterioration warning (¶39); Review Decision contents incl. unreasonable-
management-action finding (¶37); records obtained without Form 29 (¶25). Virtually nothing rests
on the member's word alone — the officer cross-checks his account against his OPPONENT'S pleading.
(2) MEMBER → PROTECTED DISCLOSER: the ESU letter is a formal statutory determination (24 Dec 2024)
with the protections recited — incl. that reprisal is a CRIMINAL OFFENCE (ss 40-41) and a tort
(s 42), detriment defined to include adverse treatment re employment. The officer now reads the
July lockout not merely as unfair but as adverse treatment of a STATUTORILY PROTECTED person with
a PARTIALLY ADMITTED prior reprisal chronology — the highest-duty-of-care category a union has.
EXPECTED EFFECTS: urgency up; handling care up (s 65 confidentiality; criminal-adjacent dimension
means the union treads deliberately, likely pulls industrial leadership/legal in); the "impunity or
blindness" read — MSH doing this WHILE the admissions sit on a court record — hardens resolve.
Prediction discipline: test against actual Friday outcome.

## 2026-07-16 — Emily Petering (Together industrial officer — presumably the referral recipient)
Cory asked for research. THREE web searches: no public professional footprint found — no QIRC
reported-decision appearances surfaced, no accessible profile. NOTE: absence of reported QIRC
appearances is NORMAL for union IOs (most industrial work is correspondence/conciliation, never
reported; agents appear via Form 33 and only surface in published decisions). Together does run
junior/trainee IO roles (qldunions.com posting), so seniority unknown — could be junior or simply
low-profile. IMPLICATIONS: (1) the brief must carry itself regardless of reader seniority — it
does (built for exactly that); (2) verify role/seniority the polite way: ask Heath "who will be
looking after it and what's their background?" — normal member question; (3) if she acts as agent
in anything QIRC-facing a Form 33 would be filed and her appearances would become checkable.
Discipline: professional information only — no personal research on union staff (same rule as HR
staff, and she's on OUR side).

## 2026-07-16 — THE CLOSED LOOP (Cory's observation) + what union engagement means for each track
CORY'S POINT, verified against the record: every channel he ever used TERMINATED IN THE SAME UNIT.
(a) 7 Aug 2023 grievance → dismissed same day by the local chain (admitted, Form 24 ¶5);
(b) 13 May 2024 PID → ESU: no corrupt-conduct suspicion BUT "other administrative issues identified"
→ REFERRED TO HR LOGAN & BEAUDESERT (ESU letter 24 Dec 2024) — i.e. remediation of the issues was
handed to the unit whose conduct raised them; (c) NO DOCUMENTED OUTCOME of that referral has ever
been provided to Cory, and MSH's own 5 June 2026 letter confirms NO consequential changes (Item
3(c)) and FRMS only after 30 Jun 2024 (Items 4-5) — so whatever HR did with the referral, the
environment did not change; (d) injury management = IM desk INSIDE HR (roles map); (e) the July
2026 lockout decision = the same HR team. HR has been investigator, remediator, case manager and
gatekeeper of the same set of facts. DISCIPLINE: "covered up" stays working-theory; the ON-PAPER
version is the provable chain: referred → no documented outcome → admitted no change.
NEW FRIDAY ASK (add): the union should demand particulars of WHAT ACTIONS followed the ESU's
24 Dec 2024 referral of "administrative issues" to HR L&B — the answer is either "nothing"
(devastating) or a document trail that then exists and can be pursued.
WHAT UNION ENGAGEMENT MEANS —
FOR THE APPEAL (WC/2024/227): no direct legal effect (separate proceedings; demarcation holds).
Indirect, all favourable: (1) attrition neutralised — the lockout reads (on one view) as pressure
on an unrepresented appellant; a union-defended appellant can't be starved into a cheap settlement;
(2) settlement pressure UP — union activity raises MSH systemic exposure feeding the post-mention/
post-production revaluation nodes; (3) evidence generation — possible risk assessment (unchanged-
environment bridge), member witnesses, records; (4) severity/consequences record grows while the
lockout persists (their own letter ties the lockout to the rejection under appeal); (5) exit-
pathway suppression protects the appellant's status while the appeal runs. Models: no change to
v3 numbers yet; union's first move may shift MSH-folds up.
FOR THE HR ISSUES / FULL OUTLOOK: the structural meaning is EXTERNALISATION. For the first time,
every fight exits the loop: union letters go over the unit (Workforce Relations/ED People); the
certified-agreement dispute procedure exits to the QIRC (external umpire); the WHS route exits to
WHSQ (external regulator); the appeal sits with the Commission; the reprisal tort (reserved) sits
with the courts. The node that absorbed every complaint for two years is now surrounded by forums
it cannot absorb. CONVERGENCE MAP: appeal=Cory (+counsel); lockout/pay/process=union; hazard=union
collective/WHSQ; reprisal=reserved behind settlement (rule 8).

## 2026-07-16 — "Write to the Commission about the lockout timing?" — NO in the 64G/appeal file; the
## inference's proper homes; the status-quo lever
THE TIMELINE CLUSTER (real, banked): 5 Jun MSH objection to Form 29 → 23 Jun 64G filed (produce-or-
swear) → 24-25 Jun served on MSH → **3 Jul lockout (8 days after service)** → 15 Jul "discretion"
letter → 16 Jul Calderbank rejected. Inference-capable either way (intent OR effect: pressure on a
self-represented litigant with a listed application against the same entity).
WHY NOT A LETTER TO THE COMMISSION IN WC/2024/227 or the 64G file:
1. WRONG VEHICLE: the 64G proceeding is about production; there is no order available in it about
   his employment. A registry letter raising the lockout = grievance in the wrong file.
2. HANDS MSH THE COLLATERAL-PURPOSE NARRATIVE: MSH's defence to the 64G is easiest if Cory looks
   like he's using the proceeding as leverage in an industrial fight. A letter linking the two
   MERGES the channels HE has kept separate — it would damage the application it rode in on.
3. TONE DISCIPLINE (rules 1/5): a stated pattern is discounted argument; Dwyer discovering MSH's
   conduct himself is evidence. The letter would spend the asymmetry for nothing.
4. NO PRESENT PREJUDICE TO CURE: he can still prosecute the application. If MSH's conduct ever
   actually impedes the proceeding, different question.
WHERE THE INFERENCE LIVES (its native forums):
(a) GENERAL PROTECTIONS (IR Act) — the "even if no intent" insight is CODIFIED there: adverse
    action + workplace right (party to proceedings, WC claim/appeal, complaints) + REVERSE ONUS =
    the employer must disprove the reason; effect establishes the action, timing feeds the
    inference. Reserved track; union/advice-led; interim orders possible if escalation (IME/show-
    cause) occurs mid-proceedings.
(b) UNION DISPUTE ROUTE — certified-agreement dispute-settling procedure exits to QIRC lawfully
    (the lockout before the Commission through the PROPER door). **STATUS QUO LEVER: QLD public
    sector certified agreements' dispute clauses typically preserve/restore the pre-dispute status
    quo while the dispute is processed — i.e., notification of a dispute may itself require
    restoring him to the roster/pay.** FLAG TO THE INDUSTRIAL OFFICER (they will know the clause).
(c) SETTLEMENT/SEVERITY NARRATIVE — the cluster prices the deal; their own 15 Jul letter ties the
    lockout to the rejection under appeal.
(d) 7 AUG HEARING: volunteer NOTHING about the lockout; if Dwyer asks about circumstances, answer
    honestly and briefly. Engineered mentions = discounted argument + collateral-purpose gift.

## 2026-07-16 — STATUS QUO applied to Cory's facts + the IO briefing script
MECHANICS: QLD public health sector certified-agreement dispute clauses provide (in substance) that
once a dispute is notified under the dispute-settling procedure, the STATUS QUO existing immediately
BEFORE the dispute continues while the procedure runs (local resolution → escalation → QIRC), work
continuing as normal — typically subject to a GENUINE-SAFETY exception. (Exact clause number/wording
to be confirmed by the IO against the operative agreement — do not assert a clause number.)
APPLIED HERE: the dispute = the 3 JULY decisions (exclusion + leave-debit). Status quo immediately
prior = ROSTERED AND WORKING (12 months, same role, adjusted hours). Union notifies dispute →
status quo argument = restore to roster + stop debiting leave until resolved.
MSH'S PREDICTABLE COUNTER: the safety exception ("pending medical clarification"). ANSWERS: (1)
treating GP certifies FIT with restrictions — on their own instrument (the ECC they required);
(2) 12 months working the same role; (3) NO risk assessment exists (they cannot invoke safety
having never assessed it); (4) Forrest 7 Jul letter acknowledged restrictions already being
accommodated (usable with the union — distinct from the banked 8-hr item); (5) even if exclusion
is maintained on claimed safety grounds, the safety exception does not authorise charging HIS
accruals — the orthodox compromise is exclusion ON PAID SPECIAL LEAVE pending resolution.
REALISTIC OUTCOMES ladder: best = restored to roster; middle (likelier fast win) = held out ON PAY,
leave re-credited, pending the RFI; floor = dispute escalates to QIRC with the pay question live.
IO SCRIPT delivered to Cory (ask-not-instruct tone; IO owns the running; confirm operative
certified agreement + clause; appeal demarcation one line only).

## 2026-07-16 — The "genuine safety issue" exception: PRECISION on Cory's point
Cory: "there is no real genuine safety issue because MSH has never raised it." REFINED — they HAVE
used safety VOCABULARY ("psychosocial hazards or risks," "safely accommodate," "safe and
sustainable") so "never raised it" is quotable-against-us. The accurate, unanswerable version:
**MSH has never IDENTIFIED or PARTICULARISED a genuine safety issue** — no specific hazard named,
no incident cited, no risk assessment conducted, no connection drawn between any restriction and
any danger. Generic references to unassessed "potential" risks are not a genuine safety issue; the
status-quo exception requires specificity and is construed narrowly (real/immediate, not
speculative caution). THE PROOF SET: (1) decision inside 58 minutes — no assessment could have
occurred; (2) 12 months working the same role — if a genuine issue existed it existed all year,
unraised; (3) Forrest 7 Jul: restrictions already accommodated; (4) the ECC is THEIR OWN instrument
for answering the safety question and it answered it: fit with restrictions; (5) no incident ever
cited. PRE-EMPT their best card ("safety-critical emergency-codes role justifies caution"): the
treating doctor certified fit FOR THAT ROLE; the role's criticality was identical for the 12 months
they rostered him; caution unattached to an assessment is not a safety issue, it is a decision
looking for a justification. DRAFTING RULE: never "they never raised safety" — always "no genuine
safety issue has been identified, particularised, or assessed."

## 2026-07-16 — Channel discipline CLARIFIED: appeal-as-motive is UNION-CHANNEL material (correctly placed)
Cory flagged he has already put the appeal facts to Heath as possible cause of MSH's motive (14 Jul
email: "concerned this may be connected to my current WorkCover appeal... injury and subsequent
reprisal"). CORRECT PLACEMENT — the rule is channel-specific, not content-suppression:
✅ TO THE UNION (his representative, in confidence): the suspected motive is necessary background,
   and stating it on 14 July created a DATED CONTEMPORANEOUS RECORD of the belief — valuable if a
   general-protections case is ever run (belief formed in real time, not reverse-engineered).
✅ IN A FUTURE GP/reprisal FORUM: motive is the pleaded case; reverse onus makes MSH disprove it.
❌ TO MSH/HR (any letter, incl. the dispute letter): never — the IO's letter stays facts/instruments
   (roster, pay, leave, particulars); motive in an MSH-facing letter converts a clean dispute into
   a war of allegations and hands them "vexatious" framing.
❌ TO THE COMMISSION in the 64G/appeal files: never (collateral-purpose gift).
NUANCE for the IO: the motive brief sits BEHIND their letter, not in it — IOs know this; if the
union escalates to GP, it surfaces there with the onus doing the work.
NOTE: union correspondence is confidential but not legal-professional-privileged per se — keep
union emails factual and dated (his are), assertions framed as belief/concern (his was: "I am
concerned that this MAY be connected").

## 2026-07-16 — Calderbank economics clarified for Cory: the concessions were CONDITIONAL and now REVERT
Cory processing the rejection: he conceded the privacy/medical-info complaint (6.2(d)) and laid out
the full merits roadmap, and they still declined. CLARIFICATIONS LOGGED:
1. **The 6.2(d) release DIED WITH THE REJECTION.** Releases in a rejected/lapsed offer never take
   effect — the privacy-handling complaint is FULLY PRESERVED (as is the 64G, per 6.2(c) never
   operating). He offered generosity; declined generosity evaporates; the RECORD of having offered
   it remains — for costs and for the model-litigant point.
2. **The merits roadmap cost almost nothing:** paras 2-5.4 are the pleaded/admitted public record
   (9A, Form 24, Review Decision, MSH 5 Jun letter) — they already had every document. The two NEW
   arguments shown (5.5 Reese FTE misrepresentation; 5.6 ultra vires delegation) were deliberate
   pressure levers built on documents BOTH sides hold (Item 13 instrument; 10 May email) — new
   argument, not new evidence. The BANKED items (8-hr admission, direction-of-flow, timing
   inference, Forrest set) were NOT in the offer and remain banked.
3. **A reasoned offer is the POINT of a Calderbank:** a bare offer has weak costs consequences; an
   offer the offeree could fully evaluate — merits + authorities + concessions — makes rejection
   maximally "unreasonable" on assessment. Their no-reasons rejection of a fully-reasoned,
   concession-laden offer ≈ the strongest costs posture available to an appellant.
4. NEXT-OFFER NOTE: the lapsed concessions do NOT have to reappear. The post-production renewal can
   drop 6.2(d) (keep the complaint), drop or reprice 6.2(c), and raise the costs ask — the price of
   saying no is the offer getting worse, and the July offer documents they were warned.

## 2026-07-16 — "Start the privacy complaint / the proceeding NOW as pressure?" — NO (analysed); limitation caveat
RECOMMENDATION: do NOT commence the privacy complaint or any reprisal proceeding now as settlement
pressure. Reasons:
1. **OPTICS TORCH THE COSTS POSTURE JUST BUILT:** a complaint filed within days of the 16 Jul
   rejection reads as retaliation for non-acceptance — undermines "genuine good-faith offeror" and
   hands the Regulator a pressure-campaign/vexatious narrative for both the costs fight and the
   settlement table. The offer's model-litigant framing works BECAUSE he has been restrained.
2. **PRESSURE ASYMMETRY (the maths fail):** OIC privacy processes are slow (agency-first step,
   ~45 business days, then OIC, months+), remedies modest, handled by a different unit — LOW felt
   pressure on the appeals/legal decision-makers. Cost to him: bandwidth before 7 Aug (critical
   path = mention + Krishnaiah), hardened respondent (multi-front attack → wagons circle →
   P(settle) DOWN not up), muddied restraint posture before Dwyer.
3. **RULE 8 (sequencing) + DEAL INVENTORY:** the complaint's HIGHEST value is as the 6.2(d)-style
   release chip in the eventual deed — spent now, it can't sweeten the renewal offer. The rejection
   REVERTED the chip to him; launching it burns it.
4. **REPRISAL TORT ("the proceeding"):** hard no now — rule 8 sequenced behind WC settlement;
   requires specialist advice first (PIPA applicability/late-notice s 9A — standing action item);
   3-yr limitation open to ~mid-2027; premature commencement is the collateral grenade.
5. **THE REAL PRESSURE IS ALREADY SCHEDULED:** 7 Aug produce-or-swear; Krishnaiah report; counsel
   appearance; union flank (dispute/status quo; possible WHS collective action). Each moves the
   Regulator/MSH more than an OIC complaint could.
⚠️ **CAVEAT — VERIFY THE PRIVACY COMPLAINT CLOCK:** IP Act complaint pathway is agency-first, then
OIC, with time limits (commonly 12 months from the conduct). Conduct spans: records obtained
without Form 29 (2024-25, admitted Form 24 ¶25 — OLDER, window may be closing/closed) vs the 13 Jul
2026 QSuper disclosure (FRESH window). ACTION: verify the applicable window(s); if the older
conduct's clock is closing, PRESERVE quietly (minimal internal agency complaint, administrative
tone, no publicity, no linkage to the appeal) — preservation ≠ pressure campaign. Distinguish
preserving rights from launching fronts.

## 2026-07-16 — TWO NEW DISCLOSURES FROM CORY (privacy track inventory)
**1. TAYLOR SHARED A SENSITIVE PERSONAL LEGAL MATTER (DV-adjacent).** Cory reports manager Taylor
shared information about a domestic/family legal matter involving him and his younger sister —
which he describes as a LESSER order/matter than a DV order (exact instrument TBC). Logged
deliberately at LOW DETAIL (dignity + privacy; detail only as/if evidentially needed).
PROVENANCE NEEDED before any use: (a) when shared, (b) to whom, (c) how Cory knows (who told him /
did he hear it), (d) witnesses, (e) HOW TAYLOR KNEW — critical fork: if she learned it through
employment systems/disclosures (leave forms, EAP, HR file, police-check paperwork) → IP Act/privacy
breach territory + serious misconduct; if private/social knowledge shared at work → conduct/
bullying/dignity issue (still union brief material, different instrument). (f) approx date.
USES: union brief (conduct pattern re Taylor); severity/institutional-attitude thread; privacy
complaint inventory IF the employment-systems fork is confirmed. NEVER in correspondence; NEVER on
the WC/64G track. Cory to write a dated private statement (who/what/when/how known) THIS WEEK.
**2. THE QSUPER MEDICAL-RECORDS SCOPE POINT SHARPENED.** Cory's own request to the fund was a
PAYSLIP-BASED reassessment (partial payments) — payslips only. He had HIMSELF already told the fund
he was working at reduced amounts (and the prior against-advice year). The 13 Jul push of the ECC
(medical information) to ART by Harrison therefore: (a) exceeded the object of HIS request
(payslips); (b) supplied medical info the fund did not need for anything he asked; (c) rests on the
p7 authorisation which permits the FUND TO REQUEST info "in relation to your claim" — direction-of-
flow gap + closed-claim gap (both already banked). NUANCE preserved for honesty: the earlier
recoupment thread (Ings) included a fund request for payslips/RTW docs/WC status — any MSH reliance
on THAT request must still fail the 13 Jul context (different purpose: "return to duties" support,
claim closed, employer-initiated call). ZAPPIA LETTER ADDITION: ask the fund to confirm IN WRITING
(i) what information ART requested from MSH and when, (ii) what ART received from MSH and when —
the fund-side mismatch artifact (what was requested vs what was pushed).
IP ACT FRAME (post-1 Jul 2025 QPPs): agency disclosure of personal (incl. health) information
requires purpose-consistency or an exception (consent/scope; reasonably-expected directly-related
secondary purpose; authorised by law). Scope of a claim-application authorisation ≠ standing
authority to volunteer medical records post-closure. FRESH complaint window runs from 13 Jul 2026.
All of it: INVENTORY (banked) — no new letters now; the what-authority answer (p7) is already an
artifact; deed chip + union brief + possible preserved complaint per the limitation check.

## 2026-07-16 — THE ECC'S PURPOSE (Cory's point): a partial-payment instrument PRESUPPOSES working
Cory's clarification: the fund's interest in the ECC does not signify absence from work. The ECC in
the QSuper context is the fund's instrument for PARTIAL injury benefit arithmetic — certifying
capacity/restrictions so the fund can pay a PARTIAL top-up while the member WORKS reduced hours
(and/or retrospectively document capacity for the payslip-based recoupment reassessment). Work-half
+ half-top-up is the DESIGN of partial IP benefits.
THE INVERSION OF THE DOCUMENT: MSH took a work-support instrument (exists BECAUSE the member works)
and read it as an exclusion trigger ("unable to facilitate... return"). The document presupposes
work; they used it to end work.
THE TAXONOMY DEFECT in the 15 Jul discretion paragraph: MSH classes "those receiving QSuper IP
benefits" alongside "Health Management processes" as non-WCRA management categories — implicitly
treating benefit recipients as non-working. WRONG BY SCHEME DESIGN: partial IP benefits exist
precisely FOR working people on reduced hours. Even on an ACTIVE claim, working + partial top-up
coexist by design — so "QSuper arrangement → employer discretion → no duties in any capacity" is
incoherent: the exclusion DEFEATS the very arrangement cited to justify it.
FORMULATION (for the IO, union brief): "The letter treats my QSuper arrangement as a reason I
cannot work. The arrangement is the opposite — partial income protection exists to support people
who ARE working reduced hours. The exclusion doesn't respect that arrangement; it destroys it."
STATUS: IO talking point + union brief; Heath email already carries the serving-employee framing
(Issue 1) — no reopening; correspondence unchanged.

## 2026-07-16 — Further sharpened: his actual ask to QSuper was SELF-SERVE ARITHMETIC
Cory's clarification of the fund request: he asked QSuper to calculate his benefit position from
data THE FUND ALREADY HOLDS — his contribution flows (~15% from wage), which map to earnings — and
said if they needed every payslip they should REQUEST it. Context: he was struggling mentally with
the volume of admin and reasonably delegated the arithmetic to the fund.
EFFECT: the request-vs-received gap is now MAXIMAL: he asked for (a) a calculation from the fund's
own records, (b) at most a payslip request if needed. What MSH pushed (13 Jul): MEDICAL RECORDS.
Nothing in his ask required, invited, or touched medical information. Zappia-letter questions
already cover it (what was requested vs received; calculation basis/provision/period).
HANDLING NOTE: the "struggling mentally at too many things" context is honest and humanising —
UNION/inventory/severity material only. NEVER volunteered in correspondence with MSH or the fund
(incapacity-file risk). In letters the admin-delegation point, if ever needed, is framed as:
"I asked the fund to calculate from its own contribution records and to request any payslips it
required" — reasonable, complete, no health commentary.

## 2026-07-17 — External-AI revision of the Zappia letter REVIEWED — REJECTED in key parts
Cory pasted an externally-revised Zappia letter ("ready to send immediately"). Red-team verdict:
ADOPT: the priority-split (Q1/3/4/5/6 immediate; Q2 calculation within 14 days) — good mechanics.
REJECT (each logged):
1. **Point 5 second paragraph = STRATEGIC BREACH.** Adds WHS Act duty-of-care + "Fair Work Act 2009
   (Cth) adverse action" + "employer accountability" + "recent attempts by the employer to place me
   out of work" to a FUND letter. (a) THE FUND CHANNEL IS NOT PRIVATE — Harrison corresponds with
   Zappia and the 15 Jul letter was JOINTLY ADDRESSED; anything sent to ART must be assumed readable
   by MSH within days. This paragraph would: preview the adverse-action theory (tips off the
   reverse-onus play), volunteer "recovery phase" self-description + "against medical advice" +
   "unfair dismissal" history IN WRITING (incapacity-file gifts), and convert the neutral
   administrative letter into advocacy — killing the blandness that makes Q4 deadly. (b) **FWA 2009
   (Cth) DOES NOT APPLY to Qld public sector employees** — QH employees are state-system (IR Act
   2016 (Qld)). The citation is flatly wrong and would mark the letter as boilerplate.
2. **Unverified policy citations REJECTED (rule: verified-only).** "Super Savings Insurance Guide"/
   "Income Protection Benefit Guide 1 July 2026" + quoted definitions were never verified against
   HIS product — and "Super Savings" is the ex-Sunsun/ART product line; QSuper members typically
   remain on QSuper-branded insurance guides post-merger. Wrong-product citations = easy deflection
   + credibility hit. The stronger move stands: ASK THE FUND to cite its provisions (Q2(b)).
3. **The inserted partial-disability definition is an OWN GOAL:** "partial payments do not apply to
   an employee who is fit to work and able to perform all duties" — he is NOW certified fit with
   minor restrictions; arguing definitions invites the fund to shrink the partial entitlement and
   GROW the overpayment. The recoupment position stays documentation-driven, not definition-argued.
4. Q4 preamble "to confirm the employer's compliance..." — accusation vector removed; Q4's power is
   its administrative blandness.
5. Posted-letter format dropped — email to Zappia keeps the established channel and speed.
FINAL letter (v2) written to drafts/2026-07-16_ART_Zappia_letter_DRAFT.md: original six questions +
priority split + 14-day overall ask. CHANNEL RULE RESTATED: write every fund letter as if MSH reads
it the same afternoon.

## 2026-07-17 — Heath status update: brief DELIVERED in full; industrial team ACTIVELY engaged
Saved: documents/2026-07-17_Heath_still-reviewing_industrial-team.pdf.
1. **The six-issue policy brief WENT on Thu 16 Jul 16:42** — verified complete against the draft:
   all six issues intact (incl. Issue 6 inversion + the Caroline/full-time paragraph + the held-
   response line). Cory's own tweaks: "I will however include you in any further correspondence";
   Issue 1 adds "as requested by my employer" (accurate — the ECC was their requirement); Caroline
   paragraph lightly trimmed. All fine.
2. **Heath, Fri 17 Jul 15:27:** "still reviewing this information and I'm speaking to our industrial
   team about best steps forward. Once I have more I'll let you know." READ: active engagement —
   the industrial-team conversation is LIVE and concerns the SHAPE of intervention ("best steps
   forward"), not whether to intervene. A Friday-afternoon unprompted status update from an
   organiser = the file is being worked, not parked.
3. CADENCE: expect substantive word early-mid week of 20 Jul. NO CHASING before ~Wed 22; if quiet
   by then, one polite line — or tie any contact to a NEW event (next payslip debit; the RFI
   landing; a SmartJobs ad).
4. HOLDS unchanged: nothing to HR; held letter stays held; Zappia letter GOES (fund admin ≠
   employer action); payslip to obtain; SmartJobs daily; if the Ma RFI lands → brief Ma, copy to
   union same day. Critical path unchanged: Krishnaiah report + 7 Aug mention. Calderbank lapses
   Wed 22 Jul 4pm — no action, let it lapse.

## 2026-07-17 — INDUSTRIAL OFFICER CONSULT BOOKED: 12pm, 28 JULY 2026
Timing map: Calderbank lapses 22 Jul → IO consult 28 Jul → 64G mention 7 Aug (10 days later). If
the union moves in the week after the consult (letter/dispute notification), MSH faces union
pressure and the mention in the same fortnight — maximal compounding, aligned with the v3
settlement model's post-mention pathway.
PREP PLAN (build the MEETING PACK by ~25 Jul, updated for anything that lands between):
1. ONE-PAGE CHRONOLOGY (3 Jul 14:32→15:30 lockout; the four unanswered/refused asks; 15 Jul
   discretion letter; leave debits running).
2. DOCUMENT SET (in order): 15 Jul Harrison letter; ECC; 3 Jul emails; Forrest 7 Jul letter;
   CURRENT PAYSLIP (⚠️ obtain before the 28th — Exhibit A); the six-issue brief (already with
   Heath); Zappia letter + any ART reply by then.
3. THE THREE ASKS: (a) dispute notification + STATUS QUO (restore roster / stop debits);
   (b) fallback: exclusion on PAID SPECIAL LEAVE (Directive 12/24), leave re-credited;
   (c) particulars: which Health Management process/instrument/decision-maker + what followed the
   ESU 24 Dec 2024 referral to HR L&B.
4. THE QUESTIONS: operative agreement + clause number; dispute timeline/local step; notification
   recipient; what they need from him; their QH health-management experience.
5. ONE-LINE DEMARCATION: appeal is separate, counsel-run; this consult = roster/pay/leave/process.
6. EVENTS BETWEEN NOW AND THEN feed the pack: Calderbank lapse (22nd, no action); possible RFI to
   Ma (if it lands: to Ma briefed + union same day); ART/Zappia reply; payslip; SmartJobs.

## 2026-07-17 — What ACTUALLY landed on the union's desk (Cory's category analysis — adopted)
Cory's point, adopted into the read: the review is slow because the file contains OBJECTS OUTSIDE
AN ORGANISER'S PROFESSIONAL CATEGORY SET, not just volume: (1) a VERIFIED PID — statutory
protected-discloser status, formally determined, protections recited on MSH letterhead (organisers
handle grievances; almost never a determined PID with a partially-admitted reprisal chronology);
(2) the ENTIRE SWITCHBOARD INFRASTRUCTURE documented — comm book, paging retention, FRMS absence,
directory/information-flow restriction — a system-level anatomy converting their "recurring theme"
anecdotes into a documented case study; (3) the PATIENT-SAFETY dimension (misrouted codes, delayed
urgent pathology) — a card unions rarely hold; transforms industrial issue → public-interest issue;
(4) the MANAGEMENT-CONDUCT pattern they'd sensed but never had paper for; (5) a Form 29 NNPD +
64G produce-or-swear — instruments an organiser may literally never have seen. CONSEQUENCE: a
TRANSLATION task — Heath must explain to the industrial team what he's even holding; explains the
observed behaviour (careful, escalating, parallel review). IMPLICATION FOR THE 28th PACK: include a
half-page "WHAT THIS FILE IS" orientation map (the five objects, one line each + which forum each
belongs to) — do not assume IO familiarity with NNPD/64G mechanics; Cory may know the disclosure
machinery better than anyone in the room, and the pack should make that easy, not awkward.

## 2026-07-17 — The 5 June letter → oath conversion (the produce-or-swear trap, restated sharp)
Cory's framing adopted: the MSH objection letter we have dismantled analytically is now the
document MSH must STAND BEHIND ON OATH at 7 Aug. Mechanism: the letter's assertions were FREE
(lawyer-drafted, unsworn, no personal exposure): no FRMS applied (Item 4); implemented only after
30 Jun 2024 (Item 5); no consequential change (3(c)); paging records not retained (Items 1-2);
texts off-system (Item 14). The 64G verification-affidavit structure forks them: PRODUCE (the
records arrive — his case builds) or SWEAR (a named deponent verifies searches + non-existence on
personal oath, exposed to cross-examination). Each branch serves the appellant:
- Sworn "no FRMS existed / not retained / nothing changed" = the course-of-inaction case PROVED BY
  THEIR OATH — and sworn non-retention of paging records for a life-safety desk raises its own
  records-governance problem (Public Records Act obligations) the deponent personally owns.
- Production = the documents themselves.
DEPONENT PROBLEM (theirs): someone at MSH must put their name and oath on statements a lawyer
wrote — the letter's author (Ruttan) can't swear to operational facts; an operational witness may
not adopt the letter's confident wording once personal exposure attaches. This gap is the engine of
the MSH-FOLDS pathway (consent to production to avoid the affidavit) — WATCH for a consent-order
letter pre-7 Aug; protect the verification affidavit in any consent order (per §16 v2).
POSTURE RULE unchanged: at the mention this is presented as ordinary machinery, neutrally — the
Commission should see a tidy application, not a trap being savoured.

## 2026-07-17 — Form 20 re-read against the "bigger picture" standard + open lead CLOSED
1. **LEAD CLOSED:** the phone-directory restriction Cory raised on 15 Jul ("second information
   manager... access restricted from Switchboard") is ALREADY IN EVIDENCE — Form 20 ¶22: the
   Telecommunications Coordinator role (Stibbard), her 18 Jul 2023 email "removing everyone's
   access to the database," updates funnelled through her part-week attendance, numbers falling
   out of date, complaints landing at the Switchboard. Provenance question answered — documented,
   sworn, with the records gap tied to Form 29 Items 3(a)-(c).
2. **Assessment (for the register):** the Form 20 performs the panorama function by construction —
   Part B builds the world (¶6 "the point at which urgent help is summoned"; ¶19-22 the complaints
   funnel incl. complaints about the manager routing to the person who'd escalate to her — the
   closed loop in miniature; ¶23-25 the "standing condition" baseline); Parts C-F drop dated,
   admission-anchored facts into that world; the reader assembles the pattern unassisted. Every
   evidentiary hole is tied to a Form 29 item (¶9, ¶22, ¶26, ¶29) — the picture and the necessity
   case are the same text. ¶50 (SPOK upgrade-vs-disposal reconciliation on oath) is the sharpest
   paragraph in the file. Empirical validation: Heath's one-pass escalation.
3. Note: ¶45 ("currently working at 0.5 FTE") was accurate when affirmed 18 Jun 2026 — the July
   lockout post-dates it; the ONE-PAGER carries the spine to the present for the IO meeting.

## 2026-07-17 — 9C (Regulator SOFC) contradiction matrix built
Cory's insight — the 9C contradicts itself and the record — validated and structured into
skill/references/9C-contradiction-matrix.md. TIER 1 (provable now): (A) "not causative"/"reasonable"
vs the Regulator's OWN admitted Review Decision (7-hr = UMA; employment = significant contributing
factor; Form 24 ¶37) while asking to CONFIRM that decision; (B) 7<8 breach CONCEDED on their pleading
(¶22a + ¶22e); (C) "human error" ≠ reasonable management action (¶22a, ¶14); (D) COVID decline reason
conceded wrong — attachments "WERE present" (¶14); (E) "timely manner" vs admitted 25-day AVAC delay
(¶20 vs Form 24 ¶40-41); (F) cherry-picked medical records (¶8 relies on records for anxiety history /
¶9 won't admit diagnosis; admitted clean 16 Nov 2023 record). TIER 2: (G) "reasonable" fatigue action
vs MSH 5 June admission NO FRMS until after 30 Jun 2024. TIER 3 (disclosure tests): (H) "Reese unaware
of PID" vs 15-16 May correspondence; (I) "equitable roster" vs Items 8-9; (J) grievance Aug-Nov
timeline corroborates the unresolved issue. Discipline: T3 = working; not for the 64G; feeds hearing
submissions + settlement + reception model. Note the defence is at v4.4 (repeatedly redrafted).

## 2026-07-17 — Causation/severity: the injury mechanism of raising safety concerns and being ignored
Cory's point — how acute is the effect of raising a patient-safety concern and having it not taken
seriously/not investigated, in a life-safety environment. This is a CAUSATION spine point for the
KRISHNAIAH BRIEF + evidence-in-chief (NOT the 64G). Structure:
1. ROUTE IT CLEANLY — separate the two things: (a) the corrupt-conduct PID (13 May 2024, determined)
   = REPRISAL/parallel track, keep the "fraud" content off the WC record; (b) the repeated
   PATIENT-SAFETY/WHS concerns (comm-book on-call-contact entry; 7 Aug 2023 grievance re unsafe
   rostering/fatigue; misrouting/roster/directory failures; fatigue) raised through proper channels
   and NOT investigated or actioned = the clean WC COURSE-OF-INACTION spine. The severity/causation
   power lives in (b); it does not need the corrupt-conduct allegation.
2. MECHANISM (for the psychiatrist to develop, not for me to assert as medico-legal fact): the
   specific stressor of holding RESPONSIBILITY for a life-safety function WITHOUT AUTHORITY or
   support (affidavit ¶¶23-25 "standing condition"), raising the danger repeatedly, and being met
   with dismissal/non-investigation/no change — a recognised psychological injury pathway
   (powerlessness/entrapment; the moral weight of a foreseeable-harm concern ignored where patients
   are at risk). Hawes already recorded the mechanism ("ongoing breaking of workplace rules by
   bosses, victimizing him" — Form 24 ¶36 admits the certificate states it).
3. PROVABLE FROM THEIR OWN ADMISSIONS: PID determined (admitted, Form 24 ¶20); grievance
   acknowledged a rostering error (Form 24 ¶5); NO FRMS until after 30 Jun 2024 + no consequential
   changes (MSH 5 June, Items 4-5, 3(c)); comm-book page removed (admitted ¶6). So "raised it →
   nothing investigated/changed" is largely PROVEN, not merely asserted — the non-action is on the
   record. The acuteness follows from the environment being LIFE-SAFETY (their own admission ¶8).
4. DISCIPLINE: this is the psychiatrist's causal opinion to make; I articulate the mechanism, the
   report proves the link (Willson probes causation hardest — see comparable-cases §7). Krishnaiah
   brief must connect: safety concerns raised → institutional non-response → powerlessness in a
   life-safety role → MDD onset 18 Jun 2024. Keep corrupt-conduct/PID-qua-fraud OFF; use the WHS/
   patient-safety non-investigation framing.

## 2026-07-17 — Causation dimension 2: the complaints load "I could never put down" (no-recovery mechanism)
Distinct from the ignored-safety-concerns stressor: the CHRONIC, CYCLICAL, UNDISCHARGEABLE load —
affidavit ¶¶19-22. Complaints from public/clinicians/staff arrive at the Switchboard FIRST, to Cory;
he actions/resolves a substantial proportion himself; those he escalates to the Line Manager return
UNACTIONED (she was frequently unavailable) and accumulate BACK at the Switchboard — including
complaints ABOUT the manager herself, i.e. he managed complaints concerning the very person he'd
escalate to. The 15 May 2024 email (his words): matters "often left unresolved due to ambiguity
around when [Ms Taylor] is available." MECHANISM (psychiatrist's to develop): the absence of any
OFFLOAD POINT or CLOSURE — a terminal accountability sink with no boundary and no recovery state —
is the chronic-load / no-detachment pathway (allostatic load; entrapment), compounding the acute
stressors (fatigue, ignored safety concerns) into the cumulative COURSE that produced the injury.
PROVABLE: ¶¶19-22 sworn; the 15 May 2024 email; the escalated-complaint records held in the Line
Manager's mailbox (Form 29 Items 3(a),(b)) — disclosure. Feeds the Krishnaiah brief: the injury is
CUMULATIVE (global evaluation / Delaney) — not one event but a standing condition of unrelieved,
unresolvable responsibility. Keep WC-clean; corrupt-conduct content stays parallel-track.

## 2026-07-17 — Causation dimension 3: DURATION — "unresolved for prolonged time" (the injury variable)
The temporal amplifier that unifies dimensions 1-2. Transient stress resolves; PROLONGED UNRESOLVED
exposure is what converts stress into injury (sustained allostatic load with no return to baseline).
The duration IS the pleaded "course" (~June 2023 - June 2024). LEGAL FORCE:
1. Defeats the Regulator's ATOMISATION defence — the 9C tries to isolate events as one-off "human
   error... NOT intentional or repeated" (¶22a). Duration/persistence is the answer: these were not
   isolated errors but a sustained unremedied condition. Global evaluation (Delaney) looks at the
   whole course, not discrete incidents.
2. The Regulator's OWN material proves the prolongation: the 9C grievance narrative runs Aug→Nov
   2023 (¶13, "14 Nov re shift/break compliance"); delegate suppression ran >9 months (Form 24
   ¶19 disputed, Item 19); pay issues Feb-May 2024; MSH 5 June confirms no change until AFTER 30
   Jun 2024. The failure to resolve OVER TIME is on their record.
3. THIS IS THE 64G NECESSITY RATIONALE (affidavit ¶47): individual examples show conduct OCCURRED;
   only the complete export shows the CUMULATIVE VOLUME AND FREQUENCY across the whole period — i.e.
   the prolongation. The disclosure is sought precisely to prove duration/extent, which is the
   injury-producing variable. Duration ties the medical case and the disclosure case together.
Krishnaiah brief: frame the injury as the product of PROLONGED UNRESOLVED exposure (chronicity),
not any single stressor — this is what makes it clinically an MDD and legally a course-of-conduct
injury that survives Willson. Keep WC-clean.

## 2026-07-17 — Medical causation framework built (Krishnaiah brief + pre-existing-anxiety rebuttal)
Built skill/references/medical-causation-framework.md. Answers Cory's "most defensible diagnosis +
mechanism vs the displaced/undiagnosed anxiety" question. BOUNDARY stated: diagnosis = Krishnaiah's
independent judgment; I supply questions/foundation/legal tests, not a scripted conclusion.
FOUR independent answers to the 9C ¶8 "past history of anxiety" displacement: (a) admitted clean
16 Nov 2023 baseline + symptom-mention ≠ diagnosed disorder; (b) NEW discrete MDD onset 18 Jun 2024;
(c) AGGRAVATION compensable even if pre-existing (significant contributing factor to the aggravation);
(d) eggshell-skull. Mechanism = the 3-dimensional course (acute powerlessness / chronic no-recovery /
temporal prolongation) anchored in admitted facts. Whole-arc requirement: own the 2025 against-advice
return + crash as SEQUELAE/severity, not intervening cause. Letter-of-instruction question set drafted.
⚠️ VERIFY operative s 32 threshold + aggravation subsection as at the mid-2024 claim before filing.
Critical path: this is the report that converts the admitted CONDUCT record into proven CAUSATION.
