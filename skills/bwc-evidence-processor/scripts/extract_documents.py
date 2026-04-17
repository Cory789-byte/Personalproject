"""Extract plain text from PDF / DOCX / XLSX / TXT / RTF disclosure documents.

Produces:
- <stem>.doc.json     per-file record: path, type, extracted text, pages/sheets
- Updates a shared corpus.txt that other stages (contradictions) consume.

Gracefully degrades when optional deps are missing. For each format, prints
what is installed and what is not.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

HEADER = "MACHINE-GENERATED - UNVERIFIED"
SUPPORTED = {".pdf", ".docx", ".xlsx", ".xls", ".txt", ".rtf", ".md"}


@dataclass
class DocRecord:
    path: str
    stem: str
    kind: str
    sha256: str
    size: int
    text: str
    pages: int = 0
    sheets: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def sha256_file(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


def _read_txt(path: Path) -> tuple[str, list[str]]:
    try:
        return path.read_text(encoding="utf-8"), []
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1", errors="replace"), ["utf-8 decode failed; used latin-1"]


def _read_rtf(path: Path) -> tuple[str, list[str]]:
    try:
        from striprtf.striprtf import rtf_to_text  # type: ignore
        return rtf_to_text(path.read_text(encoding="utf-8", errors="replace")), []
    except Exception as e:
        return "", [f"striprtf unavailable: {e}"]


def _read_pdf(path: Path) -> tuple[str, int, list[str]]:
    warnings: list[str] = []
    # Try pdfminer.six first (best layout fidelity)
    try:
        from pdfminer.high_level import extract_text  # type: ignore
        text = extract_text(str(path)) or ""
        pages = text.count("\x0c") + (1 if text else 0)
        return text, pages, warnings
    except Exception as e:
        warnings.append(f"pdfminer failed: {e}")
    try:
        from pypdf import PdfReader  # type: ignore
        reader = PdfReader(str(path))
        parts = [p.extract_text() or "" for p in reader.pages]
        return "\n".join(parts), len(reader.pages), warnings
    except Exception as e:
        warnings.append(f"pypdf failed: {e}")
    return "", 0, warnings + ["no PDF backend available (pip install pdfminer.six or pypdf)"]


def _read_docx(path: Path) -> tuple[str, list[str]]:
    try:
        from docx import Document  # type: ignore
        d = Document(str(path))
        paras = [p.text for p in d.paragraphs]
        for tbl in d.tables:
            for row in tbl.rows:
                paras.append("\t".join(c.text for c in row.cells))
        return "\n".join(paras), []
    except Exception as e:
        return "", [f"python-docx failed: {e}"]


def _read_xlsx(path: Path) -> tuple[str, list[str], list[str]]:
    try:
        from openpyxl import load_workbook  # type: ignore
        wb = load_workbook(str(path), data_only=True, read_only=True)
        sheets = wb.sheetnames
        chunks: list[str] = []
        for name in sheets:
            ws = wb[name]
            chunks.append(f"### Sheet: {name}")
            for row in ws.iter_rows(values_only=True):
                cells = [str(c) if c is not None else "" for c in row]
                if any(cells):
                    chunks.append("\t".join(cells))
        return "\n".join(chunks), sheets, []
    except Exception as e:
        return "", [], [f"openpyxl failed: {e}"]


def extract_one(path: Path) -> DocRecord:
    path = Path(path).resolve()
    ext = path.suffix.lower()
    record = DocRecord(
        path=str(path),
        stem=path.stem,
        kind=ext.lstrip("."),
        sha256=sha256_file(path),
        size=path.stat().st_size,
        text="",
    )
    if ext in (".txt", ".md"):
        record.text, record.warnings = _read_txt(path)
    elif ext == ".rtf":
        record.text, record.warnings = _read_rtf(path)
    elif ext == ".pdf":
        record.text, record.pages, record.warnings = _read_pdf(path)
    elif ext == ".docx":
        record.text, record.warnings = _read_docx(path)
    elif ext in (".xlsx", ".xls"):
        record.text, record.sheets, record.warnings = _read_xlsx(path)
    else:
        record.warnings.append(f"unsupported extension: {ext}")
    return record


def save_record(record: DocRecord, dest_dir: Path) -> Path:
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    out = dest_dir / f"{record.stem}.doc.json"
    payload: dict[str, Any] = {"header": HEADER, **asdict(record)}
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    return out


def append_to_corpus(record: DocRecord, corpus_path: Path) -> None:
    corpus_path = Path(corpus_path)
    corpus_path.parent.mkdir(parents=True, exist_ok=True)
    with corpus_path.open("a", encoding="utf-8") as f:
        f.write(f"\n===== {record.path} ({record.kind}) =====\n")
        f.write(record.text)
        f.write("\n")


def process_directory(
    source: Path,
    dest_dir: Path,
    corpus_path: Path,
) -> list[DocRecord]:
    source = Path(source)
    dest_dir = Path(dest_dir)
    records: list[DocRecord] = []
    for p in sorted(source.rglob("*")):
        if p.is_file() and p.suffix.lower() in SUPPORTED:
            rec = extract_one(p)
            save_record(rec, dest_dir)
            append_to_corpus(rec, corpus_path)
            records.append(rec)
            print(f"  doc: {p.name} ({len(rec.text)} chars)")
    return records


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--corpus", required=True)
    args = parser.parse_args()
    recs = process_directory(
        Path(args.source), Path(args.output_dir), Path(args.corpus)
    )
    print(f"\n{len(recs)} documents processed.")
