-- Southport matter — MySQL 8.x schema
--
-- Run on your PC:
--   mysql -u root -p < db/southport_schema.sql
--
-- Schema scope: minimal 4 tables (matters, exhibits, documents, issues)
-- plus read-only views for common queries. Designed to be loaded by the
-- bwc-evidence-processor pipeline (skills/bwc-evidence-processor) once a
-- matter_southport.json keyword set is in place.

CREATE DATABASE IF NOT EXISTS southport_matter
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

USE southport_matter;

-- Drop in reverse-dependency order so the script is idempotent.
DROP VIEW  IF EXISTS v_matter_counts;
DROP VIEW  IF EXISTS v_issues_by_document;
DROP VIEW  IF EXISTS v_issues_by_exhibit;
DROP VIEW  IF EXISTS v_issues_open;
DROP VIEW  IF EXISTS v_exhibits_by_officer;
DROP TABLE IF EXISTS issues;
DROP TABLE IF EXISTS documents;
DROP TABLE IF EXISTS exhibits;
DROP TABLE IF EXISTS matters;

-- ---------------------------------------------------------------------------
-- 1. matters — one row per legal matter. Southport is a single row here, but
--    the table is keyed so the same DB can hold sibling matters later.
-- ---------------------------------------------------------------------------
CREATE TABLE matters (
  id              INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  matter_ref      VARCHAR(64)   NOT NULL,                  -- e.g. CO-25-XXXX
  parties         VARCHAR(255)  NOT NULL,                  -- e.g. "Shepherd v QPS"
  court           VARCHAR(128)  NULL,
  evidence_root   VARCHAR(512)  NULL,                      -- e.g. C:\Evidence\Southport
  opened_on       DATE          NULL,
  notes           TEXT          NULL,
  created_at      TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_matters_ref (matter_ref)
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------------
-- 2. exhibits — BWC and other primary evidentiary exhibits.
-- ---------------------------------------------------------------------------
CREATE TABLE exhibits (
  id               INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  matter_id        INT UNSIGNED  NOT NULL,
  exhibit_id       VARCHAR(64)   NOT NULL,                 -- e.g. BWC-001
  officer          VARCHAR(255)  NULL,
  captured_on      DATETIME      NULL,
  duration_seconds INT UNSIGNED  NULL,
  location         VARCHAR(255)  NULL,
  key_issue        VARCHAR(512)  NULL,
  source_path      VARCHAR(512)  NULL,
  sha256           CHAR(64)      NULL,
  notes            TEXT          NULL,
  created_at       TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_exhibits_matter_exhibit (matter_id, exhibit_id),
  KEY ix_exhibits_officer (officer),
  KEY ix_exhibits_captured (captured_on),
  CONSTRAINT fk_exhibits_matter
    FOREIGN KEY (matter_id) REFERENCES matters (id)
    ON DELETE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------------
-- 3. documents — supporting documents (QPS records, correspondence, court
--    filings, medical, third-party). Mirrors output/DOCUMENT_INDEX.md.
-- ---------------------------------------------------------------------------
CREATE TABLE documents (
  id           INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  matter_id    INT UNSIGNED  NOT NULL,
  doc_id       VARCHAR(64)   NOT NULL,                     -- e.g. DOC-0001
  category     ENUM('qps','correspondence','court','medical','third_party','other')
                              NOT NULL DEFAULT 'other',
  title        VARCHAR(512)  NOT NULL,
  author       VARCHAR(255)  NULL,
  dated_on     DATE          NULL,
  source_path  VARCHAR(512)  NULL,
  sha256       CHAR(64)      NULL,
  notes        TEXT          NULL,
  created_at   TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_documents_matter_doc (matter_id, doc_id),
  KEY ix_documents_category (category),
  KEY ix_documents_dated (dated_on),
  CONSTRAINT fk_documents_matter
    FOREIGN KEY (matter_id) REFERENCES matters (id)
    ON DELETE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------------
-- 4. issues — flagged issues across the corpus (mirrors MASTER_ISSUES_LOG.md).
--    May cite one exhibit and/or one document; both optional.
-- ---------------------------------------------------------------------------
CREATE TABLE issues (
  id           INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  matter_id    INT UNSIGNED  NOT NULL,
  severity     ENUM('low','medium','high','critical') NOT NULL DEFAULT 'medium',
  status       ENUM('open','in_review','resolved','dismissed') NOT NULL DEFAULT 'open',
  title        VARCHAR(255)  NOT NULL,
  description  TEXT          NULL,
  exhibit_id   INT UNSIGNED  NULL,
  document_id  INT UNSIGNED  NULL,
  opm_ref      VARCHAR(128)  NULL,                         -- e.g. "OPM 14.3.2"
  created_on   DATE          NULL,
  notes        TEXT          NULL,
  created_at   TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY ix_issues_status_severity (status, severity),
  CONSTRAINT fk_issues_matter
    FOREIGN KEY (matter_id) REFERENCES matters (id)
    ON DELETE CASCADE,
  CONSTRAINT fk_issues_exhibit
    FOREIGN KEY (exhibit_id) REFERENCES exhibits (id)
    ON DELETE SET NULL,
  CONSTRAINT fk_issues_document
    FOREIGN KEY (document_id) REFERENCES documents (id)
    ON DELETE SET NULL
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------------
-- Views — read-only convenience queries.
-- ---------------------------------------------------------------------------

CREATE VIEW v_exhibits_by_officer AS
SELECT m.matter_ref,
       e.officer,
       COUNT(*)                     AS exhibit_count,
       SUM(e.duration_seconds) / 60 AS total_minutes
FROM exhibits e
JOIN matters m ON m.id = e.matter_id
WHERE e.officer IS NOT NULL
GROUP BY m.matter_ref, e.officer;

CREATE VIEW v_issues_open AS
SELECT i.id,
       m.matter_ref,
       i.severity,
       i.status,
       i.title,
       i.opm_ref,
       e.exhibit_id   AS exhibit_ref,
       d.doc_id       AS document_ref,
       i.created_on
FROM issues i
JOIN matters m       ON m.id = i.matter_id
LEFT JOIN exhibits e ON e.id = i.exhibit_id
LEFT JOIN documents d ON d.id = i.document_id
WHERE i.status IN ('open', 'in_review')
ORDER BY FIELD(i.severity,'critical','high','medium','low'),
         i.created_on DESC;

CREATE VIEW v_issues_by_exhibit AS
SELECT e.exhibit_id,
       e.officer,
       COUNT(i.id) AS issue_count,
       SUM(i.severity = 'critical') AS critical_count,
       SUM(i.severity = 'high')     AS high_count
FROM exhibits e
LEFT JOIN issues i ON i.exhibit_id = e.id
GROUP BY e.id, e.exhibit_id, e.officer;

CREATE VIEW v_issues_by_document AS
SELECT d.doc_id,
       d.category,
       d.title,
       COUNT(i.id) AS issue_count,
       SUM(i.severity = 'critical') AS critical_count,
       SUM(i.severity = 'high')     AS high_count
FROM documents d
LEFT JOIN issues i ON i.document_id = d.id
GROUP BY d.id, d.doc_id, d.category, d.title;

CREATE VIEW v_matter_counts AS
SELECT m.matter_ref,
       m.parties,
       (SELECT COUNT(*) FROM exhibits  e WHERE e.matter_id  = m.id) AS exhibits,
       (SELECT COUNT(*) FROM documents d WHERE d.matter_id  = m.id) AS documents,
       (SELECT COUNT(*) FROM issues    i WHERE i.matter_id  = m.id) AS issues,
       (SELECT COUNT(*) FROM issues    i WHERE i.matter_id  = m.id
                                          AND i.status IN ('open','in_review')) AS open_issues
FROM matters m;

-- ---------------------------------------------------------------------------
-- Seed row — replace the <<FILL IN>> markers with the real Southport matter
-- details, then re-run this script (or just this INSERT) on your MySQL.
-- ---------------------------------------------------------------------------
INSERT INTO matters (matter_ref, parties, court, evidence_root, opened_on, notes)
VALUES (
  '<<FILL IN: matter_ref e.g. CO-25-XXXX>>',
  '<<FILL IN: parties e.g. Surname v QPS>>',
  '<<FILL IN: court e.g. Magistrates Court of Queensland, Southport>>',
  '<<FILL IN: evidence_root e.g. C:\\Evidence\\Southport>>',
  NULL,
  'Southport matter — scaffolded from db/southport_schema.sql'
);
