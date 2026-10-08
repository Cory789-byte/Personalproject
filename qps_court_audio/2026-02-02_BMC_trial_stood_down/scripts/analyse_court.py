"""Per-speaker structure, pitch and level for a diarised court recording.

Usage: python -I analyse_court.py PROSODY.jsonl DIARDIR VARIANT NAMES OUT.json
  NAMES like "0=MAGISTRATE,1=PROSECUTOR,2=SHEPHERD"
"""
import json, sys, math, statistics as st
from pathlib import Path

pros_p, diard, variant, names_s, out = sys.argv[1:6]
segs = [json.loads(l) for l in open(pros_p, encoding="utf-8")]
d = Path(diard)
clusters = json.load(open(d / "clusters.json"))
idx = json.load(open(d / "embedded_index.json"))
lab = dict(zip(idx, clusters[variant]))
names = {}
for pair in filter(None, names_s.split(",")):
    k, _, v = pair.partition("=")
    names[int(k)] = v

rows = []
for i, s in enumerate(segs):
    who = names.get(lab.get(i), "UNASSIGNED") if i in lab else "UNASSIGNED"
    p = s.get("pros") or {}
    rows.append({"i": i, "who": who, "start": s["start"], "end": s["end"],
                 "dur": round(s["end"] - s["start"], 2), "text": s["text"],
                 "nwords": len(s.get("words") or []) or len(s["text"].split()),
                 "f0": p.get("f0_med", 0.0), "db": p.get("db_mean", 0.0),
                 "range_st": p.get("f0_range_st", 0.0), "wps": p.get("wps", 0.0),
                 "gap_before": s.get("gap_before")})

def med(v):
    v = [x for x in v if x]
    return round(st.median(v), 1) if v else 0.0

spk = {}
for r in rows:
    spk.setdefault(r["who"], []).append(r)
total_talk = sum(r["dur"] for r in rows)
summary = {}
for w, rs in spk.items():
    talk = sum(r["dur"] for r in rs)
    words = sum(r["nwords"] for r in rs)
    summary[w] = {"segments": len(rs), "talk_s": round(talk, 1),
                  "share_pct": round(100 * talk / total_talk, 1) if total_talk else 0,
                  "words": words, "wpm": round(60 * words / talk, 1) if talk else 0,
                  "f0_median": med([r["f0"] for r in rs]),
                  "db_median": med([r["db"] for r in rs]),
                  "range_st_median": med([r["range_st"] for r in rs]),
                  "longest_turn_s": max(r["dur"] for r in rs)}

# turns: merge consecutive segments by the same speaker
turns = []
for r in rows:
    if turns and turns[-1]["who"] == r["who"] and (r["start"] - turns[-1]["end"]) < 1.5:
        t = turns[-1]; t["end"] = r["end"]; t["text"] += " " + r["text"]; t["segs"].append(r["i"])
        t["nwords"] += r["nwords"]
    else:
        turns.append({"who": r["who"], "start": r["start"], "end": r["end"], "text": r["text"],
                      "segs": [r["i"]], "nwords": r["nwords"]})
for t in turns:
    t["dur"] = round(t["end"] - t["start"], 2)
    segp = [rows[i] for i in t["segs"]]
    wt = sum(x["dur"] for x in segp) or 1
    t["f0"] = round(sum(x["f0"] * x["dur"] for x in segp if x["f0"]) / max(sum(x["dur"] for x in segp if x["f0"]), 1e-9), 1)
    t["db"] = round(sum(x["db"] * x["dur"] for x in segp if x["db"]) / max(sum(x["dur"] for x in segp if x["db"]), 1e-9), 1)

changes, latencies, overlaps = 0, [], 0
for a, b in zip(turns, turns[1:]):
    if a["who"] != b["who"]:
        changes += 1
        g = round(b["start"] - a["end"], 2)
        latencies.append((b["who"], g))
        if g < 0:
            overlaps += 1
lat_by = {}
for w, g in latencies:
    lat_by.setdefault(w, []).append(g)
lat_summary = {w: {"n": len(v), "median_s": round(st.median(v), 2),
                   "over_2s": sum(1 for x in v if x > 2)} for w, v in lat_by.items()}

# speaker-relative extremes
ext = {}
for w, rs in spk.items():
    tw = [t for t in turns if t["who"] == w and t["dur"] >= 1.5 and t["db"]]
    if not tw:
        continue
    base_db = summary[w]["db_median"]; base_f0 = summary[w]["f0_median"]
    def stv(f):
        return round(12 * math.log2(f / base_f0), 1) if f and base_f0 else 0.0
    loud = sorted(tw, key=lambda t: -t["db"])[:3]
    quiet = sorted(tw, key=lambda t: t["db"])[:3]
    longest = sorted(tw, key=lambda t: -t["dur"])[:3]
    fmt = lambda t: {"start": t["start"], "dur": t["dur"], "db": t["db"],
                     "d_db": round(t["db"] - base_db, 1), "f0": t["f0"], "d_st": stv(t["f0"]),
                     "text": t["text"][:160]}
    ext[w] = {"loudest": [fmt(t) for t in loud], "quietest": [fmt(t) for t in quiet],
              "longest": [fmt(t) for t in longest]}

json.dump({"variant": variant, "names": names, "summary": summary, "turn_count": len(turns),
           "speaker_changes": changes, "overlaps": overlaps, "latency": lat_summary,
           "extremes": ext, "turns": turns}, open(out, "w"), indent=1, ensure_ascii=False)
for w, s in sorted(summary.items(), key=lambda kv: -kv[1]["talk_s"]):
    print(w, s)
print("turns", len(turns), "changes", changes, "overlaps", overlaps)
print("latency", lat_summary)
