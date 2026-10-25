"""Two role shifts, measured: (1) did Cory's content outrun the officers in the 24 Feb 2025 interview, and did
he become the one asking the questions; (2) did the Commissioner move to "we" at the 7 Aug 2026 mention.

Interview: the transcript is held outside the repo, and output is counts and times only. Officer turn codes
and uptake are read from qps_interview_acoustic/officer_question_coding.py. Mention: mention_segs.json, with
the Matheson re-attributions used in listening.py. Questions are sentences ending "?" in the machine
transcript, so punctuation is the transcriber's.

Usage: python -I content_load_and_roles.py REPO_ROOT INTERVIEW_ROWS_JSON"""
import json, re, statistics as st, sys
from collections import Counter

R, rows = sys.argv[1], json.load(open(sys.argv[2]))
pct = lambda a, b: f"{100 * a / b:.0f}%" if b else '-'
mmss = lambda t: f"{int(t) // 60:02d}:{int(t) % 60:02d}"
src = open(f'{R}/qps_interview_acoustic/officer_question_coding.py').read()
OC = {}
for cell in src.split('CODES = """')[1].split('"""')[0].replace('\n', '|').split('|'):
    p = cell.split()
    if p:
        m, s = p[0].split(':')
        OC[int(m) * 60 + int(s)] = (p[1], p[2])

# ---------- interview ----------
for r in rows:
    r['who'] = 'C' if r['spk'].strip('*') == 'SHEPHERD' else 'O'
    r['w'] = len(r['text'].split())
    r['q'] = len([x for x in re.split(r'(?<=[.?!])\s+', r['text']) if x.strip().endswith('?')])
T = []
for r in rows:
    if T and T[-1]['who'] == r['who']:
        T[-1]['w'] += r['w']; T[-1]['q'] += r['q']; T[-1]['end'] = r['t']
    else:
        T.append({'who': r['who'], 't': int(r['t']), 'end': r['t'], 'w': r['w'], 'q': r['q']})
W = [(360, 1200), (1200, 1800), (1800, 2400), (2400, 3000), (3000, 3600), (3600, 3970)]
print("INTERVIEW (from 6:00)")
print("window      | words: Cory  officers  Cory share | questions: Cory  officers  Cory share")
for a, b in W + [(360, 3970)]:
    rr = [r for r in rows if a <= r['t'] < b]
    cw = sum(r['w'] for r in rr if r['who'] == 'C'); ow = sum(r['w'] for r in rr if r['who'] == 'O')
    cq = sum(r['q'] for r in rr if r['who'] == 'C'); oq = sum(r['q'] for r in rr if r['who'] == 'O')
    lab = 'all' if (a, b) == (360, 3970) else f"{a // 60:02d}-{b // 60:02d} min"
    print(f"{lab:11s} | {cw:10d} {ow:9d} {pct(cw, cw + ow):>10s} | {cq:14d} {oq:9d} {pct(cq, cq + oq):>10s}")
ct = [x for x in T if x['who'] == 'C' and x['t'] >= 360]; ot = [x for x in T if x['who'] == 'O' and x['t'] >= 360]
print(f"turn length (words): Cory median {st.median(x['w'] for x in ct)}, officers {st.median(x['w'] for x in ot)} | "
      f"Cory turns of 60+ words: {sum(x['w'] >= 60 for x in ct)}, carrying {pct(sum(x['w'] for x in ct if x['w'] >= 60), sum(x['w'] for x in ct))} of his words")

# what the officers did next, by the length of Cory's turn before
print("\nofficers' next turn, by the length of Cory's turn before it (substantive officer turns)")
buckets = [(0, 20, 'under 20 words'), (20, 60, '20-59 words'), (60, 10 ** 6, '60+ words')]
for lo, hi, lab in buckets:
    nxt = [b for a, b in zip(T, T[1:]) if a['who'] == 'C' and b['who'] == 'O' and lo <= a['w'] < hi and b['t'] in OC
           and OC[b['t']][0] not in ('PROC', 'ACK', 'EXCL')]
    u = Counter(OC[b['t']][1] for b in nxt); k = Counter(OC[b['t']][0] for b in nxt)
    red = k['REDIR'] + k['CTRL']
    print(f"  after {lab:15s} n={len(nxt):3d} | explored his point {pct(u['P'], len(nxt))} | contested {pct(u['C'], len(nxt))} | "
          f"did not engage {pct(u['N'], len(nxt))} | of which redirect/closure {pct(red, len(nxt))}")
long_after = [(a, b) for a, b in zip(T, T[1:]) if a['who'] == 'C' and b['who'] == 'O' and a['w'] >= 60 and b['t'] in OC]
print("  after his 60+ word turns, the officers' next move: "
      + ', '.join(f"{mmss(b['t'])} {OC[b['t']][0]}/{OC[b['t']][1]} (after {a['w']} words)" for a, b in long_after))

# who asks: counter-questions (Cory answering a question with a question) and questions by half
cq_turns = [(a, b) for a, b in zip(T, T[1:]) if a['who'] == 'O' and a['q'] and b['who'] == 'C' and b['q'] and b['t'] >= 360]
print(f"\nCory's turns containing a question, in reply to an officer question: {len(cq_turns)} at "
      + ', '.join(mmss(b['t']) for a, b in cq_turns))
for a, b, lab in [(360, 1800, '6-30 min'), (1800, 3600, '30-60 min'), (3600, 3970, '60-66 min')]:
    cq = sum(r['q'] for r in rows if r['who'] == 'C' and a <= r['t'] < b)
    oq = sum(r['q'] for r in rows if r['who'] == 'O' and a <= r['t'] < b)
    mins = (b - a) / 60
    print(f"  {lab}: Cory {cq / mins:.2f} questions/min, officers {oq / mins:.2f}/min | Cory's share {pct(cq, cq + oq)}")

# ---------- mention ----------
ms = json.load(open(f'{R}/cognitive_speech/mention_segs.json'))
MATH = [1065.2, 2440.4, 2441.7, 2461.2, 2463.5, 2464.6]
for s in ms:
    if s['spk'] == 'MR SHEPHERD' and any(abs(s['start'] - t) < 0.6 for t in MATH):
        s['spk'] = 'MS MATHESON'
WE = re.compile(r"\b(we|we're|we've|we'll|we'd|us|our|ours|let's)\b", re.I)
YOU = re.compile(r"\b(you|you're|you've|you'll|you'd|your|yours)\b", re.I)
# Hand classification of each Commissioner segment that uses "we": J = joint (him and Cory, or the
# hearing); A = joint and hands Cory the agenda; V = voicing a party (the staff, the Regulator, Ms Matheson);
# O = other (generational).
WE_CLASS = """01:46 J | 02:29 J | 05:03 J | 06:35 J | 10:06 J | 11:42 J | 12:08 J | 15:03 J | 20:25 V | 22:34 J
24:16 J | 24:37 J | 27:36 J | 27:38 J | 27:54 V | 27:56 V | 29:56 J | 30:14 J | 30:57 J | 31:01 J | 31:12 J
32:43 O | 33:57 V | 34:13 V | 34:28 V | 36:12 J | 36:18 J | 41:17 J | 44:40 V | 44:41 V | 44:45 V | 44:49 V
45:56 V | 49:15 V | 50:42 J | 53:30 J | 53:36 A | 53:39 A | 53:48 J | 54:04 J | 54:09 A | 54:13 J | 54:54 J
54:57 J | 55:04 J | 60:17 J | 60:22 V | 60:27 V | 61:58 J | 62:19 V | 62:23 J | 63:07 J | 64:11 J"""
cls = {}
for cell in WE_CLASS.replace('\n', '|').split('|'):
    p = cell.split()
    if p:
        m, s = p[0].split(':'); cls[int(m) * 60 + int(s)] = p[1]
dw = [s for s in ms if s['spk'] == 'DWYER IC']
we_segs = {int(s['start']) for s in dw if WE.search(s['text'])}
print(f"\nMENTION: Commissioner segments using 'we' {len(we_segs)}, hand-classified {len(cls)}, "
      f"unmatched {sorted(mmss(t) for t in we_segs ^ set(cls))}")
tot = max(s['end'] for s in ms)
print("quarter | Commissioner: words  we/100w  you/100w  we-share | joint 'we' lines (of which agenda to Cory) | voicing a party")
for q in range(4):
    a, b = q * tot / 4, (q + 1) * tot / 4
    seg = [s for s in dw if a <= s['start'] < b]
    w = sum(len(s['text'].split()) for s in seg)
    we = sum(len(WE.findall(s['text'])) for s in seg); yo = sum(len(YOU.findall(s['text'])) for s in seg)
    c = Counter(v for t, v in cls.items() if a <= t < b)
    print(f"Q{q + 1} {mmss(a)}-{mmss(b)} | {w:5d} {100 * we / w:8.2f} {100 * yo / w:9.2f} {pct(we, we + yo):>9s} | "
          f"{c['J'] + c['A']:3d} ({c['A']}) | {c['V']}")
