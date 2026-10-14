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

N("Shepherd and the Workers' Compensation Regulator. The mention of the seventh of August 2026, before Industrial Commissioner Dwyer. This explainer covers two things the record shows and one thing it explains. The shift from you to we. The interruption licence. And why the bench did what it did with the health service. Every clip is the original recording.")

N("Part one. The pronoun. In the first twenty-nine minutes the Commissioner used a we-form about six times in every thousand words, and it meant the Commission. In the last eleven minutes the rate was fourteen per thousand, more than double, and every one of them had the appellant inside it. Here is the adversarial we, at twenty-nine fifty-eight. If we can't work this out. If we can't reach some understanding. Joint failure, used to load the outcome onto the appellant.")
A(1812.83,1824.16)
N("Here is the navigating we, at fifty-three forty-eight and fifty-five oh four. Are we still dealing with this one. Are we going into that. That is a chair asking a co-chair.")
A(3230.15,3255.46)
A(3304.19,3306.74)
N("And here is the closing we, at sixty-three oh nine. In all of what we've been through. If you decide you want to press it, we'll get down to the serious business. The verb is the appellant's. The consequence is joint. It is the same grammar as you can have it, half an hour later, with the pressure gone.")
A(3789.35,3853.74)

N("Part two. The licence. At fifty-three oh two the Commissioner was pressing a point in the challenging register. Probably, or is. Disclosure is about what you know. The point had already been withdrawn. The appellant told him so, with cover. I think I actually said. Then three softeners at minus two decibels. Then the we that shares the fault. Then a rule change delivered loud and fast, plus three point eight decibels, five and a half words a second. I'll leave it up to you to tell me. Then the pitch falls through don't worry about interrupting me. Descending pitch is closure. The thing was settled before the sentence ended.")
A(3203.09,3230.3)
N("Twenty seconds later he applied the rule to himself. Sorry, I'll recall that. That's all I need to know. From that point his voice ran at its quietest average of the hour and his highest rate of filled pauses. That is a person composing, not delivering. He had stopped running a plan.")

N("Part three. The two minds. The Commissioner runs on a prepared script and a strong prior. The script was the opening speech about interlocutory disputes. The prior was set at nine oh two: papers too good to be the person's, so a grievance dressed as a documents fight. He tests a prior by playing the case aloud and watching what the litigant does with it. He changes his mind on content, not on tone, and he holds a conclusion only when he has generated it himself. At twenty-nine forty-five, with the premise gone, he defended: a prepared speech at four fillers per thousand words. At fifty-three thirty-one, with the premise gone again, he repaired: softeners, a shared we, and an apology. A threatened authority doubles down. A secure one apologises and delegates. He crossed from the first to the second inside this mention.")
N("The appellant held one model across the whole hour and released it once, in fifty words, when the record was about to close on the wrong conclusion. His turn latency was a third of a second, independent of how long the bench had spoken, so he was always ready and mostly chose silence. His filled-pause rate was half the bench's. His construction was event after event with no argument in it, the register of a witness, not an advocate. And his two interventions after the fifty words were acknowledgements of the bench, not restatements of himself. Yeah, I actually understand what you're getting at. I understand where you're getting at, I can meet most of the way. Each was followed within seconds by the bench pointing away from him. He never talked over the Commissioner. He spoke into pauses. The licence at fifty-three forty-one authorised the one thing he had never done.")

N("Part four. The health service. Metro South Health is not a party. On the twenty-second of May it did not attend the mention. The Commissioner noted the absence and directed its objections by four p m on the fifth of June. What came back was signed by the Chief Executive of the Hospital and Health Service, with the Principal Lawyer, Ms Ruttan, named as the contact. The letter says the emergency paging records were not retained. That a spreadsheet of recorded MET calls exists for the seventeenth and eighteenth of March 2024. That switchboard complaints go to one line manager and are handled by email or verbally. That there were no consequential changes to procedure. That no fatigue assessment existed until after the thirtieth of June 2024. That the communication book's destruction was already conceded. Under the Chief Executive's hand, each of those is a control that was not there.")
N("On the twenty-third of June the appellant filed his rule 64G application. It asked for one order: produce, or swear. Where the health service said a record did not exist, its Chief Executive or a delegated Director was to say so on oath, after a defined search by a named person, and to explain what the MET-call spreadsheet is and who holds it. The notice of listing of the fifteenth of June required Ms Ruttan to attend on the seventh of August. So the Commissioner had, on his desk, a non-party that had missed a mention, a letter from the head of that organisation conceding the absence of its controls, and an application to put the head of that organisation on oath about emergency-code records in a hospital.")
N("He had read it. At thirty-two forty-three: your response to the objection, and your application as well.")
A(2000.51,2010.96)
N("Here is what he did with it. At eighteen thirty-three he called a non-party order quite an imposition, because the health service is not a party, and sent the appellant to the Regulator first.")
A(1113.37,1141.68)
N("At twenty-seven thirty-two, the moment the subject touched patient safety, he closed it.")
A(1649.97,1658.4)
N("Then the appellant answered anyway. Fifty words. Doctors called for an emergency sent to the wrong side of the room. Not to someone in cardiac arrest. Not to someone in respiratory distress. Then five point seven four seconds of silence that nobody at the table filled.")
A(1757.21,1786.5)
N("And at thirty twenty, having heard it, he named the consequence for the health service on the record. The health service is going to need to call evidence to talk to their objections. At thirty thirty-six, a very comprehensive objection, and work to do down at the bar table. He never read the letter's concessions aloud. He never said the word emergency himself. He never mentioned the verification affidavit. He parked the Form 29 at sixty-one thirty-nine and sent the appellant to Ms Matheson to whittle the list.")
N("Why. Because the Commissioner understood the seriousness before anyone said it. A sworn statement from a Chief Executive that a hospital does not retain its emergency-code paging logs, kept no fatigue assessment, and changed nothing after misroute complaints is not a document about one worker's claim. It is a governance record. Ordering it from the bench in a mention would put the health service into the proceeding as a witness-calling body, with Crown Law, at cost, in a matter he had opened by describing as a documents dispute. He kept the label off the transcript and steered the substance to the consent route: the Regulator, who has access to the health service, producing what it can, with the hearing held in reserve. And he gave the hearing to the appellant anyway. If you want it, you can have it. The person who could have answered for the letter was in the room. Her only words all morning came here.")
A(3691.59,3703.18)
N("The injury. The appellant is a switchboard operator of five years at Logan Hospital whose job was to send emergency notifications to the right team within the timeframe. He reported the hazard in writing on the seventh of August 2023 and the grievance was dismissed the same day. He worked the seventeenth and eighteenth of March 2024 on a seven-hour break. He was certified with a psychiatric injury with a date of injury of the eighteenth of June 2024, and the treating doctors named the same workplace events on the day. He was returned to work without rehabilitation, sent an abandonment notice while certified, and excluded again in 2026, with the employer's own 2026 movement forms and an early-intervention record treating the injury as real two years after its insurer said it was not compensable. Two hundred and ninety-eight of three hundred and three facts are now admitted, most of them from the health service's own documents.")
N("At fifty-six thirty-four the Commissioner said, unprompted, what he had taken from the morning.")
A(3396.59,3455.02)
N("Systemically, the place in which you worked had a number of failings. That is the investigation's conclusion in the bench's own mouth, reached after he had spent twenty-eight minutes steering away from it, and offered while narrowing the paperwork. The paperwork narrowed. The conclusion stayed. And by the close the pronoun for the whole morning was we.")
y=np.concatenate(parts)
write_mp3(y,'seq/EXPLAINER_the_we_shift_and_the_licence.mp3')
print("seconds",round(len(y)/sr,1))
