"""Parse CORRECTION_REGISTER.md into the corrections table."""
from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from .utils import (
    extract_blockquote,
    slugify,
    split_markdown_sections,
    strip_md_emphasis,
)

ID_RE = re.compile(r"^(C-\d+)\s*[—-]\s*(.+)$")
FIELD_RE = re.compile(r"\*\*([A-Z][A-Za-z ]+):\*\*\s*(.+?)$")


def parse(md_path: Path, source_doc_id: str, conn: sqlite3.Connection) -> dict:
    text = md_path.read_text(encoding="utf-8")
    sections = split_markdown_sections(text, level=3)
    cur = conn.cursor()
    n = 0
    for heading, _anchor, body in sections:
        if not heading:
            continue
        m = ID_RE.match(heading.strip())
        if not m:
            continue
        cor_id = m.group(1)
        status = m.group(2).strip()
        quote = extract_blockquote(body)
        original = _field(body, "Original attribution")
        corrected = _field(body, "Corrected attribution")
        anchor = _field(body, "Anchor")
        category = _field(body, "Category")
        legal_effect = _field(body, "Legal effect")

        cur.execute(
            """INSERT OR REPLACE INTO corrections
               (id, status, quote, original_speaker, corrected_speaker, anchor,
                category, legal_effect, source_doc_id)
               VALUES (?,?,?,?,?,?,?,?,?)""",
            (cor_id, status, quote, original, corrected, anchor,
             category, legal_effect, source_doc_id),
        )
        n += 1

    conn.commit()
    return {"corrections": n}


def _field(body: str, name: str) -> str:
    """Return text of '**<name>:** ...' field; supports multi-line continuation."""
    out_parts: list[str] = []
    capture = False
    for ln in body.splitlines():
        s = ln.strip()
        if s.startswith(f"**{name}:**"):
            payload = s.split(f"**{name}:**", 1)[1].strip()
            if payload:
                out_parts.append(payload)
            capture = True
            continue
        if capture:
            if not s:
                if out_parts:
                    break
                else:
                    continue
            if s.startswith("**") and s.endswith(":**"):
                break
            if s.startswith("- "):
                # bullet under this field
                out_parts.append(s[2:].strip())
                continue
            if s.startswith("**"):
                # Different bold field follows, even if not strictly a label form
                break
            out_parts.append(s)
    return strip_md_emphasis(" ".join(out_parts).strip())
