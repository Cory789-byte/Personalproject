"""Hand-coded content of every officer turn in the 24 Feb 2025 interview, set against timing and level.

The codes were assigned by reading the full speaker-labelled transcript. The transcript is kept outside the
repo and never committed. This file holds start times and codes only, with no transcript text.

Rubric: one primary code per officer turn. Question types follow Griffiths & Milne 2006 and Oxburgh,
Myklebust & Grant 2010. Accusatory forms follow Kassin & Gudjonsson 2004 and Kassin, Goldstein & Savitsky
2003.
  PROC   procedure: caution, rights, recording, closing questions, logistics
  ACK    acknowledgement only
  OPEN   open or probing question, neutral (tell, explain, describe; what, when, how, who)
  CLOSED neutral closed or clarifying question, or an echo or summary that does not suggest the answer
  ENG    engaged, non-accusatory reply to Cory's point
  REDIR  topic change or closure with no question
  CTRL   command or closure aimed at Cory (told to answer, his point called irrelevant, interview closed on him)
  LEAD   do-you-agree-that-you question: asks him to accept the police version
  CHAL   challenges his account or credibility (why-didn't-you, pointing to an inconsistency, is-it-false)
  OPIN   asks his opinion of his own conduct against a standard (good behaviour, fair, reasonable, fearful)
  PUT    direct accusation: a put-to statement of guilt, or an accusation of lying
  NARR   officer reads evidence or narrates the police version
  EXCL   excluded: the words are probably Cory's (speaker attribution doubtful)

Uptake (how the turn relates to Cory's immediately preceding turn):
  P  took up his point and explored it on its terms
  C  took up his words to contest them or to establish the allegation
  N  did not engage his point
  -  not applicable

Flags:
  R  repeats a question he had already answered
  K  control or interruption words inside the turn
  M  several questions in one turn
  D  redirect words inside a question
  L  refers to the aggrieved as the victim
  T  transcription or attribution doubtful

Coding choices at the margin favour the officers. For example, echoes and chronology summaries are coded
neutral, and a fragment that is probably Cory's is excluded rather than counted against them.

Usage: python -I officer_question_coding.py REPO_ROOT [TRANSCRIPT_ROWS_JSON]
With the rows file (a JSON list of {t, spk, text}), the script checks the code table against the
transcript's officer turns and adds the length of Cory's replies. Output is counts only."""
import json, random, re, statistics as st, sys
from collections import Counter

CODES = """
06:01 PROC - | 06:18 PROC - | 06:29 OPEN - | 07:51 PROC - | 08:50 ACK -
11:39 OPEN P | 12:43 REDIR N | 12:48 LEAD C | 12:56 LEAD N R | 13:04 CLOSED P | 13:23 CLOSED P T
14:01 REDIR N | 14:13 CLOSED N | 14:18 CLOSED N R | 14:22 CLOSED N R | 14:27 CLOSED P | 14:34 LEAD C
15:11 ACK - | 15:16 LEAD N R | 15:24 ACK - | 15:29 ACK - | 15:45 CLOSED N | 16:05 OPEN N
16:13 CLOSED N R | 16:18 OPEN P | 16:38 CHAL C | 16:43 CHAL N | 16:47 CLOSED P | 16:58 OPEN P
17:01 CHAL C | 17:38 CLOSED N L | 18:14 CLOSED N D | 18:34 REDIR N | 18:58 LEAD N | 19:15 LEAD N R
19:30 LEAD N R | 19:41 CLOSED P | 19:50 LEAD C | 20:05 LEAD N RK | 20:17 OPEN N | 20:26 CLOSED P
20:44 CLOSED P | 20:55 OPEN P | 21:02 OPEN P | 21:06 CLOSED P | 21:14 CLOSED P | 21:21 CLOSED P
21:27 CLOSED P | 22:56 OPEN P | 23:16 OPEN P | 23:24 CLOSED P | 23:58 REDIR N | 24:34 OPEN N M
25:43 ACK - | 25:57 LEAD N | 26:09 NARR N | 27:24 CLOSED P | 27:51 OPIN N | 27:58 OPIN N R
28:12 CTRL N | 28:41 OPIN N | 29:05 CLOSED P T | 29:47 REDIR N | 29:57 LEAD C M | 30:40 OPEN P
31:03 NARR N | 32:02 CHAL C | 32:14 OPEN P | 32:47 CLOSED P | 32:58 CHAL N R | 33:29 LEAD N MKD
34:50 LEAD N T | 35:02 CHAL C K | 35:45 CHAL C | 36:28 LEAD C | 36:38 LEAD N | 36:59 NARR C
37:05 ACK - | 37:07 CHAL N | 37:27 CHAL C | 37:38 CHAL C R | 38:11 PUT N K | 38:27 PUT N RK
38:36 PUT N R | 38:48 CLOSED P | 39:50 REDIR N | 40:03 NARR N K | 40:20 LEAD N R | 40:33 LEAD N
40:45 OPEN P | 40:54 PUT N | 41:17 LEAD N R | 41:25 NARR N | 41:39 NARR N | 41:49 ACK -
41:51 LEAD N | 42:26 NARR N | 42:36 LEAD N M | 42:55 LEAD N R | 43:11 CLOSED P | 43:14 OPEN P
44:12 PUT N | 44:20 CHAL C | 44:24 CHAL C RT | 44:31 LEAD C | 44:39 CHAL C | 44:45 CHAL C R
44:51 CLOSED P | 45:06 ACK - | 45:09 OPEN P | 45:14 CLOSED P | 45:25 CHAL C | 45:35 CHAL C R
45:44 CLOSED P | 46:00 LEAD N | 46:32 CLOSED P | 46:43 CLOSED N | 46:53 PUT N | 46:57 NARR N
47:05 LEAD N R | 50:01 OPIN N | 50:36 OPIN N R | 51:01 CLOSED P | 51:22 OPIN N | 51:29 OPIN C
51:40 ACK - | 51:44 OPIN C | 52:12 CHAL C | 52:25 CHAL C | 53:23 OPIN N | 53:38 OPEN P
54:15 CLOSED N | 54:25 CLOSED N | 54:38 CLOSED N | 54:49 CLOSED N | 54:53 NARR N | 55:00 LEAD C R
55:10 CLOSED P | 55:34 CLOSED P | 55:45 CLOSED P | 56:02 NARR C | 56:24 CHAL C T | 56:40 CHAL C
56:52 EXCL - T | 56:57 CHAL C | 57:19 PROC - | 57:34 CHAL C R | 57:47 OPIN N | 57:53 LEAD N K
58:14 CLOSED P | 58:22 CLOSED P | 58:51 REDIR N | 58:54 CTRL N | 59:00 LEAD N | 59:10 CHAL N R
59:31 ACK - | 59:36 CHAL C | 59:56 PUT C | 60:06 CHAL C | 60:11 CHAL C T | 60:32 CLOSED P T
60:40 NARR C T | 61:26 ENG P | 61:33 PROC - | 61:50 ENG P | 62:00 CLOSED P | 62:09 CTRL N
62:13 PROC - | 62:28 PROC - | 62:51 PROC - | 63:09 PROC - | 63:14 PROC - | 63:26 PROC -
63:49 PROC - | 64:14 ENG P | 64:41 CTRL N | 64:57 PROC - | 65:19 ENG P | 65:57 PROC -
"""
# Evidence Cory offered, the officers' next turn, and what happened. Times only, with generic labels.
OFFERS = [
    ('15:31', 'phone messages', '15:45', 'not taken up'),
    ('17:56', 'USB footage; phone damage', '18:14', 'not taken up (redirected to the order)'),
    ('22:45', 'unlock phone to show texts', '22:56', 'not taken up (next question on property)'),
    ('24:22', 'document collection', '24:34', 'declined for this interview'),
    ('40:41', 'video of the exchange', '40:45', 'what was said was asked about; the video was not'),
    ('41:22', 'recording of leaving', '41:25', 'not taken up'),
    ('42:01', 'camera footage', '42:26', 'not taken up'),
    ('59:08', 'the permission text', '59:10', 'not taken up; challenged on not giving it earlier'),
    ('61:42', 'full download of the phone', '61:50', 'engaged; phone already seized, review deferred'),
    ('62:03', 'summary of the message history', '62:09', 'interview wound up'),
]

ACC = {'LEAD', 'CHAL', 'OPIN', 'PUT', 'NARR'}
CTL = {'CTRL', 'REDIR'}
NEU = {'OPEN', 'CLOSED', 'ENG'}
ADMIN = {'PROC', 'ACK', 'EXCL'}

tbl = []
for cell in CODES.replace('\n', '|').split('|'):
    p = cell.split()
    if not p:
        continue
    m, s = p[0].split(':')
    tbl.append({'mmss': p[0], 't': int(m) * 60 + int(s), 'code': p[1], 'up': p[2], 'flags': p[3] if len(p) > 3 else ''})
assert len({r['t'] for r in tbl}) == len(tbl), 'duplicate times'
assert all(r['code'] in ACC | CTL | NEU | ADMIN for r in tbl)
R = sys.argv[1]
rows = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else None
pct = lambda a, b: f"{100 * a / b:.0f}%" if b else '-'

# 1. check the table against the transcript's officer turns (merge consecutive same-speaker rows)
reply_words = {}
if rows:
    T = []
    for r in rows:
        who = 'C' if r['spk'].strip('*') == 'SHEPHERD' else 'O'
        if T and T[-1]['who'] == who:
            T[-1]['text'] += ' ' + r['text']
        else:
            T.append({'who': who, 't': int(r['t']), 'text': r['text']})
    O = [x for x in T if x['who'] == 'O' and x['t'] >= 360]
    have, want = {x['t'] for x in O}, {r['t'] for r in tbl}
    print(f"check: {len(O)} officer turns after 6:00 in the transcript; {len(tbl)} coded; "
          f"uncoded {sorted(have - want)}; codes without a turn {sorted(want - have)}")
    for a, b in zip(T, T[1:]):
        if a['who'] == 'O' and b['who'] == 'C':
            reply_words[a['t']] = len(b['text'].split())
    # word uptake: share of a turn's content words that came from the other side's previous turn, v shuffled
    STOP = set("""a about after again all also am an and any are as at be because been before being but by can could
    did do does doing don't down for from had has have having he her here hers him his how i i'm if in into is it it's
    its just me more most my no nor not of off on once only or other our out over own same she so some such than that
    that's the their them then there these they this those through to too under until up very was we were what when
    where which while who why will with would you your yeah yes okay ok right well like really get got going know think
    mean sort kind thing things say said one actually um uh alright all-right agree""".split())
    def cw(x):
        out = set()
        for w in re.findall(r"[a-z][a-z']+", x.lower()):
            w = w.strip("'")
            if len(w) >= 3 and w not in STOP:
                out.add(w[:-1] if len(w) > 4 and w.endswith('s') and not w.endswith('ss') else w)
        return out
    for who, name in [('O', 'officers taking up Cory'), ('C', 'Cory taking up the officers')]:
        pairs = [(cw(b['text']), cw(a['text'])) for a, b in zip(T, T[1:]) if b['who'] == who and a['who'] != who]
        pairs = [(x, y) for x, y in pairs if len(x) >= 2]
        act = st.mean(len(x & y) / len(x) for x, y in pairs)
        random.seed(7); prompts = [y for _, y in pairs]; base = []
        for _ in range(300):
            sh = prompts[:]; random.shuffle(sh)
            base.append(st.mean(len(x & q) / len(x) for (x, _), q in zip(pairs, sh)))
        print(f"word uptake, {name}: n={len(pairs)} | {100 * act:.0f}% of content words from the previous turn "
              f"(shuffled {100 * st.mean(base):.0f}%, x{act / st.mean(base):.1f}) | turns reusing any word "
              f"{pct(sum(len(x & y) > 0 for x, y in pairs), len(pairs))}")

sub = [r for r in tbl if r['code'] not in ADMIN]
c = Counter(r['code'] for r in tbl)
print(f"\nofficer turns coded: {len(tbl)} | procedure {c['PROC']}, acknowledgement {c['ACK']}, excluded {c['EXCL']} | substantive {len(sub)}")
for grp, name in [(ACC, 'ACCUSATORY'), (CTL, 'CONTROL / REDIRECT'), (NEU, 'NEUTRAL')]:
    n = sum(r['code'] in grp for r in sub)
    print(f"  {name:19s} {n:3d} ({pct(n, len(sub))}): " + ', '.join(f"{k} {c[k]}" for k in sorted(grp, key=lambda k: -c[k])))

print("\nby window (substantive turns):  n | accusatory | control/redirect | neutral | of which open")
W = [(360, 600), (600, 1200), (1200, 1800), (1800, 2400), (2400, 3000), (3000, 3600), (3600, 3970)]
for a, b in W:
    w = [r for r in sub if a <= r['t'] < b]
    if w:
        n = len(w); ac = sum(r['code'] in ACC for r in w); ct = sum(r['code'] in CTL for r in w)
        ne = sum(r['code'] in NEU for r in w); op = sum(r['code'] == 'OPEN' for r in w)
        print(f"  {a // 60:02d}-{b // 60:02d} min {n:3d} | {ac:3d} ({pct(ac, n):>4s}) | {ct:3d} ({pct(ct, n):>4s}) | {ne:3d} ({pct(ne, n):>4s}) | {op}")
for a, b, name in [(360, 1800, 'first half (6-30 min)'), (1800, 3600, 'second half (30-60 min)')]:
    w = [r for r in sub if a <= r['t'] < b]; ac = sum(r['code'] in ACC for r in w)
    print(f"  {name}: accusatory {ac}/{len(w)} ({pct(ac, len(w))})")

print("\nuptake of what Cory had just said (substantive turns after one of his turns)")
u = [r for r in sub if r['up'] in 'PCN']
cu = Counter(r['up'] for r in u)
print(f"  n={len(u)} | explored his point P {cu['P']} ({pct(cu['P'], len(u))}) | used his words to contest C {cu['C']} "
      f"({pct(cu['C'], len(u))}) | did not engage N {cu['N']} ({pct(cu['N'], len(u))})")
for a, b, name in [(360, 1800, '6-30 min'), (1800, 3600, '30-60 min'), (3600, 3970, '60-66 min')]:
    w = [r for r in u if a <= r['t'] < b]; cw = Counter(r['up'] for r in w)
    print(f"  {name}: n={len(w)} | P {pct(cw['P'], len(w))} | C {pct(cw['C'], len(w))} | N {pct(cw['N'], len(w))}")

fl = lambda f: [r for r in tbl if f in r['flags']]
print(f"\nflags: repeats of an answered question {len(fl('R'))} | turns with control/interruption words "
      f"{len(fl('K')) + c['CTRL']} (CTRL turns {c['CTRL']} + inside other turns {len(fl('K'))}) | multiple questions {len(fl('M'))} "
      f"| redirect words inside a question {len(fl('D'))} | aggrieved called the victim {len(fl('L'))} | doubtful transcription {len(fl('T'))}")
print(f"direct accusations (PUT): {c['PUT']} at " + ', '.join(r['mmss'] for r in tbl if r['code'] == 'PUT'))
print(f"opinion-of-conduct questions (OPIN): {c['OPIN']}, all from {min(r['mmss'] for r in tbl if r['code'] == 'OPIN')} on")

print("\nevidence Cory offered -> the officers' next turn")
for t0, what, t1, out in OFFERS:
    print(f"  {t0} {what:32s} -> {t1} {out}")
print(f"  offers {len(OFFERS)} | taken up on the spot 0 | engaged but deferred 1 | content asked, evidence not 1 | not taken up 8 (1 declined, 1 at wind-up)")

# 2. timing and level, from the acoustic segments (same stitched timeline; no text in them)
# Transcript row times sit about 2 s from the acoustic segment starts (spread to about +/-6 s), so the
# transcript's turn sequence is aligned to the acoustic turn sequence by dynamic programming (speaker must
# match; cost = time difference; skips allowed) rather than matched by nearest time.
if rows:
    iv = [json.loads(l) for l in open(f'{R}/qps_interview_acoustic/bickery.labelled.jsonl')]
    segs = sorted([s for s in iv if s['spk'] in (0, 1)], key=lambda s: s['start'])
    beeps = [29.9 + 120.0038 * k for k in range(33)]
    def clean(s):
        p = s['pros']
        return (p.get('f0_med') or 0) and 70 < p['f0_med'] < 200 and (p.get('voiced_frac') or 0) >= 0.25 \
            and s['end'] - s['start'] >= 0.8 and not any(s['start'] - 0.3 <= b <= s['end'] + 0.3 for b in beeps)
    db_o = st.median([s['pros']['db_mean'] for s in segs if s['spk'] == 1 and clean(s)])
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
    print(f"\nalignment: {len(S)} transcript turns, {len(A)} acoustic turns, {len(match)} matched; "
          f"median |offset| {st.median(abs(A[v]['start'] - S[k]['t']) for k, v in match.items()):.1f} s")
    byt = {r['t']: r for r in tbl}
    for k, x in enumerate(S):
        r = byt.get(x['t']) if x['who'] == 1 else None
        if not r or k not in match:
            continue
        a = A[match[k]]
        if abs(a['start'] - x['t']) > 6:
            continue
        if match[k] > 0 and A[match[k] - 1]['who'] == 0:
            r['gap'] = a['start'] - A[match[k] - 1]['end']
        lv = [s['pros']['db_mean'] for s in a['segs'] if clean(s)]
        if lv:
            r['lvl'] = st.median(lv) - db_o
    acc = [r for r in sub if r['code'] in ACC]; neu = [r for r in sub if r['code'] in NEU]
    ga = [r['gap'] for r in acc if r.get('gap') is not None]; gn = [r['gap'] for r in neu if r.get('gap') is not None]
    ma, mn = st.median(ga), st.median(gn)
    print(f"response gap after Cory stopped (s): accusatory median {ma:.2f} (n={len(ga)}) | neutral {mn:.2f} (n={len(gn)})")
    print(f"  within 0.5 s: accusatory {pct(sum(g < 0.5 for g in ga), len(ga))} | neutral {pct(sum(g < 0.5 for g in gn), len(gn))}")
    random.seed(3); pool = ga + gn; obs = mn - ma; hits = 0
    for _ in range(5000):
        random.shuffle(pool)
        hits += (st.median(pool[len(ga):]) - st.median(pool[:len(ga)])) >= obs
    print(f"  permutation test, neutral minus accusatory median {obs:+.2f} s: p = {hits / 5000:.3f} (one-sided)")
    for a, b, name in [(360, 1800, '6-30 min'), (1800, 3600, '30-60 min')]:
        x = [r['gap'] for r in acc if r.get('gap') is not None and a <= r['t'] < b]
        y = [r['gap'] for r in neu if r.get('gap') is not None and a <= r['t'] < b]
        print(f"  {name}: accusatory {st.median(x) if x else float('nan'):.2f} (n={len(x)}) | neutral {st.median(y) if y else float('nan'):.2f} (n={len(y)})")
    print("  all officer turns after one of Cory's, by window (median gap, s):  "
          + ' | '.join(f"{a // 60:02d}-{b // 60:02d} {st.median(v):.2f}" for a, b in W[1:6]
                       for v in [[r['gap'] for r in sub if r.get('gap') is not None and a <= r['t'] < b]] if v))
    la = [r['lvl'] for r in acc if r.get('lvl') is not None]; ln = [r['lvl'] for r in neu if r.get('lvl') is not None]
    print(f"officer level relative to their own median (dB): accusatory {st.median(la):+.1f} (n={len(la)}) | neutral {st.median(ln):+.1f} (n={len(ln)})")
else:
    print("\n(timing and level need the transcript rows to align turns; skipped)")

if reply_words:
    print("\nCory's next reply (words), by the kind of officer turn before it")
    for grp, name in [({'OPEN'}, 'open/probing'), ({'CLOSED', 'ENG'}, 'neutral closed/engaged'), ({'LEAD'}, 'do-you-agree'),
                      ({'CHAL'}, 'challenge'), ({'OPIN'}, 'opinion of conduct'), ({'PUT'}, 'accusation'), ({'NARR'}, 'narration/evidence'),
                      ({'CTRL', 'REDIR'}, 'control/redirect')]:
        v = [reply_words[r['t']] for r in tbl if r['code'] in grp and r['t'] in reply_words]
        if v:
            print(f"  after {name:24s}: median {st.median(v):5.0f} words (n={len(v)})")
