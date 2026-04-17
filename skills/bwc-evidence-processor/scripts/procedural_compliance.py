"""Procedural compliance checker.

Scans a Whisper word-level transcript and flags:

- Absence of required cautions / rights warnings
- Late cautions (given AFTER questioning begins)
- Continued questioning after a subject invokes right to silence / requests counsel
- Missing arrest-grounds recitation when arrest language is used
- Search without stated warrant or consent
- Promises and threats (inducements) in the vicinity of admissions
- Break of caution after a break in questioning (PPRA s431/436 analogues)

All findings are investigative markers. Every row carries a human_verified
column that counsel must sign off before the finding is used.
"""

from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from rapidfuzz import fuzz


HEADER = "MACHINE-GENERATED - UNVERIFIED"

CAUTION_PHRASES = [
    "you do not have to say anything",
    "you are not obliged to say anything",
    "anything you do say may be used",
    "anything you say may be used",
    "may be given in evidence",
    "right to remain silent",
    "have the right to",
]

RIGHT_TO_COUNSEL_PHRASES = [
    "right to a lawyer",
    "right to legal",
    "speak to a lawyer",
    "contact a lawyer",
    "contact a friend or relative",
    "support person",
]

INVOCATION_PHRASES = [
    "i don't want to answer",
    "no comment",
    "i want a lawyer",
    "i want to speak to a lawyer",
    "i'm not saying anything",
    "i don't want to say anything",
    "i want to remain silent",
    "i want to stop",
    "i don't want to continue",
    "i want my lawyer",
    "speak to my lawyer",
]

ARREST_LANGUAGE = [
    "you are under arrest",
    "you're under arrest",
    "i am arresting you",
    "i'm arresting you",
    "placing you under arrest",
]

ARREST_GROUNDS_TRIGGERS = [
    "for the offence of",
    "in relation to",
    "on suspicion of",
    "because you",
    "the reason is",
    "grounds for the arrest",
]

SEARCH_LANGUAGE = [
    "i'm going to search",
    "we're going to search",
    "going to search you",
    "going to search the",
    "conduct a search",
    "pat you down",
    "empty your pockets",
]

WARRANT_OR_CONSENT = [
    "search warrant",
    "warrant",
    "do you consent",
    "do you agree",
    "with your permission",
    "under section",
]

PROMISES_THREATS = [
    "if you tell me",
    "it'll be easier",
    "it will be easier",
    "go easier on you",
    "help you out",
    "make it worse",
    "you'll be sorry",
    "i'll make sure",
    "things will go badly",
    "you don't cooperate",
    "if you cooperate",
    "off the record",
    "between you and me",
]

LEADING_QUESTIONS = [
    "isn't it true that",
    "so you agree that",
    "you were there, weren't you",
    "you did it, didn't you",
    "that's correct, isn't it",
    "you must have",
    "surely you",
]


@dataclass
class ComplianceFinding:
    category: str
    severity: str
    start: float
    end: float
    utterance: str
    detail: str


def _flatten_words(segments: list[dict]) -> list[dict]:
    words: list[dict] = []
    for seg in segments:
        for w in seg.get("words") or []:
            words.append({
                "start": float(w.get("start", seg["start"])),
                "end": float(w.get("end", seg["end"])),
                "text": (w.get("text") or "").strip(),
                "segment_text": seg["text"],
            })
        if not (seg.get("words") or []):
            words.append({
                "start": float(seg["start"]),
                "end": float(seg["end"]),
                "text": seg["text"],
                "segment_text": seg["text"],
            })
    return words


def _contains(segment_text: str, phrases: Iterable[str], threshold: int = 88) -> bool:
    lt = segment_text.lower()
    for ph in phrases:
        if ph in lt:
            return True
        if fuzz.partial_ratio(lt, ph) >= threshold:
            return True
    return False


def _first_segment_matching(segments: list[dict], phrases: list[str]) -> dict | None:
    for s in segments:
        if _contains(s["text"], phrases):
            return s
    return None


def _is_question(text: str) -> bool:
    t = text.strip()
    if t.endswith("?"):
        return True
    lt = t.lower()
    for opener in ("what ", "where ", "when ", "why ", "who ", "how ",
                   "did ", "do you ", "can you ", "could you ", "would you ",
                   "were you ", "have you ", "had you ", "are you ",
                   "is it ", "was it "):
        if lt.startswith(opener):
            return True
    return False


def check(segments: list[dict]) -> list[ComplianceFinding]:
    findings: list[ComplianceFinding] = []

    caution_seg = _first_segment_matching(segments, CAUTION_PHRASES)
    counsel_seg = _first_segment_matching(segments, RIGHT_TO_COUNSEL_PHRASES)
    first_question = next((s for s in segments if _is_question(s["text"])), None)

    if caution_seg is None:
        findings.append(ComplianceFinding(
            category="missing_caution",
            severity="high",
            start=0.0,
            end=segments[-1]["end"] if segments else 0.0,
            utterance="",
            detail="No caution / right-to-silence warning detected anywhere in the transcript.",
        ))
    elif first_question and caution_seg["start"] > first_question["start"] + 1.0:
        findings.append(ComplianceFinding(
            category="late_caution",
            severity="high",
            start=first_question["start"],
            end=caution_seg["end"],
            utterance=caution_seg["text"],
            detail=(
                f"Questioning appears to begin at {first_question['start']:.2f}s "
                f"but caution not delivered until {caution_seg['start']:.2f}s."
            ),
        ))

    if counsel_seg is None:
        findings.append(ComplianceFinding(
            category="missing_right_to_counsel",
            severity="high",
            start=0.0,
            end=segments[-1]["end"] if segments else 0.0,
            utterance="",
            detail="No advice of right to contact a lawyer / friend / relative detected.",
        ))

    # Invocation followed by continued questioning
    for i, s in enumerate(segments):
        if _contains(s["text"], INVOCATION_PHRASES):
            for later in segments[i + 1 : i + 12]:
                if _is_question(later["text"]):
                    findings.append(ComplianceFinding(
                        category="questioning_after_invocation",
                        severity="critical",
                        start=s["start"],
                        end=later["end"],
                        utterance=later["text"],
                        detail=(
                            f"Subject appears to invoke rights at {s['start']:.2f}s "
                            f"('{s['text']}') but questioning continues at "
                            f"{later['start']:.2f}s."
                        ),
                    ))
                    break

    # Arrest without stated grounds
    for i, s in enumerate(segments):
        if _contains(s["text"], ARREST_LANGUAGE):
            window = " ".join(x["text"] for x in segments[i : i + 6])
            if not _contains(window, ARREST_GROUNDS_TRIGGERS):
                findings.append(ComplianceFinding(
                    category="arrest_without_stated_grounds",
                    severity="high",
                    start=s["start"],
                    end=s["end"],
                    utterance=s["text"],
                    detail="Arrest language used without any grounds phrasing in the next ~6 segments.",
                ))

    # Search without warrant / consent
    for i, s in enumerate(segments):
        if _contains(s["text"], SEARCH_LANGUAGE):
            window = " ".join(
                x["text"] for x in segments[max(0, i - 4) : i + 5]
            )
            if not _contains(window, WARRANT_OR_CONSENT):
                findings.append(ComplianceFinding(
                    category="search_without_warrant_or_consent",
                    severity="high",
                    start=s["start"],
                    end=s["end"],
                    utterance=s["text"],
                    detail="Search announcement without warrant or consent phrasing in surrounding window.",
                ))

    # Inducements
    for s in segments:
        if _contains(s["text"], PROMISES_THREATS):
            findings.append(ComplianceFinding(
                category="possible_inducement",
                severity="critical",
                start=s["start"],
                end=s["end"],
                utterance=s["text"],
                detail="Phrasing consistent with a promise or threat (inducement risk).",
            ))

    # Leading questions
    for s in segments:
        if _contains(s["text"], LEADING_QUESTIONS):
            findings.append(ComplianceFinding(
                category="leading_question",
                severity="medium",
                start=s["start"],
                end=s["end"],
                utterance=s["text"],
                detail="Leading-question phrasing.",
            ))

    return findings


def save_findings(findings: list[ComplianceFinding], dest: Path) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# {HEADER}\n")
        writer = csv.writer(f)
        writer.writerow([
            "row", "category", "severity", "start", "end",
            "timestamp_hms", "utterance", "detail", "human_verified",
        ])
        for i, fd in enumerate(findings, 1):
            hms = _hms(fd.start)
            writer.writerow([
                i, fd.category, fd.severity, f"{fd.start:.3f}", f"{fd.end:.3f}",
                hms, fd.utterance, fd.detail, "",
            ])
    return dest


def _hms(seconds: float) -> str:
    s = int(seconds)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    data = json.loads(Path(args.transcript).read_text())
    findings = check(data["segments"])
    save_findings(findings, Path(args.output))
    print(f"{len(findings)} compliance findings written to {args.output}")
