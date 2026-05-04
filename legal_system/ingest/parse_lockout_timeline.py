"""Parse LOCKOUT_NIGHT_TIMELINE_CARD.md into lockout_rows + events."""
from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from .utils import (
    classify_evidence,
    extract_bullets,
    extract_date,
    extract_time,
    slugify,
    split_markdown_sections,
    strip_md_emphasis,
)

ROW_HEADING_RE = re.compile(r"^Row\s+(\d+)\s*—\s*(.+?)\s*—\s*(.+)$")


def parse(md_path: Path, source_doc_id: str, conn: sqlite3.Connection) -> dict:
    text = md_path.read_text(encoding="utf-8")
    sections = split_markdown_sections(text, level=3)
    cur = conn.cursor()
    counts = {"rows": 0, "events": 0, "evidence": 0, "links": 0}

    for heading, _, body in sections:
        if not heading:
            continue
        m = ROW_HEADING_RE.match(heading.strip())
        if not m:
            continue
        row_no = int(m.group(1))
        time_label = m.group(2).strip()
        actor = m.group(3).strip()

        # Description from "**Event.** ..." line
        description = _extract_event_paragraph(body)
        defeats = _extract_event_paragraph(body, marker="**What this row defeats:**")

        ev_id = f"lockout-row-{row_no:02d}"
        # Insert into events too (for the master timeline)
        cur.execute(
            """INSERT OR REPLACE INTO events
               (id, phase_id, event_date, event_time, date_label, description,
                source_doc_id, source_anchor, defeats)
               VALUES (?,?,?,?,?,?,?,?,?)""",
            (
                ev_id,
                "phase-5",  # Lockout night = Phase 5 in the alternative case
                extract_date(time_label),
                extract_time(time_label),
                f"{time_label} ({actor})",
                description,
                source_doc_id,
                None,
                defeats,
            ),
        )
        counts["events"] += 1

        # Lockout row table
        cur.execute(
            """INSERT OR REPLACE INTO lockout_rows
               (row_no, event_id, time_label, actor, event_text, defeats)
               VALUES (?,?,?,?,?,?)""",
            (row_no, ev_id, time_label, actor, description, defeats),
        )
        counts["rows"] += 1

        # Evidence anchors
        for a_text in extract_bullets(body, "Evidence anchors"):
            ref = a_text.split(":", 1)[0].split(" — ", 1)[0][:80]
            evid_id = "evid-" + slugify(ref + "-" + a_text[:40])
            cur.execute(
                "INSERT OR IGNORE INTO evidence (id, ref, text, kind) VALUES (?,?,?,?)",
                (evid_id, ref, a_text, classify_evidence(a_text)),
            )
            counts["evidence"] += 1
            cur.execute(
                "INSERT OR IGNORE INTO event_evidence (event_id, evidence_id) VALUES (?,?)",
                (ev_id, evid_id),
            )
            counts["links"] += 1

    conn.commit()
    return counts


def _extract_event_paragraph(body: str, marker: str = "**Event.**") -> str:
    """Return paragraph text following a bold marker like '**Event.**' or '**What this row defeats:**'."""
    out: list[str] = []
    capture = False
    for ln in body.splitlines():
        s = ln.strip()
        if s.startswith(marker):
            after = s.split(marker, 1)[1].strip()
            if after:
                out.append(after)
            capture = True
            continue
        if capture:
            if not s:
                if out:
                    break
                continue
            if s.startswith("**") and s.endswith(":**"):
                break
            out.append(s)
    return strip_md_emphasis(" ".join(out)).strip()
