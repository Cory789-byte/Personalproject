"""Response timing, situational awareness, arousal (stress) and recall markers for one target speaker.
segs: list of {start,end,text,spk,pros} in time order. Descriptive speech measures only: not a clinical assessment."""
import re, json, statistics as st, math, sys
import numpy as np
YN = re.compile(r"^\s*(is|are|do|does|did|have|has|had|can|could|would|will|was|were|should|shall|am|may)\b", re.I)
WH = re.compile(r"\b(what|how|why|when|where|who|which)\b", re.I)
RECALLQ = re.compile(r"\b(remember|recall|when did|what date|what time|how long|have you got|do you have|did you|where were|what happened)\b", re.I)
CHALLENGE = re.compile(r"\b(yes or no|answer (my|the) question|just answer|hang on|stop|let me finish|no,? no|that'?s not|i'?m asking)\b", re.I)
DATE = re.compile(r"\b(january|february|march|april|may|june|july|august|september|october|november|december|monday|tuesday|wednesday|thursday|friday|saturday|sunday|\d{1,2}(st|nd|rd|th)|20\d\d|19\d\d)\b", re.I)
TIME = re.compile(r"\b(\d{1,2}(:\d\d)?\s?(am|pm|a\.m\.|p\.m\.)|o'?clock|morning|afternoon|evening|night|midnight|noon)\b", re.I)
NUM = re.compile(r"\b(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|thirty|forty|fifty|hundred|thousand|percent)\b", re.I)
DOCREF = re.compile(r"\b(email|emails|text|message|form|document|tab|paragraph|letter|lease|record|footage|screenshot|roster|payslip|order|direction)\b", re.I)
MEMHEDGE = re.compile(r"\b(i don'?t (recall|remember|know)|i can'?t (recall|remember)|not sure|i think|i believe|i'?m not certain|from memory|if i remember)\b", re.I)
REPAIR = re.compile(r"(\bsorry\b|\bi mean\b|\bactually\b|\bor rather\b|\bno,? (it|i|that) (was|is|wasn'?t)\b|\blet me rephrase\b)", re.I)
ADDRESS = re.compile(r"\b(commissioner|your honou?r|sir|officer|constable|mate)\b", re.I)
CLARIFY = re.compile(r"\b(sorry\?|pardon|can you repeat|do you mean|what do you mean|say that again|could you clarify|you'?re asking)\b", re.I)
ACK = re.compile(r"^\s*(yes|yeah|yep|no|okay|ok|right|understood|correct|that'?s correct|sure|absolutely)\b", re.I)
PROC = re.compile(r"\b(direction|order|rule|form \d+|form|disclosure|hearing|conference|mention|regulator|statement of facts|affidavit|evidence|charge|bail|court|magistrate|lease|tenancy)\b", re.I)
def wc(t): return len(re.findall(r"[A-Za-z0-9']+", t))
def z(xs):
    xs=np.array(xs,float); return (xs-xs.mean())/(xs.std() or 1)
def analyse(segs, me):
    out={}
    base=[s for s in segs if s['spk']==me and s.get('pros') and s['pros'].get('f0_med') and 70<s['pros']['f0_med']<260 and s['pros'].get('voiced_frac',0)>=0.35 and s['end']-s['start']>=0.8]
    f0b=np.median([s['pros']['f0_med'] for s in base]) if base else None
    dbb=np.median([s['pros']['db_mean'] for s in base]) if base else None
    # turns
    turns=[]; cur=None
    for s in segs:
        if s['spk'] is None: continue
        if cur and s['spk']==cur['spk'] and s['start']-cur['end']<2.0:
            cur['segs'].append(s); cur['end']=s['end']; cur['text']+=' '+s['text']
        else:
            cur={'spk':s['spk'],'start':s['start'],'end':s['end'],'segs':[s],'text':s['text']}; turns.append(cur)
    # A. response timing
    R=[]
    for a,b in zip(turns,turns[1:]):
        if b['spk']==me and a['spk']!=me:
            prompt=a['text'].strip(); last=re.split(r'(?<=[.?!])\s+',prompt)[-1] if prompt else ''
            kind='yes/no Q' if ('?' in last and YN.search(last)) else ('open Q' if ('?' in last or WH.search(last) and '?' in prompt[-60:]) else 'statement')
            lat=b['start']-a['end']
            ans=b['text'].strip()
            R.append({'t':round(b['start'],1),'lat':round(lat,2),'kind':kind,'recallQ':bool(RECALLQ.search(last)),
                      'challenge':bool(CHALLENGE.search(prompt[-160:])),'prompt_words':wc(prompt),'ans_words':wc(ans),
                      'direct':bool(ACK.search(ans)) if kind=='yes/no Q' else None,'prompt':last[-140:],'answer':ans[:160]})
    def summ(rows):
        L=[r['lat'] for r in rows]
        if not L: return None
        return {'n':len(L),'median_s':round(st.median(L),2),'p25':round(float(np.percentile(L,25)),2),'p75':round(float(np.percentile(L,75)),2),
                'overlap_pct':round(100*sum(x<0 for x in L)/len(L),1),'latched_lt0.3_pct':round(100*sum(0<=x<0.3 for x in L)/len(L),1),
                'long_gt2s_pct':round(100*sum(x>2 for x in L)/len(L),1),'median_answer_words':st.median([r['ans_words'] for r in rows])}
    out['A_response_timing']={'all':summ(R),'yes_no_Q':summ([r for r in R if r['kind']=='yes/no Q']),
        'open_Q':summ([r for r in R if r['kind']=='open Q']),'after_statement':summ([r for r in R if r['kind']=='statement']),
        'recall_Q':summ([r for r in R if r['recallQ']]),'after_challenge':summ([r for r in R if r['challenge']])}
    yn=[r for r in R if r['kind']=='yes/no Q']
    out['A_response_timing']['yes_no_direct_start_pct']=round(100*sum(1 for r in yn if r['direct'])/max(1,len(yn)),1)
    # time course: quartiles
    if R:
        T0,T1=segs[0]['start'],segs[-1]['end']; q=[[] for _ in range(4)]
        for r in R: q[min(3,int(4*(r['t']-T0)/(T1-T0)))].append(r['lat'])
        out['A_latency_by_quarter_median_s']=[round(st.median(x),2) if x else None for x in q]
    # latency vs prompt length correlation
    if len(R)>5:
        out['A_corr_latency_vs_prompt_words']=round(float(np.corrcoef([r['lat'] for r in R],[r['prompt_words'] for r in R])[0,1]),2)
    # B. situational awareness
    mytext=' '.join(t['text'] for t in turns if t['spk']==me); n=max(1,wc(mytext))
    p100=lambda rx: round(100*len(rx.findall(mytext))/n,2)
    # interruptions received: other speaker starts <0.3s after my seg end and my turn text lacks terminal punctuation
    intr=0; resumed=0
    for i,(a,b) in enumerate(zip(turns,turns[1:])):
        if a['spk']==me and b['spk']!=me and b['start']-a['end']<0.3 and not a['text'].rstrip().endswith(('.','?','!')):
            intr+=1
            nxt=next((t for t in turns[i+2:] if t['spk']==me),None)
            if nxt: resumed+=1
    out['B_situational']={'my_turns':sum(1 for t in turns if t['spk']==me),'words':n,
        'address_forms_per100':p100(ADDRESS),'clarification_requests_per100':p100(CLARIFY),
        'procedural_refs_per100':p100(PROC),'acknowledgement_openers_pct':round(100*sum(1 for r in R if ACK.search(r['answer']))/max(1,len(R)),1),
        'interrupted_mid_turn':intr,'overlapping_starts':sum(1 for r in R if r['lat']<0)}
    # C. arousal
    C={}
    if f0b:
        rows=[]
        for s in segs:
            if s['spk']!=me or not s.get('pros') or not s['pros'].get('f0_med') or s['end']-s['start']<0.8: continue
            p=s['pros']
            if not(70<p['f0_med']<260) or p.get('voiced_frac',0)<0.35: continue
            rows.append({'t':s['start'],'st':12*math.log2(p['f0_med']/f0b),'db':p['db_mean']-dbb,'wps':p.get('wps',0),'f0sd':p.get('f0_sd_st',0),'text':s['text'][:120]})
        if rows:
            ar=z([r['st'] for r in rows])+z([r['db'] for r in rows])
            for r,a in zip(rows,ar): r['arousal']=round(float(a),2)
            C['baseline_f0_hz']=round(float(f0b),1); C['n_segments']=len(rows)
            T0,T1=segs[0]['start'],segs[-1]['end']; q=[[] for _ in range(4)]
            for r in rows: q[min(3,int(4*(r['t']-T0)/(T1-T0)))].append(r)
            C['by_quarter']=[{'pitch_st':round(st.median([r['st'] for r in x]),2),'db':round(st.median([r['db'] for r in x]),2),'wps':round(st.median([r['wps'] for r in x]),2)} if x else None for x in q]
            top=sorted(rows,key=lambda r:-r['arousal'])[:8]
            C['peak_segments']=[{'t':f"{int(r['t']//60)}:{int(r['t']%60):02d}",'pitch_st':round(r['st'],1),'db':round(r['db'],1),'wps':r['wps'],'text':r['text']} for r in top]
            # arousal after challenge vs other
            chal_t=[r['t'] for r in R if r['challenge']]
            near=[r['arousal'] for r in rows if any(0<=r['t']-c<20 for c in chal_t)]
            far=[r['arousal'] for r in rows if not any(0<=r['t']-c<20 for c in chal_t)]
            C['arousal_within20s_after_challenge_median']=round(st.median(near),2) if near else None
            C['arousal_other_median']=round(st.median(far),2) if far else None
            # speech under arousal: disfluency in top vs bottom tercile
            srt=sorted(rows,key=lambda r:r['arousal']); k=max(1,len(srt)//3)
            def disf(x):
                tx=' '.join(r['text'] for r in x); w=max(1,wc(tx))
                return round(100*(len(re.findall(r"\b(um|uh|er|erm)\b",tx,re.I))+len(REPAIR.findall(tx)))/w,2)
            C['disfluency_per100_low_vs_high_arousal']=[disf(srt[:k]),disf(srt[-k:])]
            C['rate_wps_low_vs_high_arousal']=[round(st.median([r['wps'] for r in srt[:k]]),2),round(st.median([r['wps'] for r in srt[-k:]]),2)]
    out['C_arousal']=C
    # D. recall
    out['D_recall']={'dates_per100':p100(DATE),'times_per100':p100(TIME),'numbers_per100':p100(NUM),'document_refs_per100':p100(DOCREF),
        'memory_hedges_per100':p100(MEMHEDGE),'self_repairs_per100':p100(REPAIR),
        'memory_hedge_examples':[m.group(0) for m in MEMHEDGE.finditer(mytext)][:12]}
    rq=[r for r in R if r['recallQ']]
    out['D_recall_questions']=[{'t':f"{int(r['t']//60)}:{int(r['t']%60):02d}",'lat':r['lat'],'q':r['prompt'],'a':r['answer']} for r in rq][:25]
    out['A_slowest']=[{'t':f"{int(r['t']//60)}:{int(r['t']%60):02d}",'lat':r['lat'],'q':r['prompt'],'a':r['answer'][:100]} for r in sorted(R,key=lambda r:-r['lat'])[:6]]
    return out
if __name__=='__main__':
    segs=json.load(open(sys.argv[1])); me=sys.argv[2]
    print(json.dumps(analyse(segs,me),indent=1,default=str))
