"""Command-line query tool for the case database.

Examples:
    python -m legal_system.build.search events --on 2025-02-24
    python -m legal_system.build.search events --phase phase-5
    python -m legal_system.build.search evidence --kind bwc
    python -m legal_system.build.search evidence --grep "Easthope"
    python -m legal_system.build.search ware --outstanding
    python -m legal_system.build.search corrections
    python -m legal_system.build.search paragraphs --status dispositive
    python -m legal_system.build.search quotes --bucket drift
    python -m legal_system.build.search forensic --field "stealing"
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path
from textwrap import shorten

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "legal_system" / "db" / "case.db"


def _connect():
    return sqlite3.connect(str(DB_PATH))


def cmd_events(args):
    sql = "SELECT id, event_date, event_time, description, phase_id FROM events WHERE 1=1"
    params: list = []
    if args.on:
        sql += " AND event_date = ?"
        params.append(args.on)
    if args.from_:
        sql += " AND event_date >= ?"
        params.append(args.from_)
    if args.to:
        sql += " AND event_date <= ?"
        params.append(args.to)
    if args.phase:
        sql += " AND phase_id = ?"
        params.append(args.phase)
    if args.grep:
        sql += " AND LOWER(description) LIKE ?"
        params.append(f"%{args.grep.lower()}%")
    sql += " ORDER BY event_date IS NULL, event_date, event_time, id"
    conn = _connect()
    rows = conn.execute(sql, params).fetchall()
    print(f"# {len(rows)} events")
    for r in rows:
        print(f"{r[0]:60s}  {r[1] or '':10s} {r[2] or '':5s}  [{r[4]}]  {shorten(r[3] or '', 100)}")


def cmd_evidence(args):
    sql = "SELECT id, ref, kind, text FROM evidence WHERE 1=1"
    params: list = []
    if args.kind:
        sql += " AND kind = ?"
        params.append(args.kind)
    if args.grep:
        sql += " AND (LOWER(ref) LIKE ? OR LOWER(text) LIKE ?)"
        params.extend([f"%{args.grep.lower()}%", f"%{args.grep.lower()}%"])
    sql += " ORDER BY ref"
    conn = _connect()
    rows = conn.execute(sql, params).fetchall()
    print(f"# {len(rows)} evidence anchors")
    for r in rows:
        print(f"{r[0]:60s}  {r[2]:14s}  {shorten(r[3] or '', 100)}")


def cmd_ware(args):
    sql = "SELECT id, part, description, current_status, days_out FROM ware_schedule WHERE 1=1"
    params: list = []
    if args.outstanding:
        sql += " AND current_status LIKE '%OUTSTANDING%'"
    sql += " ORDER BY part, id"
    conn = _connect()
    rows = conn.execute(sql, params).fetchall()
    print(f"# {len(rows)} Ware-schedule items")
    for r in rows:
        print(f"{r[0]:6s} {r[1]:2s} {r[3] or '':30s} {r[4] or '':>4}d  {shorten(r[2] or '', 100)}")


def cmd_corrections(args):
    conn = _connect()
    rows = conn.execute(
        "SELECT id, status, corrected_speaker, quote FROM corrections ORDER BY id"
    ).fetchall()
    print(f"# {len(rows)} corrections")
    for r in rows:
        print(f"{r[0]}  status={shorten(r[1] or '', 30)}  -> {r[2] or ''}  q='{shorten(r[3] or '', 70)}'")


def cmd_paragraphs(args):
    sql = "SELECT id, statement_id, para_label, status, verbatim FROM statement_paragraphs WHERE 1=1"
    params: list = []
    if args.status:
        sql += " AND status = ?"
        params.append(args.status)
    if args.grep:
        sql += " AND (LOWER(verbatim) LIKE ? OR LOWER(legal_effect) LIKE ?)"
        params.extend([f"%{args.grep.lower()}%", f"%{args.grep.lower()}%"])
    sql += " ORDER BY statement_id, ordinal"
    conn = _connect()
    rows = conn.execute(sql, params).fetchall()
    print(f"# {len(rows)} paragraphs")
    for r in rows:
        print(f"{r[0]:60s}  {r[3]:11s}  {r[1]}  {r[2]}  {shorten(r[4] or '', 80)}")


def cmd_quotes(args):
    sql = "SELECT id, bucket, ratio, source_doc_file, submission_text FROM quote_diffs WHERE 1=1"
    params: list = []
    if args.bucket:
        sql += " AND bucket = ?"
        params.append(args.bucket)
    if args.grep:
        sql += " AND (LOWER(submission_text) LIKE ? OR LOWER(largev3_text) LIKE ?)"
        params.extend([f"%{args.grep.lower()}%", f"%{args.grep.lower()}%"])
    sql += " ORDER BY bucket DESC, ratio"
    conn = _connect()
    rows = conn.execute(sql, params).fetchall()
    print(f"# {len(rows)} quote-diff rows")
    for r in rows:
        print(f"{r[1]:9s} {r[2] if r[2] is not None else '   ':>4}  {shorten(r[3] or '', 50)}  {shorten(r[4] or '', 80)}")


def cmd_forensic(args):
    sql = "SELECT ordinal, field, iter1_value, iter2_value, iter3_value, legal_significance FROM iteration_field_changes WHERE 1=1"
    params: list = []
    if args.field:
        sql += " AND (LOWER(field) LIKE ? OR LOWER(iter1_value) LIKE ? OR LOWER(iter3_value) LIKE ?)"
        params.extend([f"%{args.field.lower()}%"] * 3)
    sql += " ORDER BY ordinal"
    conn = _connect()
    rows = conn.execute(sql, params).fetchall()
    print(f"# {len(rows)} iteration-field-changes")
    for r in rows:
        print(f"#{r[0]:2}  {r[1][:35]:35s}  {shorten(r[5] or '', 100)}")


def cmd_actor(args):
    conn = _connect()
    rows = conn.execute(
        "SELECT id, display_name, role, reg_number, organisation FROM actors WHERE LOWER(display_name) LIKE ? OR id LIKE ?",
        (f"%{args.name.lower()}%", f"%{args.name.lower()}%"),
    ).fetchall()
    for aid, name, role, reg, org in rows:
        print(f"{aid:30s}  {name:40s}  {role or '':14s}  {reg or '':10s}  {org or ''}")
        for ev_row in conn.execute(
            "SELECT e.id, e.event_date, e.description FROM event_actors ea "
            "JOIN events e ON e.id=ea.event_id WHERE ea.actor_id=? "
            "ORDER BY e.event_date IS NULL, e.event_date LIMIT 30",
            (aid,),
        ):
            print(f"    {ev_row[1] or '':10s}  {shorten(ev_row[2] or '', 110)}")


def main(argv=None):
    p = argparse.ArgumentParser(description="Query the Shepherd v QPS case database")
    sub = p.add_subparsers(dest="cmd", required=True)

    pe = sub.add_parser("events"); pe.add_argument("--on"); pe.add_argument("--from", dest="from_"); pe.add_argument("--to"); pe.add_argument("--phase"); pe.add_argument("--grep")
    pe.set_defaults(func=cmd_events)

    pv = sub.add_parser("evidence"); pv.add_argument("--kind"); pv.add_argument("--grep")
    pv.set_defaults(func=cmd_evidence)

    pw = sub.add_parser("ware"); pw.add_argument("--outstanding", action="store_true")
    pw.set_defaults(func=cmd_ware)

    pc = sub.add_parser("corrections")
    pc.set_defaults(func=cmd_corrections)

    pp = sub.add_parser("paragraphs"); pp.add_argument("--status", choices=["agreed","disputed","partial","dispositive","info"]); pp.add_argument("--grep")
    pp.set_defaults(func=cmd_paragraphs)

    pq = sub.add_parser("quotes"); pq.add_argument("--bucket", choices=["exact","drift","no_match"]); pq.add_argument("--grep")
    pq.set_defaults(func=cmd_quotes)

    pf = sub.add_parser("forensic"); pf.add_argument("--field")
    pf.set_defaults(func=cmd_forensic)

    pa = sub.add_parser("actor"); pa.add_argument("name")
    pa.set_defaults(func=cmd_actor)

    args = p.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
