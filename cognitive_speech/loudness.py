"""Loudness (intensity) per speaker across the QPS interview (Feb 2025), the court hearing (2 Feb 2026)
and the QIRC mention (7 Aug 2026). Everything is relative to each speaker's own median in that
recording: absolute dB is not comparable across microphones or between speakers on different mics.

Usage: python -I loudness.py REPO_ROOT [COURT_AUDIO]
COURT_AUDIO (not committed) enables the within-turn first-third v last-third measure for the court.
Descriptive only; not clinical.
"""
import json, math, re, statistics as st, sys
import numpy as np

R = sys.argv[1]
AUDIO = sys.argv[2] if len(sys.argv) > 2 else None
C = R + '/qps_court_audio/2026-02-02_BMC_trial_stood_down/data'

# mention lines re-attributed to Ms Matheson (wc2024227/analysis/2026-09-27_MENTION_ACOUSTICS_correction...)
MATHESON = [1065.2, 2440.4, 2441.7, 2461.2, 2463.5, 2464.6]
AMBIGUOUS = [1351.4, 3697.0]   # 22:31 and 61:37: acoustics and words disagree; excluded


def load():
    rec = {}
    iv = [json.loads(l) for l in open(f'{R}/qps_interview_acoustic/bickery.labelled.jsonl')]
    rec['interview'] = [{'t0': r['start'], 't1': r['end'], 'spk': {0: 'CORY', 1: 'OFFICERS'}.get(r['spk']),
                         'db': r['pros'].get('db_mean'), 'wps': None, 'text': ''} for r in iv]
    cs = json.load(open(f'{C}/court_segs.json'))
    rec['court'] = [{'t0': r['start'], 't1': r['end'], 'spk': {'SHEPHERD': 'CORY'}.get(r['spk'], r['spk']),
                     'db': r['pros'].get('db_mean'), 'wps': r['pros'].get('wps'), 'text': r['text']} for r in cs]
    ms = json.load(open(f'{R}/cognitive_speech/mention_segs.json'))
    out = []
    for r in ms:
        spk = {'MR SHEPHERD': 'CORY', 'DWYER IC': 'DWYER', 'MS MATHESON': 'MATHESON'}.get(r['spk'])
        if spk == 'CORY' and any(abs(r['start'] - t) < 0.6 for t in MATHESON):
            spk = 'MATHESON'
        if spk == 'CORY' and any(abs(r['start'] - t) < 1.0 for t in AMBIGUOUS):
            spk = None
        p = r.get('pros') or {}
        out.append({'t0': r['start'], 't1': r['end'], 'spk': spk, 'db': p.get('db_mean'),
                    'wps': p.get('wps'), 'text': r['text']})
    rec['mention'] = out
    for k in rec:   # keep short segments for turn-building; statistics use segments of 0.5 s or more
        rec[k] = [dict(s, ok=(s['t1'] - s['t0'] >= 0.5)) for s in rec[k] if s['spk'] and s['db']]
    return rec


def turns(segs):
    T, cur = [], None
    for s in sorted(segs, key=lambda x: x['t0']):
        if cur and s['spk'] == cur['spk'] and s['t0'] - cur['t1'] < 1.5:
            cur['segs'].append(s); cur['t1'] = s['t1']
        else:
            cur = {'spk': s['spk'], 't0': s['t0'], 't1': s['t1'], 'segs': [s]}; T.append(cur)
    return T


def analyse(name, segs, who_list):
    print(f'\n===== {name.upper()}')
    base = {w: np.median([s['db'] for s in segs if s['spk'] == w and s['ok']]) for w in who_list}
    for s in segs:
        if s['spk'] in base:
            s['rel'] = s['db'] - base[s['spk']]
    T0, T1 = min(s['t0'] for s in segs), max(s['t1'] for s in segs)
    T = turns([s for s in segs if s['spk'] in base])
    for w in who_list:
        S = [s for s in segs if s['spk'] == w and s['ok']]
        rel = np.array([s['rel'] for s in S]); t = np.array([s['t0'] for s in S])
        q = [np.median(rel[(t >= T0 + i * (T1 - T0) / 4) & (t < T0 + (i + 1) * (T1 - T0) / 4)]) if
             np.any((t >= T0 + i * (T1 - T0) / 4) & (t < T0 + (i + 1) * (T1 - T0) / 4)) else float('nan') for i in range(4)]
        slope = np.polyfit(t / 600.0, rel, 1)[0] if len(S) > 5 else float('nan')
        loud = 100 * np.mean(rel > 3); quiet = 100 * np.mean(rel < -3)
        # within-turn trajectory: last segment minus first segment, multi-segment turns
        traj = [[s for s in tt['segs'] if s['ok']] for tt in T if tt['spk'] == w]
        traj = [g[-1]['rel'] - g[0]['rel'] for g in traj if len(g) >= 2]
        wl = [(s['rel'], s['wps']) for s in S if s.get('wps')]
        rw = np.corrcoef([a for a, _ in wl], [b for _, b in wl])[0, 1] if len(wl) > 5 else float('nan')
        print(f"{w}: n={len(S)} | spread SD {rel.std():.1f} dB, p10..p90 {np.percentile(rel,10):+.1f}..{np.percentile(rel,90):+.1f} | "
              f"loud(>+3) {loud:.0f}% quiet(<-3) {quiet:.0f}% | by quarter {', '.join(f'{x:+.1f}' for x in q)} | "
              f"drift {slope:+.2f} dB/10 min | turn end minus start {st.median(traj) if traj else float('nan'):+.1f} dB "
              f"(n={len(traj)}) | r(level, rate) {rw:+.2f}")
    # accommodation: other speaker's previous-turn level -> this speaker's first-segment level
    for w in who_list:
        xs, ys = [], []
        for a, b in zip(T, T[1:]):
            if b['spk'] == w and a['spk'] != w and a['spk'] in base:
                ga = [s['rel'] for s in a['segs'] if s['ok']]; gb = [s['rel'] for s in b['segs'] if s['ok']]
                if ga and gb:
                    xs.append(np.mean(ga)); ys.append(gb[0])
        if len(xs) > 5:
            print(f"  {w} follows the previous speaker's level: r = {np.corrcoef(xs, ys)[0,1]:+.2f} (n={len(xs)})")
    return T


def court_thirds(segs):
    import parselmouth
    from faster_whisper.audio import decode_audio
    SR = 16000
    wav = decode_audio(AUDIO, sampling_rate=SR).astype(np.float64)
    T = turns(segs)
    print('\n  Court, within each turn of 2 s or more: last third minus first third (dB)')
    for w in ['CORY', 'MAGISTRATE', 'PROSECUTOR']:
        d = []
        for tt in T:
            if tt['spk'] != w or tt['t1'] - tt['t0'] < 2.0:
                continue
            snd = parselmouth.Sound(wav[int(tt['t0'] * SR):int(tt['t1'] * SR)], sampling_frequency=SR)
            iv = snd.to_intensity(minimum_pitch=60, time_step=0.01)
            v = iv.values[0]; n = len(v)
            a, b = v[: n // 3], v[2 * n // 3:]
            a, b = a[a > np.percentile(v, 20)], b[b > np.percentile(v, 20)]   # voiced/active frames only
            if a.size and b.size:
                d.append(float(np.mean(b) - np.mean(a)))
        print(f"  {w}: median {st.median(d):+.1f} dB, turns ending quieter by >3 dB: {sum(x < -3 for x in d)} of {len(d)}")


rec = load()
analyse('interview', rec['interview'], ['CORY', 'OFFICERS'])
Tc = analyse('court', rec['court'], ['CORY', 'MAGISTRATE', 'PROSECUTOR'])
analyse('mention', rec['mention'], ['CORY', 'DWYER'])
if AUDIO:
    court_thirds(rec['court'])

print('\n===== COURT: your turns, level against your own median')
for tt in Tc:
    if tt['spk'] == 'CORY':
        rel = np.mean([s['rel'] for s in tt['segs'] if s['ok']] or [s['rel'] for s in tt['segs']])
        txt = ' '.join(re.sub(r'\[[^]]*\]', '', s['text']) for s in tt['segs'])
        print(f"{int(tt['t0']//60):02d}:{tt['t0']%60:04.1f} {rel:+5.1f} dB | {txt[:95]}")

print('\n===== MENTION: your opening segment level by first word')
Tm = turns([s for s in rec['mention'] if s['spk'] in ('CORY', 'DWYER')])
groups = {'Correct / Exactly / Yes / Yeah': r'^(correct|exactly|yes|yeah|yep)\b', 'Well': r'^well\b', 'No': r'^no\b'}
for g, rx in groups.items():
    v = [tt['segs'][0]['rel'] for tt in Tm if tt['spk'] == 'CORY' and re.match(rx, tt['segs'][0]['text'].strip().lower())]
    print(f"  {g}: n={len(v)}, median {st.median(v) if v else float('nan'):+.1f} dB")
other = [tt['segs'][0]['rel'] for tt in Tm if tt['spk'] == 'CORY' and not any(re.match(rx, tt['segs'][0]['text'].strip().lower()) for rx in groups.values())]
print(f"  other openings: n={len(other)}, median {st.median(other):+.1f} dB")
loudest = sorted([tt for tt in Tm if tt['spk'] == 'CORY' and len(tt['segs']) >= 3], key=lambda tt: -np.mean([s['rel'] for s in tt['segs']]))[:5]
print('  loudest sustained turns (3+ segments):')
for tt in loudest:
    print(f"   {int(tt['t0']//60):02d}:{int(tt['t0']%60):02d} {np.mean([s['rel'] for s in tt['segs']]):+.1f} dB | {' '.join(s['text'] for s in tt['segs'])[:110]}")
quietest = sorted([tt for tt in Tm if tt['spk'] == 'CORY' and len(tt['segs']) >= 2], key=lambda tt: np.mean([s['rel'] for s in tt['segs']]))[:4]
print('  quietest turns (2+ segments):')
for tt in quietest:
    print(f"   {int(tt['t0']//60):02d}:{int(tt['t0']%60):02d} {np.mean([s['rel'] for s in tt['segs']]):+.1f} dB | {' '.join(s['text'] for s in tt['segs'])[:110]}")
