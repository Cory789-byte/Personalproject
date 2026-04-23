"""Google Drive ingester for CO-25-2722 evidence pipeline.

Walks a Drive folder (or the whole "My Drive") and downloads every file that
the defence pipeline can read: PDFs, DOCX, XLSX, TXT, RTF, MD, images (JPG,
PNG, TIFF, WebP), and audio/video files already supported by the BWC
pipeline. Google-native formats (Docs, Sheets, Slides) are exported to
docx/xlsx/pptx.

Output layout:
    <dest>/
      manifest.json              # one row per file: drive_id, mime, sha256, size, local path, parents
      files/<drive_relative_path>   # mirrors the Drive folder hierarchy

The manifest is the canonical record — every downstream step should read
this, not the filesystem. SHA-256 is computed locally after download so the
hash can be compared against any later re-download.

OAuth setup (one-off, per machine):
    1. In Google Cloud Console, create a project and enable the Drive API.
    2. Create an OAuth client ID (Desktop app) and download the JSON as
       `credentials.json` next to this script (or pass --credentials).
    3. First run will open a browser to authorise; token is cached in
       `token.json` for subsequent runs.

This module is read-only on your Drive. It never modifies, moves, deletes,
or shares anything.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

HEADER = "MACHINE-GENERATED - UNVERIFIED"

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

GOOGLE_NATIVE_EXPORTS = {
    "application/vnd.google-apps.document": (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".docx",
    ),
    "application/vnd.google-apps.spreadsheet": (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ".xlsx",
    ),
    "application/vnd.google-apps.presentation": (
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ".pptx",
    ),
    "application/vnd.google-apps.drawing": ("application/pdf", ".pdf"),
}

DOWNLOADABLE_EXTS = {
    ".pdf", ".docx", ".xlsx", ".xls", ".pptx", ".txt", ".rtf", ".md", ".csv",
    ".jpg", ".jpeg", ".png", ".tiff", ".tif", ".webp", ".heic", ".bmp", ".gif",
    ".mp4", ".mov", ".mkv", ".webm", ".wav", ".mp3", ".m4a", ".aac", ".ogg",
    ".json", ".xml", ".html", ".htm", ".eml", ".msg",
}

FOLDER_MIME = "application/vnd.google-apps.folder"
SHORTCUT_MIME = "application/vnd.google-apps.shortcut"


@dataclass
class FileRecord:
    drive_id: str
    name: str
    mime_type: str
    size: int
    sha256: str
    md5_drive: str
    modified_time: str
    drive_path: str
    local_path: str
    parents: list[str] = field(default_factory=list)
    exported_as: str | None = None
    warnings: list[str] = field(default_factory=list)


def _load_service(credentials_path: Path, token_path: Path):
    try:
        from google.auth.transport.requests import Request  # type: ignore
        from google.oauth2.credentials import Credentials  # type: ignore
        from google_auth_oauthlib.flow import InstalledAppFlow  # type: ignore
        from googleapiclient.discovery import build  # type: ignore
    except ImportError as e:
        print(
            "Missing Google API libraries. Install with:\n"
            "    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib",
            file=sys.stderr,
        )
        raise SystemExit(1) from e

    creds = None
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not credentials_path.exists():
                raise SystemExit(
                    f"OAuth credentials not found at {credentials_path}. "
                    "Download the Desktop app OAuth client JSON from Google "
                    "Cloud Console and place it there (or pass --credentials)."
                )
            flow = InstalledAppFlow.from_client_secrets_file(
                str(credentials_path), SCOPES
            )
            creds = flow.run_local_server(port=0)
        token_path.write_text(creds.to_json(), encoding="utf-8")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def _sha256_file(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


def _safe_name(name: str) -> str:
    bad = '<>:"/\\|?*\x00'
    cleaned = "".join("_" if c in bad else c for c in name).strip().rstrip(".")
    return cleaned or "unnamed"


def _list_children(service, folder_id: str) -> list[dict[str, Any]]:
    children: list[dict[str, Any]] = []
    page_token: str | None = None
    fields = (
        "nextPageToken, files(id, name, mimeType, size, md5Checksum, "
        "modifiedTime, parents, shortcutDetails, trashed)"
    )
    while True:
        resp = (
            service.files()
            .list(
                q=f"'{folder_id}' in parents and trashed = false",
                pageSize=1000,
                fields=fields,
                pageToken=page_token,
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
            )
            .execute()
        )
        children.extend(resp.get("files", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return children


def _download_binary(service, file_id: str, dest: Path) -> None:
    from googleapiclient.http import MediaIoBaseDownload  # type: ignore

    req = service.files().get_media(fileId=file_id, supportsAllDrives=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("wb") as fh:
        downloader = MediaIoBaseDownload(fh, req, chunksize=4 * 1024 * 1024)
        done = False
        while not done:
            _status, done = downloader.next_chunk(num_retries=3)


def _export_native(service, file_id: str, export_mime: str, dest: Path) -> None:
    from googleapiclient.http import MediaIoBaseDownload  # type: ignore

    req = service.files().export_media(fileId=file_id, mimeType=export_mime)
    dest.parent.mkdir(parents=True, exist_ok=True)
    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, req, chunksize=4 * 1024 * 1024)
    done = False
    while not done:
        _status, done = downloader.next_chunk(num_retries=3)
    dest.write_bytes(buf.getvalue())


def _should_download(name: str, mime: str) -> bool:
    if mime in GOOGLE_NATIVE_EXPORTS:
        return True
    if mime.startswith("image/") or mime.startswith("video/") or mime.startswith("audio/"):
        return True
    ext = Path(name).suffix.lower()
    return ext in DOWNLOADABLE_EXTS


def _resolve_shortcut(service, item: dict[str, Any]) -> dict[str, Any] | None:
    target_id = (item.get("shortcutDetails") or {}).get("targetId")
    if not target_id:
        return None
    try:
        return (
            service.files()
            .get(
                fileId=target_id,
                fields="id, name, mimeType, size, md5Checksum, modifiedTime, parents, trashed",
                supportsAllDrives=True,
            )
            .execute()
        )
    except Exception:
        return None


def walk_and_download(
    service,
    root_id: str,
    dest_files: Path,
    drive_root_name: str = "",
) -> list[FileRecord]:
    records: list[FileRecord] = []
    stack: list[tuple[str, str]] = [(root_id, drive_root_name)]
    visited: set[str] = set()

    while stack:
        folder_id, rel = stack.pop()
        if folder_id in visited:
            continue
        visited.add(folder_id)

        try:
            children = _list_children(service, folder_id)
        except Exception as e:
            print(f"  ! list failed for folder {folder_id}: {e}", file=sys.stderr)
            continue

        for item in children:
            name = _safe_name(item["name"])
            mime = item["mimeType"]
            child_rel = f"{rel}/{name}" if rel else name

            if item.get("trashed"):
                continue

            if mime == SHORTCUT_MIME:
                target = _resolve_shortcut(service, item)
                if not target or target.get("trashed"):
                    continue
                item = {**target, "name": item["name"]}
                mime = target["mimeType"]

            if mime == FOLDER_MIME:
                stack.append((item["id"], child_rel))
                continue

            if not _should_download(item["name"], mime):
                continue

            warnings: list[str] = []
            exported_as: str | None = None

            if mime in GOOGLE_NATIVE_EXPORTS:
                export_mime, ext = GOOGLE_NATIVE_EXPORTS[mime]
                local = dest_files / f"{child_rel}{ext}"
                try:
                    _export_native(service, item["id"], export_mime, local)
                    exported_as = export_mime
                except Exception as e:
                    warnings.append(f"export failed: {e}")
                    continue
            else:
                local = dest_files / child_rel
                try:
                    _download_binary(service, item["id"], local)
                except Exception as e:
                    warnings.append(f"download failed: {e}")
                    continue

            try:
                size = local.stat().st_size
                sha = _sha256_file(local)
            except Exception as e:
                warnings.append(f"hash failed: {e}")
                size = 0
                sha = ""

            rec = FileRecord(
                drive_id=item["id"],
                name=item["name"],
                mime_type=mime,
                size=size,
                sha256=sha,
                md5_drive=item.get("md5Checksum", ""),
                modified_time=item.get("modifiedTime", ""),
                drive_path=child_rel,
                local_path=str(local),
                parents=item.get("parents", []),
                exported_as=exported_as,
                warnings=warnings,
            )
            records.append(rec)
            print(f"  + {child_rel} ({mime}, {size} bytes)")

    return records


def write_manifest(records: list[FileRecord], dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    out = dest_dir / "manifest.json"
    payload = {
        "header": HEADER,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "file_count": len(records),
        "total_bytes": sum(r.size for r in records),
        "files": [asdict(r) for r in records],
    }
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ingest a Google Drive folder into the defence pipeline."
    )
    parser.add_argument(
        "--dest",
        required=True,
        help="Destination directory (e.g. C:/Evidence/CO-25-2722/documents/incoming)",
    )
    parser.add_argument(
        "--folder-id",
        default="root",
        help="Drive folder ID to ingest (default: 'root' — entire My Drive)",
    )
    parser.add_argument(
        "--credentials",
        default=None,
        help="Path to Google OAuth client JSON (default: ./credentials.json)",
    )
    parser.add_argument(
        "--token",
        default=None,
        help="Path to cached OAuth token JSON (default: ./token.json)",
    )
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    credentials = Path(args.credentials) if args.credentials else here / "credentials.json"
    token = Path(args.token) if args.token else here / "token.json"
    dest = Path(args.dest).resolve()
    files_dir = dest / "files"
    files_dir.mkdir(parents=True, exist_ok=True)

    service = _load_service(credentials, token)
    print(f"Walking Drive folder {args.folder_id} into {dest}")
    records = walk_and_download(service, args.folder_id, files_dir)

    manifest = write_manifest(records, dest)
    print(f"\n{len(records)} files; manifest: {manifest}")


if __name__ == "__main__":
    main()
