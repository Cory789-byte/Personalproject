#!/usr/bin/env python3
"""FRAMEWORK VERIFICATION MC — 4 Aug 2026.
Not an outcome model. Tests: which of HIS legal propositions hold, which of THEIR
defences survive, and whether any pay route succeeds. Seeded."""
import random
from collections import Counter
random.seed(40826)
N = 200_000

def B(p): return random.random() < p

# HIS PROPOSITIONS — probability each holds before a tribunal on the current record
PROPS = {
 "P1 ready/willing/able → wages payable (26 Jun–)":      0.72,
 "P2 cl 1.11.4 status quo breached by leave debit":      0.55,   # see red-team RT4
 "P3 cl 1.11.2(a) 24h not met (ADMITTED in writing)":    0.97,
 "P4 no instrument ever identified":                     0.90,
 "P5 s 101 not complied with (if suspension)":           0.88,
 "P6 s 33 8-weeks notice not given (if rec leave)":      0.93,
 "P7 sick leave mischaracterised (certified FIT)":       0.80,
 "P8 ss 47–49 consultation not conducted":               0.78,
 "P9 no psychosocial risk assessment ever (nil return)": 0.69,
 "P10 protected acts engaged + s 306 reverse onus":      0.85,
}

# THEIR DEFENCES — probability each SURVIVES scrutiny on the current record
DEFS = {
 "D1 lawful direction pending medical clearance":        0.30,
 "D2 valid s 101 suspension":                            0.06,
 "D3 leave applied by agreement":                        0.10,   # now refused in writing
 "D4 sick leave properly applicable":                    0.14,
 "D5 s 32(5) reasonable management action (appeal)":     0.45,
 "D6 Stage 1 progressed reasonably":                     0.12,
 "D7 cooperative: funded reports, offered EAP":          0.70,   # partly true, real
 "D8 'no concerns were raised'":                         0.22,
 "D9 incapacity on medical grounds":                     0.38,   # psychiatrist advised against work
 "D10 ECC delay 5 May–3 Jul was HIS delay":              0.55,   # ⭐ their best chronology counter
 "D11 leave applied = benefit not detriment":            0.40,   # ⭐ clever, real
}

prop_hits = Counter(); def_hits = Counter()
pay_route = 0; no_defence = 0; props_held = []
both_strong = 0

for _ in range(N):
    held = {k: B(v) for k, v in PROPS.items()}
    surv = {k: B(v) for k, v in DEFS.items()}
    for k, v in held.items():
        if v: prop_hits[k] += 1
    for k, v in surv.items():
        if v: def_hits[k] += 1

    n_held = sum(held.values())
    props_held.append(n_held)

    # PAY ROUTES — any one succeeding recovers the money
    r_wages  = held["P1 ready/willing/able → wages payable (26 Jun–)"] and not surv["D1 lawful direction pending medical clearance"]
    r_susp   = held["P5 s 101 not complied with (if suspension)"] and not surv["D2 valid s 101 suspension"] and B(0.55)
    r_rec    = held["P6 s 33 8-weeks notice not given (if rec leave)"] and not surv["D3 leave applied by agreement"] and B(0.60)
    r_sick   = held["P7 sick leave mischaracterised (certified FIT)"] and not surv["D4 sick leave properly applicable"] and B(0.55)
    r_status = held["P2 cl 1.11.4 status quo breached by leave debit"] and B(0.50)
    if r_wages or r_susp or r_rec or r_sick or r_status: pay_route += 1

    # Do they hold ANY defence to the exclusion/pay question?
    core_def = surv["D1 lawful direction pending medical clearance"] or surv["D2 valid s 101 suspension"] \
               or surv["D3 leave applied by agreement"] or surv["D4 sick leave properly applicable"]
    if not core_def: no_defence += 1

    # Their two best REAL counters both landing
    if surv["D10 ECC delay 5 May–3 Jul was HIS delay"] and surv["D11 leave applied = benefit not detriment"]:
        both_strong += 1

pct = lambda x: round(100*x/N, 1)
print("=== HIS PROPOSITIONS — probability each holds ===")
for k in PROPS: print(f"  {pct(prop_hits[k]):>5}%  {k}")
print("\n=== THEIR DEFENCES — probability each SURVIVES ===")
for k in DEFS: print(f"  {pct(def_hits[k]):>5}%  {k}")
props_held.sort()
print(f"\nPropositions holding: median {props_held[N//2]} of 10 · P10 {props_held[N//10]} · P90 {props_held[9*N//10]}")
print(f"⭐ AT LEAST ONE PAY ROUTE SUCCEEDS:                {pct(pay_route)}%")
print(f"⭐ THEY HOLD NO SURVIVING CORE DEFENCE:            {pct(no_defence)}%")
print(f"⚠ BOTH their best real counters land (D10+D11):   {pct(both_strong)}%")
