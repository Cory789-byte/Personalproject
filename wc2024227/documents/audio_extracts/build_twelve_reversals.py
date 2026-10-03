import numpy as np, subprocess, av
sr=16000
x=np.load('mention16k.npy').astype(np.float32)
def clip(a,b): return x[int(a*sr):int(b*sr)].copy()
def gain(seg,db): return seg*(10**(db/20))
def tts(text,fn='seq/_n.wav'):
    subprocess.run(['piper','--model','voices/en_GB-alba-medium.onnx','--output_file',fn,'--length_scale','1.05'],input=text.encode(),check=True,capture_output=True)
    c=av.open(fn); s=c.streams.audio[0]; res=av.AudioResampler(format='fltp',layout='mono',rate=sr); out=[]
    for fr in c.decode(s):
        for r in res.resample(fr): out.append(r.to_ndarray()[0])
    return np.concatenate(out).astype(np.float32)
def write_mp3(y,fn):
    y=np.clip(y,-0.99,0.99); c=av.open(fn,'w'); st=c.add_stream('mp3',rate=sr); st.layout='mono'
    fr=av.AudioFrame.from_ndarray(y[np.newaxis,:].astype(np.float32),format='fltp',layout='mono'); fr.sample_rate=sr
    for p in st.encode(fr): c.mux(p)
    for p in st.encode(None): c.mux(p)
    c.close()
sil=lambda s: np.zeros(int(s*sr),np.float32)
parts=[]
N=lambda t: parts.extend([tts(t),sil(0.7)])
A=lambda a,b,db=6: parts.extend([gain(clip(a,b),db),sil(0.7)])

N("The twelve reversals. The mention of the seventh of August 2026, before Industrial Commissioner Dwyer. This explainer lists every occasion the Commissioner reversed himself, plays what he said first and what he said after, explains why each reversal happened, and closes with why it felt the way it did, and with the coat. Every clip is the original recording.")

N("Reversal one. Authorship. At nine oh two he said this about the appellant's papers.")
A(567.53,583.74)
N("Fifty minutes later, the same papers, the same author: acting for yourself, in no way at all being critical. And after twenty-nine seventeen the word A I never appears again. Why he reversed: at twenty-five fifty-four the appellant recited sub-item numbers against the bench's own recollection, and at twenty-four forty-six gave the mechanism of his application before the bench had reached it. Nobody who did not write the instrument carries it like that. What it did: every document in the file was re-priced as the appellant's own work.")

N("Reversal two. The case itself. At twenty-seven thirty-two he closed the subject.")
A(1652.81,1658.4)
N("At fifty-six thirty-four he opened it himself, unprompted: systemically, the place in which you worked had a number of failings, non-compliance with proper protocol, procedure, legislation, and you may be right about all of that. Why: the sixty-five words at twenty-nine seventeen. A judge cannot un-hear. He carried it for half an hour and it came out as his own conclusion. What it did: put a merits impression, in the appellant's favour, on a mention transcript.")

N("Reversal three. The non-party. At eighteen thirty-three, the health service was to be protected.")
A(1113.37,1127.82)
N("At thirty twenty: the health service is going to need to call evidence to talk to their objections. Why: between the two sentences sat the misroute, described by the operator who handled it. An imposition on a bystander became an obligation on an organisation whose objection now needed proving. What it did: put the health service on notice, with its own lawyer in the room.")

N("Reversal four. The fishing net. At forty-nine fifty-three:")
A(3008.77,3014.56)
N("At sixty-two thirty-eight, the same request:")
A(3748.33,3758.4)
N("Why: the walk that was designed to show the net was empty kept finding fish. What it did: named the one live issue and predicted production. The two hundred and ninety-eight admissions a month later are that prediction landing.")

N("Reversal five. The direction of concern. At twenty-nine forty-five it was aimed at the appellant, by name.")
A(1792.69,1795.94)
N("Seventy seconds later it had a new address.")
A(1857.31,1861.08)
N("Why: at thirty twelve the appellant said, I actually understand what you're getting at. The resistance the concern assumed was not there, so the concern moved to the only side of the table where work remained. What it did: relocated fault from the appellant to the represented parties, and it never moved back.")

N("Reversal six. Move on. At twenty-nine forty-five he announced he was moving on. He then spent two and a half more minutes on the same subject, returned to it at thirty-two eleven, at sixty, at sixty-one thirty-nine, and closed the morning with it at sixty-three fifteen. Why: announcing the move was a defence of the script, and the subject would not stay closed because its premise was gone. What it did: showed on the transcript that the disclosure question had become the case.")

N("Reversal seven. The hearing. He built it as a deterrent, and ended the same breath by handing it over.")
A(1915.47,1923.44)
N("And twice more, unprompted, at fifty-nine eleven:")
A(3565.39,3570.2)
N("Why: a deterrent only works on someone who must be deterred, and the appellant had agreed. What it did: made the hearing the appellant's standing election, which it remains.")

N("Reversal eight and nine. The agenda, and the dead point. He opened the morning with a speech reserving the agenda to the bench. At fifty-three oh two he pressed an item in the challenging register, probably, or is, and the appellant told him gently that the item was already withdrawn. Listen to the whole repair: the softeners, the shared we, and the rule change.")
A(3203.09,3223.88)
N("Why: the appellant's corrections had outperformed the bench's agenda twice in one minute, so the efficient course was to delegate the map. What it did: rewrote the constitution of the room. The person the opening speech was aimed at became co-editor of the agenda.")

N("Reversal ten. The self-caught one. Twenty seconds after making the rule, he applied it to his own script, mid-sentence, with no input from the appellant at all.")
A(3244.75,3252.73)
N("Why: the update had internalised. What it did: proved the reversal was running without supervision.")

N("Reversal eleven. The fastest. One turn, one hundred and ninety-seven words, six filled pauses, twelve hedges. It begins in the old frame, floundering, and ends in the new one. Listen to a man cross from one belief to the other inside a single breath.")
A(3397.45,3467.18)
N("Why: the closing script required a fault in the appellant, and the updated model would not supply one. What it did: retracted the morning's last criticism before the sentence containing it had cooled.")

N("Reversal twelve. The scale of decision. At thirty-one twelve:")
A(1881.41,1889.71)
N("At sixty minutes, the same judge, the same question:")
A(3629.11,3636.46)
N("Why: the impossible-on-the-papers question was the old, wide model of the application. Once the ask had shrunk to identified documents, the same judge could decide it in minutes. The ask never changed. His model of it did. What it did: built the single-document express lane the appellant's next request now drives on.")

N("Why each one felt uncomfortable. The research measured it directly. Elliot and Devine showed dissonance is a felt state: arousal, an unease that something just said is wrong, relieved only when the words are brought into line with the belief. Every reversal you heard is one cycle of that arousal and relief, and the audio holds the trace of each: the softeners, the falling pitch at the resolution, the filled pauses spiking while the collision is live. Levelt's monitor explains the mid-sentence catches: a speaker audits his own output and repairs it before he can say why. Ross, Lepper and Hubbard explain why it took twelve times rather than once: a discredited belief is re-triggered by its old cues, and his script was made of those cues, so every return to the script summoned the old frame again. Higgins showed that saying becomes believing, so each softened restatement moved him further from the frame. Bem and the generation effect explain why the end state held: the final positions came out of his own mouth, built from the appellant's facts, so they were his. And Cialdini explains why he could never go back: each reversal was public, witnessed by five professionals, and reversing a witnessed reversal costs more than any bench will pay.")

N("The coat. Picture a man who has worn the same coat to work for twenty years. A good coat, cut for the weather he usually meets: the overcooked file, the grievance dressed as a claim, the litigant whose perception has left the record. On the seventh of August he buttoned it at the door, and the speech about efficiency was the buttoning. Then the weather turned out to be different. You do not notice a twenty-year coat until it is wrong for the room. At eighteen thirty-three a sleeve caught. At twenty-nine thirty-nine he stood in five point seven four seconds of silence and felt the weight of it. At twenty-nine forty-five he pulled it tighter, which is what people do first: the cost speech is a man insisting the coat is fine. At thirty-two oh two he unbuttoned it. At fifty-three thirty-one he took it off and apologised for the delay. At fifty-three fifty-two he reached for it out of habit, felt the wrongness before his hand closed, and stopped himself: sorry, I'll recall that. At fifty-six thirty-four he picked it up one last time, got one arm in, floundering, and took it off mid-gesture: you may be right about all of that. Nobody throws away a twenty-year coat once. They put it down, and habit hands it back, and they put it down again, faster each time. Twelve reaches. Twelve refusals. The first took a hundred and thirty-seven seconds of cost speech. The last took half a sentence. And he did not lose the coat, and nobody took it from him. He looked at the actual weather, twelve separate times, and chose to be dressed for the room he was really in. By the end of the morning the coat was over the back of his chair, and the last words were spoken in shirtsleeves.")
A(3850.43,3853.74)
y=np.concatenate(parts)
write_mp3(y,'seq/EXPLAINER_the_twelve_reversals.mp3')
print("seconds",round(len(y)/sr,1))
