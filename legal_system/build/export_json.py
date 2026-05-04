"""Export the entire case database to a single JSON file for portable use
(Excel imports, Notion, court-bundle indexers, downstream tools)."""
from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "legal_system" / "db" / "case.db"
OUT_PATH = ROOT / "legal_system" / "output" / "data.json"

TABLES = [
    "source_documents", "actors", "phases", "events", "evidence",
    "event_evidence", "event_actors",
    "charges", "charge_elements", "charge_failures", "charge_displacing_documents",
    "corrections", "quote_diffs",
    "statements", "statement_paragraphs", "statement_para_evidence",
    "iterations", "iteration_field_changes", "ware_schedule",
    "lockout_rows", "cross_refs", "validation_findings",
]


def main() -> int:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    out: dict = {}
    for t in TABLES:
        rows = [dict(r) for r in conn.execute(f"SELECT * FROM {t}")]
        out[t] = rows
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({sum(len(v) for v in out.values())} total rows)")
    conn.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
