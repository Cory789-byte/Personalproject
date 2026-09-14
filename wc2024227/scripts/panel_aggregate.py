#!/usr/bin/env python3
"""Panel aggregation for the 25-September forecast (E24).

Implements the aggregation stack with the best published forecasting track
record, applied to the five-lens ultracode panel:

  1. MEDIAN        — robust to single-lens outliers (the reference-class
                     skeptic and the steelman are deliberately extreme).
  2. TRIMMED MEAN  — drop min and max per quantity, mean the middle three.
  3. LOGIT EXTREMIZATION — Satopää et al. (2014): independent forecasters
                     each hold partial information; the aggregate is
                     systematically under-confident, so push the pooled
                     probability away from 50% in logit space:
                        p* = p^d / (p^d + (1-p)^d),  d = 1.3 (mild; n=5).
                     Applied to binary quantities only (thirteen_conceded,
                     register_legal, formula_absent). The S1–S5 categorical
                     distribution is aggregated by median then renormalised —
                     extremizing a multinomial toward its mode is not
                     supported by the evidence and is skipped.
  4. REFUTER UPDATE— each adversarial refutation that SURVIVES (or lands a
                     partial hit) is applied as a bounded additive shift,
                     capped at half the distance it proposed (the refuter is
                     one more forecaster, not an oracle).
  5. NORMALISE     — S1..S5 forced to sum to 100.

Scoring (run after the 25th):
  BRIER            — for each binary quantity and for the categorical shape
                     (multiclass Brier), score BOTH the solo E23 numbers and
                     the panel E24 numbers, so the file learns which process
                     to trust. Lower is better; 0.25 = ignorance on a binary.

Usage:
  python3 panel_aggregate.py            # aggregate the embedded panel
  python3 panel_aggregate.py score S1   # after the 25th: score outcome
                                        # (S1|S2|S3|S4|S5, plus flags
                                        #  --thirteen y|n --register legal|op
                                        #  --formula absent|present)
"""
import sys, json, math

# ---- the panel (wf_655766b9-cbc, 14 Sep 2026) -----------------------------
LENSES = ["empiricist", "govt_lawyer", "game_theorist", "ref_class_skeptic", "steelman"]
PANEL = {
    #                 S1  S2  S3  S4  S5   13c  reg  formula-absent
    "empiricist":        [55, 18,  9, 2, 16,  72, 63, 74],
    "govt_lawyer":       [58, 15, 10, 2, 15,  65, 68, 66],
    "game_theorist":     [50, 28,  6, 3, 13,  76, 70, 65],
    "ref_class_skeptic": [40, 14, 20, 2, 24,  48, 55, 62],
    "steelman":          [46, 29,  7, 4, 14,  74, 66, 72],
}
SHAPES = ["S1_documents_only", "S2_matter_addressed", "S3_hold_line",
          "S4_concede_by_letter", "S5_other_slippage"]
BINARIES = ["thirteen_conceded", "register_legal", "formula_absent"]

# Refuter outcomes: (label, survived_or_partial, proposed shifts as deltas)
# A shift is applied at HALF the proposed magnitude (refuter = one voice).
REFUTERS = [
    ("S2-overpriced (survived)", True,
     {"S2_matter_addressed": -9, "S1_documents_only": +6, "S5_other_slippage": +3}),
    ("thirteen-timing (partial: direction holds, timing risk real)", True,
     {"thirteen_conceded": -12, "S5_other_slippage": +5, "S1_documents_only": -5}),
    ("S3-underpriced (survived: pending-MSH maintenance letter is S3-shaped)", True,
     {"S3_hold_line": +4, "S5_other_slippage": -3, "S1_documents_only": -1,
      "thirteen_conceded": -4}),
    ("taxonomy-gap (survived: concede-plus-formula hybrid fits no shape)", True,
     {"S5_other_slippage": +11, "S1_documents_only": -9, "S2_matter_addressed": -2,
      "thirteen_conceded": +6}),
]

# Scoring resolution adopted from refute:4 — S1 is scored as the CLEAN
# documents-only letter (no formula, no fresh reservation). A letter that
# concedes the tabs but restates the formula / adds a footing reservation
# scores S5 (hybrid sub-branch). formula_absent is scored jointly with the
# shape, never in isolation.

E23 = {"S1_documents_only": 50, "S2_matter_addressed": 37.5, "S3_hold_line": 8,
       "S4_concede_by_letter": 6, "S5_other_slippage": 0,
       "thirteen_conceded": 85, "register_legal": 70, "formula_absent": 68}

def median(xs):
    s = sorted(xs); n = len(s)
    return s[n//2] if n % 2 else (s[n//2-1]+s[n//2])/2

def trimmed_mean(xs):
    s = sorted(xs)[1:-1]
    return sum(s)/len(s)

def extremize(p, d=1.3):
    p = min(max(p, 1e-6), 1-1e-6)
    num = p**d
    return 100 * num / (num + (1-p)**d)

def aggregate():
    cols = list(zip(*[PANEL[l] for l in LENSES]))
    med = {k: median(cols[i]) for i, k in enumerate(SHAPES + BINARIES)}
    trm = {k: trimmed_mean(cols[i]) for i, k in enumerate(SHAPES + BINARIES)}
    # blend median and trimmed mean 50/50 (they agree within noise; the blend
    # keeps information from both without letting either extreme lens dominate)
    agg = {k: (med[k]+trm[k])/2 for k in med}
    # extremize binaries only
    for b in BINARIES:
        agg[b] = extremize(agg[b]/100)
    # refuter updates at half strength
    for label, survived, shifts in REFUTERS:
        if not survived: continue
        for k, dv in shifts.items():
            agg[k] = agg[k] + dv/2
    # normalise the categorical
    tot = sum(agg[s] for s in SHAPES)
    for s in SHAPES:
        agg[s] = round(100*agg[s]/tot, 1)
    for b in BINARIES:
        agg[b] = round(agg[b], 1)
    return med, trm, agg

def brier_binary(p, outcome):      # p in [0,100], outcome bool
    return round(((p/100) - (1 if outcome else 0))**2, 4)

def brier_multi(dist, winner):     # dist: {shape: p}, winner: shape key
    return round(sum(((dist[s]/100) - (1 if s == winner else 0))**2 for s in SHAPES), 4)

if __name__ == "__main__":
    med, trm, agg = aggregate()
    if len(sys.argv) > 1 and sys.argv[1] == "score":
        winner = {"S1": SHAPES[0], "S2": SHAPES[1], "S3": SHAPES[2],
                  "S4": SHAPES[3], "S5": SHAPES[4]}[sys.argv[2]]
        args = dict(zip(sys.argv[3::2], sys.argv[4::2]))
        thirteen = args.get("--thirteen", "y") == "y"
        register = args.get("--register", "legal") == "legal"
        formula  = args.get("--formula", "absent") == "absent"
        print("MULTICLASS BRIER (shape):")
        print(f"  E23 solo : {brier_multi(E23, winner)}")
        print(f"  E24 panel: {brier_multi(agg, winner)}")
        print("BINARY BRIER:")
        for name, p23, p24, out in [
            ("thirteen_conceded", E23["thirteen_conceded"], agg["thirteen_conceded"], thirteen),
            ("register_legal",    E23["register_legal"],    agg["register_legal"],    register),
            ("formula_absent",    E23["formula_absent"],    agg["formula_absent"],    formula)]:
            print(f"  {name:18s} E23 {brier_binary(p23,out):.4f}  E24 {brier_binary(p24,out):.4f}")
        sys.exit(0)
    print(json.dumps({"median": med, "trimmed_mean": {k: round(v,1) for k,v in trm.items()},
                      "final_refuter_adjusted": agg}, indent=2))
