#!/usr/bin/env python3
"""Full-matter Monte Carlo — 4 Aug 2026 state.
Calibrated off the 3 Aug corrected-test run (employment 48/66, pay 59, appeal 36/70),
with only genuine deltas applied. Deterministic seed for reproducibility."""
import random
random.seed(20260804)
N = 200_000

def B(p): return random.random() < p

emp_strict = emp_fav = pay = 0
appeal_win = appeal_fav = 0
overall_fav = 0
adverse_attempt = adverse_survived = 0
assessment_commissioned = 0
settle_any = 0
weeks = []
deemed_refusal = 0

for _ in range(N):
    # ---------- EMPLOYMENT TRACK ----------
    # MSH engagement posture by 17 Aug (Stage 1/2 window)
    r = random.random()
    if r < 0.45:   posture = "engage"      # substantive: meeting/answers/legal-led resolution
    elif r < 0.80: posture = "procedural"  # holding letters, no substance
    else:          posture = "silence"

    # Engagement by him reduces the "non-cooperation" narrative (bookings made,
    # direct billing, forms allocated). This is the 4 Aug delta.
    cooperation_shield = True

    # Adverse action attempt (incapacity decision / dismissal) in Aug-Sep
    p_adverse = {"engage": 0.10, "procedural": 0.22, "silence": 0.30}[posture]
    if cooperation_shield: p_adverse *= 0.72   # engaged + documented + CE on notice + s89
    adverse = B(p_adverse)
    if adverse: adverse_attempt += 1

    # If adverse: challenge prospects (IR Act s 306 reverse onus, no instrument,
    # protected acts, CE knowledge documented)
    challenge_win = B(0.70) if adverse else False
    if adverse and challenge_win: adverse_survived += 1

    # cl 10.3.6 decision by 24 Aug
    r = random.random()
    if r < 0.28:   cl103 = "grant"     # full/partial grant of the 0.6 request
    elif r < 0.52: cl103 = "refuse"    # written refusal (reviewable, dated)
    else:          cl103 = "deemed"    # silence → s 29 deemed refusal
    if cl103 == "deemed": deemed_refusal += 1

    # Psychosocial assessment actually commissioned
    p_assess = {"engage": 0.55, "procedural": 0.25, "silence": 0.10}[posture]
    if B(p_assess): assessment_commissioned += 1

    # Return to work / restoration
    p_restore = {"engage": 0.46, "procedural": 0.24, "silence": 0.14}[posture]
    if cl103 == "grant": p_restore = min(0.85, p_restore + 0.24)
    if adverse and not challenge_win: p_restore = 0.02
    if adverse and challenge_win: p_restore = min(p_restore, 0.55)
    restored = B(p_restore)

    # Pay recovered (back-pay / leave re-credit / forward pay)
    p_pay = 0.22
    if restored: p_pay = 0.72
    if cl103 in ("grant",): p_pay += 0.08
    if adverse and challenge_win: p_pay = max(p_pay, 0.65)   # compensation limb
    p_pay = min(p_pay, 0.85)
    paid = B(p_pay)

    # Employment settlement (deed resolving employment, incl. exit on terms)
    p_settle_emp = {"engage": 0.26, "procedural": 0.20, "silence": 0.14}[posture]
    if adverse: p_settle_emp += 0.18
    settled_emp = (not restored) and B(min(p_settle_emp, 0.50))

    strict = restored or (adverse and challenge_win)
    favourable = strict or settled_emp or paid

    # ---------- APPEAL TRACK (WC/2024/227) ----------
    # 64G / disclosure enlargement after 7 Aug mention
    disclosure = B(0.75)
    # Report B obtained and of quality (needs attendance + funding + scope)
    reportB = B(0.86)
    # Causation on the CORRECT test: employment "a significant contributing factor"
    causation = B(0.84 if reportB else 0.66)
    # s 32(5) RMA — the contested centre. Manner defects + admitted reviewing-officer
    # findings + (if it lands) the unmanaged-risk record.
    p_rma = 0.40
    if disclosure: p_rma += 0.07
    if reportB: p_rma += 0.05
    if assessment_commissioned: p_rma += 0.03
    rma_survives = B(min(p_rma, 0.60))
    # Tribunal/evidentiary variance (credit, respondent expert, hearing risk)
    hearing_risk = B(0.82)

    won_hearing = causation and rma_survives and hearing_risk

    # Settlement of the appeal
    p_settle_app = 0.36
    if disclosure: p_settle_app += 0.09
    if reportB: p_settle_app += 0.05
    if favourable: p_settle_app += 0.04          # coupling: employment resolution pulls
    settled_app = (not won_hearing) and B(min(p_settle_app, 0.58))

    app_fav = won_hearing or settled_app

    # ---------- TIMING (weeks to substantive resolution of at least one track) ----------
    w = 6 if cl103 == "grant" else 10
    if posture == "silence": w += 6
    if adverse: w += 8
    if settled_app or settled_emp: w = min(w + 4, 34)
    if won_hearing: w = max(w, 30)
    weeks.append(w + random.randint(-2, 4))

    emp_strict += strict
    emp_fav += favourable
    pay += paid
    appeal_win += won_hearing
    appeal_fav += app_fav
    settle_any += (settled_emp or settled_app)
    overall_fav += (favourable or app_fav)

pct = lambda x: round(100*x/N, 1)
weeks.sort()
print(f"Employment — strict (restored or adverse-action challenge won): {pct(emp_strict)}%")
print(f"Employment — favourable incl. settlement/payment:               {pct(emp_fav)}%")
print(f"Pay recovered (back-pay / re-credit / forward):                 {pct(pay)}%")
print(f"Appeal — win at contested hearing:                              {pct(appeal_win)}%")
print(f"Appeal — favourable incl. settlement:                           {pct(appeal_fav)}%")
print(f"AT LEAST ONE TRACK FAVOURABLE:                                  {pct(overall_fav)}%")
print(f"Some settlement occurs (either track):                          {pct(settle_any)}%")
print("---- risk / process nodes ----")
print(f"Adverse action ATTEMPTED (Aug-Sep):                             {pct(adverse_attempt)}%")
print(f"  of which defeated on challenge:                               {round(100*adverse_survived/max(adverse_attempt,1),1)}%")
print(f"cl 10.3.6 ends in DEEMED REFUSAL (silence to 24 Aug):           {pct(deemed_refusal)}%")
print(f"Psychosocial assessment actually commissioned:                  {pct(assessment_commissioned)}%")
print("---- timing (weeks to first substantive resolution) ----")
print(f"P10 {weeks[N//10]}w · median {weeks[N//2]}w · P90 {weeks[9*N//10]}w")
