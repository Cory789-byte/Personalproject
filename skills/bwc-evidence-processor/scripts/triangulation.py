"""Cross-officer / statement / BWC triangulation.

Binds three sources of truth into one matrix per key event:

  - Officer statements (PDF docs under output/documents/*.doc.json)
  - BWC transcripts      (*.transcript.json)
  - BWC integrity data   (*.integrity.json - creation_time, cuts, etc.)

For each predefined event-type (arrival, arrest, caution, search,
seizure, document handover, departure, interview) the analyzer:

  1. Finds every mention in every source with surrounding context.
  2. Extracts the date / time near each mention where possible.
  3. Emits a cross-source comparison so disagreements are visible
     at a glance: officer A says 0806, officer B says 0820, BWC
     says 0813 - a 14-minute spread.

Then it produces a tampering tally per officer camera:
  scene_cuts + black + freeze + audible_turn_off + creation_gaps
  = tampering_score.

Outputs:

  TRIANGULATION.md              - readable per-event matrix
  TRIANGULATION.csv             - one row per (event, source) tuple
  TAMPERING_TALLY.md            - per-camera tampering tally
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path


HEADER = "MACHINE-GENERATED - UNVERIFIED"


EVENT_PATTERNS: dict[str, list[str]] = {
    "arrival": [
        "arrived at", "attended the", "attended to", "upon arrival",
        "we arrived", "i arrived", "got to the", "made my way",
        "knocked on", "at the front door", "approached the",
    ],
    "arrest": [
        "under arrest", "arresting", "placed under arrest",
        "taken into custody", "arrested for", "i arrested",
        "the arrest", "placed the accused under",
    ],
    "caution": [
        "cautioned", "i cautioned", "issued the caution",
        "you do not have to say anything", "anything you do say",
        "right to silence", "caution was given",
    ],
    "search": [
        "searched", "i searched", "we searched", "conducted a search",
        "patted down", "pat down", "searched the vehicle",
        "searched the bag", "searched the property",
    ],
    "dog_seizure": [
        "seized the dog", "seizure of the dog", "seizing the dog",
        "removed the dog", "took the dog", "dog was seized",
        "the dog", "romeo",
    ],
    "document_handover": [
        "handed me", "tom handed", "tom gave", "gave me",
        "provided documents", "provided the documents",
        "produced documents", "documents were produced",
        "handed over",
    ],
    "departure": [
        "we left", "i left", "left the scene", "departed",
        "returned to the station", "transported", "cleared the",
        "left the property",
    ],
    "interview": [
        "interviewed", "conducted an interview", "record of interview",
        "ROI", "interview with", "interviewed the accused",
        "questioned", "spoke to him at the station",
    ],
    "rights_to_counsel": [
        "right to a lawyer", "right to contact a",
        "contact a friend or relative", "advised of rights",
        "right to legal", "offered to contact",
    ],
}


TIME_RE = re.compile(
    r"\b(?:at|around|about|approximately)?\s*"
    r"(?P<h>\d{1,2})[:\.h](?P<m>[0-5]\d)"
    r"\s*(?P<mer>am|pm|hours|hrs)?\b",
    re.IGNORECASE,
)
MILITARY_RE = re.compile(r"\b(?P<hhmm>[01]\d[0-5]\d|2[0-3][0-5]\d)\s*(?:hrs|hours)?\b")
DATE_RE = re.compile(
    r"\b(\d{1,2})[/\-\.](\d{1,2})[/\-\.](\d{2,4})\b"
    r"|\b(\d{1,2})\s+"
    r"(january|february|march|april|may|june|july|august|september|"
    r"october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)"
    r"\s+(\d{4})\b",
    re.IGNORECASE,
)

OFFICER_RE = re.compile(
    r"\b(?:SC|Snr\s*Const|Senior\s*Constable|Sgt|Sergeant|Const|Constable|"
    r"Detective|Det|PO|Inspector|Insp)\s+([A-Z][A-Z]{2,}(?:[-'\s][A-Z][A-Z]+)?)\b"
)


@dataclass
class Mention:
    source: str
    source_kind: str  # "doc" | "transcript"
    event: str
    text: str
    context: str
    time_str: str = ""
    date_str: str = ""


@dataclass
class CameraTally:
    exhibit: str
    officer_guess: str
    scene_cuts: int = 0
    black_intervals: int = 0
    freeze_intervals: int = 0
    turn_off_mentions: int = 0
    creation_gap_events: int = 0
    anomaly_flags: int = 0

    @property
    def score(self) -> int:
        return (
            self.scene_cuts + 2 * self.black_intervals + 2 * self.freeze_intervals
            + 3 * self.turn_off_mentions + self.creation_gap_events
            + self.anomaly_flags
        )


# ---- Loaders ------------------------------------------------------------


def _load_json(p: Path) -> dict | None:
    if not p.is_file():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return None


def _load_docs(output_dir: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    docs_dir = output_dir / "documents"
    if not docs_dir.is_dir():
        return out
    for p in sorted(docs_dir.glob("*.doc.json")):
        d = _load_json(p) or {}
        out[d.get("stem", p.stem)] = d.get("text", "") or ""
    return out


def _load_transcripts(output_dir: Path) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for p in sorted(output_dir.glob("*.transcript.json")):
        d = _load_json(p) or {}
        stem = p.stem.removesuffix(".transcript")
        out[stem] = d.get("segments", []) or []
    return out


def _load_integrity(output_dir: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for p in sorted(output_dir.glob("*.integrity.json")):
        d = _load_json(p) or {}
        out[p.stem.removesuffix(".integrity")] = d
    return out


# ---- Event extraction --------------------------------------------------


def _scan_text(text: str, source: str, source_kind: str) -> list[Mention]:
    mentions: list[Mention] = []
    lt = text.lower()
    for event, patterns in EVENT_PATTERNS.items():
        for pat in patterns:
            idx = lt.find(pat)
            if idx < 0:
                continue
            ctx_start = max(0, idx - 80)
            ctx_end = min(len(text), idx + len(pat) + 140)
            ctx = text[ctx_start:ctx_end].replace("\n", " ").strip()
            time_str = ""
            date_str = ""
            m = TIME_RE.search(ctx)
            if m:
                time_str = m.group(0)
            m = MILITARY_RE.search(ctx)
            if m and not time_str:
                time_str = m.group(0)
            m = DATE_RE.search(ctx)
            if m:
                date_str = m.group(0)
            mentions.append(Mention(
                source=source, source_kind=source_kind, event=event,
                text=pat, context=ctx, time_str=time_str, date_str=date_str,
            ))
            break  # first hit per event per source
    return mentions


def _scan_transcript(stem: str, segments: list[dict]) -> list[Mention]:
    joined = " ".join(
        f"[{int(s.get('start', 0))}s] {s.get('text', '')}"
        for s in segments
    )
    return _scan_text(joined, stem, "transcript")


def _scan_doc(stem: str, text: str) -> list[Mention]:
    return _scan_text(text, stem, "doc")


# ---- Tampering tally ----------------------------------------------------


TURNOFF_CUES = [
    "turn this off", "turn the camera off", "stop the recording",
    "pause the camera", "camera's off", "off the record",
    "turn it off", "shut it off",
]


def _parse_creation(ts: str) -> datetime | None:
    if not ts:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ",
                "%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            dt = datetime.strptime(ts.strip(), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except Exception:
            continue
    return None


def _officer_from_stem(stem: str) -> str:
    # Look for ALLCAPS officer surname inside the stem
    m = re.search(r"\b([A-Z]{4,})\b", stem.replace(".", "_"))
    return m.group(1).title() if m else "(unidentified)"


def _tampering_tally(
    transcripts: dict[str, list[dict]],
    integrity: dict[str, dict],
) -> list[CameraTally]:
    tallies: dict[str, CameraTally] = {}
    # Sort dated exhibits for creation-gap accounting
    dated: list[tuple[datetime, str]] = []
    for stem, integ in integrity.items():
        tags = (integ.get("format") or {}).get("tags") or {}
        dt = _parse_creation(tags.get("creation_time", ""))
        if dt:
            dated.append((dt, stem))
    dated.sort()
    gap_exhibits: set[str] = set()
    for (a_dt, a), (b_dt, b) in zip(dated, dated[1:]):
        delta = (b_dt - a_dt).total_seconds()
        if delta > 1800 and a_dt.date() == b_dt.date():
            gap_exhibits.update([a, b])

    for stem, integ in integrity.items():
        t = CameraTally(
            exhibit=stem,
            officer_guess=_officer_from_stem(stem),
            scene_cuts=len(integ.get("scene_cuts") or []),
            black_intervals=len(integ.get("black_frames") or []),
            freeze_intervals=len(integ.get("freeze_frames") or []),
            anomaly_flags=len(integ.get("anomalies") or []),
        )
        segs = transcripts.get(stem, [])
        t.turn_off_mentions = sum(
            1 for s in segs
            for cue in TURNOFF_CUES
            if cue in (s.get("text") or "").lower()
        )
        if stem in gap_exhibits:
            t.creation_gap_events = 1
        tallies[stem] = t
    return list(tallies.values())


# ---- Orchestration ------------------------------------------------------


def analyze(matter_root: Path) -> dict:
    matter_root = Path(matter_root).resolve()
    output_dir = matter_root / "output"
    docs = _load_docs(output_dir)
    transcripts = _load_transcripts(output_dir)
    integrity = _load_integrity(output_dir)

    mentions: list[Mention] = []
    for stem, text in docs.items():
        mentions.extend(_scan_doc(stem, text))
    for stem, segs in transcripts.items():
        mentions.extend(_scan_transcript(stem, segs))

    tally = _tampering_tally(transcripts, integrity)
    return {
        "matter_root": str(matter_root),
        "mentions": mentions,
        "tally": tally,
        "integrity": integrity,
    }


def save(report: dict, output_dir: Path) -> tuple[Path, Path, Path]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "TRIANGULATION.csv"
    md_path = output_dir / "TRIANGULATION.md"
    tamper_md = output_dir / "TAMPERING_TALLY.md"

    mentions: list[Mention] = report["mentions"]

    # CSV: one row per mention
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# {HEADER}\n")
        w = csv.writer(f)
        w.writerow([
            "row", "event", "source_kind", "source", "time_str",
            "date_str", "matched_phrase", "context", "human_verified",
        ])
        for i, m in enumerate(mentions, 1):
            w.writerow([
                i, m.event, m.source_kind, m.source, m.time_str,
                m.date_str, m.text, m.context, "",
            ])

    # MD event matrix
    by_event: dict[str, list[Mention]] = defaultdict(list)
    for m in mentions:
        by_event[m.event].append(m)

    lines = [
        "# Triangulation - Cross-source event matrix",
        "",
        f"> **{HEADER}**  -  Matter: `{report['matter_root']}`",
        "> Every key event lined up across officer statements,",
        "> BWC transcripts, and BWC metadata. Divergences between",
        "> the accounts are the primary defence signal.",
        "",
    ]
    for event in [
        "arrival", "arrest", "caution", "rights_to_counsel",
        "search", "dog_seizure", "document_handover",
        "interview", "departure",
    ]:
        items = by_event.get(event) or []
        lines.append(f"## {event.upper()}  ({len(items)} source(s))")
        lines.append("")
        if not items:
            lines.append("_No mentions detected across any source._")
            lines.append("")
            continue
        lines.append("| Source kind | Source | Time | Date | Matched phrase | Context |")
        lines.append("|-------------|--------|------|------|---------------|---------|")
        for m in items:
            ctx = (m.context or "").replace("|", "\\|")
            if len(ctx) > 220:
                ctx = ctx[:217] + "..."
            lines.append(
                f"| {m.source_kind} | `{m.source}` | {m.time_str} | "
                f"{m.date_str} | `{m.text}` | {ctx} |"
            )
        # Detect time divergence
        times = [m.time_str for m in items if m.time_str]
        if len(set(times)) > 1:
            lines.append("")
            lines.append(
                f"⚠ **Time divergence**: {len(set(times))} distinct "
                f"time references across sources for this event."
            )
        lines.append("")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Tampering tally
    tally: list[CameraTally] = report["tally"]
    tally_sorted = sorted(tally, key=lambda t: -t.score)
    total_score = sum(t.score for t in tally)
    total_cuts = sum(t.scene_cuts for t in tally)
    total_black = sum(t.black_intervals for t in tally)
    total_freeze = sum(t.freeze_intervals for t in tally)
    total_turnoff = sum(t.turn_off_mentions for t in tally)
    total_gaps = sum(t.creation_gap_events for t in tally)
    total_anom = sum(t.anomaly_flags for t in tally)

    tlines: list[str] = [
        "# Tampering Tally - per camera",
        "",
        f"> **{HEADER}**",
        f"> Aggregate tampering score across all exhibits: **{total_score}**",
        "",
        "## Totals",
        "",
        f"- Scene cuts:               **{total_cuts}**",
        f"- Black-frame intervals:    **{total_black}**  (weight x2)",
        f"- Freeze-frame intervals:   **{total_freeze}**  (weight x2)",
        f"- Audible turn-off mentions:**{total_turnoff}**  (weight x3)",
        f"- Creation-time gaps:       **{total_gaps}**",
        f"- Container anomaly flags:  **{total_anom}**",
        "",
        "## Per camera",
        "",
        "| Officer (inferred) | Exhibit | Cuts | Black | Freeze | Turn-off | Gap | Anom | Score |",
        "|--------------------|---------|-----:|------:|-------:|---------:|----:|-----:|------:|",
    ]
    for t in tally_sorted:
        tlines.append(
            f"| {t.officer_guess} | `{t.exhibit}` | {t.scene_cuts} | "
            f"{t.black_intervals} | {t.freeze_intervals} | "
            f"{t.turn_off_mentions} | {t.creation_gap_events} | "
            f"{t.anomaly_flags} | **{t.score}** |"
        )
    tlines += [
        "",
        "_Score = cuts + 2*black + 2*freeze + 3*turn_off + gap + anomaly._",
        "_Higher = more tampering indicators to investigate. Not a legal finding._",
        "",
    ]
    tamper_md.write_text("\n".join(tlines) + "\n", encoding="utf-8")

    return csv_path, md_path, tamper_md


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--matter-root", required=True)
    args = ap.parse_args()
    rep = analyze(Path(args.matter_root))
    out = Path(args.matter_root) / "output"
    csvp, mdp, tmp = save(rep, out)
    print(f"{len(rep['mentions'])} event mentions across {len(rep['tally'])} cameras.")
    print(f"  {csvp}")
    print(f"  {mdp}")
    print(f"  {tmp}")
