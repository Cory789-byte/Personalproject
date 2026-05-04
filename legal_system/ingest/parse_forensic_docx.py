"""Parse the Shepherd v QPS Forensic Analysis .docx into iterations, field
changes, and Ware schedule rows. Falls back to the .txt extraction if
python-docx is unavailable.
"""
from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from .utils import slugify


def parse(docx_path: Path, source_doc_id: str, conn: sqlite3.Connection) -> dict:
    rows = _extract_tables(docx_path)
    if not rows:
        return {"iterations": 0, "field_changes": 0, "ware_rows": 0, "warning": "no_tables"}

    cur = conn.cursor()
    counts = {"iterations": 0, "field_changes": 0, "ware_rows": 0}

    # Table 0 — iteration metadata
    if 0 in rows:
        for i, row in enumerate(rows[0][1:], start=1):  # skip header
            if len(row) < 7:
                continue
            iter_id = f"iter-{i}"
            try:
                pages = int(re.search(r"\d+", row[5]).group())
            except (AttributeError, ValueError):
                pages = None
            cur.execute(
                """INSERT OR REPLACE INTO iterations
                   (id, ordinal, document, date_metadata, author, producer, pages, occasion)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (iter_id, i, row[1], row[2], row[3], row[4], pages, row[6]),
            )
            counts["iterations"] += 1

    # Table 1 — 30-field iteration field changes
    if 1 in rows:
        for row in rows[1][1:]:
            if len(row) < 10:
                continue
            try:
                ordinal = int(row[0])
            except ValueError:
                continue
            fc_id = f"fc-{ordinal:02d}"
            cur.execute(
                """INSERT OR REPLACE INTO iteration_field_changes
                   (id, ordinal, category, field, iter1_value, iter2_value, iter3_value,
                    who_changed, when_changed, contradicted_by, legal_significance)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                (fc_id, ordinal, row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                 row[8], row[9]),
            )
            counts["field_changes"] += 1

    # Tables 2 + 3 — Ware schedule Part A and Part B
    for ti, part in ((2, "A"), (3, "B")):
        if ti not in rows:
            continue
        for row in rows[ti][1:]:
            if len(row) < 8:
                continue
            ware_id = row[0].strip()
            if not ware_id or not re.match(r"^[AB]\d+$", ware_id):
                continue
            try:
                days_out = int(row[6])
            except (ValueError, IndexError):
                days_out = None
            cur.execute(
                """INSERT OR REPLACE INTO ware_schedule
                   (id, part, description, iter1_status, iter2_status, iter3_status,
                    current_status, days_out, legal_consequence)
                   VALUES (?,?,?,?,?,?,?,?,?)""",
                (ware_id, part, row[1], row[2], row[3], row[4], row[5], days_out, row[7]),
            )
            counts["ware_rows"] += 1

    conn.commit()
    return counts


def _extract_tables(docx_path: Path) -> dict[int, list[list[str]]]:
    try:
        from docx import Document
    except ImportError:
        return _extract_tables_from_txt(docx_path.with_suffix(".txt"))

    doc = Document(str(docx_path))
    tables: dict[int, list[list[str]]] = {}
    for ti, t in enumerate(doc.tables):
        out_rows = []
        for row in t.rows:
            cells = [c.text.strip() for c in row.cells]
            out_rows.append(cells)
        tables[ti] = out_rows
    return tables


def _extract_tables_from_txt(txt_path: Path) -> dict[int, list[list[str]]]:
    if not txt_path.exists():
        return {}
    text = txt_path.read_text(encoding="utf-8")
    if "=== TABLES ===" not in text:
        return {}
    section = text.split("=== TABLES ===", 1)[1]
    tables: dict[int, list[list[str]]] = {}
    cur_idx = -1
    cur_rows: list[list[str]] = []
    for ln in section.splitlines():
        m = re.match(r"^---\s*Table\s+(\d+)\s*---", ln.strip())
        if m:
            if cur_idx >= 0:
                tables[cur_idx] = cur_rows
            cur_idx = int(m.group(1))
            cur_rows = []
            continue
        if "|" in ln:
            cells = [c.strip() for c in ln.split("|")]
            cur_rows.append(cells)
    if cur_idx >= 0:
        tables[cur_idx] = cur_rows
    return tables
