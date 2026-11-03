"""WC/2024/227 - civil claim against MSH: Monte Carlo of the total recovery (16 Oct 2026).
INTERNAL planning model, not advice. Every input is an assumption, stated here so it can be argued with.
Earnings from the payslips: $44.4618/h, 76 h a fortnight base; shift penalties lift gross ~10-15%.
Damages for economic loss are on NET (after-tax) earnings. Future loss uses 5% present-value tables.
"""
import random, statistics as st
random.seed(16102026)
N = 100_000
NET_WEEK = 1320.0            # approx net weekly earnings at full-time incl. average penalties
YEARS_LEFT = (30, 32)        # age ~35 to 67
def pv_weeks(years, r=0.05): return 52 * (1 - (1 + r) ** -years) / r

def run(p_appeal, p_civil, loss_mode):
    out, gross_only = [], []
    for _ in range(N):
        appeal = random.random() < p_appeal
        stat = random.uniform(55_000, 150_000) if appeal else 0.0          # WorkCover benefits (repo range)
        if not appeal or random.random() >= random.uniform(*p_civil):
            out.append((stat, 0.0, stat)); continue
        L = random.triangular(0.15, 0.60, loss_mode)                       # lasting loss of earning capacity
        vic = random.uniform(0.15, 0.25)                                   # vicissitudes discount
        fel = L * NET_WEEK * pv_weeks(random.uniform(*YEARS_LEFT)) * (1 - vic)
        past = random.gauss(115_000, 15_000)                               # past economic loss incl. 2024 periods
        sup = 0.12 * (fel + past)                                          # superannuation
        gd = random.triangular(15_000, 55_000, 30_000)                     # general damages (ISV scale, unverified)
        med = random.uniform(15_000, 40_000)                               # future treatment
        assessed = fel + past + sup + gd + med
        settle = assessed * random.uniform(0.55, 0.85)                     # settlement discount for liability risk
        total = max(settle, stat)                                          # total recovery includes statutory (s 270)
        out.append((total, total - stat, stat))
    return out

def report(label, res):
    tot = sorted(r[0] for r in res)
    q = lambda p: tot[int(p * (len(tot) - 1))]
    print(f"\n{label}")
    print(f"  median total ${q(0.5):,.0f} | middle half ${q(0.25):,.0f} - ${q(0.75):,.0f} | top 10% above ${q(0.9):,.0f}")
    for t in (350_000, 500_000, 1_000_000):
        print(f"  chance total >= ${t:,.0f}: {sum(x >= t for x in tot)/len(tot):.0%}")
    succ = [r for r in res if r[1] > 0]
    if succ:
        s = sorted(r[0] for r in succ)
        print(f"  IF the civil claim pays: median total ${s[len(s)//2]:,.0f}; middle half ${s[len(s)//4]:,.0f} - ${s[3*len(s)//4]:,.0f}")
        inhand = sorted((r[1] * 0.78) + max(r[2] - 65_000, 0) * 0.85 for r in succ)   # less ~22% legal costs; IP debt ~65k; tax on weekly comp
        print(f"  IF the civil claim pays, in your hands roughly: median ${inhand[len(inhand)//2]:,.0f}; middle half ${inhand[len(inhand)//4]:,.0f} - ${inhand[3*len(inhand)//4]:,.0f}")

report("A. Doctors support ongoing partial incapacity (loss mode 40%), civil success 70-80% if appeal won", run(0.85, (0.70, 0.80), 0.40))
report("B. Same, but stronger: loss mode 50%, civil success 75-85%", run(0.85, (0.75, 0.85), 0.50))
report("C. Cautious: loss mode 25%, civil success 60-70%", run(0.85, (0.60, 0.70), 0.25))
