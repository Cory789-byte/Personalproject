# Shepherd v QPS — Evidence Management System

A reproducible toolchain that ingests the seven auto-generated case-file
artefacts in `source_documents/` into a normalised SQLite database, runs
cross-document validation, and emits a fully navigable, deep-linkable
static-HTML site plus a portable JSON export.

> **Disclaimer.** This is an internal navigation aid built from the
> ingested case-file artefacts. It is **not** legal advice, and it does
> **not** stand in for Australian counsel. For the QHRC conciliation on
> 14 May 2026 and the continuing CO-25-2722 / CO2500030466 prosecutions,
> retain a Queensland-admitted lawyer (LawRight, Caxton Legal Centre, or
> counsel of choice).

---

## What goes in

`source_documents/` (committed):

| File | Title |
|------|-------|
| `ALTERNATIVE_CASE.md` | Affirmative chronology — 12 phases, 63 events |
| `CHARGES_SUMMARY.md` | Per-charge element-by-element rebuttal — 4 charges |
| `CORRECTION_REGISTER.md` | Speaker mis-attribution register — 13 entries |
| `LOCKOUT_NIGHT_TIMELINE_CARD.md` | 14-row chronological exhibit (lockout night) |
| `SUBMISSION_QUOTE_DIFF.md` | 228-quote drift audit (Submission vs large-v3) |
| `UNDERLYING_FACTS_REBUTTAL.md` | 26 statements / 210 paragraph-by-paragraph rebuttals |
| `Shepherd_v_QPS_Forensic_Analysis_4May2026.docx` | Three-iteration disclosure analysis + Ware schedule |

## What comes out

After running the pipeline:

```
legal_system/
├── db/case.db                        # SQLite database (1 file, 22 tables)
└── output/
    ├── data.json                     # full JSON export (~1 MB, 2,769 rows)
    └── site/                         # static HTML site (~1,278 pages)
        ├── index.html                # dashboard
        ├── timeline.html             # all events, filterable
        ├── lockout_night.html        # 14-row card
        ├── charges/                  # per-charge teardown pages
        ├── events/                   # one page per event (deep-linkable)
        ├── evidence/                 # one page per evidence anchor
        ├── statements/               # one page per witness statement
        ├── paragraphs/               # one page per paragraph rebuttal
        ├── actors/                   # one page per person/agency
        ├── phases/                   # 12 chronological compartments
        ├── corrections.html          # speaker register
        ├── quote_diff.html           # quote drift report (filterable)
        ├── iterations.html           # 3-iteration field comparison
        ├── ware.html                 # 33-item disclosure schedule
        └── validation.html           # internal-consistency findings
```

Every entity has a stable URL fragment so submissions can deep-link.
Examples to paste into a PDF / docx / email body:

- `legal_system/output/site/events/lockout-row-09.html` — the 1:54 AM Constable warning
- `legal_system/output/site/charges/charge-co-25-2722.html` — DV-breach element-by-element
- `legal_system/output/site/ware.html#A4` — outstanding 5-page Davies statement
- `legal_system/output/site/iterations.html#fc-08` — three-officer arresting-officer contradiction
- `legal_system/output/site/statements/stmt-negro-25feb2025.html` — Negro statement paragraph grid

## How to run

Requires Python 3.9+ and `python-docx` (only needed for the `.docx` ingest).

```bash
# from the repo root
pip install -r legal_system/requirements.txt
python3 -m legal_system.build.run_all
```

Or step-by-step:

```bash
make -C legal_system db          # build SQLite from sources
make -C legal_system validate    # run internal-consistency checks
make -C legal_system site        # build static HTML site
make -C legal_system json        # export data.json
```

## CLI search

```bash
# all events on the lockout date
python3 -m legal_system.build.search events --on 2025-02-24

# all evidence anchors of kind "bwc"
python3 -m legal_system.build.search evidence --kind bwc

# anything mentioning a phrase
python3 -m legal_system.build.search evidence --grep "Form 13"

# only outstanding Ware-schedule items
python3 -m legal_system.build.search ware --outstanding

# only paragraphs marked dispositive
python3 -m legal_system.build.search paragraphs --status dispositive

# all submission quotes flagged as drift
python3 -m legal_system.build.search quotes --bucket drift

# a single actor's complete event timeline
python3 -m legal_system.build.search actor easthope
```

## Architecture

```
source_documents/   →   legal_system/ingest/   →   case.db   →   build_html / export_json / search
        (in)               (parsers)          (normalised)         (out)
```

### Schema (22 tables)

`source_documents`, `actors`, `phases`, `events`, `evidence`,
`event_evidence`, `event_actors`, `charges`, `charge_elements`,
`charge_failures`, `charge_displacing_documents`, `corrections`,
`quote_diffs`, `statements`, `statement_paragraphs`,
`statement_para_evidence`, `iterations`, `iteration_field_changes`,
`ware_schedule`, `lockout_rows`, `cross_refs`, `validation_findings`.

Schema source: `legal_system/db/schema.sql`. Drop the DB and re-run any
time the source documents change — the build is fully idempotent.

### Parsers (`legal_system/ingest/`)

Each parser is independent and only knows its own source file. Parsers
write into `case.db` directly. Add a new source by writing a new parser
+ wiring it into `build_database.py`.

| File | Source | Tables it populates |
|------|--------|---------------------|
| `parse_alternative_case.py` | ALTERNATIVE_CASE.md | phases, events, evidence |
| `parse_charges_summary.py` | CHARGES_SUMMARY.md | charges, elements, failures, displacing |
| `parse_correction_register.py` | CORRECTION_REGISTER.md | corrections |
| `parse_lockout_timeline.py` | LOCKOUT_NIGHT_TIMELINE_CARD.md | lockout_rows + events |
| `parse_quote_diff.py` | SUBMISSION_QUOTE_DIFF.md | quote_diffs |
| `parse_underlying_facts.py` | UNDERLYING_FACTS_REBUTTAL.md | statements, paragraphs, evidence |
| `parse_forensic_docx.py` | Forensic_Analysis_4May2026.docx | iterations, field_changes, ware_schedule |
| `seed_actors.py` | hand-curated | actors (canonical 33-row catalogue) |

### Validation (`legal_system/build/validate.py`)

Cross-document checks:

- **drift** — submission quotes that diverge from large-v3 BWC transcripts
- **orphan** — evidence anchors with no event/paragraph link
- **missing_date** — events without a parseable ISO date
- **outstanding_disclosure** — Ware-schedule items still flagged outstanding
- **iteration_amendment** — iteration field changes that engage s 48 Justices Act / s 590AB Code
- **cross_doc_quote** — canonical Davies / Easthope quotes appearing across multiple sources (verify wording matches)
- **correction_in_submission** — speaker corrections whose quote still appears uncorrected in a submission doc
- **duplicate_event** — events sharing date + 30-char prefix from different sources

Findings are written to the `validation_findings` table and rendered at
`output/site/validation.html`.

## Adding new evidence

1. Drop or update a file in `source_documents/`.
2. Re-run `make -C legal_system all`.
3. Re-verify `output/site/validation.html`.

## Provenance

The `source_documents` table records the SHA-256 + byte size of every
ingested file. If a file changes, the hash changes, and the diff is
visible on `index.html`.

## What this system deliberately does not do

- **It does not give legal advice.** It surfaces the user's existing
  record. Strategy, pleading, and advocacy require Australian counsel.
- **It does not "validate" external facts.** It only checks internal
  consistency between the seven ingested artefacts.
- **It does not modify source files.** All ingested files are read-only.
  Re-runs rebuild the DB from scratch — your inputs are never touched.

## Generated rows (current run)

| Bucket | Count |
|---|---|
| events | 77 |
| evidence anchors | 945 |
| witness paragraphs | 210 |
| iteration field changes | 30 |
| Ware schedule items | 33 (21 outstanding) |
| corrections | 13 |
| quote-diff rows | 228 |
| validation findings | 172 |
| HTML pages | 1,278 |
