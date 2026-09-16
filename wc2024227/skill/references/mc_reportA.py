#!/usr/bin/env python3
"""REPORT A NODE — 5 Aug 2026. Models what MSH's own funded psychiatric report says and
what it does downstream. Key premise: MSH's own questions (1(d) controls medically
necessary; Q8 tasks/situations/environments that exacerbate) CANNOT be answered without
opining on the workplace. Seeded."""
import random
from collections import Counter
random.seed(508262)
N = 300_000
def B(p): return random.random() < p
def pick(pairs):
    r = random.random(); c = 0
    for k, p in pairs:
        c += p
        if r < c: return k
    return pairs[-1][0]

out = Counter(); after = Counter()
restored = settled = dismissed_ok = 0
appeal_win = appeal_fav = 0

for _ in range(N):
    # Report A content
    r = pick([("fit with controls — controls specified", .62),
              ("fit, but NOT in that work area / redeployment", .17),
              ("fit with controls, staged/conditional", .13),
              ("not fit for any work at present", .08)])
    out[r] += 1
    controls_named = r.startswith("fit")

    # MSH response to its own report
    if controls_named:
        resp = pick([("implements controls, return", .46), ("partial/slow implementation", .29),
                     ("does not implement; impasse", .17), ("uses it to exit him", .08)])
    else:
        resp = pick([("medical exit / ill-health pathway", .55), ("settlement/exit on terms", .35),
                     ("holds position", .10)])
    after[resp] += 1

    ret = resp in ("implements controls, return", "partial/slow implementation") and B(.86)
    if ret: restored += 1
    st = (not ret) and B(.55 if resp in ("settlement/exit on terms", "uses it to exit him",
                                         "medical exit / ill-health pathway", "does not implement; impasse") else .25)
    if st: settled += 1

    # appeal effects
    p_rma = .40 + .07 + .05 + (.08 if B(.72) else 0)
    if controls_named: p_rma += .06          # medical advice that controls were necessary
    if r.startswith("fit, but NOT"): p_rma += .10   # strongest manner/causation signal
    if resp == "does not implement; impasse": p_rma += .05
    rma = B(min(p_rma, .74))
    caus = B(.86 if r != "not fit for any work at present" else .88)
    won = caus and rma and B(.82)
    p_set = .40 + (.06 if controls_named else .10) + (.05 if st else 0)
    settled_app = (not won) and B(min(p_set, .74))
    appeal_win += won; appeal_fav += (won or settled_app)

p = lambda x: round(100*x/N, 1)
print("=== WHAT REPORT A SAYS ===")
for k, v in out.most_common(): print(f"  {p(v):>5}%  {k}")
print("=== MSH RESPONSE TO ITS OWN REPORT ===")
for k, v in after.most_common(): print(f"  {p(v):>5}%  {k}")
print(f"\n  {p(restored):>5}%  returns to work off the back of the report")
print(f"  {p(settled):>5}%  resolves by settlement/exit instead")
print(f"  {p(appeal_win):>5}%  appeal win at hearing (post-report)")
print(f"  {p(appeal_fav):>5}%  appeal favourable incl. settlement (post-report)")
