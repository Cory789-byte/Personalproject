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
