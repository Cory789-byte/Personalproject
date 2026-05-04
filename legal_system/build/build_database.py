"""Build legal_system/db/case.db from the 7 source documents.

Usage:
    python -m legal_system.build.build_database
"""
from __future__ import annotations

import os
import sqlite3
import sys
from pathlib import Path

# Make the package importable when run as a script
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from legal_system.ingest import (  # noqa: E402
    parse_alternative_case,
    parse_charges_summary,
    parse_correction_register,
    parse_forensic_docx,
    parse_lockout_timeline,
    parse_quote_diff,
    parse_underlying_facts,
    seed_actors,
)
from legal_system.ingest.utils import file_sha256, now_iso  # noqa: E402

REPO = ROOT
SRC = REPO / "source_documents"
DB_DIR = REPO / "legal_system" / "db"
DB_PATH = DB_DIR / "case.db"
SCHEMA_PATH = DB_DIR / "schema.sql"

SOURCE_DOCS = [
    {
        "id": "alternative_case",
        "filename": "ALTERNATIVE_CASE.md",
        "title": "Alternative Case (10 phases — affirmative chronology)",
    },
    {
        "id": "charges_summary",
        "filename": "CHARGES_SUMMARY.md",
        "title": "Charges Summary (per-charge element-by-element rebuttal)",
    },
    {
        "id": "correction_register",
        "filename": "CORRECTION_REGISTER.md",
        "title": "Speaker Mis-Attribution Correction Register",
    },
    {
        "id": "lockout_timeline",
        "filename": "LOCKOUT_NIGHT_TIMELINE_CARD.md",
        "title": "Lockout-Night Timeline Card (14-row exhibit)",
    },
    {
        "id": "quote_diff",
        "filename": "SUBMISSION_QUOTE_DIFF.md",
        "title": "Submission Quote Diff (large-v3 vs Submission text)",
    },
    {
        "id": "underlying_facts",
        "filename": "UNDERLYING_FACTS_REBUTTAL.md",
        "title": "Underlying Facts Rebuttal (paragraph-by-paragraph)",
    },
    {
        "id": "forensic_analysis",
        "filename": "Shepherd_v_QPS_Forensic_Analysis_4May2026.docx",
        "title": "Forensic Analysis — Three Iterations + Ware Schedule",
    },
]


def main() -> int:
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys = ON")
    with open(SCHEMA_PATH, "r") as f:
        conn.executescript(f.read())

    # Register source documents
    cur = conn.cursor()
    for sd in SOURCE_DOCS:
        path = SRC / sd["filename"]
        sha = file_sha256(path) if path.exists() else ""
        size = path.stat().st_size if path.exists() else 0
        cur.execute(
            """INSERT INTO source_documents
               (id, filename, title, generated_at, ingested_at, sha256, bytes, notes)
               VALUES (?,?,?,?,?,?,?,?)""",
            (sd["id"], sd["filename"], sd["title"], None, now_iso(), sha, size, None),
        )
    conn.commit()

    # Seed actors first — parsers may want to reference them later
    n_actors = seed_actors.seed(conn)
    print(f"actors seeded: {n_actors}")

    # Run parsers
    print("--- ALTERNATIVE_CASE ---")
    print(parse_alternative_case.parse(SRC / "ALTERNATIVE_CASE.md", "alternative_case", conn))
    print("--- CHARGES_SUMMARY ---")
    print(parse_charges_summary.parse(SRC / "CHARGES_SUMMARY.md", "charges_summary", conn))
    print("--- CORRECTION_REGISTER ---")
    print(parse_correction_register.parse(SRC / "CORRECTION_REGISTER.md", "correction_register", conn))
    print("--- LOCKOUT_NIGHT_TIMELINE ---")
    print(parse_lockout_timeline.parse(SRC / "LOCKOUT_NIGHT_TIMELINE_CARD.md", "lockout_timeline", conn))
    print("--- SUBMISSION_QUOTE_DIFF ---")
    print(parse_quote_diff.parse(SRC / "SUBMISSION_QUOTE_DIFF.md", "quote_diff", conn))
    print("--- UNDERLYING_FACTS_REBUTTAL ---")
    print(parse_underlying_facts.parse(SRC / "UNDERLYING_FACTS_REBUTTAL.md", "underlying_facts", conn))
    print("--- FORENSIC_ANALYSIS ---")
    print(parse_forensic_docx.parse(SRC / "Shepherd_v_QPS_Forensic_Analysis_4May2026.docx", "forensic_analysis", conn))

    # Auto-link actors mentioned in event descriptions or evidence text
    print("--- Linking actors ---")
    n_actor_links = _link_actors_to_events(conn)
    print({"event_actor_links": n_actor_links})

    conn.close()
    print(f"\nDB written to: {DB_PATH}")
    return 0


def _link_actors_to_events(conn: sqlite3.Connection) -> int:
    """Loose substring-matching of actor display_name into event descriptions.

    Conservative: only links if a 'good' identifier appears (surname, reg
    number, or strong unique slug-component).
    """
    cur = conn.cursor()
    cur.execute("SELECT id, display_name FROM actors")
    actors = cur.fetchall()
    cur.execute("SELECT id, description FROM events WHERE description IS NOT NULL")
    events = cur.fetchall()
    n = 0
    for ev_id, desc in events:
        d_lower = desc.lower()
        for a_id, name in actors:
            # Use the most distinctive token (last word, often surname)
            distinctive = name.split()[-1].lower()
            if len(distinctive) < 4:
                continue
            if distinctive in d_lower:
                cur.execute(
                    "INSERT OR IGNORE INTO event_actors (event_id, actor_id, role_in_event) VALUES (?,?,?)",
                    (ev_id, a_id, None),
                )
                n += 1
    conn.commit()
    return n


if __name__ == "__main__":
    raise SystemExit(main())
