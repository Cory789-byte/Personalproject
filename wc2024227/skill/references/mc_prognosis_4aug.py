#!/usr/bin/env python3
"""PROGNOSIS MODEL — 4 Aug 2026. Extends mc_full_4aug.py with (a) the nil-return node,
(b) mutually-exclusive terminal scenarios, (c) runway interaction. Seeded."""
import random
from collections import Counter
random.seed(4082026)
N = 200_000

def B(p): return random.random() < p

sc = Counter(); weeks_by = {}; nil_hits = 0
appeal_win = appeal_fav = emp_strict = emp_fav = paid_c = 0
capitulation = 0

for _ in range(N):
    # --- MSH posture ---
    r = random.random()
    posture = "engage" if r < 0.45 else ("procedural" if r < 0.80 else "silence")

    # --- RTI nil return (his knowledge: never assessed) ---
    lodged = B(0.95)
    nil_return = lodged and B(0.72)      # "no documents located" for the assessment categories
    if nil_return: nil_hits += 1

    # --- adverse action ---
    p_adv = {"engage":0.10,"procedural":0.22,"silence":0.30}[posture] * 0.72
    adverse = B(p_adv)
    challenge_win = B(0.70) if adverse else False

    # --- cl 10.3.6 ---
    r = random.random()
    cl103 = "grant" if r < 0.28 else ("refuse" if r < 0.52 else "deemed")

    assessment = B({"engage":0.55,"procedural":0.25,"silence":0.10}[posture])

    # --- runway: forced capitulation if nothing lands early and no income ---
    early_relief = (cl103 == "grant") or (posture == "engage" and B(0.5))
    runway_fail = (not early_relief) and B(0.34)     # accepts whatever is offered
    if runway_fail: capitulation += 1

    # --- restoration / pay ---
    p_res = {"engage":0.46,"procedural":0.24,"silence":0.14}[posture]
    if cl103 == "grant": p_res = min(0.85, p_res + 0.24)
    if adverse and not challenge_win: p_res = 0.02
    if adverse and challenge_win: p_res = min(p_res, 0.55)
    if runway_fail: p_res *= 0.55
    restored = B(p_res)

    p_pay = 0.22
    if restored: p_pay = 0.72
    if cl103 == "grant": p_pay += 0.08
    if adverse and challenge_win: p_pay = max(p_pay, 0.65)
    if runway_fail: p_pay *= 0.7
    paid = B(min(p_pay, 0.85))

    p_set_emp = {"engage":0.26,"procedural":0.20,"silence":0.14}[posture]
    if adverse: p_set_emp += 0.18
    if runway_fail: p_set_emp += 0.20
    settled_emp = (not restored) and B(min(p_set_emp, 0.62))

    # --- appeal ---
    disclosure = B(0.75)
    reportB = B(0.86)
    causation = B(0.84 if reportB else 0.66)
    p_rma = 0.40
    if disclosure: p_rma += 0.07
    if reportB: p_rma += 0.05
    if assessment: p_rma += 0.03
    if nil_return: p_rma += 0.08          # ⭐ the absence proved from their own records
    rma = B(min(p_rma, 0.68))
    hearing_ok = B(0.82)
    won_hearing = causation and rma and hearing_ok

    p_set_app = 0.36
    if disclosure: p_set_app += 0.09
    if reportB: p_set_app += 0.05
    if nil_return: p_set_app += 0.06
    if runway_fail: p_set_app += 0.10      # settles cheap
    settled_app = (not won_hearing) and B(min(p_set_app, 0.70))

    # --- tallies ---
    strict = restored or (adverse and challenge_win)
    emp_ok = strict or settled_emp or paid
    app_ok = won_hearing or settled_app
    emp_strict += strict; emp_fav += emp_ok; paid_c += paid
    appeal_win += won_hearing; appeal_fav += app_ok

    # --- terminal scenario (mutually exclusive, ordered best→worst) ---
    if adverse and not challenge_win:
        s = "F. Dismissed, challenge fails — worst case"
    elif restored and paid and app_ok:
        s = "A. Back at work, paid, appeal resolved favourably"
    elif restored and paid:
        s = "B. Back at work and paid, appeal lost/unresolved"
    elif restored:
        s = "C. Back at work, pay unrecovered"
    elif adverse and challenge_win:
        s = "D. Dismissal attempted and defeated (reinstatement/compensation)"
    elif settled_emp and app_ok:
        s = "E. Exit on negotiated terms + appeal resolved (both settled)"
    elif settled_emp or app_ok:
        s = "G. One track resolves, the other does not"
    else:
        s = "H. Grinds on — neither track resolved in the window"
    sc[s] += 1

    w = 6 if cl103 == "grant" else 10
    if posture == "silence": w += 6
    if adverse: w += 8
    if settled_app or settled_emp: w = min(w + 4, 34)
    if won_hearing: w = max(w, 30)
    w += random.randint(-2, 4)
    weeks_by.setdefault(s, []).append(w)

pct = lambda x: round(100*x/N, 1)
print("=== TERMINAL SCENARIOS (mutually exclusive) ===")
for s, c in sc.most_common():
    ws = sorted(weeks_by[s]); med = ws[len(ws)//2]
    print(f"{pct(c):>5}%  median {med:>2}w   {s}")
print()
print("=== AGGREGATES ===")
print(f"Employment strict          {pct(emp_strict)}%")
print(f"Employment favourable      {pct(emp_fav)}%")
print(f"Pay recovered              {pct(paid_c)}%")
print(f"Appeal win at hearing      {pct(appeal_win)}%")
print(f"Appeal favourable          {pct(appeal_fav)}%")
print(f"RTI nil return obtained    {pct(nil_hits)}%")
print(f"Forced capitulation (runway) {pct(capitulation)}%")
