#!/usr/bin/env python3
"""Regenerate skill/references/INDEX.md from the notes themselves. Run from wc2024227/."""
import os, re, io
D = 'skill/references'
GROUPS = [
 ('⭐ START HERE — state of play and verified record',
  ('CONFIRMED-RECORD','STATE-OF-PLAY','WHOLE-STORY','MASTER-ALIGNMENT','WORKING-THEORIES','REALIZATION')),
 ('THE APPEAL — case theory, s 32(5), authorities, the pleading',
  ('S32','JUDGMENT','CASE-','PRIZEMAN','MAHAFFEY','DELANEY','RULE-49','RULES-','FORM24','FORM9A','9C-','SOFC','NOTICE-TO-ADMIT',
   'REVIEW-DECISION','RD69983','ONUS','BRIGINSHAW','DEFENCE','MAXIMISING','ORIGINAL-9A','TWO-COLUMN','ROLE-DESCRIPTION',
   'ELEMENT-LEDGER','REGISTER-VS','TRAP','ACCEPTANCE','FRESH-WORKCOVER')),
 ('THE HEARING — plan, witnesses, length, evidence',
  ('HEARING','WITNESS','EVIDENCE-LEDGER','HOURS-AND-PAY','MASPER','STITCHED','TRANSCRIPT','KNOWN-ITEM','LIVED-THE')),
 ('THE RECORD — chronology, sequences, maps',
  ('TIMELINE','CHRONOL','SEQUENCE','CONNECTION','MAP','FATIGUE','THREE-CLOCKS','BIDIRECTIONAL','LONGITUDINAL',
   '28-DAY','FROM-5JUNE','CONVERGENCE','SIGNAL-EXTRACTION','TURNED-WORDS')),
 ('THE MENTION of 7 August 2026',
  ('MENTION','SPEECH','DWYER','PRIOR','BENCH','THE-AI-')),
 ('MEDICAL and causation',
  ('MEDICAL','KRISHNAIAH','DOCTOR','REPORT-','ASHMORE','PSYCH','INJURY','PROGNOSIS','POSITIONING-THE-SINGLE','Q7-','SAFETY-ADVISOR')),
 ('DISCLOSURE, 64G, Form 29',
  ('64G','DISCLOS','NNPD','LOD','PRODUCTION','METADATA','FORENSIC','MSH-DOCUMENT','MSH-CITATIONS','MIRROR','RECALLED-EMAIL')),
 ('EMPLOYMENT TRACK — instruments, powers, obligations',
  ('EB1','AWARD','INSTRUMENT','LEAVE','LSL','RFMI','ECC','HUGHES','ROBERTS','POWERS','PROCEDURAL','DIRECTIVE','WHS',
   'GOOD-FAITH','HAZARD','DELEGATE','CONSULTATION','POLICY','PAY-REQUESTS','PUBLIC-ENTITY','WHAT-POWER','STAGE1',
   'DEEMED-REFUSAL','SUSPENSION','DISPLACEMENT','INVERSION','RESPONSE-OBLIGATIONS','DISCRETION','EAP','LETTER-FOUNDATION')),
 ('PID / reprisal track (⛔ off the WC track — discipline rules 1, 2, 8)',
  ('PID','REPRISAL','ESU','HOPGOOD','PROTECTED-ACTS','WHO-INVESTIGATES')),
 ('SETTLEMENT, funding, deed, costs',
  ('DEED','CALDERBANK','SETTLE','COST','ALTIUS','QSUPER','FUNDING','LONG-PATH','STRATEGIC-OPTIONS','WHAT-ACCEPTANCE')),
 ('RED TEAM, prediction and assessment',
  ('RED-TEAM','REDTEAM','ASSESS','FULL-PICTURE','SPECTRUM','BENCHMARK','AUDIT','VERIFICATION','PLAYBOOK','PREDICTIVE',
   'WHAT-EACH-PARTY','WHY-IT-READS','REVIEW-OF-THEIR','TACTICS','DONE-PROPERLY')),
]
def bucket(fn):
    u = fn.upper()
    for name, keys in GROUPS:
        if any(k in u for k in keys): return name
    return 'OTHER'
rows = {}
for fn in sorted(os.listdir(D)):
    if not fn.endswith('.md') or fn == 'INDEX.md': continue
    p = os.path.join(D, fn)
    txt = io.open(p, encoding='utf-8', errors='replace').read()
    lines = txt.split('\n')
    title = next((l.lstrip('# ').strip() for l in lines if l.startswith('#')), fn)
    prov  = next((l.lstrip('> ').strip() for l in lines if l.startswith('>')), '')
    kb = round(os.path.getsize(p)/1024)
    rows.setdefault(bucket(fn), []).append((fn, kb, title, prov))
out = ["# Reference index — generated, do not hand-edit",
       "> Regenerate: `python3 scripts/build_reference_index.py` from `wc2024227/`.",
       f"> {sum(len(v) for v in rows.values())} notes. The first blockquote line of each note is its provenance line.", ""]
for name, _ in GROUPS + [('OTHER', ())]:
    if name not in rows: continue
    out.append(f"## {name}  ({len(rows[name])})")
    out.append("")
    for fn, kb, title, prov in sorted(rows[name], key=lambda r: -r[1]):
        out.append(f"- **`{fn}`** · {kb}KB — {title}")
        if prov: out.append(f"  <br><sub>{prov[:170]}</sub>")
    out.append("")
io.open(os.path.join(D, 'INDEX.md'), 'w', encoding='utf-8').write('\n'.join(out))
print(f"INDEX.md written — {sum(len(v) for v in rows.values())} notes in {len(rows)} groups")
for k, v in rows.items(): print(f"  {len(v):>3}  {k}")
