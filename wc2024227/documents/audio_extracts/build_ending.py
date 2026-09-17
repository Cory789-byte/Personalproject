import numpy as np, av, os
from faster_whisper.audio import decode_audio
SR = 22050
START, END = 3482.00, 3874.48      # 58:02.0 -> 64:34.5 (end of recording)
src = decode_audio("mention.mp3", sampling_rate=SR)
clip = src[int(START*SR):int(END*SR)].astype(np.float32)
clip = clip/np.abs(clip).max()*0.89
print(f"clip {len(clip)/SR:.1f}s = {int(len(clip)/SR//60)}m {len(clip)/SR%60:04.1f}s"
      f"   ({int(START//60)}:{START%60:05.2f} -> {int(END//60)}:{END%60:05.2f})")
path="/home/user/Personalproject/wc2024227/documents/audio_extracts/MENTION_58m02_to_END_materiality_to_close.mp3"
cont=av.open(path,"w"); st=cont.add_stream("mp3",rate=SR); st.bit_rate=128000
pcm=(clip*32767).astype(np.int16); F=1152
for i in range(0,len(pcm),F):
    c=pcm[i:i+F]
    if len(c)<F: c=np.pad(c,(0,F-len(c)))
    fr=av.AudioFrame.from_ndarray(c.reshape(1,-1),format="s16",layout="mono")
    fr.sample_rate=SR; fr.pts=i
    for p in st.encode(fr): cont.mux(p)
for p in st.encode(None): cont.mux(p)
cont.close()
print(f"WROTE {os.path.basename(path)}  {os.path.getsize(path)/1e6:.2f} MB")
a=decode_audio(path,sampling_rate=SR); print(f"VERIFY decodes {len(a)/SR:.1f}s  peak {np.abs(a).max():.3f}")
