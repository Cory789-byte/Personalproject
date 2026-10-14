"""Merge segments + prosody + ECAPA labels into a diarised prosody transcript.

Reproduces the marker vocabulary used in the WC/2024/227 mention transcript:
  ↑/↓ Nst  pitch shift vs THAT SPEAKER'S own median   (|delta| >= --st)
  wide/flat   f0 range above p75 / below p25 for that speaker
  fast/slow N.Nw/s   rate above p75 / below p25
  louder/quieter     intensity above p75 / below p25
  (N.Ns pause)       silence before the turn, >= --pause seconds

Markers are ALWAYS speaker-relative. Absolute Hz/dB never compare across
speakers — different voices, different mics, different distances.

Usage:
  python build_diarised_prosody.py PROSODY.jsonl DIARDIR OUT.md \
      [--variant k3_cmn_ward] [--names "SPK0=BICKERY,SPK1=SHEPHERD"]
"""
from __future__ import annotations
import argparse, json, math, statistics as st
from pathlib import Path


def pctl(v, q):
    v = sorted(v)
    if not v:
        return 0.0
    return v[min(int(q * len(v)), len(v) - 1)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("prosody"); ap.add_argument("diardir"); ap.add_argument("out")
    ap.add_argument("--variant", default=None)
    ap.add_argument("--names", default="")
    ap.add_argument("--st", type=float, default=2.0)
    ap.add_argument("--pause", type=float, default=2.0)
    a = ap.parse_args()

    segs = [json.loads(l) for l in open(a.prosody, encoding="utf-8")]
    d = Path(a.diardir)
    clusters = json.load(open(d / "clusters.json"))
    idx = json.load(open(d / "embedded_index.json"))

    variant = a.variant or sorted(clusters)[0]
    if variant not in clusters:
        raise SystemExit(f"variant {variant!r} not in {sorted(clusters)}")
    lab = dict(zip(idx, clusters[variant]))

    names = {}
    for pair in filter(None, a.names.split(",")):
        k, _, v = pair.partition("=")
        names[k.strip()] = v.strip()

    def who(sid):
        k = lab.get(sid)
        return "UNASSIGNED" if k is None else names.get(f"SPK{k}", f"SPK{k}")

    for s in segs:
        s["spk"] = who(s.get("id"))

    # per-speaker baselines
    base = {}
    for spk in sorted({s["spk"] for s in segs}):
        rows = [s["pros"] for s in segs if s["spk"] == spk and s.get("pros")]
        if not rows:
            continue
        base[spk] = {
            "f0": st.median([r["f0_med"] for r in rows if r["f0_med"] > 0] or [0]),
            "rng": [pctl([r["f0_range_st"] for r in rows], q) for q in (.25, .75)],
            "db": [pctl([r["db_mean"] for r in rows], q) for q in (.25, .75)],
            "wps": [pctl([r["wps"] for r in rows], q) for q in (.25, .75)],
            "n": len(rows),
            "talk": sum(r["dur"] for r in rows),
            "words": sum(r["nwords"] for r in rows),
        }

    def markers(spk, p):
        if not p or spk not in base:
            return ""
        b = mk = base[spk]; out = []
        if p["f0_med"] > 0 and b["f0"] > 0:
            delta = 12 * math.log2(p["f0_med"] / b["f0"])
            if abs(delta) >= a.st:
                out.append(f"{'↑+' if delta > 0 else '↓'}{delta:.1f}st")
        if p["f0_range_st"] >= b["rng"][1]:
            out.append("wide")
        elif p["f0_range_st"] <= b["rng"][0]:
            out.append("flat")
        if p["wps"] >= b["wps"][1]:
            out.append(f"fast {p['wps']:.1f}w/s")
        elif p["wps"] <= b["wps"][0]:
            out.append(f"slow {p['wps']:.1f}w/s")
        if p["db_mean"] >= b["db"][1]:
            out.append("louder")
        elif p["db_mean"] <= b["db"][0]:
            out.append("quieter")
        return "  `" + " ".join(out) + "`" if out else ""

    L = ["# DIARISED TRANSCRIPT WITH PROSODY",
         "",
         "> **MACHINE-GENERATED — UNVERIFIED.** Speaker labels are acoustic inference",
         "> (ECAPA-TDNN embeddings, clustering variant `%s`), not participant evidence." % variant,
         "> Prosodic markers are **relative to each speaker's own baseline** and never",
         "> compare one speaker to another.",
         "",
         "## SPEAKING SHARE", "",
         "| Speaker | Segments | Talk time | Words | Share |", "|---|---|---|---|---|"]
    tot = sum(b["talk"] for b in base.values()) or 1.0
    for spk, b in sorted(base.items(), key=lambda kv: -kv[1]["talk"]):
        L.append(f"| {spk} | {b['n']} | {b['talk']/60:.1f} min | {b['words']} | "
                 f"**{100*b['talk']/tot:.1f}%** |")
    L += ["", "## PROSODIC MARKERS",
          "`↑/↓ Nst` pitch vs that speaker's median · `wide`/`flat` f0 range · "
          "`fast`/`slow` rate · `louder`/`quieter` intensity · *(N.Ns pause)*", "", "---", ""]

    last = None
    for s in segs:
        g = s.get("gap_before")
        if g is not None and g >= a.pause:
            L.append(f"            *({g:.1f}s pause)*\n")
        head = s["spk"] != last
        last = s["spk"]
        ts = f"{int(s['start']//60):02d}:{s['start']%60:05.2f}"
        if head:
            L.append(f"**{ts}  {s['spk']}**{markers(s['spk'], s.get('pros'))}  ")
            L.append(s["text"])
        else:
            L.append(f"{s['text']}{markers(s['spk'], s.get('pros'))}")
        L.append("")

    Path(a.out).write_text("\n".join(L), encoding="utf-8")
    print(f"wrote {a.out}  ({len(segs)} segments, {len(base)} speakers, variant {variant})")


if __name__ == "__main__":
    main()
