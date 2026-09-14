#!/usr/bin/env python3
"""Communication-signal ledger for WC/2024/227 — Regulator and MSH.

Usage:
  comms_signals.py report              latency / register / formula / open-items summary
  comms_signals.py add ...             append a row (see --help)
  comms_signals.py score               list predictions still unscored in PREDICTIONS-*.md
  comms_signals.py register TEXTFILE   classify a letter's register from its text

The ledger is index/COMMS_SIGNAL_LEDGER.tsv. Columns:
  id date time_aest dir party track doc kind answers latency_days register formula
  consequence author_field source note
Register classes (skill/references/REGULATOR-SIGNALS-the-full-data-set.md, class 2):
  operational  first person, apologetic, informal ("I apologise", "could I please")
  position     institutional third person + the fixed formula, no reasons
  legal        rules quoted, structured reservations, drafted in another hand
  procedural   listing/attendance/registry traffic
"""
import csv, os, re, sys, datetime as dt, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LEDGER = os.path.join(ROOT, "index", "COMMS_SIGNAL_LEDGER.tsv")
PRED = os.path.join(ROOT, "skill", "references", "PREDICTIONS-13SEP2026-scoreable.md")
FORMULA = re.compile(r"position remains to defend the appeal as outlined in (our|the) statement of facts and contentions", re.I)

def load():
    with open(LEDGER, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def save(rows, fields):
    with open(LEDGER, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        w.writeheader(); w.writerows(rows)

def d(s):
    return dt.date.fromisoformat(s) if s else None

def report(rows):
    today = dt.date.today()
    print(f"COMMS SIGNAL LEDGER — {len(rows)} rows — as at {today}\n")
    for party in ("Regulator", "MSH"):
        inbound = [r for r in rows if r["party"] == party and r["dir"] == "IN" and r["latency_days"]]
        if not inbound: continue
        lat = [int(r["latency_days"]) for r in inbound]
        subst = [int(r["latency_days"]) for r in inbound if r["kind"] in ("reply", "position", "legal")]
        acks = [int(r["latency_days"]) for r in inbound if r["kind"] in ("ack", "holding")]
        print(f"[{party}] inbound with latency: {len(inbound)}  all median {st.median(lat)}d"
              + (f"  substantive median {st.median(subst)}d range {min(subst)}–{max(subst)}" if subst else "")
              + (f"  ack/holding median {st.median(acks)}d" if acks else ""))
        regs = {}
        for r in rows:
            if r["party"] == party and r["dir"] == "IN" and r["register"]:
                regs[r["register"]] = regs.get(r["register"], 0) + 1
        print(f"         register mix: {regs}")
        f = [r["id"] + " " + r["date"] for r in rows if r["party"] == party and r["formula"] == "Y"]
        print(f"         SOFC formula used: {f or 'none'}")
    print("\nCONSEQUENCE RULE (class 1): inbound replies by whether a consequence was attached to what they answer")
    byid = {r["id"]: r for r in rows}
    for r in rows:
        if r["dir"] == "IN" and r["answers"] and r["latency_days"]:
            a = byid.get(r["answers"], {})
            print(f"  {r['id']} {r['date']} {r['party']:9s} {r['kind']:10s} {r['latency_days']:>3s}d  answers {r['answers']} (consequence: {a.get('consequence','?') or 'none'})")
    print("\nOPEN / EXPECTED")
    for r in rows:
        if r["kind"] == "expected" or r["dir"].endswith("?"):
            due = d(r["date"]); left = (due - today).days if due else None
            print(f"  {r['id']} {r['date']} {r['doc']}  → {'in ' + str(left) + ' days' if left is not None and left >= 0 else 'OVERDUE ' + str(-left) + ' days' if left is not None else ''}")
    # outbound requests without an answering row
    answered = {r["answers"] for r in rows if r["answers"]}
    for r in rows:
        if r["dir"] == "OUT" and r["kind"] in ("request", "offer", "notice") and r["id"] not in answered:
            print(f"  {r['id']} {r['date']} {r['doc']}  → NO REPLY ROW")

def score():
    if not os.path.exists(PRED):
        print("predictions file not found"); return
    txt = open(PRED).read()
    heads = re.findall(r"^### (.+)$", txt, re.M)
    blocks = re.split(r"^### ", txt, flags=re.M)[1:]
    n = 0
    for b in blocks:
        title = b.split("\n", 1)[0]
        if "OUTCOME:** ______" in b or "**OUTCOME:** ______" in b:
            n += 1; print(f"  UNSCORED  {title[:110]}")
    print(f"\n{n} predictions await an outcome. Score by replacing '______' with the outcome and a date.")

def register(path):
    t = open(path, errors="ignore").read()
    low = t.lower()
    ops = sum(low.count(k) for k in ("i apologise", "i am in the process", "could i please", "kindly", "i will get back", "i am in another"))
    pos = 1 if FORMULA.search(t) else 0
    pos += low.count("the respondent's position") + low.count("the regulator wishes to confirm")
    leg = sum(low.count(k) for k in ("rule 49", "r 49", "without prejudice to", "reserves", "reserved", "admissibility", "relevance", "de novo", "for the purposes of this proceeding only", "does not concede"))
    verdict = "legal" if leg >= 2 and leg >= ops else "position" if pos and pos >= ops else "operational" if ops else "procedural"
    print(f"operational markers {ops} | position markers {pos} | legal markers {leg}  →  REGISTER: {verdict}")
    print("formula present:", "YES" if FORMULA.search(t) else "no")
    print("mentions 'position':", low.count("position"))
    return verdict

def add(args):
    import argparse
    p = argparse.ArgumentParser(prog="comms_signals.py add")
    for k in ("id", "date", "dir", "party", "track", "doc", "kind"):
        p.add_argument("--" + k, required=True)
    for k in ("time_aest", "answers", "register", "formula", "consequence", "author_field", "source", "note"):
        p.add_argument("--" + k, default="")
    a = p.parse_args(args)
    rows = load(); fields = list(rows[0].keys())
    row = {k: getattr(a, k) for k in fields if k != "latency_days"}
    row["latency_days"] = ""
    if a.answers:
        prev = next((r for r in rows if r["id"] == a.answers), None)
        if prev and prev["date"]:
            row["latency_days"] = str((d(a.date) - d(prev["date"])).days)
    rows = [r for r in rows if r["id"] != a.id] + [row]
    rows.sort(key=lambda r: (r["date"], r["time_aest"]))
    save(rows, fields)
    print("added", row["id"], "latency", row["latency_days"] or "n/a")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "report"
    rows = load()
    if cmd == "report": report(rows)
    elif cmd == "score": score()
    elif cmd == "register": register(sys.argv[2])
    elif cmd == "add": add(sys.argv[2:])
    else: print(__doc__)
