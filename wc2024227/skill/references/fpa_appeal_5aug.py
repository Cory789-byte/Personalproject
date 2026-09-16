#!/usr/bin/env python3
"""
Evidence-anchored Monte Carlo for Full-Picture Analysis (stage 4).

Each BLOCK is a condition that must hold for the target outcome. The red (opposing) and
blue (advocate) passes set a defensible LOW and HIGH probability for each block; the
simulation integrates over that range (epistemic uncertainty) plus a shared latent
"decision-maker disposition" factor so correlated blocks move together (a tribunal/buyer
persuaded on one tends to be persuaded on others).

This is decision-support, not prophecy: the inputs are reasoned judgements, so the OUTPUT
is a probability *with a range*, plus a tornado showing which block actually drives it.
Edit the BLOCKS dict and OUTCOME_RULE, then run:  python3 montecarlo.py
"""
import numpy as np

rng = np.random.default_rng(42)

# ----------------------------------------------------------------------------------------
# CONFIGURE THIS BLOCK. (low, mode, high) = red / reconciled / blue.  load = how strongly the
# block tracks the shared disposition factor (0.4 weak .. 1.0 strong).
BLOCKS = {
    # WC/2024/227 — the s 32 elements the appeal must carry. red / reconciled / blue, load.
    "1 Injury: psychiatric injury established (MDD, Krishnaiah 13 Feb 2025)":
        (0.90, 0.95, 0.98, 0.4),
    "2 Arising out of employment (s 32(1) connection)":
        (0.88, 0.93, 0.97, 0.5),
    "3 Employment A SIGNIFICANT contributing factor — MEDICAL causation to the fatigue/roster strand":
        (0.52, 0.68, 0.84, 0.9),
    "4 s 32(5)(a) exclusion DEFEATED — individual-stressor (Mahaffey/Carr) not global (Delaney)":
        (0.48, 0.66, 0.82, 1.0),
    "5 Hearing conducted / evidence accepted without adverse credit or procedural failure":
        (0.78, 0.86, 0.93, 0.7),
}
# How blocks combine. "AND" = every block must hold (the usual case). "ANY" = at least one.
OUTCOME_RULE = "AND"
# Optional judgement overlay: P(acceptable settlement | not a clean win). 0 to disable.
SETTLEMENT_PICKUP = 0.55
# ----------------------------------------------------------------------------------------

WORLDS, N = 600, 40_000
logit = lambda p: np.log(p / (1 - p))
sig = lambda x: 1 / (1 + np.exp(-x))

def combine(cols):
    out = cols[0].copy()
    for c in cols[1:]:
        out = (out & c) if OUTCOME_RULE == "AND" else (out | c)
    return out

def simulate(blocks):
    pw, cond = [], {k: [] for k in blocks}
    for _ in range(WORLDS):
        T = rng.standard_normal(N)
        draws = {}
        for k, (lo, mode, hi, load) in blocks.items():
            p = rng.triangular(lo, mode, hi)               # epistemic draw in red-blue range
            draws[k] = (rng.random(N) < sig(logit(p) + load * T)).astype(int)
        win = combine([draws[k] for k in blocks])
        pw.append(win.mean())
        for k in blocks:
            m = draws[k].astype(bool)
            cond[k].append((win[m].mean() if m.any() else np.nan,
                            win[~m].mean() if (~m).any() else np.nan))
    return np.array(pw), cond

pw, cond = simulate(BLOCKS)
base = pw.mean()
print("=" * 60)
print("FULL-PICTURE MONTE CARLO")
print("=" * 60)
print(f"  P(outcome) central ........ {base:.0%}")
print(f"  80% credible interval ..... {np.percentile(pw,10):.0%} - {np.percentile(pw,90):.0%}")
print(f"  full red<->blue span ...... {pw.min():.0%} - {pw.max():.0%}")
if SETTLEMENT_PICKUP > 0:
    print(f"  P(favourable outcome incl. settlement) ~ {base + (1-base)*SETTLEMENT_PICKUP:.0%}")

print("\nConditional impact of each block (win% if it holds vs fails):")
for k in BLOCKS:
    arr = np.array(cond[k])
    print(f"  {k:<10} holds {np.nanmean(arr[:,0]):.0%}   fails {np.nanmean(arr[:,1]):.0%}")

print("\nTORNADO — swing in P(outcome) when each block moves +/-0.12:")
rows = []
for k, (lo, mode, hi, load) in BLOCKS.items():
    s = []
    for d in (-0.12, 0.12):
        L = min(max(0.02, lo+d), 0.96)
        M = min(max(L+0.005, mode+d), 0.975)
        H = min(max(M+0.005, hi+d), 0.99)
        b = dict(BLOCKS); b[k] = (L, M, H, load)
        s.append(simulate(b)[0].mean())
    rows.append((k, abs(s[1] - s[0])))
for k, sw in sorted(rows, key=lambda r: -r[1]):
    print(f"  {k[:70]:<70} {sw:.1%}")

print("\n(Inputs are reasoned priors. Treat as a structured judgement + sensitivity map,")
print(" not a measurement. The ranking of drivers is more robust than the point estimate.)")
