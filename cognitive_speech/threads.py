import json,re,sys,statistics as st
def tag(text,LEX):
    t=text.lower(); return [k for k,rx in LEX.items() if re.search(rx,t)]
def turns(segs):
    out=[];cur=None
    for s in segs:
        if s['spk'] is None: continue
        if cur and s['spk']==cur['spk'] and s['start']-cur['end']<2.0: cur['segs'].append(s); cur['end']=s['end']
        else: cur={'spk':s['spk'],'start':s['start'],'end':s['end'],'segs':[s]}; out.append(cur)
    return out
def analyse(segs,me,LEX,minwords=40):
    T=turns(segs); seen_by_me=set(); res=[]; carry=0; carry_total=0
    for i,t in enumerate(T):
        seq=[]
        for s in t['segs']:
            for k in tag(s['text'],LEX):
                if not seq or seq[-1]!=k: seq.append(k)
        t['seq']=seq; t['words']=sum(len(s['text'].split()) for s in t['segs'])
        if t['spk']!=me: continue
        prev_other=' '.join(s['text'] for s in T[i-1]['segs']) if i>0 else ''
        prompted=set(tag(prev_other,LEX))
        new_unprompted=[k for k in set(seq) if k not in prompted]
        carried=[k for k in new_unprompted if k in seen_by_me]  # brought back from earlier own talk, not prompted
        carry+=len(carried); carry_total+=len(set(seq))
        seen_by_me|=set(seq)
        if t['words']>=minwords:
            distinct=len(set(seq)); switches=max(0,len(seq)-1)
            returns=sum(1 for j,k in enumerate(seq) if k in seq[:j])
            res.append({'t':f"{int(t['start']//60)}:{int(t['start']%60):02d}",'dur':round(t['end']-t['start'],1),'words':t['words'],
                        'threads':distinct,'switches':switches,'returns':returns,'unprompted_carryover':carried,'seq':seq})
    return res,carry,carry_total
def summary(res,carry,ct,label):
    if not res: return
    print(f"\n== {label}: long turns (>=40 words): {len(res)}")
    print(" threads per long turn: median",st.median(r['threads'] for r in res),"max",max(r['threads'] for r in res))
    print(" topic switches per turn: median",st.median(r['switches'] for r in res),"max",max(r['switches'] for r in res))
    print(" returns to an earlier thread within the same turn: total",sum(r['returns'] for r in res))
    print(" words per thread (median)",round(st.median(r['words']/max(1,r['threads']) for r in res),1))
    print(f" unprompted carry-over across the whole recording: {carry} of {ct} thread-mentions ({round(100*carry/max(1,ct))}%)")
    top=sorted(res,key=lambda r:-r['threads'])[:3]
    for r in top: print("  ",r['t'],r['dur'],'s',r['words'],'w',r['threads'],'threads, switches',r['switches'],'returns',r['returns'],'|',' > '.join(r['seq'])[:260])
