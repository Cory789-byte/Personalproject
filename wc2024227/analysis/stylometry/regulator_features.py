# Each Regulator communication becomes one data point: word features (counted by rule) and
# structural features (hand-coded by the rules below). Texts come from matheson_style.py.
import re, csv, os, statistics as st
here=os.path.dirname(os.path.abspath(__file__))
ns={}; exec(open(os.path.join(here,"matheson_style.py")).read().split("def words")[0], ns); T=ns["T"]
FULL=[k for k in T if "opening only" not in k]          # full texts only
# ---- word features (regular expressions, case-insensitive unless noted)
LEX={
 "contest":   r"\b(den(y|ies|ied)|defend(s|ed|ing)?|maintain(s|ed)?|contend(s|ed)?|reject(s|ed)?|does not accept|oppose[sd]?)\b",
 "formula":   r"position remains to defend|we will be defending the appeal",
 "reserve":   r"reserves? (the|its) right|not an admission|should not be read as|de novo|notwithstanding",
 "legal":     r"in lieu of|in the first instance|undertaking|in receipt of|notwithstanding|pursuant to|for the purposes of|de novo|admissib|admission|concession|waiver|inference|characterisation|tender|rule 49|consent orders|without admission|review its position",
 "apology":   r"\b(apologi[sz]e[sd]?|apologies|sorry)\b",
 "warmth":    r"\b(thank(s|fully)?|appreciate[sd]?|assistance)\b",
 "hedge":     r"\b(believes?|would|could|may|might)\b|in the first instance|if needed|where practicable|in the hopes",
 "soft_promise": r"as soon as possible|this week|noting your requested timeframe",
 "dated_promise": r"respond by|\bas requested\b",
 "merits":    r"reasonabl|management action|section 32|\bs ?32\b|causation|stressor",
 "exit":      r"review its position|consent order|without admission|conced",
}
# ---- structural features, hand-coded: give = gives something concrete (documents, dates, confirmation,
# attendance) before or without asking; ask = asks the reader for something; defer = puts an answer off
# to a later time, person or forum. Latency = days from the message answered. Compose = seconds from
# creation to sending, new threads only (replies are not testable).
META={
"B01 2025-07-14 Cory":     dict(give=1,ask=1,defer=0,lat="",  comp=""),
"B02 2026-02-12 Cory":     dict(give=1,ask=0,defer=0,lat=0,   comp=""),
"B03 2026-02-17 Registry": dict(give=0,ask=1,defer=0,lat=0,   comp=549),
"B04 2026-02-18 Cory":     dict(give=0,ask=0,defer=0,lat=1,   comp=""),
"B05 2026-03-20 Cory":     dict(give=1,ask=0,defer=0,lat="",  comp=""),
"B06 2026-06-11 Cory":     dict(give=1,ask=0,defer=0,lat="",  comp=455),
"B07 2026-07-16 Cory":     dict(give=0,ask=0,defer=0,lat=15,  comp=""),
"B08 2026-08-03 Cory":     dict(give=0,ask=0,defer=1,lat=10,  comp=""),
"B09 2026-08-06 Registry": dict(give=1,ask=0,defer=0,lat="",  comp=101),
"B10 2026-08-14 Cory":     dict(give=1,ask=0,defer=0,lat=21,  comp=""),
"B11 2026-08-14 Cory":     dict(give=0,ask=0,defer=0,lat=14,  comp=""),
"B12 2026-09-08 Cory":     dict(give=1,ask=0,defer=0,lat=11,  comp=""),
"L1 2026-09-08 letter":    dict(give=0,ask=0,defer=0,lat=11,  comp=""),
"B13 2026-09-10 Cory":     dict(give=0,ask=1,defer=1,lat=1,   comp=""),
"B14 2026-09-24 Cory":     dict(give=1,ask=0,defer=1,lat=15,  comp=20),
"B15 2026-09-24 Registry": dict(give=1,ask=0,defer=0,lat="",  comp=5847),
"B16 2026-10-07 Cory":     dict(give=0,ask=0,defer=1,lat=0,   comp=""),
"B17 2026-10-12a Cory":    dict(give=1,ask=0,defer=0,lat=18,  comp=""),
"S1 2026-10-12b Registry": dict(give=1,ask=1,defer=1,lat=11,  comp=10),
"T1 2026-10-16 Cory":      dict(give=1,ask=0,defer=0,lat=9,   comp=""),
"T2 2026-10-19 Cory":      dict(give=1,ask=1,defer=0,lat=6,   comp=""),
"T3 2026-10-20a Registry": dict(give=1,ask=0,defer=0,lat=0.7, comp=""),
"T4 2026-10-20b Cory":     dict(give=1,ask=0,defer=0,lat=0.7, comp=""),
}
def words(t): return re.findall(r"[A-Za-z][A-Za-z']*", t)
rows=[]
for k in sorted(FULL,key=lambda k: re.search(r"\d{4}-\d{2}-\d{2}[ab]?",k).group(0)):
    t=T[k]; n=len(words(t)); date=re.search(r"\d{4}-\d{2}-\d{2}",k).group(0)
    d={"email":k,"date":date,"phase":"before admissions" if date<"2026-08-28" else "after admissions","words":n}
    for f,rx in LEX.items(): d[f]=len(re.findall(rx,t,flags=re.I))
    d["legal_per100"]=round(100*d["legal"]/n,1)
    d.update(META[k]); rows.append(d)
with open(os.path.join(here,"regulator_comms_features.csv"),"w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
cols=["contest","formula","apology","warmth","soft_promise","dated_promise","reserve","legal_per100","merits","exit","give","ask","defer","lat","comp"]
print(f"{'email':24}"+"".join(f"{c[:8]:>9}" for c in cols))
for r in rows: print(f"{r['email'][:24]:24}"+"".join(f"{str(r[c]):>9}" for c in cols))
print("\nBy phase (share of communications with the feature; latency median in days)")
for ph in ["before admissions","after admissions"]:
    R=[r for r in rows if r["phase"]==ph]; n=len(R)
    sh=lambda f: f"{sum(1 for r in R if r[f])}/{n}"
    lats=[r["lat"] for r in R if r["lat"]!=""]
    print(f"  {ph:18} n={n}: contest {sh('contest')}, formula {sh('formula')}, apology {sh('apology')}, warmth {sh('warmth')}, soft promise {sh('soft_promise')}, dated promise {sh('dated_promise')}, reservation {sh('reserve')}, legal idiom {sh('legal')}, merits words {sh('merits')}, exit words {sh('exit')}, gives {sh('give')}, defers {sh('defer')}; latency median {st.median(lats) if lats else '-'} d (range {min(lats)}-{max(lats)})")
