"""How Cory answered the officers in the 24 Feb 2025 interview: leading questions, repeated questions,
the arguments he built, and his voice after accusatory v neutral questions.

The codes were assigned by reading the full transcript, which is held outside the repo. This file holds
times and codes only, with no transcript text. The officers' turn codes are read from
officer_question_coding.py.

Answer codes for the 27 do-you-agree (LEAD) questions. The yield analogue follows Gudjonsson's
suggestibility model (Gudjonsson & Clark 1986); transformative answers follow Stivers & Hayashi 2010.
  F   accepted the fact as put
  FQ  accepted a fact in his own terms and contested its meaning ("yes, but")
  R   rejected the proposition
  X   turned the question round, or pointed to evidence instead

Answer codes for the 24 repeated questions (shift analogue):
  H   held his earlier answer
  S   shifted from it

Usage: python -I interview_resistance.py REPO_ROOT TRANSCRIPT_ROWS_JSON. Output is counts only."""
import json, math, random, statistics as st, sys
from collections import Counter

R, rows = sys.argv[1], json.load(open(sys.argv[2]))
src = open(f'{R}/qps_interview_acoustic/officer_question_coding.py').read()
OCODE = {}
for cell in src.split('CODES = """')[1].split('"""')[0].replace('\n', '|').split('|'):
    p = cell.split()
    if p:
        m, s = p[0].split(':')
        OCODE[int(m) * 60 + int(s)] = (p[1], p[3] if len(p) > 3 else '')
sec = lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1])

LEAD_ANSWER = """12:48 FQ | 12:56 FQ | 14:34 R | 15:16 FQ | 18:58 FQ | 19:15 FQ | 19:30 R | 19:50 FQ | 20:05 FQ
25:57 F | 29:57 FQ | 33:29 FQ | 34:50 R | 36:28 R | 36:38 FQ | 40:20 FQ | 40:33 X | 41:17 X | 41:51 FQ
42:36 FQ | 42:55 FQ | 44:31 FQ | 46:00 R | 47:05 R | 55:00 FQ | 57:53 R | 59:00 F"""
REPEAT_ANSWER = """12:56 H | 14:18 H | 14:22 H | 15:16 H | 16:13 H | 19:15 H | 19:30 H | 20:05 S | 27:58 H | 32:58 H
37:38 H | 38:27 H | 38:36 H | 40:20 H | 41:17 H | 42:55 H | 44:24 H | 44:45 H | 45:35 H | 47:05 H
50:36 H | 55:00 H | 57:34 H | 59:10 H"""
# Officer turns that put a characterisation of wrongdoing (not a bare fact): theft, control, forcible
# removal, lying, trying to enter, intimidation, not good behaviour, causing fear, purpose. None was accepted.
CHARACTERISATIONS = "14:34 27:51 27:58 28:41 36:28 38:11 38:27 38:36 44:12 46:53 47:05 50:01 50:36 57:53 59:56"
# What he built: groundwork in place before the interview (as he described it), and arguments made live.
BUILT = [
    ('07:05', 'groundwork', 'confirmed in advance that he could attend'),
    ('07:19', 'groundwork', 'receipts for his property'),
    ('10:05', 'groundwork', 'checked with the tenancy authority and building management'),
    ('22:28', 'groundwork', 'kept paying rent and electricity'),
    ('29:53', 'groundwork', 'notified police and her before attending'),
    ('10:49', 'conciliation', 'offered the guest furniture and a bed'),
    ('09:14', 'legal rule', 'civil partnership: joint property'),
    ('19:59', 'legal rule', 'the notice needs both signatures'),
    ('35:36', 'legal rule', 'co-tenants decide together'),
    ('21:38', 'dilemma', 'off the lease, the agreement lets him retrieve belongings; on it, it is his home'),
    ('41:05', 'inconsistent commitment', 'she called the animals his'),
    ('50:43', 'inconsistent commitment', 'stayed for hours after being asked to leave; raised her voice on video'),
    ('59:54', 'method of difference', 'his trust differed because the handcuffs differed'),
    ('43:19', 'alternative explanation', 'the remark echoed her earlier accusation'),
    ('56:59', 'alternative explanation', "the friend's distrust after the handcuffs explains the deleted video"),
    ('37:06', 'reductio', 'she was not even in the state'),
    ('65:14', 'reductio', 'wanting to get away is the opposite of control'),
    ('38:51', 'options offered', 'he had offered alternatives for who could stay'),
    ('46:41', 'perspective appeal', 'a stranger in your own home'),
    ('58:37', 'perspective appeal', 'you would introduce a friend who was staying'),
    ('40:40', 'reversal', 'turned the yelling question round and pointed to video'),
    ('32:11', 'third-party knowledge', 'why the manager would have believed the notice'),
    ('33:00', 'consistent rule', 'only entered when his position was confirmed'),
    ('28:14', 'stated intention', 'asking for his belongings'),
    ('58:04', 'stated purpose', 'ask her to leave, live in his home, take his things'),
]
# What the officers did when a line did not land (times of their turns).
OFFICER_MOVES = [
    ('29:47', 'dropped a line'), ('33:29', 'dropped a line'), ('39:50', 'dropped a line'),
    ('59:36', 'said he was confused'),
    ('35:45', 'acknowledged his point'), ('36:38', 'conceded a point'), ('38:11', 'acknowledged his point'),
    ('45:44', 'accepted his version'), ('61:50', 'accepted his concern'), ('64:14', 'acknowledged the complexity'),
    ('58:51', 'declined to engage his point'),
    ('62:09', 'wound up'), ('64:41', 'wound up'),
    ('65:19', 'answered his last question with what was being investigated, not an assertion'),
]

def table(txt):
    out = {}
    for cell in txt.replace('\n', '|').split('|'):
        p = cell.split()
        if p:
            out[sec(p[0])] = p[1]
    return out
LA, RA = table(LEAD_ANSWER), table(REPEAT_ANSWER)

# check every code against the transcript's turns
T = []
for r in rows:
    who = 'C' if r['spk'].strip('*') == 'SHEPHERD' else 'O'
    if T and T[-1]['who'] == who:
        T[-1]['text'] += ' ' + r['text']
    else:
        T.append({'who': who, 't': int(r['t']), 'text': r['text']})
followed = {a['t'] for a, b in zip(T, T[1:]) if a['who'] == 'O' and b['who'] == 'C'}
lead = {t for t, (c, f) in OCODE.items() if c == 'LEAD'}
rep = {t for t, (c, f) in OCODE.items() if 'R' in f}
cory_rows = {int(r['t']) for r in rows if r['spk'].strip('*') == 'SHEPHERD'}
print(f"check: do-you-agree turns {len(lead)}, coded {len(LA)}, mismatched {sorted(lead ^ set(LA))} | "
      f"repeats {len(rep)}, coded {len(RA)}, mismatched {sorted(rep ^ set(RA))} | "
      f"answers present {sum(t in followed for t in set(LA) | set(RA))}/{len(set(LA) | set(RA))} | "
      f"built items at a line of Cory's {sum(sec(t) in cory_rows for t, _, _ in BUILT)}/{len(BUILT)} | "
      f"officer moves at an officer turn {sum(sec(t) in OCODE for t, _ in OFFICER_MOVES)}/{len(OFFICER_MOVES)}")

c = Counter(LA.values())
print(f"\ndo-you-agree questions: {len(LA)} | accepted the fact as put {c['F']} | 'yes, but' (fact in his terms, "
      f"meaning contested) {c['FQ']} | rejected {c['R']} | turned round / pointed to evidence {c['X']}")
chars = [sec(t) for t in CHARACTERISATIONS.split()]
print(f"characterisations of wrongdoing put to him: {len(chars)} turns; accepted: 0")
cr = Counter(RA.values())
print(f"repeated questions: {len(RA)} | held his answer {cr['H']} | shifted {cr['S']} (at "
      + ', '.join(f"{t // 60:02d}:{t % 60:02d}" for t, v in RA.items() if v == 'S') + ")")
kinds = Counter(k for _, k, _ in BUILT)
live = [b for b in BUILT if b[1] not in ('groundwork', 'conciliation')]
print(f"\nwhat he built: groundwork {kinds['groundwork']}, conciliation {kinds['conciliation']}, live arguments {len(live)}:")
for k, n in Counter(k for _, k, _ in live).most_common():
    print(f"  {k:24s} {n}  (" + ', '.join(t for t, kk, _ in live if kk == k) + ")")
mv = Counter(k for _, k, in OFFICER_MOVES)
print("\nofficers when a line did not land: " + ' | '.join(f"{k} {n}" for k, n in mv.items()))

# his voice in the turn after accusatory v neutral officer turns (transcript turns aligned to acoustic turns)
ACC = {'LEAD', 'CHAL', 'OPIN', 'PUT', 'NARR'}; NEU = {'OPEN', 'CLOSED', 'ENG'}
iv = sorted([json.loads(l) for l in open(f'{R}/qps_interview_acoustic/bickery.labelled.jsonl')], key=lambda s: s['start'])
segs = [s for s in iv if s['spk'] in (0, 1)]
beeps = [29.9 + 120.0038 * k for k in range(33)]
def clean(s):
    p = s['pros']
    return (p.get('f0_med') or 0) and 70 < p['f0_med'] < 200 and (p.get('voiced_frac') or 0) >= 0.25 \
        and s['end'] - s['start'] >= 0.8 and not any(s['start'] - 0.3 <= b <= s['end'] + 0.3 for b in beeps)
A = []
for s in segs:
    if A and A[-1]['who'] == s['spk'] and s['start'] - A[-1]['end'] < 1.5:
        A[-1]['end'] = s['end']; A[-1]['segs'].append(s)
    else:
        A.append({'who': s['spk'], 'start': s['start'], 'end': s['end'], 'segs': [s]})
S = [{'who': 0 if x['who'] == 'C' else 1, 't': x['t']} for x in T]
INF, SKIP = float('inf'), 6.0
n, m = len(S), len(A)
D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
for i in range(n + 1):
    for j in range(m + 1):
        if D[i][j] == INF:
            continue
        if i < n and j < m:
            cst = min(abs(A[j]['start'] - S[i]['t']), 30) if S[i]['who'] == A[j]['who'] else 40
            if D[i][j] + cst < D[i + 1][j + 1]:
                D[i + 1][j + 1] = D[i][j] + cst; B[i + 1][j + 1] = (i, j, 1)
        if i < n and D[i][j] + SKIP < D[i + 1][j]:
            D[i + 1][j] = D[i][j] + SKIP; B[i + 1][j] = (i, j, 0)
        if j < m and D[i][j] + SKIP < D[i][j + 1]:
            D[i][j + 1] = D[i][j] + SKIP; B[i][j + 1] = (i, j, 0)
i, j, match = n, m, {}
while i or j:
    pi, pj, mt = B[i][j]
    if mt and S[pi]['who'] == A[pj]['who']:
        match[pi] = pj
    i, j = pi, pj
c_db = st.median([s['pros']['db_mean'] for s in segs if s['spk'] == 0 and clean(s)])
c_f0 = st.median([s['pros']['f0_med'] for s in segs if s['spk'] == 0 and clean(s)])
res = {'acc': [], 'neu': []}
for k, x in enumerate(S):
    oc = OCODE.get(x['t'], ('', ''))[0] if x['who'] == 1 else ''
    g = 'acc' if oc in ACC else 'neu' if oc in NEU else None
    if not g or k not in match:
        continue
    jj = match[k]
    if abs(A[jj]['start'] - x['t']) > 6 or jj + 1 >= len(A) or A[jj + 1]['who'] != 0:
        continue
    cs = [s for s in A[jj + 1]['segs'] if clean(s)]
    if cs:
        res[g].append({'gap': A[jj + 1]['start'] - A[jj]['end'], 'len': A[jj + 1]['end'] - A[jj + 1]['start'],
                       'db': st.median(s['pros']['db_mean'] for s in cs) - c_db,
                       'st': 12 * math.log2(st.median(s['pros']['f0_med'] for s in cs) / c_f0),
                       'move': st.median(s['pros']['f0_sd_st'] for s in cs)})
print("\nhis next turn, after accusatory v neutral officer turns (aligned to the audio; two-sided permutation test)")
for key, lab in [('gap', 'reply gap (s)'), ('len', 'turn length (s)'), ('db', 'level v his own median (dB)'),
                 ('st', 'pitch v his own median (semitones)'), ('move', 'pitch movement in a phrase (st)')]:
    a = [r[key] for r in res['acc']]; b = [r[key] for r in res['neu']]
    random.seed(5); pool = a + b; obs = st.median(a) - st.median(b); hits = 0
    for _ in range(5000):
        random.shuffle(pool)
        hits += abs(st.median(pool[:len(a)]) - st.median(pool[len(a):])) >= abs(obs)
    print(f"  {lab:36s} after accusatory {st.median(a):+.2f} (n={len(a)}) | after neutral {st.median(b):+.2f} (n={len(b)}) | p = {hits / 5000:.2f}")
