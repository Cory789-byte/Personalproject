"""Whole-file acoustic overview: per-second intensity and f0, long silences.

Usage: python -I overview_court.py AUDIO OUT.json
"""
import json, sys
import numpy as np
import parselmouth
from faster_whisper.audio import decode_audio

audio, out = sys.argv[1], sys.argv[2]
SR = 16000
wav = decode_audio(audio, sampling_rate=SR).astype(np.float64)
snd = parselmouth.Sound(wav, sampling_frequency=SR)
inten = snd.to_intensity(minimum_pitch=60, time_step=0.05)
pitch = snd.to_pitch(time_step=0.05, pitch_floor=60, pitch_ceiling=500)
it = inten.xs(); iv = inten.values[0]
pt = pitch.xs(); pv = pitch.selected_array["frequency"]
dur = len(wav) / SR
secs = []
for t in range(int(dur)):
    m = (it >= t) & (it < t + 1)
    pm = (pt >= t) & (pt < t + 1)
    v = pv[pm]; v = v[v > 0]
    secs.append({"t": t, "db": round(float(np.nanmean(iv[m])), 1) if m.any() else None,
                 "f0": round(float(np.median(v)), 1) if v.size else None})
dbs = np.array([s["db"] for s in secs if s["db"] is not None])
floor = float(np.percentile(dbs, 10))
# silence = seconds within 6 dB of the floor; report runs >= 4 s
sil, run = [], None
for s in secs:
    quiet = s["db"] is not None and s["db"] < floor + 6
    if quiet and run is None:
        run = s["t"]
    if not quiet and run is not None:
        if s["t"] - run >= 4:
            sil.append([run, s["t"]])
        run = None
if run is not None and int(dur) - run >= 4:
    sil.append([run, int(dur)])
json.dump({"duration": round(dur, 1), "noise_floor_db_p10": round(floor, 1),
           "db_p50": round(float(np.percentile(dbs, 50)), 1),
           "db_p90": round(float(np.percentile(dbs, 90)), 1),
           "long_quiet_runs_s": sil, "per_second": secs}, open(out, "w"))
print("duration", round(dur, 1), "floor", round(floor, 1), "p50", round(float(np.percentile(dbs, 50)), 1),
      "p90", round(float(np.percentile(dbs, 90)), 1))
print("quiet runs >=4s:", sil)
