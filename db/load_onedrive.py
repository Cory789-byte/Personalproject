"""Mirror a synced OneDrive (or SharePoint / Google Drive / Dropbox / local)
folder into the cloud_files table of the southport_matter MySQL database.

Why local-folder rather than the Microsoft Graph API: OneDrive on Windows
already syncs the matter folder to disk. Walking that folder is one tenth the
code, needs no OAuth setup, and gives the same outcome — a row per file with
size, mtime, and sha256.

Usage:
    pip install -r db/requirements.txt
    set MYSQL_USER=root
    set MYSQL_PASSWORD=your_mysql_password
    set ONEDRIVE_ROOT=C:\\Users\\you\\OneDrive\\Southport

    python db/load_onedrive.py
    python db/load_onedrive.py --provider sharepoint --root "C:\\Users\\you\\SharePoint - Firm\\Southport"
    python db/load_onedrive.py --no-hash   # skip sha256 for a fast first pass

Re-running is safe: rows are upserted on (matter_id, provider, relative_path).
Files that have disappeared from the folder are *not* deleted from the DB —
inspect with `SELECT * FROM cloud_files WHERE modified_on < NOW() - INTERVAL 30 DAY;`
to find stale rows.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
from datetime import datetime
from pathlib import Path

import pymysql

SKIP_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
SKIP_SUFFIXES = (".tmp", ".swp", ".part", ".crdownload")
HASH_CHUNK = 1024 * 1024  # 1 MiB


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


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(HASH_CHUNK), b""):
            h.update(chunk)
    return h.hexdigest()


def should_skip(name: str) -> bool:
    if name in SKIP_NAMES or name.startswith("."):
        return True
    return name.endswith(SKIP_SUFFIXES)


def walk(root: Path, max_size: int | None):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for name in filenames:
            if should_skip(name):
                continue
            p = Path(dirpath) / name
            try:
                st = p.stat()
            except OSError:
                continue
            if max_size is not None and st.st_size > max_size:
                yield p, st, True   # too large — skip hash
            else:
                yield p, st, False


def upsert(cur, matter_id: int, provider: str, root: Path, path: Path,
           st: os.stat_result, do_hash: bool, skipped_hash: bool) -> None:
    rel = path.relative_to(root).as_posix()
    sha = None
    if do_hash and not skipped_hash:
        sha = sha256_of(path)
    cur.execute(
        """
        INSERT INTO cloud_files
          (matter_id, provider, relative_path, file_name, size_bytes,
           sha256, modified_on)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
          file_name   = VALUES(file_name),
          size_bytes  = VALUES(size_bytes),
          sha256      = COALESCE(VALUES(sha256), sha256),
          modified_on = VALUES(modified_on)
        """,
        (
            matter_id, provider, rel, path.name, st.st_size,
            sha, datetime.fromtimestamp(st.st_mtime),
        ),
    )


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--matter-ref", default="SOUTHPORT-001")
    p.add_argument("--database", default="southport_matter")
    p.add_argument("--provider", default="onedrive",
                   choices=["onedrive", "sharepoint", "gdrive", "dropbox", "local"])
    p.add_argument("--root", default=os.environ.get("ONEDRIVE_ROOT"),
                   help="absolute path to the synced folder (or set ONEDRIVE_ROOT env)")
    p.add_argument("--no-hash", action="store_true", help="skip sha256 (fast first pass)")
    p.add_argument("--max-hash-size", type=int, default=500 * 1024 * 1024,
                   help="skip hashing files larger than this many bytes (default 500MB)")
    args = p.parse_args()

    if not args.root:
        sys.stderr.write("--root not given and ONEDRIVE_ROOT not set\n")
        return 2
    root = Path(args.root)
    if not root.is_dir():
        sys.stderr.write(f"root is not a directory: {root}\n")
        return 2

    for var in ("MYSQL_USER", "MYSQL_PASSWORD"):
        if var not in os.environ:
            sys.stderr.write(f"set {var} environment variable\n")
            return 2

    conn = mysql_connect(args.database)
    seen = hashed = 0
    try:
        with conn.cursor() as cur:
            matter_id = get_matter_id(cur, args.matter_ref)
            for path, st, too_big in walk(root, args.max_hash_size):
                upsert(
                    cur, matter_id, args.provider, root, path, st,
                    do_hash=not args.no_hash,
                    skipped_hash=too_big,
                )
                seen += 1
                if not args.no_hash and not too_big:
                    hashed += 1
        conn.commit()
    finally:
        conn.close()

    print(f"cloud files seen={seen} hashed={hashed} (matter {args.matter_ref}, "
          f"provider {args.provider}, root {root})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
