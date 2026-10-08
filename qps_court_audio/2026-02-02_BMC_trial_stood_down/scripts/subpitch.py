"""Median f0 / mean dB for word ranges inside segments, to check splits.

Usage: python -I subpitch.py AUDIO PROSODY.jsonl "seg:a-b,seg:a-b,..."
"""
import json, sys
import numpy as np
import parselmouth
from faster_whisper.audio import decode_audio

audio, segp, spec = sys.argv[1], sys.argv[2], sys.argv[3]
SR = 16000
wav = decode_audio(audio, sampling_rate=SR).astype(np.float64)
segs = [json.loads(l) for l in open(segp, encoding="utf-8")]
for item in spec.split(","):
    si, rng = item.split(":")
    a, b = (int(x) for x in rng.split("-"))
    w = segs[int(si)]["words"][a:b + 1]
    t0, t1 = w[0]["s"], w[-1]["e"]
    if t1 - t0 < 0.12:
        t1 = t0 + 0.12
    snd = parselmouth.Sound(wav[int(t0 * SR):int(t1 * SR)], sampling_frequency=SR)
    f = snd.to_pitch(time_step=0.01, pitch_floor=60, pitch_ceiling=500).selected_array["frequency"]
    f = f[f > 0]
    iv = snd.to_intensity(minimum_pitch=60, time_step=0.01).values[0]
    iv = iv[np.isfinite(iv)]
    txt = " ".join(x["w"].strip() for x in w)
    print(f"{si}:{a}-{b} [{t0:.2f}-{t1:.2f}] f0={np.median(f) if f.size else 0:.0f} "
          f"db={iv.mean() if iv.size else 0:.1f} | {txt}")
