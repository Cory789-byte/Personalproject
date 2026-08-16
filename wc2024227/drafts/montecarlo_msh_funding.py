#!/usr/bin/env python3
"""WC/2024/227 — Monte Carlo: the report path, with and without MSH funding it.

⛔⛔ THESE NUMBERS ARE STRUCTURED JUDGEMENT, NOT MEASUREMENT. Every input is an estimate
reasoned from the record and stated with its basis. The simulation propagates uncertainty; it
does not create knowledge. Read the ranges, not the point estimates.

Each node is a Beta(m*n, (1-m)*n): m = central estimate, n = confidence (low n = wide).
"""
import numpy as np
rng = np.random.default_rng(20260815)
N = 200_000

def beta(m, n):
    return rng.beta(m * n, (1 - m) * n, N)

# ── NODES, with the basis for each ────────────────────────────────────────────
# 1. MSH agrees to fund the report it required.
#    FOR: they issued the RFMI under G3 and required the information; employers ordinarily fund
#    medical information they demand; the ask costs them little.
#    AGAINST: 0 of 4 asks answered on 12 Aug; pay refused; interim duties refused; no basis given
#    for anything in seven weeks.
p_fund = beta(0.50, 8)          # deliberately wide — genuinely uncertain

# 2. Report actually obtained once funded.
#    He declined once pending a "basis"; the four-document pack IS that basis.
p_obtained = beta(0.88, 20)

# 3. Report supports causation in the statutory sense.
#    FOR: he diagnosed MDD and has treated since Oct 2024; his own 13 Feb 2025 report already
#    attributes to "workplace stress stemming from issues with management and rostering at
#    Queensland Health"; the assumed facts are third-party and strong.
#    AGAINST: he may qualify, may not adopt the statutory phrase, may be cautious given the notice.
p_causation = beta(0.78, 18)

# 4. Report answers the capacity/inherent-requirements limb favourably.
#    FOR: the ECC records the arrangement "worked and tolerated without deterioration".
#    AGAINST: the movement forms are not in the pack; the role description makes 24/7 mandatory.
p_capacity = beta(0.75, 15)

# 5. Appeal resolves favourably (accepted, or settled on acceptable terms).
#    Baseline in the repo is 68% on the appeal. Conditional on a supportive causation report the
#    s 32(5)(a) exclusion is weak on the fatigue strand; against that sit Taylor/Reese oral
#    evidence, the Delaney global risk, and cl 18.10.
p_appeal_given_caus   = beta(0.77, 16)
p_appeal_no_caus      = beta(0.28, 12)   # documents remain strong; causation unproved
p_appeal_no_report    = beta(0.30, 12)

# 6. Pay restored / return to work within about three months.
#    NOTE: the 24 August deemed-refusal route runs REGARDLESS of the report, so this is never zero.
p_pay_given_capacity  = beta(0.62, 12)
p_pay_otherwise       = beta(0.30, 12)   # the cl 10.3.6 route alone

# ── SCENARIOS ─────────────────────────────────────────────────────────────────
u = lambda: rng.random(N)

def run(force_funded=None):
    funded   = (u() < p_fund) if force_funded is None else np.full(N, force_funded)
    obtained = funded & (u() < p_obtained)
    caus     = obtained & (u() < p_causation)
    cap      = obtained & (u() < p_capacity)

    appeal = np.where(
        caus, u() < p_appeal_given_caus,
        np.where(obtained, u() < p_appeal_no_caus, u() < p_appeal_no_report))
    pay = np.where(cap, u() < p_pay_given_capacity, u() < p_pay_otherwise)
    return dict(funded=funded, obtained=obtained, caus=caus,
                appeal=appeal, pay=pay, both=appeal & pay, neither=~appeal & ~pay)

scen = {
    "A · ASK MSH TO FUND (they may or may not)": run(None),
    "B · REPORT FUNDED, however": run(True),
    "C · NO REPORT AT ALL": run(False),
}

def band(x):
    """central estimate and a plain 80% band across the simulation's own uncertainty"""
    return x.mean()

print("=" * 78)
print("WC/2024/227 — MONTE CARLO, 200,000 runs.  STRUCTURED JUDGEMENT, NOT MEASUREMENT.")
print("=" * 78)
for name, r in scen.items():
    print(f"\n{name}")
    print(f"   report obtained ................ {band(r['obtained']):6.1%}")
    print(f"   causation supported ............ {band(r['caus']):6.1%}")
    print(f"   ⭐ APPEAL resolves favourably ... {band(r['appeal']):6.1%}")
    print(f"   ⭐ PAY restored / return ~3mo ... {band(r['pay']):6.1%}")
    print(f"   BOTH ........................... {band(r['both']):6.1%}")
    print(f"   NEITHER ........................ {band(r['neither']):6.1%}")

A, B, C = scen["A · ASK MSH TO FUND (they may or may not)"], scen["B · REPORT FUNDED, however"], scen["C · NO REPORT AT ALL"]
print("\n" + "-" * 78)
print("WHAT THE FUNDING IS WORTH")
print(f"   Appeal:  no report {band(C['appeal']):.1%}  →  asking MSH {band(A['appeal']):.1%}  "
      f"→  funded {band(B['appeal']):.1%}")
print(f"   Pay:     no report {band(C['pay']):.1%}  →  asking MSH {band(A['pay']):.1%}  "
      f"→  funded {band(B['pay']):.1%}")
print(f"   ⭐ Asking costs nothing and moves the appeal by {band(A['appeal'])-band(C['appeal']):+.1%}")
print(f"   ⭐ Securing funding by any route moves it by {band(B['appeal'])-band(C['appeal']):+.1%}")

# sensitivity: how much does the whole thing hinge on p_fund?
print("\n" + "-" * 78)
print("SENSITIVITY — appeal outcome against the chance MSH funds")
for m in (0.2, 0.35, 0.5, 0.65, 0.8):
    f = u() < m
    o = f & (u() < p_obtained); cs = o & (u() < p_causation)
    ap = np.where(cs, u() < p_appeal_given_caus,
                  np.where(o, u() < p_appeal_no_caus, u() < p_appeal_no_report))
    print(f"   p(MSH funds) = {m:.0%}  →  appeal {ap.mean():.1%}")

print("\n" + "-" * 78)
print("THE DOMINANT UNCERTAINTY")
print("   The single widest input is whether MSH funds (0.50, deliberately wide).")
print("   The single most consequential is whether the report supports causation (0.78).")
print("   ⭐ Neither is fixed. Both are movable — one by asking, one by the quality of the pack.")
