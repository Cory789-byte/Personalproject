"""Keyword-driven frame extraction sweep.

Scans every processed transcript for terms that indicate visual
evidence is on-screen ("mail", "documents", "kitchen bench", "upstairs",
"front door", etc.) and extracts a frame at each hit - optionally
cropped + zoomed + OCR'd.

Use case: "the mail at the front door is visible to any officer who
walks past" - instead of manually scrubbing 20+ hours of footage, let
the tool find every "front door" / "mail" / "letter" utterance and
grab the frame at that second. Review the thumbnails, pick the one
that shows the mail, then re-run frame_extract.py with a tight crop
+ OCR to read the addressee.

Outputs:
  output/visual_sweep/<exhibit>/<keyword>_<time>.png  - extracted frame
  output/VISUAL_SWEEP_INDEX.md                        - browsable index
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _path_helper import ensure_tools_on_path  # noqa: E402

ensure_tools_on_path()


HEADER = "MACHINE-GENERATED - UNVERIFIED"

DEFAULT_KEYWORDS = {
    "residency": [
        "mail", "letter", "envelope", "addressed to",
        "my address", "my lease", "my keys", "my bedroom",
        "my room", "live here", "tenancy",
    ],
    "document_offer": [
        "these documents", "these papers", "look at this",
        "look at these", "here's the", "take a look",
        "this proves", "you can see",
    ],
    "physical_location": [
        "front door", "at the door", "doorway", "entrance",
        "kitchen", "bench", "counter", "table",
        "upstairs", "downstairs", "hallway", "lounge",
        "bedroom", "bathroom", "fridge", "sink",
    ],
    "third_party_handover": [
        "tom gave", "tom hands", "tom says", "tom has",
        "he gave me", "she gave me", "take these",
        "here's what", "these are from",
    ],
}


@dataclass
class Hit:
    exhibit: str
    category: str
    keyword: str
    start_seconds: float
    segment_text: str


def _load_transcripts(output_dir: Path) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for p in sorted(output_dir.glob("*.transcript.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        out[p.stem.removesuffix(".transcript")] = d.get("segments", []) or []
    return out


def _load_source_paths(source_dir: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    if not source_dir.is_dir():
        return out
    for p in source_dir.rglob("*"):
        if p.is_file() and p.suffix.lower() in {
            ".mp4", ".mov", ".mkv", ".avi", ".webm",
        }:
            out[p.stem] = p.resolve()
    return out


def _sweep(transcripts: dict[str, list[dict]], keyword_map: dict[str, list[str]]) -> list[Hit]:
    hits: list[Hit] = []
    for stem, segs in transcripts.items():
        for seg in segs:
            text = (seg.get("text") or "").lower()
            if not text:
                continue
            for category, kws in keyword_map.items():
                for kw in kws:
                    if re.search(r"\b" + re.escape(kw) + r"\b", text):
                        hits.append(Hit(
                            exhibit=stem,
                            category=category,
                            keyword=kw,
                            start_seconds=float(seg.get("start", 0)),
                            segment_text=seg.get("text", "").strip(),
                        ))
                        break  # one hit per segment per category
    return hits


def _safe_name(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", s)[:60]


def run(
    matter_root: Path,
    keyword_map: dict[str, list[str]] | None = None,
    limit_per_exhibit: int = 0,
    dry_run: bool = False,
) -> Path:
    matter_root = Path(matter_root).resolve()
    output_dir = matter_root / "output"
    source_dir = matter_root / "source"
    transcripts = _load_transcripts(output_dir)
    sources = _load_source_paths(source_dir)
    keywords = keyword_map or DEFAULT_KEYWORDS
    hits = _sweep(transcripts, keywords)

    per_exhibit: dict[str, list[Hit]] = {}
    for h in hits:
        per_exhibit.setdefault(h.exhibit, []).append(h)

    index_path = output_dir / "VISUAL_SWEEP_INDEX.md"
    lines: list[str] = [
        "# Visual evidence sweep",
        "",
        f"> **{HEADER}**  -  Matter: `{matter_root}`",
        f"> Keywords: {sum(len(v) for v in keywords.values())} across "
        f"{len(keywords)} categories.",
        f"> Hits: {len(hits)} across {len(per_exhibit)} exhibit(s).",
        "",
    ]

    extracted_count = 0
    for stem, stem_hits in sorted(per_exhibit.items()):
        lines.append(f"## {stem}  ({len(stem_hits)} hits)")
        lines.append("")
        video = sources.get(stem)
        hits_to_extract = (
            stem_hits if not limit_per_exhibit
            else stem_hits[:limit_per_exhibit]
        )
        dest_dir = output_dir / "visual_sweep" / _safe_name(stem)
        if video is not None:
            dest_dir.mkdir(parents=True, exist_ok=True)

        lines.append("| Time | Category | Keyword | Utterance | Frame |")
        lines.append("|------|----------|---------|-----------|-------|")
        for h in hits_to_extract:
            ts = h.start_seconds
            utter = h.segment_text.replace("|", "\\|")
            if len(utter) > 140:
                utter = utter[:137] + "..."
            if video is None:
                lines.append(
                    f"| {_hms(ts)} | {h.category} | `{h.keyword}` | "
                    f"{utter} | _(source video not found)_ |"
                )
                continue
            frame_name = f"{int(ts):06d}_{_safe_name(h.keyword)}.png"
            frame_path = dest_dir / frame_name
            frame_cell: str
            if dry_run:
                frame_cell = "_(dry run - not extracted)_"
            elif frame_path.is_file():
                rel = frame_path.relative_to(output_dir)
                frame_cell = f"[`{rel}`]({rel.as_posix()})"
            else:
                try:
                    from frame_extract import extract_frame
                    extract_frame(video, ts, frame_path)
                    extracted_count += 1
                    rel = frame_path.relative_to(output_dir)
                    frame_cell = f"[`{rel}`]({rel.as_posix()})"
                except Exception as e:
                    frame_cell = f"_extract failed: {str(e)[:80]}_"
            lines.append(
                f"| {_hms(ts)} | {h.category} | `{h.keyword}` | "
                f"{utter} | {frame_cell} |"
            )
        lines.append("")

    lines += [
        "---",
        "",
        f"Extracted {extracted_count} new frame(s) under `output/visual_sweep/`.",
        "",
        "To OCR a specific frame (e.g. to read mail addressee):",
        "",
        "```powershell",
        "python scripts\\frame_extract.py --video \"<VIDEO>\" \\",
        "    --timestamp <SECONDS> --output <OUT.png> \\",
        "    --crop X,Y,W,H --zoom 4 --ocr",
        "```",
        "",
    ]
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return index_path


def _hms(s: float) -> str:
    si = int(s)
    h, si = divmod(si, 3600)
    m, si = divmod(si, 60)
    return f"{h:02d}:{m:02d}:{si:02d}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--matter-root", required=True)
    ap.add_argument("--limit-per-exhibit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true",
                    help="Catalogue hits but don't extract frames")
    ap.add_argument("--keyword-file", default=None,
                    help="Optional JSON file: {category: [keywords...]}")
    args = ap.parse_args()
    kw_map = DEFAULT_KEYWORDS
    if args.keyword_file:
        kw_map = json.loads(Path(args.keyword_file).read_text(encoding="utf-8"))
    idx = run(Path(args.matter_root), kw_map,
              limit_per_exhibit=args.limit_per_exhibit,
              dry_run=args.dry_run)
    print(f"Index written: {idx}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
