"""Run the cognitive_speech measures (speech_metrics.metrics, deep_analysis.analyse) over the
2 Feb 2026 court audio, using the same speaker corrections as build_court.py.

Usage: python -I court_metrics.py AUDIO PROSODY.jsonl DIARDIR PARTS.json BUILD_COURT.py COGDIR OUTDIR
"""
import ast, json, math, sys
from pathlib import Path
import numpy as np
import parselmouth
from faster_whisper.audio import decode_audio

audio, segp, diard, partsp, buildp, cogdir, outd = sys.argv[1:8]
sys.path.insert(0, cogdir)
from speech_metrics import metrics          # noqa: E402
from deep_analysis import analyse           # noqa: E402

# speaker corrections, read from build_court.py without running it
consts = {}
for node in ast.parse(Path(buildp).read_text()).body:
    if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) \
            and node.targets[0].id in ("NAMES", "SPLITS", "WHOLE"):
        consts[node.targets[0].id] = ast.literal_eval(node.value)
NAMES, SPLITS, WHOLE = consts["NAMES"], consts["SPLITS"], consts["WHOLE"]

segs = [json.loads(l) for l in open(segp, encoding="utf-8")]
C = json.load(open(Path(diard) / "clusters.json"))["k3_cmn_kmeans"]
idx = json.load(open(Path(diard) / "embedded_index.json"))
lab = {i: NAMES[c] for i, c in zip(idx, C)}

# 1. word list with speakers
words = []
for i, s in enumerate(segs):
    W = s["words"]
    spk = [None] * len(W)
    if i in SPLITS:
        for a, b, who, _ in SPLITS[i]:
            for k in range(a, b + 1):
                spk[k] = who
    else:
        who = WHOLE[i][0] if i in WHOLE else lab.get(i, "UNATTRIBUTED")
        spk = [who] * len(W)
    for w, who in zip(W, spk):
        words.append({"w": w["w"].strip(), "s": w["s"], "e": w["e"], "spk": who})
words.sort(key=lambda w: w["s"])
words = [w for w in words if w["spk"] in ("SHEPHERD", "MAGISTRATE", "PROSECUTOR")]
M = {who: metrics([dict(w) for w in words], who) for who in ("SHEPHERD", "MAGISTRATE", "PROSECUTOR")}

# 2. segments for deep_analysis: one per part; split parts re-measured
SR = 16000
wav = decode_audio(audio, sampling_rate=SR).astype(np.float64)

def pros(t0, t1, nwords):
    if t1 - t0 < 0.12:
        t1 = t0 + 0.12
    snd = parselmouth.Sound(wav[int(t0 * SR):int(t1 * SR)], sampling_frequency=SR)
    f = snd.to_pitch(time_step=0.01, pitch_floor=60, pitch_ceiling=500).selected_array["frequency"]
    v = f[f > 0]
    iv = snd.to_intensity(minimum_pitch=60, time_step=0.01).values[0]
    iv = iv[np.isfinite(iv)]
    sd = float(np.std(12 * np.log2(v / np.median(v)))) if v.size > 2 else 0.0
    return {"f0_med": round(float(np.median(v)), 1) if v.size else 0.0,
            "db_mean": round(float(iv.mean()), 1) if iv.size else 0.0,
            "voiced_frac": round(float(v.size / max(f.size, 1)), 2),
            "f0_sd_st": round(sd, 2), "wps": round(nwords / max(t1 - t0, 0.01), 2)}

parts = json.load(open(partsp))
dsegs = []
for r in parts:
    if r["who"] not in ("SHEPHERD", "MAGISTRATE", "PROSECUTOR"):
        continue
    whole = abs(r["start"] - segs[r["seg"]]["start"]) < 1e-6 and abs(r["end"] - segs[r["seg"]]["end"]) < 1e-6
    p = segs[r["seg"]]["pros"] if whole else pros(r["start"], r["end"], len(r["text"].split()))
    dsegs.append({"start": r["start"], "end": r["end"], "text": r["text"], "spk": r["who"], "pros": p})
D = analyse(dsegs, "SHEPHERD")

out = Path(outd)
json.dump(M, open(out / "court_metrics.json", "w"), indent=1)
json.dump(D, open(out / "court_deep.json", "w"), indent=1, default=str)
json.dump(dsegs, open(out / "court_segs.json", "w"), indent=1)
print(json.dumps(M, indent=1))
print(json.dumps(D, indent=1, default=str))
