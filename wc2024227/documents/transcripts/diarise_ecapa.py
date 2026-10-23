import json, time, traceback
import numpy as np
L=open("diarise3.log","a",buffering=1)
def log(*a): L.write(" ".join(str(x) for x in a)+"\n")
try:
    import torch
    from faster_whisper.audio import decode_audio
    from speechbrain.inference.speaker import EncoderClassifier
    torch.set_num_threads(4); SR=16000
    wav=torch.from_numpy(decode_audio("mention.mp3", sampling_rate=SR))
    enc=EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb",
                                       savedir="ecapa", run_opts={"device":"cpu"})
    segs=[json.loads(l) for l in open(
      "/home/user/Personalproject/wc2024227/documents/transcripts/MENTION_7AUG2026_segments.jsonl")]
    MIN=0.60; E=[]; idx=[]
    t0=time.time()
    for i,s in enumerate(segs):
        a=int(s["start"]*SR); b=min(int(s["end"]*SR), len(wav))
        if (b-a) < int(MIN*SR): continue
        with torch.no_grad():
            e=enc.encode_batch(wav[a:b].unsqueeze(0)).squeeze().numpy()
        E.append(e); idx.append(i)
    E=np.vstack(E); np.save("E.npy",E); json.dump(idx,open("E_idx.json","w"))
    log("embedded %s  %.0fs  SAVED"%(str(E.shape),time.time()-t0))

    # channel compensation: subtract global mean, then length-normalise
    Ec = E - E.mean(axis=0, keepdims=True)
    Ec = Ec/(np.linalg.norm(Ec,axis=1,keepdims=True)+1e-9)
    Eu = E/(np.linalg.norm(E,axis=1,keepdims=True)+1e-9)

    from sklearn.cluster import AgglomerativeClustering, SpectralClustering, KMeans
    def rep(name,lab):
        a=int((lab==0).sum()); b=int((lab==1).sum())
        log("  %-28s %d / %d  (minority %.1f%%)"%(name,a,b,100*min(a,b)/len(lab)))
        return lab
    res={}
    res["raw_agglom_avg"]=rep("raw agglom avg", AgglomerativeClustering(n_clusters=2,metric="cosine",linkage="average").fit_predict(Eu))
    res["cmn_agglom_avg"]=rep("mean-norm agglom avg", AgglomerativeClustering(n_clusters=2,metric="cosine",linkage="average").fit_predict(Ec))
    res["cmn_ward"]=rep("mean-norm ward", AgglomerativeClustering(n_clusters=2,linkage="ward").fit_predict(Ec))
    res["cmn_kmeans"]=rep("mean-norm kmeans", KMeans(n_clusters=2,n_init=20,random_state=0).fit_predict(Ec))
    try:
        res["cmn_spectral"]=rep("mean-norm spectral", SpectralClustering(n_clusters=2,affinity="nearest_neighbors",n_neighbors=20,random_state=0,assign_labels="kmeans").fit_predict(Ec))
    except Exception as ex: log("  spectral failed:",ex)
    json.dump({k:[int(x) for x in v] for k,v in res.items()}, open("cluster_variants.json","w"))
    json.dump(idx,open("E_idx.json","w"))
    log("VARIANTSDONE")
except Exception:
    log("ERROR\n"+traceback.format_exc())
