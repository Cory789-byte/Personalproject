"""Load CSVs into the southport_matter MySQL database.

Usage:
    pip install -r db/requirements.txt
    # set credentials once per shell:
    set MYSQL_USER=root
    set MYSQL_PASSWORD=your_password
    python db/load_southport.py --matter-ref SOUTHPORT-001

Reads, in order, from db/templates/ (override with --csv-dir):
    exhibits.csv   -> exhibits
    documents.csv  -> documents
    issues.csv     -> issues

CSVs use the column names from each table. Foreign-key columns in issues.csv
should reference the human-readable IDs (exhibit_id like 'BWC-001', doc_id
like 'DOC-0001'); the loader resolves them to internal row IDs.

Rows with a duplicate (matter_id, exhibit_id) or (matter_id, doc_id) are
skipped — re-running the loader is safe.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from pathlib import Path

import pymysql


def connect(database: str) -> pymysql.connections.Connection:
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


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return [{k: (v or None) for k, v in row.items()} for row in csv.DictReader(f)]


def load_exhibits(cur, matter_id: int, rows: list[dict]) -> int:
    sql = """
        INSERT INTO exhibits
          (matter_id, exhibit_id, officer, captured_on, duration_seconds,
           location, key_issue, source_path, sha256, notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
          officer = VALUES(officer),
          captured_on = VALUES(captured_on),
          duration_seconds = VALUES(duration_seconds),
          location = VALUES(location),
          key_issue = VALUES(key_issue),
          source_path = VALUES(source_path),
          sha256 = VALUES(sha256),
          notes = VALUES(notes)
    """
    for r in rows:
        cur.execute(sql, (
            matter_id, r["exhibit_id"], r.get("officer"), r.get("captured_on"),
            r.get("duration_seconds"), r.get("location"), r.get("key_issue"),
            r.get("source_path"), r.get("sha256"), r.get("notes"),
        ))
    return len(rows)


def load_documents(cur, matter_id: int, rows: list[dict]) -> int:
    sql = """
        INSERT INTO documents
          (matter_id, doc_id, category, title, author, dated_on,
           source_path, sha256, notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
          category = VALUES(category),
          title = VALUES(title),
          author = VALUES(author),
          dated_on = VALUES(dated_on),
          source_path = VALUES(source_path),
          sha256 = VALUES(sha256),
          notes = VALUES(notes)
    """
    for r in rows:
        cur.execute(sql, (
            matter_id, r["doc_id"], r.get("category") or "other", r["title"],
            r.get("author"), r.get("dated_on"), r.get("source_path"),
            r.get("sha256"), r.get("notes"),
        ))
    return len(rows)


def load_issues(cur, matter_id: int, rows: list[dict]) -> int:
    sql = """
        INSERT INTO issues
          (matter_id, severity, status, title, description,
           exhibit_id, document_id, opm_ref, created_on, notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for r in rows:
        exhibit_pk = None
        if r.get("exhibit_ref"):
            cur.execute(
                "SELECT id FROM exhibits WHERE matter_id = %s AND exhibit_id = %s",
                (matter_id, r["exhibit_ref"]),
            )
            row = cur.fetchone()
            exhibit_pk = row[0] if row else None

        document_pk = None
        if r.get("document_ref"):
            cur.execute(
                "SELECT id FROM documents WHERE matter_id = %s AND doc_id = %s",
                (matter_id, r["document_ref"]),
            )
            row = cur.fetchone()
            document_pk = row[0] if row else None

        cur.execute(sql, (
            matter_id, r.get("severity") or "medium", r.get("status") or "open",
            r["title"], r.get("description"), exhibit_pk, document_pk,
            r.get("opm_ref"), r.get("created_on"), r.get("notes"),
        ))
    return len(rows)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--matter-ref", default="SOUTHPORT-001")
    p.add_argument("--database", default="southport_matter")
    p.add_argument("--csv-dir", default="db/templates",
                   help="directory containing exhibits.csv, documents.csv, issues.csv")
    args = p.parse_args()

    if "MYSQL_USER" not in os.environ or "MYSQL_PASSWORD" not in os.environ:
        sys.stderr.write("set MYSQL_USER and MYSQL_PASSWORD environment variables\n")
        return 2

    csv_dir = Path(args.csv_dir)
    exhibits_rows  = read_csv(csv_dir / "exhibits.csv")
    documents_rows = read_csv(csv_dir / "documents.csv")
    issues_rows    = read_csv(csv_dir / "issues.csv")

    conn = connect(args.database)
    try:
        with conn.cursor() as cur:
            matter_id = get_matter_id(cur, args.matter_ref)
            n_ex = load_exhibits(cur, matter_id, exhibits_rows)
            n_dc = load_documents(cur, matter_id, documents_rows)
            n_is = load_issues(cur, matter_id, issues_rows)
        conn.commit()
    finally:
        conn.close()

    print(f"loaded: exhibits={n_ex} documents={n_dc} issues={n_is} (matter {args.matter_ref})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
