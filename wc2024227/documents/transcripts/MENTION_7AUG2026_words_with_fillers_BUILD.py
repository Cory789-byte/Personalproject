import numpy as np, json, re, time
from faster_whisper import WhisperModel
sr=16000
x=np.load('mention16k.npy').astype(np.float32)
L=[json.loads(l) for l in open('/home/user/Personalproject/wc2024227/documents/transcripts/MENTION_7AUG2026_segments.jsonl')]
def spk(t):
    best=None;bd=9e9
    for r in L:
        if r['start']-0.3<=t<=r['end']+0.3: return r['speaker']
        d=min(abs(r['start']-t),abs(r['end']-t))
        if d<bd: bd=d;best=r['speaker']
    return best if bd<1.5 else 'UNK'
m=WhisperModel('large-v3',device='cpu',compute_type='int8',cpu_threads=4)
FILL=re.compile(r"^(um+|uh+|er+|erm+|ah+|hmm+|mm+)[.,]?$",re.I)
out=[]
t0=time.time()
for k in range(0,65):
    a,b=k*60,min((k+1)*60,len(x)/sr)
    seg=x[int(a*sr):int(b*sr)]
    segs,_=m.transcribe(seg,language='en',beam_size=1,word_timestamps=True,condition_on_previous_text=False,
        initial_prompt="Um, uh, so, um, I think, uh, we should, um, look at that. Uh, yeah.",vad_filter=False)
    for s in segs:
        for w in (s.words or []):
            wd=w.word.strip()
            out.append({'t':round(a+w.start,2),'w':wd,'fill':bool(FILL.match(wd)),'spk':spk(a+w.start)})
    print(k,round(time.time()-t0),flush=True)
json.dump(out,open('seq/words_with_fillers.json','w'))
