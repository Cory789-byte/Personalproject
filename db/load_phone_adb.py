"""Index (and optionally pull) files from a USB-connected Samsung / Android
phone into the cloud_files table of the southport_matter MySQL database.

Why ADB instead of Samsung's cloud / Phone Link:
  - No third-party account needed.
  - Works for any Android phone, not just Samsung.
  - Gives access to /sdcard/* file trees that PC sync products either
    surface incompletely (Phone Link) or not at all (Samsung Cloud).
  - Suitable for legal-evidence preservation: pull originals, record
    sha256, retain mtime, leave the phone untouched.

One-time setup:
  Phone:  Settings -> About phone -> tap Build number 7 times to unlock
          Developer options -> Settings -> Developer options -> enable
          'USB debugging'. Plug into PC. Approve the "Always allow from
          this computer" prompt on the phone screen.
  PC:     Install Android Platform Tools so `adb` is on PATH.
            Windows: winget install Google.PlatformTools
            Mac:     brew install --cask android-platform-tools
            Linux:   apt-get install android-tools-adb

Usage:
  pip install -r db/requirements.txt
  set MYSQL_USER=root & set MYSQL_PASSWORD=...

  # Fast first pass: list + size + mtime, no file pull, no hashing:
  python db/load_phone_adb.py --matter-ref HOWDENS-SIBLEY-001

  # Custom path set:
  python db/load_phone_adb.py --paths /sdcard/DCIM /sdcard/Pictures/Screenshots

  # Pull files for preservation + hash; staging defaults to ./phone_staging:
  python db/load_phone_adb.py --pull --staging C:\\Evidence\\phone_pull

Re-runnable: rows upsert on (matter_id, provider='samsung_adb', relative_path).
Stale rows (files later deleted from the phone) are not removed automatically;
inspect with:
  SELECT relative_path, modified_on
    FROM cloud_files
   WHERE provider='samsung_adb' AND modified_on < NOW() - INTERVAL 30 DAY;
"""

from __future__ import annotations

import argparse
import hashlib
import os
import shlex
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pymysql

from _pc_user import pc_user

DEFAULT_PATHS = [
    "/sdcard/DCIM/Camera",
    "/sdcard/Pictures/Screenshots",
    "/sdcard/Download",
    "/sdcard/Documents",
    "/sdcard/Movies",
    "/sdcard/WhatsApp/Media",
]

HASH_CHUNK = 1024 * 1024


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


def adb(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    cmd = ["adb", *args]
    try:
        return subprocess.run(
            cmd, capture_output=True, text=True, check=check,
            encoding="utf-8", errors="replace",
        )
    except FileNotFoundError:
        raise SystemExit(
            "adb not found on PATH. Install Android Platform Tools:\n"
            "  Windows: winget install Google.PlatformTools\n"
            "  Mac:     brew install --cask android-platform-tools\n"
            "  Linux:   apt-get install android-tools-adb"
        )


def require_device(serial: str | None) -> str:
    """Confirm exactly one authorized device is present (or the one specified)."""
    result = adb("devices")
    lines = [ln.strip() for ln in result.stdout.splitlines() if ln.strip() and "List of devices" not in ln]
    devices = []
    for ln in lines:
        parts = ln.split("\t") if "\t" in ln else ln.split()
        if len(parts) >= 2 and parts[1] == "device":
            devices.append(parts[0])
        elif len(parts) >= 2 and parts[1] == "unauthorized":
            raise SystemExit(
                f"device {parts[0]} is unauthorized — accept the 'Always allow' "
                "prompt on the phone screen, then re-run."
            )
    if not devices:
        raise SystemExit("no authorized devices. Plug the phone in via USB and unlock it.")
    if serial:
        if serial not in devices:
            raise SystemExit(f"device {serial!r} not found. Connected: {devices}")
        return serial
    if len(devices) > 1:
        raise SystemExit(f"multiple devices connected — pass --serial. Connected: {devices}")
    return devices[0]


def list_remote(serial: str, path: str) -> list[tuple[str, int, int]]:
    """Return [(remote_path, size_bytes, mtime_epoch), ...] under path.

    Uses busybox/toybox find + stat. Skips paths that don't exist on the phone.
    """
    quoted = shlex.quote(path)
    cmd = (
        f"if [ -d {quoted} ]; then "
        f"find {quoted} -type f -exec stat -c '%s|%Y|%n' {{}} +; "
        f"fi"
    )
    result = adb("-s", serial, "shell", cmd, check=False)
    out: list[tuple[str, int, int]] = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if not line or "|" not in line:
            continue
        try:
            size_str, mtime_str, remote = line.split("|", 2)
            out.append((remote, int(size_str), int(mtime_str)))
        except ValueError:
            continue
    return out


def relative_for(remote: str) -> str:
    """Strip leading '/sdcard/' or '/storage/emulated/0/' so paths align across paths."""
    for prefix in ("/sdcard/", "/storage/emulated/0/"):
        if remote.startswith(prefix):
            return remote[len(prefix):]
    return remote.lstrip("/")


def pull_one(serial: str, remote: str, local: Path) -> bool:
    local.parent.mkdir(parents=True, exist_ok=True)
    result = adb("-s", serial, "pull", "-a", remote, str(local), check=False)
    return result.returncode == 0 and local.exists()


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(HASH_CHUNK), b""):
            h.update(chunk)
    return h.hexdigest()


def upsert(cur, matter_id: int, remote: str, size: int, mtime_epoch: int,
           sha: str | None, ingested_by: str) -> None:
    rel = relative_for(remote)
    cur.execute(
        """
        INSERT INTO cloud_files
          (matter_id, provider, relative_path, file_name, size_bytes,
           sha256, modified_on, ingested_by)
        VALUES (%s, 'samsung_adb', %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
          file_name   = VALUES(file_name),
          size_bytes  = VALUES(size_bytes),
          sha256      = COALESCE(VALUES(sha256), sha256),
          modified_on = VALUES(modified_on),
          ingested_by = VALUES(ingested_by)
        """,
        (
            matter_id, rel, Path(remote).name, size, sha,
            datetime.fromtimestamp(mtime_epoch), ingested_by,
        ),
    )


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--matter-ref", default="SOUTHPORT-001")
    p.add_argument("--database", default="southport_matter")
    p.add_argument("--paths", nargs="+", default=DEFAULT_PATHS,
                   help=f"remote paths to index (default: {DEFAULT_PATHS})")
    p.add_argument("--serial", default=None, help="adb device serial if multiple connected")
    p.add_argument("--pull", action="store_true",
                   help="adb-pull every file to --staging and compute sha256")
    p.add_argument("--staging", default="phone_staging",
                   help="local folder to receive pulled files (only with --pull)")
    p.add_argument("--max-pull-size", type=int, default=500 * 1024 * 1024,
                   help="skip pulling individual files larger than this (default 500MB)")
    args = p.parse_args()

    for var in ("MYSQL_USER", "MYSQL_PASSWORD"):
        if var not in os.environ:
            sys.stderr.write(f"set {var} environment variable\n")
            return 2

    serial = require_device(args.serial)
    user = pc_user()
    staging = Path(args.staging)

    conn = mysql_connect(args.database)
    seen = pulled = hashed = errors = 0
    try:
        with conn.cursor() as cur:
            matter_id = get_matter_id(cur, args.matter_ref)
            for remote_path in args.paths:
                entries = list_remote(serial, remote_path)
                for remote, size, mtime in entries:
                    sha = None
                    if args.pull and size <= args.max_pull_size:
                        local = staging / relative_for(remote)
                        if pull_one(serial, remote, local):
                            try:
                                sha = sha256_of(local)
                                hashed += 1
                            except OSError:
                                errors += 1
                            pulled += 1
                        else:
                            errors += 1
                    try:
                        upsert(cur, matter_id, remote, size, mtime, sha, user)
                        seen += 1
                    except Exception:
                        errors += 1
            conn.commit()
    finally:
        conn.close()

    print(
        f"adb device={serial} seen={seen} pulled={pulled} hashed={hashed} "
        f"errors={errors} (matter {args.matter_ref}, ingested_by {user})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
