#!/usr/bin/env python3
"""RETURN-AND-APPEAL MODEL — 5 Aug 2026 late.
Decomposes the restoration node into FORM and TIMING, and prices the appeal
CONDITIONAL on the form of return. Seeded.

Reading note baked into the priors: the QSuper 'graduated return to work payment'
for 25-31 May 2026 is HISTORICAL (he was working then; partial benefit = employment
income offset). It does NOT show MSH announcing a present return. What it DOES prove:
(a) the policy's graduated-RTW category is live on his claim; (b) MSH's payslip supply
drives ART's calculations; (c) MSH's 'unable to accommodate a graduated return to work'
is a statement refusing the very arrangement the policy funds."""
import random
from collections import Counter
random.seed(50826)
N = 300_000

def B(p): return random.random() < p
def pick(pairs):
    r = random.random(); c = 0
    for k, p in pairs:
        c += p
        if r < c: return k
    return pairs[-1][0]

form = Counter(); when = Counter(); route = Counter()
appeal_by_form = {}
art_corrected = 0; returned_any = 0
appeal_win = appeal_fav = 0
both = 0

for _ in range(N):
    posture = pick([("engage", .52), ("procedural", .33), ("silence", .15)])
    escalated = B({"engage": .72, "procedural": .48, "silence": .22}[posture])

    # --- does MSH correct/withdraw the 'unable to accommodate' representation? ---
    p_corr = .30 + (.18 if posture == "engage" else 0) + (.08 if escalated else 0)
    corrected = B(min(p_corr, .58))
    if corrected: art_corrected += 1

    # --- RETURN: does it happen within ~12 weeks, and in what form? ---
    p_ret = {"engage": .50, "procedural": .27, "silence": .15}[posture]
    if corrected: p_ret += .16          # withdrawing the refusal is the precondition
    if escalated: p_ret += .04
    adverse = B(.104)                   # 5 Aug model
    if adverse and B(.27): p_ret = .02  # dismissal not defeated kills return
    ret = B(min(p_ret, .84))
    if ret: returned_any += 1

    if ret:
        f = pick([("graduated / reduced hours (the 0.6)", .56),
                  ("full permanent line with adjustments", .29),
                  ("alternative duties or redeployment", .15)])
        r_route = pick([("Stage 1/2 agreement", .40), ("cl 10.3 grant or deemed-refusal pressure", .22),
                        ("WorkCover acceptance + rehab RTW plan", .26), ("QIRC / settlement terms", .12)])
        w = {"Stage 1/2 agreement": random.randint(2, 6),
             "cl 10.3 grant or deemed-refusal pressure": random.randint(3, 8),
             "WorkCover acceptance + rehab RTW plan": random.randint(6, 16),
             "QIRC / settlement terms": random.randint(8, 20)}[r_route]
        form[f] += 1; route[r_route] += 1
        when["≤4 weeks" if w <= 4 else ("5-8 weeks" if w <= 8 else ("9-16 weeks" if w <= 16 else ">16 weeks"))] += 1
    else:
        f = "no return (exit on terms / unresolved)"
        form[f] += 1

    # --- APPEAL, conditional on the return picture ---
    disclosure = B(.78); reportB = B(.88)
    causation = B(.84 if reportB else .66)
    nil = B(.95) and B(.72)
    p_rma = .40 + (.07 if disclosure else 0) + (.05 if reportB else 0) + (.08 if nil else 0)
    # ⭐ a corrected/withdrawn 'cannot accommodate' + an actual RTW = the employer's own
    # conduct is shown to have been the barrier, which strengthens the manner case
    if corrected: p_rma += .04
    if ret and f.startswith("graduated"): p_rma += .03
    rma = B(min(p_rma, .70))
    hearing_ok = B(.82)
    # returning to work does not defeat liability; it removes the secondary-gain narrative
    credit_boost = .03 if ret else 0
    won = causation and rma and B(min(hearing_ok + credit_boost, .88))

    p_set = .36 + (.09 if disclosure else 0) + (.05 if reportB else 0) + (.06 if nil else 0) + .05
    if ret: p_set += .06                # employment resolved -> appeal settles easier
    if corrected: p_set += .03
    settled = (not won) and B(min(p_set, .74))
    fav = won or settled
    appeal_win += won; appeal_fav += fav
    appeal_by_form.setdefault(f, [0, 0])
    appeal_by_form[f][0] += won; appeal_by_form[f][1] += fav
    if ret and fav: both += 1

p = lambda x, d=N: round(100*x/d, 1)
print("=== RETURN TO WORK ===")
print(f"  {p(returned_any)}%  RETURN IN ANY FORM within ~12 weeks")
for k, v in form.most_common(): print(f"    {p(v):>5}%  {k}")
print("  Route taken (of returns):")
tot = sum(route.values())
for k, v in route.most_common(): print(f"    {p(v, tot):>5}%  {k}")
print("  Timing (of returns):")
for k in ["≤4 weeks", "5-8 weeks", "9-16 weeks", ">16 weeks"]:
    if k in when: print(f"    {p(when[k], tot):>5}%  {k}")
print(f"\n  {p(art_corrected)}%  MSH corrects/withdraws the 'unable to accommodate' position")
print("\n=== APPEAL ===")
print(f"  {p(appeal_win)}%  win at contested hearing   (5 Aug baseline 39.2%)")
print(f"  {p(appeal_fav)}%  favourable incl. settlement (5 Aug baseline 76.1%)")
print("  Appeal conditional on the form of return:")
for k, (w, f) in sorted(appeal_by_form.items(), key=lambda x: -x[1][1]):
    n = form[k]
    print(f"    win {p(w, n):>5}% · fav {p(f, n):>5}%   {k}")
print(f"\n  {p(both)}%  ⭐ BOTH: back at work AND appeal resolved favourably")
