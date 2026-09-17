"""ECAPA-TDNN speaker diarisation — same method as the WC/2024/227 mention run.

SpeechBrain spkrec-ecapa-voxceleb embeddings per transcript segment,
global-mean channel compensation, several clusterings reported side by
side so the stable partition is visible rather than assumed.

Shares NOTHING with any lexical or adjacency heuristic: purely acoustic.

Usage:
  python diarise_ecapa.py AUDIO SEGMENTS.jsonl OUTDIR [--speakers 2 3 4] [--min-dur 0.60]

Writes to OUTDIR:
  embeddings.npy        one row per embedded segment
  embedded_index.json   segment ids, aligned with embeddings.npy
  clusters.json         {variant_name: [label per embedded segment]}
  report.txt            cluster sizes per variant
"""
from __future__ import annotations
import argparse, json, time, traceback
from pathlib import Path

import numpy as np

SR = 16000


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("audio"); ap.add_argument("segments"); ap.add_argument("outdir")
    ap.add_argument("--speakers", type=int, nargs="+", default=[2, 3, 4])
    ap.add_argument("--min-dur", type=float, default=0.60)
    ap.add_argument("--threads", type=int, default=4)
    a = ap.parse_args()

    out = Path(a.outdir); out.mkdir(parents=True, exist_ok=True)
    log_lines: list[str] = []

    def log(*parts):
        line = " ".join(str(p) for p in parts)
        print(line, flush=True); log_lines.append(line)

    try:
        import torch
        from faster_whisper.audio import decode_audio
        from speechbrain.inference.speaker import EncoderClassifier

        torch.set_num_threads(a.threads)
        wav = torch.from_numpy(decode_audio(a.audio, sampling_rate=SR))
        log(f"decoded {len(wav)/SR/60:.1f} min")

        enc = EncoderClassifier.from_hparams(
            source="speechbrain/spkrec-ecapa-voxceleb",
            savedir=str(out / "ecapa"), run_opts={"device": "cpu"})

        segs = [json.loads(l) for l in open(a.segments, encoding="utf-8")]
        E, idx = [], []
        t0 = time.time()
        for i, s in enumerate(segs):
            b0, b1 = int(s["start"] * SR), min(int(s["end"] * SR), len(wav))
            if (b1 - b0) < int(a.min_dur * SR):
                continue
            with torch.no_grad():
                e = enc.encode_batch(wav[b0:b1].unsqueeze(0)).squeeze().numpy()
            E.append(e); idx.append(s.get("id", i))
            if len(E) % 250 == 0:
                log(f"  embedded {len(E)}  {time.time()-t0:.0f}s")

        E = np.vstack(E)
        np.save(out / "embeddings.npy", E)
        json.dump(idx, open(out / "embedded_index.json", "w"))
        log(f"embedded {E.shape}  {time.time()-t0:.0f}s  "
            f"({len(segs)-len(idx)} segments too short at <{a.min_dur}s)")

        # channel compensation: subtract the global mean, then length-normalise
        Ec = E - E.mean(axis=0, keepdims=True)
        Ec = Ec / (np.linalg.norm(Ec, axis=1, keepdims=True) + 1e-9)
        Eu = E / (np.linalg.norm(E, axis=1, keepdims=True) + 1e-9)

        from sklearn.cluster import AgglomerativeClustering, KMeans, SpectralClustering
        res: dict[str, list[int]] = {}

        def rep(name, lab):
            sizes = np.bincount(lab, minlength=lab.max() + 1)
            pct = " / ".join(f"{s} ({100*s/len(lab):.1f}%)" for s in sizes)
            log(f"  {name:34s} {pct}")
            res[name] = [int(x) for x in lab]

        for k in a.speakers:
            rep(f"k{k}_raw_agglom_avg", AgglomerativeClustering(
                n_clusters=k, metric="cosine", linkage="average").fit_predict(Eu))
            rep(f"k{k}_cmn_agglom_avg", AgglomerativeClustering(
                n_clusters=k, metric="cosine", linkage="average").fit_predict(Ec))
            rep(f"k{k}_cmn_ward", AgglomerativeClustering(
                n_clusters=k, linkage="ward").fit_predict(Ec))
            rep(f"k{k}_cmn_kmeans", KMeans(
                n_clusters=k, n_init=20, random_state=0).fit_predict(Ec))
            try:
                nn = max(2, min(20, len(Ec) - 1))
                rep(f"k{k}_cmn_spectral", SpectralClustering(
                    n_clusters=k, affinity="nearest_neighbors", n_neighbors=nn,
                    random_state=0, assign_labels="kmeans").fit_predict(Ec))
            except Exception as ex:
                log(f"  k{k} spectral failed: {ex}")

        json.dump(res, open(out / "clusters.json", "w"))
        log("VARIANTS DONE")
    except Exception:
        log("ERROR\n" + traceback.format_exc())
    finally:
        (out / "report.txt").write_text("\n".join(log_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
