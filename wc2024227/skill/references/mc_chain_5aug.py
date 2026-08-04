#!/usr/bin/env python3
"""CHAIN PREDICTION — disclosure → MSH → Respondent → Dwyer. 5 Aug 2026 pre-send state.
Four coupled nodes, 300k runs, seeded. Calibrated to: banked reception model (Regulator
abide ~62%), 4 Aug framework/prognosis models, Willson stand-down theory, the v16 letter
and ART-letter effects."""
import random
from collections import Counter
random.seed(5082026)
N = 300_000

def B(p): return random.random() < p
def pick(pairs):
    r = random.random(); c = 0
    for name, p in pairs:
        c += p
        if r < c: return name
    return pairs[-1][0]

n1 = Counter(); n2p = Counter(); n2q = Counter(); n2l = Counter()
n3 = Counter(); n3w = 0; n3s = 0
n4 = Counter(); enlarged = 0
script = Counter()

for _ in range(N):
    # ---------------- NODE 1: MATHESON DISCLOSURE ----------------
    arrival = pick([("pre-mention Wed/Thu", .40), ("mention-eve/Fri", .15),
                    ("late next week", .25), ("not delivered", .20)])
    arrived = arrival != "not delivered"
    quality = pick([("complete v Tier1", .35), ("curated", .50), ("thin", .15)]) if arrived else "n/a"
    tier2 = arrived and B(.30)          # MSH-sourced Jul-2026 material visible
    n1[arrival] += 1

    # ---------------- NODE 2: MSH (employment track, wk of 5-17 Aug) ----------------
    posture = pick([("engage", .45), ("procedural-harden", .35), ("silence", .20)])
    n2p[posture] += 1
    q7 = pick([("substantive answers", .25), ("partial answers", .35), ("no answers", .40)])
    # letter effects: engage posture raises answer odds
    if posture == "engage" and q7 == "no answers" and B(.5): q7 = "partial answers"
    if posture == "silence": q7 = "no answers"
    n2q[q7] += 1
    leave = pick([("special leave granted", .18), ("rec leave applied anyway", .55),
                  ("nothing applied yet", .27)])
    if posture == "engage" and leave == "rec leave applied anyway" and B(.3):
        leave = "special leave granted"
    n2l[leave] += 1
    offramp_stage2 = B({"engage": .38, "procedural-harden": .18, "silence": .08}[posture])

    # ---------------- NODE 3: RESPONDENT at the mention ----------------
    pos64 = pick([("consent/abide", .62), ("narrow objection", .28), ("full fight", .10)])
    # a complete disclosure arriving pre-mention nudges toward consent (they've already folded)
    if arrival == "pre-mention Wed/Thu" and quality != "thin" and pos64 == "narrow objection" and B(.4):
        pos64 = "consent/abide"
    n3[pos64] += 1
    willson = B(.35 if pos64 != "consent/abide" else .20)
    if willson: n3w += 1
    p_settle_appr = .30 + (.10 if pos64 == "consent/abide" else 0) + (.08 if offramp_stage2 else 0) \
                    + (.05 if quality == "complete v Tier1" else 0)
    settle_approach = B(min(p_settle_appr, .55))   # WP contact within ~3 weeks of mention
    if settle_approach: n3s += 1

    # ---------------- NODE 4: DWYER ----------------
    if pos64 == "consent/abide":
        outcome = "production by consent + timetable"
    elif pos64 == "narrow objection":
        outcome = pick([("order with narrowed categories", .70), ("adjourn for production", .20),
                        ("reserved", .10)])
    else:
        outcome = pick([("order substantially as sought", .55), ("order narrowed", .25),
                        ("adjourn/reserve", .20)])
    n4[outcome] += 1
    rec_enlarged = outcome.startswith(("production", "order")) or (arrived and quality == "complete v Tier1")
    if rec_enlarged: enlarged += 1

    # ---------------- MODAL SCRIPT ----------------
    s = (("D+" if arrived else "D-") + ("|MSH:" + posture[:4]) + ("|R:" + pos64[:7])
         + ("|Dw:" + ("prod" if rec_enlarged else "no-prod")) + ("|settle" if settle_approach else ""))
    script[s] += 1

pct = lambda x: round(100*x/N, 1)
print("NODE 1 — disclosure arrival:")
for k, v in n1.most_common(): print(f"  {pct(v):>5}%  {k}")
print("NODE 2 — MSH posture / answers / leave:")
for k, v in n2p.most_common(): print(f"  {pct(v):>5}%  {k}")
for k, v in n2q.most_common(): print(f"  {pct(v):>5}%  {k}")
for k, v in n2l.most_common(): print(f"  {pct(v):>5}%  {k}")
print("NODE 3 — Respondent 64G posture:")
for k, v in n3.most_common(): print(f"  {pct(v):>5}%  {k}")
print(f"  {pct(n3w):>5}%  Willson appears")
print(f"  {pct(n3s):>5}%  settlement approach within ~3 weeks of mention")
print("NODE 4 — Dwyer outcome:")
for k, v in n4.most_common(): print(f"  {pct(v):>5}%  {k}")
print(f"  {pct(enlarged):>5}%  ⭐ RECORD ENLARGED (order/consent/complete list)")
print("TOP CHAIN SCRIPTS:")
for k, v in script.most_common(5): print(f"  {pct(v):>5}%  {k}")
