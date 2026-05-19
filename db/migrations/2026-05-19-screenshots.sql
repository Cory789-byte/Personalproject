-- Migration: add screenshots table + view + screenshots count on v_matter_counts.
-- Run only if you already created the database with an earlier schema. Otherwise
-- re-run db/southport_schema.sql (which is idempotent).

USE southport_matter;

CREATE TABLE IF NOT EXISTS screenshots (
  id            INT UNSIGNED  NOT NULL AUTO_INCREMENT,
  matter_id     INT UNSIGNED  NOT NULL,
  file_id       VARCHAR(255)  NOT NULL,
  filename      VARCHAR(512)  NOT NULL,
  captured_on   DATE          NULL,
  sender        VARCHAR(128)  NULL,
  verbatim_text MEDIUMTEXT    NULL,
  frame_a_tag   VARCHAR(64)   NULL,
  frame_b_tag   VARCHAR(64)   NULL,
  strand        VARCHAR(64)   NULL,
  source_path   VARCHAR(512)  NULL,
  sha256        CHAR(64)      NULL,
  ingested_by   VARCHAR(128)  NULL,
  notes         TEXT          NULL,
  created_at    TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_screenshots_matter_file (matter_id, file_id),
  KEY ix_screenshots_strand (strand),
  KEY ix_screenshots_captured (captured_on),
  CONSTRAINT fk_screenshots_matter
    FOREIGN KEY (matter_id) REFERENCES matters (id)
    ON DELETE CASCADE
) ENGINE=InnoDB;

DROP VIEW IF EXISTS v_screenshots_by_strand;
CREATE VIEW v_screenshots_by_strand AS
SELECT m.matter_ref, s.strand, s.captured_on, s.sender, s.filename,
       LEFT(s.verbatim_text, 240) AS preview, s.notes
FROM screenshots s
JOIN matters m ON m.id = s.matter_id
WHERE s.strand IS NOT NULL
ORDER BY s.strand, s.captured_on;

-- Rebuild v_matter_counts to include the new screenshots count.
DROP VIEW IF EXISTS v_matter_counts;
CREATE VIEW v_matter_counts AS
SELECT m.matter_ref,
       m.parties,
       (SELECT COUNT(*) FROM exhibits  e WHERE e.matter_id  = m.id) AS exhibits,
       (SELECT COUNT(*) FROM documents d WHERE d.matter_id  = m.id) AS documents,
       (SELECT COUNT(*) FROM issues    i WHERE i.matter_id  = m.id) AS issues,
       (SELECT COUNT(*) FROM issues    i WHERE i.matter_id  = m.id
                                          AND i.status IN ('open','in_review')) AS open_issues,
       (SELECT COUNT(*) FROM emails    e WHERE e.matter_id  = m.id) AS emails,
       (SELECT COUNT(*) FROM cloud_files c WHERE c.matter_id = m.id) AS cloud_files,
       (SELECT COUNT(*) FROM screenshots s WHERE s.matter_id = m.id) AS screenshots
FROM matters m;
