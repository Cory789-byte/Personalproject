"""ECAPA-TDNN speaker clustering for a multi-party court recording.

Same embedding method as wc2024227/documents/transcripts/diarise_ecapa.py
(speechbrain spkrec-ecapa-voxceleb, mean-normalised, length-normalised),
but the number of speakers is unknown, so several k are tried and scored
by silhouette. Writes clusters.json {variant: [labels]} and
embedded_index.json [segment indices] for build_diarised_prosody.py.

Usage: python -I diarise_court.py AUDIO SEGMENTS.jsonl OUTDIR
"""
import json, sys, time
from pathlib import Path
import numpy as np

audio, segp, outd = sys.argv[1], sys.argv[2], Path(sys.argv[3])
outd.mkdir(parents=True, exist_ok=True)
import torch
from faster_whisper.audio import decode_audio
from speechbrain.inference.speaker import EncoderClassifier
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.metrics import silhouette_score

torch.set_num_threads(4)
SR = 16000
wav = torch.from_numpy(decode_audio(audio, sampling_rate=SR))
enc = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb",
                                     savedir=str(outd / "ecapa_model"), run_opts={"device": "cpu"})
segs = [json.loads(l) for l in open(segp, encoding="utf-8")]
MIN = 0.60
E, idx = [], []
t0 = time.time()
for i, s in enumerate(segs):
    a = int(s["start"] * SR); b = min(int(s["end"] * SR), len(wav))
    if (b - a) < int(MIN * SR):
        continue
    with torch.no_grad():
        e = enc.encode_batch(wav[a:b].unsqueeze(0)).squeeze().numpy()
    E.append(e); idx.append(i)
E = np.vstack(E)
np.save(outd / "E.npy", E)
Ec = E - E.mean(axis=0, keepdims=True)
Ec = Ec / (np.linalg.norm(Ec, axis=1, keepdims=True) + 1e-9)

res, report = {}, {}
for k in range(2, 7):
    if k >= len(idx):
        break
    for name, model in (
        (f"k{k}_cmn_agglom_avg", AgglomerativeClustering(n_clusters=k, metric="cosine", linkage="average")),
        (f"k{k}_cmn_ward", AgglomerativeClustering(n_clusters=k, linkage="ward")),
        (f"k{k}_cmn_kmeans", KMeans(n_clusters=k, n_init=20, random_state=0)),
    ):
        lab = model.fit_predict(Ec)
        sil = float(silhouette_score(Ec, lab, metric="cosine")) if len(set(lab)) > 1 else -1.0
        res[name] = [int(x) for x in lab]
        report[name] = {"silhouette": round(sil, 3),
                        "sizes": sorted([int((lab == c).sum()) for c in set(lab)], reverse=True)}
json.dump(res, open(outd / "clusters.json", "w"))
json.dump(idx, open(outd / "embedded_index.json", "w"))
json.dump(report, open(outd / "cluster_report.json", "w"), indent=1)
print(f"embedded {E.shape} in {time.time()-t0:.0f}s")
for n, r in sorted(report.items(), key=lambda kv: -kv[1]["silhouette"])[:10]:
    print(n, r)
