"""Apply speaker corrections, re-measure split parts, and build the
diarised prosody transcript + per-speaker analysis for the 2 Feb 2026 audio.

Usage: python -I build_court.py AUDIO PROSODY.jsonl DIARDIR OUTDIR
"""
import json, math, sys, statistics as st
from pathlib import Path
import numpy as np
import parselmouth
from faster_whisper.audio import decode_audio

audio, segp, diard, outd = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
SR = 16000
wav = decode_audio(audio, sampling_rate=SR).astype(np.float64)
segs = [json.loads(l) for l in open(segp, encoding="utf-8")]
C = json.load(open(diard / "clusters.json"))["k3_cmn_kmeans"]
idx = json.load(open(diard / "embedded_index.json"))
NAMES = {0: "PROSECUTOR", 1: "SHEPHERD", 2: "MAGISTRATE"}
lab = {i: NAMES[c] for i, c in zip(idx, C)}

# (segment -> [(first_word, last_word, speaker, basis)])  word indices inclusive
SPLITS = {
    0: [(0, 1, "MAGISTRATE", "pitch 214 Hz; calls the prosecutor"), (2, 19, "PROSECUTOR", "")],
    6: [(0, 4, "MAGISTRATE", "pitch 166 Hz"), (5, 8, "SHEPHERD", "repeats his answer")],
    8: [(0, 8, "SHEPHERD", ""), (9, 11, "MAGISTRATE", "pitch 202 Hz; question")],
    9: [(0, 4, "MAGISTRATE", "pitch 177 Hz"), (5, 10, "SHEPHERD", "answer")],
    27: [(0, 0, "MAGISTRATE", "pitch 200 Hz"), (1, 15, "SHEPHERD", "")],
    53: [(0, 2, "MAGISTRATE", "pitch 176 Hz; ends her sentence"), (3, 16, "PROSECUTOR", "pitch 130 Hz")],
    55: [(0, 5, "MAGISTRATE", "pitch 195 Hz; interjection"), (6, 16, "PROSECUTOR", "pitch 124 Hz")],
    61: [(0, 3, "PROSECUTOR", "pitch 126 Hz"), (4, 14, "SHEPHERD", "continues into 'medications in my list' (136 Hz); pitch here 128 Hz, ambiguous")],
    62: [(0, 4, "SHEPHERD", "pitch 136 Hz"), (5, 13, "MAGISTRATE", "pitch 175 Hz")],
    89: [(0, 4, "MAGISTRATE", "pitch 189 Hz; question"), (5, 14, "PROSECUTOR", "pitch 133 Hz; answer")],
    90: [(0, 8, "PROSECUTOR", "pitch 119 Hz"), (9, 17, "MAGISTRATE", "pitch 212 Hz")],
    95: [(0, 0, "PROSECUTOR", "end of 'outside'"), (1, 3, "MAGISTRATE", "pitch 178 Hz")],
    97: [(0, 5, "MAGISTRATE", "pitch 201 Hz"), (6, 6, "SHEPHERD", "pitch 152 Hz; 'Exactly.'")],
}
WHOLE = {  # whole-segment reassignments / assignments of unembedded segments
    20: ("PROSECUTOR", "time of the email; pitch 126 Hz"),
    21: ("PROSECUTOR", "time of the email (context)"),
    49: ("MAGISTRATE", "pitch 209 Hz"),
    50: ("SHEPHERD", "ECAPA said Magistrate; pitch 129 Hz and content (answers 'Which bit?')"),
    122: ("MAGISTRATE", "too short to embed; pitch 183 Hz matches the Magistrate (flagged)"),
    132: ("UNATTRIBUTED", "too short to embed; pitch 105 Hz"),
}
NOTES = {  # likely mishearings, shown in the transcript as [?…]
    "Scottsdale": "Scott schedule?", "Prince Sergeant": "?… Sergeant", "NATO": "NATA?",
    "Mr Hodges": "Mr Hodgetts", "with the women they can get a check": "?… can get a check",
    "between a horse and a car": "?horse and cart", "mr here": "?…", "VIX": "Vicks",
}

def measure(t0, t1, nwords):
    dur = max(t1 - t0, 0.01)
    if dur < 0.12:
        t1 = t0 + 0.12
    snd = parselmouth.Sound(wav[int(t0 * SR):int(t1 * SR)], sampling_frequency=SR)
    f = snd.to_pitch(time_step=0.01, pitch_floor=60, pitch_ceiling=500).selected_array["frequency"]
    v = f[f > 0]
    iv = snd.to_intensity(minimum_pitch=60, time_step=0.01).values[0]
    iv = iv[np.isfinite(iv)]
    if v.size:
        lo, hi = np.percentile(v, 5), np.percentile(v, 95)
        rng = 12 * math.log2(hi / lo) if lo > 0 else 0.0
    else:
        rng = 0.0
    return {"f0": round(float(np.median(v)), 1) if v.size else 0.0,
            "db": round(float(iv.mean()), 1) if iv.size else 0.0,
            "range_st": round(rng, 2), "wps": round(nwords / dur, 2), "dur": round(dur, 2)}

parts, amend = [], []
for i, s in enumerate(segs):
    W = s["words"]
    if i in SPLITS:
        for a, b, who, basis in SPLITS[i]:
            w = W[a:b + 1]
            t0, t1 = w[0]["s"], w[-1]["e"]
            text = " ".join(x["w"].strip() for x in w)
            parts.append({"seg": i, "who": who, "start": t0, "end": t1, "text": text,
                          "pmin": min(x["p"] for x in w), **measure(t0, t1, len(w))})
            amend.append(f"seg {i} words {a}-{b} -> {who}" + (f" ({basis})" if basis else ""))
    else:
        if i in WHOLE:
            who, basis = WHOLE[i]
            amend.append(f"seg {i} -> {who} ({basis})")
        else:
            who = lab.get(i, "UNATTRIBUTED")
        p = s.get("pros") or {}
        parts.append({"seg": i, "who": who, "start": s["start"], "end": s["end"], "text": s["text"],
                      "pmin": min((x["p"] for x in W), default=1.0),
                      "f0": p.get("f0_med", 0.0), "db": p.get("db_mean", 0.0),
                      "range_st": p.get("f0_range_st", 0.0), "wps": p.get("wps", 0.0),
                      "dur": round(s["end"] - s["start"], 2)})
parts.sort(key=lambda r: r["start"])
for k, r in enumerate(parts):
    for wrong, right in NOTES.items():
        if wrong in r["text"]:
            r["text"] = r["text"].replace(wrong, f"{wrong} [{right}]")

# turns: merge consecutive parts by the same speaker separated by < 1.5 s
turns = []
for r in parts:
    if turns and turns[-1]["who"] == r["who"] and r["start"] - turns[-1]["end"] < 1.5:
        t = turns[-1]; t["end"] = r["end"]; t["text"] += " " + r["text"]; t["parts"].append(r)
    else:
        turns.append({"who": r["who"], "start": r["start"], "end": r["end"], "text": r["text"], "parts": [r]})
def wavg(rs, key):
    num = sum(x[key] * x["dur"] for x in rs if x[key]); den = sum(x["dur"] for x in rs if x[key])
    return round(num / den, 1) if den else 0.0
for t in turns:
    t["dur"] = round(t["end"] - t["start"], 2)
    t["f0"] = wavg(t["parts"], "f0"); t["db"] = wavg(t["parts"], "db")
    t["range_st"] = wavg(t["parts"], "range_st")
    t["nwords"] = sum(len(x["text"].split()) for x in t["parts"])
    t["wps"] = round(t["nwords"] / sum(x["dur"] for x in t["parts"]), 2)

speakers = ["MAGISTRATE", "PROSECUTOR", "SHEPHERD"]
summ = {}
for w in speakers:
    rs = [r for r in parts if r["who"] == w]
    talk = sum(r["dur"] for r in rs); words = sum(len(r["text"].split()) for r in rs)
    f0s = [r["f0"] for r in rs if r["f0"]]; dbs = [r["db"] for r in rs if r["db"]]
    tw = [t for t in turns if t["who"] == w]
    summ[w] = {"turns": len(tw), "talk_s": round(talk, 1), "words": words,
               "wpm": round(60 * words / talk, 1) if talk else 0,
               "f0_median": round(st.median(f0s), 1), "f0_p25": round(float(np.percentile(f0s, 25)), 1),
               "f0_p75": round(float(np.percentile(f0s, 75)), 1),
               "db_median": round(st.median(dbs), 1), "db_p25": round(float(np.percentile(dbs, 25)), 1),
               "db_p75": round(float(np.percentile(dbs, 75)), 1),
               "range_p25": round(float(np.percentile([r["range_st"] for r in rs], 25)), 2),
               "range_p75": round(float(np.percentile([r["range_st"] for r in rs], 75)), 2),
               "wps_p25": round(float(np.percentile([r["wps"] for r in rs], 25)), 2),
               "wps_p75": round(float(np.percentile([r["wps"] for r in rs], 75)), 2),
               "longest_turn_s": max(t["dur"] for t in tw), "median_turn_s": round(st.median([t["dur"] for t in tw]), 2)}
total = sum(v["talk_s"] for v in summ.values())
for v in summ.values():
    v["share_pct"] = round(100 * v["talk_s"] / total, 1)

# transitions
trans = {}
for a, b in zip(turns, turns[1:]):
    if a["who"] != b["who"] and "UNATTRIBUTED" not in (a["who"], b["who"]):
        trans.setdefault(f"{a['who']}->{b['who']}", []).append(round(b["start"] - a["end"], 2))
trans_s = {k: {"n": len(v), "median_s": round(st.median(v), 2), "min_s": min(v),
               "overlaps": sum(1 for x in v if x < 0), "over_2s": sum(1 for x in v if x > 2)}
           for k, v in sorted(trans.items())}
who_follows = {}
for a, b in zip(turns, turns[1:]):
    if a["who"] != b["who"]:
        who_follows.setdefault(a["who"], {}).setdefault(b["who"], 0)
        who_follows[a["who"]][b["who"]] += 1

def stv(f, base):
    return round(12 * math.log2(f / base), 1) if f and base else 0.0
def markers(t):
    s = summ.get(t["who"])
    if not s:
        return ""
    m = []
    d = stv(t["f0"], s["f0_median"])
    if abs(d) >= 2: m.append(f"{'↑+' if d > 0 else '↓'}{d}st")
    if t["range_st"] > s["range_p75"] + 0.01: m.append("wide")
    elif t["range_st"] and t["range_st"] < s["range_p25"] - 0.01: m.append("flat")
    if t["wps"] > s["wps_p75"]: m.append(f"fast {t['wps']}w/s")
    elif t["wps"] < s["wps_p25"]: m.append(f"slow {t['wps']}w/s")
    if t["db"] > s["db_p75"]: m.append("louder")
    elif t["db"] and t["db"] < s["db_p25"]: m.append("quieter")
    return " ".join(m)

def ts(x):
    return f"{int(x // 60):02d}:{x % 60:05.2f}"
lines = []
prev_end = None
for t in turns:
    gap = None if prev_end is None else t["start"] - prev_end
    if gap is not None and gap >= 2.0:
        lines.append(f"            *({gap:.1f}s pause)*\n")
    mk = markers(t)
    low = [x for x in t["parts"] if x["pmin"] < 0.5]
    lines.append(f"**{ts(t['start'])}  {t['who']}**" + (f"  `{mk}`" if mk else "") +
                 f"  ·  {t['dur']:.1f}s  f0 {t['f0']:.0f} Hz  {t['db']:.1f} dB" +
                 ("  ⚑low-confidence word" if low else "") + f"\n> {t['text']}\n")
    prev_end = t["end"]

# extremes (speaker-relative), turns >= 1.0 s
ext = {}
for w in speakers:
    tw = [t for t in turns if t["who"] == w and t["dur"] >= 1.0 and t["db"]]
    s = summ[w]
    f = lambda t: {"at": ts(t["start"]), "dur": t["dur"], "db": t["db"],
                   "d_db": round(t["db"] - s["db_median"], 1), "f0": t["f0"],
                   "d_st": stv(t["f0"], s["f0_median"]), "text": t["text"][:200]}
    ext[w] = {"loudest": [f(t) for t in sorted(tw, key=lambda t: -t["db"])[:4]],
              "quietest": [f(t) for t in sorted(tw, key=lambda t: t["db"])[:3]],
              "highest": [f(t) for t in sorted(tw, key=lambda t: -t["f0"])[:4]],
              "lowest": [f(t) for t in sorted([t for t in tw if t["f0"]], key=lambda t: t["f0"])[:3]],
              "longest": [f(t) for t in sorted(tw, key=lambda t: -t["dur"])[:3]]}

outd.mkdir(parents=True, exist_ok=True)
json.dump(parts, open(outd / "parts.json", "w"), indent=1, ensure_ascii=False)
json.dump({"summary": summ, "transitions": trans_s, "who_follows": who_follows, "extremes": ext,
           "amendments": amend, "n_turns": len(turns)}, open(outd / "analysis.json", "w"),
          indent=1, ensure_ascii=False)
json.dump([{k: v for k, v in t.items() if k != "parts"} for t in turns],
          open(outd / "turns.json", "w"), indent=1, ensure_ascii=False)
open(outd / "transcript_body.md", "w", encoding="utf-8").write("\n".join(lines))
print(json.dumps(summ, indent=1))
print(json.dumps(trans_s, indent=1))
print("who follows", who_follows)
print("turns", len(turns))
