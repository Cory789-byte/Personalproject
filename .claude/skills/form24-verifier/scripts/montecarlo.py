#!/usr/bin/env python3
"""L3b - Monte Carlo over the mock classification (/tmp/f185v.json, written by
build_form24_mock_response.py). Per-fact response probabilities are STATED
ESTIMATES calibrated on the single observed response of 18 February 2026 -
present results as sensitivity, not prediction. Run from wc2024227/drafts/
after the mock. Seeded for reproducibility."""
import json, random, statistics, sys
random.seed(20260825)
import os, tempfile
F = json.load(open(os.path.join(tempfile.gettempdir(), 'f185v.json'))); N = len(F)
P = {'A': (0.97,0.025,0.005), 'A!': (0.99,0.01,0.0), 'A*': (0.90,0.08,0.02),
     'A~': (0.93,0.06,0.01), 'D?': (0.50,0.30,0.20), 'N': (0.15,0.85,0.0)}
RIDER = 0.15
def run():
    admit=na=deny=riders=0
    u = random.random()
    if u < 0.05: return N,0,0,0
    for f in F:
        a,x,d = P.get(f['v'], P['A']); r = random.random()
        if r < a:
            admit += 1
            if random.random() < RIDER: riders += 1
        elif r < a+x: na += 1
        else: deny += 1
    if u >= 0.90 and random.random() < 0.35: admit = N - na
    return admit,na,deny,riders
R = [run() for _ in range(10000)]
A = sorted(r[0] for r in R)
q = lambda p: A[int(p/100*len(A))]
print(f"{N} facts | admitted-or-deemed: p5={q(5)} median={q(50)} p95={q(95)}")
print(f"P(>=250)={sum(1 for a in A if a>=250)/len(A):.1%}  "
      f"E[denials]={statistics.mean(r[2] for r in R):.2f}  "
      f"E[riders]={statistics.mean(r[3] for r in R):.1f}")
if q(5) < N * 0.82: print(f"WARN: p5 below 82% of {N} - review classification drift"); sys.exit(1)
