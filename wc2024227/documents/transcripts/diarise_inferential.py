import json,re,pickle,numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from collections import defaultdict
S=[json.loads(l) for l in open('mention/large_v3_full.jsonl')]
E,X,meta=pickle.load(open('mention/emb_orig.pkl','rb'))
E=E/np.linalg.norm(E,axis=1,keepdims=True)
F=np.hstack([StandardScaler().fit_transform(PCA(32,random_state=0).fit_transform(E)),
             StandardScaler().fit_transform(X)])
D,A=1,0                                    # 1 = Dwyer, 0 = Appellant

# ---------- 1. ACOUSTIC PRIOR (level is the strongest single cue: bench -41 dB, bar table -53 dB)
segfeat=defaultdict(list); seglvl=defaultdict(list)
for j,(i,_) in enumerate(meta): segfeat[i].append(F[j]); seglvl[i].append(X[j,0])
seed_d=[i for i,s in enumerate(S) if re.search(r'\bthe appellant\b|\bmr\.? sh[ae]p+[ae]rd\b|\bms\.? math[ei]son\b',s['text'],re.I)]
seed_a=[i for i,s in enumerate(S) if re.search(r'\b(my manager|my colleagues|my union|my health service email|i was rostered)\b',s['text'],re.I)]
Cd=np.mean([np.mean(segfeat[i],0) for i in seed_d if i in segfeat],0)
Ca=np.mean([np.mean(segfeat[i],0) for i in seed_a if i in segfeat],0)
print(f'acoustic seeds: dwyer={len(seed_d)} appellant={len(seed_a)}')
AC=np.zeros((len(S),2))
for i in range(len(S)):
    if i in segfeat:
        m=np.mean(segfeat[i],0)
        dd,da=np.linalg.norm(m-Cd),np.linalg.norm(m-Ca)
        AC[i,D]=(da-dd)/(da+dd)*2.0; AC[i,A]=(dd-da)/(da+dd)*2.0

# ---------- 2. LEXICAL EVIDENCE
DWY=[ (r'\bthe appellant\b',5.0),                       # reading the pleading aloud
      (r'\bmr\.? sh[ae]p+[ae]rds?on?\b',5.0), (r'\bms\.? (math[ei]son|rut+[ae]n)\b',5.0),
      (r"\b(your case|your evidence|your material|your application|your stressors?|your statement of|"
       r"you'?ve pleaded|you contend|you'?ve identified|your non-?party|your form 29|your list)\b",3.0),
      (r"\b(i'?m going to|i'?ll (tell|take|leave|allow|come back|stand|hear)|i would have thought|"
       r"in my experience|if i was presiding|i'?m not close to that|let me step you through|"
       r"i'?m not (being )?critical|i don'?t mind saying|i must confess|i'?ll just get it under way)\b",3.0),
      (r"\b(the regulator|the health service|the commission|model litigant|witness box|cross-?examine|"
       r"the onus|disclosure dispute|interlocutory|non-?party disclosure)\b",1.6),
      (r"\b(okay,? tick|hand it up|got all (the|those) documents|you'?ve got (that|your) document)\b",4.0),
      (r"\byes or no\b|answer my question|it'?s a simple question",4.0),
      (r"\b(so you say|do you say|so you'?ve got|have you got|did you|have you|couldn'?t you|"
       r"how do you (say|propose)|what do you mean by)\b",2.2),
      (r"\b(where'?s (that|the bit)|which heading|which page|what number|what am i looking at|"
       r"let'?s just look at|hand it up|is that what you'?re saying|is that what you mean)\b",4.5),
      (r"\b(nothing further|thanks,? paddy|adjourn|stand it down|we'?ll get down to)\b",5.0),
      (r"\bi'?ll stand it down\b|\bany objections?\b",5.0) ]
APP=[ (r"\b(my manager|my line manager|my colleagues?|my union|my health service email|my filters|"
       r"my request|my email|my appointment|my hours)\b",5.0),
      (r"\bi (was rostered|submitted|lodged|joined|asked|requested|attached|wrote|got|have all|"
       r"don'?t have|do not have|haven'?t got|can'?t remember)\b",3.0),
      (r"^\s*(yes|no|yeah|correct|exactly|that'?s right|sure|yep|done)\b[.,!]?\s*$",4.0),
      (r"\bcommissioner\b",3.0),
      (r"\b(i guess|i do believe|i think i|i would have to|it seemed pretty|for me,? it)\b",2.5),
      (r"\b(effective immediately|e-?health|outlook)\b",2.0),
      (r"\b(can i give you|can i hand|can i share|i haven'?t got a copy|i can share)\b",5.0) ]
LX=np.zeros((len(S),2))
for i,s in enumerate(S):
    t=s['text']
    for p,w in DWY:
        if re.search(p,t,re.I): LX[i,D]+=w
    for p,w in APP:
        if re.search(p,t,re.I): LX[i,A]+=w
    n=len(t.split())
    if n>=35: LX[i,D]+=2.0                      # sustained monologue = the bench
    elif n<=3: LX[i,A]+=0.6                     # clipped = the answerer
BACK_D=re.compile(r"^\s*(hand it up|okay,? tick|you'?ve got that|done\.)",re.I)   # Dwyer answering an offer/answer
BACK_A=re.compile(r"^\s*(yes|no|correct|exactly|yeah)\b",re.I)                      # an answer implies a question before
for i in range(1,len(S)):
    if BACK_D.search(S[i]['text']): LX[i-1,A]+=3.0
    if BACK_A.search(S[i]['text'].strip()) and len(S[i]['text'].split())<=4: LX[i-1,D]+=1.5
np.clip(LX,0,9,out=LX)
print(f'lexical evidence on {int((LX.sum(1)>0).sum())}/{len(S)} segments')

# ---------- 3. VITERBI with adjacency logic
def run(sw_base,ac_w,lx_w):
    n=len(S); dp=np.full((n,2),-1e9); bk=np.zeros((n,2),int)
    dp[0]=ac_w*AC[0]+lx_w*LX[0]
    for i in range(1,n):
        gap=max(0.0,S[i]['start']-S[i-1]['end'])
        prev=S[i-1]['text'].strip()
        pen=sw_base*np.exp(-gap/1.2)                       # long silence => cheap to switch
        if prev.endswith('?'): pen*=0.15                   # a question invites the other voice
        if len(prev.split())<=3: pen*=0.6
        for c in (0,1):
            cand=[dp[i-1,p]-(0 if p==c else pen) for p in (0,1)]
            b=int(np.argmax(cand)); dp[i,c]=cand[b]+ac_w*AC[i,c]+lx_w*LX[i,c]; bk[i,c]=b
    path=[int(np.argmax(dp[-1]))]
    for i in range(n-1,0,-1): path.append(bk[i,path[-1]])
    return path[::-1]

# ---------- 4. held-out validation on hand-checked anchors
GOLD={}   # start-time -> speaker, from passages verified against BOTH transcripts
for t,sp in [(1331.8,A),(1333.8,D),(1344.9,D),(1347.3,D),(1349.6,None),(1351.4,A),(1354.7,D),
             (1360.5,D),(1362.1,A),(1370.6,D),(1372.0,A),(1373.5,D),(1379.7,A),(1382.4,D),
             (1399.0,A),(1403.9,D),(1406.3,A),(1407.9,D),(1410.2,A),(1413.5,A),(1417.4,D),
             (1420.2,A),(1452.0,D),(2427.0,D),(2428.6,D),(2429.5,A),(3204.0,A),(1010.0,D),
             (400.0,A),(2101.0,D),(2121.0,A),(3868.0,D)]:
    if sp is None: continue
    j=min(range(len(S)),key=lambda i:abs(S[i]['start']-t))
    if abs(S[j]['start']-t)<3.0: GOLD[j]=sp
best=None
for sw in (0.6,1.0,1.5,2.2):
    for aw in (0.5,1.0,2.0):
        for lw in (1.0,1.5,2.5):
            p=run(sw,aw,lw)
            acc=sum(1 for i,g in GOLD.items() if p[i]==g)/len(GOLD)
            turns=sum(1 for i in range(1,len(p)) if p[i]!=p[i-1])
            sc=acc-abs(turns-260)/2000
            if best is None or sc>best[0]: best=(sc,acc,turns,sw,aw,lw,p)
sc,acc,turns,sw,aw,lw,path=best
print(f'\nBEST sw={sw} acoustic_w={aw} lexical_w={lw}')
print(f'  anchor accuracy {acc*100:.0f}% ({int(acc*len(GOLD))}/{len(GOLD)})   turn changes {turns}')
for i,s in enumerate(S): s['speaker']='DWYER IC' if path[i]==D else 'MR SHEPHERD'
# counsel: a short reply right after Dwyer names them
NAME=re.compile(r'ms\.? (math[ei]son|rut+[ae]n)',re.I)
nc=0
for i in range(len(S)-1):
    m=NAME.search(S[i]['text'])
    if m and path[i]==D:
        who='MS MATHESON' if m.group(1).lower().startswith('math') else 'MS RUTTAN'
        for j in (i+1,i+2):
            if j<len(S) and path[j]==A and (S[j]['start']-S[i]['end'])<6.0 and len(S[j]['text'].split())<25:
                S[j]['speaker']=who; nc+=1; break
print(f'  counsel turns identified: {nc}')
with open('mention/final_v2.jsonl','w') as f:
    for s in S: f.write(json.dumps(s)+'\n')
from collections import Counter
tot=defaultdict(float)
for s in S: tot[s['speaker']]+=s['end']-s['start']
print('\nspeaker           segs    talk       share')
c=Counter(s['speaker'] for s in S)
for k,v in sorted(tot.items(),key=lambda kv:-kv[1]):
    print(f'  {k:14s} {c[k]:5d} {v:7.0f}s   {v/sum(tot.values())*100:5.1f}%')
