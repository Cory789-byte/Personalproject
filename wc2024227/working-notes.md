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

## 2026-07-17 — QSuper medical-disclosure complaint DRAFT — ADVISE DO NOT SEND AS DRAFTED + big findings
Files saved: 2026-05-28_QSuper_Resolutions_complaint_response_Beck.pdf; medical/2025-02-13_
MindAndMemory_report_QSuper_LouiseIngs.pdf; medical/2025-07-22_OurMedicalAshmore_GP_records_via_
Saines.PDF; 2025-07-22_Regulator_SOFC_served_via_Saines.pdf; evidence/ two payslip xlsx.

### FINDING 1 — the cornerstone psych report IS a QSuper document "not for medico-legal use"
The "Mind and Memory Service" report, 13 Feb 2025, addressed to Louise Ings (QSuper Claims Manager),
MDD 296.23 — is the SAME 13 Feb 2025 report the Calderbank called "Exhibit A4 Krishnaiah report."
Marked TWICE on its face: "disclosed for Qsuper and not for medico-legal use." IMPLICATION: the
appeal's cornerstone medical evidence is a QSUPER IP-claim report NOT prepared as a WC medico-legal
report. This is a WEAK medico-legal foundation and REINFORCES the critical-path action: commission a
PROPER, properly-instructed UPDATED medico-legal report (per medical-causation-framework.md). Do NOT
spotlight the QSuper report's status publicly.

### FINDING 2 — QSuper's 28 May letter (Beck) already DENIES disclosure + gives live admin facts
"ART Life... no indication that medical reports... disclosed... to any external parties... no medical
information has been released from your claim file." Invited specifics. ALSO: IP payments placed ON
HOLD from 1 June 2026 pending recalc; Zappia appointed; overpayment recalc underway; AFCA named as
escalation. So QSuper has ALREADY said "we released nothing" — a formal accusation contradicting that,
without proof of the path, is high-risk.

### FINDING 3 — the likely path is the REGULATOR'S NNPD, not a QSuper release
The report appeared in Matheson's (Regulator) 22 Jul 2025 email to Saines, attached to NNPD docs.
Most probable path: the Regulator's Notice of Non-Party Disclosure — the one NEVER SERVED ON CORY
(admitted Form 24 ¶25; affidavit ¶44) — obtained his medical records from the GP (Our Medical
Ashmore) or the provider, sweeping up a copy of the QSuper-addressed report the psychiatrist had
sent the GP. If so, QSuper disclosed NOTHING; the GP produced under legal compulsion. The REAL
privacy grievance is against the REGULATOR (unserved NNPD), which is ALREADY pleaded/admitted and
BANKED (Calderbank 6.2(d) medical-info-handling complaint; reserved, WC/reprisal track).

### ADVICE — do NOT send the accusatory complaint. Reasons:
1. Wrong target / likely-wrong premise (QSuper said no release; path points to Regulator NNPD).
2. Antagonises QSuper mid-recalculation — need their cooperation (closure confirmation, payment
   history, fair overpayment recalc). Sours it; may trigger AFCA-on-wrong-premise / lawyer-up.
3. Merges channels (privacy + overpayment + employment "losing my employment") + fires a reserved,
   off-sequence privacy item (rule 8).
4. Spotlights own-case vulnerability (cornerstone report = QSuper doc not for medico-legal use).
INSTEAD: answer Beck's invitation NARROWLY + NEUTRALLY (a QUESTION, not an accusation) — did ART/
QSuper RELEASE the report to any third party, OR PRODUCE it under any NNPD/legal compulsion? (that
distinction is the nuance behind their "released nothing"). Keep the real grievance banked vs the
Regulator. Overpayment stays in the Zappia admin channel. Employment stays with the union. Commission
the proper updated report.

### FINDING 4 — PAYSLIP DATA = Exhibit A gold (union + overpayment)
FY2025-26 (26 fns): avg 5.8 work days/fn (~58% FTE), 34.33 unpaid days, 16.32 sick; recent slips
show declining work + rising unpaid (e.g. 20/05/2026: 3 work / 4 unpaid). Corroborates "managing
almost 60% of my hours."  2025 RTW 7 fns (26 Mar-18 Jun 2025, the against-advice return): avg 29.3%
of full-time — documents the reduced-capacity self-managed return. 26 Mar 2025 lump = unfair-
dismissal payment $29,390.05 (NOT back pay) — keep classified separately for the overpayment recalc.
USE: build the leave-debit/FTE exhibit for the 28 Jul IO meeting + give Zappia the FTE basis for the
recalc. NOTE: still need the LATEST payslip showing the 3 July+ sick-leave debits specifically.

## 2026-07-17 — UPDATE: Cory confirms his GP was NEVER in receipt of the Mind and Memory report
This EXCLUDES the benign "GP-held copy swept up by the Regulator's NNPD to Our Medical Ashmore" path
I posited. Remaining candidate sources for the copy in the Regulator's 22 Jul 2025 disclosure to
Saines (report was addressed to Louise Ings, QSuper):
  (i) QSuper/ART (the ADDRESSEE) — produced under NNPD served on ART, OR released; OR
  (ii) Mind and Memory Service (the AUTHOR) — produced under NNPD served on the psychiatrist; OR
  (iii) already in Cory's/Saines' possession and re-circulated.
KEY: compelled production under an NNPD is LAWFUL, not a breach — likely what QSuper's "we released
nothing" carefully means (voluntary release ≠ compelled production). So this still does NOT establish
a QSuper voluntary breach; it makes the PATH the thing to establish.
THE DECISIVE DOCUMENT: the REGULATOR'S Form 29 / NNPD(s) — the recipient list answers "who produced
this report." Cory's own affidavit ¶44 + Form 24 ¶25: the Regulator obtained his medical records
under a Form 29 NEVER SERVED ON HIM. ACTION: obtain the Regulator's Form 29(s) recipient list (Saines
file / Regulator disclosure index) — that names who was served (GP? psychiatrist? QSuper?).
NET EFFECT: (a) strengthens the grievance against the REGULATOR (unserved Form 29 swept up a QSuper-
purpose report the GP never even held — breadth of over-collection) — the banked WC/reprisal-track
point; (b) justifies a POINTED-BUT-NEUTRAL inquiry to QSuper AND obtaining the Form 29 list; (c) does
NOT yet justify the accusatory complaint. Advice unchanged: establish path first (neutral), keep the
real grievance banked vs the Regulator, don't spotlight the report's "not for medico-legal use" status.
Add to the QSuper neutral inquiry: "Was any Notice of Non-Party Disclosure served on ART/QSuper in
WC/2024/227, and if so what did ART produce and when?"

## 2026-07-17 — "Ask the Regulator to supply their Form 29?" — NOT NOW; use low-signal sources first
Cory asked whether to write to the Regulator for its Form 29/NNPD (the one that obtained his medical
records, never served on him). RECOMMENDATION: do NOT send a standalone request to the Regulator now.
REASONS:
1. **Breaks the deliberate silence during the Calderbank lapse window.** Posture is: let the offer
   lapse 22 Jul in silence, no communication with Matheson. A letter now — even on a different topic
   — gives Matheson a reason to engage and muddies the clean lapse.
2. **Tips the privacy/reprisal hand (rule 8).** A pointed "supply your Form 29" request signals he is
   investigating the medical-records disclosure = building the medical-info-handling / reprisal angle.
   That is the RESERVED track, sequenced BEHIND settlement. Signalling it now could firm the
   Regulator's "post-injury / not relevant" defence (SOFC ¶25) and make them defensive pre-production.
3. **Off critical path + settlement-architecture risk.** Critical path = 64G mention (7 Aug) +
   Krishnaiah report. The medical-info-handling complaint is the very thing he OFFERED TO RELEASE at
   Calderbank 6.2(d); actively pursuing it now complicates the post-production renewal.
4. **Already admitted; no need to prove it happened.** Form 24 ¶25 admits the Regulator obtained his
   records under a Form 29 not served on him (affidavit ¶44). He needs only the RECIPIENT LIST to
   trace THIS report — a narrow need better served by low-signal routes.
LOW-SIGNAL SOURCES FIRST (get these before any Regulator approach):
(a) **His own SAINES FILE** — Paul Conrad forwarded the Regulator disclosure package 22 Jul 2025
    ("Your WorkCover Matter"). The covering material / disclosure index likely names the NNPD(s) and
    recipients. It is HIS file, free, no signal. Request the full file from Saines.
(b) **The QSuper letter item 2(b)** — asks ART directly whether an NNPD was served on QSuper and what
    was produced. If yes → path established (Regulator→NNPD→QSuper→report) without asking the
    Regulator at all.
ONLY IF (a)+(b) inconclusive: a Regulator request later, framed as ROUTINE DISCLOSURE within the
proceeding (not a standalone grievance letter), and timed AFTER the lapse/mention — never as
reprisal-building. Preserve silence + critical-path focus now.

## 2026-07-17 — Medical centre refused Cory's request (for the report/Form 29/disclosure info)
Cory: "my medical centre wont give me it i asked already." So the low-signal medical-provider route is
blocked. NOTE: the medical centre was never the right source for the Form 29 anyway — the REGULATOR
issued it; the medical centre isn't obliged to hand a patient litigation/third-party-disclosure
documents. Do NOT burn energy fighting them (distraction from critical path). REVISED source order:
(1) **Saines file** (his own former-solicitor file — they can't refuse his own file the way the clinic
can; the 22 Jul 2025 package + covering index likely names the NNPD recipients) — SEND Email 1.
(2) **QSuper item 2(b)** (was an NNPD served on ART).
(3) **Regulator disclosure list** (Email 2) — now more likely needed given the clinic refusal;
    send as neutral routine disclosure request, ideally AFTER the 22 Jul lapse. If "it" = his own
    HEALTH RECORDS (not the Form 29), he has a statutory right of access (privacy law; provider may
    charge a fee / take ~30 days; refusal → OAIC/OIC complaint) — but records-access is a side issue,
    not the Form 29 recipient question.

## 2026-07-17 — CORRECTION (Cory, fact): Saines was NEVER served the Regulator's Form 29
Kills the Saines-file route for the recipient list (Email 1 withdrawn for that purpose). Reinforces
the pleaded ¶44/¶25 point AND ENRICHES it: the Regulator obtained his medical records — INCLUDING the
QSuper-addressed psychiatric report the GP never held — via a Form 29 served on NEITHER Cory NOR his
solicitors. That is a significant over-collection, entirely the REGULATOR's conduct → strong material
for the RESERVED privacy/reprisal track (banked; not fired now).
REVISED SOURCE ORDER for "who produced the report":
(1) **QSuper item 2(b)** — was an NNPD served on ART? ART is the report's ADDRESSEE = the single most
    likely source. If ART says "served + produced," path = Regulator→NNPD→QSuper→report. DONE, no
    Regulator letter needed.
(2) **Regulator (Email 2, neutral)** — the authoritative source; now the real fallback since Saines
    and the clinic are both out. Guardrails unchanged: neutral routine-disclosure framing (no report/
    QSuper/privacy mention), ideally AFTER 22 Jul lapse. Not urgent — the recipient list feeds the
    RESERVED track, not the critical path.
No urgency to break silence: nothing on the 64G/report critical path needs the recipient list now.

## 2026-07-28 — CORY'S OWN LETTER SENT to HR (17:39) — "incorrect application of EB12, Award and QH policies"
Saved: documents/2026-07-28_Cory_to_HR_incorrect-application-EB12-Award-policies_SENT.pdf.
To Injury Management + Forrest; **cc Heath Moran (Together) AND Zappia (ART)**. Sent the same day as
the 12pm IO intro call. SUPERSEDES the held record-correction draft — this is the operative letter and
it is materially STRONGER than the held draft in three ways: (1) it is INSTRUMENT-ANCHORED with 8
numbered attachments (EB12 No.12 2025; HHS Award 2015; Psychosocial Code 2022; QH-IMP-401-5;
QH-POL-210; Directive 12/24; QH-POL-231; AO3 role description) and demands response "by reference to
each attachment"; (2) it demands a TASK-BY-TASK match of the role description to the ECC — converting
"we can't facilitate" from a conclusion into an itemised justification they must produce; (3) it
demands the DELEGATE AND INSTRUMENT for each day's coding since 3 July — no anonymous decisions.
STRUCTURAL WINS: special-leave demand under EB12 cl 9.12 + Directive 12/24 + QH-POL-231 (the paid
route, correctly located in the agreement); abandonment protection sought (cl 6.1) — pre-empts the
2024 "abandonment" playbook; workplace psychosocial risk assessment demanded under cl 7.2 + the Code
(REVERSES the inversion — assessment of the WORKPLACE, not of him); decision-maker identification;
5-business-day deadline (lands ~4 Aug, i.e. BEFORE the 7 Aug mention); appeal expressly fenced
("My QIRC appeal WC/2024/227 is separate"); union involvement stated ("taking industrial advice
through Together").
WATCH ITEMS (not fatal, for follow-up): (a) EB12 clause numbers (6.1, 7.1.5, 7.1.11, 7.2, 9.12) must
be VERIFIED against the operative agreement — ask the IO to confirm; a wrong pinpoint is the one thing
that lets them deflect. (b) Point 1 bullet 2 is garbled ("On the material available to me notified by
employee (myself)... ART put benefit payments are not applied from 1 June 2026") — meaning survives
but it is the weakest sentence; if they seize on it, restate simply: benefits ceased at my request /
on hold from 1 June 2026; the fund is not paying me. (c) ZAPPIA CC'd — puts the fund on employment
correspondence (against my earlier advice); consequence: ART now sees the employment dispute and MSH
sees the union. Accepted as his call; do not repeat by default. (d) Tone is firm ("WHAT YOU MUST
APPLY") — fine for the industrial channel with the union cc'd, and it is instrument-based rather than
accusatory.
NEXT: response due ~4 Aug. Non-response is itself the artifact (5 business days, 8 instruments, no
answer). Whatever comes back goes to Heath/the IO same day. Mention 7 Aug unaffected.

## 2026-07-28 — VERIFICATION PASS on the 28 July letter's attachments (partial — one real correction)
VERIFIED ✅
- **Directive 12/24 (Special Leave)** — downloaded in full. Effective 30 Sept 2024, supersedes 05/17.
  **APPLIES to Cory**: cl 4.1(b)(ii) covers Hospital and Health Services employees who are industrial-
  instrument employees. So the instrument is correctly identified and correctly applicable.
  ⚠️ **CORRECTION TO THE LETTER (real, flag to the IO):** the letter says special leave on full pay
  "**must** be applied." Directive 12/24 is **DISCRETIONARY**, not mandatory, for this situation:
  cl 6.1 "A chief executive **may** approve paid leave for employees for **any purpose**" — and
  cl 6.1(a) caps it at 5 working days/yr per reason "unless the chief executive considers that
  circumstances warrant the granting of additional paid leave." Schedule One (non-discretionary,
  "must be granted") lists only election/local-government/defence-type categories — nothing covering
  employer-directed exclusion. THE USABLE HOOK IS cl 6.5: in determining an application under 6.1/6.2
  the CE **must consider** (a) the reason, (b) the duration, (c) [fixed-term only], (d) **the impact
  on the employee if the requested leave is not approved**. So the correct formulation is: "I REQUEST
  special leave on full pay under cl 6.1; in determining it you must consider the cl 6.5 factors,
  including the impact on me of refusal." NOTE: the stronger argument is NOT special leave at all —
  it is that no power has been identified to direct a ready-willing-and-able employee off work
  WITHOUT pay (special leave is the mechanism, not the entitlement).
- **QH-IMP-401-5** (rehab/suitable duties available WITHOUT an accepted claim, where operationally
  reasonable) and **QH-POL-210** (reasonable adjustment) — verified earlier; correctly cited.
- **Psychosocial Code of Practice 2022 (Qld)** + WHS Act ss 47-49 consultation — verified earlier.
NOT VERIFIED ❌ (sites blocked/timed out through the proxy: qirc.qld.gov.au 503/timeout;
careers.health.qld.gov.au 403)
- **EB12 (Certified Agreement No. 12) 2025 clause numbers**: cl 6.1 employment security; 7.1.5 injury
  management; 7.1.11 WHS feedback; 7.2 psychosocial risk assessment; **9.12 special leave → Directive
  12/24**. Existence/effect of EB12 confirmed (certified by QIRC as CB/2025/157, effective 23 Dec
  2025) but the CLAUSE NUMBERING IS UNVERIFIED. ACTION: ask the industrial officer to confirm each
  pinpoint against the operative agreement (she will have it); or obtain the PDF via the Together
  member portal. If a number is wrong, correct it in the follow-up letter BEFORE they use it.
- **HHS General Employees (Queensland Health) Award – State 2015** — not retrieved; ask the IO.
- **QH-POL-231 (Special leave, HR Policy C7)** — not retrieved; ask the IO.
NET: the letter's FRAMEWORK is sound and its two policy pillars (QH-IMP-401-5, QH-POL-210) are
verified. The exposure is (i) the "must be applied" special-leave overstatement and (ii) unverified
EB12 pinpoints — both fixable in the follow-up, both worth raising with the IO first.

## 2026-07-28 — ATTACHMENTS VERIFIED AGAINST SOURCE — EVERY EB12 PINPOINT IS CORRECT
All 8 attachments saved to documents/instruments/. EB12 = the CERTIFIED agreement (QIRC s 193
certification; parties incl. Together Queensland). Clause-by-clause verification of the 28 July letter:
✅ **6.1 Employment Security** — correct (6.1.1-6.1.8; Employment Security Policy applies; no forced
   retrenchment; "no downgrading of positions").
✅ **7.1.5** — correct AND BETTER THAN CITED. Heading: "the parties agree to address the following
   hazards and issues" — the list expressly includes **(b) fatigue risk management; (f) INJURED
   WORKERS TO HAVE THE OPPORTUNITY TO BE RE-TRAINED IN ALTERNATIVE AREAS/DEPARTMENTS; (g) injury
   management; (h) management of ill or injured employees; (j) psychosocial issues and implementation
   of the Managing the risk of psychosocial hazards at work Code of Practice 2022; (k) security for
   administrative staff in frontline positions.** 7.1.5(f) is directly on point for the alternative-
   duties refusal and is the strongest single sub-clause in the letter.
✅ **7.1.11** — correct, verbatim: "The parties commit to ensure that appropriate feedback is provided
   to employees who raise workplace health and safety matters." (Two years of unanswered concerns.)
✅ **7.2 Psychosocial Risk Assessments** — correct. 7.2.1: committed to support workplace audits and
   risk assessments "as requested through a HCF either by an employer OR A UNION PARTY" → the UNION
   can request the assessment (route confirmed). 7.2.2: use the Code 2022; "in consultation with
   workers and HSRs." 7.2.3: audits review adequacy/effectiveness of controls.
✅ **9.12 Special Leave** — correct, verbatim: "The parties agree the Minister for Employment and
   Industrial Relations Directive 12/24: Special Leave applies to all employees covered by this
   Agreement." So the EB12→Directive 12/24 chain is exact.
BONUS CLAUSES NOT CITED (available for the follow-up):
- **7.1.10** fatigue risk management is a health and safety issue, to be managed accordingly.
- **7.3 Workplace Mental Health** — QH commitment to mentally healthy workplaces "through attention to
  safe work design, work systems and practices, and workplace environments."
- **9.23 / 9.24 Paid Meal Breaks for Switch Attendants** (continuous shift workers / sole operators) —
  the agreement expressly contemplates SWITCHBOARD roles.
- Note cl 8.2 excludes 7.1.3-7.1.11 for **FSQ** employees only — irrelevant to an HHS employee.
✅ **ATT10 QH-POL-210** verified from source: "applies to ALL Queensland Health (the department and
   Hospital and Health Services) employees"; expressly covers employees in workplace rehabilitation/
   RTW needing **temporary** reasonable adjustment AND employees with capacity restriction needing
   ongoing adjustment. Nothing limits it to accepted WC claims. Directly refutes the 15 July
   "discretion" paragraph.
✅ **ATT12 Directive 12/24** verified (see prior entry). ⚠️ Only correction stands: it is
   DISCRETIONARY (cl 6.1 "may approve... for any purpose"; 5-day/yr guide) with cl 6.5 mandatory
   CONSIDERATIONS (reason, duration, impact of refusal) — reframe "must be applied" → "I request it;
   you must consider cl 6.5 factors."
⚠️ **ATT09 QH-IMP-401-5** — the PDF is a SCANNED/IMAGE file (no extractable text). Content confirmed
   from the published source earlier (rehab may be provided to employees WITHOUT a current accepted
   claim where operationally reasonable). Fine, but note MSH may claim difficulty; a text copy is
   preferable if re-sent.
NET: the letter's legal scaffolding is SOUND — every pinpoint lands. The single soft point is the
special-leave "must", which is a wording fix, not a structural flaw.

## 2026-07-28 — "Can I make an official complaint?" — YES; four routes; the QHRC GATEWAY RULE; timing
**KEY PROCEDURAL FINDING (verified, QHRC):** the QHRC **cannot deal with a Human Rights Act complaint
until (i) an INTERNAL complaint has been made to the public entity itself, in accordance with that
entity's complaints procedure, AND (ii) 45 BUSINESS DAYS have elapsed** since the internal complaint
(waivable only in exceptional circumstances, and only where an internal complaint was still made).
→ So the internal MSH complaint is the **GATEWAY** to the external human-rights route, and lodging it
starts a ~9-week clock. That is an argument for lodging it reasonably soon — but not before the
28 July letter's own deadline runs.
FOUR ROUTES (ranked by teeth):
1. **QIRC dispute via the certified agreement (UNION)** — the only route with orders/enforcement +
   the status quo lever. THE PRIMARY ROUTE. IO-led.
2. **AD Act / QHRC discrimination complaint** (impairment; failure to adjust; positive duty from
   1 Jul 2025) — independently actionable; work-related complaints can go to QIRC.
3. **Internal MSH complaint** (QH-POL-140 Individual employee grievances, HR Policy E12) — modest
   teeth on its own (⚠️ THE CLOSED LOOP: it returns to the same HR unit — cf. the ESU's Dec 2024
   referral of "administrative issues" to HR L&B, outcome never advised), BUT it is the mandatory
   GATEWAY for route 4 and it creates a dated record.
4. **QHRC human-rights complaint (HRA s 58)** — conciliation only, **no damages (s 59(3))**; strong
   institutional/compliance pressure on a public health service.
RECOMMENDED SEQUENCE (do NOT lodge today):
- **Now → 4 Aug:** let the 28 July letter's 5-business-day deadline run. Lodging a complaint now lets
  MSH answer the COMPLAINT instead of the LETTER, splits the process, and forfeits the cleanest
  artifact (an unanswered instrument-by-instrument demand).
- **~5 Aug (if unresolved/no response):** put it to the IO first — "do we notify a dispute, and do you
  want me to lodge an internal complaint to preserve the QHRC route?" Union route leads; the internal
  complaint is filed alongside it purely to open the gateway and start the 45-business-day clock.
- **Content of the internal complaint (when lodged):** narrow, factual, instrument-based — the same
  spine as the 28 July letter + expressly state it is a complaint under QH-POL-140 AND a human-rights
  complaint under s 58 HRA (identifying equality s 15 and privacy s 25, and the failure to give
  proper consideration under s 58(1)(b)). Naming the HRA expressly is what makes it count as the
  gateway complaint.
- **Do NOT** run all four routes at once (fragments effort, hardens MSH, and the WC settlement is
  sequenced first — rule 8). The QHRC discrimination route stays reserved unless the union route
  stalls or an exit/IME step occurs.

## 2026-07-28 — Oct 2024 abandonment-reply draft filed — THE MEDICAL-EVIDENCE ASYMMETRY (two-year proof)
Saved: documents/2024-10-09_Cory_reply_DRAFT_to_abandonment_letter_Firoz_Johns.pdf.
PROVENANCE: Outlook shows "[Draft] Re: Correspondence from the Executive Director..." — reply to LBH_HR
(Faiza Firoz, HR Consultant) email of **Wed 9 Oct 2024 4:10pm** forwarding the abandonment
correspondence from **Steven Johns, Acting Executive Director, Logan & Beaudesert HS**. Header shows
"Draft saved Tue 28/07/2026 7:45 PM". ✅ **CONFIRMED BY CORY (28 Jul 2026): THIS WAS SENT in October 2024.** (The "draft saved 28/07/2026"
stamp is an artifact of re-opening the item in Outlook, not evidence it was unsent.) EFFECT: the
employer was **ON WRITTEN NOTICE** in Oct 2024 of every matter in it. ACTION: retrieve the SENT-ITEMS
copy (with sent timestamp + recipients) to prove despatch — the draft-stamped export is weaker
evidence than the sent copy. Also check for any MSH reply.
### THE INTEGRATION — "medical evidence counts only when it suits them"
The document proves the ASYMMETRY across two years, same employer, same HR unit:
- **OCT 2024** — medical evidence said INJURED/UNFIT. He held continuous certificates and a **work
  capacity certificate**; WorkCover had given QH an outcome letter acknowledging a personal injury.
  MSH's response: **ignored them and purported to terminate for "ABANDONMENT OF EMPLOYMENT."** His
  words: "I am a protected employee who has provided a work capacity certificate"; QH "acknowledg[ed]
  a 'personal injury' while making no accommodations for me and **disregarding any injury or work
  capacity certificates supplied to Human Resources**"; Taylor had been advised HR would receive
  updates through WorkCover "including a work capacity certificate."
- **JUL 2026** — medical evidence says FIT WITH RESTRICTIONS (the ECC, on their own form, by the
  treating GP). MSH's response: **refuse to act on it and demand further medical information**, with no
  timeframe, excluding him "in any capacity."
→ **Same outcome both times: he is out of the workplace.** When the certificate would keep him
EMPLOYED, it is disregarded; when it would return him to WORK, it is insufficient. Medical evidence
functions in this unit only as a reason to EXCLUDE, never a reason to INCLUDE. That is the
"reasonable management action" defence collapsing into a pattern.
### OTHER VALUE IN THE DOCUMENT
1. **He raised the SAME frameworks in Oct 2024** — "Fair Work Act, Industrial Relations Act, Human
   Rights, and the **EB11 HHS agreement**" — i.e. the 28 Jul 2026 letter is not novel escalation; it is
   the same complaint he has been making for two years. (Note: FWA reference was wrong then as now —
   state system; harmless historically, do not repeat.)
2. **Fatigue pay demand** already made to Taylor/Reece/Stibbard/Amy Mo: "allowing an employee less than
   10 hours between shifts. Chloe allowed me only 7 hours, not including travel time."
3. **Delay pattern documented**: "correspondence twice exceeding a month over the 5 days allowed."
4. **Bereavement leave weaponised**: the abandonment letter counted leave taken when his grandfather
   died — severity/dignity material.
5. **Steven Johns (A/Executive Director) named as the decision-maker** for the 2024 abandonment
   decision; Firoz the HR conduit — the escalation-gradient pattern (senior signs, junior conveys)
   already present in 2024, identical to the Forrest/Harrison set-piece in 2026.
### DISCIPLINE
⚠️ The draft contains "crime and corruption complaint" and "wage theft" language — the collateral
grenade. USE THE DOCUMENT AS A RECORD; never re-send it, never quote those passages into the WC track
or any current correspondence. The usable content is the CERTIFICATES-DISREGARDED evidence.
PLACEMENT: the asymmetry goes to the UNION BRIEF (pattern), the KRISHNAIAH BRIEF (institutional
response as stressor), severity/evidence-in-chief, and — carefully — the s 32(5)(a) reasonableness
argument at hearing. NOT the 64G.

## 2026-07-28 — CONFIRMED SENT (Oct 2024) — what the notice point unlocks
Cory confirms the reply to the abandonment letter WAS SENT in Oct 2024. Consequences:
1. **NOTICE, not just belief.** As at Oct 2024 MSH/HR were told in writing that: he held a WORK
   CAPACITY CERTIFICATE and continuous certificates; WorkCover had issued an outcome letter
   acknowledging a personal injury; HR had been told updates would come via WorkCover; no
   accommodations had been made; the 7-hour break and fatigue pay were unresolved; and he invoked
   the IR Act, HUMAN RIGHTS and the EB11 HHS agreement. They proceeded anyway → REINSTATEMENT
   followed (TD/2024/110), which itself concedes the abandonment decision could not stand.
2. **Kills the "unaware / human error" family of defences for the 2024 conduct** — the same family the
   9C uses in 2026 (¶14 "human error by Ms Taylor"; ¶16 "Ms Reese was unaware"). A decision maintained
   AFTER written notice is not inadvertence.
3. **The 2026 mirror is now evidentially symmetrical:** Oct 2024 — certificates held, disregarded,
   excluded (abandonment); Jul 2026 — certificate held, declared insufficient, excluded (no duties in
   any capacity). Both after written notice invoking the same instruments. The unifying proposition
   for the union brief/hearing: medical evidence in this unit produces exclusion regardless of its
   content — which is the antithesis of "reasonable management action taken reasonably."
4. **Institutional-response severity (Krishnaiah brief):** he wrote that letter while injured, and was
   dismissed anyway; reinstatement came only after he pursued it (TD/2024/110). That sequence —
   raise → ignored → dismissed → had to fight back in → repeated in 2026 — is the "prolonged
   unresolved exposure" mechanism in its most concrete form.
ACTIONS: (a) pull the SENT-ITEMS copy + any reply; (b) add to the union brief as the two-year pattern
exhibit; (c) supply to Krishnaiah in the report pack; (d) 9C cross-reference — the 2024 notice
undercuts the unawareness/error framing. DISCIPLINE UNCHANGED: never re-send/quote the "crime and
corruption"/"wage theft" passages; the usable content is certificates-disregarded + notice.

## 2026-07-28 — THE REGISTER SHIFT: 13 July email vs 28 July letter (side by side)
Docs 141/142 confirm the pair. THE SHIFT IS THE POINT — it is legible and deliberate.
**13 JULY (16:39)** — To: LBH Injury Management ONLY. Cc: Notes-IPEC (Solv) only.
Register: SUPPLICANT-COOPERATIVE. "Thank you for your email." "could you please confirm."
"I would welcome a discussion about how my experience can be used to the benefit of the Service."
Consent volunteered ("My consent... stands"). Offers to work in finance/scanning. No instruments
cited, no deadline, no decision-maker named. Four requests, all phrased as asks.
**28 JULY (17:39)** — To: LBH Injury Management AND **Lyndelle Forrest (Senior HR Consultant)**.
Cc: **Heath Moran (Together)** AND **James Zappia (ART)**.
Register: INSTRUMENT-COMPLIANCE. 8 attachments, clause pinpoints, "Wrong application", "WHAT YOU
MUST APPLY", 8 numbered requests, **5-business-day deadline**, delegate-and-instrument demand.
WHAT THE SHIFT ACHIEVES (the three signals):
1. **ESCALATION IN ADDRESSEE** — adding Forrest to the To line moves it above the case officer. It
   says: the person who has been answering can no longer answer this.
2. **WITNESS IN THE CC** — Heath = the correspondence is now observed by an institution with
   standing and its own escalation path. Informal handling is over; anything written now is written
   for a third party.
3. **THE COOPERATION RECORD IS COMPLETE** — 13 July is the exhibit that proves he asked politely
   first, offered alternative duties, volunteered consent, and thanked them. 28 July is only
   reasonable BECAUSE 13 July exists. The pair reads as escalation-after-exhaustion, not aggression.
   (Standing rule: restraint first makes firmness grantable — the same logic as the 64G concessions.)
ZAPPIA CC — noted again as his call, against my advice: puts the fund on employment correspondence.
Defensible rationale (the closed-claim premise is visible to both at once) but do not repeat by default.
RECIPIENT'S-EYE READ (for the file): the 13 July email could be managed by one consultant with a
holding line. The 28 July letter cannot be answered by that person, in that tone, or within that
timeframe — it requires (a) someone senior, (b) work product that does not exist, (c) a named
delegate, and (d) awareness that a union is reading. The recipient's first thought is not "what do
we say" but "who has to deal with this now" — which is exactly the intended effect.

## 2026-07-28 — SOURCE VERIFICATION of the clarification email — one issue found (QH-POL-231)
✅ **Directive 12/24 cl 6.1** — "A chief executive **may** approve paid leave for employees for any
   purpose" — discretion CONFIRMED verbatim.
✅ **Directive 12/24 cl 6.5** — verbatim: "In determining an application for leave under clause 6.1 or
   clause 6.2, a chief executive **must consider**: (a) the reason the leave is requested; (b) the
   duration of the requested leave; (c) [fixed term temporary only]; (d) **the impact on the employee
   if the requested leave is not approved.**" — the email's characterisation is EXACT.
✅ **Directive 12/24 cl 4.1(b)(ii)** — applies to Hospital and Health Services employees. Applies to Cory.
✅ **EB12 cl 9.12.1** — verbatim: "The parties agree the Minister for Employment and Industrial
   Relations Directive 12/24: Special Leave applies to all employees covered by this Agreement."
✅ **QSuper/ART hold** — Beck letter 28 May 2026 verbatim: "ART Life has also advised that your IP
   benefit payments **will be placed on hold effective 1 June 2026**, while this information is
   obtained and the recalculation is completed." Attribution correct (ART's decision, NOT his request).
✅ **March 2026 cessation at his request** — sourced to the QSuper bundle (13 Mar 2026 self-reported
   RTW + request to stop payments). Sound, though it rests on the March correspondence rather than the
   Beck letter; ART's written confirmation (Zappia letter) would put it beyond argument.
⚠️ **QH-POL-231 (ATT13) — ISSUE FOUND.** The attached version repeatedly references the SUPERSEDED
   **PSC Directive 05/17 – Special Leave** (Directive 12/24 expressly "Supersedes: 05/17"). Its History
   note refers to revisions effective 1 March 2017. TWO consequences:
   (a) The version he attached appears OUT OF DATE — MSH could say ATT13 is superseded.
   (b) More importantly, QH-POL-231's structure is a list of SPECIFIC categories (blood donation,
       cultural leave, emergency attendance, elections, reserve forces, sporting competitions, leave
       without pay in other cases, etc.). It contains **no general discretionary paid-leave provision**
       equivalent to Directive 12/24 cl 6.1, and **no category covering employer-directed exclusion.**
   → SO: QH-POL-231 adds NOTHING to the argument and carries a small currency risk. The operative
   instruments are EB12 cl 9.12 + Directive 12/24 cl 6.1/6.5. RECOMMENDATION: it is already in the
   28 July attachment list (harmless); do NOT lean on it in the clarification email — either drop the
   QH-POL-231 reference from the clarification, or keep it only as a trailing "and QH-POL-231" without
   argument attached. If MSH points out it references 05/17, the answer is simply that Directive 12/24
   supersedes 05/17 and applies via EB12 cl 9.12 — no damage done.
NET: every load-bearing proposition in the clarification email is verified from source. The only
adjustment is to not rest any weight on QH-POL-231.

## 2026-07-29 16:10 — MSH REPLY to the 28 July letter (Harrison) — movement on ONE item, silence on eight
Saved: documents/2026-07-29_Harrison_reply_EAF_WHS-basis.pdf. To Cory + Forrest, cc Heath + Zappia.
**SPEED: <24 hours** — after 11+ days of prior silence. The letter produced immediate movement. Note
the 5-business-day period does NOT expire until ~4 Aug, so this may be interim, not their full answer.
WHAT THEY DID:
1. **The RFI mechanism FINALLY appears** — 26 days after the ECC. Attached an **Employee Authority
   Form (EAF)** and offered a CHOICE: (a) Cory takes their request to Dr Ma himself, or (b) he signs
   the EAF authorising IM to write directly, **with Cory copied into the correspondence**. Predicted
   exactly ("watch for the RFI to suddenly appear this week") — and it appeared the day after the letter.
2. **NEW LEGAL BASIS — the WHS Act.** "This request is consistent with Metro South Health's
   obligations under the Work Health and Safety Act 2011 (Qld)... Queensland Health has an
   INDEPENDENT OBLIGATION to assess the medical information provided alongside the INHERENT
   REQUIREMENTS OF THE ROLE." This is their **strongest argument to date** and it is orthodox: an
   employer is not bound to accept a treating GP's certificate at face value and has its own duty.
   Do NOT dismiss it. The vulnerability is not the principle but its APPLICATION — the duty is to
   assess, and no assessment (task match, risk assessment, consultation) has been done in 26 days.
3. **"INHERENT REQUIREMENTS OF THE ROLE"** — NEW language, and a WATCH ITEM. That is the phrase used
   in incapacity/ill-health and reasonable-adjustment analysis. Consistent with (not proof of) the
   health-management frame. Flag to the union.
WHAT THEY DID NOT DO — none of the eight requests answered:
no task-by-task match; no delegate identified; no instrument for the direction; no consideration of
EB12 9.12/Directive 12/24 (the clarification email's question, unanswered); no pay answer; no leave
re-crediting; no abandonment confirmation; no psychosocial risk assessment; **STILL NO TIMEFRAME.**
IMMEDIATE ACTIONS (time-critical — respond within 1-2 days so delay cannot be attributed to Cory):
(a) **READ THE EAF BEFORE SIGNING** — scope is everything. If it authorises open-ended access to
    medical records, do not sign as-is; qualify it or decline in favour of option (a).
(b) **ASK FOR THE QUESTIONS FIRST** — request a copy of the proposed request/questions before
    electing, so scope can be checked against "capacity, restrictions, operational application."
(c) **PREFER the option that keeps the delay THEIRS** (they write directly, Cory copied) — provided
    the EAF scope is confined. Taking it himself transfers the delay risk to him.
(d) **Send to Heath/the IO TODAY** — this is exactly what the industrial officer needs before the
    28 July consult follow-up; the WHS-basis argument is the one they must answer.
(e) Do NOT let this displace the outstanding eight requests — respond on the EAF AND note the
    5-business-day items remain outstanding.

## 2026-07-30 — FINAL response letter to HR built (PDF, scrubbed) + two new verified citations
Files: drafts/2026-07-30_HR_response_FINAL_letter.txt (source);
drafts/out/Shepherd_response_30July2026_MSH-INJ-5795.pdf (4pp A4, no Info dict, no XMP, 9,539 bytes).
NEW VERIFIED CITATIONS (from the source PDFs):
- **EB12 cl 10.3 Flexible Working Arrangements** — employee may request a change in the way they work
  "including the employee's ordinary hours of work"; employer may refuse "only on reasonable grounds";
  **must give written notice of the decision, with reasons, within 21 DAYS.** (Day 27 and counting with
  no written decision and no reasons — a live obligation, not just an analogy.)
- **HHS General Employees Award 2015 cl 8.2 Part-time employment** — regular ordinary hours up to 64
  per fortnight, pro rata conditions, **minimum 8 ordinary hours per fortnight**, min 4-hour payment on
  any day worked. Reduced hours are expressly contemplated by the industrial instruments.
THE DECISIVE NEW SECTION (§4 THE RESTRICTIONS AND THE DUTIES) — built from the AO3 role description
(ATT14) read for the first time: the role's listed key responsibilities are telephone enquiries/call
queues; Omnivista + SharePoint; pager allocation/coordination/fault repair; emergency response process;
networks and records; discretion/judgement; interaction with public/service providers; multitasking
under pressure; team contribution; limited supervision; fair treatment; safety policies.
**COMPLAINT-HANDLING IS NOT A LISTED RESPONSIBILITY** — so the ECC's central restriction excludes a
duty the role description does not require. The remaining restrictions go to WHEN he works, not WHICH
duties. Counterweight (flagged honestly in the letter): the RD twice states the role is continuous
24/7 shift work — their best ground — answered by 12 months of practice + the 7 July accommodation
acknowledgment.
MC: adding the task map + 24/7 pre-emption + meeting offer lifted the letter from rank 28/32 (0.616)
to rank 1/32 (0.846), +0.230 — the largest single improvement modelled this session. Confirmed: do NOT
expand with further instruments (-0.021); PDF slightly worse than email body for speed (-0.026) but
acceptable at this length.

## 2026-07-30 — GP INVOICE + who pays for employer-required medical information (researched)
INVOICE FILED: documents/evidence/2026-07-03_Invoice574370_DrMa_ECC_150.pdf — My Doctors Clinic
Surfers, Dr Day Hong Ma, **Invoice 574370, dated 3 JULY 2026 (the ECC date), item "WCO002 Case
Conference", $150.00, no GST, "Total outstanding: 150.00", payable within 30 days.** Account to Cory.
The invoice date matches the day the ECC was provided — directly attributable to the employer-required
capability assessment.
POLICY RESEARCH (Independent medical examinations guideline, Qld public sector, downloaded — saved as
ATT18). The guideline establishes the QLD public-sector principle that **COST FOLLOWS WHO REQUIRES THE
INFORMATION**:
- where the entity directs the examination, the written direction should state "**that the entity will
  meet all reasonable costs of the employee attending the appointment**";
- where a report is released via a nominated doctor, the chief executive must "**pay the reasonable
  costs of the employee's visit to their nominated doctor to discuss the contents of the report**";
- BY CONTRAST, where the EMPLOYEE volunteers additional material in response to proposed action,
  "**Employees who seek such additional advice are to meet the associated costs**."
APPLIED: the ECC was **employer-required** (Taylor, 2 Jul: cannot facilitate return until a completed
ECC), not employee-volunteered. On the guideline's own principle the cost sits with MSH. CAUTION: the
guideline governs IMEs specifically, not treating-practitioner reports — so cite the PRINCIPLE by
analogy, do NOT assert it as a binding clause.
AD ACT VERIFIED (ATT16, current as at 19 May 2025): s 5 (meaning of unjustifiable hardship — cost,
financial circumstances, disruption, benefit/detriment); **s 34 (special terms if job capacity is
restricted by impairment — a person may fix REASONABLE TERMS where a person has restricted capacity or
requires special conditions)**; s 35 (special services/facilities — exemption only where unjustifiable
hardship); s 36 (circumstances of impairment). NOTE FOR ACCURACY: the Qld AD Act does not use the
phrase "reasonable adjustments" — the operative concepts are **reasonable terms (s 34)** and **special
services or facilities (s 35)**, with unjustifiable hardship as the employer's exemption, assessed
against s 5. The letter's wording should be adjusted accordingly.
Also saved: ATT17 WHS Act 2011 (Qld) full text.

## 2026-07-30 — THE TRIGGER IDENTIFIED (Cory): the ECC was demanded in response to HIS OWN request to
## temporarily reduce hours from 0.6 to 0.5 FTE for TWO WEEKS
This answers "what justified the ECC" and recasts the whole July sequence.
SEQUENCE AS NOW UNDERSTOOD: Cory requests a TEMPORARY reduction 0.6 -> 0.5 FTE for 2 weeks (~7.6 hrs
per fortnight less) -> Taylor (2 Jul) responds that she cannot facilitate his return until a completed
ECC, shifts to be processed as sick leave / sick leave no pay -> Cory provides ECC 3 Jul (fit with
restrictions) -> excluded entirely from 3 Jul, 27+ days and counting.
TWO CONSEQUENCES:
1. **PROPORTIONALITY (needs no clause).** He asked to work ~0.1 FTE less for two weeks. The response
   was 0 FTE, indefinitely. The measure imposed is vastly more restrictive than the request that
   prompted it - and it was imposed on a worker who was working, certified, and had raised nothing.
2. **EB12 cl 10.3 IS SQUARELY ENGAGED (verified text).** 10.3.2: an employee "may ask the employer for
   a change in the way the employee works, INCLUDING THE EMPLOYEE'S ORDINARY HOURS OF WORK."
   10.3.4: the employer may grant, grant in part, grant subject to conditions, or refuse.
   10.3.5: may grant in part/subject to conditions/refuse "ONLY ON REASONABLE GROUNDS."
   10.3.6: "The employer MUST give the employee WRITTEN NOTICE about its decision WITHIN 21 DAYS after
   receiving the request", and if granted in part/conditionally/refused the notice "must state the
   REASONS for the decision, outlining the reasonable grounds."
   -> If the request was made on/about 1-2 July, the 21-day period expired ~22-23 July. As at 30 July
   there is NO written decision and NO reasons. On the face of it that is a breach of a certified
   agreement clause, dated and verifiable.
   -> Requiring a full capability assessment, and then excluding him from all work, as the response to
   a 2-week 0.1 FTE request, is at least arguably not "reasonable grounds" within 10.3.5.
3. **It destroys the risk narrative's origin.** The ECC requirement did NOT arise from any incident,
   observation, complaint or performance concern. It arose from the employee asking to work slightly
   less, temporarily. Every "psychosocial hazard / safety / inherent requirements" formulation post-
   dates it (13, 15, 29 Jul) and was therefore constructed AFTER the requirement, not as its basis.
VERIFICATION NEEDED FROM CORY BEFORE ASSERTING cl 10.3 (do not put in the letter until confirmed):
(a) the DATE the request was made; (b) whether it was IN WRITING (10.3.3(a)); (c) whether it STATED
THE CHANGE in sufficient detail (10.3.3(b)); (d) whether it STATED REASONS (10.3.3(c)); (e) to whom it
was made (Taylor?); (f) whether any written decision has ever been received.
If (a)-(d) are satisfied, this becomes the strongest single point in the employment matter and the
lead item for the union dispute notification.

## 2026-07-30 14:33 — HARRISON HOLDING REPLY (doc 147) + the FULL 7 July Forrest letter (doc 149)
FILED: 2026-07-30_Harrison_holding_reply_RFMI_delegate_approval.pdf;
2026-07-07_Forrest_ECC_further_information_FULL.pdf (full text now in hand).
### TODAY'S REPLY (30 Jul 14:33, ~3.5 hrs after his email): pure holding line.
1. RFMI "progressing for DELEGATE APPROVAL... unable to guarantee when the approved documentation
   will be available" → NO questions before the 2pm Friday appointment; deadline will NOT be met.
2. **FIRST ADMISSION THAT A DELEGATE EXISTS** — still unnamed. Also implicitly concedes the questions
   do not yet exist in approved form, 27 days after the exclusion.
3. "Usual process: approved RFMI sent DIRECTLY TO THE EMPLOYEE, who arranges the appointment" —
   accepts his self-carry election; and NOTE: by their own usual process the EAF was never needed.
4. **AUDIENCE NARROWED**: reply To Cory, Cc Solv only — Forrest, Heath, Zappia all dropped. (He keeps
   the full cc list in HIS sends regardless.)
5. ADDRESSES NONE of: the forms, costs/reimbursement, sequence, origin/10.3, COI, pay, roster,
   decision-maker. Zero of the asks.
### THE FULL 7 JULY FORREST LETTER — three significant new items:
A. **DECISION-BEFORE-REVIEW IN THEIR OWN WORDS**: "As the completed ECC was received late on Friday,
   3 July 2026, the Health Service was unable to review Dr Hong Ma's medical recommendations at that
   time" — yet the hold-out was imposed ~3:30pm THAT DAY. Their own letter confirms the exclusion
   preceded any review. Also: "you have been certified fit to return to work effective from 3 July
   2026" — CERTIFIED FIT ACKNOWLEDGED IN WRITING.
B. **THEY ASKED HIM FOR THE 13 FEB 2025 PSYCHIATRIST REPORT** (Dr Ma referenced it in the ECC):
   "the Health Service has not been provided with, nor had the opportunity to review, this report."
   ⚠️ This is the Mind & Memory/QSuper report marked "not for medico-legal use" — the same report
   that surfaced in the Regulator's NNPD package. (i) DO NOT PROVIDE IT — condition-level scope,
   QSuper purpose, appeal medical evidence; consent stands confined to capacity/restrictions.
   (ii) MSH stating it has NEVER seen it = more evidence the NNPD copy came from ART/psychiatrist,
   not MSH; useful for the privacy trail. (iii) Their request confirms the inquiry reaches diagnosis/
   history, past the restrictions.
C. **ECC CONTENT NOW VISIBLE (via their table)**: ECC records MDD w/ anxious distress, work-related,
   onset 18 Jun 2024, symptoms exacerbated by identified workplace stressors: complaint handling;
   being held accountable/blamed for failures of others; unpredictable rostering. Their responses:
   - Complaint handling: "no expectation for Switchboard operators to manage or deal with these
     matters" (redirect to CLS/Manager) → THEY EFFECTIVELY CONCEDE complaint-handling is NOT an
     inherent requirement — which UNDERMINES any incompatibility case on that restriction AND
     contradicts the lived practice sworn in the Form 20 (¶¶19-22: complaints came to him and fell
     to him when the manager was unavailable). Their "process" description vs his sworn reality =
     the work-as-imagined vs work-as-done gap; for the union/hearing, not correspondence.
   - Rostering: "not aware of breaching this provision"; rosters 4-week rotation, min 2 weeks'
     notice; **REPEATS THE 8-HOUR AGREEMENT ADMISSION**: signed 17 Jun 2020, "this is only applied
     where staff initiated shift swaps have occurred" — the BANKED Form 24-contradicting admission
     now made TWICE in writing.
   - Accountable/blamed: "not aware of any concerns being raised" — against the 2023-24 record
     (grievance, comm book, PID, Form 24 admissions) this is the "no concerns" problem again.
D. Their closing: "Until this information is available and has been appropriately assessed, the
   Health Service is not in a position to safely facilitate your return to NORMAL duties" — note
   "normal duties" (not "any capacity") in the 7 Jul letter; the "any capacity" hardening came later.
### NET POSITION FOR TOMORROW: attend 2pm as planned; Dr Ma addresses capacity vs the 12 duties;
forward the response. The record now shows: deadline set against a booked appointment → answered
with "cannot guarantee"; delegate admitted but unnamed; questions non-existent in approved form.
4 AUGUST remains the union trigger day.

## 2026-07-31 — VALUATION MEMO (calibrated ranges, NOT advice; all contingent on the updated
## psychiatric report, DPI/election thresholds, offsets and specialist PI advice)
Benchmark verified: **Robinson v State of Queensland [2017] QSC 165 — $1,468,991 + costs** (Qld
Health, nurse/District Director, psychiatric injury from managerial mistreatment; career loss).
Inputs: age ~35; FTE gross incl. penalties est. ~$95-110k (hourly ~$43.17 base + heavy loadings);
current certified capacity 0.5-0.6 FTE; injury MDD w/ anxious distress, onset 18 Jun 2024.
- **T1 WC statutory (appeal won):** weekly comp back-pay net of earnings/ART offsets ~$25-70k;
  medicals/rehab ~$10-30k; s 558 costs (scale + possible 1.5x uplift) ~$20-50k. **~$55-150k.**
- **T2 Common law negligence (gateway = accepted claim):** past econ ~$40-90k; future econ (40-50%
  differential ~$32-38k net/yr, 5% tables ~32 yrs, less 15-20% vicissitudes) ~$430-520k; super
  ~$55-70k; general damages ISV serious-psych band ~$30-60k. Gross claim ~$600-800k mid; Robinson-
  style ceiling >$1M if career loss made out. **Realistic settlement band $300-650k** (less WorkCover
  refund, litigation risk). Everything turns on the report's prognosis.
- **T3 PID reprisal tort:** compensatory overlaps T2; exemplary damages the distinct head
  (~$20-100k if run). Function = deed leverage more than expected judgment. **$50-250k leverage value.**
- **T4 AD Act (lockout/impairment):** Qld trend rising (Golding v Sippel ICQ ~$158k high-water);
  impairment/adjustment matters typically **$30-100k** incl. hurt + wage overlap.
- **T5 GP lockout:** wages ~$6-8k+ accruing; general ~$10-30k; penalties possible; if ripens to
  dismissal → uncapped + reinstatement. **$15-45k standalone, uncapped on dismissal.**
- **Patient-safety dimension:** not a damages head — an AGGRAVATOR (institutional-response evidence,
  exemplary-damages support in T3, settlement optics).
- **No double recovery:** T2/T3 overlap on the injury; lockout loss (fit period) cleanly separate.
- **GLOBAL DEED VIEW:** statutory floor ~$150-250k (T1 + modest deed) vs properly-run global
  post-acceptance with strong report **~$350-750k+ plus statutory**, releases confined per rule 9.
Discipline: ranges are planning tools; the Krishnaiah report is the single biggest value lever;
election (lump sum vs common law) is irreversible and specialist-only.

## 2026-07-31 — THE SECOND-CLAIM TRAP (Cory's read: they want to push him into a NEW claim they can accept)
Mechanics check out. If a fresh 2026 psych claim were lodged and ACCEPTED:
1. **Pay problem solved — for them.** WorkCover pays, not MSH; the unlawful unpaid exclusion is
   retrospectively sanitised into "absence on a compensable injury." The lockout record loses its teeth.
2. **Keystone reversed.** "Certified fit and refused work" becomes "incapacitated on a claim" — the
   status quo argument dies; the incapacity file they've been building gets its foundation document,
   signed by HIM.
3. **Causation fragmented.** A new 2026 injury lets them attribute current and future loss to the NEW
   injury — muddying the 2024 appeal's damages tail and the common-law claim (which injury caused the
   32-year loss?).
4. **Scrutiny foreclosed.** Accepted claims are never adjudicated: no hearing, no findings on the July
   conduct, no RMA test it would fail. GP/AD claims weaken practically ("already compensated").
5. **Lawful structure gifted retroactively.** An accepted claim makes them the rehab employer with a
   statutory RTW framework — converting the powerless exclusion into a lawful managed absence.
TELL: the EAF extended to "authorised WorkCover Queensland representatives" — consent to exchange
info with WorkCover, for an employee with NO accepted claim. Consistent with (not proof of) a file
being shaped toward a claimable event.
COUNTER-DOCTRINE (if incapacity ever genuinely occurs and a claim becomes necessary):
**plead AGGRAVATION OF THE EXISTING 18 JUNE 2024 INJURY, never a fresh discrete 2026 injury** —
same injury continuum, exacerbated by the July conduct. Keeps causation unified with the appeal and
the common-law claim; defeats the fragmentation play; the July conduct becomes aggravation evidence
inside the existing matter rather than a separate acceptable parcel. Krishnaiah/Ma documentation to
frame the July period accordingly (aggravating stressor on the existing injury).
RULE: no claim is lodged on THEIR timetable. Only he can lodge; the push only works if he moves.

## 2026-07-31 — NEW FACT (Cory): the 2024 abandonment sequence — Coccetti initiated, Johns signed
Per Cory (⚠️ verify against the LTR_Abandonment_ShowCause document in the filed bundle):
**Anne Coccetti** wrote the FIRST letter — the show-cause asking him to give cause why he had not
abandoned his employment. **He responded stating his intention to return to work** (while holding
continuous medical certificates). The termination for abandonment then proceeded anyway — signed by
**Steven Johns as ACTING Executive Director** (confirmed: Firoz email 9 Oct 2024 conveys
"correspondence from Mr Steven Johns, Acting Executive Director"). Reinstated via TD/2024/110.
SIGNIFICANCE:
1. **The show-cause was answered and disregarded.** Abandonment requires an inference of intention
   to abandon; a written statement of intention to return + continuous certificates directly negates
   the element. Terminating anyway = the process was run as a formality over its own answer — which
   is why it could not survive and was reversed.
2. **Coccetti is NOW the substantive ED of LBHS** — the office that initiated the 2024 exclusion
   event heads the facility running the 2026 one. Continuity of decision-makers across both events;
   "unaware at the top" is unavailable — the ED's office carries institutional memory of having run
   this play once and LOST (reinstatement).
3. **The authorship-diffusion pattern repeats**: 2024 — senior initiates (Coccetti), stand-in signs
   the consequential act (Johns, acting). 2026 — line manager initiates (Taylor), junior runs it
   (Harrison), delegate unnamed. Consequential documents consistently signed by acting/junior
   figures; initiators consistently absent from the operative signature.
4. **Section 7.4 reach**: the 2024 termination is pleaded (9A Part F; affidavit ¶43) — if the 2026
   delegate chain runs to the ED's office, the "person without involvement in those proceedings"
   request arguably catches Coccetti's office too.
5. Feeds: union brief (the two-exclusion pattern, same office); GP/reprisal reserve (top-level
   knowledge + repetition = reasons harder to disprove); Krishnaiah brief (2024 as aggravation,
   already pleaded).
ACTION: verify Coccetti's authorship from the show-cause letter in the bundle before any use.

## 2026-07-31/08-01 — MATHESON SILENCE: the 24 July disclosure-list request is UNANSWERED
FILED: documents/2026-07-24_Cory_to_Matheson_disclosure_list_request.pdf
**SENT: Friday 24 July 2026, 19:08** — to Matheson only. Text (verbatim): "(1) an up-to-date list of
the documents disclosed by the Respondent in the proceeding; and (2) copies of the form 29 Notice of
Non-Party Disclosure issued by the Respondent, together with the documents produced in response to
each."
STATUS: **no response. 7 calendar days / 5 business days as at 31 July.** Mention is 7 August.
### WHY THIS REQUEST IS NOT ROUTINE FOR THEM (though it reads as routine)
Limb (2) is the pin. The Regulator's own Form 29 is the notice that obtained Cory's MEDICAL RECORDS
**and was never served on him** — admitted, Form 24 ¶25; sworn, affidavit ¶44. Producing it would
disclose, in one document: (a) WHO was served (GP? psychiatrist? ART/QSuper?) — the answer to how the
Mind & Memory report (marked "not for medico-legal use", never held by his GP) reached the 22 Jul 2025
Saines package; (b) WHAT was produced; (c) that Cory was NOT among the served parties — documenting
the r 64C(4) affected-party failure in the Regulator's own paperwork.
Limb (1) is also live: an "up-to-date list" is testable against what he actually holds; any gap =
ongoing-disclosure problem two weeks before a mention.
### READINGS (ranked)
1. **Referred up / to counsel (most likely, ~45%).** Willson is briefed for 7 Aug; with a mention
   pending, a request touching the Respondent's own NNPD conduct would not be answered by an appeals
   officer unilaterally. Consistent with the 15-day Calderbank authorisation loop — this office
   escalates anything with consequences.
2. **Answer is uncomfortable / being curated (~30%).** The list/notice documents the non-service and
   the medical-records route. Producing it hands Cory the privacy trail; refusing it is worse. Delay
   is the least-bad interim.
3. **Ordinary administrative lag / leave (~20%).** Friday-evening receipt; possible.
4. **Deliberate stonewall (~5%).** Unlikely — the Regulator has an overriding duty to the Commission
   and has shown it (11 June MSH-adverse disclosure). Stonewalling a disclosure request pre-mention
   would be out of character and risky.
### COMPARATIVE LATENCY — the two respondents now behave IDENTICALLY
- MSH: answers fast, says nothing (30 Jul: 3.5 hrs, zero substance).
- Regulator: says nothing at all (7 days, no acknowledgment).
Both have converged on the same posture: **no new positions on paper before 7 August.** That is a
litigation-management signal, not indifference.
### SIGNIFICANCE FOR 7 AUGUST
Non-production of the disclosure list before the mention is itself a modest procedural point Cory
holds in reserve — NOT to be raised as grievance, but available if the Commissioner asks about the
state of disclosure. It also means the Form 29 recipient list may only surface via order or at the
mention — i.e. the privacy-trail question stays open until the disclosure question is dealt with.
### ACTION
NO chase before the mention. A second email would (a) convert a clean unanswered request into a
back-and-forth, (b) signal the privacy interest, and (c) spend a point better made by the record.
The 24 July email stands as a dated, unanswered, entirely reasonable request. If disclosure is
canvassed on 7 Aug and it is proper to do so, the fact of the request can be mentioned neutrally.

## 2026-08-01 — THE ORIGIN DOCUMENT OBTAINED: Taylor, 2 July 2026, 14:38 ("Cory - ECC/Leave Type")
FILED: documents/2026-07-02_Taylor_ECC_LeaveType_ORIGIN_DOCUMENT.pdf
From Chloe Taylor (Switchboard Manager) to Cory's WORK address, cc his personal address. VERBATIM
KEY PASSAGES:
- "I know you had a scheduled appointment with your doctor yesterday as per text message sent on
  Monday 29th July" [NOTE: "29th July" is an ERROR in their email — chronologically must be 29 June.
  Their date error, on their document.]
- **"Until we receive appropriate medical clearance, including a completed Employee Capacity
  Certificate (ECC), we are unable to facilitate your return to work, please wait for my advice to
  when your next returning shift will be."**
- **"Unless you advise me otherwise, I will process your shifts that you have not worked as Sick
  Leave – Please confirm by Friday 3rd July before 2:00pm."**
WHAT THIS ESTABLISHES:
1. **THE CONDITION, IN WRITING, FROM TAYLOR** — return conditional on a completed ECC. The single
   clearest articulation of the gate. Taylor as author = the conflict-of-interest point (s 7) is
   anchored to a primary document, not inference.
2. **THE SICK-LEAVE CODING WAS A DEFAULT, NOT A DECISION** — "Unless you advise me otherwise, I
   will process..." Leave was debited by default, with no delegate, no instrument, and the onus of
   objection placed on the employee. Directly supports the "no decision was made" thesis.
3. **"please wait for my advice to when your next returning shift will be"** — express assertion of
   control over his attendance by the line manager, 2 July, before any IM involvement.
4. ⚠️ **SEQUENCE POINT NEEDING CLARIFICATION FROM CORY**: "your shifts that you have not worked"
   indicates shifts were ALREADY unworked as at 2 July, and "unable to facilitate your RETURN"
   implies he was already off. So the stoppage may PREDATE 2 July. His letters have said "I was
   working my rostered shifts... then told I could not work until I completed an ECC."
   → CONFIRM: what was the LAST shift actually worked, and what happened between the hours request
   and 2 July? The sequence paragraph in future correspondence must match this document exactly.
   (Safest current wording: "I was told on 2 July 2026 that I could not return to work until a
   completed ECC was provided.")
5. Their deadline was "before 2:00pm Friday 3 July"; the ECC was provided 3 July at 2:32pm — 32
   minutes later. Immaterial (he complied the same day, and the ECC required the doctor's completion)
   but note it: they may reach for it. Answer: the document was obtained and provided the same day.
USE: origin document for the union bundle and the statutory declaration; anchors s 4 (origin of the
requirement) and s 7 (conflict) in his correspondence. NOT to be re-argued with MSH.

## 31 JUL 2026 — CALDERBANK #2 (1 JULY) WAS ALSO SERVED ON THE OIR APPEALS REGISTRY

Cory advises the 1 July 2026 Calderbank offer was sent not only to Renee Matheson but also to the
OIR appeals registry mailbox (believed Appeals@oir.qld.gov.au).

**VERIFY FROM SENT ITEMS (do this first):**
- [ ] Exact addressee list, date and TIMESTAMP of the 1 July email — transcribe verbatim into the
      chronology.
- [ ] Confirm it did NOT go to QIRC registry. A without-prejudice document must not reach the
      decision-maker's file. (Expected: OIR mailbox only — OIR is the respondent's own agency, so
      service there is orthodox and correct.)
- [ ] Preserve the sent item + any delivery/read receipts. Export to PDF into evidence/.

**WHAT IT CHANGES:**
1. **Knowledge is institutional, not personal.** Earlier working assumption (that Matheson alone
   holds the 1 July knowledge) is superseded. The offer was registered in a shared government
   mailbox and seen by whoever staffs it. If the 1–2 July sequence ever has to be reconstructed,
   it is reconstructed from an auditable agency file, not one person's memory.
2. **Receipt is provable → the Calderbank is materially stronger for s 558(3) / *Canton*.** The
   usual weak point (was the offer communicated and considered?) is closed. "Not seen by the right
   person / not escalated" is no longer available, and if raised becomes an admission about the
   Regulator's own file handling.
3. **The 1 July date is a government record** — discoverable via the appeal's disclosure obligations
   or, if ever needed, RTI. No longer dependent on Cory's own sent item.
4. ⚠️ **DO NOT over-read dissemination.** The Regulator and MSH are separate entities; MSH is not
   the respondent. The one KNOWN channel is MSH Legal (Myla Ruttan, Principal Lawyer, named contact
   on the 5 June 2026 Form 29 objection under Cridland's signature). A channel existing establishes
   nothing about whether anything travelled down it on 1 July. Do not convert the existence of a
   pipe into an assumption about its contents.

**DISCIPLINE UNCHANGED:** the 1 July / 2 July juxtaposition is never asserted by Cory in any
correspondence — not to Matheson, not to MSH, not to the Commission. It is recorded as a dated
factual sequence (now with recipients and timestamps) in (a) the statutory declaration / chronology
for the union and (b) the reserved general protections file. The registry service makes the facts
MORE provable, which is exactly why there is no need to assert anything from them yet.

**CONSISTENCY POINT:** apply the same service practice going forward — where an item is intended to
bind the Regulator as respondent (offers, notices), copy the OIR appeals mailbox as well as the
individual officer, so receipt is always provable.

## 31 JUL 2026 — SERVICE OF THE 1 JULY CALDERBANK: CONFIRMED FROM THE SENT ITEM

Source: documents/2026-07-01_Cory_Calderbank2_covering_email_SERVICE_PROOF.pdf (Outlook export).

**ESTABLISHED ON THE FACE OF THE DOCUMENT:**
- Subject: "WITHOUT PREJUDICE SAVE AS TO COSTS - Calderbank Offer - WC/2024/227 Shepherd v Workers'
  Compensation Regulator"
- From: coryshepherd1@hotmail.com
- **To (both principal recipients, NOT cc): Renee.Matheson@oir.qld.gov.au AND Appeals@oir.qld.gov.au**
- **Sent: Wednesday 1 July 2026, 12:16**
- Attachments: (1) the offer; (2) bundle of authorities referred to in it.
- Open 21 days; express invitation to confer ("willing to discuss... at any time within that period",
  "or to arrange a time to confer").
- ✅ **QIRC registry NOT copied.** No WP material near the decision-maker. Clean.

**CONSEQUENCES:**
1. **Service on the Regulator as respondent is proved on the face of the document.** Both addresses
   in the To field = addressed to the AGENCY as principal, not merely copied. Receipt cannot be put
   in issue. Strengthens s 558(3) / *Canton* costs position; also proves the offer to confer was
   made twice and declined twice (Feb + 1 Jul).
2. **Matheson is NOT a necessary link in any pathway** — the offer landed in a shared registry
   mailbox. This is exactly why Cory does not and will not attribute anything to her personally.
   Consistent with the withdrawal of the February reprisal allegation at the March QIRC conference.
   Any question is INSTITUTIONAL (agency records), never personal.
3. ⭐ **THE KEY NUANCE — THE MOST LIKELY PATHWAY IS ALSO A LAWFUL ONE.** On receipt of a settlement
   offer in a s 550 appeal, the Regulator's appeals unit contacting the employer is orthodox: the
   employer holds the evidence and has a direct interest in the outcome. MSH was already engaged in
   the proceeding via the 5 June 2026 Form 29 objection (Cridland signature; Myla Ruttan, Principal
   Lawyer, named contact). So MSH plausibly learned of the offer by an entirely proper route.
   → **Transmission is NOT the wrongdoing and must never be framed as one.**
   → The ONLY live question is: **what did MSH do with the knowledge the following day?** That is a
     question about MSH's conduct alone — the entity that has since shifted position six times,
     identified no instrument, held him out four weeks, debited leave by default, and as at 30 July
     still could not guarantee a return.
   This is a CLEANER position than the personal-inference framing: nothing is alleged against the
   Regulator or its officer; MSH is simply left to explain MSH's own conduct.

**ACTIONS:**
- [x] Sent item exported and filed.
- [ ] Obtain and record the TIMESTAMP on Taylor's 2 July email so the gap is measured in hours, not
      impression. (1 Jul 12:16 → ?)
- [ ] Keep the Outlook original; do not delete.

**DO NOT (standing):**
- No RTI to OIR — premature, signals investigation, material is not at risk.
- No question to Matheson about whether MSH was told — converts a preserved position into an
  asserted one and invites an untestable denial.
- Nothing about the pathway in ANY correspondence to anyone in the proceeding.
Sequence stays in (a) the statutory declaration / union chronology and (b) the reserved general
protections file.

## 31 JUL 2026, 11:43 — THE RFMI LANDS. DELEGATE REVEALED: SCOTT HUGHES, DIRECTOR CORPORATE SERVICES

Filed: documents/2026-07-31_Harrison_RFMI_covering_email_1143.pdf;
_ScottHughes_RFMI_letter_to_EMPLOYEE.pdf; _ScottHughes_RFMI_letter_to_GP_DrMa_9questions.pdf;
_RFMI_Attachment1_ECC_3July_asServed.pdf; _RFMI_Attachment2_AO3_Switchboard_Role_Description.pdf

**SERVICE:** From LBH_InjuryManagement, Michelle Harrison IMC. To Cory. **Cc notes@solv.com.au** (new
external "Solv" injury-management case system) and LBH.HRTeam1. **Friday 31 July, 11:43.**
Both letters **signed Scott Hughes, Director, Corporate Services, LBHS, dated 31/07/2026.**

**WHAT THE 30 JULY "DELEGATE APPROVAL" WAS FOR:** not the return to work — a further medical inquiry
with a **7 calendar day** return window (31 Jul + 7 = **7 AUGUST 2026 = the 64G mention date**) and a
decision-on-the-papers threat: "If you do not return the document within this timeframe or seek a
reasonable extension, I will make a decision regarding your ability to perform your role based on the
available information."

**AUTHORSHIP SEAM:** letters written in Harrison's first person ("I am seeking", "I require", "I will
make a decision") but signed by Hughes. Decision-maker still unidentified after four weeks.

### CONCESSIONS NOW IN WRITING (all favourable)
1. **Destination is the substantive position** — GP letter: "to support a safe and sustainable return
   to his substantive position." Displaces the 15 July "remains at the discretion of the Employer."
2. **Costs** — "MSH will meet your reasonable costs of preparing this report." Invoices to Harrison at
   lbh_InjuryManagement@health.qld.gov.au. ⚠️ SILENT on reimbursing the $150 already paid 10 Jul.
3. ⭐ **COMPLAINT HANDLING IS NOT HIS ROLE — MSH'S OWN WORDS TO HIS DOCTOR** (Q5): "established process
   for client complaints received by Switchboard employees is for immediate escalation and management
   by the Health Service Client Liaison Officer and/or Manager, Switchboard Services." Corroborated by
   Attachment 2 (the AO3 RD) which contains NO complaint-handling responsibility. The restriction used
   to justify four weeks of exclusion concerns a duty they now confirm is not his.
4. **"Permanent Full-time basis 76 hours per fortnight"** — stated in BOTH letters. MSH's own
   characterisation of his contractual baseline ⇒ reduced hours were an accommodation, not a
   variation; loss is measured on 76 hrs/ft.

### FIFTH LEGAL BASIS IN FOUR WEEKS — AND IT IS HIS
Now cited: "**HR Policy G3: Reasonable Adjustment**, and **sections 17 and 19 of the Work Health and
Safety Act 2011**." Sequence: 15 Jul discretion/no accepted claim → 29 Jul WHS (EAF) → 31 Jul G3 + ss
17/19. They have ADOPTED the Reasonable Adjustment framework he put to them on 28/30 July.
⚠️ BUT ss 17 and 19 are **duty** provisions (minimise/eliminate risk; primary duty of care). Neither
confers a power to exclude a worker or to compel medical information. Defect unchanged — only the
citation has improved.
[ ] VERIFY the "HR Policy G3" ↔ QH-POL-210 mapping before citing it back.

### THE THREE QUESTIONS THAT ARE NOT ABOUT ADJUSTMENT
- **Q2** — asks the GP whether Cory can "follow a reasonable and lawful direction issued by his
  supervisor" and "participate in discussions in relation to his workplace performance and/or
  conduct." That is **discipline vocabulary**, not capacity. They are seeking medical clearance to run
  a performance/conduct process.
  Premise of Q2: "**As the Health Service is not aware of any concerns being raised for appropriate
  management**" — a written denial, to his treating doctor, over a Director's signature, that he ever
  raised concerns. Against PID 24-ESU-1130, the PT safety report, the Feb complaint, Form 24, and a
  live appeal.
- **Q3** — "whether Mr Shepherd is medically fit to return to their substantive role under the
  existing reporting arrangements, including working with and reporting to their current line
  manager." **The psychosocial inversion, express.** The hazard is not assessed; his tolerance of it
  is. (Note: Attachment 2 RD names **Chloe Taylor** as contact — the line manager, author of the
  2 July origin document.)
- **Q1(a)** — "When was Mr Shepherd first diagnosed with MDD?" No adjustment utility whatsoever.
  Direct s 32 causation / pre-existing condition utility.
  **Q1(c)** — "solely on Mr Shepherd's self-report, your own clinical assessment, or other medical
  information" = the self-report displacement argument pleaded in the Regulator's SOFC.

### THE TRAP ARCHITECTURE (Q3 → Q9)
Q9: "**If we are not able to accommodate the restrictions you have recommended, is Mr Shepherd able to
safely return to the workplace?**" — presupposes inability to accommodate BEFORE any accommodation has
been assessed. Combined with Q3:
- GP answers Q3 "yes, fit under existing arrangements" → the raised hazard is medically erased; he
  returns into it.
- GP answers Q3 "no" → Q9 harvests it → MSH declares it cannot accommodate → permanent exclusion /
  ill-health pathway, with the treating doctor's own words supplying the basis.

### OPTION 2 (the authority form)
Employee letter offers: "Provide Metro South Health permission to obtain this information directly
from your medical practitioner." ⚠️ Given the Mind and Memory / QSuper history, direct-access authority
removes him from the pathway entirely. Note it; do not sign it.

### APPEAL OVERLAP — THE HEADLINE
A Director-signed request asks the appellant's treating GP for (a) the date of first MDD diagnosis and
(b) whether the workplace stressors rest on self-report or clinical assessment — the two central
contested issues in WC/2024/227 — answers due **7 August**, the day of the mention, routed outside the
appeal's disclosure processes and cc'd to an external vendor. Whatever the intention, that is the shape
on the face of the document.

## 31 JUL 2026 — WHO SCOTT HUGHES IS, AND WHY THE SIGNATURE MATTERS

Per Cory: Hughes is the **new** Director, Corporate Services — **hired while Cory was on leave**, at the
time **Corporate Services took over Switchboard**. Aligned with Chloe Taylor. Asserted to have been
substantially detrimental to Cory and to have been **deceptive in writing**.
[ ] LOCATE AND DATE the document(s) evidencing the written deception — statement + contradicting fact
    side by side. Assertion vs exhibit is the whole difference. Until then this line is UNVERIFIED here.

### 1. THE ESCALATION WAS HORIZONTAL, NOT VERTICAL
Every decision-maker since 2 July sits inside the affected chain:
- 2 Jul — **Chloe Taylor**, Manager Switchboard Services, Corporate Services
- 7 Jul — **Forrest**
- 15 / 29 / 30 Jul — **Michelle Harrison**, Injury Management, LBHS HR
- 31 Jul — **Scott Hughes, Director, Corporate Services** (Taylor's own Director)
"Progressing for delegate approval" reads as the file going UP AND OUT. It went SIDEWAYS — from the
line manager to the top of her own reporting line. **At no point has any person outside the affected
chain of command made a decision about him.** The two functions that could have supplied independence
are both implicated: Corporate Services is the directorate; HR received the PID and referred it to
itself.

### 2. Q3 IS SELF-REFERENTIAL
Q3 asks the GP whether Cory is fit "to return to their substantive role under the existing reporting
arrangements, including working with and reporting to their current line manager." **That reporting
line terminates in Hughes.** He is decision-maker on a question about his own directorate's
arrangements and his own subordinate's conduct. Neither letter discloses any conflict; both are drafted
to read as neutral HR machinery.
→ QPS **Code of Conduct cl 1.2**: a conflict is "not wrongdoing in itself" but "failing to disclose and
manage" one is "likely to be wrongdoing." Nothing disclosed on the face of either letter.

### 3. THE "NOT AWARE OF ANY CONCERNS" SENTENCE — BOTH READINGS HURT HIM
"As the Health Service is not aware of any concerns being raised for appropriate management."
- **If he genuinely didn't know** (arrived during the restructure, briefed by the people in dispute):
  a Director signed a factual assertion to a treating doctor that he could not personally verify, in a
  matter where his own **Chief Executive signed the 5 June 2026 Form 29 objection**. Not innocence —
  signing without reading the file.
- **If he did know**: the sentence is not a mistake.
⚠️ STRUCTURAL ROLE OF THE SENTENCE: it is the **premise of Q2** (can he follow lawful directions /
participate in discussions about performance and conduct). The false premise is what makes the
disciplinary framing appear reasonable to a reader with no background.

### 4. CONSTRUCTED KNOWLEDGE — WHY THE INVERSION MAY BE SINCERE
Hughes has NO independent knowledge of Cory. Everything he believes was assembled after the fact by the
people already in dispute with him. MSH's own 5 June objection documents the restructure: "an
organisational change related to the reporting lines for Switchboard" after 30 June 2024.
→ The psychosocial inversion may not be a tactic he adopted but the only version he was ever given.
That does not make it lawful; it makes it harder to dislodge, and it makes **the briefing he received**
the material fact. (Relevant to any future disclosure request: what was Hughes told, by whom, when.)

### 5. WHAT THE SIGNATURE CONVERTS THIS INTO
Before 31 July: a diffuse institution — six shifting positions, no identified decision-maker, no name
attached to the power asserted. A **Director's signature on a letter to the treating doctor ends that.**
- IR Act general protections: a person **involved in** a contravention can be **personally liable**.
- PID Act ss 40-42: reprisal is a **tort**; it attaches to individuals; exemplary damages available.
An institution absorbs a finding. A named Director with a paper trail does not.

## 31 JUL 2026 — THE CONFLICT OF INTEREST IN THE SIGNATORY: HOW TO FRAME IT PROPERLY

### DO NOT RUN THE WEAK VERSION
"He is the Director of the directorate, therefore conflicted" FAILS. In any HHS the Director is the
natural delegate for HR decisions about staff in that directorate — that is delegation working
normally. Proximity alone is not conflict. Build on the four specific strands instead.

### THE FOUR STRANDS
1. ⭐ **THE QUESTION IS ABOUT HIMSELF.** Q3 asks the GP whether Cory is fit "under the existing
   reporting arrangements, including working with and reporting to their current line manager."
   Those arrangements ARE Hughes's — Switchboard reports into Corporate Services; Corporate Services
   is him. Only two answers exist and one is a finding against his own directorate. He has a direct
   interest in the answer being "the employee cannot tolerate the arrangements" rather than "the
   arrangements are unsafe."
2. **THE CONDUCT IN ISSUE IS HIS SUBORDINATE'S** — Chloe Taylor reports to him. Whether her conduct
   was ever addressed is a question about HIS supervision. Delegate assessing his own direct report.
3. **HE IS A POTENTIAL RESPONDENT, NOT A BYSTANDER** (subject to the prior-conduct documents being
   located) — a participant in the dispute exercising decision-making power over the other party.
4. **THE RESTRUCTURE** — he was hired into the Corporate Services takeover of Switchboard. MSH's own
   5 June 2026 objection ties the fatigue-management gap to "an organisational change related to the
   reporting lines for Switchboard." He has an interest in that restructure reading as successful.

### THE POINT THAT DOES THE WORK — cl 1.2 DOES NOT PROHIBIT CONFLICTS
QPS Code of Conduct cl 1.2: a conflict is "not wrongdoing in itself"; "failing to disclose and manage"
is "likely to be wrongdoing."
⇒ The question is never "was he conflicted" but "**was it identified, declared and managed**."
On the face of both 31 July letters: **NOTHING**. No acknowledgment that the signatory heads the
directorate, supervises the manager, or owns the reporting line the doctor is asked to bless. Both are
drafted to read as neutral machinery from an uninvolved senior officer.
NOT an oversight: two years of complaints about this directorate, a PID, a live QIRC appeal, and a
**Chief Executive who personally signed the 5 June objection**. Selecting this delegate was a CHOICE.

### THE PATTERN — THIRD INSTANCE OF THE SAME STRUCTURE
1. PID → referred to **HR**, which was part of what was complained about.
2. Complaints about line management → handled by **line management**.
3. Assessment of whether the reporting arrangements are safe → delegated to **the owner of the
   reporting arrangements**.
Every time, the body assessing the problem IS the problem. Not an isolated governance lapse — a
structural absence of independence, repeated.
⭐ **Psychosocial Code of Practice 2022 names "poor organisational justice" (lack of procedural
fairness) as a HAZARD IN ITSELF.** So the conflict is not merely a defect in how the decision was
made; it is another instance of the very hazard he raised, now operating on the process built to
assess whether that hazard exists.

### THE FRAME TO USE: APPREHENDED, NOT ACTUAL, BIAS
Test: whether a fair-minded observer might reasonably apprehend that the decision-maker might not
bring an impartial mind. Does NOT require proving partiality — only that the apprehension is
reasonable. **Met on the UNDISPUTED facts alone**, before any prior-conduct evidence: Director of the
affected directorate; supervisor of the manager whose conduct is in issue; owner of the reporting line
under assessment; live QIRC proceeding; no disclosure. Lower bar = harder to answer. Choose it.

### THEIR BEST ANSWER — AND THE REBUTTAL
Expect: "Hughes is the RIGHT delegate BECAUSE he is new — arrived after the 2024 events, no history
with Mr Shepherd, a fresh pair of eyes. That is independence."
REBUTTAL: **freshness is only independence if the information is fresh too.** A Director briefed
exclusively by the parties in dispute is not an independent mind; he is their account carried by a
more senior signature. And the letter proves it — "As the Health Service is not aware of any concerns
being raised for appropriate management," written in a matter with a PID, the PT safety report, a
Form 24, a live appeal and a CE-signed objection before the Commission. That is not the error of an
independent decision-maker who read the file; it is precisely the error of a person whose entire
picture came from one side.
⇒ Their best argument for his independence is the thing that demonstrates its absence.

## 31 JUL 2026 — LEGAL ANALYSIS OF THE RFMI: WHAT THEY CAN LAWFULLY REQUIRE

### SOURCE OF POWER
They cite **HR Policy G3** and **ss 17/19 WHS Act 2011**. NEITHER IS A SOURCE OF POWER — policy binds
them, not him; ss 17/19 impose duties on the PCBU. The only real source is the employer's right to
give a **lawful and reasonable direction** (cf *Blackadder v Ramsey Butchering Services* (2005) 221
CLR 539 — employer may require medical examination to satisfy itself of fitness, as an incident of
the duty to provide a safe workplace).
⇒ The operative constraint is **REASONABLENESS**. A direction is reasonable only to the extent the
information is genuinely needed for the purpose. Beyond that it is not a lawful and reasonable
direction at all, and declining it is NOT misconduct.

### ⭐ THEY SUPPLIED THE YARDSTICK THEMSELVES
GP letter states the purpose: "to identify and implement any appropriate workplace controls or
reasonable adjustments to support a safe and sustainable return to his substantive position."
That is now the test, in their own handwriting. They cannot later assert a wider purpose without
contradicting their own document. Apply it question by question.

### ✅ AD ACT s 124 — VERIFIED FROM ATT16 (current as at 19 May 2025)
s 124(1): "A person must not ask another person, either orally or in writing, to supply information
on which unlawful discrimination might be based."
s 124(2): exceptions — necessary to comply with / specifically authorised by another Act, court
order, award, industrial agreement, or QCAT/QIRC order.
s 124(3): **DEFENCE — "if the respondent proves, on the balance of probabilities, that the
information was reasonably required for a purpose that did not involve discrimination."**
⇒ Impairment is a protected attribute; psychiatric history is information on which discrimination
might be based. **THE ONUS IS ON MSH** to prove reasonable requirement — a reverse onus running on
the same necessity test. Strongest hook against Q1(a).

### CLASSIFICATION OF THE NINE QUESTIONS
**LAWFULLY REQUIRED — ANSWER:**
- Q1(d) foreseeable risk + medically necessary controls (the actual WHS/adjustment question)
- Q4 restrictions/adjustments in functional terms, duration, review date
- Q5 what "complaint handling" encompasses
- Q8 tasks/situations/environments that exacerbate

**LAWFUL IN SUBSTANCE, WRONG RECIPIENT:**
- Q7 functional cognitive impact — proper question, beyond a GP; needs psychiatric input

**NOT REASONABLY REQUIRED — OBJECT:**
- Q1(a) date of first MDD diagnosis — cannot inform current controls. Clearest **s 124** candidate.
- Q1(b) clinical basis for the causal link — for adjustment it matters THAT something exacerbates,
  not the clinical reasoning WHY. The "why" is the s 32 question in the appeal.
- Q1(c) self-report vs clinical assessment vs "**other medical information/reports available to
  you**" — ⚠️ the tail is a FISHING question inviting the GP to identify OTHER REPORTS. Given how the
  Mind and Memory report reached this proceeding, object most firmly here.
- Q2 follow lawful directions / participate in performance & conduct discussions — readiness for a
  management process, not capacity for the role; false premise. Either a process exists (⇒ entitled
  to particulars + procedural fairness; and note PID reprisal exposure) or it does not (⇒ no stated
  purpose).

**WRONG LEGAL TEST — REFRAME:**
- ⭐ Q6 "full inherent requirements ... **without restrictions or modifications**" — THE CLEAREST
  LEGAL ERROR IN THE DOCUMENT. Neither G3 nor **AD Act s 34** asks whether the role can be performed
  WITHOUT adjustment; they ask whether genuine occupational requirements can be met WITH reasonable
  adjustments, subject to unjustifiable hardship (ss 5, 35). "Without restrictions or modifications"
  is the incapacity-termination test. They adopted an adjustment policy and then drafted a question
  that assumes it away.
- Q3 fit under existing reporting arrangements — asks a clinician to risk-assess a WORKPLACE SYSTEM.
  WHS s 19 + Psychosocial Code 2022 put that on the PCBU. EB12 cl 7.2.1 supplies the mechanism.

**PREMATURE:**
- Q9 — inverts the sequence. Lawful order: identify restrictions → assess available adjustments →
  determine whether any genuinely cannot be made and why (unjustifiable hardship). Q9 asks the doctor
  to answer step 3 before step 2 is attempted, on a hypothetical MSH constructed.

### ⭐⭐ THE STRUCTURAL POINT — THE IME BOUNDARY
A request to his OWN treating doctor rests on the reasonable-direction power. A **specialist
opinion**, if compelled, is an **independent medical examination** — which runs through **PS Act 2022
ch 3 pt 8 div 5 (s 103 gateway)** and **Directive 04/24**, NOT a letter from Injury Management.
s 103 gateway = employee **absent from duty OR performing unsatisfactorily**, AND reasonable
suspicion the cause is mental/physical illness.
- No performance issue has ever been put to him.
- Which leaves ABSENCE — and **the absence is MSH's own act.** They excluded him on 3 July from a
  workplace he was attending, holding a certificate that he was fit with restrictions.
⇒ **An employer cannot manufacture the absence and then rely on it as the gateway to compel an
examination.** Specialist input here is therefore VOLUNTARY and arranged by him under option 1.
This is why declining option 2 is not a preference but a structural protection.

### TO VERIFY
[ ] IP Act 2009 (Qld): confirm HHSs are "health agencies" bound by the **NPPs** (Sch 4) rather than
    the IPPs (Sch 3). NPP 1.1 (collection only where **necessary** for a function/activity) and NPP 10
    (sensitive information) would add a second necessity constraint alongside AD Act s 124. Not in the
    instruments bundle — do not cite until confirmed.
[ ] Pull the exact s 103 PS Act wording and Directive 04/24 before relying on the gateway argument in
    correspondence.

### BOTTOM LINE
Answering the five and objecting to the four is NOT a refusal to comply with a lawful and reasonable
direction. **Blanket refusal WOULD be misconduct**, because four questions are plainly proper. Full
compliance on everything legitimate is what makes the objections impossible to characterise as
obstruction.

### ALSO 31 JUL — APPOINTMENT CANCELLED
Cory cancelled the 2pm Friday 31 July consult with Dr Ma because the scope was unsettled. Letter
updated accordingly: the extension ground is now that the RFMI arrived 11:43am, ~2 hours before a
consult MSH had been notified of on 30 July, and that he cancelled rather than incur a cost both
parties would have wasted, and will rebook once the question set is settled.

## 31 JUL 2026 — ⭐ THE PURPOSE INVERSION: THE ECC WAS REQUIRED SO HE COULD WORK, THEN USED TO REFUSE WORK

Cory's observation, and it is the strongest single factual point in the dispute because every
element is proved by an MSH document.

**MSH'S OWN ADMISSION OF PURPOSE — 31 July 2026 letter to employee, signed Scott Hughes, Director:**
    "your recently completed Employee Capabilities Checklist (ECC) (Attachment 1) completed by
    Dr Day Hong Ma on the 3 July 2026 **which was provided to us to facilitate a Return to Work
    Plan**."

**THE SEQUENCE (all MSH-sourced):**
1. **2 Jul** — Chloe Taylor, Manager Switchboard Services, requires a completed ECC; return to work
   cannot be facilitated until provided; deadline "before 2:00pm Friday 3 July."
   (documents/2026-07-02_Taylor_ECC_LeaveType_ORIGIN_DOCUMENT.pdf)
2. **3 Jul 14:32** — ECC provided. **Certifies FIT TO WORK WITH RESTRICTIONS.**
3. **3 Jul ~15:30** — held out of the workplace (58 minutes later); rostered shifts charged to
   accrued sick leave.
4. **31 Jul** — MSH states in writing the ECC was "provided to us to facilitate a Return to Work
   Plan."

**WHY IT MATTERS**
- **The document cannot explain the decision.** It said FIT. If it had said unfit, exclusion would
  follow logically. It said fit, and work was refused within the hour. Something other than the
  document explains the exclusion.
- **It destroys the retrospective safety narrative.** If MSH held a genuine safety concern as at
  2 July, it would not have required a document *to facilitate his return*. The 2 July direction is
  MSH's own evidence that its position that day was that he WOULD be returning.
- **Purpose deviation.** Obtained for purpose A (enable work); used for purpose B (refuse work).
  Cf QPS Code of Conduct cl 4.1(c) (powers used for the purpose granted) and cl 4.4(a) (information
  used only for the purpose collected). ⚠️ State the FACTS in correspondence; do not plead the Code
  provisions at MSH — they are for the union brief / reserved tracks.
- ⭐ **IT REFRAMES THE WHOLE FIVE WEEKS.** The 7 Jul "further information", 15 Jul "discretion",
  29 Jul WHS basis and 31 Jul RFMI are all downstream of an inversion at step one.
  **They are not clarifying the ECC. They are seeking a different document.** Q1(a)-(c) of the RFMI
  attack the certificate MSH itself demanded rather than implement it.
- Feeds the appeal/union tracks: the 2 July direction issued from the PID-subject line manager the
  day after the 1 July Calderbank. NOT asserted anywhere — chronology only.

**WHERE IT NOW SITS:** Part 1.1 of drafts/SEND_31JUL/RFMI_ALLOCATION_AND_PROPOSAL.txt (and the
built PDF), plus a short paragraph in RFMI_RESPONSE_EMAIL.txt. Framed factually, closing with the
constructive ask — that clarification be directed to identifying the adjustments which allow him to
work, being the purpose MSH itself stated.

⚠️ WORDING DISCIPLINE PRESERVED: uses the safe formulation "I was told on 2 July 2026 that my return
to work could not be facilitated until a completed ECC was provided" — NOT a claim about which shift
was last worked, which remains unresolved (see the 2 July origin-document note).

## 31 JUL 2026 — HUGHES IS ANSWERABLE FOR TAYLOR: THE CONFLICT BECOMES SPECIFIC

Cory's point: Chloe Taylor's line runs to Scott Hughes. He approves her actions. He is answerable
for them. That converts the conflict from structural to specific, and it is the version that cannot
be answered.

**THE FINDING HE WOULD HAVE TO MAKE.** To decide this matter correctly, Hughes must find that a
direction issued within his own reporting line — requiring a document so that Cory could work — was
then used to refuse him work. **No decision-maker can be expected to make that finding against his
own direct reports.** That is not a theoretical apprehension of bias; it is a specific, identifiable
finding, adverse to his own directorate, that the decision requires.

**RATIFICATION.** Before 31 July the exclusion was arguably the act of subordinates. By signing the
two letters, a **Director** has adopted its continuation. He held the authority to end it — he could
have directed a return to roster — and instead signed a request for further medical information.
From 31 July the position is his.

**CONSTRUCTIVE KNOWLEDGE.** Even on the most favourable view (arrived during the restructure,
briefed one-sidedly), a Director who signs a letter to an employee's treating doctor is taken to
have satisfied himself of its contents — including "the Health Service is not aware of any concerns
being raised."

**WHAT WENT INTO THE DOCUMENT (Part 6):**
- The factual chain, asserting nothing: the Manager, Switchboard Services who issued the 2 July
  direction reports within Corporate Services; the signatory of the 31 July letters is the Director
  of that directorate; the officer now determining the return is therefore the officer to whom the
  manager who issued the direction reports.
- NEW question (d): **"whether the direction of 2 July 2026, and the decision of 3 July 2026 by
  which I was excluded from the workplace, were made with the knowledge or approval of the officer
  now determining my return to duty."**
  ⭐ Cannot be answered well: "yes" ⇒ he is a participant, not an independent delegate; "no" ⇒ he is
  deciding on conduct in his own line he was unaware of; no answer ⇒ the failure to manage under
  cl 1.2 is documented.
- The remedy asked for: **that any decision concerning capacity or return to duty be made by an
  officer outside Corporate Services** — "Metro South Health is a large organisation and I do not
  anticipate that this would present any difficulty." (Forecloses "no one else available." NOTE for
  the union brief only: MSH's own 5 June objection puts its headcount at ~20,006 MOHRI.)
- Added to the Part 10 response list as item 2.

⚠️ DISCIPLINE: nowhere asserted that Hughes approved the 2 July direction — that is unknown, and is
put as a question. The reporting relationship is stated as fact because it is one.

## 31 JUL 2026 — ⚠️ THE DIAGNOSIS DATE COLLIDES WITH THE REVIEW DECISION DATE

Cory advises the first MDD diagnosis was **24 October 2024** and proposed stating it openly.

⛔ **CHECK PERFORMED: Review Decision 69983 is dated 24 OCTOBER 2024** — the same day.
(documents/Review_Decision_69983_24.10.2024.pdf — "Reasons for decision, 24 October 2024",
insurer ref S23LW142013, review application received 16 September 2024, reviewing WorkCover's
decision of 22 October 2024 rejecting the application for compensation.)

**THE RISK:** a bare date, volunteered without clinical context, hands the Regulator the argument
that the MDD was diagnosed on the day the adverse review decision issued — i.e. a reaction to the
claim process rather than the employment. Matheson and her counsel would see it immediately.
**The argument IS answerable — but clinically**, by a practitioner who can explain the course of the
condition from March 2024 and why the diagnosis was formalised when it was. It is NOT answerable by
Cory stating a date in an HR letter.

**RESOLUTION ADOPTED (Part 5.1, Q1(a)):** do not conceal, do not volunteer the bare date. The
document now says he does not object to the Health Service being informed, objects only to the
question AS FRAMED, and proposes a REPLACEMENT question which asks for MORE:
    "What is the employee's current condition and prognosis, **including when the diagnosis was
    made and the course of the condition since**, and over what period are the recommended
    adjustments expected to be required?"
⇒ The date arrives from the clinician WITH context. Cannot be characterised as evasive — he is
offering more information, not less. Table entry updated to "Reframed — Dr Ma, with clinical
context."

**FOR THE APPEAL (critical):** the psychiatrist preparing the updated report MUST address the
chronology explicitly — the course of the condition from the March 2024 events through to the
October 2024 diagnosis. This is now a known line of attack. Brief them on it.

## 31 JUL 2026 — TWO FURTHER ADDITIONS TO THE RESPONSE

**PART 1.3 — INFORMATION MSH ALREADY HOLDS.** Maps what is already in their possession: the ECC
(quoted via MSH's own 31 July letter, so safe to rely on while the ECC PDF remains image-only); the
Role Description at Attachment 2 (no complaint-handling duty); MSH's own statement of the complaint
escalation process; Forrest's 7 July acknowledgment that restrictions were already being
accommodated; and ~12 months working in the substantive role under the existing reporting
arrangements on adjusted hours to 3 July 2026 (MSH's own rosters/payroll evidence it).
⇒ "That material already answers Question 5, and goes a considerable way toward answering Questions
1(d), 3, 4, 6 and 8." Closing line: "I have now been excluded from the workplace for five weeks
while information the Health Service largely already holds is sought again."

**PART 3.2 — THE REFERRAL SEQUENCE.** A psychiatrist referral comes from the GP. So the order is:
rebook and hold the Dr Ma consult → Dr Ma answers within scope and, if Q7 is pressed, provides the
referral → psychiatrist appointment obtained → opinion follows. **None of that occurs within seven
calendar days, and the first step cannot sensibly occur until MSH confirms which questions it
presses.** Makes the seven-day deadline impossible on its own terms, without argument.

## 31 JUL 2026 — CORRECTION: THE 24 OCTOBER COINCIDENCE IS DEFEATABLE, AND THE CLAIM DATES

Cory clarifies: the MDD diagnosis was made on 24 October 2024 **before** he received the review
decision. Same-day coincidence only.

**WHAT THE DOCUMENT ACTUALLY SHOWS** (documents/Review_Decision_69983_24.10.2024.pdf):
- **Review decision MADE 22 October 2024**; **"Reasons for decision" letter DATED 24 October 2024.**
  So the decision PREDATES the diagnosis by two days; what coincides is the DATE ON THE LETTER.
- Issued by **Victoria Squires, Senior Reviewing Officer, Review Unit, Workers' Compensation
  Regulatory Services**, PO Box 10119 Brisbane. 28 pages.
- ⚠️ **cc Metro South Hospital And Health Service** and cc WorkCover Queensland. MSH receives the
  Regulator's decisions in his matter as a matter of course — an established routine channel.
  CHRONOLOGY ONLY; nothing to be drawn from it, and nothing to be asserted anywhere.

**WHY THE ATTACK FAILS — BUT ONLY ON EVIDENCE:** the letter issued from a Brisbane PO Box. Unless
emailed early that morning, receipt could not precede a same-day consultation. The "diagnosed in
reaction to the decision" argument requires a practically impossible sequence.
**OBTAIN NOW (both easy today, harder later):**
[ ] The clinical note for 24 October 2024 — time of consultation, presenting complaint, what was
    recorded.
[ ] Proof of actual service of the reasons — covering email with timestamp, or envelope/postmark.
⇒ Once the sequence is documented to the hour, the coincidence becomes an own-goal for whoever
raises it. Cory cannot prove it by assertion; the CLINICAL RECORD proves it — which is exactly why
Q1(a) must reach MSH from the practitioner with the course of the condition attached. Drafting
decision unchanged, now for a better reason.

**CLAIM CHRONOLOGY CORRECTED (from the review decision itself):**
- Psychological injury **sustained 18 June 2024** — "workplace stress and bullying". Employed
  full-time as an Administration Officer, Logan Hospital.
- Application for compensation lodged with WorkCover **1 July 2024**.
- WorkCover rejected **13 September 2024** (s 32). Four causative factors identified: manager's
  failure to follow rules; management's failure to take action on an ethical complaint made by him;
  his payment being withheld; roster guidelines not followed. 1st and 3rd "unable to be
  substantiated"; 2nd and 4th held to be reasonable management action taken reasonably ⇒ s 32(5)
  exclusion enlivened.
- Application for review received by the Regulator **16 September 2024**.
- Review decision **22 October 2024**; reasons dated **24 October 2024**; WorkCover's rejection
  confirmed.
⇒ The 17–18 March 2024 shifts (the "Matter in Issue" pleaded in the Form 29) are STRESSOR EVENTS
within the claim, NOT the injury date. Earlier working notes loosely treated this as a "March 2024
injury" — correct that wherever it appears.
⇒ **FOR THE PSYCHIATRIST BRIEF: the gap to explain is 18 June 2024 → 24 October 2024, ~4 months,
not 7.** Materially easier to account for clinically.

## 31 JUL 2026 — CORRECTED AGAIN: THE 24 OCTOBER SEQUENCE IS SAME-DAY, APPOINTMENT FIRST

Supersedes the framing in the preceding note, which wrongly treated the DECISION DATE (22 Oct) as
the relevant date. The relevant date is **RECEIPT**.

**THE ACTUAL SEQUENCE — 24 October 2024:**
1. Appointment with the doctor; **MDD diagnosed**.
2. **Later the same day**, the review decision (reasons dated 24 October 2024) arrived.

⇒ The diagnosis CANNOT have been caused by the decision — he did not have it yet.
⇒ BUT this is a SAME-DAY sequence. **The date proves nothing; the TIME proves everything.**

**THE SINGLE HIGHEST-VALUE DOCUMENT:**
[ ] **The email delivering the reasons on 24 October 2024, with its timestamp.** He was
    self-represented at that point (Saines cost agreement not until 26 Nov 2024), so it came to him
    directly — his own inbox, Oct 2024, from Workers' Compensation Regulatory Services /
    worksafe.qld.gov.au, ref 69983, 28 pages.
[ ] **The consultation time on the clinical note for 24 October 2024.**

⭐ **WITH BOTH TIMES DOCUMENTED THE POINT INVERTS.** It stops being a defence and becomes evidence
FOR him: on 24 October 2024 he sought medical help and was diagnosed BEFORE knowing any outcome —
a condition live and deteriorating independent of the litigation, which is the opposite of what the
coincidence would otherwise suggest.

Risk assessment: modest. The Regulator may never run it. But it is the kind of point that sounds
damaging if unanswered and is embarrassing to raise if answered. Worth ~20 minutes, not more.
No change to the RFMI drafting — Q1(a) still routes through the clinician with clinical context.

## 31 JUL 2026 — SPECIALIST PATHWAY CORRECTED: EXISTING PSYCHIATRIST, NO GP REFERRAL BOTTLENECK

Cory has an existing treating psychiatrist and can instruct him directly, provide the material, and
have the consultation and report billed to MSH.

**CORRECTION TO PART 3.2.** The earlier draft asserted the delay ran through a GP referral. That was
wrong and MSH could have pointed out he was waiting on something he did not need. Note also that an
employer-funded report is generally not Medicare-rebatable in any event, so the referral question
largely falls away once MSH is paying — it is billed privately, direct to them.

**THE ACCURATE SEQUENCE, NOW IN THE DOCUMENT:**
1. MSH confirms which questions it presses and that it will meet the cost.
2. Cory instructs his treating psychiatrist on the confirmed question set.
3. Appointment obtained; opinion prepared and provided.
4. Dr Ma's cancelled consultation likewise cannot sensibly be rebooked until the set is settled.

⭐ **THE LINE THAT DOES THE WORK:** "The only step which cannot presently begin is the one which
depends on the Health Service, and I ask that it be taken promptly so that the rest can follow."
Accurate, unarguable, and puts the delay where it belongs — on the party running the seven-day
clock.

**COSTS TIGHTENED (Part 9(c)):** the psychiatrist's invoice will be directed to the Injury
Management Consultant on the same basis as Dr Ma's, and **confirmation is sought BEFORE the
appointment is made "so that I am not required to fund it in advance as I was required to fund the
Employee Capabilities Checklist."** Ties the forward arrangement to the unreimbursed $150 of
10 July without re-arguing it.

**DRAFTING NOTE:** the document says "my treating psychiatrist" throughout and does not disclose
whether the relationship is new or existing. That is immaterial to MSH and there is no reason to
volunteer treatment history beyond what the ECC already discloses.

**STILL WORTH OBTAINING (appeal, not MSH):** the psychiatrist REFERRAL DOCUMENT and its date — an
objective contemporaneous marker of clinical escalation, and what the GP wrote as the reason for
referral is often more valuable than the date. A referral dated between 18 June 2024 and
24 October 2024 would defeat the "reaction to the review decision" point on its own, without needing
consultation timestamps.

## 31 JUL 2026 — SPECIALIST COSTS: NOTIFICATION, NOT REQUEST

Cory's call: don't seek MSH's confirmation before the psychiatrist appointment — just have the
invoice directed to them. Correct, because MSH has already committed in writing ("MSH will meet
your reasonable costs of preparing this report") and asking permission to rely on their own
undertaking both delays him and weakens the position.

**REDRAFTED AS A NOTIFICATION.** Part 3.2 now asks MSH to confirm only the SCOPE (which questions
it presses), then states:
    "I will then instruct my treating psychiatrist. The invoice for the consultation and the report
    will be directed to you, on the basis of the Health Service's written confirmation that it will
    meet my reasonable costs of preparing this report. **If the Health Service contends that its
    undertaking does not extend to specialist input which its own questions require, I ask that it
    say so now, rather than after the cost has been incurred.**"
Part 9(c) mirrors it.

⇒ Nothing blocks him; the record exists; any objection must be made in advance. If MSH later
refuses, the refusal is a document — and it would be a refusal to fund specialist input required by
its own question set, after committing in writing to meet reasonable costs.

**RESIDUAL RISK (accepted, and small):** MSH could argue "this report" meant the GP report only. The
answer is that the specialist opinion answers ITS questions, which is why the sentence inviting an
advance objection is there.

**HOUSEKEEPING:** removed a stale cross-reference ("paragraph 3 of my letter") left over from the
earlier single-letter draft; corrected the covering email's pointer to the proposal from Part 6 to
Part 7. All remaining cross-references verified against the current structure.

## 31 JUL 2026 — ASSUME REPORT A REACHES THE REGULATOR. THE SCOPE LIMIT IS A FILTER, NOT A SHIELD.

Cory's point, and it corrects an earlier framing of mine: whatever goes to MSH will reach the
Respondent regardless.

**HE IS RIGHT. THE BASIS:**
- Review Decision 69983 is **cc'd to Metro South Hospital And Health Service** — the Regulator sends
  MSH its decisions in this matter as a matter of course.
- MSH is an active participant in the proceeding as a non-party (5 June 2026 Form 29 objection, CE
  signature, Metro South Legal engaged).
- A medical report about him has already reached this proceeding once (the 13 Feb 2025 Mind and
  Memory report, surfaced in another party's disclosure material).
- Disclosure runs both ways; an NNPD to MSH for his employment/medical file is available to anyone.
⇒ **Assume anything MSH holds is available to the Regulator.**

**CORRECTED FRAMING.** The scope limit on Report A was earlier justified partly as keeping it out of
their hands. Wrong. The real protection is: **not that they won't see it — that there is nothing in
it for them to use.** Confined to current capacity, functional restrictions and adjustments, Report
A says nothing about the contested s 32 question. They can read every word and be no further
forward.
⇒ This makes the scope limit MORE important, not less. The alternative — a causation-ranging report,
generated inside MSH's framing, answering questions designed to test whether the stressors are
"solely self-report", landing with the Respondent — would be his own document damaging his case.

**REPORT B IS GENUINELY PROTECTED.** Commissioned by Cory for the dominant purpose of the
litigation ⇒ **litigation privilege**. MSH never holds it and cannot pass on what it does not have.
Disclosable only if he elects to rely on it. ⚠️ If an NNPD were ever served on the psychiatrist for
"all records concerning Cory Shepherd", there would be a privilege claim to make — manageable, not
costless. Two-report structure survives the assumption that Report A goes everywhere.

**⭐ THE CONTROL THAT NOW MATTERS MOST IS THE BRIEF TO THE PSYCHIATRIST.**
Report A must be instructed expressly: answer capacity and adjustment questions ONLY; **do not
comment on cause or origin, even in passing**; if a question invites it, state that it falls outside
the scope of the report.
A well-meant throwaway ("his condition arose from workplace bullying") would FEEL helpful and would
be dangerous — an unreasoned causation statement in a document not prepared for that purpose, later
sitting beside the reasoned opinion in Report B. That inconsistency is exactly what gets read to a
witness in cross-examination.

**ADDED TO PART 9 — "USE OF THE INFORMATION":** asks MSH to confirm the information will be used
only for the stated purpose, and to **identify any person or entity outside the Health Service to
whom it is proposed to be provided** — prospectively, "before the information is obtained rather
than after." Framed as an ordinary question about the handling of health information; no reference
to the Mind and Memory history.
⇒ Either-way value: confirmation gives a written use limitation; refusal or silence is itself a
document, and signals what is coming.

**THE UPSIDE, WHICH IS REAL:** a properly scoped Report A that finds him FIT TO WORK WITH ADJUSTMENTS
and identifies workplace features as what require control is (a) evidence the condition is real and
ongoing, (b) evidence he is fit and willing to return — which supports the ongoing-detriment framing
and forecloses any suggestion he is not trying — and (c) funded by MSH. Reaching the Regulator is
not necessarily bad; it is bad only if it is unscoped.

## 31 JUL 2026 — REVISED: ONE REPORT + A LATER SUPPLEMENTARY, NOT TWO FULL REPORTS

Cory's push-back, and he is substantially right. Earlier two-report advice was over-engineered.

**CONCEDED — THE HISTORY GOES IN REGARDLESS.** A psychiatric report cannot answer MSH's questions
without setting out the condition's course and the workplace features that drive it: Q1(d)
(foreseeable risk on return), Q4 (restrictions + clinical basis), Q8 (what exacerbates). MSH's own
questions require the history. Pretending the report could be "silent on aetiology" was unrealistic.

**WORDING FIXED (Part 3.2).** Was: "It will not address the aetiology of my condition."
Now: "It will be directed to my current capacity, functional restrictions and the adjustments
recommended — that is, to the stated purpose of this inquiry. **It is not a medico-legal opinion on
the cause of my injury**, which is a matter in issue in WC/2024/227 and is not necessary for that
purpose."
⇒ States what the report IS rather than promising what it will not contain. Accurate even when the
report contains history; does not box him in.

**COROLLARY — BRIEF THE PSYCHIATRIST FULLY.** If the history is going in anyway, a half-informed
report is worse than a fully-informed one. Give him the chronology, the events, the workplace
material. Inaccuracy is what gets exploited, not detail.

### ⭐ THE REFRAME THAT MATTERS: THE APPEAL IS NOT WON ON THE MEDICAL EVIDENCE
Review Decision 69983 (24 Oct 2024) rejected the claim on the **s 32(5) EXCLUSION**, not on s 32(1):
    "the first and third factors were unable to be substantiated, while the second and fourth factor
    amounted to reasonable management action taken in a reasonable way. This meant **to the extent
    that your injury arose out of your employment where employment was a significant contributing
    factor**, it arose out of reasonable management action taken in a reasonable way. Consequently,
    the exclusionary provisions in section 32(5) of the Act were enlivened."
⇒ WorkCover effectively ASSUMED s 32(1) and rejected on **s 32(5)(a)**.
⇒ **s 32(5)(a) is not a medical question.** Whether management action was reasonable and taken
reasonably is answered by what management ACTUALLY DID — rosters, emails, complaint records,
delegate correspondence. **That is what the 64G production is for.** This is the strongest
justification yet for the 64G being the centre of gravity of the appeal.

**QUALIFICATION — s 32(1) IS LIVE AGAIN ON APPEAL.** De novo, so the Regulator is not bound by
WorkCover's concession, and its SOFC contests causation (pre-existing anxiety / self-report
displacement). So medical causation evidence IS still needed — but for the SOFC's contentions, not
for the ground of rejection.

### PRACTICAL POSITION ADOPTED
**One properly briefed report now**, and **a short supplementary later** addressing the statutory
questions MSH never asked: significant contributing factor; the specific operative stressors; and
the response to the pre-existing-condition contention — structured as expert evidence for the
Commission. One attendance. Decision on the supplementary deferred until the first report is read.

**RESIDUAL RISK (accepted by Cory, stated once):** a report in MSH's hands cannot be withdrawn if
part of it is unhelpful. He has weighed it and formed the view the content will favour him; on what
the ECC already records, that is a reasonable bet.

## 31 JUL 2026 — HANDLING OF THE MEDICAL INFORMATION: MEDICAL-IN-CONFIDENCE + NO CONFLICTED READER

Cory's point: the report should go to someone with no conflict of interest, and be "privileged."

⚠️ **TERMINOLOGY — DO NOT USE "PRIVILEGED" FOR REPORT A.** Legal privilege attaches to
communications for the dominant purpose of litigation or legal advice. A report prepared for an
employment adjustment purpose is NOT privileged, and asserting it is invites a correction that costs
credibility on a point he does not need. (Report B — commissioned for the appeal — IS privileged.
Keep the two straight.)
✅ **CORRECT FRAME: "medical-in-confidence" + need-to-know.** Orthodox public sector practice —
medical reports are held by the injury management / occupational health function, and line managers
receive THE ADJUSTMENTS TO IMPLEMENT, not the underlying clinical detail.

**GROUNDED IN THEIR OWN POLICY (G03 cl 3, already verified):**
- "Queensland Health acknowledges the right of the person with disability, condition, cultural
  considerations or neurodivergence to **choose how disclosure of information occurs**."
- "**It may only be necessary to share information when** the ability to meet genuine occupational
  requirements and or individual safety is at risk and reasonable adjustment is required."
⇒ A need-to-know limit in MSH's own instrument.

**ADDED TO PART 9 — "HANDLING WITHIN THE HEALTH SERVICE".** Asks that any medical information be:
  (a) held by the Injury Management Consultant on a **medical-in-confidence** basis;
  (b) **not provided to the line manager or Switchboard Services** — "a line manager requires the
      adjustments to be implemented, not the underlying clinical information" (constructive framing:
      concedes the operational need while excluding the clinical detail);
  (c) accessible only to those who require it to determine what adjustments can be made; and
  (d) **considered, for any decision about capacity or return to duty, by an officer in relation to
      whom no conflict of interest arises** — expressly linked to Part 6.
Closes: "I raise this in the ordinary way, and not as a criticism of anyone's handling to date."

**PART 10 RESPONSE LIST EXPANDED to 8 items** — new item 7 folds together the purpose limitation,
prospective identification of external recipients, and the internal handling regime.

⇒ (d) is the quiet one: it converts the Part 6 conflict question from a procedural inquiry into a
condition on the provision of his health information. If MSH wants the report, it has to engage with
who reads it. Document now 8 pages.

## 31 JUL 2026 — PART 6 RESTRUCTURED: NAME THE DELEGATE, DON'T ASK WHO HE IS

Cory's edit: Hughes signed both letters, so asking "who is the delegate" reads as coy, and Hughes
sits in the direct evidentiary line of the conflict already raised by email.

**RESTRUCTURED.** Was: "(a) who is the delegate...". Now:
    "I therefore understand Mr Hughes to be the delegate for the decisions those letters describe.
    **If that is not correct, please identify the officer who is**, and explain who exercises which
    function."
⇒ States the apparent position and puts the burden of correction on MSH. They must either CONFIRM
Hughes (which locks in the conflict) or NAME SOMEONE ELSE (which then requires explaining why the
letters asserting the decision-making power are signed by someone who is not the decision-maker).
No vague third answer is available.

**THE CHAIN NOW SET OUT AS THREE NUMBERED FACTS (a)-(c):** Q3 asks the GP about reporting
arrangements within Corporate Services, of which Hughes is Director; the Manager, Switchboard
Services who gave the 2 July direction reports within that same directorate; and Hughes is asked at
Part 4 to determine whether those arrangements are safe and whether adjustments can be accommodated.

**THE LINE THAT LANDS IT:** "The officer determining my return to duty is therefore the Director of
the directorate in which the direction of 2 July 2026 was given, and the officer to whom the manager
who gave it reports. **He is not adjacent to the matters in issue; he sits within them.**"
Still no allegation — every element is a fact about the org chart and about what the letters say.

**QUESTIONS RENUMBERED (d)-(f):** source/instrument of the delegation; whether a conflict has been
identified, declared and managed; and whether the 2 July direction and the 3 July exclusion were
made with the knowledge or approval of the officer now determining the return.

**REASSIGNMENT ASK STRENGTHENED:** was conditional ("if a conflict is identified"); now unconditional
— "I ask that any decision concerning my capacity or my return to duty be made by an officer outside
Corporate Services."

⚠️ **[DATE] PLACEHOLDER** in the first line — insert the date of the earlier email in which the
conflict/delegation question was raised. Specific and provable beats "previously". Document now
8 pages.

## 31 JUL 2026 — THE CLOSED LOOP IS NOW COMPLETE: LEGAL DOES NOT HOLD THE EMPLOYMENT FILE

Cory's observation: the Director, the manager and HR are all acting within their own area, and
Legal does not have carriage of the employment matter.

**DECISION-MAKERS SINCE 2 JULY — ALL IN-LINE:**
Chloe Taylor (Manager, Switchboard Services, Corporate Services) → Forrest (7 Jul) → Michelle
Harrison (Injury Management, LBHS HR) → **Scott Hughes (Director, Corporate Services, 31 Jul)**.
Metro South Legal — the one function with both independence and file knowledge (Myla Ruttan
drafted the 5 June objection incl. Item 20 on PID 24-ESU-1130) — does not hold it.

**THIRD INSTANCE OF THE SAME STRUCTURE:**
1. PID → referred to HR, which was part of what was complained about.
2. Complaints about line management → handled by line management.
3. Whether the reporting arrangements are safe → decided inside the directorate that owns them.

⚠️ **DO NOT OVERSTATE — in-line decision-making is NOT improper per se.** Directors ordinarily
decide about their own directorates; HR administers; Legal is consulted on exception.
**WHAT MAKES IT SIGNIFICANT HERE** is the combination: formal complaints about that directorate;
a PID; a live QIRC proceeding about its conduct; a Chief-Executive-signed objection in that
proceeding; and a written request from the employee to address the conflict, unanswered.
⇒ **THE PRECISE FORMULATION: not that they were wrong to handle it, but that the circumstances
called for escalation out of the line and it did not happen.** Much stronger, and unanswerable.

⚠️ **ALSO DO NOT SAY "UNSANCTIONED" OR "ACTING ALONE".** A Director signed — that IS internal
authorisation at delegate level. "Rogue officer" gives MSH an easy exit (disown the individual,
correct the decision, walk away clean). Because Hughes signed, **MSH is the actor and there is
nobody to disown.**
✅ **THE ARGUMENT IS: they acted WITH AUTHORITY and WITHOUT POWER.** Authorised at Director level;
five weeks; six shifting bases; no instrument ever identified. No escape route.
Where "no authority" genuinely bites is the **3 July decision** — still no named decision-maker,
still no instrument. Hence question (f).

**RATIFICATION:** by signing on 31 July, Hughes adopted the earlier decisions — both letters
proceed on the footing that the exclusion is valid and continuing. Whatever the position on
3 July, from 31 July a Director owns it.

**ADDED TO PART 6:**
    "So far as I am aware, every decision concerning my attendance, my pay and my return to duty
    since 2 July 2026 has been made within Corporate Services. If that is not correct, I would be
    grateful to be told who else has been involved."
and, before the reassignment request: "I am not asking that anyone be found to have done anything
wrong. I am asking that the decision be made by someone who is not within the arrangements it
concerns."
⇒ Qualified by "so far as I am aware" so it invites correction rather than argument. Converts the
reassignment request from a procedural nicety into a request for **the first independent look the
matter has had in five weeks.**

## 31 JUL 2026 — ⭐⭐ THE ECC READ IN FULL (5 pp, image-only PDF read page-by-page as images)

Source: documents/2026-07-31_RFMI_Attachment1_ECC_3July_asServed.pdf. Signed **3.7.26**, Dr Day Hong
Ma, MBBS FRACGP FACRRM, Provider No 4696842K, My Doctors Clinic, 16/3221 Surfers Paradise Blvd.
(No OCR on this box — extracted via `pdfimages -png` and read as images. Repeat that method for any
other scanned PDF.)

### ⭐ THE HEADLINE: THE RESTRICTION AND MSH'S OWN PROCESS ARE THE SAME THING
**ECC:** "No complaint-handling duties: complaints received at the Switchboard are to be logged and
redirected to management/the dedicated complaints area, not actioned, resolved or absorbed by
Mr Shepherd."
**MSH 31 Jul:** "established process for client complaints received by Switchboard employees is for
immediate escalation and management by the Health Service Client Liaison Officer and/or Manager,
Switchboard Services."
⇒ **The sole restriction driving five weeks of unpaid exclusion asks MSH to do exactly what MSH says
it already does.**

### THE ECC ALREADY ANSWERS 7 OF THE 9 RFMI QUESTIONS
- **Q4** ← AC2: "Episodic, with symptom exacerbation linked to stressor exposure. The restrictions
  below are expected to remain necessary for at least the next 3-6 months, subject to treatment
  response and 8-weekly review." Review date on p1: **28 August 2026**.
- **Q1(d)** ← AC3 (work pattern with clinical reasoning per shift type) + AC4 (five modifications).
- **Q5** ← the complaint restriction, defined verbatim.
- **Q6** ← "**Usual switchboard operational duties remain suitable**; complaint-handling duties are
  excluded as below."
- **Q7** ← "Memorising information — Restricted. **Working memory affected under stress (treating
  psychiatrist report 13-Feb-2025)**" + AC1.
- **Q8** ← AC1 + the foreseeable-stressors box.
- **Q2** ← p2 grid: "**Understanding instructions: Normal**"; "**Carrying out instructions
  accurately: Normal**."

### THREE MORE FINDINGS ON THE FACE OF IT
1. p1: "Fit to commence the above from: 3 July 2026 **(continuation of existing arrangement)**."
2. AC3: "This reduced pattern of approximately six shifts per fortnight is the pattern Mr Shepherd
   has in fact **worked and tolerated over the past twelve months without deterioration**."
   (p1 table note: "continuation of the reduced pattern Mr Shepherd has sustained since 2025".)
3. AC4(c): "**return-to-work coordination and correspondence through the Injury Management team,
   Human Resources**" — the ECC recommended on 3 July what he now proposes at Part 7(e). The 31 July
   letters are signed by a **Director of Corporate Services**.

### COGNITIVE/RELATIONAL GRID — MOSTLY NORMAL
NORMAL: learning new tasks; initiating tasks independently; understanding instructions; carrying out
instructions accurately; executing tasks in reasonable timeframe; **working autonomously without
supervision**; prioritising tasks; making decisions; communicating with internal/external customers;
working in a team environment; supervising others ("Not a requirement of the AO3 role");
interacting appropriately with others.
RESTRICTED: maintain focus/concentration; multi-tasking; memorising information; working in a high
demand environment; handling conflict.

### ⚠️ TWO CORRECTIONS TO EARLIER ANALYSIS
1. **Q2 HAS AN INNOCENT ORIGIN.** The ECC p1 has a checkbox under "It is my opinion that they are
   fit to resume:" — "☐ **Workplace Performance Discussions**" — **left UNTICKED**. MSH is chasing an
   unticked box on its own form. The question as framed still overreaches and the premise is still
   false, but **the inference that a conduct process is contemplated is much weaker than previously
   recorded. Do not build on it.**
2. **Q1(c) WAS NEVER A FISHING EXPEDITION.** The ECC itself names "treating psychiatrist report
   13-Feb-2025". MSH has known a psychiatrist report exists since 3 July — from Cory's own document.
   Consenting to Q1(c) was right. ⚠️ NOTE: 13 Feb 2025 is also the date of the Mind and Memory
   Service report referenced in the QSuper correspondence. Same document. It is disclosed on the
   face of the ECC.
3. **Q1(a) has a legitimate origin too** — the ECC gives ONSET (18 June 2024), not date of
   diagnosis. So the question asks for something the ECC does not state. Still not necessary for
   adjustment purposes; but not baseless.

### OTHER DETAIL CAPTURED
- Diagnosis: **Major Depressive Disorder with anxious distress (DSM-5 296.23) — work-related
  psychological injury, onset 18 June 2024**. Matches the WC claim injury date exactly.
- Medications: fluoxetine 60mg mane; lisdexamfetamine (Vyvanse) 30mg mane; quetiapine 25mg nocte
  **ceased**. Functional consequence: limit nights to ≤2/fortnight; predictable rostering published
  in advance; **minimum 10-hour break between shifts consistent with the Award and fatigue risk
  management standards**.
- Dr Ma ticked BOTH "I have viewed the worker's Position Description (attached)" AND "I am aware of
  the requirements of their role" — he assessed against the AO3 RD.
- Form note: "**a separate medical certificate is also required to support the completed Capability
  Checklist**" — [ ] CHECK whether one was provided; if not, MSH may raise it.

### DOCUMENT UPDATED
Part 1.3 rebuilt as "THE CHECKLIST ALREADY ANSWERS MOST OF WHAT IS NOW ASKED" (question-by-question
mapping), and new **Part 1.4 "THREE MATTERS ON THE FACE OF THE CHECKLIST"** (continuation; twelve
months tolerated; the restriction matching MSH's own process). Summary item 5 rewritten.
Builder patched to render **bold** properly.

## 31 JUL 2026 — THE MISSING MEDICAL CERTIFICATE: VOLUNTEERED, NOT LEFT TO BE FOUND

Confirmed by Cory: **no separate medical certificate was provided with the ECC on 3 July 2026.**
The ECC form's own first line requires one: "Please note that a separate medical certificate is
also required to support the completed Capability Checklist."

**RISK ASSESSMENT — LOW, BUT REAL:**
- ⭐ **MSH has NEVER raised it.** Four weeks, five letters (7, 15, 29, 30, 31 Jul), six shifting
  bases — and not once. The 31 July letter treats the ECC as valid and seeks "further clarification"
  of it, not correction of a deficient document. Had the missing certificate been the problem, it
  would have been the first thing said.
- Trivially curable — a five-minute item from Dr Ma.
- But it is the ONE soft spot in the "I have cooperated throughout / they have not" posture, and it
  costs nothing to close.

**HANDLED BY VOLUNTEERING IT (Part 3.1, end):**
    "I also note that the Employee Capabilities Checklist form states that 'a separate medical
    certificate is also required to support the completed Capability Checklist.' One was not
    provided with the checklist on 3 July 2026. I will obtain one when I rebook with Dr Ma and
    provide it together with his answers. If the Health Service requires it sooner, please tell me
    and I will arrange it separately."
⇒ Acknowledges, commits, offers to expedite. Converts a latent weakness into another instance of him
being the reasonable party, and removes the card from their hand permanently.

⚠️ **DELIBERATELY NOT SAID: "you never raised this in four weeks."** That is BANKED. If MSH ever
attempts to rely on the missing certificate as a justification for the 3 July exclusion or anything
since, the four weeks of silence — while giving six other reasons — is the answer. Spending it now
would waste it; holding it means any late reliance on the point backfires.

Also added: GP note asks Dr Ma to issue a certificate covering the period from 3 July 2026 at the
rebooked consultation; send checklist updated.

## 31 JUL 2026 — ⚠️ CORY'S ACCOUNT: THE POSITION GIVEN AWAY, AND THE FEB 2025 PRECEDENT

**HIS ACCOUNT (UNVERIFIED — no documents sighted):**
1. His job has been advised and given to someone else.
2. Same manner as **February 2025**, when he returned and **Ms Taylor quickly put a full-time
   employee on**.
3. **Scott Hughes and Ms Taylor attempted to isolate him in a different department entirely.**

### WHY IT MATTERS
⭐ **It supplies the prior conduct that makes the Hughes conflict CONCRETE rather than structural.**
Earlier note recorded that "he is a potential respondent, not a bystander" was contingent on
documents being located. If Hughes was personally involved in an attempt to move Cory out of
Switchboard, he is a **participant in the dispute now deciding it** — materially stronger than the
org-chart conflict currently pleaded in Part 6.
- Also connects to the existing thread: the full-time position communicated to a casual (Caroline
  text screenshot, filed) and Cory's 14 Jul email to Heath.
- Feb 2025 is POST-injury (injury date 18 June 2024) ⇒ relevant to **ongoing detriment /
  aggravation and the general protections file**, not to s 32 causation.

### ❌ NOT IN THE 31 JULY RESPONSE
Unverified; an allegation of conduct; would let MSH answer that instead of the ten items it now
must answer. Same reasoning as the "threat" framing.

### ✅ WHERE IT GOES
- **Union brief (Petering / Moran)** — position backfilled + attempted transfer is core industrial
  territory, and with five weeks' exclusion it is a far bigger matter than the RFMI.
- **General protections / reprisal file.**
- **The conflict file** — as the concrete basis for Hughes's participation.

### ⭐ THE PROTECTIVE FACT ALREADY IN HAND
Both 31 July letters describe him as **"Permanent Full-time basis 76 hours per fortnight"** in his
substantive position — signed by Hughes. **A permanent appointment to that position would
contradict MSH's own letter of 31 July.**
⇒ **NEW PART 11 ADDED to the response**: asks MSH to confirm the position "continues to be held for
me, and that no permanent appointment to it has been made or is proposed to be made while I am held
out of the workplace." Neutral, unanswerable badly, and creates the written record now. Added to the
Part 10 response list as item 10.

### EVIDENCE TO ESTABLISH (do this week)
- [ ] Who said the job has been given to someone else — when, and in writing?
- [ ] **Is it on SmartJobs?** Public and checkable TODAY — screenshot with date visible.
- [ ] Is it a TEMPORARY BACKFILL against his position, or a PERMANENT APPOINTMENT to it? This
      decides how serious it is.
- [ ] **Feb 2025**: rosters, position numbers, or recruitment records showing the full-time
      appointment made when he returned.
- [ ] **The attempted transfer to another department**: any email, meeting invitation, proposed
      role description, or file note. Anything in writing at all.

## 31 JUL 2026 — CLARIFIED: THE POSITION WAS NOT ADVERTISED; COLLEAGUES ASKED IF HE WAS FIRED

Cory clarifies: the information came from **colleagues**, who asked whether he had been **fired**
and said another staff member has obtained his position. **It was not advertised.**

### CALIBRATION — THE ABSENCE OF AN ADVERTISEMENT LOWERS THE ALARM ON ONE POINT
A **permanent** appointment to an AO3 position in Queensland Health would ordinarily require
advertisement and a merit process. No advertisement therefore makes a permanent appointment LESS
likely, not more. Far more likely: someone acting in the role, a casual absorbing the shifts, or
roster reallocation. MSH's own 31 July description of him ("Permanent Full-time basis 76 hours per
fortnight") supports that his substantive position is intact.
⇒ Earlier advice to check SmartJobs is superseded — there is nothing to find. Record the negative.

### ⭐ BUT THE POINT THAT MATTERS IS MUCH BIGGER: THE WORK IS BEING DONE
If another employee is working his shifts, **the duties exist and are available**. That destroys
**Q9** before it is answered. MSH has asked his doctor to opine on a scenario in which it "is not
able to accommodate the restrictions" — while, on his account, the work is being performed by
someone else, five days a fortnight, for five weeks.
**An employer cannot say there is no work available when someone else is doing it.**

### PART 11 REFRAMED — three neutral confirmations sought
  (a) that the substantive position continues to be held; no permanent appointment made/proposed;
  (b) ⭐ **whether the shifts he would ordinarily work are being performed by another employee** —
      expressly tied to Q9: "If the duties I would perform are being performed by someone else, the
      work is available, and the premise of that question requires examination before it is put to
      anyone";
  (c) what, if anything, has been communicated within the workplace about his absence — "I raise
      (c) because my absence has been the subject of enquiry among colleagues. I would prefer that
      whatever is said about it is accurate."
⇒ No allegation, no reference to what colleagues said, nothing deniable. (b) is the one that does
the work.

### ⚠️ DO NOT SEEK COLLEAGUE STATEMENTS YET
Approaching colleagues while excluded risks being characterised as inappropriate contact and
exposes them. The clean routes to the same facts:
- **Rosters and AVAC/payroll records** — obtainable through the union, or through disclosure.
- **MSH's own answer to Part 11(b)** — which is why it is asked in writing now.

### THE REPUTATIONAL DIMENSION
Colleagues asking whether he was **fired** is itself a harm and evidence of how a five-week
unexplained absence is being read in the workplace. Part 11(c) records it neutrally. Fuller
treatment belongs in the union brief and the general protections file, not here.

## 31 JUL 2026 — CORY'S THEORY: THE WP LETTER FORWARDED → RFMI RUSHED BEFORE LEGAL REVIEW

Theory as put: Chloe and Scott working together; Scott, Corporate Services and Legal; the WP letter
to the appeal officer was forwarded so Legal could not review what Scott was finishing, which rushed
the sending.

### ❌ THE PART THE EVIDENCE CONTRADICTS
**"Scott and Legal working together" is NOT supported — the drafting evidence says the opposite.**
5 Jun objection: institutional third person, pinpoint Rule 64E(4) sub-provisions, submission
register, clean across 28 pp. RFMI: first person, "the provisions of", "cab be found out their
website", "Mr Shepherds", "fulfill", **he/their pronoun drift between adjacent questions**. Plus the
false premise, which **Ruttan cannot have approved** having drafted Item 20 addressing PID
24-ESU-1130 by reference number.
⇒ **Legal was not involved.** Record it that way.

### ✅ THE PART THAT IS COHERENT — AND TESTABLE TODAY
"Rushed before Legal could review" is consistent with Legal not being involved. It needs a trigger.

**⭐ THE DECISIVE TEST — ONE TIMESTAMP:**
Harrison's holding reply is filed at **30 July 14:33** ("progressing for delegate approval… unable to
guarantee").
[ ] **What time did the WP letter to Matheson go?**
- **Before 14:33 on 30 Jul** → theory stays open.
- **After 14:33 on 30 Jul, or on 31 Jul** → the holding reply PREDATES it, the RFMI was already in
  train, and the theory CLOSES.
Two minutes in the sent items. Record the time either way.

### ⚠️ EVEN IF THE TIMING WORKS, IT ESTABLISHES PROXIMITY, NOT CAUSATION
Three unproven links remain: (a) the Regulator forwarded it; (b) MSH received it before the RFMI
issued; (c) that caused Hughes to expedite. Identical structure to the 1 Jul → 2 Jul inference — a
pathway that exists but has not been shown to have carried anything.
**Same discipline: record the sequence, assert nothing.** A second inference built on the same
unproven pathway does not strengthen the first; asserting either weakens both.

### THE SIMPLER EXPLANATION STILL FITS EVERYTHING
**His own 28 and 30 July letters.** Documented, sufficient, no external pathway needed. Detailed
letter citing EB12, the Award and the policies → 29 Jul basis changes to WHS → 30 Jul they stop
answering → 31 Jul a formal process. Accounts for the sequence, the haste, and the absence of legal
review.

### ⚠️ AND "SO LEGAL COULDN'T REVIEW" IS A FURTHER, WEAKER INFERENCE
Rushing a document is not evidence of rushing it TO AVOID review. Equally consistent with perceived
urgency. Do not conflate the two.

## 31 JUL 2026 — ⭐ THE MATHESON TIMESTAMP: 10:46. AND MSH'S OWN LETTER CLOSES THE INFERENCE

Filed: documents/correspondence-2026/2026-07-31_1046_Cory_WP_material-development_to_Matheson_SENT.pdf
Subject: "WITHOUT PREJUDICE SAVE AS TO COSTS — WC/2024/227 Shepherd — material development".
To Renee Matheson only. **Sent Friday 31 July at 10:46 AEST.** 3 pp.

### THE MEASURED SEQUENCE (all AEST, Fri 31 Jul 2026)
| Time | Event | Source |
|---|---|---|
| **10:46** | Cory's WP letter to Matheson sent | the email itself |
| 11:10:27 | GP letter PDF created | PDF metadata |
| 11:11:02 | Employee letter PDF created | PDF metadata |
| 11:11:27 / 11:11:42 | Signature image applied (Fill & Sign) | recovered revision 3 |
| 11:43 | RFMI transmitted | covering email |

**24 minutes** email → first PDF. **57 minutes** email → transmission.

### ⛔ THE INFERENCE IS CLOSED — BY MSH'S OWN DOCUMENT
**30 July 14:33** — twenty hours EARLIER — Harrison wrote the request was "**progressing for
delegate approval**" and MSH was "**unable to guarantee**" when it would be available.
⇒ **The RFMI already existed on 30 July.** The 10:46 email cannot have caused a document that was
awaiting delegate approval the previous afternoon.
⇒ Corroborated by the revision analysis: **the text was final at PDF creation**. The Word documents
were complete before 11:10; the export was only the export.

For the 24 minutes to mean anything the chain would have to be: Regulator receives 10:46 → forwards
→ MSH receives, reads, decides to expedite → Hughes signs → sent 11:43. Inside 57 minutes, on a
Friday, on a document already at delegate approval. Possible; unproven at every link; and it would
explain only the timing of RELEASE, not the document's existence.

### ⭐ WHY THIS MATTERS FOR THE OTHER TWO
This is the **third** measured proximity identified today — 1 Jul → 2 Jul; 30 Jul → 31 Jul; and now
10:46 → 11:10. Each is real. Each needs the same unproven middle link (the Regulator passing
something to MSH).
**What distinguishes this one: MSH's own letter rules it out.** The other two remain open only
because nothing rules them out.
⇒ **Record this one as CLOSED.** Doing so protects the other two: a set of inferences in which one
has been tested and abandoned reads as observation. A set in which all are asserted reads as habit.

### ALSO NOTED — THE WP LETTER'S CONTENT (as sent)
Confirms the drafting recorded pre-compaction: does not revive the 1 July offer (lapsed 22 July);
the 2 July condition; the 3 July ECC; MSH's written acknowledgment of being "certified fit to return
to work effective from 3 July 2026"; four weeks without wages; leave debited; medical costs
self-funded; the deliberately ambiguous QSuper sentence ("At my direction earlier this year, my
income protection benefits were reduced to partial payments and subsequently stopped altogether, as
I had returned to work"); "**I therefore have no income from any source**"; and the 30 July
"progressing for delegate approval… unable to guarantee" admission.
⚠️ Note: it says the direction "has now continued for four weeks" — the RFMI response says five.
Both were accurate when written (28 days vs the fifth week). No inconsistency, but be aware of it.

## Session 1–2 Aug 2026 — the 3 August package built, verified and finalised
- EB12 cl 10.3 found (21-day decision, s 29 deemed refusal) → Part 7 constituted as a request,
  then split out as the standalone cl 10.3 instrument (s 27(1)(a) hours limb severed from (c)).
- cl 1.11 Stage 1 dispute notice built (process-identification, suspension question, RWA pay
  claim, Schedule 2 policy request); PS Act s 89 conflict letter to the CE (solo); appointments
  notice converted to confirm-then-rebook with 7-day backstop; response compressed 14→8pp with
  the 3pp Proposal for Return to Work split out. Package: 6 docs, 26pp, 5 emails, 0 placeholders.
- Strategy layer written: powers map, red team (+individuals, absent-lane audit), suspension/
  dismissal exposure (s 101 fork), s 19 duty-not-power, good-faith discipline, displacement
  pattern, psychosocial frequency, mention prep (+signals, date architecture), full-picture read
  (+2 addenda: employment 42%/63%, appeal 29%/68%).
- Corrections logged: 26 Jun origin; cl 3.9.1 is Schedule 3 only; ATT09 verified by page render;
  3 Oct 2025 (not 4 Oct) review request — and its only send BOUNCED as spam to both recipients:
  "no reply 10 months" SUSPENDED pending proof of a successful re-send (ask Cory).
- Next: send Mon 3 Aug; mention Fri 7 Aug (silent on employment; watch 7–10 Aug decision window);
  clocks per CURRENT.md.

## 2026-08-02 (cont.) — Matheson child-material confinement email drafted
- Established: the QPS occurrence number NEVER entered the record — offered 14 Jan 2024 (text) and
  3 Apr 2025 (email) but never supplied. Standing rule: keep it out of all correspondence.
- Instrument analysis: DFVP Act could not support a DVO/PPN against a 15-year-old in a family
  relationship → whatever police issued against the sister was non-DFVP (likely YJ Act caution or
  informal good-behaviour direction). Email therefore says only "no protection order was made".
- Drafted `drafts/MATHESON_CHILD_MATERIAL_EMAIL.txt`: confinement + non-reliance + QPP 11
  destroy/de-identify + redaction-on-tender + 14-day response. Non-accusatory (Matheson's request
  was proper; excess was in the supply). Legislation: DFVP s 159, IP Act QPPs 6/11, HR Act ss 25,
  26(2). HOLD until after 7 Aug mention; suggested send Mon 10 Aug. Verify pinpoints before send.
- Updated taylor-DFV-disclosure-to-Matheson.md to-do with number status + draft location.

## 2026-08-02 (cont. 2) — DFVP Act verified and filed as ATT25
- Downloaded the authorised DFVP Act 2012 consolidation (current 1 Jan 2026) →
  documents/instruments/ATT25_DFVP_Act_2012_current_2026-01-01.pdf; verified extracts at
  documents/instruments/DFVP2012_VERIFIED_EXTRACTS.md.
- s 22(2) VERIFIED: child respondent only in intimate-personal/informal-care relationships →
  a DVO or PPN against the 15-y-o sister (family relationship) was LEGALLY IMPOSSIBLE. The
  Matheson email's "no protection order was made" is corroborated by the statute itself.
- s 159 VERIFIED: child limb (1)(b)(iii) is the widest (bare "a child"); penalty 100 PU / 2
  years imprisonment; "publish" = to the public → prior inter-party disclosure is no breach;
  the section bites on public deployment. Posture unchanged: backdrop, not accusation.
- s 160 BANKED: no entitlement to DFVP court records — gate if MSH/Regulator ever seek the
  ex-partner order files.
- Matheson draft header updated: DFVP caveat discharged; QPP/HR Act numbering still to eyeball.

## 2026-08-02 (cont. 3) — CORRECTION: the 10 days DFVL-requested leave WAS taken
- Cory [A]: ~10 days taken after 14 Jan 2024 (helping his mother move; she went to NSW a week).
  My §4B line "no such leave was ever taken" was an overstatement of an open to-do — withdrawn
  and corrected in taylor-DFV-disclosure-to-Matheson.md.
- Corpus holds ZERO Jan–Feb 2024 messages; the leave coding exists only in MSH payroll.
- NEW OBTAIN: Jan–Feb 2024 leave/payroll coding. If coded A/L-S/L-rec after the written "10 days
  FDV leave (special leave)" text → the Taylor substitution was EXECUTED, not offered — first
  instance of the pattern. If coded DFVL → corroborates the DV character. Either resolves it.
- Cross-exam line adjusted: practical help with a family move, then five clean months, no
  treatment, no certificate. Never self-describe as "a stressor".

## 2026-08-02 (cont. 4) — Jan 2024 account refined [A]
- The sister's conduct was directed at the MOTHER (running away, returning, picking on her) —
  not at Cory. He had no party status at all: not aggrieved, not respondent — the supporting
  adult who attended at police direction and then helped his mother move (the ~10 days).
- s 22(2) check holds for mother-as-aggrieved too: mother–daughter is a family relationship →
  no DVO/PPN possible against the child whoever the aggrieved was. Non-DFVP direction was the
  only available instrument. Reference file account block updated.

## 2026-08-02 (cont. 5) — Standing suppression rule added (discipline rule 10)
- Cory's instruction: the Dec 2024 respondent status (Southport PPN, MAG-00196566/24(4)), its
  strike-out, and the service of the separation document are NEVER voiced in the WC or
  employment tracks — filings, correspondence, the mention, the Monday package, the Matheson
  letter. QPS-track/personal file only. Added as CLAUDE.md discipline rule 10.
- Verified before adding: full grep sweep of drafts/SEND_31JUL/*.txt and the Matheson draft —
  zero references to any of the three items. Package clean.

## 2026-08-02 (cont. 6) — Amended 9A does not plead 14 Jan 2024 [A]
- Cory: the 8 Apr 2026 amended 9A (Neville pleading) does not touch the 14 Jan 2024 event.
  Recorded in taylor-DFV file as superseding note; the "he put para 9 in issue" weakness becomes
  historical if confirmed. OBTAIN: the amended 9A text is NOT held in the repo — ingest it.
- Effect: the Taylor material is orphaned (tethered to a superseded particular) → the Matheson
  confinement letter's "no connection to any pleaded issue" becomes verifiable against the live
  pleadings. Residuals: superseded 9A usable on credit in cross; Stressor 1(a) roster generality
  could keep the rostering half factually adjacent.

## 2026-08-02 (cont. 7) — Occasion-vs-stressor frame recorded
- Cory: the pleaded stressor (if pleaded at all) was Taylor's ROSTERING DECISION — management
  action — not the family matter, which was only the occasion and should have been accommodated
  (DFV leave). Para-9 hook was the SOFAC, not the 9A — two documents; verify both on ingest.
- Consequence: family/police content was never relevant at ANY point — Matheson's narrow request
  itself recognised the boundary. Confinement letter position upgrades to "at no time relevant".
- s 32(5) discipline noted: pattern (Stressor 1(a)), not single-decision reasonableness.

## 2026-08-02 (cont. 8) — Slow-hour manner point banked
- Cory [A]: the 14 Jan 2024 roster-out occurred in a slow hour, not high call volume — undercuts
  the stated coverage rationale. Evidence would be switchboard call logs for that morning
  (MSH-held). NOT pursued while the event is unpleaded; banked in the taylor-DFV file.
- Tone discipline reaffirmed: insensitivity runs on substance (roster-out despite notice, quiet
  hour, entitlement substituted), never on her polite text wording.

## 2026-08-03 (send morning) — FINAL REROUTE per Cory, PDFs rebuilt
- Request (cl 10.3): To HR ONLY (LBH.HRTeam1); Taylor removed entirely. 21 days runs on HR receipt.
- RFMI Response (+ Proposal + Arrangements): To HR; Cc Injury Management (kept for the 7-day
  receipt chain — flagged DO NOT REMOVE), union Cc.
- Dispute: To Taylor AND HR; Cc union only; IM off.
- CE letter: unchanged — CE alone, no legal (Part 7A reasoning stands; advised against adding
  MSH Legal).
- All six PDFs rebuilt 3 Aug 09:2x AEST; pages 8/3/2/5/4/4 (26pp), metadata clean, headers
  verified by pdftotext. EMAILS_TO_PASTE_3AUG.txt updated with routing + rationale notes.

## 2026-08-03 (send morning, 2) — Two substantive additions per Cory, rebuilt
- Dispute §4(d): forward-pay limb added — permanent-line rostered shifts paid in full as they
  fall, until return OR the power is identified in writing; if the basis is the medical
  information, payment continues through the reasonable period (framed as the pay dimension of
  the cl 1.11.4 status quo).
- Request 2.1: the change sought now NAMED as ~0.6 FTE, the 12-month average actually worked,
  precise figure to be established from MSH's roster/payroll records. Consistent with the ECC
  "continuation of existing arrangement" and the no-reduction framing; substantive 76h line
  expressly preserved.
- Both PDFs rebuilt; pages unchanged (5pp request, 4pp dispute).

## 2026-08-03 (send morning, 3) — FULL FINALISATION RUN complete
- Built EMAIL_0..4 body PDFs (record copies) + ATTACHMENTS_STITCHED_all_six_documents_3Aug2026.pdf
  (26pp, send order, metadata clean) via new build_email_pdfs.py. Petering email updated: four
  numbered items (CE letter added), attachments = 13 Jul email + the stitched PDF.
- TRIPLE-CHECK SWEEPS (all PASS): placeholders none; rule-10/sensitive terms none (no Southport,
  MAG-, sister, ex-partner, QPS numbers anywhere); no wrong-year dates; 17/17 anchors hit
  (24 Aug, 0.6, line-not-varied, 1.11.2(a), forward-pay, s 89, option 1, 1(b), 7-day backstop,
  invoice 574370, controls...); phone+date on all six docs; stitched pack integrity confirmed.
- MONTE CARLO (calibrated to 1 Aug baseline, then final-package deltas only):
  employment strict 46→48 (+2.6) · employment favourable 64→66 (+2.7) · PAY RECOVERED 55→59
  (+4.6, the forward-pay limb's work) · appeal win 29 (unchanged) · appeal favourable 66 (±0).
  Conclusion: the weekend's edits bought pay-recovery points; the package remains at the
  drafting ceiling. SEND.

## 2026-08-03 (send morning, 4) — Petering withdrawn; receiver-clean pass
- Cory: Petering email NOT sending today — marked HELD in both files; union still sees all live
  via Cc on emails 1–3. EMAIL_0 record PDF removed.
- Combined pack renamed receiver-neutral: Shepherd_Documents_MSH-INJ-5795_3Aug2026.pdf (no
  "stitched" anywhere a receiver could read; wording in the held Petering draft also neutralised).
- Jargon sweep of the four MSH bodies: clean (only substring false-positives).
- FINAL metadata check across every attachable file: no Title/Author/Creator/Producer/Subject,
  Custom Metadata no, Metadata Stream no — on all six documents, the combined pack, and the four
  email record PDFs.

## 2026-08-03 (send morning, 5) — Four CE enclosures extracted, all attachments produced
- ENCLOSURE_A: RFMI 31 Jul GP letter p1 (Hughes signature page) · B: p3 (question 3) ·
  C: ECC 3 Jul p1 (certification + "continuation of existing arrangement", verified by page
  render — no text layer) · D: 2 Jul 2026 email (2pp origin document). All metadata scrubbed.
- Complete attachment set delivered to Cory: 6 documents + 4 enclosures (10 files).

## 2026-08-03 (send morning, 6) — CE named; her address found
- Letter and email now addressed to Ms Noelle Cridland by name (she signed the 5 Jun objection
  as CE — the name was already established in the record).
- Address: MetroSouthCorro@health.qld.gov.au — the PUBLISHED Office of the Chief Executive
  correspondence address (MSH executive-team page via search). Direct address
  noelle.cridland@health.qld.gov.au is the QH convention but UNVERIFIED — optional second
  recipient; if it bounces the Corro address still lands (Oct 2025 bounce lesson applied).
- Email body asks her office to bring it to her personal attention, citing s 89's direction to
  the chief executive. Letter PDF + EMAIL_4 record rebuilt, verified, metadata clean.

## 2026-08-03, 11:38am — ⭐ THE PACKAGE IS SENT
- All four emails sent 11:38am AEST. Outlook exports filed at documents/sent-2026-08-03/ with
  as-sent attachments (md5-verified identical to drafts/out builds).
- As-sent routing: E1 To IM, Cc lbh_hr+Moran · E2 To IM+lbh_hr, Cc Moran · E3 To Taylor+IM+
  lbh_hr, Cc Moran · E4 To cridland direct (unverified), Cc MetroSouthCorro (published).
- CLOCKS ARMED: Tue 4 Aug Stage 1 (24h) · Fri 7 Aug mention (SILENT) + RFMI 7-day end ·
  Mon 10 Aug Stage 2 referral (one line, manual) + Matheson child-material letter ·
  Mon 17 Aug Stage 2 ends · ⭐ Mon 24 Aug cl 10.3.6 decision due / s 29 deemed refusal.
- Follow-ups: forward the four sent items to Petering (she was not in Cc — Moran only);
  watch for bounce on cridland direct (Corro lands regardless); rebook consultations on MSH
  confirmation or day-7 silence; obtain + HOLD Dr Ma certificate.

## 2026-08-03, 12:45pm — ⭐⭐ CE RECEIPT ACKNOWLEDGED AT CRIDLAND'S PERSONAL DIRECTION
- 67 minutes after send, Metro South Corro (Mark, Executive Services): "I have been asked by
  Noelle Cridland, Health Service Chief Executive to acknowledge receipt of your correspondence."
- Filed: documents/sent-2026-08-03/2026-08-03_1245_MSH_Corro_ACK_CE_letter_at_Cridlands_direction.pdf
- ESTABLISHES: (1) the direct address Noelle.Cridland@health.qld.gov.au is VALID — no bounce,
  bounce-watch closed; (2) the CE PERSONALLY received the s 89 disclosure same day and directed
  the acknowledgment — her personal knowledge is now documented BY HER OWN OFFICE, dated 3 Aug
  12:45; (3) the s 89(1)(b) bar now operates on documented personal knowledge — the element the
  ledger listed as completing "on any answer" partially completed on the acknowledgment itself.
- NO REPLY NEEDED to the acknowledgment. The five questions in the letter remain outstanding —
  their answers (or silence) are the next record.

## 2026-08-03 — Cory's read: can Cridland even reply, given her own 5 June signature?
- Refined analysis: her signing the K-LM26/729 objection is an OFFICIAL act — an institutional
  role-tension, not a s 89 "personal interest" conflict, so she is not legally disabled from
  performing the s 89 function. She can answer, or delegate (HHB Act delegation powers).
- BUT the structural point stands and is banked: she cannot engage with the letter's substance
  (esp. anything touching Q1(b)/litigation advantage) without her own signature being in the
  frame. Branch map: answer → documents; delegate outward → concedes the layered conflict and
  takes the matter outside the CE line (extraordinary, favourable); silence → five s 89
  questions outstanding at CE level on DOCUMENTED personal receipt (12:45 ack).
- Every branch favourable. Nothing for Cory to do. If the response ever comes from the Board or
  the Department instead of MSH, that is the strongest possible tell — note it immediately.

## 2026-08-03 — CRIDLAND-END full-picture evaluation written
- skill/references/CRIDLAND-END-full-picture.md: her complete stack (appeal, 64G+her objection
  signature, PID knowledge, Calderbank, exclusion, RFMI Q1(b), today's four docs, 12:45 ack);
  the honest adviser brief (6 points, incl. withdraw Q1(b) and take the s 89 exit); her likely
  conclusions ranked 1–6; her personal calculus (two signatures — easiest exit = his best
  outcome, by design); watch-for signals list for the week.

## 2026-08-03 — Hazard nomination banked (decision-making = organisational justice)
- skill/references/HAZARD-NOMINATION-decision-making.md: the ready position for nominating
  "poor organisational justice — the decision-making processes" as the cl 7.2 hazard, WITH the
  six dated data points, at the Stage 1/2 discussion or assessment consultation. NOT sent cold —
  ask-for-the-assessment discipline preserved.

## 2026-08-03 — Stage 1 script banked
- skill/references/STAGE1-SCRIPT.md: opening statement, the eight asks in meeting order, the
  verbatim hazard framing (organisational justice + job insecurity, quoting THEIR "line
  management" phrase to reach all of Corporate Services without naming anyone), scripted
  answers to their four likely questions, meeting discipline, after-meeting file-note rule.

## 2026-08-03 (evening) — 28–30 July thread re-analysed on Cory's paste
- ⭐ SECOND ASYMMETRY ADMISSION: 30 Jul 14:33 Harrison — RFMI "progressing for delegate
  approval... unable to guarantee when the approved documentation will be available for release"
  → issued next morning 31 Jul 11:41 WITH a 7-day deadline on Cory. Pairs with 15 Jul "unable
  to commit to a timeframe". Two dated instances: no timeframe for themselves, day-counts for him.
- DELEGATE EXISTS: the RFMI went through "delegate approval" — an approval record with a name
  and date exists in their system. Discovery/asks target. Undercuts any "no decision-maker" line.
- ⚠ POSSIBLE EARLIER cl 10.3 CLOCK: the late-June request to temporarily reduce 0.6→0.5 was
  cited in his own 30 Jul email §4.2 with the cl 10.3 21-day framework, and MSH never decided
  it. IF the June request met s 27(2)/cl 10.3.3 form (writing/detail/reasons — UNVERIFIED),
  a deemed refusal may already have occurred ~mid-late July. Do NOT rely; the 3 Aug request is
  the clean clock (24 Aug). VERIFY: locate the June request's form/text in the record.
- TOMORROW IS A DOUBLE MARKER: Tue 4 Aug = Stage 1 24h "should" AND expiry of the 28 Jul
  letter's own "5 business days" response window (28 Jul + 5 = 4 Aug). Silence = two logged items.
- Enforceability audit of the July thread: the 5-day window and §10 asks carried no machinery
  (record-builders only). Directive 12/24 special leave is binding but needed a channel — now
  has one (the dispute). The 31 Jul written costs commitment became enforceable footing on
  acceptance (3 Aug arrangements notice). Their statements now banked as admissions: 15 Jul
  no-timeframe · 29 Jul WHS-as-power framing ("independent obligation") · 30 Jul no-guarantee +
  "usual process is for approved RFMI documentation to be sent directly to the employee" ·
  delegate-approval existence.

## 2026-08-03 (close of day) — Full picture 3 Aug written; sources-text mirror added
- skill/references/FULL-PICTURE-READ-3AUG.md — send-day field state: day-1 events, clocks table,
  five new established items, calibrated numbers (48/66/59/28/66), week decision points, risks.
- evidence-index/sources-text/2026-07-30_1433_Harrison_holding_reply_FULL.txt — full-text mirror
  with banked key facts (asymmetry pair, delegate record, "usual process", Solv/IPEC cc).

## 2026-08-03 — Matheson 07:17 reply filed + assessed
- 2026-08-03_0717_Matheson_reply_disclosure_list_and_NNPD_commitment.pdf: replying to Cory's
  24 JULY disclosure-list request (10 days), 7:17am Monday — BEFORE his 11:38 send. Three
  sentences: apology for delay + commitment to updated list of documents AND NNPD (Form 29
  non-party disclosure) COPIES "as soon as possible this week".
- What she responded to: the procedural records request ONLY. What she put aside: the 31 Jul
  WP material-development letter (unanswered in any channel), the reconsideration invitation,
  the continuing-detriment point, the conferral offer.
- Read: pre-mention decks-clearing / covering the Regulator's procedural side so Friday shows
  compliance. WP silence 4 days pre-mention = normal carriage discipline; real tell is Friday's
  64G posture.
- ⭐ VALUE: the NNPD copies commitment — the Respondent's own Form 29s + documents produced =
  window into their evidence base. DIARISE: if list+copies not received by Thu 6 Aug EOD, do
  NOT chase pre-mention; the commitment is on record and speaks for itself if disclosure comes
  up Friday.
- WP letter export was byte-identical to the filed SENT copy — duplicate discarded.
- CORRECTION: the two WP-letter PDFs were same size but NOT byte-identical (differing md5s —
  likely export timestamp). Same letter content on inspection; the original SENT proof filed
  31 Jul is retained as the service copy. If a byte-exact export ever matters, re-file Cory's
  Outlook_Document165 export alongside it.

## 2026-08-03 — The QSuper/IP premise: closed loop confirmed [A]
- Cory confirms the elements: (1) notifications to fund/employer May 2025, Feb 2026, 3 Jul 2026;
  (2) benefits stopped from 1 Jun 2026 at his direction (working); (3) ⭐ an OVERPAYMENT was
  identified and he ACCEPTED it (repayment/acknowledgment) — the fund's own accounting that
  benefits were NOT payable because he was working; (4) ongoing engagement via Zappia/ART, whom
  MSH itself emailed directly (15 Jul email to Cory AND Zappia).
- ⇒ FORENSIC IMPOSSIBILITY: MSH's 13 Jul coding premise ("current QSuper IP claim → no pay per
  our guidelines") cannot coexist with the fund's overpayment position (benefits not payable
  because working). Both cannot be true; MSH's premise is the one contradicted by the fund's
  own records and by three dated prior notifications.
- DISCIPLINE: never "false claim" on paper — always "a decision made on an incorrect factual
  premise, corrected in advance, in writing, on three dated occasions." The word false invites
  a bad-faith fight; the impossibility needs no adjective.
- OBTAIN (via Zappia): ART/QSuper benefit-cessation confirmation (from 1 Jun 2026), the
  overpayment notice + Cory's acceptance/repayment record. These are the two exhibits that
  end the point wherever it's raised. File to documents/ when received.
- Already deployed: dispute §4(d) (which guidelines + neither-wages-nor-benefit); WP letter to
  Matheson (no income from any source); Petering appeal-window question (HELD — send with the
  forward of the four sent items).

## 2026-08-03 — Lane separation + the fit/unfit tension flagged
- Standing frame: the fund lane (QSuper/ART, via Zappia) is Cory's lane; the wages lane is
  MSH's under the instruments. If MSH runs the IP premise again, the one-sentence answer:
  "My arrangements with the fund are between me and QSuper; my pay is between me and my
  employer under the agreement." Never argue fund detail with MSH.
- ⚠ STRATEGIC TENSION to manage with Zappia BEFORE any future fund claim: the employment
  record says certified FIT (ready-willing-able); an IP claim asserts incapacity. If dismissal
  ever occurs and the fund path revives, sequence and framing need advice so a benefit claim
  never undercuts the employment/appeal record. Also check with Zappia: continuation of
  insured cover if employment ends (policy terms), so the safety net is confirmed BEFORE it
  is ever needed.
- The clean overpayment history preserves the fund relationship as the intact safety net —
  part of why addressing it promptly mattered.

## 2026-08-03 — CORRECTION [A]: certification history
- Cory: the 3 July 2026 ECC is the ONLY certification that has ever existed — no certification
  of any kind before it. And his PSYCHIATRIST ADVISED AGAINST working; he worked the reduced
  pattern regardless, sustaining it from his own leave.
- ⇒ My earlier "fit-vs-unfit tension" framing OVERSTATED the problem: the record is not
  "always fit". It is: real incapacity (partial IP benefits, psychiatrist caution), work
  attempted against advice, certification obtained 3 July when demanded. A coherent, honest
  arc — prior benefits consistent with partial incapacity; ready-willing-able needs fitness
  only FROM 3 JULY, exactly when the certificate exists. The wage claim is untouched.
- ⭐ Appeal upside: worked against medical advice = anti-malingering evidence + severity +
  explains leave patterns as genuine. The opposite of the exaggeration narrative.
- ⚠ CAREFUL SPOT: the psychiatrist's CURRENT view vs the GP's ECC. RFMI questions to the
  psychiatrist (Q7, 1(a), 1(d), 8 per the allocation) will surface his present opinion. Before
  the rebooked consult, Cory should understand — not shape — what that opinion now is. If the
  treater's honest current view is that work (even restricted) is harmful, strategy must
  accommodate that truth; ready-willing-able cannot be run against your own treater. Discuss
  openly at the consult; Report A scoping (current capacity/adjustments only) already fits.

## 2026-08-03 — QPS-track Case Study report read (14 Jul 2026, CO-25-2722/QP2500332406)
- Cory shared the full 25pp QPS/CCC complaint + exec summary + navigation guide. READ, not
  filed here — parallel-tracks discipline: it lives in the QPS repo side. Pointer only.
- Two anchors overlap the employment track legitimately and are ALREADY known to MSH from its
  own records: D17 (8 Oct 2024 abandonment decision, S. Johns A/ED LBHS) and D18 (E. Bain HR
  chain confirming return to work 7:00am Mon 24 Feb 2025, Logan lobby). The REASON the 24 Feb
  return was missed is QPS-track and stays out of all WC/employment correspondence (rule 10
  family). The employment file needs only: a return was confirmed for 24 Feb 2025 and did not
  proceed; MSH's own records show what it did next.
- Context now fully understood: the "worked against psychiatrist's advice" year (2025) ran
  through homelessness, criminal process, property seizure and family displacement — while he
  built both files. No action items for this repo from the report itself.

## 2026-08-03 — Chronology shield banked
- skill/references/CHRONOLOGY-SHIELD-post-injury-events.md: the defence if the Regulator pulls
  the QPS/personal story into the appeal. Core: diagnosis 24 Oct 2024 PRE-DATES the first
  personal event (1-2 Dec 2024) — post-onset events cannot cause onset on a liability appeal.
  "Put a date on it" answer to undated blurring; NNPD clinical records flagged as the primary
  entry vector (check date ranges when the list arrives); completeness doctrine if they open
  the door; Report B instruction; rule-10 and never-volunteer discipline restated.

## 2026-08-03 — Pre-injury fragment defence added to the shield
- Cory's flag: the Respondent will try to run the Jan 2024 DFV-leave matter (pre-injury) in a
  different, undated context — and the sister's pregnancy as innuendo. Added Part 7 to
  CHRONOLOGY-SHIELD: their knowledge gap (they hold fragments, not the benign truth), the
  relevance-first defence (one January morning + five clean months before injury ≠ dilution),
  the short protective true account if the door opens (name no one), the s 159 child gate,
  completeness (their own screenshots rebut), and the pregnancy = her event, no evidentiary
  foundation. VERIFY on NNPD arrival: whether any 2024 clinical note touches the family matter.

## 2026-08-03 — Respondent playbook banked
- skill/references/RESPONDENT-PLAYBOOK-appeal.md: the twelve standard tactics (s 32(5) RMA,
  major-significant dilution, pre-existing, credit, perception-vs-events, expert contest,
  fragmentation, onus, attrition, personal-story narrative, witness denial, settlement
  squeeze) each mapped to the counter already built. Honest correction recorded: the statute
  itself makes competing causes relevant — the frame is "the comparison is won on documents",
  not "other things don't matter". Over-reach analysis: their hard personal-story play is
  high-risk for them; sanitised expert line is the real threat → the dating cross is the most
  important prepared question in the appeal.

## 2026-08-03 (late) — [A] Stressor inventory, Cory's own words, to capture properly
- His list tonight, verbatim spine: "the wage withheld · PT [patient] safety · the PID · the
  rostering errors · everyone managing through their leave · the tearing out paper · the
  screaming." NONE of it his choice — the choice asymmetry frame.
- ⚠ Corpus check: "screaming" and "tearing out paper" incidents appear NOWHERE in the corpus
  or synthesis — they live only in memory. They belong in HIS WRITTEN ACCOUNT (the standing
  to-do that already covers 7am 24 Feb 2025 — widen it): each incident with approximate date,
  place, who was present, what was said/done, and any document/witness that could anchor it.
  [A] working-theory until anchored; NOT for filings; primary use = Report B history +
  evidence-in-chief reservoir + the hazard data set.
- Frame banked: every stressor was someone else's act; every response of his was lawful and
  procedural. "I didn't choose any of it" = the agency asymmetry that underwrites both the
  injury narrative (things done TO him) and the credit contrast (what he did about it).

## 2026-08-03 (late) — ⭐ LEGAL STANDARD CORRECTED: "a significant", never "major"
- Cory caught me applying the REPEALED standard. Verified against the authorised WCRA
  consolidation (downloaded, filed as documents/instruments/ATT26_WCRA_2003_current_2025-01-01.pdf,
  current 1 Jan 2025): s 32(1) — "personal injury arising out of, or in the course of,
  employment if the employment is A SIGNIFICANT CONTRIBUTING FACTOR to the injury." No "major"
  anywhere in s 32; the 2013 psychiatric "major" test was repealed in 2019.
- Corrected in: RESPONDENT-PLAYBOOK (tactic 2 + correction section rewritten), CHRONOLOGY-SHIELD
  (2 instances), taylor-DFV §4B (1 instance), CLAUDE.md standing rule added.
  medical-causation-framework.md already had it right — recent files contradicted it; standing
  rule now prevents recurrence.
- CONSEQUENCE: the dilution tactic is much weaker than my analysis assumed — competing causes
  can coexist; the Respondent must show employment was not significant AT ALL. Cory's "the work
  case is significant regardless of what else is going on" is the correct statement of the
  current law. Appeal-win estimate should nudge UP on the corrected standard (28 → low 30s;
  re-run properly after Report B).

## 2026-08-03 (late) — Full picture re-run on the corrected significant test
- Appeal win at hearing 28→36; appeal favourable 66→70; employment/pay unchanged (48/66/59).
- Contested centre shifts to s 32(5) RMA; Report B re-scoped accordingly (significance +
  manner, not outweighing). Addendum appended to FULL-PICTURE-READ-3AUG.md.

## 2026-08-03 (night) — [A] The patient-safety report: the breaking point, and their anticipated excuse
- Cory: the most stressful thing = the hospital never moved on his PATIENT-SAFETY report. "That
  was the end after the PID — my last full — I had enough." The PID/PT-safety non-response is
  the subjective breaking point, proximate to the Aug-Oct 2024 sequence (PID 30 Aug → no action
  → abandonment 8 Oct → diagnosis 24 Oct). BELONGS IN: Report B clinical history (the breaking-
  point sequence, his own words) + the PID track (substance-never-investigated question). NOT a
  new front now.
- ⭐ THE ANTICIPATED EXCUSE, PRE-ANSWERED: if MSH ever says "no investigation because he became
  too unwell to give further information" — that is an admission stack, not a defence:
  (1) investigation duties on a patient-safety matter are INSTITUTIONAL (clinical governance /
  PID handling obligations / WHS) and do not depend on the reporter's continued availability —
  the information already given must be assessed on its face; systems exist independently of
  the discloser; (2) the excuse concedes KNOWLEDGE of his unwellness; (3) it relies on the very
  harm the workplace caused as the reason for not investigating what he reported — circular,
  self-serving, and it leaves the reported hazard unassessed (joins the 7 Jul unassessed-hazard
  pattern). Counter lives here until the PID track sequences.
- The later question for the PID channel (sequenced BEHIND WC settlement, never now): "Separate
  from the reprisal determination of 24 Dec 2024 — was the SUBSTANCE of the disclosure ever
  investigated, by whom, and with what outcome?" One sentence, devastating, correct channel only.

## 2026-08-04 — ⭐ CONFIRMED: the non-investigation IS pleaded (upgrades last night's caveat)
- Amended 9A (8 Apr 2026), Stressor 1: (a) Dereliction of Clinical Governance; (c) Refusal to
  Investigate WHS & Fatigue Complaints; (e) PID; (f) Immediate Reprisal. The PID↔patient-safety
  link via non-investigation is ALREADY PLEADED. The anticipated "he was too unwell" excuse, if
  ever written, lands on pleaded particulars 1(a)+(c) directly — no amendment needed.
- Discipline UNCHANGED (case-theory-synthesis): 1(e)/(f)/(g) stay NON-load-bearing — the spine
  remains Stressor 3 (fatigue/Neville/Mahaffey) + 1(a); the non-investigation material runs in
  the GOVERNANCE register (1(a)/(c)), never the reprisal register, to avoid the
  personal-campaign framing Willson wants.
- Also consistent: the 13 particulars contain NO 14 Jan 2024 item — corroborates Cory's account
  that the amended pleading does not touch that morning.
- Report B history instruction updated: the breaking-point sequence (report → silence → "I had
  enough" → diagnosis, Aug–Oct 2024) anchors to PLEADED stressors 1(a)/(c)/(e).

## 2026-08-04 — Disclosure-as-signal read + Calderbank #3 trigger
- Disclosure is never itself an offer (compliance, not negotiation) — but its MANNER can signal
  a resolution posture. PRE-OFFER SIGNALS to log: list arrives complete + on time + NNPD copies
  fulsome · any cover wording touching conferral/s 552A/"the parties' positions" · anything WP
  alongside or shortly after · Friday: consent/narrowing + any conciliation mention · Willson
  unbriefed again · delivery timed near 24 Aug. COUNTER-SIGNALS: late/partial/redacted list ·
  full-width fight Friday · an IME referral notice (building for hearing = opposite signal).
- ⭐ REFRAME (the standing architecture): the disclosure completing is the condition precedent
  for HIS next move, not theirs — "settle on the enlarged record" = Calderbank #3, timed AFTER
  the list + the mention + ideally 24 Aug (deemed refusal in hand), with Report B if available.
  Don't wait to receive an offer; the list arriving is the cue to start building one.
- If an approach comes first: standing rule — no response without the settlement architecture
  prepared (deed scope = compensation claim ONLY, rule 9; employment track stays separate).

## 2026-08-04 — Hypothesis: MSH may have ALREADY given the Regulator the 64G material
- Cory's hypothesis: the rosters/payroll/records he seeks from MSH via the 64G may already sit
  in the Regulator's file — produced by MSH through the Regulator's own NNPDs or conferencing.
- ONE INSTANCE ALREADY CONFIRMED: the Item 20 pattern — MSH's 5 Jun objection asserted "does
  not exist" while the Regulator's file held the McGinley routing (MSH-produced, Jul 2025).
  The pattern exists; the question is its extent.
- ⭐ THE CHECK (when the list + NNPD copies arrive this week): CROSS-REFERENCE every list entry
  against the 64G items — build a two-column map: 64G item ↔ Regulator-held equivalent (source,
  date). Three findings possible: (1) overlap → MSH resisting production of material already
  produced = oppression objection collapses + model-litigant contrast + Regulator's disclosure
  duty delivers the records to Cory regardless; (2) no overlap → hypothesis dies cheaply;
  (3) partial → the map shows exactly what remains worth fighting for Friday.
- MENTION CONTINGENCY: ONLY if the list arrives before Friday AND shows overlap — a measured
  procedural note is legitimate ("some categories appear to have been produced to the
  Respondent; production to the Appellant cannot then be oppressive"). Goes to the 64G scope
  question, NOT employment. If the list hasn't arrived: nothing changes, posture unchanged.

## 2026-08-04 — Read: they don't want Friday. Pre-mention approach discipline banked.
- Supporting signals: MSH no-show at the 22 May mention; Willson unbriefed same; objection run
  on papers; RFMI 7-day deadline lands ON mention day; the Regulator's decks-clearing Monday.
- What not-wanting-it produces: (a) a pre-mention consent/narrowing proposal, (b) thin/phone
  appearance, (c) on-the-papers request, (d) adjournment attempt.
- ⛔ DISCIPLINE if a pre-mention approach comes: informal "we'll provide X if you don't press
  the order" = DECLINE POLITELY. Orders or nothing — only ORDERS carry the timetable and the
  produce-or-swear alternative. Consent orders at the mention are the win condition; informal
  promises are the objection surviving in disguise. Any proposal: respond considered and fast,
  agree to CONSENT ORDERS on full items gladly, trade nothing narrow-for-full without analysis.

## 2026-08-04 — Known-item completeness test built (pre-arrival audit tool)
- skill/references/KNOWN-ITEM-completeness-test.md: Tier 1 must-appear (provably Regulator-held:
  Taylor's 7 attachments, McGinley, NNPD returns, conferencing records, his served documents,
  the 69983 file) · Tier 2 proves-the-channel (MSH-sourced 64G categories, Jul 2026 employment
  material, leave/DV/QSuper items) · Tier 3 cross-audit (employment-track production impeaches
  any "complete" appeal list that lacks the same documents) · the two-column 64G map · rules
  (name the missing document; a list is a representation; no volume of disclosure discharges
  an order except compliance).
- Cory's two scenarios both covered: tactical/curated disclosure → caught by named gaps +
  order still pressed Friday; genuine give-up → map shows overlap, records land, Regulator
  re-prices → settlement branch. Either way the disclosure materially feeds the appeal because
  the 64G/9A machine routes whatever arrives onto pleaded particulars.

## 2026-08-04 — The quarantine spot and its three exits (Item 20), s 65 verified
- The spot they'll still fight in a give-up: ITEM 20 — institutional-response / PID-handling
  records (implicates, not embarrasses; "does not exist" already burnt).
- Exit 1 RELEVANCE ("that's the reprisal complaint, not this appeal") → answer: pleaded 9A
  Stressor 1(a) Dereliction of Clinical Governance + 1(c) Refusal to Investigate — the handling
  of his complaints IS an operative stressor; records go to real-events + s 32(5) manner.
- Exit 2 PID CONFIDENTIALITY → ⭐ VERIFIED against ATT23 (current 30 Aug 2024): s 65(3)(c)
  expressly permits disclosure "for a proceeding in a court or tribunal"; s 65(3)(d) permits it
  with the written consent of the person the information relates to (largely HIM — offer
  consent on his own information); s 65(5) identity protection exists for the DISCLOSER's
  benefit — his to waive. The confidentiality door has a statutory exception built in.
- Exit 3 LPP → legitimate only for genuine advice; the routing/factual handling records are
  not advice; privilege must be claimed ITEM BY ITEM on affidavit — which itself confirms the
  documents exist (kills "does not exist" permanently either way).
- If wholly quarantined anyway: the same records remain reachable via the employment track
  (s 89 answers, Stage 2), the PID channel, and RTI — quarantine delays, never defeats.
- THE TELL: whichever single item they fight hardest for is the map of where the harm is.

## 2026-08-04 — The thesis statement, in Cory's words
- "They never investigated. My entire Form 29 IS the investigation. And they dismissed me after
  I fell apart from it." Banked as the case's organising truth: the 64G is the shadow
  investigation — each item a question the ESU/governance should have asked in 2024; produce-
  or-swear the powers an investigator would have had; the 9A its terms of reference; the QIRC
  the room it finally gets held in. Consequence of their non-investigation: NO contrary
  institutional findings exist anywhere — the only completed inquiry into these events is his.
- Sequence for Report B history + closing: report → no investigation → he broke (diagnosis
  24 Oct 2024) → the institution treated the breakdown as the problem (8 Oct abandonment;
  2026 exclusion) — punished for the symptom of their failure. Governance register, always.

## 2026-08-04 — [A] Working theory: Hughes as the "clean officer" who acquired the conflict
- Cory's read: Hughes was routed the decisions BECAUSE he looked unconflicted (the 13 May 2024
  PID named Taylor AND Reese, not him) — and "he has now acted on this". Supported by the
  record's shape: Hughes appears as decision-maker from ~Feb 2025 (DV-leave handling, Sept 2025
  performance plan, 2026 exclusion decisions, RFMI signature) — exactly the period after the
  ESU determination (24 Dec 2024) made Taylor/Reese untouchable as deciders.
- The flaw in their arrangement (the seam the s 89 letter probes): un-named ≠ unconflicted.
  Hughes supervises the named persons, answers for the unit's management, and each adverse
  decision in a PID-affected matter ACQUIRED him the conflict they assumed he lacked. If no
  s 89 assessment/authorisation was ever documented for that routing, the conflict-management
  choice itself is the governance failure — cl 1.2 Code, undocumented.
- Knowledge = exposure: PID s 40 reprisal analysis attaches to decision-makers WITH knowledge;
  Hughes sits at the information junction (ESU determination, unit facts for the objection,
  the 24 Feb 2025 7am lobby return he was part of). What he knew when is exactly what the
  delegate-approval record, the s 89 answers, and Item-20-adjacent material reveal.
- DISCIPLINE unchanged: never on paper as theory/motive. The questions already sent (who
  decides · what conflict identified and managed · does a s 89(2) authorisation exist) surface
  it structurally. [A] until documents date his knowledge.

## 2026-08-04 — RFMI letters read in full; ⭐ the extension valve
- Employee letter, operative sentence: "If you do not return the document within this timeframe
  OR SEEK A REASONABLE EXTENSION, I will make a decision..." — the letter's OWN TERMS make an
  extension request defeat the decision trigger. Cory sought the extension 3 Aug → the 7-day
  trigger condition is NOT MET by the letter's own words. Any "7 days passed" decision now
  contradicts the letter it purports to enforce. Banked for the dismissal-scenario answer.
- Q2's tell: premise "the Health Service is not aware of any concerns being raised for
  appropriate management" (contradicted by their own 7 Jul letter + the record) sits beside
  asks whether he can "follow a reasonable and lawful direction" and "participate in
  discussions in relation to his workplace performance and/or conduct" — discipline-adjacent
  destination revealed while its predicate is denied. Non-medical questions to a GP.
- Register read: aggressive in intent, weak in execution — template assembly, typos ("cab be
  found out their website", "bases", broken Q2 grammar), compound questions, "primarily" leak
  (C5), duties-cited-as-powers (WHS ss 17/19 + G3). Q1(c) asks the GP to rate his own
  patient's reliability; Q3 asks medicine to certify the conflict away; Q6 asks if he can work
  with NO adjustments (against G3's own premise); Q9 invites manufactured unfitness ("if we
  are not able to accommodate... is he able to safely return").

## 2026-08-04 — The 31 Jul 15:15 Harrison email filed; before/after pair complete
- 15:15 Fri 31 Jul — 75 min after the 2pm appointment slot: "ACTION REQUIRED | Request for
  Reimbursement". Answers the 30 Jul reimbursement request (28h old) ONLY after the appointment
  window passed. Content: "more than happy to assist" BUT a NEW gate — the Medical Centre must
  email MSH DIRECTLY with invoice + remittance "before we can proceed", despite his receipt
  (N471065713633) already provided as 30 Jul Attachment 3.
- SIGNALS: (1) held-until-after timing — the $150 friction answered only once it could no longer
  deter attendance; (2) ⭐ the gate opens a DIRECT MSH↔practice channel on the same afternoon
  the RFMI was to be handed over — [A] both readings live (anti-fraud pedantry vs engineered
  contact); (3) at 15:15 they did NOT yet know he cancelled — the email is the machine assuming
  the trap had fired (they learn of the cancellation only in his 3 Aug response); (4) same
  ACTION REQUIRED template as 11:43 — same production morning.
- Voice: mostly voice-one admin ("more than happy to assist") with one inserted procedural gate
  ("however, we also require...") that reads instructed. Mixed authorship consistent with the
  two-voices pattern.
- HANDLING: when rebooking with the clinic anyway, one confined line: ask accounts to email the
  invoice-574370 payment confirmation to lbh_InjuryManagement — PAYMENT DOCUMENTS ONLY, no
  clinical information, no records authority. The gate gets complied with narrowly and logged
  as friction instance #3 (his $150 needs practice-direct email; their commitments float).

## 2026-08-04 — Is the playbook systemic? [A] read + the Petering question
- Fingerprints of PRACTICE (not improvisation) in the record: the RFMI/ECC/EAF template
  machinery (templates exist for repeated use); the abandonment mechanism (deployed 8 Oct 2024,
  A/ED-signed); the SAME leave substitution by two managers 14 months apart (trained move, not
  personality); "Health Management processes" as a named internal pathway; the Solv/IPEC case
  platform (industrialised); EB12 cl 7.1.5's bargained commitments re "management of ill or
  injured employees" (bargaining fossils = the union has seen this terrain before).
- NOT established: comparative files (no evidence others went through the pipeline). Never
  alleged to MSH. The lawful windows into it: the cl 7.2 assessment + Code data sources
  (complaints, absence, turnover, EAP usage) + dispute §4 asks.
- ⭐ THE ONE QUESTION FOR PETERING (with the sent-items forward): "Have you seen this
  ECC→RFMI→'decision about your role' pipeline used on other members at LBH/MSH?" The union is
  the repository of comparative knowledge; if yes, pattern evidence exists through HER channel,
  and Stage 3 (EB12IG) becomes the systemic forum it was built to be.

## 2026-08-04 — RTI/IP-access: YES (timed, scoped). CCC: NOT NOW (banked for the adverse-act branch)
- RTI/IP access plan: lodge MON 10 AUG (with the Stage 2 line + Matheson letter — the writing
  day), NOT this week. Vehicle split: IP Act access application (free) for personal-file
  material; RTI for procedures/non-personal. SIX CATEGORIES: (1) RFMI delegate-approval record
  (name/date); (2) decision records + instruments for the 2-13 Jul exclusion and pay coding;
  (3) conflict-of-interest assessments/register entries touching his matters (⭐ a "no documents
  located" response = the s 89 gap OFFICIALLY proven); (4) the "Health Management processes"
  procedure documents; (5) ESU records re the PID substance-investigation status (expect PID/
  privilege exemption fights — s 65(3) analysis banked); (6) complaint-handling records for
  each complaint he raised. Scope tight — no "everything about me" application.
- Rationale for the 10th: nothing lost (25-business-day clock lands mid-Sept regardless);
  avoids pre-mention noise; and by then the disclosure list + any s 89 answer show what
  remains ungiven — don't RTI what's arriving free.
- CCC adverse-action complaint: NOT NOW. (a) anticipatory — the completing adverse act hasn't
  happened; (b) CCC would refer it back to MSH ESU (inside the building); (c) multi-front
  optics feed the personal-campaign frame pre-mention; (d) it is the BANKED CARD for the
  adverse-act branch — if a detrimental decision lands, the complaint writes itself with the
  full ladder (protected acts, CE knowledge, timing) and arrives with force. Existing CCC
  refs (CO-25-2722/CO-26-1318) already preserve the relationship.
- Ask Petering first whether any category is obtainable industrially faster.

## 2026-08-04 — Red-team yield: five unmined holes banked
1. ⭐ 28 AUG ECC REVIEW-DATE COLLISION: their own checklist schedules review 28 Aug 2026 — four
   days AFTER the 24 Aug deemed-refusal date. Any exclusion "pending review" collides with
   their own instrument's architecture; the deemed refusal lands before their own review date.
2. THE 24 FEB 2025 WELFARE VOID: E. Bain chain confirmed the 7am return; it didn't proceed; MSH
   records show NO welfare inquiry, no follow-up, no "are you ok" — from the org now demanding
   medical information. Usable in the organisational-justice/manner register WITHOUT the QPS
   story (the fact is the void in THEIR records). Handle with rule-10-adjacent care.
3. STIBBARD ACCESS CHANGE (affidavit ¶22): dated operational change (18 Jul 2023 email,
   "removing everyone's access") that CAUSED directory failures — a third-party-attributable
   systemic cause; kills operator-blame lines; underexploited beyond pleading.
4. WEEKEND-MANAGEMENT VACUUM (¶18): he WAS the management function on weekends — capability
   evidence + governance-vacuum corroboration; underexploited.
5. SOLV/IPEC VENDOR FLOWS: medical/RFMI correspondence Cc'd to notes@solv.com.au — personal
   information routing through an external vendor; low-priority privacy thread; hold.
- Also confirmed mined-and-pleaded: the Reviewing Officer's findings fulcrum (¶41 admitted:
  unreasonable MA + significant contribution → under the CURRENT test the Mahaffey
  single-unreasonable-stressor route is close to complete on admissions; the Form 9C reasons
  seam is Willson's needle) — already the 9A's pleaded spine.

## 2026-08-04 — Cost model corrected: the Form 29 compliance mountain priced separately
- Cory rightly flagged the earlier invoice underweighted 64G compliance. If orders are made,
  full compliance is its own mountain for MSH: native email exports + privilege/relevance
  review at scale (potentially thousands of messages, 50-150 review hours alone); the SPOK
  upgrade archaeology to support the ¶50 sworn sub-questions; security-access and payroll
  extraction; verification affidavits drafted against the BINDS (maximum-care documents,
  10-30h legal each); PLUS the hidden multiplier — consistency review of every produced page
  against the 5 June objection's assertions (post-Item 20, someone senior reads everything
  twice). MSH 64G-compliance estimate: 150-400h ≈ $30k-$80k+.
- Regulator knock-on: the enlarged record must be read/analysed/re-priced by Matheson+Willson:
  40-100h ≈ $10k-$40k.
- CORRECTED COMBINED TOTAL (spent + committed incl. 64G compliance): ~$150k-$350k.
- Design note: the 64G is an audit whose cost falls on the audited, either fork — production
  funds the audit of their records; sworn non-existence funds the records-management audit via
  the verification questions. The only cheap fork (ignore it) was removed by sealing.

## 2026-08-04 — Labour ledger built and priced
- skill/references/LABOUR-LEDGER-what-the-matter-cost-them.md: 16 actors, rates Award-anchored
  where possible, 27 line items across 8 phases, ~1,090 hours midpoint, ≈$153k (range $92k-215k),
  38:1 vs the withheld wages, 1.9 years of his salary. Willson's 95h (≈$43k) mostly READING him.

## 2026-08-04 — The Done-Properly blueprint banked
- skill/references/DONE-PROPERLY-consultation-blueprint.md: 10 asks × requirement source ×
  concrete consulted implementation + the standing consultation architecture (support person,
  alongside-not-instead, writing-before-resolved, no waiver, ordinary-way register). The
  constructive half of the file, ready for whichever door opens first.

## 2026-08-04 — Annex A: the Switchboard Operating Model banked
- Cory's five reform proposals professionalised into a controls package (consult-before-
  directive; rotational integrated manager on the phones; complaint SLA 1/3 days with CLS
  escalation; one rulebook for the room; patient-safety design principle incl. SPOK ownership
  + directory-access fix). Each tied to a Code category + affidavit evidence anchor. Tabling
  rules: controls-in-consultation only, room-not-person, lead with patient safety, near-zero
  cost framing. The "inversion" reframed: ss 47-49 already require it — it's compliance.

## 2026-08-04 — Consultation Proposals finalised as table-ready PDF
- drafts/out/Consultation_Proposals_Shepherd_Aug2026.pdf (2pp, metadata clean): Part 1 the
  eight consultation-appropriate asks with proposed implementations; Part 2 the Switchboard
  Operating Model (patient-safety design principle leading, consult-before-change, rotational
  integrated manager, 1/3-day complaint standard, one rulebook); Part 3 the consultation
  architecture. Litigation references stripped; item 10 (PID substance) correctly EXCLUDED
  per its sequencing rule; CE-letter internals excluded.
- DEPLOYMENT RULE: TABLED at Stage 1/2, the assessment scoping, or a settlement conference —
  never emailed cold. Closing line: "I would rather build the fix than continue the dispute."

## 2026-08-04 — A6 (24/7 on-shift supervisor + career pathway) and A7 (evidence-based
rostering) added to the model; Consultation Proposals PDF rebuilt (still 2pp, clean).
- A6 completes the Code coverage: reward & recognition was the untreated category — the
  rotating supervisor function with allowance + development pathway treats it. A7 converts
  the roster-equity contest into a measurable and builds the Stressor 3 fix into design.

## 2026-08-04 — A6 refined per Cory: authority follows the clock
- Supervisor = the after-hours/shift-time decision function, NOT a second manager. Design
  principle written in: "in a real-time environment, escalation is delay" — decisions the
  board needs now are held on shift; only what can wait escalates to the manager in hours.
  Two complementary tiers: manager (frameworks/admin/business hours) + rotating supervisor
  (the shift). PDF rebuilt (2pp, clean).

## 2026-08-04 — Psychosocial Hazard Mapping (WHS) built
- drafts/out/Psychosocial_Hazard_Mapping_WHS_Shepherd_Aug2026.pdf (2pp, clean): Part 1 the
  WHS framework (s 19 psychological health, Regulation psychosocial provisions, ss 47-49,
  the Code); Part 2 TEN hazard mappings (demands, control, support, role clarity, change
  mgmt, reward/recognition, organisational justice, isolated after-hours work, distressed/
  aggressive callers, fatigue) each: presentation → risk → proposed control cross-referenced
  to the Consultation Proposals; Part 3 consultation + review asks (worker's contribution to
  identification under ss 47-49; independent assessor; Code data sources; review dates).
- Deliberately EXCLUDED from the tabled version: job insecurity as a named category (it
  concerns his individual live matter — raised at the scoping consultation orally per the
  HAZARD-NOMINATION ready position, not in the standing room document); all names; all
  litigation references. Companion + same deployment rule as the Proposals: TABLED, never
  emailed cold.

## 2026-08-04 — Consult-then-handover loop added; mapping TABULARISED
- Proposal 6 now carries the real-time loop: "consultation at the speed of the room" —
  supervisor decisions made with the operators present consulted there and then; NEW
  Proposal 8: STRUCTURED HANDOVER AND DECISION LOG (context transfers at shift change —
  a recognised failure point; decisions auditable; the manager gets a complete account
  without interrupting the room). Proposals PDF now 3pp.
- Mapping rebuilt as a LANDSCAPE TABLE (10 hazards × presentation × risk × control w/
  P-references, repeat header, 2pp, metadata clean) with Parts 1/3 as frame. The handover
  (P8) now appears as control in rows 3, 4, 8; real-time team consultation in row 2.

## 2026-08-04 — Annex B: external validating frameworks researched + banked
- APCO Project RETAINS (staffing/retention toolkit, 3 national surveys) + NENA STA-014.2-2025
  + Erlang C → P7. PSAP supervisor-console room design + supervisor-support systems → P6.
  ISBAR + NSQHS Std 6 (Communicating for Safety) → P8 (the hospital's OWN handover standard,
  extended to its comms hub). ISO 45003/45001 → the mapping approach. RETAINS retention tools
  → the recognition pathway. Killer framing banked: "the Switchboard is the one emergency
  communications room in the building that has none of it."

## 2026-08-04 — Fatigue row upgraded: the leave-as-fatigue-control pattern (all staff)
- Cory's observation folded in: fatigue is currently managed BY STAFF through personal leave
  on/after high-volume periods — a TEAM-WIDE pattern visible when rosters × leave records ×
  demand data are read together. Mapping row 10 + Part 3 data ask updated ("map the team's
  leave usage against the rosters and the demand data"). Framing: "recovery provided by the
  roster, not purchased by the worker."
- Evidentiary significance banked: (1) generalises his own "sustained out of my own leave"
  from individual to systemic — kills the personal-vulnerability read (tactic 3): everyone
  absorbs it; he just ran out first; (2) the §4(f) roster/payroll record + unit absence data
  he's already seeking would PROVE the correlation; (3) it's a testable claim in THEIR
  records — the assessment either runs the correlation or visibly declines to look.

## 2026-08-04 — Gold-standard assessment design banked
- skill/references/ASSESSMENT-DESIGN-gold-standard.md: 8-phase methodology (governance/
  independence, work-as-recorded data incl. the leave×demand test, People at Work survey —
  WorkSafe QLD's own validated instrument, work-as-done observation incl. nights/weekends,
  interviews + exit interviews, convergence/rating, controls co-design, review dashboard)
  + EIGHT further improvements beyond P1-P8 (critical-incident debrief, recovery micro-breaks
  + surge protocol, acoustic/ergonomic physical assessment, protective QA call-recording
  framework, occupancy cap, upstream departmental data SLAs, training matrix, psychological
  safety measure). Scoping-meeting posture included.

## 2026-08-04 — Assessment Methodology finalised as table-ready PDF
- drafts/out/Assessment_Methodology_Proposal_Shepherd_Aug2026.pdf (2pp, clean): the eight
  phases neutrally framed + scope items (a)-(h) + consultation close. The tabling set is now
  THREE documents: Proposals (3pp) + Hazard Mapping table (2pp) + Methodology (2pp). Tactical
  posture ("every no recorded") stays in the strategy file only.

## 2026-08-04 — THE CEILING SET produced (drafts/CEILING_SET/)
- The documents that can still move numbers (drafting-to-MSH is at ceiling; these convert
  coming events): 01 Report B instruction letter (THE ceiling-raiser, HOLD for the consult;
  scoped to the corrected test, chronology head-on, course-vs-cause, anti-malingering,
  capacity excluded); 02 Report A scope note (boundary keeper); 03 Stage 2 referral email
  (final text, 10 Aug); 04 IP access application + 05 RTI application (six categories split
  by vehicle, lodge 10 Aug); 06 Calderbank #3 skeleton (conditions precedent gated — fires
  late Aug/Sept on the enlarged record; compensation claim ONLY per rule 9); 07 witness
  account prompts (24 Feb, screaming, torn pages, leave-as-fatigue, the report — private,
  evidence preservation); 08 runway action sheet (Centrelink, hardship, Zappia's two
  exhibits, the Petering forward w/ appeal-window + comparative questions).

## 2026-08-04 — CEILING SET finalised as structured PDFs (drafts/out/CEILING_SET/)
- Nine PDFs, all metadata-clean: 00 INDEX (deployment map + integration paragraph: 07→01;
  01+64G+24Aug→06; 04/05 feed both tracks; 08 protects the timeline) · 01 Report B
  instruction (clean, sendable, HOLD) · 02 Report A scope note (clean) · 03 Stage 2 email
  (reference) · 04 IP application + 05 RTI application (lodgement-ready) · 06 Calderbank
  skeleton (INTERNAL-marked) · 07 prompts (PRIVATE-marked) · 08 runway sheet.
- Deployment discipline on the index's face: nothing sent early, nothing sent hot,
  everything on its trigger.

## 2026-08-04 — THE INTEGRATED PSYCHOSOCIAL/WHS RISK REPORT built (the unmanaged-risk exhibit)
- drafts/out/Psychosocial_WHS_Risk_Report_Switchboard_Aug2026.pdf (landscape, clean): ONE
  document integrating framework + 7-column matrix (hazard | presentation | ⭐ EXISTING
  CONTROLS IDENTIFIED | required-by | risk rating D×F×S | proposed control) + findings +
  integrated controls + consultation. The load-bearing column: "None identified" in red,
  row after row — the only control anywhere = "informal only: workers' own personal leave
  as the de facto fatigue control". Row 10 carries the reviewing-officer finding; ratings
  use "injury of this kind has occurred" (consequence realised, not speculative).
- DUAL USE by design: (1) tabled = the assessment input (neutral in form, ss 47-49
  contribution, invites the assessment to "confirm, correct, or complete" the matrix);
  (2) evidentiary = the standing demonstration the room operated with UNMANAGED risks —
  feeds the s 32(5) manner case, the ss 47-49 breach record, and reg 38. The neutrality IS
  the evidentiary strength: it records absence factually and dares correction.

## 3 Aug 2026 (late evening) — sent-record verification closed, all four emails
Cory supplied the native sent records; every one verified against plan and repo:
- E1 (Response): export with attachment list filed. Exactly the 3 planned attachments;
  all md5-identical to attachments-as-sent (RFMI_Response c3d7e69a / NOTICE 193a8178 /
  PROPOSAL 0f3dfb22). Body = script verbatim.
- E2 (Request, the 21-day clock): NATIVE .msg filed. Subject/routing (IM + lbh_hr, Cc
  Moran), body opening = script, single attachment REQUEST (00b007a8) = as-sent copy.
- E3 (Dispute): NATIVE .eml filed. Message-ID SY9P300MB1547…, sent 01:38:14 UTC
  (11:38:14 AEST), To Taylor direct + IM + HR, Cc Moran; attachment hash 705daea2
  matched THREE ways (inside eml / upload / repo). Stage 1 service moment is now a
  transport header, not an assertion.
- E4 (CE): NATIVE .eml filed. Sent 01:38:02 UTC (first of the four), To cridland direct,
  Cc MetroSouthCorro; LETTER_Conflict (8a5453b8) + ENCLOSURES A–D all md5-identical
  across eml/upload/repo (e7b1f804 / ad3db019 / 7d09fbaa / b313b51c). Body = s 89 script.
  No bounce ever received on the direct address; 12:45 Corro ack (at Cridland's
  direction) completes service + knowledge.
⇒ The 3 Aug send is now evidentially closed end-to-end: what was written, to whom, at
what second, with which byte-exact attachments. MSH silent all day (expected branch).
Next: Tue 4 Aug 11:38 file note if Stage 1 silence holds. Also today: booking emails +
provider enquiries finalised in drafts/ (sendable, non-MSH).

## 5 Aug 2026 (Wed, logged 17:52) — send executed; the machine's first returns
- ⭐ 07:30 EXACT: Stage 1 reply sent as scheduled (cover + v16 locked PDF). Routing:
  Taylor + IM + HR, Cc Moran AND Petering. Filed.
- 07:31 Petering auto-reply: OOO, returns THU 6 Aug (urgent → representation@together.org.au).
  ⇒ union/delegate-notice conversation lands Thursday; Moran holds coverage meanwhile.
- 09:35 Altius (Glockling): today impossible; offers THU 11am or 1pm Teams. Still nothing
  in writing (no fee range, no answers to the five/scope questions). Commit one slot; run
  the call script — colleague name/role first, conflict Qs, answers in writing after.
- ⭐ 11:45 Mind & Memory clinic (Brittney): "I have left a message with Michelle to
  discuss the total of the invoice." THE DIRECT-BILLING CHANNEL IS LIVE — the
  psychiatrist's clinic is phoning Michelle Harrison (IM) about the cost of HIS report,
  exactly per the 31 Jul letter's own arrangement. MSH now hears about the report's
  progress from the clinic, not from him. Subject line carried "QLD HEALTH REQUEST".
  (His booking email as actually sent 4 Aug 11:39 also filed — short version, clean.)
- 16:12 QSuper automated: "graduated return to work payment" SENT to his bank covering
  25–31 May 2026. Day after Zappia's letter ⇒ claim actively being reworked; label
  "graduated RTW" notable. ⚠ Verify the deposit lands + amount; do not over-read (likely
  the final pre-suspension slice being reconciled).
- ⛔ STILL NO MATHESON DISCLOSURE at 17:52 Wed. Pre-mention window now = Thursday only.
  Supports the she-holds-nothing hypothesis; expect mention statement + timetable Friday.
- Standing: file note 4 Aug logged; Thu = Altius call + Petering back (delegate notice) +
  possible last-minute list; FRI 7 AUG MENTION — silent, procedural, consent-orders-
  with-dates rule armed.

## 5 Aug 20:53 — ⭐ PSYCH GROUP RESPONDS IN WRITING (the quote is in hand)
From Sarah Hellwege, DIRECTOR / PRINCIPAL PSYCHOLOGIST (not a BD manager), cc admin,
with two brochures attached. Answered every question in one email, same day.
- "Yes, we do provide the services aligned with your outline."
- Most applicable: ⭐ PSYCHOSOCIAL RISK INFRASTRUCTURE AUDIT — reviews internal data
  (surveys, reporting systems, claims, ROSTERS, policies) + interviews across WHS, HR,
  senior executives, HSRs and workers "where risk is indicated"; in-depth report and
  briefing with recommendations against state regs, codes of practice and ISO standards.
- ⭐ COST: "$10-30,000 depending on the size of the review and number of interviews",
  definitive price once "the client is available to scope the project".
- Also offers psychosocial risk assessments (independently hosted/facilitated survey +
  qualitative interviews, screens all active hazards, comprehensive report) — FREE as part
  of a 12-month Partner Program.
- Role-related risk assessment offered as a service; NOTE: an individual role-related
  assessment "to inform either fitness for work, return to work or to guide a medical
  practitioner" is a SEPARATE, individualised service. ⇒ answers Q5 affirmatively AND
  distinguishes the two — exactly the separation the file already maintains.
- ⭐ "please pass these details on to your relevant contact within the hospital for a more
  definitive scoping and costing as required." — an EXPRESS invitation to table it.
- Brochure: heat maps by team/work area, prevention plans, job (re)design, led exclusively
  by registered psychologists, "direct experience inside a state regulator and an ongoing
  consulting partnership with WorkSafe Victoria".
⇒ CONTRAST WITH ALTIUS: 3 emails, no fee, no scope, no answers, colleague unnamed, still
  seeking a Teams call. PSYCH GROUP IS NOW THE PRIMARY PROVIDER for the tabled package.
⇒ Altius call (Thu 11am/1pm) still worth taking for a second data point ONLY.

---

# ═══ SESSION 5 AUG 2026 (evening) — RED TEAM, CONNECTION MAP, MASTER LOG ═══

## 1. ALTIUS — CLOSED. Five paths, nil.
Banked: `skill/references/ALTIUS-RED-TEAM-5AUG.md`.
- **Path 1 — Altius on the claim file: NIL.** Grep of `corpus/FULL_CORPUS.md` (154 msgs
  2020–2026), the claim documents, confirmed-record and all six packs. Altius/Glockling
  appear NOWHERE before Cory's own 4 Aug 2026 enquiry. They hold nothing of his.
- **Path 2 — Willson via Aussafe Consulting: NIL.** She was Senior Consultant there; no
  corporate link to Altius (different businesses; Altius acquisitions don't include it).
- **Path 3 — Willson ↔ Altius direct: NIL** (re-confirms the 4 Aug check).
- **Path 4 — Altius ↔ QH/MSH contract: not found, NOT conclusive.** Registered govt
  supplier in NSW (buy.nsw). Proper check = Metro South contract disclosure reports on the
  Qld Open Data Portal.
- **Path 5 — Altius ↔ OIR appeals: no ordinary channel.**
- ⭐ **The one residual: a BOOK, not a network.** Glockling's LinkedIn = "QLD State
  Manager, Executive Health Solutions" (an Altius division selling to large Qld employers).
  His own contacts plausibly include health-sector clients. That is the exact risk Cory's
  4 Aug 11:54 email addressed ("I'd ask that my enquiry not be raised with anyone on the
  client side") — a request now in writing, dated, on file.
- **Decision: do not take the Thu Teams call.** Written conflict questions only. Provider
  question handed to Petering/Moran. Employer never named.
- ⚠ Acknowledgement-of-Country footer is NOT a signal — universal in Australian
  signatures. Recorded because it was tested and rejected.

## 2. ⭐ CONNECTION MAP — the real links are INTERNAL
Banked: `skill/references/CONNECTION-MAP-5AUG.md`.
- ⭐⭐ **THE QIRC DISTRIBUTION LIST.** Registry sends every listing in WC/2024/227 to Cory,
  Matheson, Appeals@oir, **Ruttan**, **Tribunalmatters@health.qld.gov.au (QH CENTRAL, not
  Metro South)**, **Chris Thorburn**, **Lauren Griffin**. MSH is a NON-PARTY and four
  MSH/QH addresses sit on the Commission's list. ⇒ **MSH HR cannot claim ignorance of the
  appeal**; QH central has had continuous visibility.
- ⭐ **Griffin ACTED, not just received.** 30 Apr 2026 15:59 she forwarded MSH
  correspondence to the QIRC Registry herself, cc Ruttan/Matheson/Tribunal Matters, copying
  Cory "by way of service". Signature: **Director, Employment Relations, Metro South HR**.
- **MSH → Regulator witness channel** (lawful): Reese witness-conferencing 50pp, the 52MB
  bundle, FRMS 47pp, QH Payroll 24pp — from the 14 Jul 2025 Quatrix production.
- **ESU loop:** PID 13 May 2024 → CCC 30 Aug → CCC refers back to MSH 22 Nov → Loader
  determines 24 Dec 2024.
- **FALSE LEAD RESOLVED:** METADATA_REGISTER reads as though Lauren Griffin sits in
  Commissioner Dwyer's chambers. She does not — "on behalf of the Chambers of Industrial
  Commissioner Dwyer" describes the SENDER (QIRC Registry). Griffin is the last TO-name,
  on a health.qld.gov.au address. Formatting artefact.

## 3. ⭐⭐⭐ PAGE 7 READ FROM SOURCE — the Item 20 kill, and Harrison cleared
Read `WC.2024.227_Shepherd_REG_disclosure_to_APP_11.06.2026.pdf` p 7 directly.
> **From: LBH_HR · Sent: Wednesday, May 15, 2024 3:41 PM**
> **To: Brendon Punch; Elise McGinley; Adriana McNamee**
> "Please see email from Corey Shephard to ESU and CO Complaints regarding Chloe Taylor."
> **Michelle Harrison — Support Officer, Human Resources, LBHS**

**CORRECTIONS to the working theory:**
1. In May 2024 Harrison was a **Support Officer, HR** — NOT Injury Management Consultant.
   Her 2026 title is an ordinary role change. No inference available.
2. She did not "handle" the PID. Cory addressed his 15 May 15:35 email to LBH_HR himself;
   she routed it from the shared mailbox six minutes later.
3. ⭐ **She routed it to three HR officers — NOT to Taylor, NOT to Reese.** On that page
   hers is the correct step. **No Harrison↔Taylor connection is established.**
4. The escalation to Taylor's Director was **Elise McGinley's** (A/Senior Consultant, HR),
   16 May 11:43 → Reese + Tracey Smith, cc Punch/Pritchard/McNamee, attaching
   "Chloe Taylor scc-complaint-form.docx".

⭐ **WHAT PAGE 7 ACTUALLY IS:** an operational HR reaction to the PID, dated INSIDE the
Item 20 window, naming six HR officers, attaching the complaint form, recording that HR
knew ESU held the matter and was awaiting documentation. **MSH told the Commission that
document "does not exist" (Item 20, reference "commenced in November 2024"). The
REGULATOR produced it.** Affidavit ¶52, annexed CS-4.
⭐ **The draft order already pre-empts the answer** — Schedule Part 2, Item 20 requires the
deponent to address the 15–16 May 2024 correspondence "independently of when the reference
'PID24-ESU-1130' was assigned."

**NEW NAMES (all HR, LBHS, May 2024):** Elise McGinley (A/Senior Consultant) · Brendon
Punch · Adriana McNamee · Mack Pritchard · Tracey Smith.

## 4. ⚠ MY ERROR, CAUGHT BY CORY — the AD Act anchor
I had been running an AD Act limitation of ~8 Sep 2026, anchored to the 8 Sep 2025 Hughes
attendance letter. **Wrong.** The conduct founding an AD Act complaint is the exclusion and
failure to provide work from 26 Jun / 3 Jul 2026 (**s 15(2)** — "dismissing includes…
failure to provide work"), which is CONTINUING and puts any window in **2027**. Nothing is
closing next month. The ask was removed from the union email. ⚠ ATT20 is current only to
19 May 2025 — verify against a current consolidation before relying on any of it.

## 5. DOCUMENTS BUILT THIS SESSION
| File | What |
|---|---|
| `drafts/EMAIL_TO_UNION_context_and_assessment.txt` | Union email to Petering cc Moran. Six headings; IN SHORT hook; asks (a)–(d); delegate arrangements for **three** delegates; assessment as a union request in its own right; tracks kept separate |
| `skill/references/THE-SEQUENCE-for-Stage2.md` | 25 Jun–5 Aug chronology + four propositions + the two sentences for the conference + the do-not-include list |
| `skill/references/FROM-5JUNE-the-two-tracks.md` | Two tracks side by side, the actors ledger, the PID thread and where it sits in the 64G |
| `drafts/out/LIST_OF_DOCUMENTS_WC2024227.pdf` | Appellant's List of Documents, 2pp landscape, 5 parts, for service on the Respondent |
| `drafts/out/MASTER_LOG_PID_to_5Aug2026.pdf` | 5pp, nine phases, PID→5 Aug + forward calendar. ⛔ INTERNAL ONLY |
| `drafts/build_disclosure_list.py`, `drafts/build_master_log.py` | Build scripts |

## 6. ⛔ OUTSTANDING — CARRY FORWARD
1. ⚠ **The last shift actually worked before 26 Jun 2026 is STILL unverified.** Settle from
   `Shepherd_Payslips_FY2025-26_analysis.xlsx` + the roster. Decides how Phase 6 reads
   against Phase 7. (CLAUDE.md task 6, still open.)
2. ⛔ **PRESERVATION REQUEST NOT SENT.** Send before 7 Aug. Covers Form 29 categories,
   employment records since 26 Jun, custodian mailboxes, Cory's own QH mailbox, and Solv.
   Neutral, unarguable, starts a clock that only runs his way. Jones v Dunkel only becomes
   available on an actual failure — never on assertion.
3. ⛔ **Mailbox access unknown** — is `Cory.Shepherd@health.qld.gov.au` still accessible?
   Taylor cc'd the hotmail address on both 26 Jun and 2 Jul.
4. **IP Act application (10 Aug) is the ONLY route to the 2026 employment file** — Form 29
   date ranges stop at 30 Jun 2024. Scope by named custodians (Harrison, Forrest, Hughes,
   Taylor, Griffin, LBH_InjuryManagement, LBH_HR/LBH.HRTeam1, MSHR.EmploymentRelations),
   period 1 Jun 2026→, described categories. **Add notes@solv.com.au.**
5. **List of Documents — two scope decisions HELD for Cory:** (a) the 2026 employment
   correspondence (in = imports the employment dispute into the appeal, discipline rule 8;
   the ECC is in at Item 2 as medical); (b) the 2025 restricted category. **Serve AFTER
   Friday** — the PID category should not go to the Respondent before order 6 is made.
   Page-count placeholders `[n]` still to fill.

## 7. DISCIPLINE NOTE
Three escalating inferences were tested and set down this session (the AoC footer; the
either/or; the ecosystem theory). Each was built on the same two Glockling scheduling
emails. Discipline rule 1 held — **nothing reached paper.** The material that hurts MSH has
been in their own documents every single time: the objection's admissions, the ECC, the
payslips, the "unable to accommodate" statement, and now page 7.

---
## 9 August 2026 — Report B letter of instruction (the ceiling deliverable)

Built the three Report B deliverables the user asked for, via a verify-hardened workflow
(3 draft agents + 3 adversarial verify lenses on the letter):

1. `drafts/out/CEILING_SET/01_Letter_of_Instruction_Report_B.md/.pdf` (4pp) — the finalised
   letter of instruction to Dr Krishnaiah for the causation report. Supersedes the 3 Aug draft.
2. `drafts/out/CEILING_SET/01b_Source_Package_Guide_Report_B.md/.pdf` (6pp) — "what to give the
   psychiatrist": the signed statement as the spine, the documents bundle, the medical history
   to disclose, and what NOT to do.
3. `drafts/out/CEILING_SET/01c_Why_Report_B_Is_The_Ceiling.md/.pdf` (5pp) — why a properly-built
   causation report is the single highest-leverage document (bimodal forecast; causation is the
   only open, non-substitutable block).

All three adversarial lenses' confirmed defects were resolved in the finalised letter — full
record at `skill/references/REPORT-B-LOI-VERIFICATION-9AUG2026.md`. Headline fixes:
- ⛔ Review Decision 69983's CONCLUSIONS removed from the doctor's assumed-facts basket and
  enclosures (they read as an instructed answer; kept for hearing/settlement only). Enclosure D
  = Form 24 admitted facts only.
- ⛔ Q6.8 no longer quotes the A4 premorbid line (the "perceives as unjust" s 32(5)(b) landmine)
  or presupposes causation — asks from the doctor's own assessment; the A4 line stays for ORAL
  handling on 12 Aug.
- Q6.10 no longer instructs "consistent with" the ECC (which is Dr Ma's, not Krishnaiah's).
- ⭐ FACTUAL CORRECTION: first presentation is **1 July 2024** (Hawes WCC), not "September 2024".
  Onset→presentation is ~2 weeks, not ~3 months — the earlier drafts overstated the gap and
  conceded the Regulator's best point for free. The ~3-month interval is March roster→June onset.
- Added missing source documents (GP records, Hawes WCC, ECC, the 13 Feb 2025 report) and a new
  Q6.11 on capacity trajectory (his own Feb-2025 "complete incapacity" → now fit-with-adjustments).

Build scripts: `drafts/build_letter_of_instruction.py` (reportlab, house style) and
`drafts/build_ceiling_companions.py` (Chromium md→pdf, for the table). PDFs metadata-scrubbed.

⛔ Open before the letter goes: (a) reconcile the deed-20-Sep vs Form-20-¶43-8-Oct cessation date;
(b) confirm the 3 July 2026 ECC author is Dr Ma; (c) the signed statement (Enclosure A) must carry
every load-bearing timing/load fact so nothing rests on the doctor's memory.

## 9 August 2026 (later) — Krishnaiah suitability answer + Griffin memoir
- Answered whether Krishnaiah can write Report B given A4 (assessment in chat; grounded in
  A4-RED-TEAM.md read in full): yes with managed risks — his file is the asset (observed signs,
  contemporaneous mechanism, treatment escalation), A4's flaws are flaws of purpose/haste fixable
  by instruction; watchpoints are report craft, the footer confirmation, and cross-examination
  willingness. Fallback (fresh IME) is weaker on causation-at-June-2024.
- `drafts/GRIFFIN_MEMOIR_7AUG_INTERNAL.txt` — ⛔ internal perspective exercise (Matheson's-chair
  genre), exterior facts sourced to CONNECTION-MAP-5AUG.md, interior voice invented. Never serve.
- `drafts/RUTTAN_MEMOIR_7AUG_INTERNAL.txt` — ⛔ second perspective exercise (Ruttan): the Form 29
  arc from the objection author's chair through to the appearance-only mention. Exterior facts
  verified against confirmed-record.md (incl. the 2:57 PM created / 3:02 PM served timestamps and
  the Schedule A row 6 adoption of MSH's own narrowing); mention account = Cory's recollection;
  interior voice invented and labelled. Never serve.

## 9 August 2026 (evening) — transcript research + Form 29/64G withdrawal draft
- TRANSCRIPT/AUDIO of the 7 Aug mention: order via **QTranscripts**
  (qtranscripts.justice.qld.gov.au, QGov/myGovID login) — the platform covers QIRC. Under the
  **Recording of Evidence Regulation 2018 a party is entitled to ONE FREE COPY of the transcript**;
  audio can also be requested. If the mention has not been transcribed it is typed on request
  (production cost may apply — call Recording and Transcription Services **1800 842 122** for an
  estimate and hardship/fee-waiver options). Manual form exists ("Queensland Courts, QIRC & QCAT
  Request for Transcript", courts.qld.gov.au). Delivery = secure download link, expires 30 days.
  Note: VIQ Solutions (one of two providers) exited 30 Jun 2026 — allow for slower turnaround.
- `drafts/WITHDRAWAL_Form29_and_64G_DRAFT.txt` + `drafts/out/WITHDRAWAL_Form29_and_64G_WC2024227.pdf`
  (1 pp) — withdraws the 23 Jun application AND all outstanding Form 29 items; MSH released; further
  documents via the Respondent's Appeals Officer; awaits further orders. NO reasons given (rules 5–6).
  ⚠ Note 3 in the draft: the MET-call spreadsheet (identified as available in K-LM26/729) goes with
  it — route (a) preserved via para 3. Send Mon 10 Aug with the witness list; never let the
  preservation/conflict enquiry arrive alone.
- `drafts/EMAIL_TO_UNION_Stage2_psychosocial_DRAFT.txt` — rewrite of Cory's email to Moran +
  Petering: thanks in advance; why they've been on the correspondence; ask 1 = Stage 2 support
  (referral Mon 10 Aug, representation/attendance); ask 2 = independent union referral of the
  matters in Together's own name, with the psychosocial assessment of Switchboard (Code + EB12) as
  the named specific; delegate-type framing kept honest. ⚠ date check: his response = 4 or 5 Aug
  (record says v16 went 5 Aug 07:30) — left undated in the draft. Send before the Stage 2 referral.
- `drafts/STAGE2_REFERRAL_FINAL_10AUG.txt` — the Stage 2 referral, finalised from the 4 Aug
  skeleton and ALIGNED AGAINST SOURCE: Taylor 4 Aug 13:35 quoted verbatim (lodged per 1.11.2(a);
  "24-hour timeframe... will not be achieved"); the response's five facts/seven questions;
  availability dates corrected to the response's own §7 (Wed 5 / Thu 6 Aug); status quo anchored
  to 26 JUNE per the response's correction; the §7 foreshadowing quote verbatim; independence ask
  mirrors the CE letter. THREE BRACKETS remain (1.4, 1.5, 1.6 + check 2.4) — all await MSH's
  latest Stage 1 response (~8-9 Aug, NOT yet in repo; hotmail not reachable from this session).
  Delegate ¶ held out until Together's own written confirmation exists. Conference clock: by Mon
  17 Aug; chase Thu 14 Aug.
- `drafts/out/STAGE2_REFERRAL_DRAFT_FOR_REVIEW.docx` — the Stage 2 referral as a Word draft for
  review: DRAFT banner, the five fill-in passages highlighted YELLOW (two [DATE], three [Adjust]),
  metadata scrubbed (Creator/LastModifiedBy/Application/Company empty, revision 1, neutral
  timestamps — verified with exiftool). Built with build_stage2_docx.js (docx npm, installed
  --no-save). ⚠ soffice is broken in this environment (javaldx/java) so verification was
  XML-level + text extraction, not visual render.
- Stage 2 docx REVISED per Cory: all slots closed on his instruction ("the only response is the
  one email they sent and no other; the issues have not been resolved") — 1.4 none of the seven
  questions answered; 1.5 one further written response only, resolves nothing; 1.6 special-leave
  request unanswered; 2.4 slot removed. ONE open section remains: "3 Union representation and
  delegate status" (reserved for Together's confirmation); Arrangements renumbered to 4.
  Metadata re-scrubbed and verified.
- Stage 2 docx CORRECTED per Cory's clarification: Chloe's 4 Aug letter is the ONLY MSH response
  in Stage 1 (no later response exists). 1.5 rewritten — "the only communication received from
  the Health Service during the Stage 1 period; my response of 5 August has not been answered";
  phantom attachment (4) removed (three attachments, mirroring the union email). The single open
  area in the Word doc = section 3 (reserved for Together Queensland). Verified: exactly 1
  bracket remains; metadata clean.

## 10 August 2026 — Stage 2 referral FINALISED from Cory's co-edit, ready to send
- `drafts/out/REFERRAL_Stage2_cl1.11.2b_MSH-INJ-5795.pdf` (3pp) — built from his co-edited docx
  (which added Hughes to Cc, the long-form agreement title matching Taylor's own letter, the
  suspension/status expansion of 2.1, the 7.1.5/Code/7.2.2/WHS-Reg-s36 expansion of 2.5, the
  E12/E13 + 12-month roster/payroll expansion of 2.6, the s 101/s 33 cites, the QH-IMP-401-5 line
  in 2.3, a "What this referral does not include" section, and an instruments schedule).
  FINISHING CHANGES applied: union placeholder REMOVED per his standing instruction (Arrangements
  renumbered 5→4; "union representative present" retained in Arrangements); "That date has
  passed" → "has been reached" (true on the 10th and after); cl 1.11.5 words set in quotation
  marks (verbatim clause text, quoted that way in the Stage 1 notice — verified in FULLTEXT).
  Cites 1.11.5 and 1.12.2 VERIFIED against the Stage 1 notice quotes in the index. Style matches
  the filed v16 (title/ref-line/footer, Helvetica, A4). Metadata fully stripped (qpdf+pikepdf; no
  Info, no XMP). 10 automated content checks passed.
- Send: attach to a two-line email to LBH_HR, cc per the Copies line. The Stage 2 seven days run
  from sending; diarise the chase 3 business days out.
- `drafts/out/STAGE2_REFERRAL_FOR_UNION_EDIT.docx` — the union's editable copy: Cory's co-edited
  docx with the two finishing text fixes applied in place (date phrasing; 1.11.5 in quotes), the
  UNION SECTION KEPT (the note to Heath and Emily, in his own latest wording), all his
  formatting preserved, metadata scrubbed. The send-ready PDF (union section removed) and this
  editable docx (union section in) are the two live artifacts: if the union completes their
  section, rebuild the PDF from their text; if not, the PDF goes as is.

## 10 Aug 2026 (evening) — ATTENDANCE AT THE 7 AUG MENTION (Cory's recollection, ⚠ verify against transcript)
Present per Cory: Myla Ruttan (compelled, named in the notice — appearance only); **Lauren
Griffin (NOT ordered to attend, attended anyway)**; Renee Matheson; and **an unidentified man
WITH the group** (not a gallery stranger — with them). Cory has never met him.
- Griffin attending voluntarily: the Director ER whose directorate runs the 2026 exclusion has
  now PERSONALLY heard Dwyer read the 9A and group the fatigue material. Knowledge brick —
  document, never plead as motive (discipline rule 1).
- The man: identify from the TRANSCRIPT appearances when it arrives. If not announced, remains
  open — record, no theory. Candidates ranked in chat 10 Aug: QH central legal (Tribunalmatters
  is on every listing) / second OIR-Regulator officer / Crown Law / metrosouthlegal / WorkCover
  liaison. ⛔ No inference beyond identity; no HopgoodGanim theorising.
- Four attendees for the other side(s) at a procedural mention vs the appellant alone —
  institutional turnout is itself a data point on how the matter is priced internally.
- ⚠ The Griffin memoir (drafts/GRIFFIN_MEMOIR_7AUG_INTERNAL.txt) assumed she was NOT in the
  room — now contradicted by Cory's recollection. The memoir is labelled invented-interior, but
  note the factual frame is superseded.
- ⭐⭐ GRIFFIN — CORY'S RECOLLECTION (10 Aug): **she handled his October 2024 dismissal**, and she
  runs MSH's unfair-dismissal/QIRC matters generally. NOT yet corroborated in the searchable
  record — the TD/2024-110 Form 12 is NO_TEXT_LAYER and the 2024 dismissal-era correspondence is
  not in the corpus. ⚠ VERIFY: render TD2024-110 PDF + locate 2024 reinstatement correspondence.
  If confirmed, her arc spans: 2024 dismissal (reversed) → every appeal listing → service in the
  appeal (30 Apr 2026) → the 2026 exclusion inside her directorate → voluntary attendance at the
  7 Aug mention → likely Stage 2 actor. ⛔ Discipline rule 1: knowledge + continuity, documented;
  motive never pleaded. Note the Stage 2 referral's "officer independent of the matters in
  dispute" request now has concrete content if she self-selects for the conference.
- `drafts/EXEMPLAR_REPORT_B_INTERNAL_BENCHMARK.md` — ⛔⛔ INTERNAL ONLY, fictitious drafting
  exercise at Cory's request: a textbook-psychiatrist exemplar of Report B on his facts
  (17 sections, 16–22pp real-world equivalent), with a 12-point benchmark checklist to evaluate
  the REAL report against, and a gap-check (⚠ FIND the Aug 2023 0.8→FT request document; verify
  first-consult date, medication dates, bereavement date). NEVER shown to the doctor, never
  served — a drafted exemplar reaching Krishnaiah would destroy the report's independence.
- `drafts/WEDNESDAY_QUESTION_MAP_12AUG.md` — the consultation question map: six timeline phases
  (baseline → exposure → decompensation → presentation → nadir/return → continuation → integration),
  open questions only, facts-to-put per phase, [elicits] notes for Cory's understanding only.
  ⭐ NEW FACT captured: the approach-avoidance attendance pattern (would get ready/travel, then
  call up unable to go in) — Phase 2's core; converts the attendance record into symptom evidence;
  needs frequency/weeks in the statement. Five confirmations + oral-only discipline + pre-Wednesday
  gap list included.

## 10 Aug 2026 (late) — TWO SOURCE FINDS filed from the uploads store
1. `documents/2024-12-09_Deed_DRAFT_v2_MinterEllison.docx` — the DEED DRAFT v2 (9 Dec 2024),
   negotiation-era, placeholders intact ("xxx hours", "[insert exact amount]"). Verbatim reads:
   - ¶45 the carve-out INSIDE the release: "...excluding any statutory claim under the Workers'
     Compensation and Rehabilitation Act 2003 or any claim that cannot be excluded at law".
   - NO "will not oppose the appeal" covenant exists in this draft. The functional equivalent is
     ¶48 (deed pleadable as a BAR only to claims "agreed to forego") + the carve-out ⇒ the deed
     can NEVER be pleaded against the WC appeal by any Beneficiary (MSH, every HHS, the
     Department, the STATE OF QUEENSLAND, all current/former officers).
   - ⭐⭐⭐ ¶38: "$287.72 in daily earnings... from 7 October 2024 being the date upon which the
     Applicant would have resumed work HAD HE NOT BEEN DISMISSED" — MSH's OWN DRAFTING calls it
     a dismissal (not abandonment).
   - ⭐⭐ DATE CONFLICT RESOLVED (the ¶43/deed open item): ¶21 — correspondence RECEIVED 8 Oct
     2024, nominating separation 20 Sep 2024; ¶36 20 Sep–6 Oct treated as LWOP; ¶38 would have
     resumed 7 Oct. All three dates true, different events. Form 20 ¶43's "8 Oct" = receipt.
   - ⭐⭐ ¶45 release covers common-law PI claims "arising out of or related to the Abandonment
     Process or Reinstatement Application" ONLY ⇒ a common-law claim for the WORKPLACE INJURY
     itself (roster/fatigue, pre-dismissal) appears NOT released + WCRA claim excluded ⇒ the
     future damages pathway looks preserved. ⚠ Check the EXECUTED deed's final wording.
   - ¶50 MUTUAL non-disparagement: Health Service owes best endeavours that no employee makes
     adverse comment about the Applicant re the deed matters.
   ⚠ This is DRAFT v2, not the executed instrument — executed version remains the authority.
2. `documents/2023-09-27_Taylor_FullTime_Appointment_APPROVED.pdf` — ⭐⭐⭐ THE GAP-CHECK ITEM
   FOUND, and better than memory: 27 Sep 2023, FROM CHLOE TAYLOR: "your application for
   Permanent Fulltime hours... has been approved... happy to commence Full-time hours from the
   16th October 2023." "Very pleased." ⇒ the premorbid-engagement fact is now a DOCUMENT from
   the Respondent's central witness, who was "very pleased" with him 5 months before the break.
   Statement dates: applied ~Aug-Sep 2023; approved 27 Sep 2023; commenced FT 16 Oct 2023.

## 10 Aug 2026 (night) — ⭐⭐⭐ THE EXECUTED DEED + THE NEGOTIATION RECORD (6 documents filed)
⛔⛔ CORRECTION TO DEED-AND-LOD-8AUG2026.md: that analysis was built on a DRAFT. The EXECUTED
deed (signed Cory 14.02.2025, witness Thomas Balsley; signed Cridland digitally 21.02.2025,
witness Ellen Duckering) DIFFERS MATERIALLY — every difference favourable:
1. ⭐⭐⭐ Recital D DEFINES the event: "...a separation date being 20 September 2024 **(the
   Dismissal)**". MSH executed an instrument defining it as the Dismissal. "Abandonment" is
   dead as a characterisation, over the CE's signature.
2. ⭐⭐⭐ Clause 8 (release, FINAL): released = claims "arising from the Dismissal" ONLY
   (narrowed from v2's "matters recited"+absenteeism), excluding "**any common law personal
   injury claim**, statutory Workers' Compensation claim, or any claim that cannot be excluded
   at law" (broadened from v2's WCRA-only). ⇒ the WC appeal AND any common-law PI claim —
   UNQUALIFIED — survive. The future damages pathway is fully open, in terms.
3. ⭐⭐⭐ Clause 7 — NEW, not in v2: "The Applicant reserves any legal rights or claims he may
   have in relation to any FUTURE management action taken against him by the Health Service
   pursuant to clause 6." ⇒ the 8 Sep 2025 letter and arguably the 2026 exclusion (both
   clause-6 territory: absenteeism/communication) are events HIS RIGHTS ARE EXPRESSLY RESERVED
   over. No release argument can ever touch the post-deed conduct.
4. Clause 2(c): wages 20 Sep–13 Dec 2024 + $5,000 legal expenses; leave credited (AL 54.16h +
   loading 54.16h); Clause 4: LWOP 13 Dec 2024 – 23 Feb 2025. ⭐⭐ THE RETURN TIMING PROVEN BY
   THE DEED'S OWN ARCHITECTURE: wages only resumed on attendance; deed took effect 21 Feb
   (Cridland); he returned 24 Feb — the first business day. The "employment-driven return" is
   now a documented mechanism, not an inference. He signed 14 Feb — ONE DAY after A4
   ("complete incapacity"; "advised to defer decisions regarding work settlement or legal
   matters"). Documented, held; not a live front (he was represented at signing).
5. Cl 10/11 mutual non-disparagement re deed matters; cl 12 confidentiality (as-required-by-law
   exception); cl 16 WP→open once agreed. Cridland signed BOTH the deed and K-LM26/729.
GRIFFIN'S ROLE — RECOLLECTION CONFIRMED FROM HER OWN EMAILS:
- 26 Nov 2024 (to Registry): "I confirm that I will appear for the Health Service in person"
  — TD/2024/110. She ran the dismissal defence. VERIFICATION FLAG CLOSED.
- 11 Dec 2024: Stone Group (Joubert) forwarding "a further email from Lauren" — she negotiated
  the deed with his then-lawyers.
- 28 Jan 2025, WP, DIRECT to Cory ("further to correspondence with your FORMER lawyer" — he
  was between firms/unrepresented): restating the "full and final offer" with time-pressure
  framing — during the clinical nadir (~first Krishnaiah consult period). Documented; rule 1.
- Saines (Conrad, 13 Feb 2025) CONFIRMS the negotiation account: "we have amended the deed to
  clarify that you are not waiving your right to bring a statutory WorkCover claim and to
  reserve your right to bring common law personal injury claim about the dismissal." Cory's
  account verified: the carve-outs were negotiated in by his side.
- He was represented by TWO firms in sequence: Stone Group (Nov-Dec 2024) → Saines (Feb 2025).
Files: documents/2024-11-26_Griffin_appearance…, 2024-12-11_StoneGroup…, 2025-01-28_Griffin…,
2025-02-13_Saines_Conrad…, 2025-02-14_Saines…, 2025-02_Deed_EXECUTED….
- FURTHER from the full chains (same six documents):
  ⭐⭐⭐ Saines' 13 Feb 2025 advice lists the amendments AND their origin story: (1) WC-claim
  clarification; (2) common-law PI reservation; (3) clause 7 = "Ensure that you retain any legal
  rights you may have if the Health Service takes disciplinary action against you in the future";
  (4) ⛔⭐ Saines sought an express **"non-reprisal" clause** and amendments limiting clause 6 —
  **MSH REFUSED BOTH** (call with MSHHS, 13 Feb 2025). Then: 8 Sep 2025 letter; 2026 exclusion.
  Documented context; rule 1 — never pleaded as motive.
  ⭐ Saines referred him to Littles Lawyers (Peter Bandarian) for the common-law PI claim —
  the damages pathway was professionally flagged in Feb 2025 and is preserved by cl 8.
  ⭐ Griffin, 28 Jan 2025 (WP, direct to unrepresented Cory): MSH "is not able to entertain a
  settlement on the basis that it cannot manage you by way of REASONABLE MANAGEMENT ACTION, and
  will not 'wipe the slate clean'" — the s 32(5)(a) vocabulary in the ER Director's negotiation
  correspondence, Jan 2025. Underpayments expressly preserved ("not restrained from continuing
  to pursue them outside the context of this matter").
  ⚠ WP status: the negotiation emails are without-prejudice (internal analysis only; not
  tenderable); the deed itself became open on agreement (cl 16) but stays confidential (cl 12,
  as-required-by-law exception). Standing advice unchanged: prove payments by payslips.
- ⭐⭐⭐ SYNTHESIS (Cory's, 10 Aug night) — THE KNOWLEDGE–AUTHORITY GAP: the officers with
  complete knowledge of the deed's architecture (Griffin negotiated every clause; Tribunal
  Matters cc'd throughout; Cridland signed) are the same officers/offices running the 2026
  exclusion WITH NO IDENTIFIED INSTRUMENT (question 3.1, unanswered). Clause 6 reserved a right
  to deal with absenteeism/communication — a reservation, NOT a power; it preserved lawful means
  and created none. THE FORK: if the 2026 exclusion is clause-6 conduct-management → no
  disciplinary instrument invoked + clause 7 reserves his rights over it; if it is medical/WHS
  (their stated basis: G3 + ss 17/19) → the unassessed-hazard problem + the fit-with-adjustments
  ECC against them. Either characterisation fails on their own documents. Griffin's Jan 2025
  line ("cannot entertain settlement on the basis that it cannot manage you by way of reasonable
  management action") = they insisted on retaining lawful management powers, then acted without
  identifying any. ⛔ Rule 1: never pleaded as motive; deployed only through the instrument
  question (Stage 2), the s 89 letter (already with Cridland), and — if ever — the sequenced
  reprisal track. Deed + WP emails remain internal-analysis only.
- v9.1 + DEED-WEAPON-MAP-10AUG2026.md: the deed converted to its deployment map (W1 return
  mechanism → Wednesday; W2 fatigue-pay payslip → appeal, non-admission discipline; W3
  consent-model contrast → Stage 2 orally; W4 cl 7 + refused non-reprisal → reprisal track,
  HELD; W5 preserved damages → Calderbank #3 paragraph; W6 "the Dismissal" vocabulary; W7
  entire-agreement shield; W8 tripwires). Numbers: 47/51 hearing (unchanged), 79/85 compensated
  (+1). Full prohibitions list in the map. Deed stays in the drawer.
- THE DOUBLE-LENS READ (deed + PID) banked 10 Aug: every 3-Aug document lands on readers charged
  with knowledge of BOTH the deed (refused non-reprisal; cl 6/7; consent model) and the PID
  (13 May 2024; circulated within 26 hrs; retraction 15 May; closed 24 Dec 2024 without
  investigation DURING the incapacity nadir — the non-reply is clinically explained; protection
  attaches at MAKING, not outcome). Each letter = 5 things at once: neutral procedure /
  performance of his obligations / documentation of their non-performance / accrual of protected
  acts / completion of knowledge elements. ⛔ The word reprisal stays unsaid everywhere (rules
  2/8) — the elements are being proven, not pleaded.
- DEED vs FORM 29 vs CE LETTER (banked 10 Aug): (i) the Form 29's ranges STOP 30 Jun 2024 — his
  instrument never touched deed-era matters (perfect cl 10/12 compliance by design); (ii) the
  objection's "not retained"/"does not exist" answers are CE-SIGNED by the deed's own signatory —
  and cl 6's reserved right to "deal with outstanding matters" PRESUPPOSES a record base the
  objection denies exists (the reserved-right/no-records tension); (iii) Cridland's two
  signatures (deed Feb 2025; objection Jun 2026) bracket the knowledge; the s 89 letter then
  landed on the same signatory, ack'd at her personal direction. His documents respected the
  deed's fences precisely while their responses accumulated against their own instrument.
- THE 64G THROUGH THEIR EYES (deed lens, banked 10 Aug): (i) the application threatened to
  convert the reserved-right/no-records contradiction into SWORN testimony (the verification-
  on-oath sought at Form 20 ¶48/¶50) — the swearers would be the deed's own
  signatory/negotiator; (ii) served on Ruttan personally 25 Jun 08:31 — the one reader holding
  the deed + objection + Form 20 + (later) the CE letter together; (iii) DATES: sealed 64G
  served 24–25 Jun; the "position changed" advice 26 Jun — the adjacency cuts BOTH ways
  (⚠ their 34-occasions counter-material stands; task 6 still open: whether the stoppage
  predates); under a reversed onus THEY would carry the burden of disproving the connection;
  (iv) Schedule A row 6 adopted THEIR narrowing — the second time (after the Feb 2025 deed
  amendments) the institution watched his side take their drafting and turn it; (v) the
  withdrawal leaves the contradiction UNADJUDICATED BUT UNDISCHARGED — relief that is
  provisional (RTI/IP + the soft channel reach the same records; the return path is
  bench-endorsed); (vi) even the Form 20 stayed inside the deed's fences — dismissal FACTS
  sworn for a proceeding, no deed, no settlement terms, no characterisation.
- ⭐⭐ THE COMPLETED CONFLICT ARCHITECTURE (Cory's cap, 10 Aug): the objection ITSELF nominated
  Cridland as the gate — three times, "would require approval from the Health Service Chief
  Executive" (expense items). So THEIR drafting made the approver of production the signatory of
  the positions production would test (the deed cl 6; the "does not exist" answers). His s 89
  CONFLICT-OF-INTEREST letter then went to precisely that officer — ack'd at her personal
  direction. The conflict is structural and self-documented in their instruments: she cannot
  independently decide questions her own signatures answer. Her three doors — answer (must
  address her own role) / delegate (concedes the conflict) / silence (question stands on
  documented personal knowledge) — are all his. ⛔ Never alleged; the letter already asked it;
  channels remain RTI/IP + the sequenced tracks.
- `drafts/THE_SIGNATURE_short_story_INTERNAL.txt` — ⛔ internal perspective piece (the memoir
  genre; protagonist = the signature itself, no interior attributed to any person): the deed →
  the objection → the exclusion → the s 89 letter → the 64G spared. The mistake analysis banked:
  each node is individually explainable as ordinary process (CEO signs what's put up) — and the
  charitable reading is itself the s 89 governance problem; after the 3 Aug letter + the 12:45
  acknowledgment, "mistake" is no longer available going forward — continuation is choice. The
  file never needs to pick a reading: conflict OR unchecked-signature governance failure both
  serve; his letter is what forecloses the innocent future. Rule 1 absolute.
- `drafts/CRIDLAND_MEMOIR_INTERNAL.txt` — ⛔ fourth perspective piece (her hat): the arrival
  sequence at the CE's desk (deed → objection → s 89 letter → 64G produce-or-swear → conflict
  question) and the "did he plan it" question answered inside the story: he planned his PART
  (channel discipline); the CONVERGENCE was built by their own org chart — every document
  reached her signature by their routing, not his targeting; the only document he ever aimed at
  her was the one asking if anyone had noticed. Exterior facts cited; interior invented; rule 1.
- ⭐⭐ THE REFLEXIVE READING OF THE s 89 LETTER (Cory's, 10 Aug): the letter's conflict question
  reads at TWO depths — (surface) conflicts in the officers deciding the exclusion/RTW/info
  (Hughes etc.); (deeper) the RECEIVER'S own conflict: the signatory of the objection (whose
  production-gate is herself) and the deed, asked to preside over matters her signatures already
  committed. s 89 covers PERCEIVED conflicts — the fair-minded-observer test is made out on
  documents alone. Receipt (12:45, documented) CREATED the statutory moment: the duty to
  consider/disclose/manage arose on delivery; handling it personally proves the thesis by
  conduct; delegating concedes it; silence leaves the duty visibly unmet. The letter is a
  mirror — whoever holds it must first ask whether they may hold it. FUTURE USE: RTI category —
  any COI declaration/assessment recorded after 3 Aug receipt (absence = s 89 process not
  followed even when asked in writing). Nothing further to send; the letter already did this.
- THE ACKNOWLEDGMENT'S FORM (Cory's read, 10 Aug): "I have been asked by Noelle Cridland... to
  acknowledge receipt" = the arm's-length HALF of conflict management (personal receipt + no
  personal handling) WITHOUT the second half the Act requires (disclose/manage/refer). The
  gratuitous naming of her personal direction documented the exact element (personal knowledge)
  generic corro practice would have left unproven; 67 minutes = triaged as significant on
  arrival. Their careful handling produced his evidence. Mundane reading (standard Exec Services
  practice) noted and probable — the FORM's evidentiary effect is identical either way.
- ⭐ NEW FACT FLAGGED (Cory, 10 Aug late): he was told "the other staff member was doing that"
  when it was NEVER done — a checkable misrepresentation about task/work distribution
  (comparator/roster-equity territory, Stressor 1 / items 8-9 anchor). FOR THE STATEMENT: date
  it, name the task, identify the record that disproves it (roster/task logs). It is a FACT
  question, not motive — cross-examination anchor if the records disprove the claim.
  His accumulation list for Phases 1-2 of the question map: pay delay (≤5 months) = ERI ·
  union/delegate non-response = support failure · the rostering = control · the false
  "someone else was doing it" = organisational-justice/integrity fact.
- SOFC CONVINCINGNESS AUDIT (full read, 10 Aug): their genuinely forceful points = ¶8 (2022
  history exists — but doesn't collide with the quoted Nov 2023 baseline), ¶11 (no-particulars
  re 1(a)), ¶13 (2023 responsiveness — meetings/emails happened), ¶24(b) (cl 18.10 fatigue leave
  requires overtime — REAL technical point, verify item already open), ¶16(a) (Reese unaware of
  PID at retraction — consistent with our own N.13 finding), ¶25 (post-dating, partial force
  only — ignores aggravation-as-injury). SELF-HARM inventory: ¶12 admits page removal; ¶14
  admits attachments "were in fact present" (wrongful leave decline = ADMITTED HUMAN ERROR #2 —
  both errors cost HIM); ¶15 admits stressor 1(e) OUTRIGHT; ¶21 pleads the 3 May→28 May AVAC
  delay itself; ¶22(a)(c)(e) admit the keystone facts; ¶22(b) "could refuse shifts at anytime"
  CONTRADICTS ¶22(e) (the signed break agreement); ¶20 "no outstanding underpayments /
  remedied in a timely manner" collides with Form 24 ¶¶40-41 (25-day delay admitted) AND the
  deed's Feb 2025 payments ($377.19 fatigue + $5,512.66 HE + $1,237.50 public holidays);
  ¶27 calls him "the Plaintiff" (civil-precedent copy artifact). THE HOLLOW CORE: the entire
  affirmative defence = ¶27's single conclusory sentence + ¶22(f)'s six unwitnessed words; no
  expert referenced, no authority cited, "reasonable in all respects" x6 as refrain; 32(5)(b)
  recited in the elements (¶6(d)(ii)) but NOT contended (¶27 = RMA only) — confirms unpleaded.
  NEW PREP ITEMS: answer cl 18.10 (overtime point) — note the deed PAID fatigue pay for the
  shift; the 42% Easter payroll check (items 8-9 anchor — payroll arithmetic decides ¶19(c)).
- ⭐⭐⭐ SOFC OUTRIGHT-ADMISSIONS REGISTER (verified against both filed documents, 10 Aug):
  EXPRESS "admits": ¶10 the Hawes certificate + its recorded mechanism words (denied as fact,
  document admitted); ¶12(a) Taylor removed Communication Book pages ~6 Jun 2023; ⭐⭐⭐ ¶15
  STRESSOR 1(e) ADMITTED IN FULL = "On 13 May 2024, the Appellant lodged a corrupt conduct
  complaint regarding clinical risks. The Ethical Standards Unit formally determined this
  constituted a Public Interest Disclosure" — THE PROTECTED ACT IS NOW ADMITTED ON THE
  PLEADINGS of the WC appeal by the Regulator itself (the reprisal track's first element needs
  no proof, ever); ¶26 worker status s 11.
  FUNCTIONAL ("says") ADMISSIONS: ¶22(a) 7-hr break + "human error" (error #1); ¶22(e) the
  Jun 2020 agreement exists; ¶22(c)/¶24(a) 19 Mar leave taken; ¶14(e)-(f) attachments "were in
  fact present" — wrongful COVID-leave declines = "human error by Ms Taylor" (error #2);
  ¶16(b)(i) attendance difficulty 13-15 May (THE PRODROME, their pleading); ¶16(b)(vi)-(vii)
  he did not want to retract + "the email was ultimately removed from the server"; ¶13(a)(c)
  the 7 Aug 2023 email + 10 Aug meeting; ¶17(a)(d) the delegate-interest text; ¶19(a) the
  4 Apr 2023 pay text; ¶20(a) pay issues raised "over the period of 2023 and 2024" (the
  pattern); ¶21(a)-(c) the AVAC chain 3→28 May (25 days, their own timeline).
  NET: nearly every EVENT is admitted somewhere across SOFC + Form 24; the live contest is
  characterisation ("reasonable in all respects" ×6) + the six unwitnessed causation words.
- ⭐⭐⭐ THE REGISTER OF THE READING (the closing synthesis, 10 Aug): cross-referencing the
  read-aloud 9A against the admissions ledger — most sentences Dwyer voiced were ADMITTED
  (destruction, PID, retraction, break, wrongful declines, prodrome, pay pattern) or
  functionally conceded; the only genuinely contested content voiced = the ADJECTIVES
  (hostile/capricious/suppression/reprisal — which the bench itself aired, so Cory need never
  say them again) + 1(a) particulars + the six causation words. ⇒ the mention was, in effect,
  the first oral recitation of a substantially AGREED chronology, performed by the tribunal to
  the parties who agreed it, unopposed (appearance-only). The accepting judgment's fact section
  has already been read aloud once — by its author. ⚠ Discipline forward: at hearing prove the
  NOUNS, retire the adjectives; the frame was voiced once by the bench and needs no repetition.
- ⭐⭐ THE DE FACTO CLINICAL RISK REGISTER (Cory's insight, 10 Aug): the Form 29 + 64G corpus,
  read with the admissions, now FUNCTIONS as the clinical risk register MSH never kept for the
  Switchboard: hazard identification (MET/on-call routing failures, fatigue at the code centre —
  his emails + the 9A 1(a) pathology-delay content), exposure data (the MET-call spreadsheet
  MSH says "is available"), incident record (the comm-book — its one contemporaneous entry, the
  on-call numbers, ADMITTED destroyed ¶12(a)), control state (no FRMS until after 30 Jun 2024,
  CE-signed), consultation record (none — ss 47-49), complaint history (items 3(a)/(b) — "not
  retained"), escalation/response (Item 20 — "does not exist"), disclosure (the PID re CLINICAL
  RISKS — ADMITTED ¶15, closed uninvestigated). ⇒ The only systematic documentation of that
  function's clinical risks in existence is HIS corpus; the institution's own register, on the
  record, is empty at every field. DEPLOYMENT: the union/Code channel + Stage 2 2.5 NOW (the
  psychosocial assessment request = asking MSH to build the register he has outlined); the PID
  track LATER; at the WC hearing it stays CONTEXT ONLY (Dwyer signalled patient-safety detail
  off the record at the mention; the injury case needs the fatigue keystone, not the clinical
  cascade). ⛔ No patient-harm claims — risks documented as RAISED, not as materialised.
- MATHESON AND THE CLINICAL RISK (banked 10 Aug): she cannot NOT have seen it — five proofs in
  her own file: (1) HER pleading admits the PID was about clinical risks (SOFC ¶15, her office's
  drafting); (2) HER 11 Jun disclosure produced the "Urgent: Issues Affecting Workplace Safety"
  emails; (3) the witness-conferencing haul her office received included ~47pp of FRMS-content
  material — the Regulator specifically collected fatigue-risk-management evidence; (4) her
  counsel WILLSON is a WHS-specialist barrister (the dual-role fact long banked — the one
  professional in the cast trained to read this as a systems-safety case; briefing her signals
  early classification of the matter as WHS-flavoured); (5) she sat through the 9A's 1(a)
  clinical-governance content read aloud and watched Dwyer contain it. STRUCTURAL NOTE
  (document, never allege): the WC Regulator sits within OIR, which also houses WHSQ — her
  file contains material that, in the other half of her agency, reads as compliance subject
  matter. EFFECT: the clinical dimension adds the systemic-embarrassment overlay to any lost
  public hearing and is fully priced in her advice pipeline via Willson — which is why patient
  safety needs NO voice at the hearing; its work in her risk assessment is already done.
- ⭐⭐⭐ FRMS BUNDLE DEEP-DIVE (11 Aug ~1am) — see FRMS-BUNDLE-DEEP-DIVE-11AUG2026.md. Four
  bombshells from Reese's own disclosed emails: B1 the RATING OF 11 (Reese+Taylor applied his
  risk matrix 10 May 2024, scored the roster MODERATE "at best", 5 weeks pre-onset); B2 "a few
  rostering errors... in past rosters" on his line — FALSIFIES SOFC ¶22(a) "not repeated"; B3
  the non-response was systemic (Reese herself chased HR unanswered, 10→20 May); B4 the roster
  consultation asymmetry ("Cory is not yet aware of this") + Reese validating his CASA citation
  as referenced in QH's own FRMS Implementation Guidelines. All from the Regulator's OWN
  disclosure, paginated "Renee Matheson". Feed: statement, Report B assumed facts, manner
  block, pleading impeachment. Follow-ups listed in the reference file.
- THE REGISTER MATCH, 2024 emails vs 2026 submissions (banked 11 Aug): seven shared
  fingerprints — courtesy-first openings; self-correction on the record ("I realized that I had
  been mistakenly referencing this section", 1 May 2024); instrument citation (Ops Manual
  s 4/10.4.1, Award, CASA → s 89, r 64G, cl 1.11); duty-framing ("It is incumbent upon
  management..."); attachments-as-receipts; standing offers ("happy to...", "I do not object
  and will attend"); dates as skeleton. Same voice, matured: 2026 = the 2024 voice with
  adjectives removed, asks isolated, bridges added. ONE stress-fracture: the 15 May "defrauds"
  line — a single heated phrase in two years, dated to the crisis peak — the deviation proves
  the baseline (clinically eloquent: written function preserved while attendance collapsed).
  Legal value: BIDIRECTIONAL AUTHENTICATION — the contemporaneous emails prove the filings
  aren't ghost-written; the filings prove the emails weren't aberrant; the premorbid
  conscientiousness exhibits itself across the whole arc.
- ⭐⭐⭐ THE CASE THESIS IN ITS FINAL FORM (Cory's, 11 Aug ~1:30am, after reading his own
  disclosure emails end to end): his emails were never fighting management — they were asking
  management to FOLLOW ITS OWN POLICY (the Ops Manual fatigue toolkit, the Award break, the QH
  FRMS guidelines Reese herself confirmed reference his CASA citation, the leave process, the
  consultation obligations). Every ask = "apply your own instrument." Their responses = the
  departures. ⇒ THE RMA INVERSION: the "management action" the defence protects is largely
  MSH's NON-COMPLIANCE with its own written standards; his pathologised "conduct" was
  policy-adherence advocacy. Legal edge: the employer's own policies are the classic objective
  yardstick of reasonable management — action inconsistent with the employer's own framework is
  the paradigm of "not taken in a reasonable way," and HIS emails cite the very instruments
  that define the benchmark. THE ONE-LINE CASE THEORY (closing-submission grade): "This is a
  case about an employee who asked his employer to follow its own policies — and what it cost
  him." For the doctor: the rule-follower watching the rules ignored = organisational justice
  erosion personified.
- ⭐⭐ THE ADVERSE READ OF THEIR DEFENCE FILE (Reese 50pp bundle mined, 11 Aug): THE HONEST
  INVENTORY AGAINST CORY — (1) late starts/long breaks/early finishes raised by Taylor — but
  their own note records it as GROUP-WIDE ("addressing this with other staff also... some staff
  including Cory") and his engagement ("thought he did call... usually does but not always");
  (2) one under-2-hours shift notice, hedged ("I think"), timed MID-JUNE 2024 = the
  decompensation peak — and the planned "behavioural issues" discussion NEVER HAPPENED because
  he was on sick leave ⇒ NO conduct process was ever run; nothing was put, tested or found;
  (3) ⚠ THE ONE REAL ITEM: the comm-book confrontation (Taylor's 6 Jun 2023 email): "aggressive
  tone and raised voice... talking over the top of me. I DID RAISE MY VOICE" — one incident,
  12 months pre-onset, MUTUAL (her words), inside the email that ADMITS the removal ("I took it
  out last week") + her "burn book" contempt + his contemporaneous "he feels like he is being
  attacked" (distress documented Jun 2023). STATEMENT GUIDANCE: OWN IT if asked — owned it is
  human; denied it is a credibility wound; (4) colleague hearsay ("comments towards management
  and rostering... IR have been made aware") — hearsay, true in substance; (5) the multitasking
  frustration note — which DOCUMENTS his pre-onset exhaustion and disproportionate call volume
  ("he feels exhausted... others are not picking the same call volume") with Reese routing it
  to call-stats review = a verifiable workload claim.
  BONUS ADMISSIONS inside the same bundle: Reese acknowledges the 21.8.23 roster went out LATE
  (another process failure owned); the 29/8/23 meeting record confirms his roster concerns +
  additional-shifts request; his 12-hr roster proposal critiqued on reasoned grounds (their
  best genuine-engagement evidence, 2023).
  VERDICT: their defence file nets FOR him — every adverse item is mitigated/unprocessed/
  hedged/mutual/symptom-timed, and the file's credible witness (Reese reads conscientious)
  AUTHENTICATES the admissions her own documents carry (rating of 11, plural errors, late
  roster, unanswered chases). ⚠ Willson's cross-mosaic = comm book + notice + hallway comments
  ("difficult colleague") — counter = ownership + dates + group-wide/mutual/never-processed.
  The deepest finding: THE CONDUCT CONVERSATIONS NEVER OCCURRED — none of it was ever put to
  him; unraised contemporaneous allegations carry little hearing weight.
- ⭐⭐ THE AUTHORSHIP SPLIT (Cory's precision correction, 11 Aug): audit the adverse inventory
  BY AUTHORSHIP — of the five adverse items, the number in HIS OWN HAND = ZERO. The
  confrontation = HER account of an oral exchange (his comm-book ENTRY itself was professional
  — the on-call numbers instruction); the lateness = their characterisation; the notice = their
  hedged recollection; the hallway comments = double hearsay. His single authored heat in five
  years = the 15 May "defrauds" line. ⇒ THE EVIDENTIARY ASYMMETRY: his case rests on THEIR
  WRITINGS (fixed, tendered, theirs); their case rests on THEIR INTERPRETATIONS OF HIS SPEECH
  (contested recollection, cross-examinable, Briginshaw-weighted). Documents beat memories.
  Statement handling refined: own the comm-book MOMENT as his experience WITHOUT adopting her
  adjectives — his account of the same exchange; the only mutually agreed fact is that voices
  rose (hers too, her admission).
- ⭐⭐ TAYLOR'S SELF-NARRATION PATTERN (Cory's read, 11 Aug — correct): her 6 Jun 2023 email is
  a PRE-EMPTIVE SELF-REPORT, not neutral evidence — written same afternoon TO the Director,
  by the person whose own conduct was in question (the removal, admitted mid-email), opening
  with HIS approach not HER removal, adjectives one-directional ("aggressive"/"wouldn't let me
  speak" vs her minimised "I did raise my voice and asked him to please stop"), bolstered with
  hallway hearsay, plus the "burn book" contempt line. THE PATTERN ACROSS THE RECORD: three
  self-narrations by the same witness, each following her own exposure — (1) 6 Jun 2023 (after
  the removal was questioned); (2) 17 May 2024 account "as requested" (after the retraction);
  (3) the "out to get me" HR email (after PID knowledge reached management). Cross-exam
  architecture (dates, never motive): "each time your conduct was questioned, you wrote an
  account to your Director" — the timestamps do the work. EVIDENTIARY WEIGHT: a self-serving
  contemporaneous account is NOT corroboration — it is the same witness, twice; HIS version of
  the June 2023 incident EXISTS IN WRITING via the 7 Aug 2023 grievance + Reese's own 29/8/23
  meeting summary ("Concerns about Chloe") — competing written accounts, his corroborated by
  their documents, hers by herself.

## 11 Aug 2026 (morning) — PETERING REPLY + 4:30PM CALL PREP
- ⭐⭐ EMILY PETERING REPLIED Tue 11 Aug 09:27 (to the 10 Aug 7:55pm union email; cc Moran):
  tried to CALL first + voicemail; "I have significant concerns about the course of action
  you're proposing in your email"; offers 4:30pm TODAY (despite "a number of commitments with
  other members") or Thursday morning; union office CLOSED Wed 12 Aug (Brisbane show day /
  Ekka People's Day). Upload: e208c141-Outlook_Document184.PDF.
- CLOSE READING (banked): (1) read + triaged FIRST THING next morning = priority handling;
  (2) speed driven by HIS "refer Stage 2 week commencing Mon 10 Aug" line — the email is an
  INTERCEPT (reach him before lodgement); (3) concern scoped to "the course of action you're
  proposing" — the PLAN, not his facts/grievances/person; (4) "advice on the points you raise"
  = read point-by-point, per-point responses formed; (5) substance moved to PHONE deliberately
  — zero substantive content or particulars in writing (whatever the concerns are, she won't
  email them = sensitive: delegate deployment / union-name decision / other-member landscape /
  welfare); (6) does NOT say "don't lodge" but the whole email functionally requests a hold;
  (7) warm bookends ("Hi Cory... soon Cory"), cc Heath = office-aligned position, relationship
  intact; (8) answers NONE of the three asks in writing (delegate confirm / union-name
  referral / Stage 2 form-recipient).
- FACTS SETTLED THIS MORNING: Cory IS the union delegate (his confirmation — removes the
  "can't confirm" concern candidate); psychiatrist appointment is GOLD COAST (show day is
  per-LGA; Wed 12 Aug = Brisbane only) — WEDNESDAY APPOINTMENT UNAFFECTED, confirmed by Cory.
- ⭐ CONCERNS AS FINALLY RANKED (with the assumption the department has MANY issues / other
  members — Cory's instruction to assume): (1) COLLISION with existing union activity in the
  department he can't see (other members' matters; confidentiality = phone-only); (2) THE LANE
  PROBLEM — collective issues travelling inside his personal Stage 2 lets MSH dismiss the
  systems case as one unwell employee's grievance AND makes his dispute the lens on the
  department; union likely wants the collective piece in ITS lane, his Stage 2 narrowed to the
  irreducibly-personal core (exclusion/pay/leave) — i.e., HIS OWN ARGUMENT MIRRORED ("coming
  only from me it keeps being folded back into a medical process about me"); (3) DELEGATE
  DEPLOYMENT while excluded = a card played once (exclusion becomes an industrial incident;
  he becomes the face of the collective case; site-representation question) — union wants it
  deliberate or held; (4) sequencing vs the medical process (Stage 2 mid-RFMI = "awaiting
  medical information" answer); (5) welfare / load-shedding. NOT on the list: the merits of
  his workplace claims (a problem department validates the systems framing).
- STRATEGIC READ: if the call runs "we take the collective piece, you keep pay-and-leave
  narrowed, hold the delegate card" that is the UNION BUYING THE COLLECTIVE HALF OF HIS CASE
  — converts one-person-systems-case into institution-vs-institution, the frame sought since
  the first email. Only TEMPO is negotiable: the pay/leave core (5 weeks unpaid) presses
  regardless; short hold of lodgement costs nothing; the 24 Aug cl 10.3.6 deemed-refusal
  clock (E2 request) runs independently of anything agreed on this call.
- Call prep sheet: drafts/CALL_PREP_PETERING_430PM_11AUG.md
- ATTACHMENT SET AS EMILY HOLDS IT (all four read from source, 11 Aug): (A1) Stage 1 notice
  4pp — 2.1-2.6 scope; status-quo-incl-pay claim; s 36 hierarchy pre-rebuttal; part 5 conflict
  question; "I have a phrase. I do not have a process." (A2) Taylor 4 Aug — ADMITS valid
  lodgement + "the 24-hour timeframe... will not be achieved" + "I am required to process
  leave on your behalf" with same-day payroll default = disputed subject matter changed
  MID-dispute against cl 1.11.4, in writing. (A3) his response 4pp — §4 INSURER CONTRADICTION
  (ART Life told "currently unable to accommodate a graduated return to work" while he's told
  "under review"; RFMI Q9 premise pre-adopted); §1 no consent + Directive 12/24 special leave
  ask; §5 neither-wages-nor-benefit; seven questions unanswered. (A4) Stage 2 referral 3pp —
  1.1-1.6 record in their own words; "That date has been reached"; 2.1-2.6 agenda; §4 open
  union note; instruments footer. (A5 cited-sections pack NOT in repo — assembled by Cory
  separately; contents = the instruments footer list.)
- ⭐ CONCERN ANCHORS IN THE TEXT (refined after reading what she read): (1) MOST LIKELY
  TRIGGER = Stage 2 opening line — CE-letter reference + demand for "an officer independent
  of the matters in dispute" (imports the governance/conflict theme into the industrial
  track); (2) item 2.5 = the lane problem in text (systems case inside personal referral);
  (3) Part 2 scope (six composite items vs 7-day conference) → expect narrowing to 2.1-2.2;
  (4) §4 insurer issue may be flagged AS serious → own channel (privacy/complaint route);
  (5) tone is NOT a concern — zero intemperate sentences across all four documents.
- LIKELY UNION ADVICE SHAPE: keep the airtight procedural core (1.1-1.6 + 2.1-2.2); union
  takes 2.5/systems; park independence demand + CE-thread out of industrial track; insurer
  issue to its own channel. ALL acceptable — the fixed point (pay/leave from 26 Jun) sits
  wholly inside what she'd keep.
- ⭐ PETERING PRIOR EMAIL (earlier call, pre-10-Aug — provided by Cory 11 Aug): shows her
  position has been CONSISTENT across all three communications (capacity information first →
  employer assesses → then act) — the 11 Aug "significant concerns" was consistency, not
  reaction; his 10 Aug email departed from her already-stated sequence. TWO BANKED TEST-LINES
  (union-authored, in writing, deployable at Stage 2): (1) "Your employer should not be
  making medical decisions about what you are fit to do. The relevant medical advice should
  come from your treating doctor" — MSH holding him out DESPITE the fit-with-restrictions ECC
  = employer substituting its own medical judgment = fails the union's own test (pairs with
  the G3 asymmetry); (2) her earlier "communicate their position" test (11 Aug email). ALSO:
  her consent/gatekeeping advice ("requests for medical information provided directly to you
  first, rather than permitting unrestricted direct communication") = EXACTLY the 3 Aug
  architecture he already built — instincts and professional advice identical. OPERATIONAL:
  (a) STANDING REQUEST — when Report A exists, send a copy to EMILY at the same time as MSH
  (union holds the document while the engagement clock runs); (b) her WC-separation line =
  union-endorsed Report A/B boundary; (c) SUBSTANTIVE ROLE FIRST — do not lead with
  alternative duties/redeployment (concedes the substantive role is in question; their
  argument, not his); alternative-duties card stays in the deck. Same forensic fingerprints
  as the 11 Aug letter (headed sections, graded hedges, element-form tests, agency
  preservation) — profile holds.
- ⭐ PETERING TWO-EMAIL FORENSIC DISSECTION (comprehension audit, 11 Aug): FULL COMPREHENSION
  MARKERS — (1) compressed the case to the opacity of the decision state ("exactly where your
  employer's consideration... is up to" = his 2.6 in one sentence, from a phone call);
  (2) diagnosed the mechanism unprompted ("employer should not be making medical decisions" =
  the certificate-overridden defect / G3 asymmetry); (3) understands the game (specificity of
  medical advice removes employer discretion = closes stall hatches); (4) ⭐⭐ independently
  spotted the RFMI dual-use/discovery risk ("requests... beyond your current capacity...
  identify exactly what is being sought before providing") = the file's own Q9 harvesting
  analysis, reached from a phone call; (5) real-time correction of the redeployment misstep
  (substantive role first — alternatives concede the role is in question); (6) audited MSH's
  position and found no legitimate obstacle ("exactly what is preventing"); (7) evidence
  filter (banked past workload/roster management as workability-of-adjustments proof);
  (8) instrument-vs-conduct dissection (RFMI questions standard / process "not necessarily
  handled well"); (9) stall taxonomy in the trigger (engage / meaningful updates / explain
  continuing delay); (10) the fork pre-labelled (decide or manufacture remaining concerns).
  THE SILENCES (deliberate scoping, not gaps — she demonstrably read the attachments):
  never papers cl 1.11.4 pay/status-quo claim, the insurer contradiction, the PID, or any
  individual's name — parks contested/explosive material rather than endorsing it in writing.
  HER MODEL = the tractable RTW core (certified-fit member + opaque employer + specificity
  forcing + provable failure modes + escalate). ⚠ DISCIPLINE: her model is deliberately
  NARROWER than the matter — the accountability layer (pay remedy, process breaches, insurer
  conduct, PID context, psychosocial systems) is SEQUENCED, not resolved, and is carried by
  HIS file alone (Stage 2 draft 2.2/2.4 + the tracks). Her lane first is correct — a
  returned, paid employee prosecutes the accountability layer from stronger ground — but her
  silence on those items must never be read as their resolution.
- ⭐ NEW FACT (Cory's recollection, 11 Aug — not previously banked): HEATH MORAN said he had
  taken the matters to a CONFERENCE OF THE INDUSTRIAL OFFICERS before/around the referral to
  Petering. Chain now: documents → Heath "this is serious" → collective IO conference on the
  matters → allocation to Petering (senior carriage, Heath retained on Cc). IMPLICATIONS:
  (1) Emily's positions are likely TEAM-VETTED — the two emails read as Together's
  institutional position delivered through its assigned officer (explains the consistency and
  the office-aligned handling); (2) the parked asks (union-name referral / psychosocial
  assessment / delegate confirmation) were almost certainly IN THE ROOM at that conference —
  her written silence = position still forming, nothing papered until settled; institutional
  answers to come; (3) the department landscape (other members/history at Logan Switchboard)
  would have surfaced at the conference — her "course of action" concerns were assessed
  against a map Cory can't see; (4) continuity insurance — a conferenced matter with senior
  carriage stays on the team's board. THE REVEALED-BEHAVIOUR LEDGER (4 institutions, 6 weeks,
  same file, all read it as serious): Dwyer (10am Friday mention slot); Cridland's office
  (67-minute acknowledgment at personal direction); the Regulator (soft disclosure signal via
  appeals officer); Together (IO conference + senior allocation). Objective external
  validation via institutional behaviour, not modelling.
- ASSEMBLY FEEDBACK + EXTERNAL SECOND-OPINION BRIEF (11 Aug): comprehensive self-audit of
  the matter's assembly delivered. STRENGTHS confirmed: verification-before-assertion;
  two-audience record-building; chronology-never-motive; removable-module design; admission
  mining; sequencing restraint. ⚠ COULD-BE-BETTER LIST (the honest seven): (1) single-point-
  of-failure — get a ONE-OFF professional review of the two highest-stakes documents (Report
  B LOI; Calderbank #3) via direct-access counsel or CLC; (2) VERIFICATION DEBT rule adopted:
  no new analytical pass while a verification item feeding a servable document is open;
  (3) analysis-to-action ratio — the file is done enough; marginal hours go to rest, the
  debt list, and statement gap items, not re-confirmation; (4) CONTINGENCY for the hinge:
  define plan B before the appointment (alternative IME pathway + a chase rule for report
  delay); (5) multiplicity temptation is structural — counsel presents if it reaches
  hearing; (6) financial RUNWAY plan deserves the same rigour as the legal file; (7) build a
  two-page COUNSEL HANDOVER BRIEF (case theory, keystone, admissions register,
  prohibitions). EXTERNAL AI BRIEF: drafts/GROK_BRIEF_method_critique.txt — sanitised,
  method-critique-only, with the do-not-add exclusion list; replies = red-team input,
  verified before acted on.
- ⭐⭐ REPORT B QUESTIONS+EVIDENCE PACK AUDITED (uploaded 11 Aug, 165pp/186 bookmarks/31MB,
  "REPORT_B_QUESTIONS_AND_EVIDENCE_BOOKMARKS.pdf"): assembly = expert-briefing instrument
  (cover reading order → 18 Q-pages with pinned evidence lists → Form 24 ×3 incl key-
  admissions schedule → 9A + stressor map → LOI/chronology/Form 20 spine → themed proof
  E–J → jump list). Fact anchors verified vs banked record (onset 18 Jun; WCC 1 Jul; CS-3
  31 Aug 2023; FT mid-Oct 2023; 16 Nov 2023 baseline; Krishnaiah 13 Feb 2025; competing
  causes ~Oct/Dec 2024). Quality: above most solicitor briefs. ⛔ STRUCTURAL FLAW: Q6.4
  (complete sources list) makes the pack DISCOVERABLE — it will appear in the report's
  sources; audit standard = "as read by Willson". FIX LIST (before tomorrow): (1) STRIP
  QL0–QL6 ("Later Q if asked") from the doctor's copy — written contingency questions =
  instructions not in the served LOI (11 vs 18 mismatch = cross-exam gift); they return to
  CORY'S question map, oral only; evidence stays in E–J; (2) label sweep: "Hours double
  standard"→"Hours requests and responses — sequence"; cover "CASE THEORY:"→"ASSUMED
  CHRONOLOGY (per pleadings):"; Q6.8 drop "Do not merely repeat earlier characterisations"
  → "from your own current assessment"; bookmark "Stressor 1 hostile course start"→
  "Stressor 1 (as pleaded)"; (3) bereavement date still missing at Q6.7 — add to chronology
  or supply orally (gap-list item); (4) logistics: 31MB may bounce email — confirm delivery
  channel with clinic TODAY; bookmarks panel not auto-open everywhere (cover line + p.X pins
  mitigate); (5) oral triage line for the doctor: 30pp core = questions + chronology p.26 +
  admissions p.34 + March roster p.55 + CE letter p.62. Boundary check PASSED: no Report A
  material, no deed, no rule-10 items. Verdict: 9/10 with one structural error; fixes are
  small and tonight-sized.
- ⛔ AUDIENCE RULE BANKED (11 Aug): the Report B questions+evidence pack NEVER goes to
  Matheson — it is trial architecture made visible (theory cover, question steering, QL
  contingencies, section skeleton = closing structure, jump list = proof map). Work product;
  arrangement is the asset. She receives: Report B when served (with its sources list);
  instruction materials only if properly requested (why the four pack fixes matter —
  producible without embarrassment). ⭐ THE MATHESON SETTLEMENT BUNDLE (rides with Calderbank
  #3, post-report, ~30pp, admissions-forward, arranged so the accepting judgment visibly
  writes itself): (1) Calderbank cover (W5 damages para + s 558(3)); (2) Report B;
  (3) one-page chronology; (4) KEY-ADMISSIONS SCHEDULE (their own pleading: 7-hr break human
  error, page removal, PID ¶15, wrongful declines, prodrome); (5) March 2024 roster page;
  (6) CE letter FRMS-gap extract; (7) the 10 May 2024 rating-of-11 page (her own
  disclosure). Every enclosure except the report and roster is THEIRS. Principle: the two
  instruments (doctor's pack / Matheson bundle) never swap audiences.
- HEARING-READINESS MAP vs AMENDED 9A (11 Aug): the pack = documentary spine (~70% of
  hearing-readiness): Stressor 3 best-proved (roster/pairing, Att 6, CE FRMS gap, guideline,
  chains, 1 May refusal); Stressor 2 (AVAC chain, 21 May, NNPD); Stressor 1 (MASPER CS-1,
  comm book ×2, PID outcome, retract strand, hours sequence); baseline medical; Form 24 ×3.
  Contest at hearing is narrow (diagnosis + six causation words + "reasonable" ×6) since
  events largely admitted. FIVE MISSING COMPONENTS to "run the 9A": (1) Report B (pending
  Wed); (2) HIS SIGNED STATEMENT — biggest unbuilt piece (gap list already banked: comm-book
  owned, call-up frequency, roster arithmetic, "other staff member" fact, FT dates,
  bereavement date); (3) corroborating witness statements — Patrisha Co (Anh Doan call)
  named in his own email, no statement exists; decide list + summons needs; (4) ⚠ FRMS
  disclosure pages ABSENT from pack — rating-of-11 (10 May 2024) + "a few rostering errors"
  line not in bookmark tree; add to section E on rebuild + hearing bundle (rating page
  already specced for Matheson bundle); (5) legal layer — authorities to ratio (open debt),
  submissions outline (one-mechanism), cross plans (Taylor timestamps → actual plan).
  SEQUENCE UNCHANGED: pack feeds report → settlement bundle → hearing brief only if
  Calderbank #3 fails (counsel presents). Components 2–4 build calmly post-report.
- FULL REPO-vs-PACK SWEEP (11 Aug): ADDS (ranked): (1) FRMS bundle key pages — rating-of-11
  10 May 2024 + "a few rostering errors... past rosters" + Reese unanswered chases (feeds
  Q6.9); (2) 2023-09-27 Taylor FT APPROVAL ("very pleased... 16 Oct 2023") — completes CS-3
  trajectory arc (Q6.1/6.3/QL0); (3) Hawes WCC 8 Sep 2024 — continuing incapacity/course
  (Q6.11); (4) MSH production system records — Item 15 Leave Takings 19 Mar 2024 + Item 11
  myHR/pandemic leave forms (system corroboration of Att 6 + COVID declines); (5) CONTENT
  CHECK: chronology one-page must carry 13-15 May 2024 attendance-difficulty prodrome (SOFC
  ¶16(b)(i), their pleading; SOFC itself correctly excluded); (6) JUDGMENT CALL: Review
  Decision 69983 — lean INCLUDE listed last (kills "did you read the decision?" cross beat;
  de novo exclusion also defensible if deliberate). VERIFY TONIGHT: (a) ⚠ E23 authorship —
  repo file is MindAndMemory_report_QSuper_LouiseIngs 13 Feb 2025; if Ings not Krishnaiah,
  fix label + reword Q6.11 premise; (b) 4 Apr 2023 pay text (¶19(a)) — confirm inside
  "phone photos" or add to J; (c) Individual_monthly_stats_April2025.xlsx — if call-volume
  data = only quantified role-load evidence (QL1), check contents. CORRECT EXCLUSIONS
  CONFIRMED: 18 May "issues" email (defrauds); Reese/Taylor accounts; 8 Sep 2025 letter
  (oral-ready only); deed/WP/DFV/rule-10; SOFC whole document. Verdict: one major omission
  (FRMS pages), four corroborating adds, one label verify, one judgment call — otherwise
  the pack captured the repo completely.
- ATTRIBUTION CHECK (11 Aug, Cory asked "Griffin wrote about the 8-hour agreement?"):
  corrected — it was FORREST (MSH HR), twice in writing (7 Jul 2026 ECC-further-information
  letter + later July response): the 17 Jun 2020 agreement "is only applied where staff
  initiated shift swaps have occurred" → 17-18 Mar 2024 was manager-rostered, not a swap →
  on MSH's own statement the 8-hr agreement did NOT apply → floor was 10 hours → breach is
  7-vs-10 → undercuts SOFC ¶22(e). DECISION: NOT in the doctor's pack (legal not clinical;
  pack is Q6.4-discoverable and this is the banked do-not-flag quiet weapon — ¶22(e) must
  arrive at hearing unrepaired). Documents already in repo as PDFs — nothing to print.
  Fires at: hearing contradiction matrix (home); OPTIONAL one sentence in Calderbank #3
  (raises Matheson risk vs tips the point early — decide at Calderbank drafting, not now).
- LEAN PACK v2 AUDIT (REPORT_B_LEAN_DOCTOR_PACK.pdf, 174pp, 11 Aug): fixes APPLIED by Cory:
  QL pages removed ✓; neutral labels ✓; FRMS-11/FT-approval/Hawes-Sep/Item15/Item11/RD
  added ✓; E23 resolved (Krishnaiah author, Ings recipient) ✓; Q6.11 retitled ✓; chronology
  carries 13-15 May ✓. ⛔ THREE REMAINING DEFECTS (Cory spotted, verified): (1) ALL printed
  question-page pins STALE (old 165pp layout): E01 p22→34, E02 p26→38, E05 p34→13, E06
  p40→41, E19 p101→87, E21 p110→93, E22 p113→96, E23 p114→97; matrix→32, 9A→27, roster→56,
  Att6→58, CE→60; regenerate ALL from final positions (links/bookmarks resolve correctly —
  print pins don't); (2) new adds NOT WIRED IN: no E-numbers, cited on zero question pages —
  assign E35 FRMS-11 p159 (→Q6.6+Q6.9), E36 FT approval p160 (→Q6.1+Q6.3; verified by
  render: "very pleased... 16th October 2023" + HIS gracious 28 Sep reply beneath = premorbid
  voice bonus, keep), E37 Hawes-Sep p161 (→Q6.11), E38 Item15 p162 + E39 Item11 p163
  (→Q6.6), E40 RD p166 (→Q6.4 completeness note); (3) COVER rewrite (full replacement text
  provided in chat): remove "as prodrome marker" (clinical conclusion supplied), remove
  "= pre-injury engagement" equation, remove "Minimize dump · selected originals only"
  (note-to-self), add "navigate by bookmarks — bookmark order is reading order; physical
  order differs", dates-as-documents-show-them paragraph, fuller independence statement.
  Physical-vs-bookmark divergence (adds at pp.155-174) accepted via the cover line rather
  than reorder.
- ⭐⭐⭐ MASTER SPEC WRITTEN: skill/references/REPORT-B-PACK-MASTER-SPEC-11AUG2026.md — the
  complete consolidated build instruction for the doctor's pack: design doctrine (discovery
  not instruction; five conclusion→evidence designs; chronology as master instrument; three
  readers), content manifest (sections A–J, E-codes frozen, exclusions locked), six-layer
  navigation architecture (cover hub / bookmark grammar / banners+return links / question
  switchboards / linked chronology spine / alphabetical jump list), conventions, the
  10-step BUILD PIPELINE (named destinations kill the stale-pin bug class; programmatic
  pins; OCR; optimize<20MB), the QA CHECKLIST (pin verification, dead-link walk, search
  test, STEERING SWEEP grep list, wiring check, boundary sweep, two-click rule), delivery
  (30pp printed core + oral layer), and freeze/change control (immutable after the report
  cites E-codes; corrections as dated supplements). Supersedes the scattered audit notes as
  the build authority.
- ⭐⭐⭐ DOCTOR'S PACK BUILT BY CLAUDE (v-final, 11 Aug): REPORT_B_DOCTOR_PACK_FINAL_11AUG.pdf
  — 170pp, built per the master spec from Cory's lean pack v2. Executed: physical reorder to
  bookmark order (sections contiguous, adds inlined); front matter regenerated (cover per
  spec with 10 live links; Q6.1–6.11 with computed pins + live links, evidence ordered by
  probative weight); E38–E43 assigned + wired (E38 FRMS-11 first line of Q6.6/6.9; E39
  approval → Q6.1/6.3; E40 → Q6.11; E41/E42 → Q6.6; E43 → Q6.4 note); full bookmark tree
  rebuilt 125 nodes date·author grammar incl. the governance cluster v2 had DROPPED (MASPER,
  comm book, COVID, PID, ESU, CS-4, retract — restored); ◂Questions return-link on every
  body page; internal note pages (164-165) REMOVED; steering purged from our hand — "double
  standard" banners (visual+text via rasterize), "Chloe pattern" labels, "COVID leave
  obstruction" banner, cover self-notes, Q6.5 "union suppression"→neutral, Q6.8 rewritten;
  ⛔ E00 MATRIX REMOVED from doctor's pack (saturated with "Clinical use" coaching lines +
  notes-to-self — reassigned to PACK 2 as the hearing tool it is); metadata scrubbed (Cory
  authorship only); linearized. QA PASSED: 58/58 pins correct · 227 links 0 dead ·
  steering/boundary sweeps clean (only p28 = the filed 9A's own pleaded words) · 125
  bookmarks · 34MB (no gs in env — image downsampling + OCR of image pages remain LOCAL
  tasks if wanted; bookmarks+pins mitigate). Build system banked: drafts/
  build_reportb_pack_final.py + reportb_qtexts.json (single-script regeneration; the script
  is the source of truth per spec §4). Pack sent to Cory.
- ⛔→✅ LOI-ALIGNMENT CORRECTION (Cory caught it — "this is all incorrect read it", quoting LOI
  §5 enclosures): my v3/v5 build CONTRADICTED the served letter of instruction. Errors fixed
  in the v6 rebuild (REPORT_B_DOCTOR_PACK_LOI_ALIGNED_SEND.pdf, 156pp, delivered): (1) the
  ASSUMED FACTS are Enclosure A (signed statement) corroborated by B (chronology) + D
  (admissions) — LOI ¶4 — NOT the 9A and NOT the Form 20; (2) the 9A is Enclosure C, dated
  7 APRIL 2026, "scope and context only... not facts you are asked to assume"; "not a case
  of bullying or harassment"; (3) HAWES IS ONE CERTIFICATE (Enclosure F: records first
  attendance 1 Jul 2024, SIGNED 8 SEP 2024) — my two-certificates story (E22+E40) was wrong;
  verified on the certificate's face (injury 18/06/2024 · first seen 01/07/2024); merged +
  re-bannered + rasterized; (4) question pages now VERBATIM LOI 6.1–6.11 (v2's enriched
  paraphrases removed — same instructions-mismatch class as the QL pages); (5)
  enclosure-letter labelling throughout (A–H) so the report's citations match the LOI;
  E-code system retired from front matter; (6) FORM 20 REMOVED (not an enclosure; its
  "assumed-facts spine" banner contradicted LOI ¶4); (7) Enclosure A NOTE PAGE inserted
  (statement provided separately; assumed-facts hierarchy stated). QA: 52 pins verified ·
  207 links 0 dead · sweeps clean (p28 = 9A's own pleaded words only) · 123 bookmarks ·
  22.3 MiB. ⚠ STANDING FLAGS: the LOI in the pack still carries [Date]/[email]/[date]
  blanks — complete before service; ⛔ ENCLOSURE A (the signed statement) DOES NOT EXIST
  YET — it is the foundation of the assumed facts and the pack's Q6.5/6.9 point to its note
  page; building it is the top post-appointment task. Build script:
  drafts/build_reportb_pack_LOI_aligned.py (supersedes build_reportb_pack_final.py).
- ⭐⭐⭐ THE 9C AS A DELANEY MACHINE (9A-vs-9C forensic, case-law weighted, 11 Aug — revises
  the "unwitting" read partway): the 9C's oddities align with ONE authority = deliberate
  global-evaluation architecture (the same method that won Review 69983 — unreasonable break
  FOUND, claim denied globally): (1) ¶22(a) "human error" = the BLEMISH CONCESSION (Dwyer's
  own word at the mention — bench knows the fight): concede the isolated defect so the
  course absorbs it; (2) "not repeated" = the ISOLATION CLAMP — an otherwise unnecessary
  sentence; single error absorbable, pattern fatal ⇒ the FRMS "a few rostering errors...in
  past rosters" line BREAKS THE CLAMP (their own disclosure) — its highest strategic value
  now understood; (3) FLATTENING — the break processed as just item N, "reasonable in all
  respects" ×6 flat refrain = converting his Mahaffey case into a Delaney case (13 mini-
  trials invite global weighing; one tall keystone defeats it) — the one-mechanism
  discipline is the refusal of that conversion; (4) ¶11 particulars attack on 1(a) = the
  Carr counter (prune the vague strand); (5) ¶25 post-dating = temporal filter — partial
  force only: no answer to ss 32(3)(b)/(4) aggravation + their ¶16(b)(i) prodrome admission
  hands an onset window predating the filtered items; (6) empty ¶27 + six causation words =
  POWDER DELIBERATELY DRY (repeat player post-disclosure won't commit to a theory its own
  rating-of-11 could contradict; the denying judgment's empty chair is being HELD for a
  future IME); (7) 32(5)(b) recited-not-contended = ARMED TRIPWIRE (amendment/submissions if
  his oral evidence drifts into perception vocabulary — the never-say-perception rule is the
  weld). COUNTER-MAP (all already in-file): Mahaffey keystone + Report B Q6.5; FRMS lines v
  the clamp; one-mechanism v flattening; aggravation + prodrome v the filter; report-first
  sequencing v dry powder; two-year clean record v the tripwire. ⚠ Delaney/Mahaffey still on
  the read-to-ratio list before any filed use.
- ⭐⭐ THE PID CONTAINMENT-AND-SEVERANCE PLAY (Cory's read, 11 Aug — correct; refines the
  Delaney-machine model for the PID strand): the 9C's design re the PID = (1) ADMIT the
  disclosure completely (¶15 — denial impossible post-ESU determination; SAFE in this forum
  because the 9A pleads the PID as stressor-event, not reprisal — forum containment: the WC
  appeal never asks the reprisal question); (2) SEVER the knowledge wire at the one dangerous
  May-2024 junction — ¶16(a) Reese unaware of PID at the retraction (kills the 48-hour
  adjacency inference); (3) CROP the frame — the 9C says nothing about what happened TO the
  PID (routing, ten months, closed uninvestigated 24 Dec 2024 during his incapacity,
  operational response "does not exist" per CE letter). ⚠ DISCIPLINE: do NOT fight
  Reese-unaware — our own verified record supports it (Harrison→three HR officers, not
  Taylor/Reese; McGinley escalated) — and it defeats an argument we never make: the
  retraction is manner-unreasonable REGARDLESS of knowledge (direction to retract a written
  concern + email removed from server (their words) + no process + same week as their
  rating-of-11). Chronology, manner, system — no motive. THE ACCIDENTAL GIFT: severance
  covers May 2024 ONLY; the 2025-26 knowledge chain is theirs end-to-end in writing
  (Griffin, Tribunal Matters cc'd, refused non-reprisal clause) — and ¶15 permanently ADMITS
  the protected act for the held track: to defuse the PID where it's harmless they banked it
  where it isn't. Full model: Delaney machine (fatigue course) + containment-and-severance
  (PID strand); both answered by keystone + chronology + the drawer.
- THE FOUNDATION UNDER THE CONTAINMENT (Cory, 11 Aug): the PID was VALIDATED and the patient
  safety concern was TRUE — which is WHY containment is their only available strategy: (1)
  their own ESU certified the disclosure; their own remediation corroborates the substance
  (FRMS implemented after 30 Jun 2024 = behaving as if he was right; rating-of-11; the
  2-hour pathologist delay); the substance is unattackable → shrink frame/cut wire/crop
  aftermath; (2) the TRUTH is why 32(5)(b) was abandoned — cannot run "perception" against a
  disclosure their own unit validated; (3) truth INVERTS the aftermath: retracting a TRUE
  safety concern (email removed from server) = suppression of accurate safety information;
  closing a VALIDATED disclosure uninvestigated during the discloser's incapacity = the
  system failing its own test — validation converts process into evidence; (4) CLINICAL (for
  the room, dates only): he carried an unvalidated truth through the whole exposure window —
  validation 24 Dec 2024 = six months POST-onset; right-and-unheard in a safety-critical
  role = the organisational-justice erosion Q6.9 reaches; the doctor does the arithmetic
  (13 May disclosure · 18 Jun onset · 24 Dec validation); (5) hearing calculus: publicly
  attacking a validated patient-safety PID = institutional self-harm, priced into Matheson's
  risk — the gravity their defence orbits without touching.
- ⭐⭐⭐ ORIGINAL-vs-AMENDED 9C DIFF (full structural diff run 11 Aug; orig Jul 2025 vs amended
  13 May 2026 — the strategy IN MOTION; every change responds 1:1 to HIS amended 9A):
  NEW INSERTIONS (deliberate): (1) ¶16(a) Reese-unaware-of-PID — knowledge severance DID NOT
  EXIST in original; added when his 1(f) pleaded the 48-hr adjacency; (2) ¶22(f) "not
  causative" six words — ADDED onto the keystone alone when his amendment elevated it = ⭐
  TARGETING CONFESSION (their only causation firewall placed on the one item they think
  decides the case); (3) ¶8 past-history-of-anxiety contest (anti-baseline move); (4) ¶25
  post-dating filter (answering his post-injury section); (5) ¶14(e)-(f) NEW ADMISSION
  attachments "were in fact present" + "human error... on the background of HIGH WORK
  DEMANDS" — ⭐ they pleaded the demand environment to excuse Taylor = Q6.9's demand limb
  supplied by the respondent; (6) full 1(g) delegate rebuttal built; (7) Easter figure
  "$1,500.00" → "42% less" — THEY ADOPTED HIS UNITS (his pleading sets the terms);
  (8) ¶10 admits Hawes certificate + QUOTES its mechanism ("ongoing breaking of workplace
  rules by bosses, victimizing him") before denying — the treating doctor's causation words
  now recited inside their pleading; (9) ¶16(b) timestamps NEW: his email 1.15pm → Taylor to
  Reese 1.20pm = ⭐ THE FIVE-MINUTE ESCALATION (vs 25-day AVAC) — institutional-urgency
  asymmetry timestamped by them; (10) amended intro confirms 9A dated 7 APRIL 2026.
  DELETIONS (retreats): the denial that he told Taylor he was exhausted (old ¶20(c)) — GONE;
  14 Jan 2024 lateness engagement — GONE. THE VISIBLE IME SKELETON: ¶8 anxiety + ¶25
  post-dating + ¶22(f) = the denying judgment's draft theory, pre-answered by the LOI
  (Q6.3 aggravation / Q6.7 timing / Q6.5 keystone-first). PATTERN CONFIRMED: every
  defensive repair leaks new admissions because the facts are his and true. His amended 9A
  = the controlling document; their pleading mirrors its structure and marks its own loss
  point. ("the Plaintiff" artifact INTRODUCED by the amendment — different drafter/civil
  precedent in the rewrite.)
- ⭐⭐ THE 1(a) PARTICULARS REGISTER (Cory's answer to SOFC ¶11 "no particulars", 11 Aug —
  destination: Enclosure A signed statement, 1(a) section; NOT a 9A amendment; also the
  ready answer if particulars are ever formally demanded): (1) ELLEN INTEGRATION +
  ACCESS RESTRICTION — 18 Jul 2023 database-access removal email (E27, in pack) = unassessed
  unilateral directive; PROVEN on paper. (2) ON-CALL CHANGE WHILE NON-RESPONSIVE to clinical
  staff — on-call email set (Ellen after-hours / Taylor self-delegation / 17 May all-staff) +
  the "multiple emails to contact Chloe during business hours" anchor (15 May record); the
  pairing = emergency workflow bottleneck; VERIFY: date the non-responsiveness instances.
  (3) MASPER REGISTER 6 DAYS — 9 May (business-hours direction) → 15 May (2-hr pathologist
  failure + Doan call) = SIX DAYS, matching his recollection; errors built at the register
  then blamed on Switchboard ("insinuating switchboard can not do their job") — witness
  PATRISHA CO (statement on build list); dates proven via CS-1. (4) RESPIRATORY CLINIC —
  GAP: pin the dates from records before it serves; undated particular = gift to their
  objection; hold until dated. (5) ⭐ THE 2:05PM PARTICULAR (the jewel; likely = the banked
  "other staff member was doing that when it was never done" fact): no answer → he stayed
  back POST-SHIFT to make the recommendation → Chloe's response claimed "it was being done
  that morning" → the action record shows HE actioned it at 2:05PM after shift = CHECKABLE
  FALSE ASSURANCE disproven by timestamp; VERIFY: locate the email/system record + her
  actual reply words. PATTERN: all five = one mechanism (responsibility left with him, means
  withheld) — the 1(a) section will read like the rest of the file. STATEMENT BUILD LIST
  ADDS: date respiratory clinic; find 2:05pm record + Chloe's reply; date on-call
  non-response instances; Co statement.
- ⭐⭐⭐ 1(a) PARTICULARS — DOCUMENTS FOUND + PLEADING DRAFTS (11 Aug): particulars (4)+(5)
  = ONE CHAIN, in the REGULATOR'S OWN DISCLOSURE (FRMS bundle pp.40-42, "Respiratory Nurse
  Educators"): 22 Feb 2024 Clinic-contact-Details doc modified without notice to switchboard
  (root cause, identified in HIS email) → 15 May 2024 11:47am Marriott/IRS High-importance
  correction request ("no doctors... cannot reschedule") → 20 May 11:03am Marriott again
  ("WE CONTINUE TO GET CALLS" = FIVE DAYS of misdirected clinical calls) → 20 May 2:05PM
  CORY to Taylor cc Windeatt+Marriott: identifies the 22 Feb modification, "I recommend a
  modification and review of the document" → 20 May 4:30PM TAYLOR: "this task was being
  actioned. I had discussed with Richard this morning... I believe you were aware of that...
  for my approval" — the verbatim "being done that morning" response; HER "you were aware"
  contradicted by HIS same-chain "switchboard staff may not be aware". BONUSES: (a) Taylor
  SELF-FORWARDED the chain 1 Jul 2025 during witness prep (their side collected it as
  significant); (b) the ORIGINAL 9C ¶20 engaged this exchange ("not required or given
  authority to do any updating work"; denied he said he was EXHAUSTED) and that engagement
  was DELETED from the amended 9C — met the chain once and retreated. OTHER PARTICULARS:
  (1) Ellen access removal 18 Jul 2023 = E27 in pack (image page — verify exact wording by
  render); (2) on-call set: PP24 list dated 13-26 May 2024 (attachment title); verify
  self-delegation email date; non-response anchor = his 15 May "multiple emails to contact
  Chloe during business hours"; (3) MASPER 9→15 May via CS-1, Co witness. PLEADING-GRADE
  DRAFTS (i)-(v) delivered in chat — dates/documents/quotes only; absence framed as "no
  record... has been disclosed". VERIFY BEFORE SIGNING: shift end 20 May 2024 (roster) for
  the post-shift line; E27 wording; E36 date; ⭐ pack 02 "Fw Respiratory Nurse Educators.msg"
  for HIS post-4:30pm reply — the original 9C's denial that he "advised Ms Taylor that he
  was exhausted" implies a WRITTEN exhausted line exists in that chain = dated symptom
  report ~4 weeks pre-onset (statement + clinical value).
- ✅ FINAL PACK v2 DELIVERED (REPORT_B_DOCTOR_PACK_FINAL_SEND2.pdf, 159pp, 22.3MiB):
  RESPIRATORY CHAIN ADDED per Cory — FRMS disclosure pp.40-42 extracted, bannered
  ("Respondent's disclosure · p.n of 3"), placed in section H beside MASPER (E11 already in
  pack), wired into Q6.9 ("Respiratory Nurse Educators chain · 15-20 May 2024"). Inherited
  junk annotations from the source disclosure pages stripped (29 broken refs removed).
  FINAL QA: 211 links 0 dead · 125 bookmarks · renders verified (2:05pm email + 4:30pm
  reply legible under banner). Build script updated in repo
  (drafts/build_reportb_pack_LOI_aligned.py — regenerates this exact pack). The clinical
  logic of the add: the chain gives Q6.9's mechanism opinion a documented governance-failure
  instance (misdirected clinical calls, 5 days, his corrective work, the response) from the
  Respondent's own disclosure — steering-free, discovery-safe.
- ✅ STRESSOR 1(a) PARTICULARS BUNDLE BUILT + DELIVERED (STRESSOR_1A_PARTICULARS_BUNDLE_
  11AUG.pdf, 30pp/6 tabs/5.5MB; script drafts/build_1a_particulars_bundle.py): cover+index →
  TAB 1 (i) database access 18 Jul 2023 → TAB 2 (ii) on-call set May 2024 → TAB 3 (iii)
  MASPER CS-1 9-15 May → TAB 4 (iv)+(v) directory modification + the 20 May exchange (resp
  chain, junk annots stripped) → TAB 5 (vi) latency (Apr chain + 1 May block) → TAB 6 (vii)
  hours sequence. Each divider = the particular "as it would be given" (pleading-grade,
  quotes+dates only). Metadata scrubbed. ⭐ DISCLOSURE DECISION (Cory: "both have ongoing
  obligations of disclosure i will give her them"): principle AGREED — continuing duty of
  disclosure is real and runs both ways; MECHANISM refined: the DUTY covers the DOCUMENTS,
  not the arrangement — satisfy it by UPDATING THE LIST OF DOCUMENTS (LIST_OF_DOCUMENTS_
  WC2024227.pdf already built, service pending per plan) with the 1(a) items in his control
  (Ellen 18 Jul 2023; on-call set; hours pages; phone photos/rosters not already listed) and
  producing on request. Tabs 3-4 content is HER OWN disclosure (already has it). Serving the
  tabbed bundle itself is optional — it reveals the particulars architecture early; the
  standing sequence (statement at evidence exchange; schedule on demand) already delivers
  it at the right time. STRATEGIC UPSIDE of prompt list-update: model-litigant posture,
  costs protection, and makes ¶11 untenable before ever answered. Bundle audiences: HIS
  statement-support + counsel brief; serve-safe if he chooses to give it — nothing in it
  is characterisation, every explainer is dates/documents/quotes.
- ✅ 1(a) BUNDLE v2 — STRATEGIC HEADERS (delivered): every tab header now leads with
  verbatim quotes/dated facts, zero authored adjectives: T1 "Hello & Update" · access
  removed; T2 on-call self-delegated · hours never stated; T3 MASPER · six days of errors
  while contact attempts went unanswered; T4 "we can not help patients" · five days of
  misdirected clinical calls · the 2:05pm recommendation and the 4:30pm reply; T5 "more
  than two weeks without response"; T6 office hours asked in writing · retract sent to him
  only. Index mirrors. Principle: headers carry each tab's verdict in THEIR words — the
  flip-through reader (Matheson/tribunal/counsel) gets the case from the dividers alone.
  Serve-safe maintained (quotes are of documents; every clause is a date or a record).
  PLUS: settlement pricing updated in chat (~86-88% compensated strong-report; timing
  earlier — their hearing branch degraded); Taylor reliability ledger banked in chat form:
  FIVE-FOR-FIVE documented check-failures (20 May reply; COVID declines basis vs
  "attachments in fact present"; 21 May "still waiting" vs 3 May instruction; comm-book
  self-narration; contactability vs latency record) → unreliable where uncorroborated;
  their "reasonable in all respects" refrain has no reliable narrator; counterweights noted
  (prepared witness, sympathetic register, Reese-unaware true, discount not annihilation).
- ✅ 1(a) BUNDLE v3 (final, delivered): pronoun sweep — all he/him/his → "the appellant"
  (verified zero pronouns in authored pages); Tab 3 header now leads with the PLEADED term:
  'The pleaded "erratic physical presence" · the MASPER register · six days of errors while
  contact attempts went unanswered · 9-15 May 2024', explainer closes: "These records, with
  Tabs 2 and 6, particularise the 'erratic physical presence' pleaded at Stressor 1(a)" —
  the term is safe as a QUOTE OF THE PLEADING (the 9C itself recites it). Index updated.
  Build script current in drafts/build_1a_particulars_bundle.py.
- ⭐⭐ THE REVERSAL REGISTER (night's last entry, 11-12 Aug): every document THEY planned to
  use against him, with its context-container — the crop-vs-frame principle (his acts only
  look bad cropped; the bundle/chronology uncrop): (1) 15 May office-hours email ("sent to
  many people" ¶16(b)(iii)) → Tabs 6+3 (single-channel direction, six days silence,
  register failing) CONTAINED; (2) 20 May respiratory email (orig-9C "not required or given
  authority to do any updating work") → Tab 4 (patients, five days, his fix) — AND they
  DELETED that engagement from the amended 9C = met it in context once and retreated;
  (3) comm-book entry → his entry professional (on-call numbers), removal admitted —
  statement owns the moment; (4) "just putting his hand up" text → their own admitted 4 Apr
  2023 pay text proves texts were the department's register; (5) call-up-not-attend →
  their pleaded prodrome dates convert conduct to symptom; (6) mid-June lateness notes →
  decompensation-timed, group-wide, never processed; (7) ⚠ the ONE exception: 18 May
  "issues"/"defrauds" note — SELF-ADDRESSED private note at crisis peak, never a
  communication; standing handling (never relied on, owned if raised, dated to their own
  pleaded collapse week). FINDING: nothing in his hand survives-as-adverse in context;
  their adverse case = crops; the instruments = frames. Consistency affords context;
  cropping cannot. FILE STATUS AT CLOSE: every document framed, every attack answered,
  every room instrumented. Next page = the consulting room, morning of 12 Aug 2026.
- ✅ 1(a) BUNDLE v4 (final-final, delivered): Tab 3 upgraded — header adds "(urgent clinical
  call routing)"; explainer opens: "The MASPER register is used by switchboard to route
  urgent clinical calls to the responsible medical registrars; the criticality of the
  Switchboard function is among the admitted facts (Enclosure D to the letter of
  instruction)." Anchors chosen for provability: the urgent-routing function is proven by
  the bundle's own documented instance (pathologist/critical results/2 hours) + the
  ADMITTED criticality (Form 24, per the LOI's own Enclosure D description). ⚠ VERIFY ITEM:
  Cory's "code phones" point — if the MASPER register is formally part of the emergency/code
  phone system, that specific link goes in the STATEMENT sourced to the role description
  (Form 20 / AO3 role description in RFMI Attachment 2), not in the bundle header until
  sourced. Also banked in chat: the 4:30pm reply anatomy (reframe/diminish/control; the
  2.5-hour status-repair turnaround vs 25-day pay correction); ORDER-AS-ARGUMENT confirmed
  (Tabs 3-4-5 pre-justify the Tab 6 office-hours ask — "before weight is given to the email
  at Tab 6, read Tabs 3, 4 and 5, which precede it in time").
- ✅✅ 1(a) BUNDLE SEND-READY (v5 final, delivered): cover carries full details (Cory Lea
  Shepherd · Appellant (self-represented) · AO3 Switchboard Services, Logan Hospital ·
  0417 400 227 · coryshepherd1@hotmail.com · 11 August 2026); metadata scrubbed and set to
  his authorship only (Title/Author/Creator/Producer/Subject verified — nothing else).
  30pp · 5.5MB · qpdf-linearized. THE PROVENANCE REVERSAL banked (his ask): Tabs 3-4's
  documents came from the APPEAL OFFICER'S OWN DISCLOSURE (Jul 2025 witness-conferencing/
  FRMS bundle, "Renee Matheson" paginated; Taylor SELF-FORWARDED the respiratory chain
  1 Jul 2025 and the pay chain 10 Jul 2025 during witness prep) — collected by their side
  TO USE AGAINST HIM: the office-hours email as conduct ("sent an email to many people",
  ¶16(b)(iii)); the respiratory exchange as overreach (original 9C: "not required or given
  authority to do any updating work" — engagement DELETED in the amended 9C); the lateness
  notes as attendance conduct. Their intended weapons, re-framed by chronology, now
  headline HIS bundle — and the cover DECLARES the provenance ("several are drawn from the
  Respondent's own disclosure") as a credibility feature.
- ✅ MATHESON DISCLOSURE COVER EMAIL DRAFTED (drafts/EMAIL_MATHESON_ongoing_disclosure_1A_
  bundle.txt): flat/procedural per the standing register — NO quotes, NO dates from the
  bundle in the email body (the contrast is the effect); "for completeness of the sequence"
  = the only weighted phrase (factual); "supplements my list of documents" discharges the
  continuing duty with production made; "tab notes... convenience of reference only" fences
  the explainers against any quasi-submission quibble. TIMING = Cory's call: now (prompt
  disclosure) or REPORT WEEK (the sequenced pairing — bundle + Report B landing in the same
  fortnight as the season's double answer). Send as PDF, keep sent record per 3-Aug
  practice, expect no reply.
- ⭐⭐ SERVICE PLAN LOCKED (Cory's decision, 12 Aug): FOUR bundles built, TWO to be served in
  sequence — (1) the 1(a) PARTICULARS BUNDLE serves NOW/MORNING with the drafted cover email
  (drafts/EMAIL_MATHESON_ongoing_disclosure_1A_bundle.txt); (2) the STRESSOR 3 FATIGUE/
  ROSTERING BUNDLE serves WITH REPORT B (report week — the paired landing); (3) Stressor 1
  course (1(b)-(f), 23pp) and Stressor 2 pay (18pp) bundles HELD as statement-support /
  counsel-brief units, not served standalone (content = substantially their admissions;
  the statement carries those strands). ⛔ NAMING: the internal label "keystone" is RETIRED
  from all filenames/documents per Cory — Stressor 3 file renamed STRESSOR_3_FATIGUE_
  ROSTERING_BUNDLE_11AUG.pdf (internal titles never contained it). Principle banked: a
  served bundle answers an attack or marks a sequence moment — never merely mirrors the
  pleading. Builder: drafts/build_stressor_bundles.py. Service practice: PDF attachment,
  sent-record filed per 3-Aug practice, no reply expected. When Stressor 3 goes with the
  report, the report-week covering correspondence adds one line for it.
- ✅ STRESSOR 3 BUNDLE v2 (deduplicated + upgraded, delivered, 20pp): DEDUPE — the Apr-May
  rostering chains (E30/E31/R1MAY, 10pp) REMOVED (already served in the 1(a) bundle Tab 5;
  cover carries the cross-reference instead). ⭐⭐ TAB 2 UPGRADED from the actual Att 6 faces:
  (a) HIS 8 Apr 2024 3:56pm request (High importance, pay period 8-31 Mar 2024) enclosing
  "policies that delineate... a minimum of a TEN-HOUR break between shifts" — the ten-hour
  minimum cited in writing on 8 Apr; (b) 24 Apr 3:15pm follow-up (High importance);
  (c) ⭐⭐⭐ TAYLOR'S REPLY ADMITS THE ON-CALL/CODES ROLE IN HER OWN WORDS: "As the
  Switchboard Manager, it is part of my role to be on call after hours for urgent matters,
  which include emergencies like any general codes (Code Red, Yellow, Purple, Brown, and
  Orange), system outages or staffing issues due to illness" — Cory's code-phones point now
  SOURCED (feeds the erratic-presence particular: the duty defined by her, the channel then
  silent) + her reply acknowledges review "during your tenure as a PART-TIME employee" +
  she ATTACHED an after-hours protocol; (d) Tab 3 carries the FOUR-YEARS arithmetic on the
  17 Jun 2020 agreement (date math, unimpeachable) with the casual-classification fact
  HELD for the statement pending source. ⚠ RETRIEVAL GAPS (Cory to pull — full Att 6 /
  Saines PDF or QH Outlook, per E03's own note): (1) the WRITTEN REFUSAL email citing the
  2020 agreement (~1 May 2024); (2) HIS TRAVEL-TIME email; slots reserved in Tab 3's
  explainer ("held in the complete Att 6 records... statement annexures"). NEW CROSS/
  DISCLOSURE ITEM banked: how Taylor LOCATED the 17 Jun 2020 agreement she was not a
  manager for — cross question ("You were not the manager in June 2020?" / "How did this
  agreement come to you?") + future disclosure category (records of the identification/
  retrieval of the June 2020 agreement in connection with the March-May 2024 decisions).
  ⚠⚠ FLAG — DOCTOR'S PACK E03 (pp39-40): the fatigue-raised table carries internal working
  labels ("A Wednesday map Phase 1"; "Hotmail search... returned almost nothing"; "Pull
  those PDFs") — fails the pack's own no-notes-to-self standard; RECOMMEND rebuilding the
  doctor's pack without E03 (or with a cleaned E03) before it goes to the doctor; Q6.6's
  E03 citation would re-point to Enclosure B chronology. One-command fix available on
  Cory's word.

## 11 Aug 2026 (late evening) — the doctor set for 12 Aug: letter, question index, four bundles in doctor clothing · TWO SERVICE-COPY DEFECTS FOUND AND FIXED
- **The doctor set built** (`drafts/build_doctor_set.py`; outputs delivered): the four stressor
  bundles re-clothed for the doctor — service framing removed ("prepared in support of the
  appellant's statement of evidence" → "supporting documents, organised by the stressors pleaded
  in the Amended Form 9A (Enclosure C)"; divider lead-in "The particular, as it would be given:"
  → "What the documents record:"; SOFC pinpoints → "admitted on the Respondent's pleadings"),
  each cover carrying its question wiring (all four → Q6.5; 1(a)/1-course/S3 also Q6.6 + Q6.9;
  S2 → Q6.9). Files: STRESSOR_1A_BUNDLE_DR_12AUG (30pp) · STRESSOR_1_COURSE_BUNDLE_DR_12AUG
  (23pp) · STRESSOR_2_PAY_BUNDLE_DR_12AUG (18pp) · STRESSOR_3_FATIGUE_BUNDLE_DR_12AUG (20pp).
  Bundle count settled by the pleaded structure: exactly four — 1(a) · 1 course (1(b)–(f)) ·
  2 (pay) · 3 (fatigue/rostering).
- **LETTER_TO_DR_KRISHNAIAH_12AUG** (pdf + txt): one page — lists the four handovers, the
  independence paragraph, and the five written confirmations (QIRC-use / no medico-legal-use
  footer · complete sources list · questions answered with reasons · oral evidence + fee ·
  timeframe). Timeframe ask feeds the Petering engagement clock.
- **QUESTIONS_EVIDENCE_INDEX_DR_12AUG** (1p): Q6.1–6.11 → where the documents sit (pack
  sections, enclosure letters, bundle tabs). 6.2/6.8 marked "clinical — your own assessment".
- ⛔⛔ **DEFECT FOUND IN THE 11 AUG SERVICE BUNDLES — DO NOT SERVE THE ORIGINALS.** The lean-pack
  source pages carried old advocacy banners, visibly stacked under the retitles: Tab 6 hours
  pages (S155–158) showed "Hours double standard 1–4" bars + a "hours double-standard block"
  footer; the COVID text pages (S75–77) showed "COVID leave obstruction texts". Both were in
  STRESSOR_1A_PARTICULARS_BUNDLE_11AUG.pdf (pp27–30) and STRESSOR_1_COURSE_BUNDLE_1b-1f_11AUG.pdf
  (pp9–11). **v2 copies built and delivered** (`drafts/fix_banners.py`): white-out + neutral
  restamp ("Hours sequence n of 4 · author · date/time"; "COVID leave texts · Feb–Mar 2024") +
  full rasterization of the six pages (stale text layers purged; those pages now image-only).
  Serve the _v2 files. The FINAL_SEND2 doctor pack was checked and is CLEAN (its single sweep
  hit is the filed 9A's own heading on p28 — the known exception).
- **Second inherited defect fixed:** Tab 6's first page was labelled "Ellen all-department
  hours" but is actually the appellant's 7:09pm 15 May reply (Ellen's email is its attachment),
  and the four pages sat out of order. Both builders now run Tab 6 chronologically — 1:15pm
  request → 6:23pm retract (to the appellant only) → 7:09pm reply → 17 May all-staff hours —
  with accurate banners and a rewritten explainer. Applies to the DR bundle and the 1(a) v2
  service bundle (`drafts/build_1a_particulars_bundle.py` updated).
- QA: steering sweep zero across all eight outputs' authored pages ("reprisal" inside the ESU's
  own PID-Act letter and "campaign image" email artifact = their documents, acceptable);
  bookmarks intact; letter and index each verified one page; metadata scrubbed to Cory only.
- Open for the morning: LOI blanks ([Date]/[email]) still to complete before handover; E03
  internal-labels rebuild of the pack still offered, awaiting his word; print run —
  letter + index + the four bundle covers at minimum.
