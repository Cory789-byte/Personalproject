---
name: form24-verifier
description: >
  Verify the WC/2024/227 Form 24 notice to admit (Part A), the Part B summary and
  Annexure A against the record before any rebuild is committed or served. Use
  whenever a fact is added, edited or deleted in build_form24_second.py, whenever
  the annexure ITEMS change, whenever Part B rows change, and always before
  service. Also use when asked to "verify the form 24", "run the checks", "test
  the admit deny against the record", or assess whether a proposed fact is safe.
---

# Form 24 verification — the five-layer architecture

## Why this exists

Every defect found in this notice was found the same way: **by checking the
document against the record instead of against memory.** The specific failures
this system exists to prevent, each of which actually happened:

1. **Quotes not in the cited annexure tab** — Tab 2 stopped at Reese p19 while
   clause 11.7 sat at p21; Tab 26 held the Response while six facts quoted the
   Notice. A fact whose quote is not behind its tab invites a denial.
2. **Arithmetic that a pedant can deny** — "five days" for an interval of
   4 days 23 hours 16 minutes.
3. **Facts sourced to documents the Respondent never held**, or to an unfiled
   draft ("employed since 2019").
4. **Editorial additions inside quotes** ("without any prior consultation"),
   assumed honorifics (Dr Kwok), smoothed ellipses, wrong subject lines.
5. **Two numbering schemes both called Annexure A**; duplicated facts; the
   renumbering pass running after the render so zeros reached the PDF.
6. **Deniable propositions** — universal negatives ("has not disclosed any
   document") instead of negatives tied to a defined universe ("as presently
   constituted, does not allege").
7. **The summary drifting from the facts** — Part B rows paraphrasing away
   admissions, misattributing approvals, inventing dates the admission does
   not carry.

## The layers

**L0 — extraction.** The single source of truth is `wc2024227/drafts/
build_form24_second.py`. Facts are extracted by exec of the FACTS block plus
the renumber/relabel pass (marker: `import re as _re` … `_L, _relab`). Never
hand-count fact numbers; they are assigned at build time.

**L1 — deterministic battery.** Run `scripts/verify_form24.py` from
`wc2024227/drafts/`. Exit 0 = green. It checks: sequential numbering with no
zeros; exact-duplicate facts; repeated quotes (against the allowlist in
`repeat_allowlist.json` — subject lines, audit-trail entries and document
titles legitimately recur; anything else is a defect); every cited tab exists
in the annexure; every quoted string in a tab-cited fact is present in the
built bundle text (normalised for curly quotes, line wraps and whitespace),
except tabs in `image_tabs.json`, which have no usable text layer and are
verified by render — re-verify by render if the source file hash changes;
interval-arithmetic regressions (every dated interval claimed in a fact is
recomputed); Part B coverage (every Part A section appears in some row; every
long quote in a Part B body exists in Part A); metadata stripped on all four
outputs; and the mock returns **zero denials** — a single DENY is a build
failure, because the notice's design invariant is that every fact is
undeniable on the Respondent's own documents.

**L2 — source-anchored verification (model).** When facts are ADDED or their
quotes changed, verify each against its actual source page, not the bundle:
open the source PDF at the mapped pages, confirm wording verbatim, headers
(From/Sent/To/Subject) against the header block, dates against the page.
Batch by source document (the 15-group workflow pattern). Pages with no text
layer are rendered with `pdftoppm -r 150 -png` and read — never quoted from
the index, whose OCR carries errors ("sub-delegatethe", "Section 46%").
Record verdicts; a fact verified once needs re-verification only if its text
or its source file changes.

**L3 — adversarial mock (model).** `build_form24_mock_response.py` answers
every fact as the Senior Appeals Officer would, calibrated on her actual
18 February 2026 behaviour: she admits atomic facts anchored to documents her
side holds; she refuses on provenance; she denies characterisation, compound
propositions and inference. Classification rules live in the script. Any fact
classed DENY must be narrowed until the only truthful answer is admission, or
deleted. NOT-ADMIT on provenance is acceptable only when an admitted backstop
exists (record which fact backstops it).

**L4 — negative-universe audit.** Every "does not allege" fact: grep the SOFC
text for the negated proposition — if any paragraph arguably alleges it, the
fact is deniable and must be narrowed. Every "not identified or disclosed"
fact: search `index/FULLTEXT.txt` AND check `index/MANIFEST.tsv` for
NO_TEXT_LAYER files that grep cannot see, then render-check those. An absence
asserted over a corpus you have not actually searched is a false fact waiting
to be served.

## Drafting invariants (what the checks enforce)

- One fact, one source, one date. No "and" bundling two propositions.
- Quote verbatim or as an honest fragment; never insert a full stop that is
  not in the source; interior double quotes may become single quotes.
- Negatives tie to a defined universe: "as presently constituted" for the
  pleading; "identified or disclosed in the Respondent's disclosed material
  presently before the Commission" for disclosure.
- Facts are stated; conclusions are never pleaded ("thereby admits",
  "Applying paragraph X" are the historical failures).
- A composite in Part B is expressly additive and never replaces Part A.
- The strongest material is the documented absence — never paraphrase it away
  in a summary.

## After any change

Rebuild in order: `build_form24_second.py` → `build_form24_official.py` →
`build_form24_annexureA.py` → `build_form24_partB.py` →
`build_form24_mock_response.py` (refresh `/tmp/f185.json` between second and
mock — see the extraction snippet in verify_form24.py). Then run L1. Then
commit. The serve-clean copy is `SERVE=1 python3 build_form24_official.py`.
