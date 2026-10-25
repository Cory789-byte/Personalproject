"""Listening measures: does a speaker follow the other person or run their own point?

For every response turn (a turn that follows another speaker's turn), each content word is classed as:
  FOLLOW  - it appeared in the turn just answered (uptake of the other person's words)
  OWN     - not in that turn, but in the speaker's own previous three turns (own thread carried on)
  NEW     - neither
Uptake is compared with a shuffled baseline (the same answer paired with a random other turn from the same
recording), so it measures following beyond chance word overlap.
Also: lexical entrainment - key terms one speaker introduced (used 2+ times) that the other later adopted.

Usage: python -I listening.py REPO_ROOT. Court and mention (the interview has no word-level text on disk).
Descriptive only; not clinical.
"""
import json, random, re, statistics as st, sys

R = sys.argv[1]
STOP = set("""a about above after again against all also am an and any are aren't as at be because been before being
below between both but by can can't cannot could couldn't did didn't do does doesn't doing don't down during each few for
from further had hadn't has hasn't have haven't having he he'd he'll he's her here here's hers herself him himself his how
how's i i'd i'll i'm i've if in into is isn't it it's its itself let's me more most mustn't my myself no nor not of off on
once only or other ought our ours ourselves out over own same shan't she she'd she'll she's should shouldn't so some such
than that that's the their theirs them themselves then there there's these they they'd they'll they're they've this those
through to too under until up very was wasn't we we'd we'll we're we've were weren't what what's when when's where where's
which while who who's whom why why's with won't would wouldn't you you'd you'll you're you've your yours yourself yourselves
yeah yes okay ok right well just like really get got going know think mean sort kind thing things say said says one also
actually basically probably maybe sure oh um uh er gonna want wanted something anything everything look see go come
done make made even still way much many lot bit back now then today time first last because whether""".split())


def words(t):
    t = re.sub(r'\[[^]]*\]', ' ', t.lower())
    out = []
    for w in re.findall(r"[a-z][a-z'\-]+", t):
        w = w.strip("'-")
        if w.endswith("'s"):
            w = w[:-2]
        if len(w) < 3 or w in STOP:
            continue
        if len(w) > 4 and w.endswith('s') and not w.endswith('ss'):
            w = w[:-1]
        out.append(w)
    return out


def turns(segs):
    T, cur = [], None
    for s in segs:
        if cur and s['spk'] == cur['spk'] and s['start'] - cur['end'] < 1.5:
            cur['text'] += ' ' + s['text']; cur['end'] = s['end']
        else:
            cur = {'spk': s['spk'], 'start': s['start'], 'end': s['end'], 'text': s['text']}; T.append(cur)
    return T


def analyse(name, T, A, B):
    print(f'\n===== {name}')
    for who, other in [(A, B), (B, A)]:
        resp = []
        for i in range(1, len(T)):
            if T[i]['spk'] == who and T[i - 1]['spk'] == other:
                cw = set(words(T[i]['text']))
                if len(cw) < 2:
                    continue
                prompt = set(words(T[i - 1]['text']))
                own = set()
                k = i - 1; n = 0
                while k >= 0 and n < 3:
                    if T[k]['spk'] == who:
                        own |= set(words(T[k]['text'])); n += 1
                    k -= 1
                resp.append((cw, prompt, own))
        if len(resp) < 5:
            print(f"{who} answering {other}: n={len(resp)} (too few to measure)")
            continue
        fol = [len(c & p) / len(c) for c, p, o in resp]
        ownc = [len((c & o) - p) / len(c) for c, p, o in resp]
        new = [len(c - p - o) / len(c) for c, p, o in resp]
        prompts = [p for _, p, _ in resp]
        random.seed(7)
        base = []
        for _ in range(300):
            sh = prompts[:]; random.shuffle(sh)
            base.append(st.mean(len(c & q) / len(c) for (c, _, _), q in zip(resp, sh)))
        b = st.mean(base)
        print(f"{who} answering {other}: n={len(resp)} | FOLLOW {100*st.mean(fol):.0f}% (shuffled baseline {100*b:.0f}%, "
              f"x{st.mean(fol)/b:.1f}) | OWN thread {100*st.mean(ownc):.0f}% | NEW {100*st.mean(new):.0f}% | "
              f"answers using at least one of the question's words: {100*sum(x>0 for x in fol)/len(fol):.0f}%")
    # entrainment: key terms introduced by X (first use by X, X uses 2+ times) later adopted by Y
    first, uses = {}, {}
    for t in T:
        for w in words(t['text']):
            uses.setdefault((t['spk'], w), 0)
            uses[(t['spk'], w)] += 1
            if w not in first:
                first[w] = t['spk']
    for x, y in [(A, B), (B, A)]:
        keys = [w for w, s in first.items() if s == x and uses.get((x, w), 0) >= 2]
        adopted = [w for w in keys if uses.get((y, w), 0) > 0]
        top = sorted(adopted, key=lambda w: -uses.get((y, w), 0))[:12]
        print(f"  key terms {x} introduced: {len(keys)}; adopted by {y}: {len(adopted)} ({100*len(adopted)/max(1,len(keys)):.0f}%) "
              f"e.g. {', '.join(top)}")


# court
ct = json.load(open(f'{R}/qps_court_audio/2026-02-02_BMC_trial_stood_down/data/turns.json'))
T = [{'spk': t['who'], 'start': t['start'], 'end': t['start'] + t['dur'], 'text': t['text']} for t in ct]
analyse('COURT: you and the Magistrate', T, 'SHEPHERD', 'MAGISTRATE')
analyse('COURT: you and the prosecutor', T, 'SHEPHERD', 'PROSECUTOR')

# mention (Matheson re-attributions; question sentences removed from your segments, which merge the
# Commissioner's questions with your answers)
ms = json.load(open(f'{R}/cognitive_speech/mention_segs.json'))
MATH = [1065.2, 2440.4, 2441.7, 2461.2, 2463.5, 2464.6]; AMB = [1351.4, 3697.0]
segs = []
for s in ms:
    spk = s['spk']
    if spk == 'MR SHEPHERD' and any(abs(s['start'] - t) < 0.6 for t in MATH):
        spk = 'MS MATHESON'
    if spk == 'MR SHEPHERD' and any(abs(s['start'] - t) < 1.0 for t in AMB):
        continue
    if not spk:
        continue
    text = s['text']
    if spk == 'MR SHEPHERD':
        text = ' '.join(x for x in re.split(r'(?<=[.?!])\s+', text) if not x.strip().endswith('?'))
    segs.append({'spk': spk, 'start': s['start'], 'end': s['end'], 'text': text})
analyse('MENTION: you and the Commissioner', turns(segs), 'MR SHEPHERD', 'DWYER IC')


# ---- new-information uptake: of the terms a speaker uses for the first time in the recording,
# how many does the other speaker take up in the very next turn?
def new_term_uptake(name, T, A, B):
    seen = set()
    stats = {A: [], B: []}
    for i in range(len(T) - 1):
        cur, nxt = T[i], T[i + 1]
        cw = words(cur['text'])
        new = {w for w in cw if w not in seen}
        seen |= set(cw)
        if nxt['spk'] != cur['spk'] and nxt['spk'] in stats and cur['spk'] in (A, B) and new:
            stats[nxt['spk']].append(len(new & set(words(nxt['text']))) / len(new))
    for who, v in stats.items():
        if len(v) >= 5:
            print(f"  {name}: {who} took up {100*st.mean(v):.0f}% of the other's brand-new terms in the very next turn "
                  f"(n={len(v)} turns; at least one taken up in {100*sum(x>0 for x in v)/len(v):.0f}%)")

print('\n===== NEW-INFORMATION UPTAKE')
new_term_uptake('COURT', T if False else [{'spk': t['who'], 'start': t['start'], 'end': t['start'] + t['dur'], 'text': t['text']} for t in ct], 'SHEPHERD', 'MAGISTRATE')
new_term_uptake('MENTION', turns(segs), 'MR SHEPHERD', 'DWYER IC')
