"""Speech/cognitive-linguistic metrics per speaker from word-timed transcripts.
Input: list of dicts {w, s, e(optional), spk, fill(optional)} in time order."""
import re, statistics as st, collections
FILL = {'um','uh','er','ah','erm','mm','hmm','uhm'}
SUB = {'because','if','although','though','unless','whereas','since','when','whether','which','that','who','while','until','so that'}
COORD = {'and','but','so','or','then'}
HEDGE = ['i think','sort of','kind of','maybe','probably','i guess','i believe','i suppose','perhaps','i don\'t know','not sure']
CERT = ['definitely','clearly','obviously','certainly','absolutely','exactly','always','never']
META = ['what i mean','i mean','in other words','to be clear','the point is','basically','essentially','which is']
def norm(w): return re.sub(r"[^a-z']", '', w.lower())
def mattr(tokens, win=50):
    if len(tokens) < win: return len(set(tokens))/max(1,len(tokens))
    return st.mean(len(set(tokens[i:i+win]))/win for i in range(len(tokens)-win+1))
def turns(words):
    out=[]; cur=None
    for w in words:
        if cur and w['spk']==cur['spk']: cur['w'].append(w)
        else:
            cur={'spk':w['spk'],'w':[w]}; out.append(cur)
    return out
def metrics(words, who, gap_pause=0.5):
    for i,w in enumerate(words):
        if w.get('e') is None: w['e']=min(words[i+1]['s'], w['s']+0.6) if i+1<len(words) else w['s']+0.3
    T=turns(words); mine=[t for t in T if t['spk']==who]
    toks=[norm(w['w']) for t in mine for w in t['w']]; toks=[x for x in toks if x]
    fills=sum(1 for t in mine for w in t['w'] if w.get('fill') or norm(w['w']) in FILL)
    content=[x for x in toks if x not in FILL]
    n=len(content); text=' '.join(content)
    # pauses and runs within own turns
    pauses=[]; runs=[]; spk_time=0; art_time=0
    for t in mine:
        ws=t['w']; run=1
        spk_time += ws[-1]['e']-ws[0]['s']
        for a,b in zip(ws,ws[1:]):
            g=b['s']-a['e']
            if g>=gap_pause: pauses.append(g); runs.append(run); run=1
            else: run+=1
        runs.append(run)
        art_time += sum(w['e']-w['s'] for w in ws)
    # latency: gap from previous other-speaker turn end to this turn start
    lat=[]
    for a,b in zip(T,T[1:]):
        if b['spk']==who and a['spk']!=who: lat.append(max(0,b['w'][0]['s']-a['w'][-1]['e']))
    reps=sum(1 for a,b in zip(content,content[1:]) if a==b and a not in ('that','had'))
    cnt=lambda L: sum(len(re.findall(r'\b'+re.escape(p)+r'\b',text)) for p in L)
    per100=lambda x: round(100*x/max(1,n),2)
    tl=[len(t['w']) for t in mine]
    return {
      'turns':len(mine),'words':n,'speaking_time_s':round(spk_time,1),
      'turn_words_median':st.median(tl) if tl else 0,'turn_words_max':max(tl) if tl else 0,
      'speech_rate_wpm':round(60*n/max(1,spk_time),1),
      'articulation_rate_wps_est':round(n/max(1,art_time),2),
      'pauses_per_100w':per100(len(pauses)),'pause_median_s':round(st.median(pauses),2) if pauses else 0,
      'run_length_median_words':st.median(runs) if runs else 0,'run_length_mean_words':round(st.mean(runs),1) if runs else 0,
      'fillers_per_100w':per100(fills),'immediate_repeats_per_100w':per100(reps),
      'MATTR50':round(mattr(content),3),
      'subordinators_per_100w':per100(sum(1 for x in content if x in SUB)),
      'coordinators_per_100w':per100(sum(1 for x in content if x in COORD)),
      'sub_to_coord_ratio':round(sum(1 for x in content if x in SUB)/max(1,sum(1 for x in content if x in COORD)),2),
      'hedges_per_100w':per100(cnt(HEDGE)),'certainty_per_100w':per100(cnt(CERT)),
      'meta_markers_per_100w':per100(cnt(META)),
      'I_per_100w':per100(content.count('i')),'we_per_100w':per100(content.count('we')),
      'negations_per_100w':per100(sum(1 for x in content if x in ('not',"don't","didn't","wasn't","isn't","can't","no","never","couldn't","won't"))),
      'response_latency_median_s':round(st.median(lat),2) if lat else None,
      'latched_responses_pct':round(100*sum(1 for x in lat if x<0.3)/max(1,len(lat)),1),
    }
