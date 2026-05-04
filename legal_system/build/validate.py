"""Cross-document validation. Populates the validation_findings table with
internal-consistency issues across the 7 source documents.

Categories:
  - drift: Submission quotes drift > 0.65 from large-v3 (already in quote_diffs)
  - missing_anchor: events missing dates that we can probably extract
  - duplicate: same event/quote appearing in multiple sources w/ different wording
  - orphan: evidence anchors with no event link
  - date_inconsistency: events on the same day labelled differently across sources
  - cross_doc: quotes that appear differently in two sibling source docs

Run:
    python -m legal_system.build.validate
"""
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

DB_PATH = ROOT / "legal_system" / "db" / "case.db"


def _add(conn, severity, category, table, entity_id, msg, detail=None):
    conn.execute(
        """INSERT INTO validation_findings
           (severity, category, entity_table, entity_id, message, detail)
           VALUES (?,?,?,?,?,?)""",
        (severity, category, table, entity_id, msg, detail),
    )


def main() -> int:
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("DELETE FROM validation_findings")

    # ----- DRIFT -----
    n = 0
    for row in conn.execute(
        "SELECT id, ratio, source_doc_file, submission_text FROM quote_diffs WHERE bucket='drift'"
    ):
        _add(conn, "warning", "drift", "quote_diffs", row[0],
             f"Submission quote drift ratio={row[1]:.2f} in {row[2]}",
             row[3])
        n += 1
    print(f"drift findings: {n}")

    # ----- ORPHAN EVIDENCE -----
    n = 0
    for row in conn.execute(
        """SELECT e.id, e.ref FROM evidence e
           LEFT JOIN event_evidence ee ON ee.evidence_id = e.id
           LEFT JOIN statement_para_evidence spe ON spe.evidence_id = e.id
           WHERE ee.evidence_id IS NULL AND spe.evidence_id IS NULL"""
    ):
        _add(conn, "info", "orphan", "evidence", row[0],
             f"Evidence anchor not linked to any event or paragraph",
             row[1])
        n += 1
    print(f"orphan-evidence findings: {n}")

    # ----- EVENTS MISSING DATES -----
    n = 0
    for row in conn.execute(
        "SELECT id, date_label, description FROM events WHERE event_date IS NULL"
    ):
        _add(conn, "info", "missing_date", "events", row[0],
             f"Event has no parseable date",
             f"label='{row[1]}' desc='{(row[2] or '')[:80]}'")
        n += 1
    print(f"missing-date findings: {n}")

    # ----- WARE SCHEDULE OUTSTANDING ITEMS (legal-significance flag) -----
    n = 0
    for row in conn.execute(
        "SELECT id, description, current_status, days_out FROM ware_schedule "
        "WHERE current_status LIKE '%OUTSTANDING%'"
    ):
        _add(conn, "error", "outstanding_disclosure", "ware_schedule", row[0],
             f"Outstanding disclosure: {row[1]} ({row[3]} days)",
             row[2])
        n += 1
    print(f"outstanding-disclosure findings: {n}")

    # ----- ITERATION FIELD CHANGES MARKED AMENDMENT -----
    n = 0
    for row in conn.execute(
        "SELECT id, field, legal_significance FROM iteration_field_changes "
        "WHERE legal_significance LIKE '%amendment%' "
        "   OR legal_significance LIKE '%s 48%' "
        "   OR legal_significance LIKE '%s 590AB%'"
    ):
        _add(conn, "warning", "iteration_amendment", "iteration_field_changes", row[0],
             f"Iteration change with statutory significance: {row[1]}",
             row[2])
        n += 1
    print(f"iteration-amendment findings: {n}")

    # ----- CROSS-DOC QUOTE DRIFT BETWEEN ALTERNATIVE_CASE / LOCKOUT / CHARGES -----
    # The same Davies BWC quote appears in 3 sources. Check that the ts/quote
    # tokens line up.
    n = _check_davies_consistency(conn)
    print(f"cross-doc Davies-quote findings: {n}")

    # ----- CORRECTIONS POINTING AT QUOTES STILL IN SUBMISSION -----
    n = _check_corrections_against_submission(conn)
    print(f"corrections-vs-submission findings: {n}")

    # ----- DUPLICATE EVENTS BY (date, description-prefix) -----
    n = _check_duplicate_events(conn)
    print(f"duplicate-event findings: {n}")

    conn.commit()
    total = conn.execute("SELECT COUNT(*) FROM validation_findings").fetchone()[0]
    print(f"\nTotal findings written: {total}")
    conn.close()
    return 0


def _check_davies_consistency(conn) -> int:
    """The 'we have to defer / we don't reinvestigate' Davies quote should
    appear in CHARGES_SUMMARY (cross-cutting), ALTERNATIVE_CASE Phase 5 verbatim,
    and LOCKOUT_NIGHT row 13 with consistent wording.
    """
    canonical = "we have to defer to the judgment of our other police"
    n = 0
    # Fetch every text field that should contain it
    fields = [
        ("events", "id", "description"),
        ("statement_paragraphs", "id", "verbatim"),
        ("charge_failures", "id", "notes"),
    ]
    hits = []
    for tbl, idcol, txtcol in fields:
        for row in conn.execute(f"SELECT {idcol}, {txtcol} FROM {tbl} WHERE LOWER({txtcol}) LIKE ?",
                                (f"%defer to the judgment%",)):
            hits.append((tbl, row[0], (row[1] or "")[:200]))
    if len(hits) >= 2:
        _add(conn, "info", "cross_doc_quote", "events", "davies-defer-quote",
             f"Canonical 'defer to other police' quote found in {len(hits)} places — verify wording matches",
             " | ".join(f"{t}:{i}::{x}" for t, i, x in hits[:6]))
        n += 1
    return n


def _check_corrections_against_submission(conn) -> int:
    """If a CORRECTION_REGISTER entry's quote (e.g. 'I think he's in your room now')
    appears in the SUBMISSION_QUOTE_DIFF without correction in the body, surface
    it for hand review.
    """
    n = 0
    for row in conn.execute("SELECT id, quote, corrected_speaker, status FROM corrections"):
        cor_id, quote, corrected, status = row
        if not quote:
            continue
        # Find any submission-text references to the same quote
        for q_row in conn.execute(
            "SELECT id, submission_text, source_doc_file FROM quote_diffs WHERE submission_text LIKE ?",
            (f"%{quote[:40]}%",),
        ):
            _add(conn, "warning", "correction_in_submission",
                 "corrections", cor_id,
                 f"Correction {cor_id} ({status}) — quote still appears in submission ({q_row[2]})",
                 f"submission: {q_row[1][:160]}")
            n += 1
            break
    return n


def _check_duplicate_events(conn) -> int:
    """Flag events with the same date + a 30-char prefix overlap from different
    source docs (likely the same incident captured twice; not necessarily wrong,
    but worth confirming the wording matches)."""
    rows = conn.execute(
        "SELECT id, event_date, description, source_doc_id FROM events WHERE event_date IS NOT NULL"
    ).fetchall()
    by_key: dict[tuple[str, str], list[tuple[str, str]]] = {}
    for ev_id, date, desc, src in rows:
        if not desc:
            continue
        key = (date, desc[:30].lower())
        by_key.setdefault(key, []).append((ev_id, src))
    n = 0
    for (date, prefix), entries in by_key.items():
        if len(entries) < 2:
            continue
        _add(conn, "info", "duplicate_event", "events", entries[0][0],
             f"{len(entries)} events on {date} share a 30-char prefix",
             " | ".join(f"{src}:{eid}" for eid, src in entries))
        n += 1
    return n


if __name__ == "__main__":
    raise SystemExit(main())
