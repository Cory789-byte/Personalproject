"""Officers v Cory: level, pitch, pitch movement, turn length and response gap across the 66-minute QPS
interview (24 Feb 2025), from bickery.labelled.jsonl. Segments overlapping the 120 s tone grid are removed.
The two officers share one acoustic cluster; a two-component pitch model separates a lower (~97 Hz) and a
higher (~125 Hz) voice. Usage: python -I officer_tone.py REPO_ROOT. Descriptive only."""
import json, math, statistics as st, sys
import numpy as np
from sklearn.mixture import GaussianMixture
R = sys.argv[1]
iv = [json.loads(l) for l in open(f'{R}/qps_interview_acoustic/bickery.labelled.jsonl')]
beeps = [29.9 + 120.0038 * k for k in range(33)]
def clean(s):
    p = s['pros']; d = s['end'] - s['start']
    return (p.get('f0_med') or 0) and 70 < p['f0_med'] < 200 and (p.get('voiced_frac') or 0) >= 0.25 and d >= 0.8 \
        and not any(s['start'] - 0.3 <= b <= s['end'] + 0.3 for b in beeps)
C1 = [s for s in iv if s['spk'] == 1 and clean(s)]
C0 = [s for s in iv if s['spk'] == 0 and clean(s)]
x = np.log2(np.array([s['pros']['f0_med'] for s in C1])).reshape(-1, 1) * 12
for k in (1, 2):
    g = GaussianMixture(k, random_state=0).fit(x)
    print(f"officers' pitch, {k} component(s): BIC {g.bic(x):.0f}; means {[round(2**(m/12),1) for m in g.means_.ravel()]} Hz")
g2 = GaussianMixture(2, random_state=0).fit(x)
lab = g2.predict(x); lo = int(np.argmin(g2.means_.ravel()))
sep = abs(np.diff(g2.means_.ravel()))[0] / np.sqrt(g2.covariances_.ravel()).mean()
print(f"separation (difference in means / average sd): {sep:.2f}")
T0, T1 = 0, max(s['end'] for s in iv)
bins = [(0, 480), (480, 1200), (1200, 1800), (1800, 2400), (2400, 3000), (3000, 3700)]
def rel(rows, f0b, dbb):
    return [12 * math.log2(s['pros']['f0_med'] / f0b) for s in rows], [s['pros']['db_mean'] - dbb for s in rows]
f0b1 = np.median([s['pros']['f0_med'] for s in C1]); db1 = np.median([s['pros']['db_mean'] for s in C1])
f0b0 = np.median([s['pros']['f0_med'] for s in C0]); db0 = np.median([s['pros']['db_mean'] for s in C0])
print(f"\nbaselines: officers {f0b1:.0f} Hz {db1:.1f} dB | Cory {f0b0:.0f} Hz {db0:.1f} dB")
print("window      | OFFICERS talk-s  level  pitch  pitch-move  low-voice share | CORY talk-s  level  pitch  pitch-move")
for a, b in bins:
    o = [s for s in C1 if a <= s['start'] < b]; c = [s for s in C0 if a <= s['start'] < b]
    if not o or not c:
        continue
    os_, od = rel(o, f0b1, db1); cs, cd = rel(c, f0b0, db0)
    olo = [l for s, l in zip(C1, lab) if a <= s['start'] < b]
    share_lo = 100 * np.mean([l == lo for l in olo]) if olo else float('nan')
    print(f"{a//60:02d}-{b//60:02d} min   | {sum(s['end']-s['start'] for s in o):7.0f} {np.median(od):+6.1f} {np.median(os_):+6.1f} "
          f"{np.median([s['pros'].get('f0_sd_st',0) for s in o]):9.2f} {share_lo:10.0f}%    | {sum(s['end']-s['start'] for s in c):7.0f} "
          f"{np.median(cd):+6.1f} {np.median(cs):+6.1f} {np.median([s['pros'].get('f0_sd_st',0) for s in c]):9.2f}")
# slopes per officer component
for name, idx in [('lower-pitched officer voice', lo), ('higher-pitched officer voice', 1 - lo)]:
    rows = [s for s, l in zip(C1, lab) if l == idx]
    t = np.array([s['start'] for s in rows]) / 600
    d = np.array([s['pros']['db_mean'] for s in rows]); f = 12 * np.log2(np.array([s['pros']['f0_med'] for s in rows]) / np.median([s['pros']['f0_med'] for s in rows]))
    sd = np.array([s['pros'].get('f0_sd_st', 0) for s in rows])
    print(f"{name}: n={len(rows)}, median {np.median([s['pros']['f0_med'] for s in rows]):.0f} Hz | level slope {np.polyfit(t,d,1)[0]:+.2f} dB/10min "
          f"(r={np.corrcoef(t,d)[0,1]:+.2f}) | pitch slope {np.polyfit(t,f,1)[0]:+.2f} st/10min | pitch-movement slope {np.polyfit(t,sd,1)[0]:+.2f} st/10min")
for name, rows in [('ALL officers', C1), ('Cory', C0)]:
    t = np.array([s['start'] for s in rows]) / 600; d = np.array([s['pros']['db_mean'] for s in rows])
    f = 12 * np.log2(np.array([s['pros']['f0_med'] for s in rows]) / np.median([s['pros']['f0_med'] for s in rows]))
    sd = np.array([s['pros'].get('f0_sd_st', 0) for s in rows])
    print(f"{name}: level slope {np.polyfit(t,d,1)[0]:+.2f} dB/10min (r={np.corrcoef(t,d)[0,1]:+.2f}) | pitch slope {np.polyfit(t,f,1)[0]:+.2f} st/10min (r={np.corrcoef(t,f)[0,1]:+.2f}) | pitch-movement slope {np.polyfit(t,sd,1)[0]:+.2f}")
# turn structure over time: officers' turn length and response gap after Cory
segs = sorted([s for s in iv if s['spk'] in (0, 1)], key=lambda s: s['start'])
turns = []; cur = None
for s in segs:
    if cur and s['spk'] == cur['spk'] and s['start'] - cur['end'] < 1.5:
        cur['end'] = s['end']
    else:
        cur = {'spk': s['spk'], 'start': s['start'], 'end': s['end']}; turns.append(cur)
print("\nwindow      | officers' median turn (s) | officers' median gap after you (s) | your median turn (s) | your gap after them (s)")
for a, b in bins:
    ot = [t['end'] - t['start'] for t in turns if t['spk'] == 1 and a <= t['start'] < b]
    ct = [t['end'] - t['start'] for t in turns if t['spk'] == 0 and a <= t['start'] < b]
    og = [y['start'] - x['end'] for x, y in zip(turns, turns[1:]) if x['spk'] == 0 and y['spk'] == 1 and a <= y['start'] < b]
    cg = [y['start'] - x['end'] for x, y in zip(turns, turns[1:]) if x['spk'] == 1 and y['spk'] == 0 and a <= y['start'] < b]
    if ot and ct:
        print(f"{a//60:02d}-{b//60:02d} min   | {st.median(ot):6.1f}                     | {st.median(og) if og else float('nan'):6.2f}                            | {st.median(ct):6.1f}            | {st.median(cg) if cg else float('nan'):6.2f}")
