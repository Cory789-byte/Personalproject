import json
S='/tmp/claude-0/-home-user/6625dff5-a18f-544c-a62c-8ea1e8b9d28c/scratchpad'
lab=[json.loads(l) for l in open(f'{S}/bickery.labelled.jsonl')]
pros={r['id']:r['pros'] for r in (json.loads(l) for l in open(f'{S}/bickery.pros2.jsonl'))}
W=[w for l in open(f'{S}/bickery.words.jsonl') for w in json.loads(l)['words']]
NAME={0:'C0',1:'C1',None:None}
segs=[{'start':r['start'],'end':r['end'],'spk':NAME[r['spk']],'pros':pros.get(r['id'],r['pros']),'words':[]} for r in lab]
import bisect
starts=[s['start'] for s in segs]; un=0
for w in W:
    m=(w['s']+w['e'])/2; i=bisect.bisect_right(starts,m)-1
    if i>=0 and segs[i]['start']<=m<=segs[i]['end']+0.3: segs[i]['words'].append(w)
    else: un+=1
for s in segs: s['text']=''.join(w['w'] for w in s['words']).strip()
out=[s for s in segs if s['text']]
for s in out: s.pop('words')
json.dump(out,open('/home/user/Personalproject/cognitive_speech/interview_segs.json','w'))
print('words',len(W),'unassigned',un,'segs with text',len(out))
