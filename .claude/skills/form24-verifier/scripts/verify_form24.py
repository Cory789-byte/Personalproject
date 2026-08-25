#!/usr/bin/env python3
"""WC/2024/227 - deterministic verification battery for the Form 24 set (layer L1).

Run from wc2024227/drafts/:  python3 ../../.claude/skills/form24-verifier/scripts/verify_form24.py
Exit 0 = green. Any FAIL line = exit 1. See the skill's SKILL.md for the full architecture.
"""
import json, os, re, subprocess, sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
FAILS = []
def ok(msg): print(f"  ok    {msg}")
def fail(msg): FAILS.append(msg); print(f"  FAIL  {msg}")

def norm_soft(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    return ' '.join(t.split())
LIG = {'\ufb00':'ff','\ufb01':'fi','\ufb02':'fl','\ufb03':'ffi','\ufb04':'ffl'}
def deligature(t):
    for k,v in LIG.items(): t = t.replace(k, v)
    return t
def norm_hard(t):
    return ' '.join(re.sub(r'[^a-z0-9 ]', ' ', deligature(t).lower()).split())
def nospace(t):
    return norm_hard(t).replace(' ', '')
def present(q, FLAT, NOSP):
    """Quote present in the corpus, tolerating one page-break interruption
    (footers/page numbers interleave when a sentence spans bundle pages)."""
    if norm_hard(q) in FLAT: return True
    qs = nospace(q)
    if qs in NOSP: return True
    lo, hi = 0, len(qs)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if qs[:mid] in NOSP: lo = mid
        else: hi = mid - 1
    return lo >= 30 and (len(qs) - lo < 20 or qs[lo:] in NOSP)
def pdftext(path, first=None, last=None):
    cmd = ['pdftotext', '-layout']
    if first: cmd += ['-f', str(first), '-l', str(last or first)]
    return subprocess.run(cmd + [path, '-'], capture_output=True, text=True).stdout

# ---------- L0: extraction ----------
src = open('build_form24_second.py').read()
_blk = src[src.index('R_TAYLOR ='):src.index('\n]\n', src.index('FACTS = ')) + 2]
_ren = src[src.index('import re as _re'):src.index('_L, _relab') + len('_L, _relab')]
g = {}; exec(_blk, g, g); exec(_ren, g, g)
facts, sec, last = [], None, None
for f in g['FACTS']:
    if isinstance(f[0], str):
        sec = f[0]; continue
    s = f[2]
    if s == 'As above': s = last
    elif s.startswith('As above;'): s = s.replace('As above', last, 1)
    else: last = s
    facts.append({'n': f[0], 'sec': sec, 't': f[1], 's': s})
letters = [f[0] for f in g['FACTS'] if isinstance(f[0], str)]
print(f"L0  extracted {len(facts)} facts, {len(letters)} sections")

a = open('build_form24_annexureA.py').read()
_i = a.index('ITEMS = ['); _j = a.index('\n]\n', _i) + 2
ns = {}; exec(a[_i:_j], ns, ns)
ITEMS = ns['ITEMS']; TABSET = {str(t) for t, *_ in ITEMS}

# ---------- L1.1 numbering ----------
print("L1.1 numbering")
nums = [f['n'] for f in facts]
if 0 in nums: fail("zero-numbered fact reached extraction")
elif nums == list(range(1, len(nums) + 1)): ok(f"facts 1-{len(nums)} sequential, no gaps")
else: fail(f"numbering not sequential: {[x for x in nums if nums.count(x)>1] or 'gaps present'}")
exp = [chr(ord('A') + i) for i in range(len(letters))]
ok("sections " + letters[0] + "-" + letters[-1] + " sequential") if letters == exp else fail(f"section letters not sequential: {letters}")

# ---------- L1.2 duplicates & repeated quotes ----------
print("L1.2 duplicates")
allow = set(json.load(open(os.path.join(HERE, 'repeat_allowlist.json')))['allow'])
seen, quotes = {}, {}
for f in facts:
    k = norm_hard(f['t']); seen.setdefault(k, []).append(f['n'])
    parts = f['t'].split('"')
    for qi in range(1, len(parts), 2):
        if len(parts[qi]) >= 35: quotes.setdefault(norm_hard(parts[qi]), []).append(f['n'])
d = [v for v in seen.values() if len(v) > 1]
fail(f"exact duplicate facts: {d}") if d else ok("no exact duplicates")
r = {k: sorted(set(v)) for k, v in quotes.items() if len(set(v)) > 1 and k not in allow}
fail(f"repeated quotes not allowlisted: {list(r.values())}") if r else ok("repeated quotes all allowlisted")

# ---------- L1.3 tab citations exist ----------
print("L1.3 tab citations")
bad = []
for f in facts:
    for m in re.findall(r'Annexure A Tabs? ([0-9A-C]+(?:[,\- ]+(?:and )?[0-9A-C]+)*)', f['s']):
        for t in re.split(r'[,\-]|and', m):
            if t.strip() and t.strip() not in TABSET: bad.append((f['n'], t.strip()))
fail(f"facts citing nonexistent tabs: {bad}") if bad else ok(f"all cited tabs exist among {len(TABSET)} tabs")

# ---------- L1.4 quotes present in the bundle ----------
print("L1.4 quotes vs bundle")
img = set(json.load(open(os.path.join(HERE, 'image_tabs.json'))).keys()) - {'_comment'}
QEX = [e['fragment'] for e in json.load(open(os.path.join(HERE, 'quote_exceptions.json')))['exceptions']]
bundle = pdftext('out/FORM24_ANNEXURE_A.pdf')
BFLAT = norm_hard(bundle); BNOSP = nospace(bundle)
miss = []
for f in facts:
    if 'Annexure A Tab' not in f['s']: continue
    flat = set()
    for m in re.findall(r'Annexure A Tabs? ([0-9A-C]+(?:[,\- ]+(?:and )?[0-9A-C]+)*)', f['s']):
        flat |= {x.strip() for x in re.split(r'[,\-]|and', m) if x.strip()}
    if flat and flat <= img: continue
    parts = f['t'].split('"')
    for qi in range(1, len(parts), 2):
        q = parts[qi]
        if len(q) < 30 or '...' in q: continue
        if present(q, BFLAT, BNOSP): continue
        if any(x in q for x in QEX): continue
        if not (flat & img):
            miss.append((f['n'], q[:60])); break
fail(f"tab-cited quotes absent from bundle: {miss}") if miss else ok("every checkable tab-cited quote present in the bundle")

# ---------- L1.5 interval regressions ----------
print("L1.5 interval arithmetic")
def days(a, b): return (datetime.strptime(b, '%Y-%m-%d') - datetime.strptime(a, '%Y-%m-%d')).days
REG = [
 ("response of 1 May 2024 is 23 days", days('2024-04-08', '2024-05-01') == 23),
 ("thirteen minutes and thirty-five seconds",
  (datetime(2024,2,29,11,21,3)-datetime(2024,2,29,11,7,28)).seconds == 13*60+35),
 ("ten days, four hours and forty minutes",
  (datetime(2024,3,1,16,5,8)-datetime(2024,2,20,11,24,48)) == (datetime(2024,3,1,16,5,8)-datetime(2024,2,20,11,24,48)) and
  (datetime(2024,3,1,16,5,8)-datetime(2024,2,20,11,24,48)).days == 10 and
  (datetime(2024,3,1,16,5,8)-datetime(2024,2,20,11,24,48)).seconds//3600 == 4 and
  ((datetime(2024,3,1,16,5,8)-datetime(2024,2,20,11,24,48)).seconds%3600)//60 == 40),
 ("five days, two hours and eighteen minutes",
  (datetime(2024,5,20,14,5)-datetime(2024,5,15,11,47)).days == 5 and
  (datetime(2024,5,20,14,5)-datetime(2024,5,15,11,47)).seconds == 2*3600+18*60),
 ("three hours and two minutes", (datetime(2024,5,20,14,5)-datetime(2024,5,20,11,3)).seconds == 3*3600+2*60),
 ("two hours and twenty-five minutes", (datetime(2024,5,20,16,30)-datetime(2024,5,20,14,5)).seconds == 2*3600+25*60),
 ("approximately thirty-one months", (2025-2023)*12 + (11-4) == 31),
]
alltext = ' '.join(f['t'] for f in facts)
for frag, holds in REG:
    if frag not in alltext: fail(f"regression fragment no longer pleaded: '{frag}'")
    elif not holds: fail(f"arithmetic false for: '{frag}'")
    else: ok(f"'{frag}' pleaded and arithmetically true")

# ---------- L1.6 Part B coverage ----------
print("L1.6 Part B")
pb = open('build_form24_partB.py').read()
used = set()
for m in re.findall(r'\(("?[A-Z]"?(?:,\s*"[A-Z]")*),?\)\),', pb):
    used |= set(re.findall(r'[A-Z]', m))
unc = [L for L in letters if L not in used]
fail(f"Part A sections with no Part B row: {unc}") if unc else ok(f"all {len(letters)} sections covered by Part B")
FACT_FLAT = norm_hard(alltext); FACT_NOSP = nospace(alltext)
_pi = pb.index('ITEMS = ['); _pj = pb.index('\n]\n', _pi) + 2
_pn = {'rng': lambda *a: ''}; exec(pb[_pi:_pj], _pn, _pn)
pbmiss = []
for _limb, _head, _body, _secs in _pn['ITEMS']:
    parts = re.sub(r'<[^>]+>', ' ', _body).split('"')
    for qi in range(1, len(parts), 2):
        q = parts[qi]
        if len(q) < 45 or '...' in q: continue
        if present(q, FACT_FLAT, FACT_NOSP) or present(q, BFLAT, BNOSP): continue
        if any(x in q for x in QEX): continue
        pbmiss.append((_limb, q[:60]))
fail(f"Part B quotes not found in Part A or bundle: {pbmiss}") if pbmiss else ok("every long Part B quote traces to Part A or the bundle")

# ---------- L1.7 outputs: metadata + zero-render + mock ----------
print("L1.7 outputs")
import pikepdf
for f in ['out/FORM24_COMPLETED_OFFICIAL_FORM.pdf', 'out/FORM24_ANNEXURE_A.pdf',
          'out/FORM24_PART_B_SUMMARY.pdf', 'out/FORM24_MOCK_RESPONSE.pdf']:
    if not os.path.exists(f): fail(f"missing output {f}"); continue
    p = pikepdf.open(f)
    if dict(p.docinfo) or '/Metadata' in p.Root: fail(f"metadata not stripped: {f}")
    else: ok(f"metadata stripped: {f} ({len(p.pages)}pp)")
served = pdftext('out/FORM24_COMPLETED_OFFICIAL_FORM.pdf')
z = len(re.findall(r'^\s*0\s+[A-Z]', served, re.M))
fail(f"{z} zero-numbered rows render in the served form") if z else ok("no zero-numbered rows in the served form")
mock = subprocess.run([sys.executable, 'build_form24_mock_response.py'], capture_output=True, text=True)
m = re.search(r'denied (\d+)', mock.stdout)
if not m: fail("mock response did not report a denial count")
elif m.group(1) != '0': fail(f"MOCK RETURNS {m.group(1)} DENIALS - narrow or delete the deniable facts")
else: ok("mock response: zero denials (" + mock.stdout.strip().splitlines()[-1].strip() + ")")

print()
if FAILS:
    print(f"RED: {len(FAILS)} failure(s)"); sys.exit(1)
print("GREEN: all deterministic checks passed"); sys.exit(0)
