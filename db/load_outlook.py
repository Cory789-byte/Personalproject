"""Pull emails from your *Windows-signed-in* Outlook desktop profile into the
emails table — no IMAP, no app password.

How this uses your PC login:
  Outlook desktop is already authenticated as your Windows user via
  Microsoft 365 SSO. This script talks to it via COM automation
  (win32com), so it inherits that session — there's nothing to type.

Pre-requisites (one-time on the PC):
  1. Outlook desktop installed and signed in.
  2. pip install pywin32 pymysql
  3. MySQL env vars set:
        set MYSQL_USER=root
        set MYSQL_PASSWORD=your_mysql_password

Usage:
  python db/load_outlook.py --query "Southport"
  python db/load_outlook.py --query "Southport" --since-days 365
  python db/load_outlook.py --query "Southport" --folder "Inbox/Southport"

Re-running is safe: rows upsert on (matter_id, message_id).
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pymysql

from _pc_user import pc_user

OL_FOLDER_INBOX = 6  # OlDefaultFolders.olFolderInbox


def mysql_connect(database: str) -> pymysql.connections.Connection:
    return pymysql.connect(
        host=os.environ.get("MYSQL_HOST", "127.0.0.1"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        database=database,
        charset="utf8mb4",
        autocommit=False,
    )


def get_matter_id(cur, matter_ref: str) -> int:
    cur.execute("SELECT id FROM matters WHERE matter_ref = %s", (matter_ref,))
    row = cur.fetchone()
    if not row:
        raise SystemExit(
            f"matter_ref {matter_ref!r} not found — run db/southport_schema.sql first"
        )
    return row[0]


def open_outlook():
    try:
        import win32com.client  # type: ignore[import-not-found]
    except ImportError:
        raise SystemExit(
            "pywin32 not installed. Run: pip install pywin32\n"
            "(this loader is Windows-only — use db/load_emails.py for IMAP elsewhere.)"
        )
    outlook = win32com.client.Dispatch("Outlook.Application")
    return outlook.GetNamespace("MAPI")


def resolve_folder(namespace, folder_path: str | None):
    """folder_path = None -> default Inbox; otherwise 'Inbox/Southport'."""
    if not folder_path:
        return namespace.GetDefaultFolder(OL_FOLDER_INBOX)
    parts = [p for p in folder_path.replace("\\", "/").split("/") if p]
    folder = namespace.GetDefaultFolder(OL_FOLDER_INBOX)
    if parts and parts[0].lower() == "inbox":
        parts = parts[1:]
    for name in parts:
        folder = folder.Folders[name]
    return folder


def filter_items(items, query: str, since_days: int | None):
    """Apply Outlook's Restrict() — server-side filter, much faster than walking."""
    items.Sort("[ReceivedTime]", True)
    clauses: list[str] = []
    if since_days is not None:
        cutoff = datetime.now() - timedelta(days=since_days)
        clauses.append(
            f"[ReceivedTime] >= '{cutoff.strftime('%m/%d/%Y %H:%M %p')}'"
        )
    if query:
        q = query.replace("'", "''")
        clauses.append(
            f"(@SQL=\"urn:schemas:httpmail:subject\" LIKE '%{q}%' OR "
            f"\"urn:schemas:httpmail:textdescription\" LIKE '%{q}%')"
        )
    if not clauses:
        return items
    restrict = " AND ".join(clauses)
    return items.Restrict(restrict)


def thread_id_for(item) -> str | None:
    cv = getattr(item, "ConversationID", None)
    return cv or None


def to_naive_dt(value) -> datetime | None:
    if value is None:
        return None
    try:
        if hasattr(value, "tzinfo") and value.tzinfo is not None:
            value = value.replace(tzinfo=None)
    except (AttributeError, TypeError):
        return None
    return value


def upsert(cur, matter_id: int, item, ingested_by: str) -> bool:
    message_id = (
        getattr(item, "InternetMessageID", None)
        or getattr(item, "EntryID", None)
    )
    if not message_id:
        return False
    body_text = getattr(item, "Body", None)
    body_html = getattr(item, "HTMLBody", None)
    has_attach = 1 if int(getattr(item.Attachments, "Count", 0) or 0) else 0
    cur.execute(
        """
        INSERT INTO emails
          (matter_id, message_id, thread_id, subject, from_addr, to_addrs,
           cc_addrs, sent_on, body_text, body_html, has_attachments,
           ingested_by, source)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'outlook')
        ON DUPLICATE KEY UPDATE
          thread_id = VALUES(thread_id),
          subject = VALUES(subject),
          from_addr = VALUES(from_addr),
          to_addrs = VALUES(to_addrs),
          cc_addrs = VALUES(cc_addrs),
          sent_on = VALUES(sent_on),
          body_text = VALUES(body_text),
          body_html = VALUES(body_html),
          has_attachments = VALUES(has_attachments),
          ingested_by = VALUES(ingested_by),
          source = VALUES(source)
        """,
        (
            matter_id,
            str(message_id),
            thread_id_for(item),
            (getattr(item, "Subject", "") or "")[:512],
            (getattr(item, "SenderEmailAddress", "") or "")[:255],
            getattr(item, "To", None),
            getattr(item, "CC", None),
            to_naive_dt(getattr(item, "ReceivedTime", None) or getattr(item, "SentOn", None)),
            body_text,
            body_html,
            has_attach,
            ingested_by,
        ),
    )
    return True


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--matter-ref", default="SOUTHPORT-001")
    p.add_argument("--database", default="southport_matter")
    p.add_argument("--folder", default=None,
                   help="folder path under Inbox, e.g. \"Inbox/Southport\". "
                        "Default: Inbox.")
    p.add_argument("--query", required=True, help="search term, e.g. \"Southport\"")
    p.add_argument("--since-days", type=int, default=None,
                   help="restrict to messages newer than N days")
    args = p.parse_args()

    for var in ("MYSQL_USER", "MYSQL_PASSWORD"):
        if var not in os.environ:
            sys.stderr.write(f"set {var} environment variable\n")
            return 2

    namespace = open_outlook()
    folder = resolve_folder(namespace, args.folder)
    items = filter_items(folder.Items, args.query, args.since_days)

    user = pc_user()
    conn = mysql_connect(args.database)
    loaded = skipped = errors = 0
    try:
        with conn.cursor() as cur:
            matter_id = get_matter_id(cur, args.matter_ref)
            for item in items:
                if getattr(item, "Class", None) != 43:  # olMail
                    skipped += 1
                    continue
                try:
                    if upsert(cur, matter_id, item, ingested_by=user):
                        loaded += 1
                    else:
                        skipped += 1
                except Exception:
                    errors += 1
        conn.commit()
    finally:
        conn.close()

    print(f"outlook emails loaded={loaded} skipped={skipped} errors={errors} "
          f"(matter {args.matter_ref}, folder {args.folder or 'Inbox'}, "
          f"query {args.query!r}, ingested_by {user})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
