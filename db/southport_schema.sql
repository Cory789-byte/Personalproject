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
DROP VIEW  IF EXISTS v_cloud_unlinked;
DROP VIEW  IF EXISTS v_emails_by_thread;
DROP VIEW  IF EXISTS v_matter_counts;
DROP VIEW  IF EXISTS v_issues_by_document;
DROP VIEW  IF EXISTS v_issues_by_exhibit;
DROP VIEW  IF EXISTS v_issues_open;
DROP VIEW  IF EXISTS v_exhibits_by_officer;
DROP TABLE IF EXISTS cloud_files;
DROP TABLE IF EXISTS emails;
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
-- 5. emails — ingested mailbox messages linked to the matter. Populated by
--    db/load_emails.py (IMAP) or by hand-loading from .eml files.
-- ---------------------------------------------------------------------------
CREATE TABLE emails (
  id              INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  matter_id       INT UNSIGNED  NOT NULL,
  message_id      VARCHAR(255)  NOT NULL,                  -- RFC 2822 Message-ID
  thread_id       VARCHAR(255)  NULL,                      -- IMAP X-GM-THRID or References hash
  subject         VARCHAR(512)  NULL,
  from_addr       VARCHAR(255)  NULL,
  to_addrs        TEXT          NULL,
  cc_addrs        TEXT          NULL,
  sent_on         DATETIME      NULL,
  body_text       MEDIUMTEXT    NULL,
  body_html       MEDIUMTEXT    NULL,
  has_attachments TINYINT(1)    NOT NULL DEFAULT 0,
  document_id     INT UNSIGNED  NULL,                      -- optional link if also stored as a document
  notes           TEXT          NULL,
  created_at      TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_emails_matter_msg (matter_id, message_id),
  KEY ix_emails_thread (thread_id),
  KEY ix_emails_sent (sent_on),
  KEY ix_emails_from (from_addr),
  CONSTRAINT fk_emails_matter
    FOREIGN KEY (matter_id) REFERENCES matters (id)
    ON DELETE CASCADE,
  CONSTRAINT fk_emails_document
    FOREIGN KEY (document_id) REFERENCES documents (id)
    ON DELETE SET NULL
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------------
-- 6. cloud_files — every file seen in a synced cloud folder (OneDrive,
--    SharePoint local mirror, Google Drive, Dropbox, or just a local path).
--    Populated by db/load_onedrive.py. May link to a documents row once
--    a file has been formally indexed.
-- ---------------------------------------------------------------------------
CREATE TABLE cloud_files (
  id            INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  matter_id     INT UNSIGNED  NOT NULL,
  provider      ENUM('onedrive','sharepoint','gdrive','dropbox','local')
                              NOT NULL DEFAULT 'onedrive',
  relative_path VARCHAR(1024) NOT NULL,
  file_name     VARCHAR(255)  NOT NULL,
  size_bytes    BIGINT UNSIGNED NULL,
  sha256        CHAR(64)      NULL,
  modified_on   DATETIME      NULL,
  document_id   INT UNSIGNED  NULL,
  notes         TEXT          NULL,
  created_at    TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_cloud_matter_path (matter_id, provider, relative_path(512)),
  KEY ix_cloud_sha256 (sha256),
  KEY ix_cloud_modified (modified_on),
  CONSTRAINT fk_cloud_matter
    FOREIGN KEY (matter_id) REFERENCES matters (id)
    ON DELETE CASCADE,
  CONSTRAINT fk_cloud_document
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
                                          AND i.status IN ('open','in_review')) AS open_issues,
       (SELECT COUNT(*) FROM emails    e WHERE e.matter_id  = m.id) AS emails,
       (SELECT COUNT(*) FROM cloud_files c WHERE c.matter_id = m.id) AS cloud_files
FROM matters m;

CREATE VIEW v_cloud_unlinked AS
SELECT m.matter_ref,
       c.provider,
       c.relative_path,
       c.file_name,
       c.size_bytes,
       c.modified_on
FROM cloud_files c
JOIN matters m ON m.id = c.matter_id
WHERE c.document_id IS NULL
ORDER BY c.modified_on DESC;

CREATE VIEW v_emails_by_thread AS
SELECT m.matter_ref,
       e.thread_id,
       COUNT(*)        AS message_count,
       MIN(e.sent_on)  AS first_sent,
       MAX(e.sent_on)  AS last_sent,
       GROUP_CONCAT(DISTINCT e.from_addr ORDER BY e.from_addr SEPARATOR ', ') AS senders
FROM emails e
JOIN matters m ON m.id = e.matter_id
WHERE e.thread_id IS NOT NULL
GROUP BY m.matter_ref, e.thread_id;

-- ---------------------------------------------------------------------------
-- Seed row — usable defaults so the schema runs cleanly. Update once the real
-- matter ref / parties are known, e.g.:
--   UPDATE matters SET matter_ref='CO-25-XXXX', parties='Surname v QPS'
--   WHERE matter_ref='SOUTHPORT-001';
-- ---------------------------------------------------------------------------
INSERT INTO matters (matter_ref, parties, court, evidence_root, opened_on, notes)
VALUES (
  'SOUTHPORT-001',
  'TBC',
  'Magistrates Court of Queensland, Southport',
  'C:\\Evidence\\Southport',
  NULL,
  'Southport matter — scaffolded from db/southport_schema.sql'
);
