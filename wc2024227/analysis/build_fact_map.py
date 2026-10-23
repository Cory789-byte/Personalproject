import json,re
F={x['n']:x['t'] for x in json.load(open('facts_served_303.json'))}
def R(a,b): return list(range(a,b+1))
# primary placement: group code -> facts (in strategic order)
G=[
("L1-A","The role: 24/7, emergency codes, database, judgement without procedures",R(1,13)),
("L1-B","Continuous shift worker throughout",R(14,16)),
("L1-C","Critical function admitted",[289]),
("L1-D","The life-safety load on 17-19 March (register not admitted; employer says a MET-call spreadsheet exists)",[268]+R(228,231)),
("L1-E","He took the responsibility on willingly; clean record",R(30,38)+R(300,302)),
("L2-A","Database access removed July 2023, never restored",R(39,48)+[55]),
("L2-B","Contact/number and Communication Book removed",R(143,154)+[288,292]),
("L2-C","Manager's hours undefined while every directive said 'contact me in office hours'",[70,71,72,73,81,82,83,84,88,85,86,87]),
("L2-D","Directives issued without consultation",R(49,54)+[181,273,66,67,101,277,278,279]),
("L2-E","Misrouting, the directory, and 'a procedure in place'",R(56,65)+[68,69,111,112,113]+R(89,93)+R(94,99)+[100]+R(102,110)+[290,291]),
("L2-F","How to report unavailability: via the Switchboard, never told otherwise",R(162,166)+[294]),
("L3-A","The 7-hour break of 17-18 March 2024",[284,285,257,258,259,260,227,226,180,239,240,241,251]),
("L3-B","The 2020 agreement: signed under a different manager, for swaps only, never reviewed",[17,18,19,20,21,22,23,24,25,224,225,232,233,234,252,253,254,286]),
("L3-C","Sick leave on 19 March 2024",R(235,237)),
("L3-D","The fatigue request: 23 days",R(242,250)),
("L3-E","No fatigue risk management before 30 June 2024",R(263,265)+R(269,271)),
("L3-F","Pay: wrong for four fortnights, AVAC 25 days later",R(182,210)+[255,256,296,297,298,299]),
("L3-G","Pandemic leave: declined twice, approved in 13 min 35 s",R(114,142)),
("L3-H","Rostering errors repeated",[156,157,287,159]),
("L3-I","The Review Unit's own conclusion",[261,262,295]),
("L4-A","August 2023: raised, redirected, grievance offered",[26,27,28,29,155,158,160,161]),
("L4-B","April-May 2024: roster and fatigue concerns",R(211,223)),
("L4-C","15 May 2024: the hours email, retraction, 'I will follow up'",R(74,80)),
("L4-D","The complaint system: email or verbal, to the line manager only; nothing changed",[266,267,272]),
("CTX-U","Union context (reserve; 1(g) only)",[31,32]+R(167,179)+[293]),
("REC","The contemporaneous account and the pleadings record",[274,275,276,280,281,282,283,238,303]),
]
# move 31,32 out of L1-E (they're in CTX-U)
G[4]=(G[4][0],G[4][1],[n for n in G[4][2] if n not in (31,32)])
seen={}
for code,_,ns in G:
  for n in ns:
    assert n not in seen,(n,code,seen.get(n)); seen[n]=code
missing=[n for n in range(1,304) if n not in seen]
print('missing',missing)
NA={154,228,229,230,231}
HELD={292,159}
# interlocks: fact -> other limbs it serves
IL={6:"L2",8:"L3",2:"L3",13:"L3",44:"L1",45:"L1",55:"L1",289:"L2",268:"L3",228:"L3",229:"L3",230:"L3",231:"L3",
 33:"L3",34:"L3",
 70:"L4",71:"L4",72:"L4",73:"L4",81:"L4",88:"L4",96:"L4",103:"L4",85:"L1",86:"L1",
 75:"L2",78:"L2",79:"L2",80:"L2",
 94:"L4",97:"L4",98:"L4",100:"L4",101:"L4",89:"L4",91:"L4",90:"L4",93:"L4",
 162:"L3,L4",165:"L3",166:"L4",
 68:"L1",67:"L1",58:"L1",
 211:"L3",212:"L3",213:"L3",214:"L3",215:"L3",216:"L3",218:"L3",219:"L3",220:"L3",221:"L3",222:"L3",223:"L3",
 156:"L4",157:"L4",287:"L4",
 225:"L2",234:"L2",249:"L4",250:"L4",246:"L4",244:"L4",
 193:"L4",195:"L4",
 260:"L4",267:"L2",272:"L2",
 300:"L4",301:"L4",302:"L4",
 264:"L1",269:"L1",270:"L1",271:"L1",
 277:"L2",278:"L2",279:"L2,L4",
 180:"L2",181:"L3",
}
def short(t):
  t=re.sub(r'\s+[A-Z] [A-Z0-9 ,()\'\-:.]+$','',t) if False else t
  t=re.sub(r'( (Not admitted|Admitted))+( |$)',' ',t)
  t=re.sub(r' [A-S] (STRESSOR|THE |MATTERS|FACTS|PART).*$','',t)
  t=re.sub(r' PART (ONE|TWO|THREE|FOUR|FIVE).*$','',t)
  t=t.replace("The Respondent's amended statement of facts and contentions dated 13 May 2026, as presently constituted, ","SOFC ")
  t=t.replace("The Respondent's amended List of Documents dated 14 August 2026 ","LOD ")
  t=t.replace("Review Decision 69983 of the Workers' Compensation Regulator, dated 24 October 2024, ","RD ").replace("Review Decision 69983 dated 24 October 2024 ","RD ").replace("Review Decision 69983 ","RD ")
  t=re.sub(r'\s*\(Annexure A, (Tabs? [^)]*)\)',r' [\1]',t).strip()
  return t if len(t)<=230 else t[:227].rstrip()+'…'
out=["| Fact | Primary | Also serves | Status | Text (condensed; quote only from the served response) |","|---|---|---|---|---|"]
for n in range(1,304):
  st="**Not admitted**" if n in NA else ("Admitted · held for XX" if n in HELD else "Admitted")
  out.append(f"| {n} | {seen[n]} | {IL.get(n,'')} | {st} | {short(F[n]).replace('|','/')} |")
open('fact_map_appendix.md','w').write("\n".join(out)+"\n")
from collections import Counter
c=Counter(v[:2] for v in seen.values()); print(c, len(IL))
for code,t,ns in G: print(code,len(ns))
