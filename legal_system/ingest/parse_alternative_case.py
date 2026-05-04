"""Parse ALTERNATIVE_CASE.md into phases + events + evidence anchors."""
from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from .utils import (
    IdMinter,
    classify_evidence,
    extract_bullets,
    extract_date,
    extract_time,
    slugify,
    split_markdown_sections,
    strip_md_emphasis,
)

PHASE_HEADING_RE = re.compile(r"^Phase\s+([\d.]+)\s*[—-]\s*(.*)$", re.IGNORECASE)
EVENT_DATE_HEADING_RE = re.compile(r"^[\d.\-:\s]")  # heading starts with digits = a date


def parse(md_path: Path, source_doc_id: str, conn: sqlite3.Connection) -> dict:
    text = md_path.read_text(encoding="utf-8")
    sections = split_markdown_sections(text, level=2)

    cur = conn.cursor()
    inserted = {"phases": 0, "events": 0, "evidence": 0, "links": 0}
    minter = IdMinter("ev")

    phase_ordinal = 0.0
    for heading, anchor, body in sections:
        if not heading:
            continue
        m = PHASE_HEADING_RE.match(heading.strip())
        if not m:
            continue

        phase_num_raw = m.group(1)
        try:
            ordinal = float(phase_num_raw)
        except ValueError:
            ordinal = phase_ordinal + 1
        phase_ordinal = ordinal

        phase_id = "phase-" + phase_num_raw.replace(".", "_")
        phase_title = heading.strip()
        # Phase summary is the italic _..._ leader paragraph at top of body
        summary = ""
        for ln in body.splitlines():
            s = ln.strip()
            if s.startswith("_") and s.endswith("_") and len(s) > 4:
                summary = strip_md_emphasis(s)
                break
            if s and not s.startswith("_"):
                break

        cur.execute(
            "INSERT OR REPLACE INTO phases (id, ordinal, title, summary, source_doc_id) VALUES (?,?,?,?,?)",
            (phase_id, ordinal, phase_title, summary, source_doc_id),
        )
        inserted["phases"] += 1

        # Each event inside the phase is a level-3 heading with a date label.
        for ev_heading, ev_body in _iter_event_subsections(body):
            if not ev_heading:
                continue
            date_label = ev_heading.strip()
            # First non-blank, non-italic line is the bold-titled event description
            description = _first_bold_line(ev_body) or _first_text_line(ev_body)
            if not description:
                continue
            ev_id = minter.mint(phase_id, date_label, description[:40])

            cur.execute(
                """INSERT OR REPLACE INTO events
                   (id, phase_id, event_date, event_time, date_label, description,
                    source_doc_id, source_anchor)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (
                    ev_id,
                    phase_id,
                    extract_date(date_label),
                    extract_time(date_label),
                    date_label,
                    description,
                    source_doc_id,
                    anchor,
                ),
            )
            inserted["events"] += 1

            # Evidence anchor bullets
            anchors = extract_bullets(ev_body, "Evidence anchors")
            for a_text in anchors:
                ref = _short_ref(a_text)
                ev_anchor_id = "evid-" + slugify(ref + "-" + a_text[:40])
                cur.execute(
                    """INSERT OR IGNORE INTO evidence (id, ref, text, kind)
                       VALUES (?,?,?,?)""",
                    (ev_anchor_id, ref, a_text, classify_evidence(a_text)),
                )
                inserted["evidence"] += 1
                cur.execute(
                    "INSERT OR IGNORE INTO event_evidence (event_id, evidence_id) VALUES (?,?)",
                    (ev_id, ev_anchor_id),
                )
                inserted["links"] += 1

    conn.commit()
    return inserted


def _iter_event_subsections(body: str):
    sections = split_markdown_sections(body, level=3)
    for heading, _, sub in sections:
        if heading:
            yield heading, sub


def _first_bold_line(body: str) -> str:
    for ln in body.splitlines():
        s = ln.strip()
        if s.startswith("**") and s.endswith("**") and len(s) > 4 and not s.endswith(":**"):
            return strip_md_emphasis(s)
    return ""


def _first_text_line(body: str) -> str:
    for ln in body.splitlines():
        s = ln.strip()
        if not s or s.startswith("_") or s.startswith("#"):
            continue
        return strip_md_emphasis(s)
    return ""


def _short_ref(bullet_text: str) -> str:
    """Pull the leading file/identifier-like token from an evidence bullet."""
    s = bullet_text.strip()
    # Tokens like 'Phillips QPS statement ¶3:' or 'Easthope BWC [02:00]:'
    head = s.split(":", 1)[0]
    head = head.split(" — ", 1)[0]
    head = head.split(" - ", 1)[0]
    return head[:80]
