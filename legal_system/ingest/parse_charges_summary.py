"""Parse CHARGES_SUMMARY.md into charges + elements + per-element failures."""
from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from .utils import (
    classify_evidence,
    extract_bullets,
    slugify,
    split_markdown_sections,
    strip_md_emphasis,
)

CHARGE_HEADING_RE = re.compile(r"^(\S+?)\s*—\s*(.+)$")


def parse(md_path: Path, source_doc_id: str, conn: sqlite3.Connection) -> dict:
    text = md_path.read_text(encoding="utf-8")
    sections = split_markdown_sections(text, level=2)
    cur = conn.cursor()
    counts = {"charges": 0, "elements": 0, "failures": 0, "displacing": 0}

    for heading, anchor, body in sections:
        if not heading:
            continue
        if heading.startswith("Quick reference") or heading.startswith("Cross-cutting") \
                or heading.startswith("Companion"):
            continue
        m = CHARGE_HEADING_RE.match(heading)
        if not m:
            continue
        matter_id = m.group(1).strip()
        title = m.group(2).strip()
        charge_id = "charge-" + slugify(matter_id)

        court = _extract_field(body, "**Court / forum:**")
        status = _extract_field(body, "**Current status:**")

        cur.execute(
            """INSERT OR REPLACE INTO charges
               (id, matter_id, title, court, status, alleged_summary, source_doc_id)
               VALUES (?,?,?,?,?,?,?)""",
            (charge_id, matter_id, title, court, status,
             _extract_section(body, "What QPS alleges"), source_doc_id),
        )
        counts["charges"] += 1

        # Elements
        elements_block = _extract_section(body, "Elements the prosecution must prove")
        for i, e in enumerate(_bullets_from(elements_block), start=1):
            elem_id = f"{charge_id}-el-{i}"
            cur.execute(
                "INSERT OR REPLACE INTO charge_elements (id, charge_id, ordinal, text) VALUES (?,?,?,?)",
                (elem_id, charge_id, i, e),
            )
            counts["elements"] += 1

        # Per-element failure subsections (level-4 bold paragraphs under "Why each element fails on the record")
        # In the source, each starts with **Element N fails — ...** followed by bullets.
        why_block = _extract_section(body, "Why each element fails on the record")
        for fail_heading, bullets in _iter_failure_blocks(why_block):
            element_ref = _ref_from_heading(fail_heading)
            failure_id = "fail-" + slugify(charge_id + "-" + fail_heading[:60])
            reason = strip_md_emphasis(fail_heading).strip()
            note_text = " | ".join(bullets) if bullets else None
            cur.execute(
                """INSERT OR REPLACE INTO charge_failures
                   (id, charge_id, element_ref, reason, notes) VALUES (?,?,?,?,?)""",
                (failure_id, charge_id, element_ref, reason, note_text),
            )
            counts["failures"] += 1

        # Displacing documents
        disp_block = _extract_section(body, "Displacing documents on the case file")
        for doc_text in _bullets_from(disp_block):
            cur.execute(
                """INSERT OR IGNORE INTO charge_displacing_documents (charge_id, ref, evidence_id)
                   VALUES (?,?,?)""",
                (charge_id, doc_text[:200], None),
            )
            counts["displacing"] += 1

    conn.commit()
    return counts


def _extract_field(body: str, marker: str) -> str:
    for ln in body.splitlines():
        if marker in ln:
            return ln.split(marker, 1)[1].strip().rstrip(".")
    return ""


def _extract_section(body: str, header_text: str) -> str:
    """Return the body after a level-3 heading containing header_text."""
    sections = split_markdown_sections(body, level=3)
    for heading, _, sub in sections:
        if heading and header_text.lower() in heading.lower():
            return sub
    return ""


def _bullets_from(block: str) -> list[str]:
    out = []
    for ln in block.splitlines():
        s = ln.strip()
        if s.startswith("- "):
            out.append(s[2:].strip())
    return out


def _iter_failure_blocks(why_block: str):
    """Yield (heading_text, [bullets]) for each '**Element N fails — ...**' block."""
    cur_heading = None
    cur_bullets: list[str] = []
    for ln in why_block.splitlines():
        s = ln.strip()
        if s.startswith("**") and s.endswith("**") and "fail" in s.lower():
            if cur_heading is not None:
                yield cur_heading, cur_bullets
            cur_heading = strip_md_emphasis(s)
            cur_bullets = []
        elif s.startswith("- ") and cur_heading is not None:
            cur_bullets.append(s[2:].strip())
    if cur_heading is not None:
        yield cur_heading, cur_bullets


def _ref_from_heading(heading: str) -> str:
    m = re.match(r"(Element\s+\d+|Procedural defects|.+?)\b", heading)
    return m.group(1) if m else heading[:30]
