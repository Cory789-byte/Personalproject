"""Local-folder ingester producing the same manifest format as gdrive_ingest.

Walks a local directory tree (e.g. an OneDrive-synced folder) and produces
the canonical `manifest.json` that `defence_analysis.py` consumes. This is
the on-PC counterpart to `gdrive_ingest.py` — same downstream pipeline,
different source.

No files are copied or moved. The manifest references the originals in
place. For evidence chain-of-custody, that is the correct behaviour.

Run:
    python scripts/local_ingest.py \
        --source "C:/Users/User/OneDrive/002 SIBLEY" \
        --dest   "C:/Evidence/CO-25-2722/screenshots/incoming"
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

HEADER = "MACHINE-GENERATED - UNVERIFIED"

INGESTABLE_EXTS = {
    ".pdf", ".docx", ".xlsx", ".xls", ".pptx", ".txt", ".rtf", ".md", ".csv",
    ".jpg", ".jpeg", ".png", ".tiff", ".tif", ".webp", ".heic", ".bmp", ".gif",
    ".mp4", ".mov", ".mkv", ".webm", ".wav", ".mp3", ".m4a", ".aac", ".ogg",
    ".json", ".xml", ".html", ".htm", ".eml", ".msg",
}

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".tiff", ".tif", ".webp", ".heic", ".bmp", ".gif"}


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


def _sha256_file(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


def walk(source: Path, images_only: bool = False) -> list[FileRecord]:
    records: list[FileRecord] = []
    allowed = IMAGE_EXTS if images_only else INGESTABLE_EXTS
    for p in sorted(source.rglob("*")):
        if not p.is_file():
            continue
        ext = p.suffix.lower()
        if ext not in allowed:
            continue
        try:
            stat = p.stat()
            sha = _sha256_file(p)
        except Exception as e:
            records.append(
                FileRecord(
                    drive_id="",
                    name=p.name,
                    mime_type="",
                    size=0,
                    sha256="",
                    md5_drive="",
                    modified_time="",
                    drive_path=str(p.relative_to(source)),
                    local_path=str(p),
                    warnings=[f"stat or hash failed: {e}"],
                )
            )
            continue
        mime = mimetypes.guess_type(str(p))[0] or "application/octet-stream"
        records.append(
            FileRecord(
                drive_id=sha[:24],
                name=p.name,
                mime_type=mime,
                size=stat.st_size,
                sha256=sha,
                md5_drive="",
                modified_time=time.strftime(
                    "%Y-%m-%dT%H:%M:%S", time.gmtime(stat.st_mtime)
                ),
                drive_path=str(p.relative_to(source)).replace("\\", "/"),
                local_path=str(p),
            )
        )
    return records


def write_manifest(records: list[FileRecord], dest_dir: Path, source: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    out = dest_dir / "manifest.json"
    payload = {
        "header": HEADER,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source_root": str(source),
        "file_count": len(records),
        "total_bytes": sum(r.size for r in records),
        "files": [asdict(r) for r in records],
    }
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ingest a local directory into a manifest the defence pipeline can consume."
    )
    parser.add_argument(
        "--source",
        required=True,
        help='Source directory (e.g. "C:/Users/User/OneDrive/002 SIBLEY")',
    )
    parser.add_argument(
        "--dest",
        required=True,
        help="Destination directory for manifest.json",
    )
    parser.add_argument(
        "--images-only",
        action="store_true",
        help="Only index image files (screenshots / photos). Useful for the screenshot workflow.",
    )
    args = parser.parse_args()

    source = Path(args.source).resolve()
    if not source.is_dir():
        raise SystemExit(f"--source is not a directory: {source}")
    dest = Path(args.dest).resolve()

    records = walk(source, images_only=args.images_only)
    manifest = write_manifest(records, dest, source)
    images = sum(1 for r in records if Path(r.local_path).suffix.lower() in IMAGE_EXTS)
    print(
        f"Indexed {len(records)} files ({images} images) under {source}\n"
        f"Manifest: {manifest}"
    )


if __name__ == "__main__":
    main()
