import numpy as np, wave, io, av
from faster_whisper.audio import decode_audio
from piper import PiperVoice

SR = 22050
START, END = 1757.00, 1922.90            # 29:17.0 -> 32:02.9

# ---- 1. the clip, resampled to 22050 to match the TTS voice ----
src = decode_audio("mention.mp3", sampling_rate=SR)
clip = src[int(START*SR):int(END*SR)].astype(np.float32)
peak = np.abs(clip).max()
clip = clip / peak * 0.89
print(f"clip {len(clip)/SR:.1f}s  ({START/60:.0f}:{START%60:04.1f} -> {END/60:.0f}:{END%60:04.1f})")

# ---- 2. the explainer ----
TEXT = """
This is an extract from the mention of the seventh of August, twenty twenty six,
in the Queensland Industrial Relations Commission. Matter W C 2024 227, Shepherd
versus the Workers Compensation Regulator. It runs from twenty nine minutes and
seventeen seconds, to thirty two minutes and two seconds.

In the first fifty words, the appellant describes the mechanism of his first
pleaded stressor. Calls directed to a number that is an emergency contact. And
emergency responders not reaching a patient having a cardiac arrest, or a patient
in respiratory distress.

Acoustic analysis of that passage records the following. The delivery carries one
pitch rise, of three semitones, and it falls on the words, direct calls to this
number. That is the mechanism, not the consequence. On the words, cardiac arrest,
the speaker's pitch is the lowest of the entire turn, below his own median, while
his volume is at his ninetieth percentile, the loudest of the turn. Pitch falling
while volume rises is a dissociation. Arousal raises both together. There is no
adjective anywhere in the passage, and no characterisation of any person.

What follows is five point seven four seconds of silence. That is ten and a half
times the Commissioner's median response time to this speaker, measured across
seventy six handovers. It is the longest gap in the hearing that does not contain
a document being read.

The Commissioner then re enters at his ninth percentile for volume. He reaches
the loudest utterance of the entire hearing on the words, I am going to schedule
this disclosure dispute for a hearing. He states that the health service will
need to call evidence to support its objections, that he sees a very
comprehensive objection, that the parties have work to do at the bar table, and
that a hearing will carry cost consequences.

This is machine analysis. It is unverified, and it is offered for verification.
It is not a legal determination.
"""

voice = PiperVoice.load("voices/en_GB-alba-medium.onnx")
buf = io.BytesIO()
with wave.open(buf, "wb") as w:
    voice.synthesize_wav(" ".join(TEXT.split()), w)
buf.seek(0)
with wave.open(buf) as w:
    tts = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(np.float32)/32768
    assert w.getframerate() == SR, w.getframerate()
tts = tts/np.abs(tts).max()*0.89
print(f"tts  {len(tts)/SR:.1f}s")

# ---- 3. assemble: clip | 2.0s gap | explainer ----
gap = np.zeros(int(2.0*SR), np.float32)
out = np.concatenate([clip, gap, tts])
print(f"total {len(out)/SR:.1f}s")

# ---- 4. encode mp3 via PyAV ----
path = "/home/user/Personalproject/qps_interview_acoustic/MENTION_29m17_to_32m02_patient_safety_to_costs.mp3"
cont = av.open(path, "w")
st = cont.add_stream("mp3", rate=SR)
st.bit_rate = 128000
frame_size = 1152
pcm = (out*32767).astype(np.int16)
for i in range(0, len(pcm), frame_size):
    chunk = pcm[i:i+frame_size]
    if len(chunk) < frame_size:
        chunk = np.pad(chunk, (0, frame_size-len(chunk)))
    f = av.AudioFrame.from_ndarray(chunk.reshape(1,-1), format="s16", layout="mono")
    f.sample_rate = SR
    f.pts = i
    for p in st.encode(f): cont.mux(p)
for p in st.encode(None): cont.mux(p)
cont.close()
import os
print(f"WROTE {path}  {os.path.getsize(path)/1e6:.2f} MB")
