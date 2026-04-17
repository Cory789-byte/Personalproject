"""Build an evidence matrix and contradictions register from a transcript."""

from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from rapidfuzz import fuzz


HEADER = "MACHINE-GENERATED - UNVERIFIED"
MATRIX_COLUMNS = [
    "row",
    "start",
    "end",
    "timestamp_hms",
    "speaker",
    "utterance",
    "category",
    "matched_phrase",
    "match_score",
    "annexure_ref",
    "matter_ref",
    "notes",
    "human_verified",
]
CONTRADICTION_COLUMNS = [
    "row",
    "start",
    "end",
    "transcript_utterance",
    "sworn_statement_excerpt",
    "similarity",
    "contradiction_type",
    "notes",
    "human_verified",
]


@dataclass
class KeywordBank:
    categories: dict[str, list[str]] = field(default_factory=dict)
    matter_refs: list[str] = field(default_factory=list)
    annexure_map: dict[str, str] = field(default_factory=dict)
    fuzzy_threshold: int = 85

    @classmethod
    def load(cls, path: Path | None) -> "KeywordBank":
        if path is None:
            return cls()
        data = json.loads(Path(path).read_text())
        return cls(
            categories=data.get("categories", {}),
            matter_refs=data.get("matter_refs", []),
            annexure_map=data.get("annexure_map", {}),
            fuzzy_threshold=int(data.get("fuzzy_threshold", 85)),
        )


def _hms(seconds: float) -> str:
    s = int(seconds)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def _match_phrase(utterance: str, phrase: str, threshold: int) -> int:
    if phrase.lower() in utterance.lower():
        return 100
    score = fuzz.partial_ratio(utterance.lower(), phrase.lower())
    return int(score) if score >= threshold else 0


def _find_matter_refs(utterance: str, refs: Iterable[str]) -> list[str]:
    hits = []
    for ref in refs:
        if re.search(re.escape(ref), utterance, re.IGNORECASE):
            hits.append(ref)
    return hits


def build_evidence_matrix(
    transcript_json: Path,
    bank: KeywordBank,
    dest: Path,
) -> Path:
    data = json.loads(Path(transcript_json).read_text())
    segments = data["segments"]

    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)

    rows: list[dict] = []
    row_no = 0
    for seg in segments:
        utter = seg["text"]
        seg_matched = False
        for category, phrases in bank.categories.items():
            for phrase in phrases:
                score = _match_phrase(utter, phrase, bank.fuzzy_threshold)
                if score:
                    row_no += 1
                    rows.append({
                        "row": row_no,
                        "start": f"{seg['start']:.3f}",
                        "end": f"{seg['end']:.3f}",
                        "timestamp_hms": _hms(seg["start"]),
                        "speaker": "",
                        "utterance": utter,
                        "category": category,
                        "matched_phrase": phrase,
                        "match_score": score,
                        "annexure_ref": bank.annexure_map.get(category, ""),
                        "matter_ref": ";".join(
                            _find_matter_refs(utter, bank.matter_refs)
                        ),
                        "notes": "",
                        "human_verified": "",
                    })
                    seg_matched = True
        if not seg_matched:
            matter_hits = _find_matter_refs(utter, bank.matter_refs)
            if matter_hits:
                row_no += 1
                rows.append({
                    "row": row_no,
                    "start": f"{seg['start']:.3f}",
                    "end": f"{seg['end']:.3f}",
                    "timestamp_hms": _hms(seg["start"]),
                    "speaker": "",
                    "utterance": utter,
                    "category": "matter_identifier",
                    "matched_phrase": "",
                    "match_score": 100,
                    "annexure_ref": "",
                    "matter_ref": ";".join(matter_hits),
                    "notes": "",
                    "human_verified": "",
                })

    with dest.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# {HEADER}\n")
        writer = csv.DictWriter(f, fieldnames=MATRIX_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    return dest


def build_contradictions(
    transcript_json: Path,
    sworn_corpus: Path | None,
    dest: Path,
    threshold: int = 60,
) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)

    with dest.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# {HEADER}\n")
        writer = csv.DictWriter(f, fieldnames=CONTRADICTION_COLUMNS)
        writer.writeheader()

        if sworn_corpus is None or not Path(sworn_corpus).is_file():
            return dest

        sworn_sentences = [
            s.strip() for s in re.split(
                r"(?<=[.!?])\s+", Path(sworn_corpus).read_text()
            ) if s.strip()
        ]
        data = json.loads(Path(transcript_json).read_text())
        segments = data["segments"]

        row_no = 0
        for seg in segments:
            utter = seg["text"]
            best_match = None
            best_score = 0
            for sworn in sworn_sentences:
                score = fuzz.partial_ratio(utter.lower(), sworn.lower())
                if score > best_score:
                    best_score = score
                    best_match = sworn
            if best_match and threshold <= best_score < 90:
                row_no += 1
                writer.writerow({
                    "row": row_no,
                    "start": f"{seg['start']:.3f}",
                    "end": f"{seg['end']:.3f}",
                    "transcript_utterance": utter,
                    "sworn_statement_excerpt": best_match,
                    "similarity": best_score,
                    "contradiction_type": "partial_match_divergence",
                    "notes": "",
                    "human_verified": "",
                })
    return dest


def build_viewing_log(
    transcript_json: Path,
    dest: Path,
    source_name: str,
) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    data = json.loads(Path(transcript_json).read_text())
    segments = data["segments"]

    lines = [
        f"# Forensic Viewing Log - {source_name}",
        "",
        f"> **{HEADER}** - every entry requires human verification before use.",
        "",
        "| # | Time | Utterance | Reviewer Notes | Verified |",
        "|---|------|-----------|----------------|----------|",
    ]
    for i, seg in enumerate(segments, start=1):
        safe = seg["text"].replace("|", "\\|")
        lines.append(f"| {i} | {_hms(seg['start'])} | {safe} |  |  |")
    dest.write_text("\n".join(lines) + "\n")
    return dest


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript", required=True)
    parser.add_argument("--matter-config")
    parser.add_argument("--matrix")
    parser.add_argument("--contradictions")
    parser.add_argument("--sworn-corpus")
    parser.add_argument("--viewing-log")
    parser.add_argument("--source-name", default="evidence")
    args = parser.parse_args()

    bank = KeywordBank.load(
        Path(args.matter_config) if args.matter_config else None
    )
    if args.matrix:
        build_evidence_matrix(Path(args.transcript), bank, Path(args.matrix))
    if args.contradictions:
        build_contradictions(
            Path(args.transcript),
            Path(args.sworn_corpus) if args.sworn_corpus else None,
            Path(args.contradictions),
        )
    if args.viewing_log:
        build_viewing_log(
            Path(args.transcript), Path(args.viewing_log), args.source_name
        )
