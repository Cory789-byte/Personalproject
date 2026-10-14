"""Why the voice is steady: pitch-loudness coupling, within-phrase pitch movement and pitch range
for each speaker in the QPS interview, the 2 Feb 2026 court hearing and the 7 Aug 2026 mention.
Usage: python -I steady_voice.py REPO_ROOT. Descriptive only; not clinical."""
import json, math, statistics as st, sys
import numpy as np
R = sys.argv[1]; C = R + '/qps_court_audio/2026-02-02_BMC_trial_stood_down/data'
def stats(rows, f0key='f0_med', dbkey='db_mean'):
    f0b = np.median([r['pros'][f0key] for r in rows]); dbb = np.median([r['pros'][dbkey] for r in rows])
    stv = np.array([12*math.log2(r['pros'][f0key]/f0b) for r in rows]); dbv = np.array([r['pros'][dbkey]-dbb for r in rows])
    k = max(1, len(rows)//5); top = np.argsort(-dbv)[:k]
    sd = [r['pros'].get('f0_sd_st', 0) for r in rows]
    return (f"n={len(rows)} f0 {f0b:.0f} Hz | r(pitch,level)={np.corrcoef(stv,dbv)[0,1]:+.2f} | loudest fifth: "
            f"pitch {stv[top].mean():+.2f} st at {dbv[top].mean():+.1f} dB | within-segment f0 SD {st.median(sd):.2f} st | "
            f"segment-to-segment pitch SD {stv.std():.2f} st")
ok = lambda r: r.get('pros') and (r['pros'].get('f0_med') or 0) > 70 and r['end']-r['start'] >= 0.8 and (r['pros'].get('voiced_frac') or 0) >= 0.3
print("== COURT")
cs = json.load(open(f'{C}/court_segs.json'))
for who in ['SHEPHERD', 'MAGISTRATE', 'PROSECUTOR']:
    print(who, stats([r for r in cs if r['spk'] == who and ok(r)]))
t = json.load(open(f'{C}/turns.json'))
for who in ['SHEPHERD', 'MAGISTRATE', 'PROSECUTOR']:
    rr = [x for x in t if x['who'] == who and 2 <= x['dur'] <= 12 and x['range_st'] > 0]
    import re; q = sum(re.sub(r'\[[^]]*\]', '', x['text']).count('?') for x in t if x['who'] == who)
    print(f"  {who}: turns of 2-12 s: n={len(rr)}, median pitch range {st.median([x['range_st'] for x in rr]):.1f} st "
          f"(median length {st.median([x['dur'] for x in rr]):.1f} s); questions asked: {q}")
print("== MENTION")
ms = json.load(open(f'{R}/cognitive_speech/mention_segs.json'))
for who in ['MR SHEPHERD', 'DWYER IC']:
    print(who, stats([r for r in ms if r['spk'] == who and ok(r)]))
print("== INTERVIEW (acoustic clusters: C0 = Cory, C1 = officers)")
iv = [json.loads(l) for l in open(f'{R}/qps_interview_acoustic/bickery.labelled.jsonl')]
for spk, name in [(0, 'C0 Cory'), (1, 'C1 officers')]:
    print(name, stats([r for r in iv if r['spk'] == spk and ok(r)]))
