"""Who could follow whom at the 7 Aug 2026 mention (WC/2024/227).

Internal / self-analysis only. Reads mention_segs.json (labels as at A1), applies the A3
re-attributions (six segments to Ms Matheson), merges segments into turns, and counts:
  - speaking volume, rate and turn length per speaker;
  - clarification requests (other-initiated repair) and candidate understandings;
  - comprehension checks and redirects by the Commissioner;
  - Ms Matheson's turns: who selected her, and how she answered.
Pattern hits are printed with their text so each can be checked by eye; the write-up
counts only hits confirmed on reading. Segment labels are imperfect inside some
multi-line segments (two voices in one segment), so per-speaker counts are approximate.
"""
import json, re, statistics as st

A3_STARTS = [1065.2, 2440.4, 2441.7, 2461.2, 2463.5, 2464.6]

segs = json.load(open('mention_segs.json'))
for s in segs:
    if any(abs(s['start'] - a) < 0.35 for a in A3_STARTS):
        s['spk'] = 'MS MATHESON'

def mmss(t):
    return f"{int(t // 60):02d}:{t % 60:05.2f}"

def words(t):
    return re.findall(r"[A-Za-z']+", t)

# ---- volume and rate ----
print("== VOLUME AND RATE (labels A1-A3)")
spk = ['DWYER IC', 'MR SHEPHERD', 'MS MATHESON']
for p in spk:
    ss = [s for s in segs if s['spk'] == p]
    w = sum(len(words(s['text'])) for s in ss)
    d = sum(s['end'] - s['start'] for s in ss)
    print(f"{p:12s} segs={len(ss):4d} words={w:5d} secs={d:7.1f} words/sec={w / d:4.2f}")

# ---- turns (merge consecutive same-speaker segments) ----
turns = []
for s in segs:
    if turns and turns[-1]['spk'] == s['spk']:
        turns[-1]['text'] += ' ' + s['text']
        turns[-1]['end'] = s['end']
    else:
        turns.append({'spk': s['spk'], 'start': s['start'], 'end': s['end'], 'text': s['text']})
print("\n== TURN LENGTH (words)")
for p in spk:
    lens = [len(words(t['text'])) for t in turns if t['spk'] == p]
    long60 = sum(1 for x in lens if x >= 60)
    print(f"{p:12s} turns={len(lens):3d} median={st.median(lens):5.1f} mean={st.mean(lens):6.1f} "
          f"max={max(lens):4d} turns>=60w={long60} ({100 * long60 / len(lens):.0f}%)")
dw = sorted([t for t in turns if t['spk'] == 'DWYER IC'], key=lambda t: -len(words(t['text'])))[:5]
print("  Commissioner's five longest turns:",
      [(mmss(t['start']), len(words(t['text'])), round(t['end'] - t['start'])) for t in dw])

# ---- pattern families ----
PAT = {
 'CLARIFY (other-initiated repair)': r"\bsorry\?|\bpardon\b|what do you mean|what are you (saying|talking)|i don'?t (follow|understand)|i'?m not (following|sure what)|not with you|say that again|what am i looking at|you've lost me|i'?m (confused|lost)",
 'CANDIDATE UNDERSTANDING (formulation)': r"do you mean|you mean\b|tell me if i'?ve got (this|that) wrong|so you say|you say that|so you'?re saying|what you'?re saying|if i understand|i understand the case|is that what you|is that right|is that correct|what you'?re getting at",
 'COMPREHENSION CHECK': r"\bokay\?|\ball right\?|\bright\?|do you understand|you follow|does that make sense|with me\?|do you see|you see what i",
 'REDIRECT / ANSWER-THE-QUESTION': r"answer my question|yes or no|move on|come back to|direction this is going|that's not what i asked|my question (is|was)|listen to (my|the) question",
 'CLAIM OF UNDERSTANDING': r"\bi understand\b|\bi see\b|\bunderstood\b|\bi take (your|the) point|\bi get (it|that|what)|\bi appreciate (that|what)",
}
print()
for name, rx in PAT.items():
    print(f"== {name}")
    tally = {p: 0 for p in spk}
    for s in segs:
        for m in re.finditer(rx, s['text'], flags=re.I):
            tally[s['spk']] += 1
            lo = max(0, m.start() - 70); hi = min(len(s['text']), m.end() + 50)
            print(f"   {mmss(s['start'])} {s['spk']:12s} ...{s['text'][lo:hi]}...")
    print("   TALLY (raw):", tally)
    print()

# ---- Ms Matheson's turns ----
print("== MS MATHESON: each turn, and the turn before it")
for i, t in enumerate(turns):
    if t['spk'] == 'MS MATHESON':
        prev = turns[i - 1]
        print(f" {mmss(t['start'])} after {prev['spk']} ({len(words(prev['text']))}w, last words: "
              f"'...{prev['text'][-90:]}')")
        print(f"     SHE: {t['text']}")
