"""Overlay matrix: every served fact x every pleaded stressor (home + carried-in). 1(e) excluded."""
import json, re, html
F = {x['n']: x['t'] for x in json.load(open('facts_served_303.json'))}
R = lambda a, b: list(range(a, b + 1))
COLS = ['1a', '1b', '1c', '1d', '1f', '1g', '2', '3ab', '3c', '3d']
LAB = {'1a': '1(a) directives/misrouting', '1b': '1(b) comm book', '1c': '1(c) Aug 2023', '1d': '1(d) pandemic leave',
       '1f': '1(f) 15 May email', '1g': '1(g) union (reserve)', '2': '2 pay', '3ab': '3(a)-(b) 7-hr break / minimum',
       '3c': '3(c) agreement / 19 Mar', '3d': '3(d) Review Decision'}
home = {}
def H(ns, s):
    for n in ns: home[n] = s
H(R(1, 13), 'role'); H(R(14, 16), '3ab'); H(R(17, 25), '3c'); H(R(26, 38), 'ctx'); H(R(39, 113), '1a'); H(R(74, 80), '1f')
H(R(114, 142), '1d'); H(R(143, 154), '1b'); H(R(155, 161), '1c'); H(R(162, 166), '1a'); H(R(167, 181), '1g')
H(R(182, 210), '2'); H(R(211, 223), '3ab'); H([224, 225], '3ab'); H(R(226, 231), '3ab'); H(R(232, 237), '3c'); H([238], 'all')
H(R(239, 241), '3ab'); H(R(242, 254), '3c'); H([255, 256], '2'); H(R(257, 262), '3d'); H(R(263, 266), '3ab'); H([267, 268], '1a')
H(R(269, 271), '3ab'); H([272, 273], '1a'); H(R(274, 282), 'rec'); H([283], 'rec'); H([284], '3ab'); H([285], '3ab'); H([286], '3c')
H([287], '1c'); H([288, 292], '1b'); H(R(289, 291), '1a'); H([293], '1g'); H([294], '1a'); H([295], '3d'); H(R(296, 299), '2'); H(R(300, 303), 'all')
carry = {
 '1a': [2, 6, 8, 9, 13, 289, 290, 291, 162, 163, 164, 165, 166, 294, 181, 273, 211, 212, 213, 216, 193, 194, 195, 267, 272, 268, 277, 278, 279, 282, 281],
 '1b': [45, 267, 289, 12, 158],
 '1c': [26, 27, 28, 29, 287, 220, 211, 212, 213, 218, 219, 221, 239, 240, 264, 269, 270, 271, 272],
 '1d': [199, 200, 201, 205, 206, 226, 162, 163, 164, 165, 166],
 '1f': R(70, 73) + R(81, 84) + [88, 50, 162, 163, 164, 165, 158, 267],
 '1g': [31, 32, 36] + R(49, 53),
 '2': [242, 246, 249, 28, 18, 19, 20, 30, 37, 38, 241],
 '3ab': [2, 8, 13, 268, 156, 157, 28, 287, 220, 180, 257, 52, 135],
 '3c': R(17, 25) + [225, 234, 188, 227] + R(242, 246),
 '3d': [18, 19, 20, 46, 47, 48, 54] + R(136, 139) + R(242, 256) + [238],
}
ALL = [238, 300, 301, 302, 303, 267, 272, 289]
cell = {n: {} for n in F}
for n, s in home.items():
    if s in COLS: cell[n][s] = 'H'
    if s == 'all':
        for c in COLS: cell[n][c] = 'H'
for s, ns in carry.items():
    for n in ns: cell[n].setdefault(s, 'C')
for n in ALL:
    for c in COLS: cell[n].setdefault(c, 'C')
NA = {154, 228, 229, 230, 231}; HELD = {159, 292}; RESERVE = set(R(167, 179)) | {31, 32, 293}
def short(t):
    t = re.sub(r'( (Not admitted|Admitted))+( |$)', ' ', t)
    t = re.sub(r' [A-S] (STRESSOR|THE |MATTERS|FACTS|PART).*$', '', t); t = re.sub(r' PART (ONE|TWO|THREE|FOUR|FIVE).*$', '', t)
    t = t.replace("The Respondent's amended statement of facts and contentions dated 13 May 2026, as presently constituted, ", "SOFC ")
    t = t.replace("The Respondent's amended List of Documents dated 14 August 2026 ", "LOD ").replace("Review Decision 69983 ", "RD ")
    t = re.sub(r'\s*\(Annexure A, (Tabs? [^)]*)\)', r' [\1]', t).strip()
    return t if len(t) <= 170 else t[:167].rstrip() + '…'
rows = sorted(F, key=lambda n: (-len(cell[n]), n))
cnt = {c: [sum(1 for n in F if cell[n].get(c) == 'H'), sum(1 for n in F if cell[n].get(c) == 'C')] for c in COLS}
# markdown
md = ["| Fact | Stressors | " + " | ".join(COLS) + " | Flag | Text |", "|---|---|" + "---|" * len(COLS) + "---|---|"]
for n in rows:
    if not cell[n]: continue
    fl = 'NOT ADMITTED' if n in NA else 'HELD' if n in HELD else 'reserve' if n in RESERVE else ''
    md.append(f"| {n} | {len(cell[n])} | " + " | ".join(cell[n].get(c, '') for c in COLS) + f" | {fl} | {short(F[n]).replace('|','/')} |")
open('2026-09-26_OVERLAY_matrix.md', 'w').write("\n".join(md) + "\n")
none = [n for n in F if not cell[n]]
multi = sorted([n for n in F if len(cell[n]) >= 2])
print('counts', cnt); print('facts in 2+ stressors', len(multi)); print('3+', sum(len(cell[n]) >= 3 for n in F))
print('context/record only', len(none))
# html
col = {'H': 'var(--h)', 'C': 'var(--c)'}
tr = []
for n in rows:
    if not cell[n]: continue
    fl = 'not admitted' if n in NA else 'held' if n in HELD else 'reserve' if n in RESERVE else ''
    tds = "".join(f'<td class="{cell[n].get(c, "")}">{cell[n].get(c, "")}</td>' for c in COLS)
    tr.append(f'<tr data-k="{len(cell[n])}"><th>{n}</th><td class="k">{len(cell[n])}</td>{tds}<td class="fl">{fl}</td><td class="tx">{html.escape(short(F[n]))}</td></tr>')
head = "".join(f'<th title="{LAB[c]}">{c}</th>' for c in COLS)
summ = "".join(f'<tr><td>{LAB[c]}</td><td>{cnt[c][0]}</td><td>{cnt[c][1]}</td><td>{sum(cnt[c])}</td></tr>' for c in COLS)
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Admissions Overlay Matrix</title><style>
:root{{--bg:#fbfaf7;--fg:#1d1d1b;--mut:#6b6a66;--line:#e2e0da;--h:#1f5f8b;--c:#9ec5e0;--ht:#fff;--ct:#0d2d44}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#161615;--fg:#ecebe6;--mut:#a09e97;--line:#34332f;--h:#4a9ad0;--c:#24465e;--ht:#08131c;--ct:#d8e9f5}}}}
:root[data-theme="dark"]{{--bg:#161615;--fg:#ecebe6;--mut:#a09e97;--line:#34332f;--h:#4a9ad0;--c:#24465e;--ht:#08131c;--ct:#d8e9f5}}
body{{background:var(--bg);color:var(--fg);font:14px/1.45 system-ui,sans-serif;margin:0;padding:16px;max-width:1200px}}
h1{{font-size:20px;margin:0 0 4px}} p{{color:var(--mut);margin:4px 0 12px}}
.wrap{{overflow-x:auto;border:1px solid var(--line);border-radius:8px}}
table{{border-collapse:collapse;width:100%}} th,td{{border-bottom:1px solid var(--line);padding:4px 6px;text-align:center;white-space:nowrap}}
td.tx{{text-align:left;white-space:normal;min-width:320px;font-size:13px}} td.fl{{color:#b0552c;font-size:12px}}
td.H{{background:var(--h);color:var(--ht);font-weight:600}} td.C{{background:var(--c);color:var(--ct)}}
thead th{{position:sticky;top:0;background:var(--bg)}} .k{{font-weight:700}}
.ctl{{margin:8px 0 12px}} .sum td{{text-align:left}} .key span{{display:inline-block;width:14px;height:14px;vertical-align:-2px;border-radius:3px;margin:0 4px 0 10px}}
</style></head><body>
<h1>Admissions overlay: every served fact across every stressor</h1>
<p>Internal, not for service. H = the stressor the fact was drafted under; C = carried in from another stressor. Sorted by how many stressors each fact proves. 1(e) is excluded by rule. Quote only from the served response.</p>
<div class="key">Key:<span style="background:var(--h)"></span>home<span style="background:var(--c)"></span>carried in</div>
<div class="ctl"><label>Show facts proving at least <select id="min"><option>1</option><option selected>2</option><option>3</option><option>4</option></select> stressors</label></div>
<div class="wrap"><table class="sum"><tr><th>Stressor</th><th>Home</th><th>Carried in</th><th>Total</th></tr>{summ}</table></div><br>
<div class="wrap"><table><thead><tr><th>Fact</th><th>#</th>{head}<th>Flag</th><th style="text-align:left">Text (condensed)</th></tr></thead><tbody>{''.join(tr)}</tbody></table></div>
<script>const s=document.getElementById('min');function f(){{const m=+s.value;document.querySelectorAll('tbody tr').forEach(r=>r.style.display=(+r.dataset.k>=m)?'':'none')}};s.onchange=f;f();</script>
</body></html>"""
open('2026-09-26_OVERLAY_matrix.html', 'w').write(page)
