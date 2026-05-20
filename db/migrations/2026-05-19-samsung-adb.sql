-- Migration: add Samsung ADB / Phone Link providers + per-provider view.
-- Safe to re-run; idempotent.

USE southport_matter;

ALTER TABLE cloud_files
  MODIFY COLUMN provider
    ENUM('onedrive','sharepoint','gdrive','dropbox','local','samsung_adb','phone_link')
    NOT NULL DEFAULT 'onedrive';

DROP VIEW IF EXISTS v_cloud_by_provider;
CREATE VIEW v_cloud_by_provider AS
SELECT m.matter_ref,
       c.provider,
       COUNT(*)              AS file_count,
       SUM(c.size_bytes)     AS total_bytes,
       SUM(c.sha256 IS NULL) AS unhashed_count,
       MAX(c.modified_on)    AS latest_mtime
FROM cloud_files c
JOIN matters m ON m.id = c.matter_id
GROUP BY m.matter_ref, c.provider;
