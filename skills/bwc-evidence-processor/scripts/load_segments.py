"""Normalise an EXISTING transcript into segments.jsonl — the shortcut.

Avoids re-running Whisper. Accepts:
  * faster-whisper / whisper JSON  (dict with "segments", or a bare list)
  * this skill's <stem>.transcript.json
  * SubRip .srt
Emits one JSON object per line:
  {"id","start","end","text","words":[{"w","s","e","p"}...]}
matching the schema used by MENTION_7AUG2026_segments.jsonl so the
outputs of both matters are directly comparable.

Usage:  python load_segments.py IN.(json|srt) OUT.jsonl
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

SRT_TS = re.compile(
    r"(\d{2}):(\d{2}):(\d{2})[,.](\d{1,3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})[,.](\d{1,3})")


def _secs(h, m, s, ms) -> float:
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms.ljust(3, "0")) / 1000.0


def from_srt(text: str) -> list[dict]:
    out, cur = [], None
    for line in text.splitlines():
        m = SRT_TS.search(line)
        if m:
            if cur:
                out.append(cur)
            cur = {"start": _secs(*m.group(1, 2, 3, 4)),
                   "end": _secs(*m.group(5, 6, 7, 8)), "text": "", "words": []}
        elif cur is not None and line.strip() and not line.strip().isdigit():
            cur["text"] = (cur["text"] + " " + line.strip()).strip()
    if cur:
        out.append(cur)
    return out


def _words(seg: dict) -> list[dict]:
    raw = seg.get("words") or seg.get("word_timestamps") or []
    out = []
    for w in raw:
        if not isinstance(w, dict):
            continue
        out.append({
            "w": w.get("w", w.get("word", w.get("text", ""))),
            "s": float(w.get("s", w.get("start", 0.0)) or 0.0),
            "e": float(w.get("e", w.get("end", 0.0)) or 0.0),
            "p": float(w.get("p", w.get("probability", w.get("confidence", 0.0))) or 0.0),
        })
    return out


def from_json(obj) -> list[dict]:
    segs = obj["segments"] if isinstance(obj, dict) and "segments" in obj else obj
    if not isinstance(segs, list):
        raise SystemExit("unrecognised transcript JSON: no segment list found")
    out = []
    for s in segs:
        out.append({
            "start": float(s.get("start", s.get("s", 0.0)) or 0.0),
            "end": float(s.get("end", s.get("e", 0.0)) or 0.0),
            "text": (s.get("text") or "").strip(),
            "words": _words(s),
        })
    return out


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    body = src.read_text(encoding="utf-8", errors="replace")
    segs = from_srt(body) if src.suffix.lower() == ".srt" else from_json(json.loads(body))
    segs = [s for s in segs if s["end"] > s["start"]]
    segs.sort(key=lambda s: s["start"])
    with dst.open("w", encoding="utf-8") as fh:
        for i, s in enumerate(segs):
            s["id"] = i
            fh.write(json.dumps(s, ensure_ascii=False) + "\n")
    dur = segs[-1]["end"] if segs else 0.0
    withw = sum(1 for s in segs if s["words"])
    print(f"{len(segs)} segments -> {dst}")
    print(f"  span {dur/60:.1f} min | {withw} segments carry word-level timings")


if __name__ == "__main__":
    main()
