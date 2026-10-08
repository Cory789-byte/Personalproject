"""Appendix: every fact grouped under Stressor 1, 2, 3 (home H or carried C), from the overlay mapping."""
import runpy
g = runpy.run_path('build_overlay.py')
F, cell, short, NA, HELD, RES = g['F'], g['cell'], g['short'], g['NA'], g['HELD'], g['RESERVE']
S = {'Stressor 1': ['1a', '1b', '1c', '1d', '1f', '1g'], 'Stressor 2': ['2'], 'Stressor 3': ['3ab', '3c', '3d']}
out = []
for s, cols in S.items():
    ns = [n for n in sorted(F) if any(c in cell[n] for c in cols)]
    out.append(f"\n### {s}: {len(ns)} facts\n\n| Fact | Particular(s) | Other stressors | Flag | Text (condensed) |\n|---|---|---|---|---|")
    for n in ns:
        parts = ", ".join(f"{c}{'' if cell[n][c]=='H' else '*'}" for c in cols if c in cell[n])
        other = ", ".join(k for k, v in S.items() if k != s and any(c in cell[n] for c in v))
        fl = 'NOT ADMITTED' if n in NA else 'HELD' if n in HELD else 'reserve' if n in RES else ''
        out.append(f"| {n} | {parts} | {other} | {fl} | {short(F[n]).replace('|','/')} |")
open('_by_stressor_appendix.md', 'w').write("\n".join(out) + "\n")
for s, cols in S.items():
    print(s, sum(1 for n in F if any(c in cell[n] for c in cols)))
print('in all three', sum(1 for n in F if all(any(c in cell[n] for c in v) for v in S.values())))
print('in two+', sum(1 for n in F if sum(any(c in cell[n] for c in v) for v in S.values())>=2))
