"""Prosecutor turn profile for the 2 Feb 2026 hearing: per-part pitch and level against his own median,
speaking rate, and counts of positional, deferral and own-knowledge phrases.
Usage: python -I prosecutor_profile.py DATA_DIR. Descriptive only: no inference about honesty is drawn from voice."""
import json, math, re, statistics as st, sys
import numpy as np
C = sys.argv[1]
cs = json.load(open(f'{C}/court_segs.json'))
P = [r for r in cs if r['spk'] == 'PROSECUTOR']
good = [r for r in P if (r['pros'].get('f0_med') or 0) > 70]
f0b = np.median([r['pros']['f0_med'] for r in good]); dbb = np.median([r['pros']['db_mean'] for r in good])
print(f"prosecutor baseline f0 {f0b:.0f} Hz, level {dbb:.1f} dB")
for r in P:
    p = r['pros']; f = p.get('f0_med') or 0
    stv = 12*math.log2(f/f0b) if f > 70 else float('nan')
    nw = len(re.sub(r'\[[^]]*\]', '', r['text']).split()); d = r['end']-r['start']
    print(f"{int(r['start']//60):02d}:{r['start']%60:04.1f} {d:5.1f}s {60*nw/max(d,0.1):5.0f}wpm pitch {stv:+5.1f}st level {p['db_mean']-dbb:+5.1f}dB | {r['text'][:110]}")
txt = ' '.join(r['text'] for r in P).lower()
pats = {'for the court to decide/determine': r'for the court to (decide|determine)|court to decide',
        'my position / prosecution position': r"my position|position that prosecution|prosecution's position|position that the prosecution",
        'evidence indicates / witness will': r'evidence indicates|will attest|will be able to speak|made apparent with my evidence|intend on calling',
        "can't / don't / haven't (own knowledge)": r"i can't|i don't|i haven't|not something that i'm able",
        'hedges (I think / I guess / probably / maybe)': r"\bi think\b|\bi guess\b|\bprobably\b|\bmaybe\b",
        'Your Honour': r'your honou?r'}
for k, rx in pats.items():
    print(f"{k}: {len(re.findall(rx, txt))}")
