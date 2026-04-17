"""Detect moments where physical / documentary evidence was offered to
officers and score whether the officer engaged.

Defence-side intent: if an officer was presented with contemporaneous
exculpatory evidence (lease, mail, photos, documents, contemporaneous
witness offering papers) and did not read it, ask about it, or refer
back to it, that is a direct failure of impartial investigation.

Categories (kind column):

  OFFERED_AND_IGNORED            subject / third party offers evidence;
                                 officer does not engage in next ~90s
  OFFERED_ACKNOWLEDGED_ONLY      officer says "okay / thanks" but
                                 never references the evidence again
  OFFERED_AND_DISCUSSED          officer asks follow-up or refers back
                                 (positive - no flag, informational)
  PHYSICAL_REFERENCE_UNEXAMINED  subject points to visible physical
                                 evidence ("look at the mail",
                                 "these papers on the bench") but
                                 officer does not respond to it
  RESIDENCY_EVIDENCE_IGNORED     keywords consistent with residency
                                 proof (mail addressed to me, lease
                                 here, my keys) mentioned and not
                                 engaged with

All findings are MACHINE-GENERATED - UNVERIFIED. Every row has a
human_verified column empty by default.
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from rapidfuzz import fuzz


HEADER = "MACHINE-GENERATED - UNVERIFIED"

OFFER_PHRASES_SUBJECT = [
    "here's my", "here are my", "these are my",
    "i have the", "i have my", "i've got my", "i've got the",
    "take a look", "have a look", "look at this", "look at these",
    "can i show you", "let me show", "i can show",
    "here's the", "this is the", "you can see",
    "these documents", "these papers", "this proves",
    "this shows", "this is proof", "as you can see",
]

OFFER_PHRASES_THIRD_PARTY = [
    "tom says", "tom has", "tom gave", "tom's got",
    "here's what", "he gave me", "she gave me",
    "take these", "have these",
]

OFFICER_ACKNOWLEDGEMENT = [
    "thanks", "thank you", "okay", "alright",
    "i'll take that", "hand that over", "give me that",
    "yep", "mhm", "got it", "noted",
]

OFFICER_ENGAGEMENT = [
    "what is this", "what's this", "tell me about",
    "when did you", "where did you get",
    "how did", "who gave you", "what does it say",
    "can you walk me through", "explain", "read it",
    "let me see", "show me more", "what does this mean",
    "is this signed", "when was this",
]

PHYSICAL_REFERENCE_CUES = [
    "mail at", "my mail", "letter addressed", "envelope",
    "on the bench", "on the counter", "on the table",
    "in the kitchen", "by the door", "at the front door",
    "on the fridge", "on the wall", "on the floor",
    "in the drawer", "my keys", "my lease",
]

RESIDENCY_CUES = [
    "my mail", "addressed to me", "this is my address",
    "i live here", "my lease", "on the lease",
    "my keys", "my bedroom", "my room",
    "my belongings", "my things",
    "bills in my name", "bill in my name",
]


@dataclass
class EngagementFinding:
    kind: str
    severity: str
    exhibit: str
    timestamp: str
    offered_by: str
    offered_text: str
    officer_response: str
    detail: str


def _contains(text: str, phrases, threshold: int = 88) -> list[str]:
    t = (text or "").lower()
    hits = [p for p in phrases if p in t]
    if hits:
        return hits
    for p in phrases:
        if fuzz.partial_ratio(t, p) >= threshold:
            hits.append(p)
    return hits


def _hms(s: float) -> str:
    s = int(s)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def _load_transcripts(output_dir: Path) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for p in sorted(output_dir.glob("*.transcript.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        out[p.stem.removesuffix(".transcript")] = d.get("segments", []) or []
    return out


def _keyword_window(
    segments: list[dict], start_index: int, window_seconds: float
) -> list[dict]:
    """Return segments within `window_seconds` after segments[start_index]."""
    if start_index >= len(segments):
        return []
    anchor_end = float(segments[start_index].get("end", 0))
    window_end = anchor_end + window_seconds
    out = []
    for s in segments[start_index + 1 :]:
        if float(s.get("start", 0)) > window_end:
            break
        out.append(s)
    return out


def _scan_offers(exhibit: str, segments: list[dict]) -> list[EngagementFinding]:
    findings: list[EngagementFinding] = []
    for i, s in enumerate(segments):
        text = s.get("text", "") or ""
        subject_offer = _contains(text, OFFER_PHRASES_SUBJECT)
        tp_offer = _contains(text, OFFER_PHRASES_THIRD_PARTY)
        if not subject_offer and not tp_offer:
            continue
        offered_by = "subject" if subject_offer else "third_party"
        phrases = subject_offer or tp_offer
        window = _keyword_window(segments, i, 90.0)
        engaged = False
        acknowledged = False
        response_text = ""
        for w in window:
            wt = (w.get("text") or "").lower()
            if _contains(wt, OFFICER_ENGAGEMENT):
                engaged = True
                response_text = w.get("text", "")
                break
            if _contains(wt, OFFICER_ACKNOWLEDGEMENT):
                acknowledged = True
                response_text = response_text or w.get("text", "")

        if engaged:
            findings.append(EngagementFinding(
                kind="OFFERED_AND_DISCUSSED", severity="low",
                exhibit=exhibit,
                timestamp=_hms(float(s.get("start", 0))),
                offered_by=offered_by,
                offered_text=text.strip(),
                officer_response=response_text,
                detail=f"Evidence offered ({', '.join(phrases)}); officer engaged with follow-up.",
            ))
        elif acknowledged:
            findings.append(EngagementFinding(
                kind="OFFERED_ACKNOWLEDGED_ONLY", severity="medium",
                exhibit=exhibit,
                timestamp=_hms(float(s.get("start", 0))),
                offered_by=offered_by,
                offered_text=text.strip(),
                officer_response=response_text,
                detail=f"Evidence offered ({', '.join(phrases)}); officer acknowledged but did not discuss.",
            ))
        else:
            findings.append(EngagementFinding(
                kind="OFFERED_AND_IGNORED", severity="high",
                exhibit=exhibit,
                timestamp=_hms(float(s.get("start", 0))),
                offered_by=offered_by,
                offered_text=text.strip(),
                officer_response="",
                detail=f"Evidence offered ({', '.join(phrases)}); no officer engagement or acknowledgement in next 90s.",
            ))
    return findings


def _scan_physical(exhibit: str, segments: list[dict]) -> list[EngagementFinding]:
    findings: list[EngagementFinding] = []
    for i, s in enumerate(segments):
        text = s.get("text", "") or ""
        hits = _contains(text, PHYSICAL_REFERENCE_CUES)
        if not hits:
            continue
        window = _keyword_window(segments, i, 60.0)
        engaged = any(_contains((w.get("text") or ""), OFFICER_ENGAGEMENT)
                      for w in window)
        if engaged:
            continue
        findings.append(EngagementFinding(
            kind="PHYSICAL_REFERENCE_UNEXAMINED",
            severity="high", exhibit=exhibit,
            timestamp=_hms(float(s.get("start", 0))),
            offered_by="subject_or_third_party",
            offered_text=text.strip(),
            officer_response="",
            detail=f"Reference to physical evidence ({', '.join(hits)}) with no officer engagement in next 60s.",
        ))
    return findings


def _scan_residency(exhibit: str, segments: list[dict]) -> list[EngagementFinding]:
    findings: list[EngagementFinding] = []
    for i, s in enumerate(segments):
        text = s.get("text", "") or ""
        hits = _contains(text, RESIDENCY_CUES)
        if not hits:
            continue
        window = _keyword_window(segments, i, 60.0)
        engaged = any(_contains((w.get("text") or ""), OFFICER_ENGAGEMENT)
                      for w in window)
        if engaged:
            continue
        findings.append(EngagementFinding(
            kind="RESIDENCY_EVIDENCE_IGNORED",
            severity="critical", exhibit=exhibit,
            timestamp=_hms(float(s.get("start", 0))),
            offered_by="subject",
            offered_text=text.strip(),
            officer_response="",
            detail=f"Residency proof referenced ({', '.join(hits)}) without officer engagement in next 60s.",
        ))
    return findings


def analyze(output_dir: Path) -> list[EngagementFinding]:
    transcripts = _load_transcripts(Path(output_dir))
    findings: list[EngagementFinding] = []
    for stem, segs in transcripts.items():
        findings += _scan_offers(stem, segs)
        findings += _scan_physical(stem, segs)
        findings += _scan_residency(stem, segs)
    return findings


def save(findings: list[EngagementFinding], output_dir: Path) -> tuple[Path, Path]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "EVIDENCE_ENGAGEMENT.csv"
    md_path = output_dir / "EVIDENCE_ENGAGEMENT.md"

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# {HEADER}\n")
        w = csv.writer(f)
        w.writerow([
            "row", "kind", "severity", "exhibit", "timestamp",
            "offered_by", "offered_text", "officer_response", "detail",
            "human_verified",
        ])
        for i, fd in enumerate(findings, 1):
            w.writerow([
                i, fd.kind, fd.severity, fd.exhibit, fd.timestamp,
                fd.offered_by, fd.offered_text, fd.officer_response,
                fd.detail, "",
            ])

    by_kind: dict[str, list[EngagementFinding]] = defaultdict(list)
    for fd in findings:
        by_kind[fd.kind].append(fd)
    kind_order = ["RESIDENCY_EVIDENCE_IGNORED", "OFFERED_AND_IGNORED",
                  "PHYSICAL_REFERENCE_UNEXAMINED",
                  "OFFERED_ACKNOWLEDGED_ONLY", "OFFERED_AND_DISCUSSED"]

    lines: list[str] = [
        "# Evidence Engagement Findings",
        "",
        f"> **{HEADER}**",
        f"> Total findings: {len(findings)}",
        "",
        "_A finding in `OFFERED_AND_DISCUSSED` is informational (good).",
        "Everything else is a failure of impartial investigation worth"
        " flagging for counsel._",
        "",
    ]
    for kind in kind_order:
        items = by_kind.get(kind) or []
        lines.append(f"## {kind}  ({len(items)})")
        lines.append("")
        if not items:
            lines.append("_None detected._")
            lines.append("")
            continue
        lines.append("| Severity | Exhibit | Time | Offered by | Offered text | Officer response |")
        lines.append("|----------|---------|------|-----------|--------------|------------------|")
        for fd in items[:50]:
            ot = (fd.offered_text or "").replace("|", "\\|")
            orr = (fd.officer_response or "").replace("|", "\\|")
            lines.append(
                f"| {fd.severity} | {fd.exhibit} | {fd.timestamp} | "
                f"{fd.offered_by} | {ot} | {orr or '_(none)_'} |"
            )
        if len(items) > 50:
            lines.append(f"| ... | ... | ... | ... | ... | {len(items) - 50} more in CSV |")
        lines.append("")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return csv_path, md_path


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", required=True)
    args = ap.parse_args()
    findings = analyze(Path(args.output_dir))
    csvp, mdp = save(findings, Path(args.output_dir))
    print(f"{len(findings)} engagement findings.")
    print(f"  {csvp}")
    print(f"  {mdp}")
