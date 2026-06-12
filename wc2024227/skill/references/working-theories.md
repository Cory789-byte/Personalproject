# Working Theories — WC/2024/227

**Everything here is hypothesis, not confirmed fact.** Each carries a confidence level. These frames are analytically useful and shape strategy, but NONE may enter a filing as an asserted fact. When a theory is confirmed against a source, move it to `confirmed-record.md` and note it there. Keep this separation absolute — it is the point of the skill.

---

## 1. Two-stream disclosure model (confidence: moderate–high, but UNSETTLED by the Form 29 finding)

**Theory:** MSH produced in two streams. Stream 1 (to the Regulator): full, informal collection in Cory's Form 29 compliance window (22 Apr–6 May), flowing to WCRS, supplemented by conferencing — complete, uncurated. Stream 2 (to Cory): triggered not by the Form 29 but by the Commission's 22 May direction — partial, lawyer-assembled, curated, late. Collected early, packaged late, completeness to the Respondent, selectivity to the Appellant.

**Support:** metadata (see below) — WCRS bundle container 6 May 1:31 PM (= day 14 from Form 29 service); payroll report run 8 May 9:53 AM by operator 105777; then NO Cory-facing artifact until after 22 May (prints by "Renee Dawson" 25 May, Ruttan 29 May & 2 June, letter 5 June).

**CAUTION — the Form 24 ¶23 finding complicates this.** There demonstrably IS a Form 29 mechanism in this matter (the medical-records Form 29, Registry-signed 4 July 2025). So Matheson's "Notice of Non-Party Disclosure request" in her 11 June email is NOT as certainly a reference to Cory's own Form 29 as earlier sessions concluded. It could be: (a) Cory's Form 29; (b) a separate Regulator-issued Form 29 to QH; (c) loose drafting. **Resolve via the index email — do not treat as settled.**

## 2. Metadata findings (confidence: high — extracted from the actual PDF; but inferences about MOTIVE are lower)

> **UPDATE 11 June 2026 — extraction re-run in-repo and CONFIRMED; migrated to
> `confirmed-record.md` + `documents/METADATA_REGISTER.md`.** New extracted
> facts beyond the original session: the bundle is **10 pages** (not 23);
> revision-1 page-tree `/Count` = **4** (the 6 May container), expanded to 10
> in the 11 June 10:56 re-save — i.e. the Outlook prints + ESU form pages
> were APPENDED on 11 June (CONFIRMED 12 June by splitting the file at its
> revision boundary: revision 1, as it stood on 6 May, holds ONLY the 4
> leave-form screenshot pages; pages 5–10 = the May-2024 emails + ESU form
> were added in the 11 June 10:56 re-save — see
> `documents/disclosure-2026-06_MSH_production/CROSS_SOURCE_TIMELINE.md`). The Item 11 AVAC
> history print shows myHR session user **"Estelle Bain"** — a new unknown
> name for the access-log request, alongside operator 105777 and "Renee
> Dawson".

**Extracted facts (these are real, from file properties):**
- Regulator's 11 June bundle: container created 6 May 2026 1:31 PM (Word, "WCRS FactSheet PortraitWide" template); ModDate 11 June 10:56 AM (7 min before Matheson's 11:03 email). Three font families = three sources: screenshot pages in current M365 (Aptos); email prints as a single Outlook batch from Matheson's mailbox; ESU form pages.
- The screenshot pages show a LIVE administrative session with EDIT rights (Upload link, Document Type dropdown, delete × on Cory's own attachment) — i.e. someone with admin access recently walked all five tabs of Cory's leave record (Request, Attachments, Comments, Process Flow, History).
- The **McGinley email (16 May 2024) was never addressed to Cory** (To: Reese, Tracey Smith; Cc: Punch, Pritchard, McNamee) — so it cannot have come from Cory; an MSH-side custodian supplied it. **Provenance kill-shot for the conferencing channel.**
- MSH enclosures: Leave Takings Report generated 8 May 9:53 AM by operator 105777; leave form printed by "Renee Dawson" 25 May 1:06 PM (edited ~2 hrs later); myHR report printed by Ruttan 29 May FROM AN .xlsx (native exists); Role/AVAC prints 2 June; MSH letter created 5 June 2:57 PM, internal title "Attachment 4… Letter to Court response to Non production order Shepherd FINAL" (attachments 1–3 exist somewhere); Cridland signature 2:54, served 3:02.

**RESOLVED 12 June 2026 — MSH "For disclosure" folder metadata (Shepherd_1.zip); full forensic timeline in `documents/disclosure-2026-06_MSH_production/METADATA_FORENSIC_TIMELINE.md`:**
- **"Renee Dawson" is MSH-side** — dc:creator of Cory's leave-form PDF (Item 11), created 25 May 13:06, modified 25 May 15:09. The unknown name is resolved: an MSH custodian who handled the leave record after the 22 May direction. (NO assumed link to Renee Matheson — different surname, MSH vs Regulator.)
- **operator 105777 is a myHR/SAP operator ID**, not a person — sole artifact is the 8 May Leave Takings Report export (PDF Engine winx64h). The early artifact, in the Form 29 window.
- **Myla Ruttan** assembled the package by Print-To-PDF, 29 May–2 June.
- **TRIM/Content Manager marker (3 June) confirms records-system provenance** — the production was exported from a managed records system, which strengthens the "production is frictionless" limb (asymmetry reply, reserve).
- **Assembly window 25 May–4 June** (after the direction), except the 8 May export — corroborates and sharpens the two-stream model. Redacted Items 12/16 added last (2–4 June) with all metadata flattened.

**Inferences (LOWER confidence — do not assert):**
- That the searches were complete by early May and the file then "slept" until the direction. (Plausible; print dates prove package-assembly timing, not search timing — but the early artifacts carry the search-date burden.)
- "Renee Dawson" — RESOLVED as MSH-side custodian (see 12 June update above); still a target of the IP/access-log request for the 25 May edit session, but no longer an unknown.

## 3. Motive of Renee Matheson's 11 June disclosure (confidence: individual self-protection ~dominant)

> **UPDATE 11 June 2026 — timing refinement (theory, but anchored to extracted
> facts):** "never identified" stopped being a safe assumption the moment MSH
> objected (5 June) asserting Item 20 documents "do not exist" while the
> Regulator held responsive internal MSH correspondence (container 6 May).
> Once the 64G compelled production, anything MSH produced became comparable
> against the Regulator's file — a dated, provable hold. The 5–12 June window
> was the last moment disclosure could read as voluntary discharge rather than
> compelled surrender; the 11 June 10:56 re-save (appending the email prints,
> 7 minutes before sending) is consistent with a same-morning decision about
> exactly what to put on the record before the application landed. Disclosure
> also moved the Regulator to the right side of the foreseeable verification-
> affidavit contradiction before MSH swore anything.

**Theory:** Matheson disclosed primarily to clear her OWN professional position before Cory's 64G could implicate her — the continuing disclosure duty and model-litigant obligation are personally hers, and she has direct experience (the Feb application) that Cory attacks disclosure conduct. Not goodwill toward Cory (price none); not coordination with MSH against him (the no-CC to MSH and the metadata cut against it). The careful provenance clause is an experienced officer being accurate-but-careful.

**Wording analysis (12 Jun) — the cover sentence as a chosen instrument.** She had MSH's objection (incl. the Item 20 "does not exist") in hand from 5 June 3:02 PM and watched it for six days before disclosing. The sentence she then wrote — "As part of the Regulator's ongoing disclosure obligation in this matter, please see attached documentation received through Notice of Non-Party Disclosure request and conferencing" — does four things at once: (1) "ongoing disclosure obligation" frames the act as continuing-duty discharge, conceding no lateness; (2) "received through… and conferencing" attributes provenance to MSH's own channels — "MSH gave us this" — and volunteers the existence of the conferencing channel, which she did not have to name; (3) it makes NO reference to MSH's objection or Item 20 — the contradiction is placed on the record by juxtaposition, never stated (the same discovered-not-stated technique the 64G uses); (4) "Notice of Non-Party Disclosure request" is left deliberately unspecified as to whose — the precise ambiguity the index email asks about. Functional effect, whatever the motive: she moved the contradiction from inside her file (her problem) onto the record (MSH's problem) without taking a side. Counter-reading (keep live): the sentence could be template compliance wording; but day-6 timing + the same-morning append + six days of watching MSH's answer favours considered choice.

**Operational consequence:** she will answer a *written* request because not answering recreates the exposure she just moved to avoid. The index email works on her specifically.

## 3A. Regulator posture on the 64G — counsel stood down (confidence: moderate)

**Observed pattern (Appellant recollection + documented spine):** Willson (WHS-specialist panel counsel) appeared at every contested-phase listing — 27 Feb mention, 13 Mar conference, 7 Apr mention — through the pleading fight, sought 5 weeks to answer the Neville pleading, and then did not appear at the 22 May mention, the first listing after the Regulator's amended SOFC was filed (13 May).

**Theory:** counsel was briefed for the pleading contest and stood down once the responsive pleading was in — i.e. the Regulator does not intend to fight the disclosure phase. Consistent with: the 22 May mention being MSH's timetable issue (MSH absent too); the reception model (Regulator abide ~62% on the 64G); and the 11 June disclosure (a party planning to oppose does not volunteer the McGinley page). **Predictive use:** expect the Regulator to abide or consent on the 64G; expect Willson to reappear only if the matter moves toward hearing or settlement-conference territory — her reappearance is itself a signal worth logging. Do not rely on absence as fact at hearing; it is posture-reading only.

## 4. Coordination + the seam (confidence: high on coordination, high on the seam)

**Confirmed-ish:** MSH and the Regulator run a coordinated defence (conferencing channel, witness supply, the 52MB witness file, the Willson meeting). This is lawful and ordinary, not sinister.

**The seam (the useful part):** coordination holds until it threatens the Regulator's OWN standing with the Commission. Holding responsive documents past that line becomes the Regulator's individual disclosure breach — so the Regulator will not burn its standing with the court to protect MSH. The 11 June disclosure is where the seam opened. **Exploit via process (the served application forces responses coordination can't absorb privately), never via accusation.**

## 5. Liability layers / distancing model (confidence: structural, persuasive)

**Theory:** institutions are shielding the institution from the point its records convert Cory's allegations into its obligations — not shielding the manager.
- Layer 1 (certain): WC + s 40–42 PID reprisal tort (MSH vicariously liable; facts largely admitted).
- Layer 2 (real, contingent): individual criminal — s 41 reprisal is Reese's personal exposure (welded to MSH's vicarious liability, hence shielded); Chloe's fraud-allegation exposure is individual misconduct the institution can disown (hence Chloe-adverse material surrendered). Possible s 38 CC Act referral duty on Cridland if the logs confirm.
- Layer 3 (created by the 64G): false-verification exposure on the affidavit deponent.

**Distancing tells (watch, each a free model update):** who swears the verification affidavit (corporate officer = distancing confirmed; Chloe/Reese = institution backing them); whether MSH's response defends the *merits* of Chloe's conduct anywhere (predict: never — confirmation by silence); how hard Item 9 is fought (ferocity = the unproven fact still feared; soft fold = distancing complete).

**Endgame read:** settlement IS the shield — a heard appeal produces portable findings; a settled appeal produces payment and no findings. Hence the release-scope discipline rule.

## 6. Severity / injury theory (confidence: high as a frame; it is Cory's case)

The injury is the cumulative institutional response to raising concerns: union delegate (offered, blocked), rostering (6 differential cyclic patterns authored, declined), manager grievances (dismissed, treated badly), director escalation (declined), PID (routed back to subjects, retraction in 48 hrs), pay withheld — every channel closed, and using them made Cory "the problem." Degree/duration/density. Belongs to evidence-in-chief, the medical case (Hawes mechanism), and closing — NOT the 64G.

**Roster-seam discovery:** the 7-hour break sits in the SEAM between two fortnightly rosters (variance forms run 5–18 Feb, 19 Feb–3 Mar; 17 March = last day of the 4–17 March period, 18 March = day one of the next). The breach lived where two rosters met and no system existed to look there. Manager works Mon–Fri, so the weekend keystone shows STRUCTURAL supervision vacuum by design; the Monday (18 March) is the probative weekday inside the floor.

## 7. Reserve weapon — the asymmetry reply (DRAWER, not in the application)

Deploy ONLY if MSH maintains the expense ground (r 64E(4)(a)) in its responsive submissions. Trigger probability ~12.5% (Section G is the expense rebuttal pre-deployed). Full drafted text:

> "The expense grounds are maintained in the terms of the response of 5 June 2026: Chief Executive approval, engagement of eHealth Queensland, diversion from the delivery of health care. The Respondent's disclosure of 11 June 2026 records what production from these custodians involves in practice: correspondence from the Director's own mailbox, and the complete tabs of a form produced to the Appellant only in part, were provided to the Respondent through its conferencing of MSH officers — without, so far as appears, any of the apparatus the objection describes. The documents are the same; the custodians are the same; only the requester differs. A burden that varies with the identity of the party asking is not a burden within rule 64E(4)(a); and to the extent any real expense attends production under the Notice, rule 64I meets it."

Also available: the **differential-answer inference** — MSH answered "not retained" freely for seven items (incl. SPOK) and gave no such answer for Items 8–9; you don't object on privacy to records you haven't confirmed exist. Same trigger.

## 8. Post-filing target list (sequenced behind settlement)

- Index email to Matheson (post-service): Form 29 question (is it Cory's? date/source received? more coming? Form 29 for records about Cory?).
- IP access-log request: myHR/AVAC audit log Feb–Jun 2026 (names operator 105777, "Renee Dawson," the walkthrough session operator/date).
- Contradiction matrix from the 52MB July 2025 witness bundle — extract every attendance/supervision/presence assertion BEFORE Items 8–9 land (statements locked blind in 2025).
- July 2025 diff: was the McGinley chain / full tabs in the 2025 bundles? (If yes, Regulator held them 11 months; if no, 2026 conferencing.)
- Load-profile witness statement (Cory's evidence): ~400 calls/shift, ~20 emergency codes, pathology/Dr-to-Dr/hospital-to-hospital — anchored to the produced MET spreadsheet, NOT sent to the Regulator early.
- Psychiatrist report: commission AFTER production; structured as instructed-assumptions on Cory's statement; treating notes meanwhile to capture work context.
- Six cyclic rostering proposals + decline responses → matrix anchor rows.
- February residue supplement (post-production): COVID decline dates 20–29 Feb + the 4–17 March roster authoring fortnight — one targeted notice, justified by two pleaded events.
