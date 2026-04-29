-- Migration: add ingested_by audit column + email source enum.
-- Run this only if you've already created the southport_matter database
-- with the previous schema and want to keep your data. Otherwise just
-- re-run db/southport_schema.sql (which is idempotent and starts fresh).

USE southport_matter;

ALTER TABLE emails
  ADD COLUMN ingested_by VARCHAR(128) NULL AFTER document_id,
  ADD COLUMN source ENUM('imap','outlook','manual') NOT NULL DEFAULT 'imap'
    AFTER ingested_by;

ALTER TABLE cloud_files
  ADD COLUMN ingested_by VARCHAR(128) NULL AFTER document_id;
