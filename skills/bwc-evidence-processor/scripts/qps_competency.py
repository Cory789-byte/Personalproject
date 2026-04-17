"""QPS officer competency and decision-making analyzer.

Scans processed transcripts + integrity reports + document corpus for
signals that go to the competency of the officers involved and the
quality of decisions made in the field. Every flag is investigative -
counsel must verify.

Categories (kind column):

  UNCERTAINTY                     officer hedging / not knowing
  RUSH_TO_JUDGMENT                presumption of guilt before investigation
  ESCALATION_FAILURE              aggressive tone when subject is compliant
  IGNORED_EXCULPATION             subject offers explanation, officer dismisses
  CHARGE_CONFUSION                officer unsure of / changes the charge
  SECTION_MISCITATION             wrong statute section referenced
  BWC_COMPLIANCE_GAP              footage cut / camera turned off at
                                  sensitive moments, or audible "turn off"
  SUPERVISOR_ABSENT               significant decision with no
                                  supervisor-consultation language
  CONTRADICTORY_OFFICERS          officer A says X, officer B says Y
                                  at the same scene
  DV_HANDLING_FAILURE             DV-specific procedural shortfall
  MENTAL_HEALTH_UNCONSIDERED      distress signals with no welfare response
  IDENTITY_MIX_UP                 officer calls subject by wrong name
  INCONSISTENT_GROUNDS            arrest grounds differ between statements
                                  and BWC
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict, Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from rapidfuzz import fuzz


HEADER = "MACHINE-GENERATED - UNVERIFIED"

# ----- Phrase banks -------------------------------------------------------

UNCERTAINTY_PHRASES = [
    "i think", "i believe", "i'm not sure", "i am not sure",
    "not entirely sure", "might be", "could be", "probably",
    "i don't know", "i'm not certain", "let me check",
    "i'll have to check", "hang on", "hold on, let me",
    "wait a second", "what is it", "what's the section",
    "is it s", "is it section",
]

RUSH_TO_JUDGMENT = [
    "we know you did it", "we've got you", "you might as well",
    "no point lying", "stop pretending", "we have evidence",
    "the camera caught you", "witnesses saw you",
    "you're going down for this", "you did it we know",
    "just admit",
]

ESCALATION_FAILURE = [
    "stop resisting", "get on the ground", "shut up",
    "shut your mouth", "don't talk back", "don't move",
    "calm down" , "settle down",  # these can be problematic when used at compliant subjects
    "i'm not going to tell you again",
    "last warning", "one more time",
    "get down", "on the ground now",
]

IGNORED_EXCULPATION_SUBJECT_CUES = [
    "but i didn't", "i didn't do", "let me explain",
    "that's not what happened", "you don't understand",
    "i was trying to", "the reason is", "i'm trying to tell you",
    "please listen", "that's not true",
]

CHARGE_CONFUSION = [
    "is it trespass", "or is it break", "what's the charge",
    "what are we charging", "is this s",
    "let me check the charge", "which offence",
    "breaking or entering", "or is that", "hmm which one",
]

SECTION_MISCITATION_PATTERNS = [
    re.compile(r"\bsection\s+\d+[A-Z]?\s+of\s+the\s+\w+"),
    re.compile(r"\bs\s*\.\s*\d+[A-Z]?\b"),
    re.compile(r"\bPPRA\s+s\s*\.?\s*\d+"),
]

BWC_TURNOFF_CUES = [
    "i'll turn this off", "turn the camera off",
    "stop the recording", "pause the camera",
    "we'll turn off", "camera's off",
    "off the record",
]

SUPERVISOR_CUES = [
    "sergeant", "senior constable", "supervisor", "o.i.c",
    "officer in charge", "comms", "dispatch", "call my sergeant",
    "let me call", "speak to my supervisor", "my sergeant says",
    "sarge", "duty sergeant", "roster sergeant",
]

DV_HANDLING_CUES_REQUIRED = [
    "support person", "domestic violence liaison", "DVLO",
    "protection order", "safety plan", "referral",
    "do you want someone", "is there anyone",
]

DV_CONTEXT_TRIGGERS = [
    "domestic", "partner", "spouse", "ex-partner", "girlfriend",
    "boyfriend", "DV", "protection order", "PPN",
]

MENTAL_HEALTH_DISTRESS = [
    "i can't breathe", "panic attack", "i'm having",
    "i can't cope", "please stop", "i want to die",
    "self harm", "i'm scared", "i'm terrified",
    "i'm going to pass out", "heart racing",
]

MENTAL_HEALTH_RESPONSES_REQUIRED = [
    "qas", "ambulance", "paramedic", "mental health",
    "welfare check", "are you ok", "are you all right",
    "do you need help", "let's get you",
]

COMPLIANT_SUBJECT_CUES = [
    "yes officer", "okay okay", "i'll do it", "i am",
    "i'm doing it", "okay mate", "i understand",
    "not resisting", "i'm cooperating", "on my knees",
    "hands up", "i've got my hands up",
]

GROUNDS_CUES = [
    "for the offence of", "in relation to", "on suspicion of",
    "the reason is", "because you", "grounds for the arrest",
    "for the purpose of",
]


# ----- Helpers ------------------------------------------------------------


def _contains(text: str, phrases: Iterable[str], threshold: int = 88) -> list[str]:
    hits: list[str] = []
    lt = text.lower()
    for p in phrases:
        if p in lt:
            hits.append(p)
        elif fuzz.partial_ratio(lt, p) >= threshold:
            hits.append(p)
    return hits


def _hms(seconds: float) -> str:
    s = int(seconds)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def _is_question(text: str) -> bool:
    t = text.strip()
    if t.endswith("?"):
        return True
    lt = t.lower()
    return any(lt.startswith(o) for o in (
        "what ", "where ", "when ", "why ", "who ", "how ",
        "did ", "do you ", "were you ", "are you ",
    ))


# ----- Finding dataclass --------------------------------------------------


@dataclass
class CompetencyFinding:
    kind: str
    severity: str
    exhibit: str
    timestamp: str
    speaker_hint: str
    utterance: str
    detail: str


# ----- Loaders ------------------------------------------------------------


def _load_transcripts(output_dir: Path) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for p in sorted(output_dir.glob("*.transcript.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        stem = p.stem.removesuffix(".transcript")
        out[stem] = data.get("segments", [])
    return out


def _load_integrity(output_dir: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for p in sorted(output_dir.glob("*.integrity.json")):
        try:
            out[p.stem.removesuffix(".integrity")] = json.loads(
                p.read_text(encoding="utf-8", errors="replace")
            )
        except Exception:
            continue
    return out


def _load_docs_text(output_dir: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    docs_dir = output_dir / "documents"
    if not docs_dir.is_dir():
        return out
    for p in sorted(docs_dir.glob("*.doc.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8", errors="replace"))
            out[d.get("stem", p.stem)] = d.get("text", "") or ""
        except Exception:
            continue
    return out


# ----- Detectors ----------------------------------------------------------


def _detect_uncertainty(exhibit: str, segments: list[dict]) -> list[CompetencyFinding]:
    out: list[CompetencyFinding] = []
    for s in segments:
        hits = _contains(s.get("text", "") or "", UNCERTAINTY_PHRASES)
        if hits:
            out.append(CompetencyFinding(
                kind="UNCERTAINTY", severity="medium", exhibit=exhibit,
                timestamp=_hms(float(s.get("start", 0))),
                speaker_hint="officer (inferred)",
                utterance=s.get("text", ""),
                detail=f"Hedging / uncertainty phrases: {', '.join(hits)}",
            ))
    return out


def _detect_rush_to_judgment(exhibit: str, segments: list[dict]) -> list[CompetencyFinding]:
    out: list[CompetencyFinding] = []
    for s in segments:
        hits = _contains(s.get("text", "") or "", RUSH_TO_JUDGMENT)
        if hits:
            out.append(CompetencyFinding(
                kind="RUSH_TO_JUDGMENT", severity="high", exhibit=exhibit,
                timestamp=_hms(float(s.get("start", 0))),
                speaker_hint="officer (inferred)",
                utterance=s.get("text", ""),
                detail=f"Presumptive phrasing: {', '.join(hits)}",
            ))
    return out


def _detect_escalation_failure(
    exhibit: str, segments: list[dict],
) -> list[CompetencyFinding]:
    out: list[CompetencyFinding] = []
    # Heuristic: if compliant-subject cues appear within 20s before an
    # escalation cue, flag.
    for i, s in enumerate(segments):
        esc_hits = _contains(s.get("text", "") or "", ESCALATION_FAILURE)
        if not esc_hits:
            continue
        window_start = float(s.get("start", 0)) - 20
        compliant = False
        for j in range(max(0, i - 8), i):
            if float(segments[j].get("end", 0)) >= window_start:
                if _contains(segments[j].get("text", "") or "", COMPLIANT_SUBJECT_CUES):
                    compliant = True
                    break
        if compliant:
            out.append(CompetencyFinding(
                kind="ESCALATION_FAILURE", severity="high", exhibit=exhibit,
                timestamp=_hms(float(s.get("start", 0))),
                speaker_hint="officer (inferred)",
                utterance=s.get("text", ""),
                detail=f"Aggressive/commanding tone despite compliance cues within 20s: {', '.join(esc_hits)}",
            ))
    return out


def _detect_ignored_exculpation(exhibit: str, segments: list[dict]) -> list[CompetencyFinding]:
    out: list[CompetencyFinding] = []
    for i, s in enumerate(segments):
        if not _contains(s.get("text", "") or "", IGNORED_EXCULPATION_SUBJECT_CUES):
            continue
        # Look at the next 1-3 segments - does officer engage with the
        # explanation (ask follow-up), or move on?
        following = segments[i + 1 : i + 4]
        engaged = False
        for nxt in following:
            nxt_text = (nxt.get("text") or "").lower()
            if any(tok in nxt_text for tok in ("tell me more", "what happened", "go on", "explain", "walk me through")):
                engaged = True
                break
        if not engaged and following:
            out.append(CompetencyFinding(
                kind="IGNORED_EXCULPATION", severity="medium", exhibit=exhibit,
                timestamp=_hms(float(s.get("start", 0))),
                speaker_hint="subject (inferred)",
                utterance=s.get("text", ""),
                detail="Subject offered explanation; no follow-up engagement in next 3 segments.",
            ))
    return out


def _detect_charge_confusion(exhibit: str, segments: list[dict]) -> list[CompetencyFinding]:
    out: list[CompetencyFinding] = []
    # Direct phrase hits
    for s in segments:
        hits = _contains(s.get("text", "") or "", CHARGE_CONFUSION)
        if hits:
            out.append(CompetencyFinding(
                kind="CHARGE_CONFUSION", severity="high", exhibit=exhibit,
                timestamp=_hms(float(s.get("start", 0))),
                speaker_hint="officer (inferred)",
                utterance=s.get("text", ""),
                detail=f"Unclear / changing charge: {', '.join(hits)}",
            ))
    # Multiple sections cited across the transcript
    sections: Counter[str] = Counter()
    for s in segments:
        for pat in SECTION_MISCITATION_PATTERNS:
            for m in pat.finditer(s.get("text", "") or ""):
                sections[m.group(0).lower()] += 1
    if len(sections) >= 2:
        out.append(CompetencyFinding(
            kind="CHARGE_CONFUSION", severity="medium", exhibit=exhibit,
            timestamp="",
            speaker_hint="officer(s)",
            utterance="",
            detail=f"Multiple distinct statute references cited: {', '.join(sorted(sections))}",
        ))
    return out


def _detect_bwc_compliance(
    exhibit: str, segments: list[dict], integrity: dict | None,
) -> list[CompetencyFinding]:
    out: list[CompetencyFinding] = []
    # Explicit turnoff phrases
    for s in segments:
        hits = _contains(s.get("text", "") or "", BWC_TURNOFF_CUES)
        if hits:
            out.append(CompetencyFinding(
                kind="BWC_COMPLIANCE_GAP", severity="critical", exhibit=exhibit,
                timestamp=_hms(float(s.get("start", 0))),
                speaker_hint="officer (inferred)",
                utterance=s.get("text", ""),
                detail=f"Audible reference to stopping / pausing camera: {', '.join(hits)}",
            ))
    # Many scene cuts or black intervals
    if integrity:
        n_cuts = len(integrity.get("scene_cuts") or [])
        n_black = len(integrity.get("black_frames") or [])
        n_freeze = len(integrity.get("freeze_frames") or [])
        if n_cuts >= 4 or n_black >= 2 or n_freeze >= 1:
            out.append(CompetencyFinding(
                kind="BWC_COMPLIANCE_GAP", severity="high", exhibit=exhibit,
                timestamp="",
                speaker_hint="",
                utterance="",
                detail=f"Unusual footage artefacts: scene_cuts={n_cuts}, "
                       f"black_intervals={n_black}, freeze_intervals={n_freeze}",
            ))
    return out


def _detect_supervisor_absent(
    exhibit: str, segments: list[dict],
) -> list[CompetencyFinding]:
    if not segments:
        return []
    duration = float(segments[-1].get("end", 0))
    if duration < 60:
        return []  # short clips rarely warrant supervisor talk
    all_text = " ".join((s.get("text") or "") for s in segments)
    supervisor_found = _contains(all_text, SUPERVISOR_CUES, threshold=92)
    arrest_found = _contains(all_text, ["you are under arrest", "you're under arrest"])
    if arrest_found and not supervisor_found:
        return [CompetencyFinding(
            kind="SUPERVISOR_ABSENT", severity="medium", exhibit=exhibit,
            timestamp="", speaker_hint="", utterance="",
            detail=f"Arrest made during exhibit ({duration:.0f}s) with no "
                   "audible supervisor consultation or radio call.",
        )]
    return []


def _detect_dv_handling(exhibit: str, segments: list[dict]) -> list[CompetencyFinding]:
    all_text = " ".join((s.get("text") or "") for s in segments).lower()
    if not any(t in all_text for t in DV_CONTEXT_TRIGGERS):
        return []
    required_hits = _contains(all_text, DV_HANDLING_CUES_REQUIRED)
    if not required_hits:
        return [CompetencyFinding(
            kind="DV_HANDLING_FAILURE", severity="high", exhibit=exhibit,
            timestamp="", speaker_hint="", utterance="",
            detail="DV context detected (references to partner / DV / PPN) but "
                   "no language indicating support-person offer, DVLO referral, "
                   "or safety plan.",
        )]
    return []


def _detect_mental_health_unconsidered(
    exhibit: str, segments: list[dict],
) -> list[CompetencyFinding]:
    out: list[CompetencyFinding] = []
    for i, s in enumerate(segments):
        hits = _contains(s.get("text", "") or "", MENTAL_HEALTH_DISTRESS)
        if not hits:
            continue
        # Look forward 30 seconds for a welfare response
        end_window = float(s.get("end", 0)) + 30
        response = False
        for nxt in segments[i + 1 : i + 10]:
            if float(nxt.get("start", 0)) > end_window:
                break
            if _contains(nxt.get("text", "") or "", MENTAL_HEALTH_RESPONSES_REQUIRED):
                response = True
                break
        if not response:
            out.append(CompetencyFinding(
                kind="MENTAL_HEALTH_UNCONSIDERED", severity="high",
                exhibit=exhibit,
                timestamp=_hms(float(s.get("start", 0))),
                speaker_hint="subject (inferred)",
                utterance=s.get("text", ""),
                detail=f"Distress signal ({', '.join(hits)}) with no welfare "
                       "response in the following ~30s.",
            ))
    return out


def _detect_cross_officer_contradictions(
    transcripts: dict[str, list[dict]],
) -> list[CompetencyFinding]:
    """Very light-touch: look for named offences cited in different exhibits."""
    offence_re = re.compile(
        r"\b(?:assault|trespass|break\s+and\s+enter|domestic\s+violence|"
        r"breach\s+of\s+(?:bail|protection\s+order)|stealing|obstruct(?:ing)?|"
        r"resist\s+arrest|public\s+nuisance|wilful\s+damage)\b",
        re.IGNORECASE,
    )
    offence_by_exhibit: dict[str, set[str]] = defaultdict(set)
    for stem, segs in transcripts.items():
        for s in segs:
            for m in offence_re.finditer((s.get("text") or "")):
                offence_by_exhibit[stem].add(m.group(0).lower())

    findings: list[CompetencyFinding] = []
    all_offences = {o for offs in offence_by_exhibit.values() for o in offs}
    if len(all_offences) >= 3 and len(transcripts) >= 2:
        findings.append(CompetencyFinding(
            kind="CONTRADICTORY_OFFICERS", severity="medium",
            exhibit="<multi>",
            timestamp="",
            speaker_hint="",
            utterance="",
            detail=f"Across {len(transcripts)} processed exhibits, {len(all_offences)} "
                   f"distinct offence references detected: {', '.join(sorted(all_offences))}. "
                   "Confirm officers agree on the charge being pursued.",
        ))
    return findings


def _detect_identity_mix_up(
    transcripts: dict[str, list[dict]],
    docs_text: dict[str, str],
) -> list[CompetencyFinding]:
    """Flag officer calling subject by a name that fuzzy-differs from the
    canonical subject name present in the documents corpus."""
    # Heuristic: find the most frequent surname from docs, then find all
    # transcript occurrences that look like a name but don't match it.
    surname_counts: Counter[str] = Counter()
    surname_re = re.compile(r"\b([A-Z][A-Z]{2,}(?:[-' ][A-Z]{2,})?)\b")
    for text in docs_text.values():
        for m in surname_re.finditer(text):
            surname_counts[m.group(1)] += 1
    if not surname_counts:
        return []
    canonical, _ = surname_counts.most_common(1)[0]
    variants: set[str] = set()
    findings: list[CompetencyFinding] = []
    for stem, segs in transcripts.items():
        for s in segs:
            text = s.get("text") or ""
            for m in re.finditer(r"\bMr\.?\s+([A-Z][a-z]+)\b", text):
                name = m.group(1)
                if name.upper() == canonical.upper():
                    continue
                if fuzz.ratio(name.upper(), canonical.upper()) >= 65:
                    variants.add(name)
                    findings.append(CompetencyFinding(
                        kind="IDENTITY_MIX_UP", severity="high",
                        exhibit=stem,
                        timestamp=_hms(float(s.get("start", 0))),
                        speaker_hint="officer (inferred)",
                        utterance=text,
                        detail=f"Officer refers to subject as '{name}' but "
                               f"documents corpus canonical surname is '{canonical}'.",
                    ))
    return findings


# ----- Orchestration ------------------------------------------------------


def analyze(output_dir: Path) -> list[CompetencyFinding]:
    output_dir = Path(output_dir)
    transcripts = _load_transcripts(output_dir)
    integrity = _load_integrity(output_dir)
    docs_text = _load_docs_text(output_dir)

    findings: list[CompetencyFinding] = []
    for stem, segs in transcripts.items():
        findings += _detect_uncertainty(stem, segs)
        findings += _detect_rush_to_judgment(stem, segs)
        findings += _detect_escalation_failure(stem, segs)
        findings += _detect_ignored_exculpation(stem, segs)
        findings += _detect_charge_confusion(stem, segs)
        findings += _detect_bwc_compliance(stem, segs, integrity.get(stem))
        findings += _detect_supervisor_absent(stem, segs)
        findings += _detect_dv_handling(stem, segs)
        findings += _detect_mental_health_unconsidered(stem, segs)
    findings += _detect_cross_officer_contradictions(transcripts)
    findings += _detect_identity_mix_up(transcripts, docs_text)
    return findings


def save(findings: list[CompetencyFinding], output_dir: Path) -> tuple[Path, Path]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "COMPETENCY_FINDINGS.csv"
    md_path = output_dir / "COMPETENCY_FINDINGS.md"

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# {HEADER}\n")
        w = csv.writer(f)
        w.writerow([
            "row", "kind", "severity", "exhibit", "timestamp",
            "speaker_hint", "utterance", "detail", "human_verified",
        ])
        for i, fd in enumerate(findings, 1):
            w.writerow([
                i, fd.kind, fd.severity, fd.exhibit, fd.timestamp,
                fd.speaker_hint, fd.utterance, fd.detail, "",
            ])

    by_kind: dict[str, list[CompetencyFinding]] = defaultdict(list)
    for fd in findings:
        by_kind[fd.kind].append(fd)

    kind_order = [
        "BWC_COMPLIANCE_GAP", "RUSH_TO_JUDGMENT", "ESCALATION_FAILURE",
        "IDENTITY_MIX_UP", "MENTAL_HEALTH_UNCONSIDERED", "CHARGE_CONFUSION",
        "DV_HANDLING_FAILURE", "CONTRADICTORY_OFFICERS",
        "IGNORED_EXCULPATION", "SUPERVISOR_ABSENT", "UNCERTAINTY",
    ]
    lines: list[str] = [
        "# QPS Competency & Decision-Making Findings",
        "",
        f"> **{HEADER}**",
        f"> Total findings: {len(findings)}",
        "",
    ]
    for kind in kind_order:
        items = by_kind.get(kind) or []
        lines.append(f"## {kind} ({len(items)})")
        lines.append("")
        if not items:
            lines.append("_None detected._")
            lines.append("")
            continue
        lines.append("| Severity | Exhibit | Time | Speaker | Utterance | Detail |")
        lines.append("|----------|---------|------|---------|-----------|--------|")
        for fd in items[:80]:
            ev = (fd.utterance or "").replace("|", "\\|")
            detail = (fd.detail or "").replace("|", "\\|")
            lines.append(
                f"| {fd.severity} | {fd.exhibit} | {fd.timestamp} | "
                f"{fd.speaker_hint} | {ev} | {detail} |"
            )
        if len(items) > 80:
            lines.append(f"| ... | ... | ... | ... | ... | {len(items) - 80} more rows in CSV |")
        lines.append("")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return csv_path, md_path


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", required=True)
    args = ap.parse_args()
    f = analyze(Path(args.output_dir))
    csvp, mdp = save(f, Path(args.output_dir))
    print(f"{len(f)} competency findings.")
    print(f"  {csvp}")
    print(f"  {mdp}")
