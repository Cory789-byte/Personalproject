#!/usr/bin/env python3
"""POST-SEND MODEL — 5 Aug 2026, 17:52. Re-runs the 4 Aug prognosis with only the
deltas actually earned today:
  D1 the v16 submission is DELIVERED (07:30) and read by MSH/HR before close
  D2 MSH now KNOWS he holds the ART disclosure (information asymmetry gone)
  D3 escalate-within-Stage-1 invitation on the record
  D4 cooperation independently proven (clinic phoned Harrison re invoice, 11:45)
  D5 special leave requested on correct discretionary footing (cl 6.1/6.5 + C7)
  D6 QSuper reclassified 25-31 May as 'graduated return to work payment' -> claim file
     active, partial-capacity category in use -> IP resumption more plausible
  D7 Matheson still silent at close of Wed -> pre-mention window = Thu only
Seeded. Baseline in comments = 4 Aug prognosis run."""
import random
from collections import Counter
random.seed(5082026)
N = 300_000

def B(p): return random.random() < p
def pick(pairs):
    r = random.random(); c = 0
    for k, p in pairs:
        c += p
        if r < c: return k
    return pairs[-1][0]

sc = Counter(); weeks_by = {}
emp_strict = emp_fav = paid_c = appeal_win = appeal_fav = 0
adverse_att = adverse_beat = 0
nil_hits = capitulation = 0
ip_resume = 0; settle_any = 0; assess_c = 0; deemed = 0
esc_above_taylor = 0

for _ in range(N):
    # ---- MSH posture (D1,D2,D3 shift mass off silence toward engagement) ----
    posture = pick([("engage", .52), ("procedural", .33), ("silence", .15)])
    # baseline was .45/.35/.20

    # ---- matter escalates above Taylor within Stage 1/2 (D3) ----
    escalated = B({"engage": .72, "procedural": .48, "silence": .22}[posture])
    if escalated: esc_above_taylor += 1

    # ---- adverse action: D4 cooperation now independently evidenced ----
    p_adv = {"engage": .10, "procedural": .22, "silence": .30}[posture] * 0.72
    p_adv *= 0.85            # D4: clinic->Harrison invoice call = third-party proof
    adverse = B(p_adv)
    if adverse: adverse_att += 1
    challenge_win = B(0.73) if adverse else False   # D2 pre-judgment doc now known-known
    if adverse and challenge_win: adverse_beat += 1

    # ---- cl 10.3.6 by 24 Aug ----
    cl103 = pick([("grant", .30), ("refuse", .24), ("deemed", .46)])
    if cl103 == "deemed": deemed += 1

    # ---- special leave / leave coding (D5) ----
    leave = pick([("special leave", .22), ("rec leave applied", .50), ("nothing yet", .28)])
    if posture == "engage" and leave == "rec leave applied" and B(.35): leave = "special leave"

    # ---- psychosocial assessment commissioned ----
    if B({"engage": .55, "procedural": .25, "silence": .10}[posture]): assess_c += 1

    # ---- RTI nil return ----
    nil = B(.95) and B(.72)
    if nil: nil_hits += 1

    # ---- D6: IP resumption for the current period within ~6 weeks ----
    ip = B(.34)          # baseline implied ~.22 before the reclassification signal
    if ip: ip_resume += 1

    # ---- runway / forced capitulation (D6 relieves it when IP resumes) ----
    early_relief = (cl103 == "grant") or (leave == "special leave") or (posture == "engage" and B(.5))
    p_cap = .34
    if ip: p_cap *= 0.55
    runway_fail = (not early_relief) and B(p_cap)
    if runway_fail: capitulation += 1

    # ---- restoration / pay ----
    p_res = {"engage": .48, "procedural": .25, "silence": .14}[posture]
    if cl103 == "grant": p_res = min(.85, p_res + .24)
    if escalated: p_res += .04
    if adverse and not challenge_win: p_res = .02
    if adverse and challenge_win: p_res = min(p_res, .55)
    if runway_fail: p_res *= .55
    restored = B(min(p_res, .88))

    p_pay = .24
    if restored: p_pay = .74
    if cl103 == "grant": p_pay += .08
    if leave == "special leave": p_pay += .06
    if adverse and challenge_win: p_pay = max(p_pay, .65)
    if runway_fail: p_pay *= .70
    paid = B(min(p_pay, .87))

    p_set_emp = {"engage": .28, "procedural": .20, "silence": .14}[posture]
    if adverse: p_set_emp += .18
    if runway_fail: p_set_emp += .20
    settled_emp = (not restored) and B(min(p_set_emp, .62))

    strict = restored or (adverse and challenge_win)
    emp_ok = strict or settled_emp or paid

    # ---- appeal ----
    disclosure = B(.78)          # D7: order/timetable route now dominant
    reportB = B(.88)             # clinic engaged, billing live -> attendance more certain
    causation = B(.84 if reportB else .66)
    p_rma = .40 + (.07 if disclosure else 0) + (.05 if reportB else 0) \
            + (.03 if assess_c else 0) + (.08 if nil else 0)
    rma = B(min(p_rma, .68))
    hearing_ok = B(.82)
    won = causation and rma and hearing_ok

    p_set_app = .36 + (.09 if disclosure else 0) + (.05 if reportB else 0) \
                + (.06 if nil else 0) + (.05 if emp_ok else 0)
    p_set_app += .05             # D2: they know he holds the pre-judgment document
    if runway_fail: p_set_app += .10
    settled_app = (not won) and B(min(p_set_app, .72))
    app_ok = won or settled_app

    emp_strict += strict; emp_fav += emp_ok; paid_c += paid
    appeal_win += won; appeal_fav += app_ok
    settle_any += (settled_emp or settled_app)

    # ---- terminal scenario ----
    if adverse and not challenge_win: s = "F. Dismissed, challenge fails"
    elif restored and paid and app_ok: s = "A. Back at work, paid, appeal resolved"
    elif restored and paid: s = "B. Back at work and paid, appeal unresolved"
    elif restored: s = "C. Back at work, pay unrecovered"
    elif adverse and challenge_win: s = "D. Dismissal attempted and defeated"
    elif settled_emp and app_ok: s = "E. Exit on terms + appeal resolved"
    elif settled_emp or app_ok: s = "G. One track resolves, the other does not"
    else: s = "H. Grinds on"
    sc[s] += 1
    w = 6 if cl103 == "grant" else 10
    if posture == "silence": w += 6
    if adverse: w += 8
    if settled_app or settled_emp: w = min(w + 4, 34)
    if won: w = max(w, 30)
    if escalated: w -= 1
    weeks_by.setdefault(s, []).append(w + random.randint(-2, 4))

p = lambda x: round(100*x/N, 1)
print("=== TERMINAL SCENARIOS (4 Aug baseline in brackets) ===")
base = {"G. One track resolves, the other does not": 32.6, "A. Back at work, paid, appeal resolved": 17.9,
        "H. Grinds on": 12.0, "E. Exit on terms + appeal resolved": 10.3, "C. Back at work, pay unrecovered": 9.0,
        "B. Back at work and paid, appeal unresolved": 7.8, "D. Dismissal attempted and defeated": 6.4,
        "F. Dismissed, challenge fails": 4.0}
for k, v in sc.most_common():
    ws = sorted(weeks_by[k]); med = ws[len(ws)//2]
    b = base.get(k)
    print(f"  {p(v):>5}%  (was {b:>4}%)  median {med:>2}w   {k}")
print("\n=== AGGREGATES (baseline) ===")
for label, val, b in [("Employment strict", emp_strict, 41.2), ("Employment favourable", emp_fav, 66.8),
                      ("Pay recovered", paid_c, 42.5), ("Appeal win at hearing", appeal_win, 37.6),
                      ("Appeal favourable", appeal_fav, 70.5), ("Some settlement", settle_any, None),
                      ("RTI nil return", nil_hits, 68.6), ("Forced capitulation (runway)", capitulation, 18.8),
                      ("Adverse action attempted", adverse_att, 13.2)]:
    bs = f"(was {b}%)" if b else ""
    print(f"  {p(val):>5}%  {label} {bs}")
print(f"  {round(100*adverse_beat/max(adverse_att,1),1)}%  of attempts defeated (was 69.7%)")
print(f"  {p(esc_above_taylor):>5}%  matter escalates above Taylor in Stage 1/2  [NEW]")
print(f"  {p(ip_resume):>5}%  IP benefit resumes within ~6 weeks  [NEW]")
print(f"  {p(assess_c):>5}%  psychosocial assessment commissioned")
print(f"  {p(deemed):>5}%  cl 10.3.6 deemed refusal")
