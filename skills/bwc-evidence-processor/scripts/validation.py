"""Post-processing validation / sanity pass.

Runs after the full pipeline. For each processed exhibit it confirms that:

  1. Every expected artefact file exists and is non-empty.
  2. Transcript JSON parses and contains at least one segment.
  3. Integrity JSON parses and carries a 64-char SHA-256.
  4. The SHA-256 on record still matches the source file on disk
     (chain-of-custody sanity check).
  5. CSVs have a header row + the expected columns.
  6. Master report mentions the expected machine-generated banner.
  7. Matter-wide files exist: MATTER_INDEX.md, CASE_THEORY.md,
     DEEP_CONTRADICTIONS.md, COMPETENCY_FINDINGS.md, sworn/corpus.txt.
  8. For every source media file, a master report exists (coverage).

Writes VALIDATION_REPORT.md + .csv with PASS / WARN / FAIL per exhibit.
Exit code non-zero on any FAIL so batch_process and CI can gate on it.
"""

from __future__ import annotations

import csv
import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path


HEADER = "MACHINE-GENERATED - UNVERIFIED"

PER_EXHIBIT_ARTEFACTS = [
    ".transcript.json",
    ".srt",
    ".vtt",
    ".evidence_matrix.csv",
    ".viewing_log.md",
    ".contradictions.csv",
    ".compliance.csv",
    ".bias.csv",
    ".bias_summary.json",
    ".word_review.csv",
    ".master_report.md",
    ".integrity.json",
]

MATTER_WIDE_ARTEFACTS = [
    "MATTER_INDEX.md",
    "CASE_THEORY.md",
    "DEEP_CONTRADICTIONS.md",
    "DEEP_CONTRADICTIONS.csv",
    "COMPETENCY_FINDINGS.md",
    "COMPETENCY_FINDINGS.csv",
]


@dataclass
class Check:
    target: str
    status: str   # PASS | WARN | FAIL
    detail: str = ""


@dataclass
class ExhibitValidation:
    exhibit: str
    source_path: str = ""
    source_present: bool = True
    checks: list[Check] = field(default_factory=list)

    @property
    def status(self) -> str:
        statuses = {c.status for c in self.checks}
        if "FAIL" in statuses:
            return "FAIL"
        if "WARN" in statuses:
            return "WARN"
        return "PASS"


def _sha256_of(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


def _csv_check(path: Path, expected_header_contains: list[str]) -> Check:
    if not path.is_file():
        return Check(path.name, "FAIL", "missing")
    if path.stat().st_size == 0:
        return Check(path.name, "FAIL", "empty")
    try:
        text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception as e:
        return Check(path.name, "FAIL", f"read error: {e}")
    if not text:
        return Check(path.name, "FAIL", "empty after strip")
    lines = text[1:] if text[0].startswith("#") else text
    if not lines:
        return Check(path.name, "FAIL", "no header row")
    header = lines[0].lower()
    missing = [h for h in expected_header_contains if h not in header]
    if missing:
        return Check(path.name, "FAIL", f"header missing columns: {missing}")
    return Check(path.name, "PASS", f"{len(lines) - 1} rows")


def _json_check(path: Path, require_keys: list[str]) -> Check:
    if not path.is_file():
        return Check(path.name, "FAIL", "missing")
    if path.stat().st_size == 0:
        return Check(path.name, "FAIL", "empty")
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except Exception as e:
        return Check(path.name, "FAIL", f"parse error: {e}")
    missing = [k for k in require_keys if k not in data]
    if missing:
        return Check(path.name, "FAIL", f"keys missing: {missing}")
    return Check(path.name, "PASS")


def _non_empty_check(path: Path) -> Check:
    if not path.is_file():
        return Check(path.name, "FAIL", "missing")
    if path.stat().st_size == 0:
        return Check(path.name, "FAIL", "empty")
    return Check(path.name, "PASS")


def validate_exhibit(stem: str, output_dir: Path, source_dir: Path) -> ExhibitValidation:
    v = ExhibitValidation(exhibit=stem)

    # Locate source file
    matches = list(source_dir.rglob(f"{stem}.*"))
    matches = [m for m in matches if m.is_file()
               and m.suffix.lower() in {
                   ".mp4", ".mov", ".mkv", ".avi", ".webm",
                   ".wav", ".mp3", ".m4a",
               }]
    if matches:
        v.source_path = str(matches[0])
    else:
        v.source_present = False
        v.checks.append(Check(
            "source media", "WARN",
            "source file not found for this exhibit",
        ))

    for ext in PER_EXHIBIT_ARTEFACTS:
        p = output_dir / f"{stem}{ext}"
        if ext == ".transcript.json":
            v.checks.append(_json_check(p, ["header", "segments"]))
            if p.is_file():
                try:
                    data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
                    segs = data.get("segments") or []
                    if not segs:
                        v.checks.append(Check(
                            p.name, "WARN",
                            "zero transcript segments (silent audio?)",
                        ))
                except Exception:
                    pass
        elif ext == ".integrity.json":
            v.checks.append(_json_check(p, ["header", "sha256", "source"]))
            if p.is_file() and matches:
                try:
                    data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
                    recorded = (data.get("sha256") or "").lower()
                    if len(recorded) != 64:
                        v.checks.append(Check(
                            p.name, "FAIL",
                            f"sha256 not 64 chars: {recorded!r}",
                        ))
                    else:
                        current = _sha256_of(matches[0])
                        if current != recorded:
                            v.checks.append(Check(
                                "chain_of_custody", "FAIL",
                                f"source SHA mismatch: on disk {current[:12]}... "
                                f"vs recorded {recorded[:12]}...",
                            ))
                        else:
                            v.checks.append(Check(
                                "chain_of_custody", "PASS",
                                f"sha256 matches ({recorded[:12]}...)",
                            ))
                except Exception as e:
                    v.checks.append(Check(
                        "chain_of_custody", "FAIL", f"hash recompute failed: {e}",
                    ))
        elif ext == ".bias_summary.json":
            v.checks.append(_json_check(p, ["header", "summary"]))
        elif ext.endswith(".csv"):
            expected = {
                ".evidence_matrix.csv": ["row", "timestamp_hms", "utterance"],
                ".contradictions.csv": ["row", "similarity"],
                ".compliance.csv": ["row", "category", "severity"],
                ".bias.csv": ["index", "speaker_role"],
                ".word_review.csv": ["row", "word", "confidence"],
            }
            v.checks.append(_csv_check(p, expected.get(ext, ["row"])))
        else:
            check = _non_empty_check(p)
            if ext == ".master_report.md" and check.status == "PASS":
                try:
                    text = p.read_text(encoding="utf-8", errors="replace")
                    if HEADER not in text:
                        v.checks.append(Check(
                            p.name, "FAIL",
                            "master_report missing 'MACHINE-GENERATED - UNVERIFIED'",
                        ))
                    else:
                        v.checks.append(check)
                except Exception:
                    v.checks.append(check)
            else:
                v.checks.append(check)
    return v


def validate_matter(matter_root: Path) -> dict:
    matter_root = Path(matter_root).resolve()
    source_dir = matter_root / "source"
    output_dir = matter_root / "output"

    exhibits: list[ExhibitValidation] = []
    master_reports = sorted(output_dir.glob("*.master_report.md"))
    for rep in master_reports:
        stem = rep.stem.removesuffix(".master_report")
        exhibits.append(validate_exhibit(stem, output_dir, source_dir))

    # Matter-wide artefacts
    wide_checks: list[Check] = []
    for name in MATTER_WIDE_ARTEFACTS:
        p = output_dir / name
        wide_checks.append(_non_empty_check(p))
    corpus = matter_root / "sworn" / "corpus.txt"
    wide_checks.append(_non_empty_check(corpus))

    # Coverage: every source media should have a master report
    source_media: list[Path] = []
    for p in source_dir.rglob("*") if source_dir.is_dir() else []:
        if p.is_file() and p.suffix.lower() in {
            ".mp4", ".mov", ".mkv", ".avi", ".webm",
            ".wav", ".mp3", ".m4a",
        }:
            source_media.append(p)
    processed_stems = {e.exhibit for e in exhibits}
    uncovered = [m for m in source_media if m.stem not in processed_stems]

    status_counts: dict[str, int] = {"PASS": 0, "WARN": 0, "FAIL": 0}
    for e in exhibits:
        status_counts[e.status] = status_counts.get(e.status, 0) + 1

    return {
        "matter_root": str(matter_root),
        "exhibits": exhibits,
        "matter_wide": wide_checks,
        "source_media_count": len(source_media),
        "uncovered": uncovered,
        "status_counts": status_counts,
        "overall": (
            "FAIL" if any(e.status == "FAIL" for e in exhibits)
            or any(w.status == "FAIL" for w in wide_checks)
            else "WARN" if any(e.status == "WARN" for e in exhibits)
            or any(w.status == "WARN" for w in wide_checks)
            or uncovered
            else "PASS"
        ),
    }


def save(report: dict, output_dir: Path) -> tuple[Path, Path]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "VALIDATION_REPORT.csv"
    md_path = output_dir / "VALIDATION_REPORT.md"

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# {HEADER}\n")
        w = csv.writer(f)
        w.writerow(["exhibit", "target", "status", "detail"])
        for e in report["exhibits"]:
            for c in e.checks:
                w.writerow([e.exhibit, c.target, c.status, c.detail])
        for c in report["matter_wide"]:
            w.writerow(["<matter>", c.target, c.status, c.detail])

    lines: list[str] = [
        "# Validation Report",
        "",
        f"> **{HEADER}**",
        f"> Matter: `{report['matter_root']}`",
        f"> Overall: **{report['overall']}**",
        "",
        "## Summary",
        "",
        f"- Exhibits processed: {sum(report['status_counts'].values())}",
        f"  - PASS: {report['status_counts'].get('PASS', 0)}",
        f"  - WARN: {report['status_counts'].get('WARN', 0)}",
        f"  - FAIL: {report['status_counts'].get('FAIL', 0)}",
        f"- Source media in total: {report['source_media_count']}",
        f"- Media not yet covered: {len(report['uncovered'])}",
        "",
        "## Matter-wide artefacts",
        "",
        "| Artefact | Status | Detail |",
        "|----------|--------|--------|",
    ]
    for c in report["matter_wide"]:
        lines.append(f"| {c.target} | {c.status} | {c.detail} |")
    lines += ["", "## Per-exhibit results", ""]
    lines += ["| Exhibit | Status | Failing / warning checks |",
              "|---------|--------|--------------------------|"]
    for e in report["exhibits"]:
        failing = [f"{c.target} ({c.status}: {c.detail})"
                   for c in e.checks if c.status != "PASS"]
        failing_str = "; ".join(failing).replace("|", "\\|") if failing else "-"
        lines.append(f"| {e.exhibit} | {e.status} | {failing_str} |")

    if report["uncovered"]:
        lines += ["", "## Source media not yet processed", ""]
        for m in report["uncovered"]:
            lines.append(f"- `{m.name}`")

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return csv_path, md_path


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--matter-root", required=True)
    args = ap.parse_args()
    report = validate_matter(Path(args.matter_root))
    out = Path(args.matter_root) / "output"
    save(report, out)
    print(f"Overall: {report['overall']}")
    print(f"  PASS={report['status_counts'].get('PASS', 0)} "
          f"WARN={report['status_counts'].get('WARN', 0)} "
          f"FAIL={report['status_counts'].get('FAIL', 0)}")
    return 0 if report["overall"] != "FAIL" else 1


if __name__ == "__main__":
    raise SystemExit(main())
