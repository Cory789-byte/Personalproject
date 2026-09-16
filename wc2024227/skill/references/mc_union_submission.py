#!/usr/bin/env python3
"""UNION SUBMISSION NODE — what changes if Together makes a CE-level submission on the
work area. Baseline = 5 Aug post-send model (assessment 38.5%, adverse attempted 10.4%,
employment favourable 71.4%, appeal favourable 76.1%). Seeded."""
import random
from collections import Counter
random.seed(60826)
N = 300_000
def B(p): return random.random() < p
def pick(pairs):
    r = random.random(); c = 0
    for k, p in pairs:
        c += p
        if r < c: return k
    return pairs[-1][0]

path = Counter(); resp = Counter()
assess = adverse = adverse_beat = 0
emp_fav = appeal_fav = appeal_win = 0
survives_settlement = 0; hcf = 0; ce_letter = 0
refusal_in_writing = 0

for _ in range(N):
    # --- does the union pick it up, and how far ---
    u = pick([("carries it: CE submission + HCF", .34),
              ("carries it: CE submission only", .21),
              ("carries it: HCF/local only", .18),
              ("supports but he remains the requester", .17),
              ("declines / no capacity", .10)])
    path[u] += 1
    union_ce = u.startswith("carries it") and "CE submission" in u
    union_any = u.startswith("carries it")
    if union_ce: ce_letter += 1
    if "HCF" in u: hcf += 1

    # --- MSH response to a union CE-level request ---
    if union_ce:
        r = pick([("commissions an assessment", .46), ("commits in principle, slow", .24),
                  ("refers to existing wellbeing activity", .17), ("refuses in writing", .09),
                  ("no substantive response", .04)])
    elif union_any:
        r = pick([("commissions an assessment", .32), ("commits in principle, slow", .25),
                  ("refers to existing wellbeing activity", .24), ("refuses in writing", .10),
                  ("no substantive response", .09)])
    else:
        r = pick([("commissions an assessment", .18), ("commits in principle, slow", .17),
                  ("refers to existing wellbeing activity", .25), ("refuses in writing", .10),
                  ("no substantive response", .30)])
    resp[r] += 1
    if r in ("commissions an assessment",) or (r == "commits in principle, slow" and B(.55)):
        assess += 1
    if r == "refuses in writing": refusal_in_writing += 1
    if union_any and B(.92): survives_settlement += 1

    # --- adverse action risk: delegate + union + CE-level protected activity ---
    p_adv = .104
    if union_ce: p_adv *= 0.62
    elif union_any: p_adv *= 0.78
    a = B(p_adv)
    if a: adverse += 1
    p_beat = .73 + (.09 if union_ce else (.05 if union_any else 0))
    if a and B(min(p_beat, .88)): adverse_beat += 1

    # --- employment / appeal knock-on ---
    p_empfav = .714 + (.03 if union_ce else 0) + (.02 if assess else 0)
    if B(min(p_empfav, .82)): emp_fav += 1
    p_rma = .40 + .07 + .05 + (.08 if B(.72) else 0)
    if r == "refuses in writing": p_rma += .07     # documented refusal of a union WHS request
    if r == "commissions an assessment": p_rma += .04
    if union_ce: p_rma += .03
    rma = B(min(p_rma, .74))
    won = B(.86) and rma and B(.82)
    p_set = .41 + (.05 if union_ce else 0) + (.04 if r == "refuses in writing" else 0)
    fav = won or B(min(p_set, .74))
    appeal_win += won; appeal_fav += fav

p = lambda x: round(100*x/N, 1)
print("=== DOES THE UNION CARRY IT? ===")
for k, v in path.most_common(): print(f"  {p(v):>5}%  {k}")
print(f"  → {p(ce_letter)}% CE-level union submission · {p(hcf)}% reaches the HCF")
print("\n=== MSH RESPONSE ===")
for k, v in resp.most_common(): print(f"  {p(v):>5}%  {k}")
print(f"\n  {p(assess):>5}%  ⭐ ASSESSMENT COMMISSIONED   (baseline 38.5%)")
print(f"  {p(survives_settlement):>5}%  request survives his own settlement")
print(f"  {p(refusal_in_writing):>5}%  written refusal of a union WHS request [evidence]")
print(f"  {p(adverse):>5}%  adverse action attempted     (baseline 10.4%)")
print(f"  {round(100*adverse_beat/max(adverse,1),1)}%  of attempts defeated        (baseline 72.8%)")
print(f"  {p(emp_fav):>5}%  employment favourable        (baseline 71.4%)")
print(f"  {p(appeal_win):>5}%  appeal win at hearing        (baseline 39.2%)")
print(f"  {p(appeal_fav):>5}%  appeal favourable            (baseline 76.1%)")
