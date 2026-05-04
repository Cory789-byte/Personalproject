-- Shepherd v QPS — Evidence Management System
-- SQLite schema. Generated tables are populated by the parsers under legal_system/ingest/
-- Every row has a stable, slug-style id you can deep-link to from submissions.

PRAGMA foreign_keys = ON;

-- =====================================================================
-- Source documents (the 7 inputs ingested by the pipeline)
-- =====================================================================
CREATE TABLE IF NOT EXISTS source_documents (
  id              TEXT PRIMARY KEY,           -- e.g. 'alternative_case'
  filename        TEXT NOT NULL,
  title           TEXT NOT NULL,
  generated_at    TEXT,                       -- self-reported by the doc
  ingested_at     TEXT NOT NULL,              -- ISO timestamp
  sha256          TEXT NOT NULL,
  bytes           INTEGER NOT NULL,
  notes           TEXT
);

-- =====================================================================
-- Actors (people / officers / entities that appear in the record)
-- =====================================================================
CREATE TABLE IF NOT EXISTS actors (
  id              TEXT PRIMARY KEY,           -- slug
  display_name    TEXT NOT NULL,
  role            TEXT,                       -- 'complainant' / 'qps_officer' / 'witness' / 'magistrate' / 'lawyer' / 'aggrieved' / 'other'
  reg_number      TEXT,                       -- QPS regulation number where known
  organisation    TEXT,
  notes           TEXT
);

-- =====================================================================
-- Phases (chronological compartments from ALTERNATIVE_CASE.md)
-- =====================================================================
CREATE TABLE IF NOT EXISTS phases (
  id              TEXT PRIMARY KEY,           -- 'phase-0_5', 'phase-1', ...
  ordinal         REAL NOT NULL,              -- 0.5, 1, 2, 3 ... (real to fit phase 0.5 / 9.5)
  title           TEXT NOT NULL,
  summary         TEXT,
  source_doc_id   TEXT REFERENCES source_documents(id)
);

-- =====================================================================
-- Events (the chronology backbone)
-- Single canonical events table; rows can come from multiple sources and
-- be linked together via cross_refs.
-- =====================================================================
CREATE TABLE IF NOT EXISTS events (
  id              TEXT PRIMARY KEY,
  phase_id        TEXT REFERENCES phases(id),
  event_date      TEXT,                       -- ISO 'YYYY-MM-DD' or partial 'YYYY-MM'
  event_time      TEXT,                       -- 'HH:MM' if known
  date_label      TEXT,                       -- raw label from doc, may be approximate
  description     TEXT NOT NULL,
  ordinal         INTEGER,                    -- ordering within phase
  source_doc_id   TEXT REFERENCES source_documents(id),
  source_anchor   TEXT,                       -- markdown anchor in the source
  defeats         TEXT                        -- which prosecution element this row defeats (LOCKOUT TIMELINE col)
);

CREATE INDEX IF NOT EXISTS idx_events_phase    ON events(phase_id);
CREATE INDEX IF NOT EXISTS idx_events_date     ON events(event_date);

-- =====================================================================
-- Evidence anchors (the "Evidence anchors:" bullets under every event)
-- =====================================================================
CREATE TABLE IF NOT EXISTS evidence (
  id              TEXT PRIMARY KEY,           -- slug from anchor text
  ref             TEXT NOT NULL,              -- short ref e.g. 'AFF11', 'Easthope BWC 02:00', 'AFF05_19Feb_0726'
  text            TEXT NOT NULL,              -- full bullet text
  kind            TEXT,                       -- 'bwc' / 'affidavit' / 'email' / 'court_order' / 'whatsapp' / 'rti' / 'forensic' / 'statement' / 'other'
  source_path     TEXT,                       -- path inside case file if mentioned
  bwc_timestamp   TEXT,                       -- 'HH:MM:SS' or 'MM:SS' if applicable
  bwc_officer     TEXT,
  notes           TEXT
);

CREATE INDEX IF NOT EXISTS idx_evidence_kind ON evidence(kind);

-- =====================================================================
-- Many-to-many: events <-> evidence
-- =====================================================================
CREATE TABLE IF NOT EXISTS event_evidence (
  event_id        TEXT NOT NULL REFERENCES events(id) ON DELETE CASCADE,
  evidence_id     TEXT NOT NULL REFERENCES evidence(id) ON DELETE CASCADE,
  PRIMARY KEY (event_id, evidence_id)
);

-- =====================================================================
-- Many-to-many: events <-> actors
-- =====================================================================
CREATE TABLE IF NOT EXISTS event_actors (
  event_id        TEXT NOT NULL REFERENCES events(id) ON DELETE CASCADE,
  actor_id        TEXT NOT NULL REFERENCES actors(id) ON DELETE CASCADE,
  role_in_event   TEXT,
  PRIMARY KEY (event_id, actor_id)
);

-- =====================================================================
-- Charges + their elements + per-element failures
-- =====================================================================
CREATE TABLE IF NOT EXISTS charges (
  id              TEXT PRIMARY KEY,
  matter_id       TEXT NOT NULL,              -- e.g. 'CO-25-2722'
  title           TEXT NOT NULL,
  court           TEXT,
  status          TEXT,
  alleged_summary TEXT,
  source_doc_id   TEXT REFERENCES source_documents(id)
);

CREATE TABLE IF NOT EXISTS charge_elements (
  id              TEXT PRIMARY KEY,
  charge_id       TEXT NOT NULL REFERENCES charges(id) ON DELETE CASCADE,
  ordinal         INTEGER NOT NULL,
  text            TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS charge_failures (
  id              TEXT PRIMARY KEY,
  charge_id       TEXT NOT NULL REFERENCES charges(id) ON DELETE CASCADE,
  element_ref     TEXT,                       -- e.g. 'Element 4'
  reason          TEXT NOT NULL,
  notes           TEXT
);

CREATE TABLE IF NOT EXISTS charge_displacing_documents (
  charge_id       TEXT NOT NULL REFERENCES charges(id) ON DELETE CASCADE,
  evidence_id     TEXT REFERENCES evidence(id) ON DELETE SET NULL,
  ref             TEXT NOT NULL,
  PRIMARY KEY (charge_id, ref)
);

-- =====================================================================
-- Speaker corrections / mis-attributions (CORRECTION_REGISTER.md)
-- =====================================================================
CREATE TABLE IF NOT EXISTS corrections (
  id              TEXT PRIMARY KEY,           -- 'C-001' ...
  status          TEXT NOT NULL,
  quote           TEXT NOT NULL,
  original_speaker TEXT,
  corrected_speaker TEXT,
  anchor          TEXT,
  category        TEXT,
  legal_effect    TEXT,
  source_doc_id   TEXT REFERENCES source_documents(id)
);

-- =====================================================================
-- Submission Quote Diff (SUBMISSION_QUOTE_DIFF.md)
-- Each row records a quoted line in the user's submission docs and the
-- closest large-v3 BWC transcript line.
-- =====================================================================
CREATE TABLE IF NOT EXISTS quote_diffs (
  id              TEXT PRIMARY KEY,
  bucket          TEXT NOT NULL,              -- 'exact' / 'drift' / 'no_match'
  ratio           REAL,
  source_doc_file TEXT,                       -- e.g. '2026-05-03_CShepherd_SUB_Submission_EDR19098.docx'
  submission_text TEXT NOT NULL,
  largev3_file    TEXT,
  largev3_text    TEXT,
  source_doc_id   TEXT REFERENCES source_documents(id)
);

CREATE INDEX IF NOT EXISTS idx_quote_diffs_bucket ON quote_diffs(bucket);

-- =====================================================================
-- Statements (witness paragraphs from UNDERLYING_FACTS_REBUTTAL.md)
-- =====================================================================
CREATE TABLE IF NOT EXISTS statements (
  id              TEXT PRIMARY KEY,
  witness_id      TEXT REFERENCES actors(id),
  taken_date      TEXT,
  taking_officer_id TEXT REFERENCES actors(id),
  qprime_ref      TEXT,
  source_path     TEXT,
  source_doc_id   TEXT REFERENCES source_documents(id)
);

CREATE TABLE IF NOT EXISTS statement_paragraphs (
  id              TEXT PRIMARY KEY,
  statement_id    TEXT NOT NULL REFERENCES statements(id) ON DELETE CASCADE,
  para_label      TEXT NOT NULL,              -- '¶1', '¶6-25', '¶27'
  status          TEXT NOT NULL,              -- 'agreed' / 'disputed' / 'partial' / 'dispositive'
  status_emoji    TEXT,                       -- ✓ / ✘ / ⚠ / 🎯
  verbatim        TEXT,
  legal_effect    TEXT,
  ordinal         INTEGER
);

CREATE TABLE IF NOT EXISTS statement_para_evidence (
  paragraph_id    TEXT NOT NULL REFERENCES statement_paragraphs(id) ON DELETE CASCADE,
  evidence_id     TEXT REFERENCES evidence(id) ON DELETE SET NULL,
  ref             TEXT NOT NULL,
  PRIMARY KEY (paragraph_id, ref)
);

-- =====================================================================
-- Forensic Iteration Comparison (Shepherd_v_QPS_Forensic_Analysis docx)
-- =====================================================================
CREATE TABLE IF NOT EXISTS iterations (
  id              TEXT PRIMARY KEY,           -- 'iter-1', 'iter-2', 'iter-3'
  ordinal         INTEGER NOT NULL,
  document        TEXT NOT NULL,
  date_metadata   TEXT,
  author          TEXT,
  producer        TEXT,
  pages           INTEGER,
  occasion        TEXT
);

CREATE TABLE IF NOT EXISTS iteration_field_changes (
  id              TEXT PRIMARY KEY,
  ordinal         INTEGER NOT NULL,
  category        TEXT,
  field           TEXT NOT NULL,
  iter1_value     TEXT,
  iter2_value     TEXT,
  iter3_value     TEXT,
  who_changed     TEXT,
  when_changed    TEXT,
  contradicted_by TEXT,
  legal_significance TEXT
);

CREATE TABLE IF NOT EXISTS ware_schedule (
  id              TEXT PRIMARY KEY,           -- 'A1' .. 'B10'
  part            TEXT NOT NULL,              -- 'A' or 'B'
  description     TEXT NOT NULL,
  iter1_status    TEXT,
  iter2_status    TEXT,
  iter3_status    TEXT,
  current_status  TEXT,
  days_out        INTEGER,
  legal_consequence TEXT
);

-- =====================================================================
-- Lockout-night row table (LOCKOUT_NIGHT_TIMELINE_CARD.md)
-- (mirror of 14 rows; also exploded into events for the master timeline)
-- =====================================================================
CREATE TABLE IF NOT EXISTS lockout_rows (
  row_no          INTEGER PRIMARY KEY,
  event_id        TEXT REFERENCES events(id),
  time_label      TEXT,
  actor           TEXT,
  event_text      TEXT,
  defeats         TEXT
);

-- =====================================================================
-- Cross-references (typed links between any two entities)
-- Used to wire ALTERNATIVE_CASE phases <-> CHARGES <-> CORRECTIONS etc.
-- =====================================================================
CREATE TABLE IF NOT EXISTS cross_refs (
  id              INTEGER PRIMARY KEY AUTOINCREMENT,
  src_table       TEXT NOT NULL,
  src_id          TEXT NOT NULL,
  dst_table       TEXT NOT NULL,
  dst_id          TEXT NOT NULL,
  kind            TEXT,                       -- 'cites' / 'contradicts' / 'corroborates' / 'duplicates' / 'see_also'
  notes           TEXT
);

CREATE INDEX IF NOT EXISTS idx_xref_src ON cross_refs(src_table, src_id);
CREATE INDEX IF NOT EXISTS idx_xref_dst ON cross_refs(dst_table, dst_id);

-- =====================================================================
-- Validation findings (output of build/validate.py)
-- =====================================================================
CREATE TABLE IF NOT EXISTS validation_findings (
  id              INTEGER PRIMARY KEY AUTOINCREMENT,
  severity        TEXT NOT NULL,              -- 'info' / 'warning' / 'error'
  category        TEXT NOT NULL,              -- 'drift' / 'missing_anchor' / 'date_inconsistency' / 'duplicate' / 'orphan'
  entity_table    TEXT,
  entity_id       TEXT,
  message         TEXT NOT NULL,
  detail          TEXT
);
