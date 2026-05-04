"""Parse UNDERLYING_FACTS_REBUTTAL.md into statements + paragraphs + evidence."""
from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from .utils import (
    classify_evidence,
    extract_blockquote,
    extract_bullets,
    first_paragraph_after,
    slugify,
    split_markdown_sections,
    strip_md_emphasis,
)

PARA_HEADING_RE = re.compile(r"^(¶\S+(?:\s*[-–]\s*\S+)?(?:\s*\([^)]*\))?)\s*[—-]\s*(.+)$")
STATUS_EMOJI_MAP = {
    "✓": "agreed",
    "✘": "disputed",
    "⚠": "partial",
    "🎯": "dispositive",
}


def parse(md_path: Path, source_doc_id: str, conn: sqlite3.Connection) -> dict:
    text = md_path.read_text(encoding="utf-8")
    sections = split_markdown_sections(text, level=2)
    cur = conn.cursor()
    counts = {"statements": 0, "paragraphs": 0, "evidence": 0, "links": 0}

    for heading, anchor, body in sections:
        if not heading:
            continue
        if heading.lower().startswith("quick navigation") or heading.lower().startswith("companion"):
            continue
        if heading.lower().startswith("cumulative effect"):
            continue
        statement_id = "stmt-" + slugify(anchor or heading[:60])

        officer = _extract_kv(body, "**Officer taking statement:**")
        source_path = _extract_kv(body, "**Source file:**")
        taken_date = _extract_taken_date(heading)

        cur.execute(
            """INSERT OR REPLACE INTO statements
               (id, witness_id, taken_date, taking_officer_id, qprime_ref, source_path, source_doc_id)
               VALUES (?,?,?,?,?,?,?)""",
            (
                statement_id,
                None,
                taken_date,
                None,
                _extract_qprime(heading),
                source_path,
                source_doc_id,
            ),
        )
        counts["statements"] += 1

        # --- subsections (paragraphs) ---
        for sub_heading, _sub_anchor, sub_body in split_markdown_sections(body, level=3):
            if not sub_heading:
                continue
            para_id, para_label, status, status_emoji = _classify_paragraph_heading(sub_heading, statement_id)
            verbatim = extract_blockquote(sub_body)
            legal_effect = first_paragraph_after(sub_body, "**Legal effect")

            cur.execute(
                """INSERT OR REPLACE INTO statement_paragraphs
                   (id, statement_id, para_label, status, status_emoji, verbatim, legal_effect, ordinal)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (para_id, statement_id, para_label, status, status_emoji,
                 verbatim, legal_effect, counts["paragraphs"]),
            )
            counts["paragraphs"] += 1

            for marker in ("Displacing evidence", "Evidence anchors", "Anchor"):
                for a_text in extract_bullets(sub_body, marker):
                    ref = a_text.split(":", 1)[0].split(" — ", 1)[0][:80]
                    evid_id = "evid-" + slugify(ref + "-" + a_text[:40])
                    cur.execute(
                        "INSERT OR IGNORE INTO evidence (id, ref, text, kind) VALUES (?,?,?,?)",
                        (evid_id, ref, a_text, classify_evidence(a_text)),
                    )
                    counts["evidence"] += 1
                    cur.execute(
                        """INSERT OR IGNORE INTO statement_para_evidence
                           (paragraph_id, evidence_id, ref) VALUES (?,?,?)""",
                        (para_id, evid_id, a_text[:200]),
                    )
                    counts["links"] += 1

    conn.commit()
    return counts


def _classify_paragraph_heading(heading: str, statement_id: str):
    """Return (para_id, para_label, status, status_emoji)."""
    h = strip_md_emphasis(heading).strip()
    status_emoji = ""
    for emoji in STATUS_EMOJI_MAP:
        if emoji in h:
            status_emoji = emoji
            break
    status = STATUS_EMOJI_MAP.get(status_emoji, "info")
    m = PARA_HEADING_RE.match(h)
    if m:
        para_label = m.group(1).strip()
    else:
        para_label = h.split("—", 1)[0].strip() if "—" in h else h[:40]
    para_id = statement_id + "-p-" + slugify(para_label)
    return para_id, para_label, status, status_emoji


def _extract_kv(body: str, marker: str) -> str:
    for ln in body.splitlines():
        if marker in ln:
            after = ln.split(marker, 1)[1].strip()
            return strip_md_emphasis(after).strip(" `")
    return ""


def _extract_taken_date(heading: str) -> str | None:
    m = re.search(r"(\d{1,2}\s+\w+\s+\d{4})", heading)
    if not m:
        return None
    raw = m.group(1)
    try:
        from datetime import datetime
        return datetime.strptime(raw, "%d %B %Y").strftime("%Y-%m-%d")
    except ValueError:
        return None


def _extract_qprime(heading: str) -> str | None:
    m = re.search(r"(QP\d{6,12})", heading)
    return m.group(1) if m else None
