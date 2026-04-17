"""Bias, tone and power-dynamics analysis.

Produces a per-segment and per-speaker breakdown of:

- questions vs statements (attributed to inferred speaker role)
- interruptions (speaker-A end time overlaps speaker-B start time)
- talk-time ratio
- aggressive/hostile lexicon density
- dehumanising or presumptive language
- confirmation-bias phrasing (looking only for evidence of guilt)
- one-sided framing markers (where the officer states the accused's intent)

Speaker inference is heuristic. It attempts to classify each segment as one
of: OFFICER, SUBJECT, OTHER. The inference is a strong aide-mémoire but MUST
be verified by counsel against the footage before use in any forum.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from pathlib import Path
from statistics import mean

from rapidfuzz import fuzz


HEADER = "MACHINE-GENERATED - UNVERIFIED"

OFFICER_CUES = [
    "sir", "ma'am", "mate",
    "i need you to", "step out of", "put your hands", "hands behind",
    "identify yourself", "you are under arrest", "you're under arrest",
    "stop resisting", "stop moving", "calm down",
    "we're the police", "i'm a police officer",
    "constable", "sergeant", "senior constable",
    "clear", "copy that", "roger", "10-4",
    "operational", "dispatch", "comms",
    "just admit", "admit it", "you did it", "you might as well",
    "tell me the truth", "tell us the truth",
    "where were you", "what did you do",
]

SUBJECT_CUES = [
    "i didn't", "i haven't", "i don't know",
    "please don't", "please sir", "why are you",
    "what did i do", "what have i done",
    "i want a lawyer", "i'm calling",
    "that's my", "that's not mine", "i swear",
    "i'm trying to", "you're hurting",
]

AGGRESSIVE_TOKENS = [
    "shut up", "shut it", "shut your", "don't talk back",
    "you're lying", "stop lying", "you're a liar",
    "don't fucking", "fucking", "piece of shit", "scumbag",
    "deadbeat", "junkie", "drunk", "crackhead",
    "don't make me", "i'll make you", "get on the ground",
    "face down", "stop resisting",
]

DEHUMANISING = [
    "you people", "your kind", "typical", "you lot",
    "you're just", "always the same",
]

PRESUMPTIVE = [
    "we know you did it",
    "we've got you",
    "you might as well tell us",
    "it's over for you",
    "no point lying",
    "we have evidence",
    "the camera saw you",
    "witnesses saw you",
]

CONFIRMATION_BIAS = [
    "admit it",
    "just admit",
    "you might as well admit",
    "everyone says",
    "everyone knows",
    "just tell me you did it",
    "be a man about it",
]

ONE_SIDED_FRAMING = [
    "you intended to",
    "you meant to",
    "your plan was",
    "you were going to",
    "you wanted to",
    "you decided to",
]


def _hit(text: str, phrases) -> list[str]:
    t = text.lower()
    return [p for p in phrases if p in t]


def _is_question(text: str) -> bool:
    t = text.strip()
    if t.endswith("?"):
        return True
    lt = t.lower()
    return any(lt.startswith(o) for o in (
        "what ", "where ", "when ", "why ", "who ", "how ",
        "did ", "do you ", "can you ", "could you ", "would you ",
        "were you ", "have you ", "are you ", "is it ",
    ))


def _word_count(text: str) -> int:
    return len([w for w in text.split() if w.strip()])


@dataclass
class SegmentScore:
    index: int
    start: float
    end: float
    text: str
    speaker_role: str
    is_question: bool
    word_count: int
    aggressive_hits: list[str] = field(default_factory=list)
    dehumanising_hits: list[str] = field(default_factory=list)
    presumptive_hits: list[str] = field(default_factory=list)
    confirmation_bias_hits: list[str] = field(default_factory=list)
    one_sided_hits: list[str] = field(default_factory=list)


def infer_role(text: str) -> str:
    lt = text.lower()
    o = sum(1 for c in OFFICER_CUES if c in lt)
    s = sum(1 for c in SUBJECT_CUES if c in lt)
    if o > s and o >= 1:
        return "OFFICER"
    if s > o and s >= 1:
        return "SUBJECT"
    # Fallback: fuzzy
    o_fz = max([fuzz.partial_ratio(lt, c) for c in OFFICER_CUES] or [0])
    s_fz = max([fuzz.partial_ratio(lt, c) for c in SUBJECT_CUES] or [0])
    if o_fz >= 92 and o_fz > s_fz:
        return "OFFICER"
    if s_fz >= 92 and s_fz > o_fz:
        return "SUBJECT"
    return "UNKNOWN"


def score_segments(
    segments: list[dict],
    role_overrides: dict[int, str] | None = None,
) -> list[SegmentScore]:
    out: list[SegmentScore] = []
    role_overrides = role_overrides or {}
    for seg in segments:
        text = seg["text"]
        idx = seg.get("index", 0)
        role = role_overrides.get(idx) or infer_role(text)
        out.append(SegmentScore(
            index=idx,
            start=float(seg["start"]),
            end=float(seg["end"]),
            text=text,
            speaker_role=role,
            is_question=_is_question(text),
            word_count=_word_count(text),
            aggressive_hits=_hit(text, AGGRESSIVE_TOKENS),
            dehumanising_hits=_hit(text, DEHUMANISING),
            presumptive_hits=_hit(text, PRESUMPTIVE),
            confirmation_bias_hits=_hit(text, CONFIRMATION_BIAS),
            one_sided_hits=_hit(text, ONE_SIDED_FRAMING),
        ))
    return out


def detect_interruptions(scores: list[SegmentScore], overlap_tol: float = 0.25) -> list[dict]:
    out = []
    for i in range(len(scores) - 1):
        a, b = scores[i], scores[i + 1]
        if (
            a.speaker_role != b.speaker_role
            and a.speaker_role != "UNKNOWN"
            and b.speaker_role != "UNKNOWN"
        ):
            gap = b.start - a.end
            if gap < -overlap_tol:
                out.append({
                    "at": b.start,
                    "by_role": b.speaker_role,
                    "over_role": a.speaker_role,
                    "interrupter_text": b.text,
                    "interrupted_text": a.text,
                    "overlap_seconds": round(-gap, 3),
                })
    return out


def summarise(scores: list[SegmentScore]) -> dict:
    def by_role(role):
        return [s for s in scores if s.speaker_role == role]

    officer = by_role("OFFICER")
    subject = by_role("SUBJECT")

    def talk_seconds(items):
        return round(sum(s.end - s.start for s in items), 3)

    def q_ratio(items):
        if not items:
            return 0.0
        return round(sum(1 for s in items if s.is_question) / len(items), 3)

    def density(items, attr):
        if not items:
            return 0.0
        return round(mean(len(getattr(s, attr)) for s in items), 3)

    return {
        "officer_talk_seconds": talk_seconds(officer),
        "subject_talk_seconds": talk_seconds(subject),
        "officer_segments": len(officer),
        "subject_segments": len(subject),
        "officer_question_ratio": q_ratio(officer),
        "subject_question_ratio": q_ratio(subject),
        "officer_aggressive_density": density(officer, "aggressive_hits"),
        "officer_dehumanising_density": density(officer, "dehumanising_hits"),
        "officer_presumptive_density": density(officer, "presumptive_hits"),
        "officer_confirmation_bias_density": density(officer, "confirmation_bias_hits"),
        "officer_one_sided_density": density(officer, "one_sided_hits"),
    }


def save_bias_csv(scores: list[SegmentScore], dest: Path) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# {HEADER}\n")
        w = csv.writer(f)
        w.writerow([
            "index", "start", "end", "speaker_role", "is_question",
            "word_count",
            "aggressive", "dehumanising", "presumptive",
            "confirmation_bias", "one_sided",
            "utterance", "human_verified",
        ])
        for s in scores:
            w.writerow([
                s.index, f"{s.start:.3f}", f"{s.end:.3f}",
                s.speaker_role, s.is_question, s.word_count,
                ";".join(s.aggressive_hits),
                ";".join(s.dehumanising_hits),
                ";".join(s.presumptive_hits),
                ";".join(s.confirmation_bias_hits),
                ";".join(s.one_sided_hits),
                s.text, "",
            ])
    return dest


def save_bias_summary(scores: list[SegmentScore], dest: Path) -> Path:
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "header": HEADER,
        "summary": summarise(scores),
        "interruptions": detect_interruptions(scores),
    }
    dest.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return dest


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--transcript", required=True)
    p.add_argument("--csv")
    p.add_argument("--summary")
    args = p.parse_args()
    data = json.loads(Path(args.transcript).read_text(encoding="utf-8"))
    scored = score_segments(data["segments"])
    if args.csv:
        save_bias_csv(scored, Path(args.csv))
    if args.summary:
        save_bias_summary(scored, Path(args.summary))
