"""Formulation patterns per speaker (contrast/exception words, causal words, negation, pronouns, openers,
repetition) for the 2 Feb 2026 court hearing and the 7 Aug 2026 mention.
Usage: python -I formulation.py REPO_ROOT. Descriptive only; not clinical."""
import json, re, sys, collections, statistics as st
R = sys.argv[1]; C = R + '/qps_court_audio/2026-02-02_BMC_trial_stood_down/data'
clean = lambda t: re.sub(r'\[[^]]*\]', '', t)
def toks(t): return re.findall(r"[a-z']+", clean(t).lower())
LEX = {
 'exclusive (but/except/unless/without/however/only/rather)': r"\b(but|except|unless|without|however|although|whereas|instead|rather|only)\b",
 'causal (because/reason/why/therefore/since)': r"\b(because|cause|therefore|reason|why|since)\b",
 'negation': r"\b(not|no|never|nothing|none|nobody|don't|didn't|wasn't|isn't|can't|couldn't|won't|haven't|hasn't|weren't|aren't|doesn't|n't)\b",
 'they/them/their': r"\b(they|them|their|they've|they're|they'd)\b",
 'he/she/his/her': r"\b(he|she|his|her|him|he's|she's)\b",
 'you/your': r"\b(you|your|you're|you've)\b",
 'I/me/my': r"\b(i|me|my|i'm|i've|i'd|i'll)\b",
 'we/us/our': r"\b(we|us|our|we're|we've)\b",
 'document/record words': r"\b(email|emails|letter|statement|footage|camera|form|document|documents|record|records|roster|rosters|schedule|application|report|policy|evidence|material|correspondence)\b",
 'time anchors (dates/days/months/clock)': r"\b(january|february|march|april|may|june|july|august|september|october|november|december|monday|tuesday|wednesday|thursday|friday|saturday|sunday|\d+(st|nd|rd|th)|20\d\d|o'clock|\d+:\d\d|am|pm)\b",
}
def turns_from_segs(segs, key):
    out = []; cur = None
    for s in segs:
        spk = s[key]
        if cur and spk == cur['spk'] and s['start'] - cur['end'] < 1.5:
            cur['text'] += ' ' + s['text']; cur['end'] = s['end']
        else:
            cur = {'spk': spk, 'start': s['start'], 'end': s['end'], 'text': s['text']}; out.append(cur)
    return out
def report(turns, who, label):
    T = [t for t in turns if t['spk'] == who]
    text = ' '.join(clean(t['text']) for t in T).lower(); n = len(toks(text))
    row = {k: round(100*len(re.findall(rx, text))/max(1, n), 2) for k, rx in LEX.items()}
    op = collections.Counter()
    for t in T:
        w = toks(t['text'])
        if w: op[w[0]] += 1
    q = sum(clean(t['text']).count('?') for t in T)
    # left dislocation: "The/That/His/My ... X, he/she/it/his/her/their ..."
    ld = re.findall(r"\b(?:the|that|this|his|her|my|their)\s+[a-z' -]{2,30},\s+(?:he|she|it|they|his|her|its|their)\b", text)
    rep = re.findall(r"\b(\w+(?: \w+){0,3}) and \1\b", text)
    print(f"\n== {label}: {who} ({n} words, {len(T)} turns)")
    for k, v in row.items(): print(f"  {k}: {v}")
    print(f"  questions asked: {q} ({round(100*q/max(1,n),2)}/100w)")
    print(f"  turn openers (top 8): {op.most_common(8)}")
    print(f"  topic-first (left-dislocation) candidates: {len(ld)} {ld[:6]}")
    print(f"  'X and X' repetitions: {rep[:8]}")
court = json.load(open(f'{C}/turns.json'))
for t in court: t['spk'] = t['who']
for who in ['SHEPHERD', 'MAGISTRATE', 'PROSECUTOR']: report(court, who, 'COURT')
ms = json.load(open(f'{R}/cognitive_speech/mention_segs.json'))
mt = turns_from_segs([s for s in ms if s['spk']], 'spk')
for who in ['MR SHEPHERD', 'DWYER IC']: report(mt, who, 'MENTION')
