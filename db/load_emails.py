"""Pull emails from an IMAP mailbox into the southport_matter MySQL database.

Works with Gmail, Outlook/Microsoft 365, Fastmail, iCloud, etc. — anything that
speaks IMAP. For Gmail/Outlook you must use an *app password*, not your real
password (regular logins are blocked by the provider).

Usage:
    pip install -r db/requirements.txt
    set MYSQL_USER=root
    set MYSQL_PASSWORD=your_mysql_password
    set IMAP_HOST=imap.gmail.com
    set IMAP_USER=you@gmail.com
    set IMAP_PASSWORD=your_app_password

    # pull every email mentioning "Southport" from the last 365 days:
    python db/load_emails.py --query "Southport" --since-days 365

    # pull from a specific folder/label:
    python db/load_emails.py --query "Southport" --mailbox "[Gmail]/All Mail"

The loader uses the IMAP search criteria SUBJECT, BODY, FROM, or TEXT depending
on --field (default TEXT, which matches subject + body + headers). Re-running
is safe: rows are upserted on (matter_id, message_id).
"""

from __future__ import annotations

import argparse
import email
import email.policy
import email.utils
import imaplib
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage

import pymysql


def imap_connect() -> imaplib.IMAP4_SSL:
    host = os.environ["IMAP_HOST"]
    port = int(os.environ.get("IMAP_PORT", "993"))
    conn = imaplib.IMAP4_SSL(host, port)
    conn.login(os.environ["IMAP_USER"], os.environ["IMAP_PASSWORD"])
    return conn


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


def build_search(field: str, query: str, since_days: int | None) -> bytes:
    parts: list[str] = []
    if since_days is not None:
        since = datetime.now(timezone.utc) - timedelta(days=since_days)
        parts.append(f'SINCE {since.strftime("%d-%b-%Y")}')
    field = field.upper()
    if field not in {"SUBJECT", "BODY", "FROM", "TO", "TEXT"}:
        raise SystemExit(f"unsupported --field {field!r}")
    parts.append(f'{field} "{query}"')
    return ("(" + " ".join(parts) + ")").encode("utf-8")


def get_body(msg: EmailMessage) -> tuple[str | None, str | None, bool]:
    text_part = None
    html_part = None
    has_attach = False
    if msg.is_multipart():
        for part in msg.walk():
            disp = (part.get_content_disposition() or "").lower()
            if disp == "attachment":
                has_attach = True
                continue
            ctype = part.get_content_type()
            if ctype == "text/plain" and text_part is None:
                text_part = part.get_content()
            elif ctype == "text/html" and html_part is None:
                html_part = part.get_content()
    else:
        ctype = msg.get_content_type()
        content = msg.get_content() if ctype.startswith("text/") else None
        if ctype == "text/html":
            html_part = content
        else:
            text_part = content
    return text_part, html_part, has_attach


def thread_id_from(msg: EmailMessage) -> str | None:
    refs = msg.get("References") or msg.get("In-Reply-To")
    if refs:
        ids = re.findall(r"<[^>]+>", refs)
        if ids:
            return ids[0]
    mid = msg.get("Message-ID")
    return mid.strip() if mid else None


def parse_sent_on(msg: EmailMessage) -> datetime | None:
    raw = msg.get("Date")
    if not raw:
        return None
    try:
        dt = email.utils.parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        return None
    if dt is None:
        return None
    if dt.tzinfo is not None:
        dt = dt.astimezone(timezone.utc).replace(tzinfo=None)
    return dt


def upsert(cur, matter_id: int, msg: EmailMessage) -> bool:
    message_id = (msg.get("Message-ID") or "").strip()
    if not message_id:
        return False
    text, html, has_attach = get_body(msg)
    cur.execute(
        """
        INSERT INTO emails
          (matter_id, message_id, thread_id, subject, from_addr, to_addrs,
           cc_addrs, sent_on, body_text, body_html, has_attachments)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
          thread_id = VALUES(thread_id),
          subject = VALUES(subject),
          from_addr = VALUES(from_addr),
          to_addrs = VALUES(to_addrs),
          cc_addrs = VALUES(cc_addrs),
          sent_on = VALUES(sent_on),
          body_text = VALUES(body_text),
          body_html = VALUES(body_html),
          has_attachments = VALUES(has_attachments)
        """,
        (
            matter_id,
            message_id,
            thread_id_from(msg),
            (msg.get("Subject") or "")[:512],
            (msg.get("From") or "")[:255],
            msg.get("To"),
            msg.get("Cc"),
            parse_sent_on(msg),
            text,
            html,
            1 if has_attach else 0,
        ),
    )
    return True


def fetch_messages(imap: imaplib.IMAP4_SSL, mailbox: str, criteria: bytes):
    typ, _ = imap.select(mailbox, readonly=True)
    if typ != "OK":
        raise SystemExit(f"cannot select mailbox {mailbox!r}")
    typ, data = imap.search(None, criteria)
    if typ != "OK":
        raise SystemExit(f"IMAP search failed: {data!r}")
    ids = data[0].split()
    for uid in ids:
        typ, payload = imap.fetch(uid, "(RFC822)")
        if typ != "OK" or not payload or not payload[0]:
            continue
        raw = payload[0][1]
        yield email.message_from_bytes(raw, policy=email.policy.default)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--matter-ref", default="SOUTHPORT-001")
    p.add_argument("--database", default="southport_matter")
    p.add_argument("--mailbox", default="INBOX")
    p.add_argument("--query", required=True, help="search term, e.g. \"Southport\"")
    p.add_argument("--field", default="TEXT",
                   help="IMAP field to search: SUBJECT, BODY, FROM, TO, or TEXT")
    p.add_argument("--since-days", type=int, default=None,
                   help="restrict to messages newer than N days")
    args = p.parse_args()

    for var in ("MYSQL_USER", "MYSQL_PASSWORD", "IMAP_HOST", "IMAP_USER", "IMAP_PASSWORD"):
        if var not in os.environ:
            sys.stderr.write(f"set {var} environment variable\n")
            return 2

    criteria = build_search(args.field, args.query, args.since_days)

    imap = imap_connect()
    conn = mysql_connect(args.database)
    loaded = skipped = 0
    try:
        with conn.cursor() as cur:
            matter_id = get_matter_id(cur, args.matter_ref)
            for msg in fetch_messages(imap, args.mailbox, criteria):
                if upsert(cur, matter_id, msg):
                    loaded += 1
                else:
                    skipped += 1
        conn.commit()
    finally:
        try:
            imap.close()
        except imaplib.IMAP4.error:
            pass
        imap.logout()
        conn.close()

    print(f"emails loaded={loaded} skipped={skipped} (matter {args.matter_ref}, "
          f"mailbox {args.mailbox}, field {args.field}, query {args.query!r})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
