"""Word-by-word forensic review.

Emits a long-form CSV: one row per Whisper word, with:
- timestamp (start, end, duration, gap-to-prev)
- confidence (Whisper per-word probability)
- low_confidence flag (probability < threshold)
- flagged_phrase: matched phrase (caution / invocation / inducement / etc.)
- flagged_category
- inferred speaker role (segment-level)

This is the "every word, every frame-level timestamp" slice counsel uses to
build precise cross-examination passages. Outputs remain machine-generated.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from bias_analysis import infer_role
from procedural_compliance import (
    CAUTION_PHRASES,
    INVOCATION_PHRASES,
    ARREST_LANGUAGE,
    PROMISES_THREATS,
    LEADING_QUESTIONS,
)

HEADER = "MACHINE-GENERATED - UNVERIFIED"

PHRASE_BANK = [
    ("caution", CAUTION_PHRASES),
    ("invocation", INVOCATION_PHRASES),
    ("arrest_language", ARREST_LANGUAGE),
    ("inducement", PROMISES_THREATS),
    ("leading_question", LEADING_QUESTIONS),
]


def _match_categories(segment_text: str) -> list[str]:
    lt = segment_text.lower()
    hits = []
    for name, phrases in PHRASE_BANK:
        if any(p in lt for p in phrases):
            hits.append(name)
    return hits


def build(transcript: Path, dest: Path, low_conf_threshold: float = 0.5) -> Path:
    data = json.loads(Path(transcript).read_text(encoding="utf-8"))
    segments = data["segments"]

    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)

    prev_end = 0.0
    with dest.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# {HEADER}\n")
        w = csv.writer(f)
        w.writerow([
            "row", "segment_index", "word_index_in_segment",
            "start", "end", "duration", "gap_from_prev",
            "word", "confidence", "low_confidence",
            "speaker_role", "segment_text",
            "flagged_categories", "human_verified",
        ])
        row = 0
        for seg in segments:
            role = infer_role(seg["text"])
            cats = _match_categories(seg["text"])
            words = seg.get("words") or []
            if not words:
                # synthesise a single-row segment entry
                start = float(seg["start"])
                end = float(seg["end"])
                row += 1
                w.writerow([
                    row, seg.get("index", 0), 0,
                    f"{start:.3f}", f"{end:.3f}",
                    f"{end - start:.3f}", f"{start - prev_end:.3f}",
                    seg["text"], "", "",
                    role, seg["text"],
                    ";".join(cats), "",
                ])
                prev_end = end
                continue
            for wi, wd in enumerate(words):
                start = float(wd.get("start", seg["start"]))
                end = float(wd.get("end", seg["end"]))
                conf = float(wd.get("probability", 0) or 0)
                row += 1
                w.writerow([
                    row, seg.get("index", 0), wi,
                    f"{start:.3f}", f"{end:.3f}",
                    f"{max(0.0, end - start):.3f}",
                    f"{start - prev_end:.3f}",
                    (wd.get("text") or "").strip(),
                    f"{conf:.3f}" if conf else "",
                    "yes" if conf and conf < low_conf_threshold else "",
                    role, seg["text"],
                    ";".join(cats), "",
                ])
                prev_end = end
    return dest


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--transcript", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--low-conf-threshold", type=float, default=0.5)
    args = p.parse_args()
    build(Path(args.transcript), Path(args.output), args.low_conf_threshold)
    print(f"Word review written to {args.output}")
