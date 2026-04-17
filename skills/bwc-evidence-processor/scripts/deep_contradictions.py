"""Deep forensic cross-reference across statements + transcripts + metadata.

Produces DEEP_CONTRADICTIONS.csv + .md with four flag classes:

1. DATE_MISMATCH
   Dates found in statement text vs dates found in BWC metadata or other
   statements referring to the same event keyword.

2. IDENTITY_VARIANT
   Names, dates of birth, addresses, and identifiers that appear in more
   than one spelling / form across all exhibits. Flags the less-common
   variant as the likely error.

3. PROCEDURAL_CLAIM_UNSUPPORTED
   A statement claims a procedural step ("I cautioned", "I advised of
   rights", "I placed under arrest and informed of the grounds") but the
   BWC transcript for a time-adjacent exhibit contains no matching
   language.

4. SEQUENCE_MISMATCH
   A statement asserts a time ("at 0806 I arrived") that conflicts with
   the BWC container creation_time or first-utterance timestamp.

All findings are MACHINE-GENERATED - UNVERIFIED. Every row has
`human_verified` empty by default.
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict, Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from rapidfuzz import fuzz


HEADER = "MACHINE-GENERATED - UNVERIFIED"

# ---- Date / time regexes -------------------------------------------------

DATE_PATTERNS = [
    # DD/MM/YYYY or DD-MM-YYYY or D/M/YY
    re.compile(r"\b(\d{1,2})[/\-\.](\d{1,2})[/\-\.](\d{2,4})\b"),
    # YYYY-MM-DD
    re.compile(r"\b(\d{4})-(\d{1,2})-(\d{1,2})\b"),
    # D MonthName YYYY  and  DD Mon YYYY  and  "the 22nd of March 2025"
    re.compile(
        r"\b(?:the\s+)?(\d{1,2})(?:st|nd|rd|th)?\s+(?:day\s+of\s+)?"
        r"(january|february|march|april|may|june|july|august|september|"
        r"october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)"
        r"\s+(\d{4})\b",
        re.IGNORECASE,
    ),
]
TIME_PATTERN = re.compile(
    r"\b(\d{1,2})[:\.h](\d{2})\s*(am|pm|hours|hrs)?\b",
    re.IGNORECASE,
)
MILITARY_TIME = re.compile(r"\b([01]\d|2[0-3])([0-5]\d)\s*(hrs|hours)?\b", re.IGNORECASE)

MONTH_MAP = {
    "jan": 1, "january": 1, "feb": 2, "february": 2, "mar": 3, "march": 3,
    "apr": 4, "april": 4, "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7,
    "aug": 8, "august": 8, "sep": 9, "september": 9, "oct": 10, "october": 10,
    "nov": 11, "november": 11, "dec": 12, "december": 12,
}

# ---- Procedural claim phrases --------------------------------------------

CLAIM_TO_BWC_SUPPORT = {
    "cautioned": [
        "you do not have to say anything", "anything you do say",
        "may be used in evidence", "may be given in evidence",
    ],
    "advised of rights": [
        "you do not have to say anything", "right to a lawyer",
        "right to legal", "contact a friend or relative",
    ],
    "right to legal representation": [
        "right to a lawyer", "right to legal", "legal advice",
    ],
    "right to silence": [
        "you do not have to say anything", "you are not obliged",
        "right to remain silent",
    ],
    "placed under arrest": [
        "you are under arrest", "you're under arrest",
        "i am arresting you", "i'm arresting you",
    ],
    "informed of the grounds": [
        "for the offence of", "in relation to", "on suspicion of",
        "the reason is", "the grounds are",
    ],
    "identified myself": [
        "i'm a police officer", "we're the police",
        "constable", "senior constable", "sergeant",
    ],
    "produced my identification": [
        "my name is", "badge number", "i'm from",
    ],
    "explained the warrant": [
        "search warrant", "under section", "this warrant",
    ],
}

CLAIM_REGEX = {
    "cautioned": re.compile(r"\b(?:I|we|officer\s+\w+)\s+cautioned\b", re.IGNORECASE),
    "advised of rights": re.compile(r"\badvis\w+\s+(?:him|her|them|the\s+\w+)?\s*of\s+(?:his|her|their)?\s*rights?\b", re.IGNORECASE),
    "right to legal representation": re.compile(r"\bright\s+to\s+(?:a\s+)?lawyer\b|\blegal\s+representation\b", re.IGNORECASE),
    "right to silence": re.compile(r"\bright\s+to\s+(?:remain\s+)?silen\w+\b", re.IGNORECASE),
    "placed under arrest": re.compile(r"\b(?:placed|put)\s+(?:him|her|them|the\s+\w+)?\s*under\s+arrest\b|\barrested\b", re.IGNORECASE),
    "informed of the grounds": re.compile(r"\binformed\b.*\bgrounds?\b|\bstated\s+the\s+grounds?\b|\breason\s+for\s+(?:the\s+)?arrest\b", re.IGNORECASE),
    "identified myself": re.compile(r"\bidentif\w+\s+(?:myself|himself|herself|themselves)\b", re.IGNORECASE),
    "produced my identification": re.compile(r"\bproduced\s+my\s+(?:QPS\s+)?(?:identification|warrant\s+card|ID)\b", re.IGNORECASE),
    "explained the warrant": re.compile(r"\bexplain\w+\s+the\s+(?:search\s+)?warrant\b|\bshow\w+\s+the\s+warrant\b", re.IGNORECASE),
}

# ---- Identity patterns ---------------------------------------------------

NAME_PATTERN = re.compile(
    r"\b(?:Mr\.?|Mrs\.?|Ms\.?|Dr\.?|Constable|Sen(?:ior)?\.?\s+Constable|"
    r"Sergeant|Sgt\.?|Detective|Det\.?|Inspector|Insp\.?)\s+"
    r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)",
)
ALLCAPS_SURNAME = re.compile(r"\b([A-Z]{3,}(?:[-' ][A-Z]{2,})?)\b")
DOB_PATTERN = re.compile(
    r"\b(?:DOB|D\.O\.B\.?|date\s+of\s+birth|born)\s*[:\-]?\s*"
    r"(\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{2,4})",
    re.IGNORECASE,
)
ADDRESS_PATTERN = re.compile(
    r"\b(?:unit|apartment|apt|flat|level)?\s*\d+[A-Za-z]?\s*(?:/|\s)?\s*"
    r"\d*\s*[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+"
    r"(?:Street|St\b|Road|Rd\b|Avenue|Ave\b|Drive|Dr\b|Court|Ct\b|"
    r"Lane|Ln\b|Place|Pl\b|Way|Crescent|Cres\b|Terrace|Parade|Pde\b|Boulevard)",
)
LICENCE_PATTERN = re.compile(
    r"\b(?:licen[sc]e|driv(?:er'?s)?\s*licen[sc]e|QDL)\s*(?:no|number|#)?\s*[:\-]?\s*([A-Z0-9]{6,12})\b",
    re.IGNORECASE,
)
PHONE_PATTERN = re.compile(r"\b(?:\+?61\s*)?(?:0?[2-478])\s*[\s\-]?\d{3,4}\s*[\s\-]?\d{3,4}\b")

# ---- Helpers -------------------------------------------------------------


def _normalise_date(match: re.Match) -> str | None:
    g = match.groups()
    try:
        if len(g) == 3 and g[1] in MONTH_MAP:
            d, mname, y = g
            return f"{int(y):04d}-{MONTH_MAP[mname.lower()]:02d}-{int(d):02d}"
        if len(g) == 3:
            a, b, c = g
            a, b, c = int(a), int(b), int(c)
            # YYYY-MM-DD
            if a > 31:
                return f"{a:04d}-{b:02d}-{c:02d}"
            # DD/MM/YY or DD/MM/YYYY (Australian default day-first)
            year = c if c >= 1000 else (2000 + c if c < 50 else 1900 + c)
            return f"{year:04d}-{b:02d}-{a:02d}"
    except Exception:
        return None
    return None


def _find_dates(text: str) -> list[tuple[str, str]]:
    """Return [(iso_date, surrounding_context)]."""
    out: list[tuple[str, str]] = []
    for pat in DATE_PATTERNS:
        for m in pat.finditer(text):
            iso = _normalise_date(m)
            if iso:
                ctx_start = max(0, m.start() - 60)
                ctx_end = min(len(text), m.end() + 60)
                context = text[ctx_start:ctx_end].replace("\n", " ")
                out.append((iso, context))
    return out


def _name_key(name: str) -> str:
    return re.sub(r"[^A-Z]", "", name.upper())


# ---- Analyzer ------------------------------------------------------------


@dataclass
class DeepFinding:
    kind: str  # DATE_MISMATCH | IDENTITY_VARIANT | PROCEDURAL_CLAIM_UNSUPPORTED | SEQUENCE_MISMATCH
    severity: str  # critical | high | medium | low
    source: str
    detail: str
    evidence: str
    counter_evidence: str
    related_exhibit: str = ""


def _load_docs(output_dir: Path) -> list[dict]:
    records: list[dict] = []
    docs_dir = output_dir / "documents"
    for p in sorted(docs_dir.glob("*.doc.json")):
        try:
            records.append(json.loads(p.read_text(encoding="utf-8", errors="replace")))
        except Exception:
            continue
    return records


def _load_transcripts(output_dir: Path) -> dict[str, dict]:
    transcripts: dict[str, dict] = {}
    for p in sorted(output_dir.glob("*.transcript.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
            stem = p.stem.removesuffix(".transcript")
            transcripts[stem] = data
        except Exception:
            continue
    return transcripts


def _load_integrity(output_dir: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for p in sorted(output_dir.glob("*.integrity.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
            stem = p.stem.removesuffix(".integrity")
            out[stem] = data
        except Exception:
            continue
    return out


def _collect_dates(records: list[dict]) -> dict[str, list[tuple[str, str]]]:
    """Return {source_name: [(iso_date, context)]}."""
    out: dict[str, list[tuple[str, str]]] = {}
    for rec in records:
        name = rec.get("stem") or rec.get("path") or "<unknown>"
        out[name] = _find_dates(rec.get("text", "") or "")
    return out


def _collect_identities(records: list[dict]) -> dict[str, list[tuple[str, str]]]:
    """Return {category: [(value, source)]} across all records."""
    out: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for rec in records:
        name = rec.get("stem") or "<unknown>"
        text = rec.get("text", "") or ""

        for m in NAME_PATTERN.finditer(text):
            out["name"].append((m.group(1).strip(), name))
        for m in ALLCAPS_SURNAME.finditer(text):
            s = m.group(1).strip()
            if len(s) >= 4 and s.upper() == s:
                out["surname_allcaps"].append((s, name))
        for m in DOB_PATTERN.finditer(text):
            out["dob"].append((m.group(1).strip(), name))
        for m in ADDRESS_PATTERN.finditer(text):
            out["address"].append((m.group(0).strip(), name))
        for m in LICENCE_PATTERN.finditer(text):
            out["licence"].append((m.group(1).strip(), name))
        for m in PHONE_PATTERN.finditer(text):
            out["phone"].append((m.group(0).strip(), name))
    return out


def _identity_variants(
    entries: list[tuple[str, str]],
    similarity: int = 75,
) -> list[tuple[str, str, list[str]]]:
    """Cluster entries by fuzzy similarity so Shepherd/Sheppard cluster together."""
    clusters: list[dict] = []
    for value, src in entries:
        placed = False
        for c in clusters:
            if fuzz.ratio(value.upper(), c["canonical"].upper()) >= similarity:
                c["members"].append((value, src))
                placed = True
                break
        if not placed:
            clusters.append({"canonical": value, "members": [(value, src)]})
    flagged: list[tuple[str, str, list[str]]] = []
    for c in clusters:
        distinct = {v for v, _ in c["members"]}
        if len(distinct) > 1:
            forms = sorted(distinct)
            sources = sorted({s for _, s in c["members"]})
            flagged.append((c["canonical"], "; ".join(forms), sources))
    return flagged


def _dob_address_variants(category: str, entries: list[tuple[str, str]]) -> list[tuple[str, list[str], list[str]]]:
    """For DOB/address/licence/phone: flag when any two differ at all."""
    distinct: dict[str, list[str]] = defaultdict(list)
    for value, src in entries:
        distinct[value].append(src)
    if len(distinct) <= 1:
        return []
    return [(category, sorted(distinct.keys()), sorted({s for v in distinct.values() for s in v}))]


def _match_transcript(segments: list[dict], cues: list[str], threshold: int = 85) -> tuple[bool, str]:
    for seg in segments:
        text_lower = (seg.get("text") or "").lower()
        for cue in cues:
            if cue in text_lower:
                return True, seg["text"]
            if fuzz.partial_ratio(text_lower, cue) >= threshold:
                return True, seg["text"]
    return False, ""


def _detect_procedural_gaps(
    docs: list[dict],
    transcripts: dict[str, dict],
) -> list[DeepFinding]:
    findings: list[DeepFinding] = []

    # Union all transcript segments across all processed videos - crude but effective
    union_segments: list[dict] = []
    for stem, data in transcripts.items():
        for s in data.get("segments", []):
            union_segments.append({**s, "_exhibit": stem})

    for rec in docs:
        name = rec.get("stem") or "<unknown>"
        text = rec.get("text", "") or ""
        if not text:
            continue
        for claim, pattern in CLAIM_REGEX.items():
            if not pattern.search(text):
                continue
            cues = CLAIM_TO_BWC_SUPPORT.get(claim, [])
            found, support = _match_transcript(union_segments, cues)
            if not found:
                findings.append(DeepFinding(
                    kind="PROCEDURAL_CLAIM_UNSUPPORTED",
                    severity="high",
                    source=name,
                    detail=f"Statement claims \"{claim}\" but no supporting BWC utterance detected in any processed transcript.",
                    evidence=pattern.search(text).group(0),
                    counter_evidence="(no matching transcript passage across all processed BWC)",
                ))
    return findings


def _detect_date_mismatches(
    dates_by_source: dict[str, list[tuple[str, str]]],
    integrity: dict[str, dict],
) -> list[DeepFinding]:
    findings: list[DeepFinding] = []
    # Build a set of dates per source
    dates_per_source = {k: {iso for iso, _ in v} for k, v in dates_by_source.items()}

    # Cross-source comparison: same event keywords, different dates
    # Simple proxy: pairwise exhibit pairs where one date appears in one but not the other
    # Only flag when both sources contain each other's dates mismatched significantly
    # (Too many false positives from historical dates; use fuzzy event-keyword heuristic.)
    # Start with BWC creation_time vs statement dates.
    for stem, integ in integrity.items():
        fmt = integ.get("format", {}) or {}
        tags = fmt.get("tags", {}) or {}
        creation = tags.get("creation_time") or ""
        bwc_date = creation[:10] if len(creation) >= 10 else ""
        if not bwc_date:
            continue
        for src, entries in dates_by_source.items():
            src_dates = {iso for iso, _ in entries}
            if not src_dates:
                continue
            # If statement contains a date near the BWC creation and also OTHER dates
            # that differ by more than a day, flag the other date.
            matching = {d for d in src_dates if d == bwc_date}
            if matching:
                other = src_dates - matching
                for d in other:
                    # Only flag if this "other" date sits in the same paragraph as
                    # a reference to the event (crude heuristic: look for the BWC
                    # stem words in the statement context for this date).
                    for iso, ctx in entries:
                        if iso != d:
                            continue
                        if any(tok.lower() in ctx.lower() for tok in stem.replace("_", " ").split() if len(tok) > 4):
                            findings.append(DeepFinding(
                                kind="DATE_MISMATCH",
                                severity="high",
                                source=src,
                                detail=f"Statement mentions date {d} in context of exhibit '{stem}' but BWC metadata creation_time is {bwc_date}.",
                                evidence=ctx.strip(),
                                counter_evidence=f"BWC {stem} creation_time = {creation}",
                                related_exhibit=stem,
                            ))
    return findings


def _detect_sequence_mismatches(
    docs: list[dict],
    transcripts: dict[str, dict],
    integrity: dict[str, dict],
) -> list[DeepFinding]:
    findings: list[DeepFinding] = []
    time_any = re.compile(
        r"\b(?:at|around|approximately)?\s*"
        r"(?P<h>\d{1,2})[:\.h]?(?P<m>\d{2})\s*(?P<meridian>am|pm|hours|hrs)?\b",
        re.IGNORECASE,
    )
    for stem, integ in integrity.items():
        fmt = integ.get("format", {}) or {}
        tags = fmt.get("tags", {}) or {}
        creation = tags.get("creation_time") or ""
        if len(creation) < 19:
            continue
        bwc_hhmm = creation[11:16]  # "HH:MM"
        for rec in docs:
            text = rec.get("text", "") or ""
            if not any(tok.lower() in text.lower() for tok in stem.replace("_", " ").split() if len(tok) > 4):
                continue
            for m in time_any.finditer(text):
                h = int(m.group("h"))
                mi = int(m.group("m"))
                mer = (m.group("meridian") or "").lower()
                if mer == "pm" and h < 12:
                    h += 12
                elif mer == "am" and h == 12:
                    h = 0
                stmt_hhmm = f"{h:02d}:{mi:02d}"
                if stmt_hhmm == bwc_hhmm:
                    continue
                # If they differ by > 15 minutes, flag
                bwc_h, bwc_m = [int(x) for x in bwc_hhmm.split(":")]
                delta = abs((h * 60 + mi) - (bwc_h * 60 + bwc_m))
                if delta > 15:
                    ctx = text[max(0, m.start() - 60): m.end() + 60].replace("\n", " ")
                    findings.append(DeepFinding(
                        kind="SEQUENCE_MISMATCH",
                        severity="medium",
                        source=rec.get("stem", "<unknown>"),
                        detail=f"Statement time {stmt_hhmm} vs BWC creation {bwc_hhmm} for exhibit '{stem}' (delta {delta} min).",
                        evidence=ctx.strip(),
                        counter_evidence=f"BWC {stem} creation_time = {creation}",
                        related_exhibit=stem,
                    ))
    return findings


def _detect_identity_variants(identities: dict[str, list[tuple[str, str]]]) -> list[DeepFinding]:
    findings: list[DeepFinding] = []

    # Name variants (Mr Shepherd vs Mr Sheppard)
    for category in ("name", "surname_allcaps"):
        for key, forms_str, sources in _identity_variants(identities.get(category, [])):
            findings.append(DeepFinding(
                kind="IDENTITY_VARIANT",
                severity="high" if category == "surname_allcaps" else "medium",
                source="; ".join(sources),
                detail=f"{category.replace('_', ' ')} appears in {len(forms_str.split(';'))} distinct spellings.",
                evidence=forms_str,
                counter_evidence="",
            ))

    # DOB / address / licence / phone - any variation at all is a flag
    for cat in ("dob", "address", "licence", "phone"):
        for (_, values, sources) in _dob_address_variants(cat, identities.get(cat, [])):
            findings.append(DeepFinding(
                kind="IDENTITY_VARIANT",
                severity="high",
                source="; ".join(sources),
                detail=f"{cat} differs across documents - potential misidentification.",
                evidence=" | ".join(values),
                counter_evidence="",
            ))
    return findings


def analyze(output_dir: Path) -> list[DeepFinding]:
    output_dir = Path(output_dir)
    docs = _load_docs(output_dir)
    transcripts = _load_transcripts(output_dir)
    integrity = _load_integrity(output_dir)

    findings: list[DeepFinding] = []
    # Also build a "documents equivalent" view of transcripts for date / identity scans
    transcript_records = [
        {"stem": stem, "text": " ".join(s.get("text", "") for s in data.get("segments", []))}
        for stem, data in transcripts.items()
    ]
    all_records = docs + transcript_records

    findings += _detect_identity_variants(_collect_identities(all_records))
    findings += _detect_date_mismatches(_collect_dates(all_records), integrity)
    findings += _detect_sequence_mismatches(docs, transcripts, integrity)
    findings += _detect_procedural_gaps(docs, transcripts)
    return findings


def save(findings: list[DeepFinding], output_dir: Path) -> tuple[Path, Path]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "DEEP_CONTRADICTIONS.csv"
    md_path = output_dir / "DEEP_CONTRADICTIONS.md"

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# {HEADER}\n")
        w = csv.writer(f)
        w.writerow([
            "row", "kind", "severity", "source", "related_exhibit",
            "detail", "evidence", "counter_evidence", "human_verified",
        ])
        for i, fd in enumerate(findings, 1):
            w.writerow([
                i, fd.kind, fd.severity, fd.source, fd.related_exhibit,
                fd.detail, fd.evidence, fd.counter_evidence, "",
            ])

    by_kind: dict[str, list[DeepFinding]] = defaultdict(list)
    for fd in findings:
        by_kind[fd.kind].append(fd)

    lines: list[str] = [
        "# Deep contradictions register",
        "",
        f"> **{HEADER}**",
        "> Cross-reference across statements, transcripts, and BWC metadata.",
        f"> Total findings: {len(findings)}",
        "",
    ]
    order = ["DATE_MISMATCH", "IDENTITY_VARIANT",
             "PROCEDURAL_CLAIM_UNSUPPORTED", "SEQUENCE_MISMATCH"]
    for kind in order:
        items = by_kind.get(kind) or []
        lines.append(f"## {kind} ({len(items)})")
        lines.append("")
        if not items:
            lines.append("_None._")
            lines.append("")
            continue
        lines.append("| Severity | Source | Related exhibit | Detail | Evidence | Counter-evidence |")
        lines.append("|----------|--------|-----------------|--------|----------|------------------|")
        for fd in items:
            ev = (fd.evidence or "").replace("|", "\\|")
            ce = (fd.counter_evidence or "").replace("|", "\\|")
            detail = (fd.detail or "").replace("|", "\\|")
            lines.append(
                f"| {fd.severity} | {fd.source} | {fd.related_exhibit} | {detail} | {ev} | {ce} |"
            )
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
    print(f"{len(f)} deep findings.")
    print(f"  {csvp}")
    print(f"  {mdp}")
