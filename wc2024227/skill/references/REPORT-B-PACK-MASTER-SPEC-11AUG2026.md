# REPORT B DOCTOR'S PACK — MASTER BUILD SPECIFICATION
> 11 Aug 2026. The complete, consolidated instruction: design doctrine → content manifest →
> navigation architecture → build pipeline → QA checklist → delivery. Supersedes the scattered
> audit notes; those remain the change-log. ⛔ This pack is Q6.4-DISCOVERABLE: every word in it
> must survive being read by the Regulator. Audience: the doctor (and later, on request, the
> Regulator). It NEVER goes to MSH, never to Matheson voluntarily.

## 0. DESIGN DOCTRINE (the why)
1. **Design for discovery, not instruction.** A steered report is a dead report. Every target
   conclusion must be reachable as the doctor's OWN inference from dated, mostly their-authored
   documents. No conclusion words in our hand anywhere (prodrome, job strain, insidious,
   hostile, reprisal, double standard). Adjacency is the only permitted argument.
2. **Target conclusions → evidence design:**
   - CLEAN BASELINE: CS-3 application → FT approval + his 28 Sep 2023 gratitude reply →
     16 Nov 2023 GP entry. 2022 ADHD/anxiety pages IN and visible (disclosure = credibility).
   - LOW CONTROL/AGENCY: a section whose every document is a decision-about-him-without-him
     (roster imposed, 1 May proposal refused, retraction directive, database access removal,
     leave "processed on your behalf", insurer-first position). No label; the pile speaks.
   - MECHANISM + DOSE: March roster (7-hr pairing) FACING the 10 May 2024 rating-of-11; the
     compression window (Mar→Jun 2024) strictly chronological; Q6.9 asks only the textbook
     question.
   - NO RIVAL CAUSE: competitors dated PROMINENTLY (job loss Oct 2024 reversed; personal
     ~Dec 2024) — timestamped, not hidden; Q6.7 acquits by dates.
   - CONDITIONAL PROGNOSIS: the 2025–26 arc (Feb 2025 return → graduated fortnights → worked
     until 26 Jun 2026 → fit-with-restrictions met with exclusion). Q6.10/6.11 + documents.
3. **The chronology is the master instrument** — the one page every expert internalises.
   Disproportionate craft there; everything else exists to verify it.
4. **Three readers served simultaneously**: panel navigator (bookmarks), linear/print reader
   (physical order + printed pins), hunter (text search — hence OCR).

## 1. CONTENT MANIFEST (sections; E-codes permanent and gap-free — NEVER renumber)
- Cover (hub; live links; see §2.1)
- A. Questions Q6.1–Q6.11 ONLY (⛔ no QL pages — those live in Cory's own question map, oral)
- B. Form 24: key-admissions schedule → original notice → Respondent response
- C. Amended 9A: stressor map → full text (bookmarks "as pleaded", no advocacy labels)
- D. Spine: LOI (final verified version) · chronology (carries 13–15 May attendance-difficulty
  entry sourced to Respondent's pleading) · Form 20 spine
- E. Fatigue: matrix · March 2024 roster ·  E35 FRMS rating-of-11 + rostering-errors +
  unanswered chase (ADJACENT to the roster) · Att 6 · CE letter FRMS gap · FRMS guideline ·
  rostering chains · 1 May block
- F. Baseline/medical: CS-3 (E19) · E36 FT approval 27 Sep 2023 (incl. his 28 Sep reply) ·
  Ashmore (incl. 2022 pages) · Hawes 1 Jul 2024 · E37 Hawes to 8 Sep 2024 · E23 prior report
  13 Feb 2025 (Krishnaiah author; Ings recipient) · ECC 3 Jul 2026 · 2 Jul 2026 email · clinic
  correspondence
- G. Governance/May/hours: MASPER CS-1 · comm book ×2 · PID outcome · ESU face · CS-4 ·
  retract strand · hours sequence (neutral name: "Hours requests and responses — sequence")
- H. Pay/leave: AVAC chain · 21 May · NNPD · E38 Item 15 leave takings 19 Mar · E39 Item 11
  myHR + pandemic forms · 4 Apr 2023 pay text (if not inside phone photos)
- I. E40 Review Decision 69983 — LAST, for sources completeness (de novo noted)
- J. Jump list (alphabetical by plain name, all lines live links)
- ⛔ EXCLUDED BY DECISION (do not revisit at midnight): 18 May "issues" email (defrauds);
  Reese/Taylor witness-conferencing accounts; 8 Sep 2025 Hughes letter (oral-ready only);
  SOFC as a document (dates mined into chronology); deed/WP/DFV/rule-10; Forrest 8-hr
  admission letters (Pack 2 weapon — ¶22(e) arrives at hearing unrepaired).

## 2. NAVIGATION ARCHITECTURE (six layers)
2.1 **Cover = hub**: title · "Navigate by bookmarks" line · reading order 1–9 with every line
    a LIVE internal link · "DATES AS THE DOCUMENTS SHOW THEM" paragraph (facts+sources only;
    no "prodrome", no "= engagement") · full independence statement ("Your opinion is yours
    alone… legal questions are not asked of you"). No notes-to-self ("minimize dump" etc.).
2.2 **Bookmark tree**: ≤3 levels; level-2 grammar = "date · author · what it is" (the closed
    tree reads as a chronology); NO "Reason:" child bookmarks (analysis = fingerprints);
    bookmark order = physical page order EXACTLY (reorder pages; no divergence disclaimer).
2.3 **Banner strip every page**: E-code · date · author · document · "p.n of m" + a "◂
    Questions" return link. Two-way navigation always.
2.4 **Question pages = switchboards**: each evidence line = live link AND printed true pin;
    lists ordered by probative weight (first item = open-this-one); ≤6 items/question.
    Wiring: E36→Q6.1+Q6.3 · E35→Q6.6+Q6.9 (FIRST line of Q6.9) · E37→Q6.11 · E38/E39→Q6.6 ·
    E40→Q6.4 note only.
2.5 **Chronology = linked spine**: every line's date links to its proving document [E-code];
    banner returns. One page from which all pages are one click away. Blocks visible in white
    space: ascending 2023 · compression 2024 · post-onset competitors · recovery 2025–26.
2.6 **Jump list = alphabet**: lookup table, alphabetical, all live.

## 3. CONVENTIONS
- One date format everywhere: "17 Mar 2024".
- E-codes frozen once assigned; new docs take new numbers at the end.
- No highlighting/annotation ON documents — originals stay virgin; question wording points.
- No colour-coding. No exhibit labels asked of the doctor.

## 4. BUILD PIPELINE (execution order matters)
1. Assemble content in FINAL physical order (sections contiguous; E docs inside E).
2. OCR image pages (`ocrmypdf --skip-text`) — approval, phone photos, scans must be searchable.
3. Stamp banners with E-codes and p.n-of-m.
4. Create NAMED DESTINATIONS per document (e.g. `E07_roster`) — all links target names, not
   page refs, so future edits never break links (the stale-pin bug class, killed permanently).
5. Generate question pages + chronology + cover + jump list FROM the destination map
   (programmatic pins — never hand-typed).
6. Generate bookmark tree from the same manifest.
7. Optimize (`qpdf --optimize-images` / gs 150dpi; target <20MB) + linearize.
8. Metadata: title/author only; scrub the rest (standard python zip/pikepdf scrub).
9. RUN QA (§5). 10. FREEZE (rename `_FINAL_<date>`; E-codes and pins locked).

## 5. QA CHECKLIST (run on every rebuild; nothing ships unchecked)
☐ Every printed pin == actual page (script: extract pins, compare to destination map).
☐ Every internal link resolves (walk all annotations; zero dead links).
☐ Search test: "16 October" hits approval; "rating of 11" hits E35; "seven-hour"/"7-hour"
  hits roster/matrix (proves OCR).
☐ Steering sweep — grep the full text layer for: prodrome · hostile · double standard ·
  reprisal · campaign · insidious · job strain · dump · weaponis · suppress. ZERO hits in
  OUR pages (pleadings quoting their own filed words are the only exception).
☐ Question wiring: E35–E40 cited where specced; no question >6 items; first item = strongest.
☐ Bookmark grammar (date·author·item), ≤3 levels, no "Reason:" children, order == physical.
☐ Boundary sweep: no Report A material, no deed, no WP, no rule-10, no Forrest 8-hr letters.
☐ Cover: links live; no notes-to-self; independence paragraph present.
☐ Chronology: every line sourced; 13–15 May entry present; bereavement date entered (or
  logged as oral-supply item).
☐ Metadata clean; size <20MB; opens to cover; linearized.
☐ The two-click rule: any document reachable in ≤2 clicks from cover, chronology, or its
  question; return path ≤1 click.

## 6. DELIVERY
- Confirm channel with clinic BEFORE the appointment (email size / USB / link).
- Print the 30-page CORE separately: questions · chronology · admissions schedule · March
  roster · rating-of-11 · CE extract · approval · both certificates. Hand the core to the
  doctor; the PDF is the same structure expanded; oral triage line: "if time is short, the
  core is pp. …".
- The oral layer (Cory's half): the question map (incl. QL items), five confirmations in
  writing, dates-not-adjectives voice matching the file.

## 7. FREEZE & CHANGE CONTROL
- After the report cites E-codes, the pack is IMMUTABLE — corrections ship as a dated
  supplement with new E-codes, never as a rebuilt pack.
- Every rebuild before freeze gets a version suffix and a QA run; the working-notes entry is
  the change-log.
