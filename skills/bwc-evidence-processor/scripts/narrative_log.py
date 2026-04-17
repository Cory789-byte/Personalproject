"""Forensic narrative log.

Produces NARRATIVE_LOG.md - a readable, counsel-style storyboard that
synthesises every artefact into a single prose document. The layout is
deliberately non-tabular: what happened, who was there, who said what,
what does not add up.

Sections:

  1. Dramatis personae            officer per exhibit (from filename),
                                  subjects inferred across transcripts
  2. Unified chronological feed   every utterance across all exhibits,
                                  sorted by absolute time (creation_time
                                  + offset), with exhibit + timestamp
                                  breadcrumbs
  3. Per-exhibit scene notes      short narrative per exhibit: who
                                  wore the camera, what happened, the
                                  key utterances, the flagged concerns
  4. Narrative contradictions     same event across multiple exhibits
                                  and statements, rendered side by side
  5. Integrity / tampering        audible "turn off" mentions, scene
                                  cuts, freeze / black intervals,
                                  creation-time gaps, SHA mismatches,
                                  anomaly flags
  6. Police decision-making       competency findings in prose form,
                                  grouped by kind and exhibit
  7. Gaps and missing procedures  compliance CRITICAL / HIGH flags as
                                  prose, plus coverage gaps

All output is MACHINE-GENERATED - UNVERIFIED. Counsel must verify
every item against the footage and the signed statements before use.
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable


HEADER = "MACHINE-GENERATED - UNVERIFIED"

OFFICER_SURNAMES = re.compile(
    r"(?:Exhibit[_\s]?#?\d+[_\s-]*)?"
    r"(?P<name>[A-Z][A-Z]{3,}(?:[-' ][A-Z]{2,})?)"
    r"[_\s]*(?:BWCF?|BWC|_)",
)


def _read_csv(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if text and text[0].startswith("#"):
        text = text[1:]
    return list(csv.DictReader(text))


def _load_json(path: Path) -> dict | None:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return None


def _officer_from_exhibit(stem: str) -> str:
    m = OFFICER_SURNAMES.search(stem.replace(".", "_"))
    if m:
        return m.group("name").title()
    # Fallback: look for ALLCAPS tokens 4+ letters
    caps = re.findall(r"\b([A-Z]{4,})\b", stem)
    if caps:
        return caps[0].title()
    return "(unidentified)"


def _parse_creation(ts: str) -> datetime | None:
    if not ts:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ",
                "%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%d %H:%M:%S"):
        try:
            dt = datetime.strptime(ts.strip(), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except Exception:
            continue
    return None


def _fmt_dt(dt: datetime | None) -> str:
    if dt is None:
        return "unknown"
    return dt.strftime("%Y-%m-%d %H:%M:%S %Z").strip()


def _hms(s: float) -> str:
    s = int(s)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def _clip(text: str, n: int = 240) -> str:
    text = (text or "").strip().replace("\n", " ")
    return text if len(text) <= n else text[: n - 1] + "..."


def _load_transcripts(output_dir: Path) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for p in sorted(output_dir.glob("*.transcript.json")):
        data = _load_json(p)
        if data is None:
            continue
        stem = p.stem.removesuffix(".transcript")
        out[stem] = data.get("segments", []) or []
    return out


def _load_integrity(output_dir: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for p in sorted(output_dir.glob("*.integrity.json")):
        d = _load_json(p)
        if d is None:
            continue
        out[p.stem.removesuffix(".integrity")] = d
    return out


def _load_bias(output_dir: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for p in sorted(output_dir.glob("*.bias_summary.json")):
        d = _load_json(p) or {}
        out[p.stem.removesuffix(".bias_summary")] = d
    return out


def _extract_subjects(transcripts: dict[str, list[dict]],
                      docs_text: dict[str, str]) -> list[str]:
    names: set[str] = set()
    for text in docs_text.values():
        for m in re.finditer(
            r"\bMr\.?\s+([A-Z][a-z]+)\b|\bMs\.?\s+([A-Z][a-z]+)\b|"
            r"\bMrs\.?\s+([A-Z][a-z]+)\b",
            text,
        ):
            for g in m.groups():
                if g:
                    names.add(g)
        for m in re.finditer(r"\b([A-Z][A-Z]{3,})\b", text):
            names.add(m.group(1).title())
    for segs in transcripts.values():
        for s in segs:
            for m in re.finditer(r"\bMr\.?\s+([A-Z][a-z]+)\b", s.get("text", "")):
                names.add(m.group(1))
    return sorted(names)


def _load_docs(output_dir: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    docs_dir = output_dir / "documents"
    if not docs_dir.is_dir():
        return out
    for p in sorted(docs_dir.glob("*.doc.json")):
        d = _load_json(p) or {}
        out[d.get("stem", p.stem)] = d.get("text", "") or ""
    return out


# --------- Section builders ----------------------------------------------


TURNOFF_CUES = [
    "turn this off", "turn the camera off", "stop the recording",
    "pause the camera", "camera's off", "off the record",
    "turn it off", "shut it off",
]


def _collect_cut_events(
    transcripts: dict[str, list[dict]],
    integrity: dict[str, dict],
) -> dict:
    """Gather every cut / black / freeze / turnoff signal across exhibits."""
    cuts_per_exhibit: dict[str, int] = {}
    black_per_exhibit: dict[str, int] = {}
    freeze_per_exhibit: dict[str, int] = {}
    turnoff_per_exhibit: dict[str, int] = defaultdict(int)
    turnoff_rows: list[dict] = []
    per_cut_context: dict[str, list[dict]] = defaultdict(list)

    for stem, integ in integrity.items():
        cuts = integ.get("scene_cuts") or []
        blacks = integ.get("black_frames") or []
        freezes = integ.get("freeze_frames") or []
        cuts_per_exhibit[stem] = len(cuts)
        black_per_exhibit[stem] = len(blacks)
        freeze_per_exhibit[stem] = len(freezes)
        segs = transcripts.get(stem, [])
        for t in cuts:
            before = next((s for s in reversed(segs)
                           if float(s.get("end", 0)) <= t), None)
            after = next((s for s in segs
                          if float(s.get("start", 0)) >= t), None)
            per_cut_context[stem].append({
                "at": float(t),
                "before": before.get("text", "") if before else "",
                "before_time": float(before.get("end", 0)) if before else None,
                "after": after.get("text", "") if after else "",
                "after_time": float(after.get("start", 0)) if after else None,
            })

    for stem, segs in transcripts.items():
        for s in segs:
            lt = (s.get("text") or "").lower()
            for cue in TURNOFF_CUES:
                if cue in lt:
                    turnoff_per_exhibit[stem] += 1
                    turnoff_rows.append({
                        "exhibit": stem, "at": float(s.get("start", 0)),
                        "text": s.get("text", ""), "cue": cue,
                    })
                    break

    dated: list[tuple[datetime, str]] = []
    for stem, integ in integrity.items():
        tags = (integ.get("format") or {}).get("tags") or {}
        dt = _parse_creation(tags.get("creation_time", ""))
        if dt:
            dated.append((dt, stem))
    dated.sort()
    creation_gaps: list[dict] = []
    for (a_dt, a), (b_dt, b) in zip(dated, dated[1:]):
        delta_s = int((b_dt - a_dt).total_seconds())
        if delta_s > 1800 and a_dt.date() == b_dt.date():
            creation_gaps.append({
                "from": a, "to": b, "from_dt": a_dt, "to_dt": b_dt,
                "gap_minutes": delta_s // 60,
            })

    return {
        "cuts_per_exhibit": cuts_per_exhibit,
        "black_per_exhibit": black_per_exhibit,
        "freeze_per_exhibit": freeze_per_exhibit,
        "turnoff_per_exhibit": dict(turnoff_per_exhibit),
        "turnoff_rows": turnoff_rows,
        "per_cut_context": dict(per_cut_context),
        "creation_gaps": creation_gaps,
        "total_cuts": sum(cuts_per_exhibit.values()),
        "total_black": sum(black_per_exhibit.values()),
        "total_freeze": sum(freeze_per_exhibit.values()),
        "total_turnoff": sum(turnoff_per_exhibit.values()),
    }


def _section_top_summary(cut_events: dict) -> list[str]:
    lines: list[str] = [
        "## 0. BWC integrity summary (top-line)",
        "",
        "| Metric | Count |",
        "|--------|-------|",
        f"| Total scene cuts across all exhibits | **{cut_events['total_cuts']}** |",
        f"| Total black-frame intervals | **{cut_events['total_black']}** |",
        f"| Total freeze-frame intervals | **{cut_events['total_freeze']}** |",
        f"| Audible camera-off / stop-recording mentions | **{cut_events['total_turnoff']}** |",
        f"| Creation-time gaps > 30 min same day | **{len(cut_events['creation_gaps'])}** |",
        "",
    ]
    # Rank exhibits by cut count
    ranked = sorted(cut_events["cuts_per_exhibit"].items(),
                    key=lambda kv: -kv[1])
    top = [r for r in ranked if r[1] > 0][:10]
    if top:
        lines.append("### Most-cut exhibits (scene cuts)")
        lines.append("")
        lines.append("| Exhibit | Scene cuts | Black | Freeze | Turn-off mentions |")
        lines.append("|---------|-----------:|------:|-------:|------------------:|")
        for ex, n in top:
            lines.append(
                f"| `{ex}` | {n} | "
                f"{cut_events['black_per_exhibit'].get(ex, 0)} | "
                f"{cut_events['freeze_per_exhibit'].get(ex, 0)} | "
                f"{cut_events['turnoff_per_exhibit'].get(ex, 0)} |"
            )
        lines.append("")
    if cut_events["turnoff_rows"]:
        lines.append("### Every audible camera-off / stop-recording mention")
        lines.append("")
        for r in cut_events["turnoff_rows"][:30]:
            lines.append(
                f"- `{r['exhibit']}` at {_hms(r['at'])}: _\"{_clip(r['text'], 200)}\"_"
            )
        if len(cut_events["turnoff_rows"]) > 30:
            lines.append(f"- ... {len(cut_events['turnoff_rows']) - 30} more")
        lines.append("")
    if cut_events["creation_gaps"]:
        lines.append("### Creation-time gaps same day, > 30 min")
        lines.append("")
        for g in cut_events["creation_gaps"]:
            lines.append(
                f"- **{g['gap_minutes']} min** gap between `{g['from']}` "
                f"({_fmt_dt(g['from_dt'])}) and `{g['to']}` ({_fmt_dt(g['to_dt'])})"
            )
        lines.append("")
    return lines


def _section_personae(
    transcripts: dict[str, list[dict]],
    integrity: dict[str, dict],
    docs_text: dict[str, str],
) -> list[str]:
    lines: list[str] = ["## 1. Dramatis personae", ""]
    officer_to_exhibits: dict[str, list[str]] = defaultdict(list)
    for stem in transcripts:
        officer_to_exhibits[_officer_from_exhibit(stem)].append(stem)
    lines.append("### Officers (camera wearer inferred from filename)")
    lines.append("")
    for officer in sorted(officer_to_exhibits):
        lines.append(f"- **{officer}**")
        for ex in officer_to_exhibits[officer]:
            integ = integrity.get(ex, {})
            creation = ((integ.get("format") or {}).get("tags") or {}).get("creation_time", "")
            dt = _parse_creation(creation)
            lines.append(f"  - `{ex}` - {_fmt_dt(dt)}")
    lines.append("")
    subjects = _extract_subjects(transcripts, docs_text)
    lines.append("### Named parties across the corpus")
    lines.append("")
    if subjects:
        for s in subjects:
            lines.append(f"- {s}")
    else:
        lines.append("_none extracted._")
    lines.append("")
    return lines


def _section_chronology(
    transcripts: dict[str, list[dict]],
    integrity: dict[str, dict],
) -> list[str]:
    lines: list[str] = [
        "## 2. Unified chronological feed",
        "",
        "_Every transcript segment across all processed exhibits, sorted by "
        "absolute time (BWC creation_time + offset). No cap - this is the "
        "canonical time log. Exhibits without creation_time are appended at "
        "the end with relative offsets only._",
        "",
    ]
    events: list[tuple[datetime | None, str, float, float, str]] = []
    for stem, segs in transcripts.items():
        integ = integrity.get(stem, {})
        creation = ((integ.get("format") or {}).get("tags") or {}).get("creation_time", "")
        base = _parse_creation(creation)
        for s in segs:
            start = float(s.get("start", 0))
            end = float(s.get("end", 0))
            dt = base + timedelta(seconds=start) if base else None
            events.append((dt, stem, start, end, (s.get("text") or "").strip()))
    events.sort(key=lambda e: (e[0] is None, e[0] or datetime.min.replace(tzinfo=timezone.utc),
                               e[1], e[2]))

    current_scene = None
    for dt, stem, start, end, text in events:
        if stem != current_scene:
            current_scene = stem
            lines.append("")
            lines.append(f"### {stem}  (start {_fmt_dt(dt)})")
            lines.append("")
        if dt is not None:
            stamp = f"{dt.strftime('%H:%M:%S')} (+{_hms(start)})"
        else:
            stamp = f"+{_hms(start)}"
        lines.append(f"- `{stamp}` - `{_hms(end)}` {_clip(text, 300)}")
    lines.append("")
    return lines


def _section_per_cut_context(cut_events: dict) -> list[str]:
    lines: list[str] = [
        "## 2b. Per-cut context (what was said around each BWC scene cut)",
        "",
        "_Every detected scene cut with the last utterance before it and the "
        "first utterance after it. Sudden subject changes or cuts in the "
        "middle of a sentence are worth scrutiny._",
        "",
    ]
    per_cut = cut_events.get("per_cut_context", {}) or {}
    if not any(per_cut.values()):
        lines.append("_No scene cuts detected across processed exhibits._")
        lines.append("")
        return lines
    for stem, cuts in per_cut.items():
        if not cuts:
            continue
        lines.append(f"### {stem}  ({len(cuts)} cut{'s' if len(cuts) != 1 else ''})")
        lines.append("")
        for c in cuts:
            at = _hms(c["at"])
            before = _clip(c["before"], 160) if c["before"] else "_(no prior utterance within scene)_"
            after = _clip(c["after"], 160) if c["after"] else "_(no subsequent utterance)_"
            before_t = _hms(c["before_time"]) if c["before_time"] is not None else "-"
            after_t = _hms(c["after_time"]) if c["after_time"] is not None else "-"
            lines.append(f"- **Cut at {at}**")
            lines.append(f"  - Before ({before_t}): _\"{before}\"_")
            lines.append(f"  - After  ({after_t}): _\"{after}\"_")
        lines.append("")
    return lines


def _section_per_exhibit(
    transcripts: dict[str, list[dict]],
    integrity: dict[str, dict],
    bias_summaries: dict[str, dict],
    output_dir: Path,
) -> list[str]:
    lines: list[str] = ["## 3. Per-exhibit scene notes", ""]
    for stem in sorted(transcripts):
        segs = transcripts[stem]
        integ = integrity.get(stem, {})
        bias = bias_summaries.get(stem, {})
        summary = (bias.get("summary") or {}) if bias else {}
        interruptions = (bias.get("interruptions") or []) if bias else []
        creation = ((integ.get("format") or {}).get("tags") or {}).get("creation_time", "")
        duration = ((integ.get("format") or {}).get("duration") or "")
        sha = integ.get("sha256", "")
        officer = _officer_from_exhibit(stem)

        compliance = _read_csv(output_dir / f"{stem}.compliance.csv")
        crit_high = [r for r in compliance if r.get("severity") in ("critical", "high")]

        lines.append(f"### {stem}")
        lines.append("")
        lines.append(f"- **Camera wearer (inferred)**: {officer}")
        lines.append(f"- **Recorded**: {_fmt_dt(_parse_creation(creation))}")
        lines.append(f"- **Duration (container)**: {duration} s")
        lines.append(f"- **SHA-256**: `{sha[:16]}...`" if sha else "- **SHA-256**: _missing_")
        lines.append(f"- **Transcript segments**: {len(segs)}")
        if summary:
            lines.append(
                f"- **Talk time**: officer {summary.get('officer_talk_seconds', 0)}s, "
                f"subject {summary.get('subject_talk_seconds', 0)}s; "
                f"officer question ratio {summary.get('officer_question_ratio', 0)}"
            )
        if interruptions:
            lines.append(f"- **Interruptions detected**: {len(interruptions)}")
        if crit_high:
            lines.append(f"- **Compliance flags**: {len(crit_high)} critical/high "
                         "(see .compliance.csv)")
        lines.append("")
        # Short narrative: first utterance, last utterance, one arrest line, one caution line.
        first = segs[0]["text"] if segs else ""
        last = segs[-1]["text"] if segs else ""
        arrest = next((s["text"] for s in segs
                       if "under arrest" in s["text"].lower()
                       or "arresting" in s["text"].lower()), "")
        caution = next((s["text"] for s in segs
                        if "anything you do say" in s["text"].lower()
                        or "you do not have to say" in s["text"].lower()), "")
        lines.append("**Narrative sample:**")
        lines.append("")
        if first:
            lines.append(f"- Opens: _\"{_clip(first, 200)}\"_")
        if arrest:
            lines.append(f"- Arrest language: _\"{_clip(arrest, 200)}\"_")
        else:
            lines.append("- Arrest language: _not detected in transcript_")
        if caution:
            lines.append(f"- Caution language: _\"{_clip(caution, 200)}\"_")
        else:
            lines.append("- Caution language: _not detected in transcript_")
        if last:
            lines.append(f"- Closes: _\"{_clip(last, 200)}\"_")
        lines.append("")
    return lines


def _section_contradictions(output_dir: Path) -> list[str]:
    lines: list[str] = ["## 4. Narrative contradictions", ""]
    rows = _read_csv(output_dir / "DEEP_CONTRADICTIONS.csv")
    if not rows:
        lines.append("_No deep contradictions register found - run the pipeline first._")
        lines.append("")
        return lines
    by_kind: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_kind[r.get("kind", "")].append(r)
    for kind in ("DATE_MISMATCH", "IDENTITY_VARIANT",
                 "PROCEDURAL_CLAIM_UNSUPPORTED", "SEQUENCE_MISMATCH"):
        items = by_kind.get(kind) or []
        if not items:
            continue
        lines.append(f"### {kind}  ({len(items)})")
        lines.append("")
        for r in items[:30]:
            lines.append(
                f"- **{r.get('severity', '').upper()}** in `{r.get('source', '')}`"
                + (f" re `{r.get('related_exhibit', '')}`"
                   if r.get("related_exhibit") else "")
                + f": {r.get('detail', '')}"
            )
            if r.get("evidence"):
                lines.append(f"  - Statement/text: _\"{_clip(r['evidence'])}\"_")
            if r.get("counter_evidence"):
                lines.append(f"  - Counter: _\"{_clip(r['counter_evidence'])}\"_")
        lines.append("")
    return lines


def _section_integrity(
    transcripts: dict[str, list[dict]],
    integrity: dict[str, dict],
    output_dir: Path,
) -> list[str]:
    lines: list[str] = ["## 5. Integrity and tampering concerns", ""]
    anomalies_total = 0
    # Explicit camera-off mentions in transcripts
    turnoff_cues = [
        "turn this off", "turn the camera off", "stop the recording",
        "pause the camera", "camera's off", "off the record",
    ]
    lines.append("### Audible camera-off mentions")
    lines.append("")
    any_turnoff = False
    for stem, segs in transcripts.items():
        for s in segs:
            lt = (s.get("text") or "").lower()
            if any(cue in lt for cue in turnoff_cues):
                lines.append(
                    f"- `{stem}` at {_hms(float(s.get('start', 0)))}: "
                    f"_\"{_clip(s.get('text', ''))}\"_"
                )
                any_turnoff = True
                anomalies_total += 1
    if not any_turnoff:
        lines.append("_None detected._")
    lines.append("")

    # Footage artefacts
    lines.append("### Scene cuts / black / freeze intervals")
    lines.append("")
    for stem, integ in sorted(integrity.items()):
        cuts = integ.get("scene_cuts") or []
        blacks = integ.get("black_frames") or []
        freezes = integ.get("freeze_frames") or []
        if cuts or blacks or freezes:
            lines.append(
                f"- `{stem}`: cuts={len(cuts)}, black={len(blacks)}, freeze={len(freezes)}"
            )
            anomalies_total += len(cuts) + len(blacks) + len(freezes)
    if anomalies_total == 0:
        lines.append("_None recorded._")
    lines.append("")

    # Anomaly flags from integrity
    lines.append("### Container / encoder anomaly flags")
    lines.append("")
    found_anom = False
    for stem, integ in sorted(integrity.items()):
        for a in integ.get("anomalies") or []:
            lines.append(f"- `{stem}`: {a}")
            found_anom = True
    if not found_anom:
        lines.append("_None recorded._")
    lines.append("")

    # Creation-time gaps across consecutive exhibits that describe the same incident
    lines.append("### Creation-time gaps between consecutive exhibits")
    lines.append("")
    dated: list[tuple[datetime, str]] = []
    for stem, integ in integrity.items():
        tags = (integ.get("format") or {}).get("tags") or {}
        dt = _parse_creation(tags.get("creation_time", ""))
        if dt:
            dated.append((dt, stem))
    dated.sort()
    for (a_dt, a), (b_dt, b) in zip(dated, dated[1:]):
        delta = b_dt - a_dt
        # Flag only if same day and > 30 min gap
        if delta.total_seconds() > 1800 and a_dt.date() == b_dt.date():
            lines.append(
                f"- Gap of {int(delta.total_seconds() / 60)} min between "
                f"`{a}` ({_fmt_dt(a_dt)}) and `{b}` ({_fmt_dt(b_dt)})"
            )
    lines.append("")

    # Chain-of-custody from validation report
    val_csv = output_dir / "VALIDATION_REPORT.csv"
    if val_csv.is_file():
        lines.append("### Chain-of-custody status (from VALIDATION_REPORT)")
        lines.append("")
        rows = _read_csv(val_csv)
        custody = [r for r in rows if r.get("target") == "chain_of_custody"]
        if custody:
            for r in custody:
                lines.append(
                    f"- `{r.get('exhibit', '<matter>')}`: {r.get('status', '')} - "
                    f"{r.get('detail', '')}"
                )
        else:
            lines.append("_No chain_of_custody rows in validation report._")
        lines.append("")
    return lines


def _section_decision_making(output_dir: Path) -> list[str]:
    lines: list[str] = ["## 6. Police decision-making concerns", ""]
    rows = _read_csv(output_dir / "COMPETENCY_FINDINGS.csv")
    if not rows:
        lines.append("_No competency findings register found - run the pipeline first._")
        lines.append("")
        return lines
    by_kind: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_kind[r.get("kind", "")].append(r)
    descriptions = {
        "BWC_COMPLIANCE_GAP": "Footage interruptions / camera-off indicators",
        "RUSH_TO_JUDGMENT": "Presumption of guilt before investigation complete",
        "ESCALATION_FAILURE": "Aggressive tone at compliant subject",
        "IDENTITY_MIX_UP": "Officer references wrong name for subject",
        "MENTAL_HEALTH_UNCONSIDERED": "Distress signals without welfare response",
        "CHARGE_CONFUSION": "Officer unsure / changes charge",
        "DV_HANDLING_FAILURE": "DV context handled without DVLO / safety plan",
        "CONTRADICTORY_OFFICERS": "Different officers cite different offences",
        "IGNORED_EXCULPATION": "Subject offered explanation, officer did not engage",
        "SUPERVISOR_ABSENT": "Significant decision without supervisor consultation",
        "UNCERTAINTY": "Officer hedging / pausing to look up procedure",
    }
    for kind in ["BWC_COMPLIANCE_GAP", "RUSH_TO_JUDGMENT", "ESCALATION_FAILURE",
                 "IDENTITY_MIX_UP", "MENTAL_HEALTH_UNCONSIDERED",
                 "CHARGE_CONFUSION", "DV_HANDLING_FAILURE",
                 "CONTRADICTORY_OFFICERS", "IGNORED_EXCULPATION",
                 "SUPERVISOR_ABSENT", "UNCERTAINTY"]:
        items = by_kind.get(kind) or []
        if not items:
            continue
        lines.append(f"### {kind}  ({len(items)})")
        lines.append(f"_{descriptions.get(kind, '')}_")
        lines.append("")
        for r in items[:12]:
            utt = r.get("utterance", "")
            ex = r.get("exhibit", "")
            ts = r.get("timestamp", "")
            detail = r.get("detail", "")
            lines.append(f"- `{ex}` at {ts}: {detail}")
            if utt:
                lines.append(f"  - _\"{_clip(utt, 200)}\"_")
        if len(items) > 12:
            lines.append(f"- ... {len(items) - 12} more in COMPETENCY_FINDINGS.csv")
        lines.append("")
    return lines


def _section_gaps(output_dir: Path, transcripts: dict[str, list[dict]]) -> list[str]:
    lines: list[str] = ["## 7. Gaps and missing procedures", ""]
    # Aggregate compliance CRITICAL / HIGH
    all_rows: list[dict] = []
    for p in sorted(output_dir.glob("*.compliance.csv")):
        exhibit = p.stem.removesuffix(".compliance")
        for r in _read_csv(p):
            r["_exhibit"] = exhibit
            all_rows.append(r)
    crit_high = [r for r in all_rows if r.get("severity") in ("critical", "high")]
    if not crit_high:
        lines.append("_No critical or high compliance flags recorded._")
        lines.append("")
    else:
        by_cat: dict[str, list[dict]] = defaultdict(list)
        for r in crit_high:
            by_cat[r.get("category", "")].append(r)
        for cat, items in sorted(by_cat.items(), key=lambda kv: -len(kv[1])):
            lines.append(f"### {cat}  ({len(items)})")
            lines.append("")
            for r in items[:10]:
                lines.append(
                    f"- `{r.get('_exhibit', '')}` at "
                    f"{r.get('timestamp_hms', '')}: {r.get('detail', '')}"
                )
            if len(items) > 10:
                lines.append(f"- ... {len(items) - 10} more")
            lines.append("")

    # Coverage gaps
    val_md = output_dir / "VALIDATION_REPORT.md"
    if val_md.is_file():
        lines.append("### Coverage gaps")
        lines.append("")
        lines.append("_See `VALIDATION_REPORT.md` for exhibit-level coverage and any source media not yet processed._")
        lines.append("")
    return lines


# --------- Orchestration -------------------------------------------------


def build(matter_root: Path) -> Path:
    matter_root = Path(matter_root).resolve()
    output_dir = matter_root / "output"
    transcripts = _load_transcripts(output_dir)
    integrity = _load_integrity(output_dir)
    bias = _load_bias(output_dir)
    docs_text = _load_docs(output_dir)

    cut_events = _collect_cut_events(transcripts, integrity)

    lines: list[str] = [
        "# Forensic Narrative Log",
        "",
        f"> **{HEADER}**  -  Matter: `{matter_root}`",
        "> A single counsel-style storyboard synthesising every artefact.",
        "> Every item must be verified against the footage and sworn",
        "> statements before any forensic or tactical use.",
        "",
    ]
    lines += _section_top_summary(cut_events)
    lines += _section_personae(transcripts, integrity, docs_text)
    lines += _section_chronology(transcripts, integrity)
    lines += _section_per_cut_context(cut_events)
    lines += _section_per_exhibit(transcripts, integrity, bias, output_dir)
    lines += _section_contradictions(output_dir)
    lines += _section_integrity(transcripts, integrity, output_dir)
    lines += _section_decision_making(output_dir)
    lines += _section_gaps(output_dir, transcripts)
    lines += [
        "",
        "---",
        "",
        "### Verification checklist",
        "",
        "- [ ] Every quoted utterance re-listened-to against the footage",
        "- [ ] Every person named confirmed against disclosed briefs",
        "- [ ] Every creation-time / chain-of-custody flag investigated",
        "- [ ] Every narrative contradiction reviewed with counsel notes",
        "- [ ] Every competency finding triaged: real vs false positive",
        "- [ ] All gaps chased: is the missing procedure captured in footage",
        "      not yet processed, or genuinely absent?",
        "",
    ]

    dest = output_dir / "NARRATIVE_LOG.md"
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return dest


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--matter-root", required=True)
    args = ap.parse_args()
    p = build(Path(args.matter_root))
    print(f"Narrative log written: {p}")
