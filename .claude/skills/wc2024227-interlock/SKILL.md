---
name: wc2024227-interlock
description: Fact-interlock protocol for Cory Shepherd's QIRC matter WC/2024/227 and the parallel Metro South employment track. Use this skill whenever the work touches this matter in any way — the appeal, the Form 9A, the Form 24 admissions, the Form 29 or rule 64G disclosure, the psychiatric or medical evidence, the RFMI, the exclusion since June 2026, the s 89 letter, the union, settlement, or any correspondence with the Regulator, Matheson, Metro South, Harrison, Hughes, Taylor, Forrest, Griffin or Ruttan. Trigger it even when the user only asks a narrow question about one document, because in this matter the answer to almost every question lives in a document other than the one being asked about. Also trigger before drafting anything for filing or service, before quoting any paragraph number, and before characterising any statement in a source document as an error.
---

# WC/2024/227 — Fact Interlock

## Why this exists

Every serious mistake made in this matter has the same cause: **reasoning from a summary,
a recollection or a single document, when the answer sat in a different document nobody
opened.**

Four real examples, all from one working session:

1. **"He was never dismissed."** Asserted confidently. He was — employment ceased 9 October
   2024 by an abandonment letter, backdated to the day after the WorkCover decision. The proof
   was in the corpus and in two filenames already listed that session. **Cost: a false claim that
   his own psychiatrist had erred.**
2. **"The onus is on the Respondent under *Prizeman*."** In the filed pleading. Wrong twice —
   the appellant bears it, and *Prizeman* is about reality versus perception. **The QIRC's own
   appeal guide says so in one line.**
3. **"Independent Review Office (IRO)."** In the filed pleading. **No such body exists.** It was
   the Regulator's own Review Unit — which is the stronger fact.
4. **The Form 24 numbering.** Response row numbers drift from Notice paragraph numbers after
   row 26. Every downstream "Admitted Fact: Para X" tag was therefore unverified, and three of
   them are wrong.

None of these were hard to catch. **They were only hard to catch without looking.**

## The protocol

Before asserting anything about this matter, work the interlock:

**1. Name the proposition.** Write down, in one sentence, the thing about to be asserted.

**2. Pull every source that touches it.** Use `references/interlock-index.md`. In this matter the
answer is usually in a document other than the obvious one — the employer's objection corroborates
his affidavit, the Regulator's pleading proves the existence of documents the employer says don't
exist, and his own emails contain the contemporaneous record.

**3. Read them from source, not from notes.** `skill/references/confirmed-record.md` is a working
record, not an authority. Every pinpoint gets checked on the page.

**4. Check the integrity rules.** See `references/source-integrity.md`. Several key documents have
no text layer or a broken one, and `pdftotext` returns confident nonsense on them.

**5. Only then reason.**

The order matters. Reasoning first and verifying second produces fluent, wrong answers — because
a plausible reconstruction feels exactly like a recollection.

## The rule about calling something an error

Before characterising any statement in any source document as wrong — a doctor's report, a
pleading, a letter, a date — **search the corpus and the filenames for the fact it asserts.**

The filename is evidence. `2025-04-08_Roberts_reinstatement_process_security_office.pdf` was sitting
in a directory listing while a confident assertion was made that no dismissal occurred.

**A source document is presumed right until the record says otherwise.** The author was usually
there and usually had the file.

## The two disciplines that survive every version of this matter

**State the chronology, never the motive.** Motive is not an element of s 32(5)(a) — *Prizeman*
makes it the reality of the employer's conduct, not the perception of it. And *Briginshaw* raises
the standard of persuasion for serious allegations, so every characterisation of a person raises
his own bar. The dated sequence produces the inference on its own, and it cannot be answered.

**Never open the s 32(5)(b) door.** Injuries connected to the worker's *expectation or perception*
of reasonable management action are not compensable. The Regulator has not pleaded it. Words like
*punishment*, *hostile*, *capricious* and *reprisal* hand it to them from his own side.

## What the case actually is

Keeping this in view prevents the recurring failure of treating thirteen grievances as thirteen
arguments:

**One mechanism — responsibility imposed, and the means to discharge it withheld — with one
admitted instance: the seven-hour break of 17–19 March 2024.**

Everything else is context threaded back to that. The Respondent admits a *"7-hour break rather
than an 8-hour break"* (SOFC ¶22(a)), so the shortfall is uncontested by anybody. It is the only
strand in fourteen months where the employer's own rule produces an answer by subtraction, and the
only one where his own conduct is not in issue at any point.

⚠ **CORRECTED 25 Sep 2026 (Cory): *Delaney* is the APPELLANT'S authority.** *Delaney v Q-COMP* [2005] QIC 11 is an
**anti-atomisation** doctrine: the composite course, not the isolated incident, is the unit of assessment. It answers the
SOFC ¶22(a) "not intentional or repeated" clamp. Review Decision 69983 **misapplied** it, using it to *dilute* (averaging the
unreasonable break against unrelated factors, the precondition never tested) instead of to *aggregate*. See
`wc2024227/analysis/2026-09-16_DELANEY_MISAPPLIED_in_RD69983.md`. **Run both:** *Delaney* against atomisation, *Mahaffey*
against flattening. The composite relied on is the standing fatigue and recovery **state**, not a global weighing of every
grievance.

## Before anything is filed or served

- Every case read to its ratio. No citation from memory, and none from a summary.
- Every "Admitted Fact" tag re-checked against the **rendered** Response and the row map.
- Every limb that fails on a rule's own words deleted, not softened.
- Every adverb of assertion struck.
- The admission moved into the sentence, not left in a parenthesis — parentheses are skipped
  when a document is read aloud, and this one was.


## ⭐⭐ Search the whole matter before you answer — do not guess which file to open

There are **411 files and ~6,330 PDF pages**. No session can hold them. But the failure has never
been that a document was unreadable — **it has been not knowing which document to open.**

`wc2024227/index/FULLTEXT.txt` holds every extractable page, each preceded by a marker line:

```
>>> documents/WC.2024.227_Regulator_SOFC_13.05.2026.pdf :: page 3
```

So one search reaches the entire matter and hands back the file and page:

```bash
grep -n -i "fatigue leave" wc2024227/index/FULLTEXT.txt
```

**Then open that document properly.** The index tells you where to look; it is not a substitute for
reading the source, and nothing is quoted into a filing from the index.

⚠ **Rebuild it whenever documents are added**, or it silently goes stale and produces exactly the
false confidence it exists to prevent:

```bash
cd wc2024227 && python3 ../.claude/skills/wc2024227-interlock/scripts/build_index.py
```

### ⛔⛔ 31 documents have NO usable text layer — grep cannot see them
`index/MANIFEST.tsv` marks them `NO_TEXT_LAYER` or `THIN`. **They return nothing to every search,
which is why things in this repo have repeatedly been called "missing" while sitting on disk.**
The ones that matter most:

| Document | Why it matters |
|---|---|
| `related-matters/TD2024-110_Form12_Application_for_reinstatement_stamped_25.10.2024.pdf` | ⭐⭐⭐ The reinstatement application. Called "the most important missing document" — **it was never missing** |
| `medical/Employee_Capability_Checklist_CShepherd_03-07-2026.pdf` | ⭐⭐ **The ECC.** The whole exclusion turns on it and it has only ever been quoted second-hand |
| `filings/2026-04-22_Form29_Notice_NonParty_Disclosure_sealed.pdf` | The sealed Notice |
| `evidence/Chloe_Work_text_messages_incl_2023-04-04_roster_board.pdf` | Taylor texts + a 2023 roster board |
| `medical/2025-07-22_OurMedicalAshmore_GP_records_via_Saines.PDF` | Exhibit A5 |
| `disclosure-2026-06_MSH_production/*` | What MSH actually **produced** — as opposed to what it refused |
| `documents/orders/*` (all four) | Every directions order |
| `documents/filings/2026-02-2*` | The recalled February 2026 Form 4 and affidavits |

**Render them: `pdftoppm -r 150 -png <file> <outstem>` and read the pages.**
⭐ **If a search returns nothing on a proposition you expect to exist, check the manifest before
concluding the document is absent.** Silence in this repo usually means no text layer, not no document.
