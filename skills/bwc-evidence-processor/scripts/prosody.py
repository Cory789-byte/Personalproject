"""Per-segment Praat prosody — f0, intensity, rate, pause structure.

Emits the SAME field set as MENTION_7AUG2026_segments.jsonl so the two
matters can be compared directly:

  f0_med f0_mean f0_sd_st f0_min f0_max f0_range_st voiced_frac
  db_mean db_sd wps dur nwords

plus gap_before (silence to the previous segment, seconds).

Semitone figures are computed on the segment's own f0 track.
Speaker-relative semitone deltas are derived later, against each
speaker's own median, so they need no reference here.

Usage:
  python prosody.py AUDIO SEGMENTS.jsonl OUT.jsonl [--start S] [--end S]

--start/--end process a time window only, so a long file can be run in
pieces and concatenated. Memory is bounded: audio is decoded once and
segments are sliced from it.
"""
from __future__ import annotations
import argparse, json, math, sys, time
from pathlib import Path

import numpy as np

SR = 16000
F0_FLOOR, F0_CEIL = 60.0, 500.0   # wide enough for mixed male/female speakers


def st(a: float, b: float) -> float:
    """Interval a->b in semitones."""
    if a and b and a > 0 and b > 0:
        return 12.0 * math.log2(b / a)
    return 0.0


def analyse(snd, nwords: int, dur: float) -> dict | None:
    import parselmouth
    try:
        pitch = snd.to_pitch(time_step=0.01, pitch_floor=F0_FLOOR, pitch_ceiling=F0_CEIL)
        f = pitch.selected_array["frequency"]
    except Exception:
        return None
    voiced = f[f > 0]
    try:
        inten = snd.to_intensity(minimum_pitch=F0_FLOOR, time_step=0.01)
        iv = inten.values[0]
        iv = iv[np.isfinite(iv)]
    except Exception:
        iv = np.array([])

    if voiced.size:
        fmin, fmax = float(voiced.min()), float(voiced.max())
        med = float(np.median(voiced))
        # SD expressed in semitones relative to this segment's median
        sd_st = float(np.std(12.0 * np.log2(voiced / med))) if med > 0 else 0.0
    else:
        fmin = fmax = med = sd_st = 0.0

    return {
        "f0_med": round(med, 1),
        "f0_mean": round(float(voiced.mean()), 1) if voiced.size else 0.0,
        "f0_sd_st": round(sd_st, 2),
        "f0_min": round(fmin, 1),
        "f0_max": round(fmax, 1),
        "f0_range_st": round(st(fmin, fmax), 2),
        "voiced_frac": round(float(voiced.size / max(f.size, 1)), 2),
        "db_mean": round(float(iv.mean()), 1) if iv.size else 0.0,
        "db_sd": round(float(iv.std()), 2) if iv.size else 0.0,
        "wps": round(nwords / dur, 2) if dur > 0 else 0.0,
        "dur": round(dur, 2),
        "nwords": nwords,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("audio"); ap.add_argument("segments"); ap.add_argument("out")
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--end", type=float, default=float("inf"))
    a = ap.parse_args()

    import parselmouth
    from faster_whisper.audio import decode_audio

    segs = [json.loads(l) for l in open(a.segments, encoding="utf-8")]
    print(f"loaded {len(segs)} segments", flush=True)
    wav = decode_audio(a.audio, sampling_rate=SR)
    total = len(wav) / SR
    print(f"decoded {total/60:.1f} min of audio @ {SR} Hz", flush=True)

    done = skipped = 0
    t0 = time.time()
    prev_end = None
    with open(a.out, "w", encoding="utf-8") as fh:
        for s in segs:
            if s["end"] < a.start or s["start"] > a.end:
                continue
            i0, i1 = int(s["start"] * SR), min(int(s["end"] * SR), len(wav))
            dur = (i1 - i0) / SR
            s["gap_before"] = None if prev_end is None else round(s["start"] - prev_end, 2)
            prev_end = s["end"]
            nwords = len(s.get("words") or []) or len(s.get("text", "").split())
            if dur < 0.10:
                s["pros"] = None; skipped += 1
            else:
                snd = parselmouth.Sound(wav[i0:i1].astype(np.float64), sampling_frequency=SR)
                s["pros"] = analyse(snd, nwords, dur)
                if s["pros"] is None:
                    skipped += 1
                else:
                    done += 1
            fh.write(json.dumps(s, ensure_ascii=False) + "\n")
            if (done + skipped) % 250 == 0:
                print(f"  {done+skipped}/{len(segs)}  {time.time()-t0:.0f}s", flush=True)

    print(f"DONE  analysed={done}  skipped={skipped}  {time.time()-t0:.0f}s  -> {a.out}")


if __name__ == "__main__":
    main()
