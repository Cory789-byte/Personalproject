# Gmail case-file ingest — 15 September 2026

Forwards from coryshepherd1@hotmail.com to the bolandsframeworks@gmail.com mailbox ("Historic
case-file copy ..."), read through the Gmail connector and written here by `scripts/gmail_ingest.py`.

- `ENUMERATION.tsv` — 173 rows (msg_id, thread_id, original sent UTC, original sender, subject,
  size, flag). Pages 1–2 of the 2024–25 items (WorkCover claim, Saines/Rinkin, OIC, Taylor/Hughes
  RTW) still to be appended.
- `MANIFEST.tsv` — the items actually written, with file paths.
- `messages/` — bodies with headers (UTC and AEST), boilerplate stripped. Filenames carry the
  original date/time and sender.
- `attachments/<date_sender_subject>/` — decoded attachments plus `_message.txt` (headers + body).
  ⛔ Inline images (image0*, ATT0*, *.gif) are never extracted or committed (.gitignore + extractor
  skip); one such image proved to be an unrelated identity document and was purged.
- Times in the original headers are UTC unless marked AEST (+10).
- ⛔ PID-track items (12–13 Feb 2026 conflict notice; 23 Feb 2026 ES 4822 outcome) are ingested
  for the record only and are not used in WC/2024/227 reasoning.
- Reasoning built from this set: `skill/references/THE-REASONING-CASE-two-lines-tracked-15SEP2026.md`.
