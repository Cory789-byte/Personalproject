"""
WC/2024/227 employment track — Monte Carlo over strategy choices.
Priors are JUDGEMENT calibrated to the documentary record in this repo, not measured
frequencies. Ranges are blue(high)/red(low) per the full-picture method.
"""
import numpy as np
rng = np.random.default_rng(20260731)
N = 200_000

def beta_from_range(lo, hi, n, disp):
    """Draw in [lo,hi] shaped by a shared decision-maker disposition (0=hostile,1=receptive)."""
    span = hi - lo
    # disposition shifts within the range; noise adds independent uncertainty
    base = lo + span * (0.30 + 0.55 * disp)
    noise = rng.normal(0, span * 0.16, n)
    return np.clip(base + noise, 0.01, 0.99)

# ---- shared disposition of the decision-maker (correlates all blocks) ----
disp = rng.beta(5, 5, N)

# ---- SUBSTANTIVE BLOCKS: blue(high) / red(low) ----
BLOCKS = {
 # name                          blue   red    what it is
 "B1_no_authority_exclusion":  (0.88, 0.55),  # nothing authorised keeping him out
 "B2_direction_unreasonable":  (0.85, 0.45),  # reasonableness limb fails
 "B3_leave_unlawful":          (0.80, 0.38),  # accrued/sick-no-pay/IP debiting
 "B4_no_psychosocial_assmt":   (0.85, 0.35),  # the assessment does not exist
 "B5_consultation_breach":     (0.82, 0.50),  # WHS s47/48 not complied with
}
B = {k: beta_from_range(lo, hi, N, disp) for k, (hi, lo) in
     ((k, (v[0], v[1])) for k, v in BLOCKS.items())}

# ---- STRATEGY VECTOR ----
# Each decision returns (credibility_delta, direct_effect_multipliers)
STRATS = {
 "DISCIPLINED": dict(respond="early", psychosocial=True, scope_consent=True,
                     name_delegate=True, motive=False, metadata=False,
                     bullying=False, reportA="tight", mention_clean=True,
                     book_first=True, extension=True),
 "AGGRESSIVE":  dict(respond="early", psychosocial=True, scope_consent=True,
                     name_delegate=True, motive=True,  metadata=True,
                     bullying=True,  reportA="loose", mention_clean=False,
                     book_first=True, extension=True),
 "MINIMAL":     dict(respond="early", psychosocial=False, scope_consent=False,
                     name_delegate=False, motive=False, metadata=False,
                     bullying=False, reportA="tight", mention_clean=True,
                     book_first=True, extension=True),
 "SILENT":      dict(respond="none", psychosocial=False, scope_consent=False,
                     name_delegate=False, motive=False, metadata=False,
                     bullying=False, reportA="tight", mention_clean=True,
                     book_first=False, extension=False),
 "LATE":        dict(respond="late", psychosocial=True, scope_consent=True,
                     name_delegate=True, motive=False, metadata=False,
                     bullying=False, reportA="tight", mention_clean=True,
                     book_first=True, extension=False),
}

def credibility(s):
    """Credibility index 0-1. The central mediating variable."""
    c = rng.beta(7, 3, N)               # baseline: strong documentary position
    if s["respond"] == "none": c *= rng.uniform(0.30, 0.45, N)
    if s["respond"] == "late": c *= rng.uniform(0.72, 0.88, N)
    if s["motive"]:            c *= rng.uniform(0.55, 0.75, N)   # unprovable allegations
    if s["metadata"]:          c *= rng.uniform(0.80, 0.93, N)   # reads as gotcha + burns capability
    if s["bullying"]:          c *= rng.uniform(0.70, 0.88, N)   # invites RMA defence, shifts register
    if not s["mention_clean"]: c *= rng.uniform(0.55, 0.78, N)   # conflating tracks before Dwyer
    if s["psychosocial"]:      c *= rng.uniform(1.03, 1.12, N)   # asks them to do a mandatory thing
    if s["extension"]:         c *= rng.uniform(1.02, 1.08, N)   # engaged, reasonable
    return np.clip(c, 0.02, 1.0)

def simulate(s):
    c = credibility(s)
    # substantive blocks are only as persuasive as the person advancing them
    eff = {k: v * (0.45 + 0.55 * c) for k, v in B.items()}

    # ---- O1: back at work within 8 weeks ----
    p_ret = 0.10 + 0.42*eff["B2_direction_unreasonable"] + 0.20*eff["B1_no_authority_exclusion"]
    if s["respond"] == "none": p_ret *= 0.35
    if s["psychosocial"]:      p_ret *= rng.uniform(1.05, 1.20, N)   # forces the assessment question
    if s["name_delegate"]:     p_ret *= rng.uniform(1.03, 1.14, N)   # removes the conflicted blocker
    if s["book_first"]:        p_ret *= rng.uniform(1.02, 1.10, N)   # no delay vector
    ret = rng.random(N) < np.clip(p_ret, 0, 0.97)

    # ---- O2: pay / leave restored (incl. backpay) ----
    p_pay = 0.06 + 0.55*eff["B3_leave_unlawful"] * (0.55 + 0.45*eff["B1_no_authority_exclusion"])
    if s["respond"] == "none": p_pay *= 0.25
    if s["extension"]:         p_pay *= rng.uniform(1.02, 1.09, N)
    pay = rng.random(N) < np.clip(p_pay, 0, 0.95)

    # ---- O3: settlement position in WC/2024/227 improves ----
    p_set = 0.12 + 0.40*c + 0.25*eff["B4_no_psychosocial_assmt"]
    if s["reportA"] == "loose": p_set *= rng.uniform(0.62, 0.82, N)  # causation opinion to the Regulator
    if not s["mention_clean"]:  p_set *= rng.uniform(0.60, 0.82, N)
    if s["motive"]:             p_set *= rng.uniform(0.70, 0.88, N)
    setl = rng.random(N) < np.clip(p_set, 0, 0.96)

    # ---- O4: adverse event (decision made against him / disciplinary escalation) ----
    p_adv = 0.10 + 0.35*(1-c)
    if s["respond"] == "none":  p_adv += 0.30
    if s["respond"] == "late":  p_adv += 0.08
    if not s["extension"]:      p_adv += 0.10
    if s["bullying"]:           p_adv += 0.06
    adv = rng.random(N) < np.clip(p_adv, 0, 0.95)

    return dict(cred=c.mean(), ret=ret.mean(), pay=pay.mean(),
                setl=setl.mean(), adv=adv.mean(),
                cred_lo=np.percentile(c,10), cred_hi=np.percentile(c,90))

print("="*94)
print(f"{'STRATEGY':<14}{'Credibility':>13}{'Back@work':>12}{'Pay restored':>14}"
      f"{'Settle+':>10}{'ADVERSE':>10}")
print("="*94)
res = {}
for name, s in STRATS.items():
    r = simulate(s); res[name] = r
    print(f"{name:<14}{r['cred']:>12.2f} {r['ret']:>11.1%} {r['pay']:>13.1%}"
          f" {r['setl']:>9.1%} {r['adv']:>9.1%}")
print("="*94)

# ---- TORNADO: single-variable deviations from DISCIPLINED ----
print("\nTORNADO — flipping ONE choice away from DISCIPLINED (Δ percentage points)")
print("-"*94)
base = res["DISCIPLINED"]
flips = [("do not respond at all", dict(respond="none")),
         ("respond after 7 Aug", dict(respond="late")),
         ("no extension sought", dict(extension=False)),
         ("raise motive theories", dict(motive=True)),
         ("raise employment at the mention", dict(mention_clean=False)),
         ("use the word bullying", dict(bullying=True)),
         ("Report A covers causation", dict(reportA="loose")),
         ("raise metadata timings", dict(metadata=True)),
         ("omit psychosocial request", dict(psychosocial=False)),
         ("omit named delegate", dict(name_delegate=False)),
         ("ask costs before booking", dict(book_first=False))]
rows = []
for label, ch in flips:
    s = dict(STRATS["DISCIPLINED"]); s.update(ch)
    r = simulate(s)
    rows.append((label, (r['ret']-base['ret'])*100, (r['pay']-base['pay'])*100,
                 (r['setl']-base['setl'])*100, (r['adv']-base['adv'])*100))
rows.sort(key=lambda x: x[4], reverse=True)
print(f"{'CHOICE':<36}{'Back@work':>11}{'Pay':>9}{'Settle':>9}{'ADVERSE':>10}")
for l, a, b_, c_, d in rows:
    print(f"{l:<36}{a:>+10.1f} {b_:>+8.1f} {c_:>+8.1f} {d:>+9.1f}")
print("-"*94)
print(f"\nDISCIPLINED credibility 80% interval: {base['cred_lo']:.2f} – {base['cred_hi']:.2f}")
print(f"N = {N:,} trials.  Priors are judgement calibrated to the record, not frequencies.")
