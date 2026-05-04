"""Parse SUBMISSION_QUOTE_DIFF.md into the quote_diffs table."""
from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from .utils import IdMinter

DRIFT_HEADING_RE = re.compile(
    r"^From\s+([^\s]+\.docx)\s*\(ratio=([\d.]+)\)\s*$"
)
EXACT_LINE_RE = re.compile(
    r"^- _(.+?\.docx)_\s+matches\s+`([^`]+)`\s+\(ratio=([\d.]+)\):\s*(.+)$"
)
NO_MATCH_LINE_RE = re.compile(r"^- _(.+?\.docx)_:\s*(.+)$")


def parse(md_path: Path, source_doc_id: str, conn: sqlite3.Connection) -> dict:
    text = md_path.read_text(encoding="utf-8")
    cur = conn.cursor()
    minter = IdMinter("qd")
    counts = {"exact": 0, "drift": 0, "no_match": 0}

    # ----- DRIFT -----
    drift_section = _section_between(text, "## Drift", "## No match")
    cur_doc = None
    cur_ratio = None
    state = None
    sub_buf: list[str] = []
    largev3_file = None
    largev3_buf: list[str] = []

    def flush_drift():
        nonlocal sub_buf, largev3_buf, cur_doc, cur_ratio, largev3_file, state
        if cur_doc and sub_buf:
            qd_id = minter.mint("drift", cur_doc, str(cur_ratio))
            cur.execute(
                """INSERT OR REPLACE INTO quote_diffs
                   (id, bucket, ratio, source_doc_file, submission_text,
                    largev3_file, largev3_text, source_doc_id)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (qd_id, "drift", cur_ratio, cur_doc,
                 " ".join(sub_buf).strip(),
                 largev3_file,
                 " ".join(largev3_buf).strip() or None,
                 source_doc_id),
            )
            counts["drift"] += 1
        sub_buf = []
        largev3_buf = []
        largev3_file = None

    for ln in drift_section.splitlines():
        s = ln.rstrip()
        m = DRIFT_HEADING_RE.match(s.strip().lstrip("#").strip()) if s.strip().startswith("###") else None
        if m:
            flush_drift()
            cur_doc = m.group(1)
            cur_ratio = float(m.group(2))
            state = None
            continue
        if s.strip().startswith("**Submission text:**"):
            state = "sub"
            continue
        if s.strip().startswith("**Closest large-v3 in"):
            mm = re.search(r"`([^`]+)`", s)
            largev3_file = mm.group(1) if mm else None
            state = "lv3"
            continue
        if state == "sub":
            if s.strip().startswith(">"):
                sub_buf.append(s.strip().lstrip(">").strip())
        elif state == "lv3":
            if s.strip().startswith(">"):
                largev3_buf.append(s.strip().lstrip(">").strip())
    flush_drift()

    # ----- NO MATCH -----
    nm_section = _section_between(text, "## No match", "## Exact matches")
    for ln in nm_section.splitlines():
        s = ln.strip()
        m = NO_MATCH_LINE_RE.match(s)
        if not m:
            continue
        doc = m.group(1)
        snippet = m.group(2)
        qd_id = minter.mint("nomatch", doc, snippet[:30])
        cur.execute(
            """INSERT OR REPLACE INTO quote_diffs
               (id, bucket, ratio, source_doc_file, submission_text,
                largev3_file, largev3_text, source_doc_id)
               VALUES (?,?,?,?,?,?,?,?)""",
            (qd_id, "no_match", None, doc, snippet, None, None, source_doc_id),
        )
        counts["no_match"] += 1

    # ----- EXACT MATCHES -----
    em_section = text.split("## Exact matches", 1)[-1]
    for ln in em_section.splitlines():
        m = EXACT_LINE_RE.match(ln.strip())
        if not m:
            continue
        doc = m.group(1)
        target_file = m.group(2)
        ratio = float(m.group(3))
        text_quote = m.group(4)
        qd_id = minter.mint("exact", doc, text_quote[:30])
        cur.execute(
            """INSERT OR REPLACE INTO quote_diffs
               (id, bucket, ratio, source_doc_file, submission_text,
                largev3_file, largev3_text, source_doc_id)
               VALUES (?,?,?,?,?,?,?,?)""",
            (qd_id, "exact", ratio, doc, text_quote, target_file, text_quote, source_doc_id),
        )
        counts["exact"] += 1

    conn.commit()
    return counts


def _section_between(text: str, start_marker: str, end_marker: str) -> str:
    if start_marker not in text:
        return ""
    after = text.split(start_marker, 1)[1]
    if end_marker in after:
        return after.split(end_marker, 1)[0]
    return after
