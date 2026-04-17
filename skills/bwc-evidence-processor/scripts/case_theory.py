"""Case theory synthesizer.

Reads every artefact already produced for a matter and emits a single
CASE_THEORY.md that aggregates the defence-relevant signal:

- Per-exhibit severity counts
- Critical / high procedural-compliance flags across ALL exhibits
- Interruption hotspots
- Inducement passages (promises / threats) with speaker role + timestamp
- Leading-question density by inferred officer role
- Contradictions vs sworn corpus, ranked by similarity
- Suggested cross-examination lines per flagged exhibit
- Unprocessed-file list (things still queued)

All output is stamped MACHINE-GENERATED - UNVERIFIED. This is a
preliminary synthesis - counsel must verify every item against the
underlying footage and sworn statements before use.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


HEADER = "MACHINE-GENERATED - UNVERIFIED"


@dataclass
class Finding:
    exhibit: str
    severity: str
    category: str
    timestamp: str
    utterance: str
    detail: str


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


def _collect_compliance(output_dir: Path) -> list[Finding]:
    out: list[Finding] = []
    for f in sorted(output_dir.glob("*.compliance.csv")):
        exhibit = f.stem.removesuffix(".compliance")
        for row in _read_csv(f):
            out.append(Finding(
                exhibit=exhibit,
                severity=row.get("severity", "low"),
                category=row.get("category", ""),
                timestamp=row.get("timestamp_hms", ""),
                utterance=row.get("utterance", ""),
                detail=row.get("detail", ""),
            ))
    return out


def _collect_bias(output_dir: Path) -> list[tuple[str, dict]]:
    summaries: list[tuple[str, dict]] = []
    for f in sorted(output_dir.glob("*.bias_summary.json")):
        exhibit = f.stem.removesuffix(".bias_summary")
        data = _load_json(f)
        if data:
            summaries.append((exhibit, data))
    return summaries


def _collect_matrix(output_dir: Path) -> dict[str, int]:
    categories: Counter[str] = Counter()
    for f in sorted(output_dir.glob("*.evidence_matrix.csv")):
        for row in _read_csv(f):
            categories[row.get("category", "")] += 1
    return dict(categories)


def _collect_contradictions(output_dir: Path) -> list[dict]:
    rows: list[dict] = []
    for f in sorted(output_dir.glob("*.contradictions.csv")):
        exhibit = f.stem.removesuffix(".contradictions")
        for row in _read_csv(f):
            row["_exhibit"] = exhibit
            rows.append(row)
    rows.sort(
        key=lambda r: float(r.get("similarity") or 0),
        reverse=True,
    )
    return rows


def _collect_processed_exhibits(output_dir: Path) -> set[str]:
    return {f.stem.removesuffix(".master_report") for f in output_dir.glob("*.master_report.md")}


def _collect_source_media(source_dir: Path) -> list[Path]:
    exts = {".mp4", ".mov", ".mkv", ".avi", ".webm", ".wav", ".mp3", ".m4a", ".flac"}
    return sorted(p for p in source_dir.rglob("*")
                  if p.is_file() and p.suffix.lower() in exts)


def _cross_ex_suggestions(findings: list[Finding]) -> list[str]:
    """Translate flag categories into concrete cross-examination prompts."""
    by_cat: dict[str, list[Finding]] = defaultdict(list)
    for f in findings:
        by_cat[f.category].append(f)
    suggestions: list[str] = []
    for cat, items in sorted(by_cat.items(), key=lambda kv: -len(kv[1])):
        ts = ", ".join(sorted({i.timestamp for i in items[:5] if i.timestamp}))
        sample_exhibits = ", ".join(sorted({i.exhibit for i in items[:3]}))
        line = None
        if cat == "missing_caution":
            line = (
                "At what point, if any, did you caution the subject? Take me to "
                f"the timestamps in the footage. ({sample_exhibits})"
            )
        elif cat == "late_caution":
            line = (
                f"You began questioning at {ts} but your caution came later. "
                "Do you accept any answers given before the caution cannot be "
                f"used against my client? ({sample_exhibits})"
            )
        elif cat == "missing_right_to_counsel":
            line = (
                "Did you at any stage advise my client of the right to contact "
                f"a lawyer, friend or relative? ({sample_exhibits})"
            )
        elif cat == "questioning_after_invocation":
            line = (
                f"After my client said [invocation] at {ts} you continued to "
                "ask questions. On what lawful basis did you continue? "
                f"({sample_exhibits})"
            )
        elif cat == "arrest_without_stated_grounds":
            line = (
                f"At {ts} you said my client was under arrest. You did not "
                "state the grounds. Do you accept PPRA s365 requires the "
                f"grounds be given at the time? ({sample_exhibits})"
            )
        elif cat == "search_without_warrant_or_consent":
            line = (
                f"At {ts} you announced a search. You did not produce a "
                "warrant, nor did my client consent in the surrounding "
                f"recording. What was the lawful power? ({sample_exhibits})"
            )
        elif cat == "possible_inducement":
            line = (
                f"At {ts} you said: \"{items[0].utterance}\". Do you accept a "
                "reasonable listener would take that as a promise or threat? "
                f"({sample_exhibits})"
            )
        elif cat == "leading_question":
            line = (
                "Several of your questions assume the answer. I take you to "
                f"{ts} - is that a question or a statement? ({sample_exhibits})"
            )
        if line:
            suggestions.append(f"- **{cat}** ({len(items)}×): {line}")
    return suggestions


def render(matter_root: Path) -> Path:
    matter_root = Path(matter_root).resolve()
    output_dir = matter_root / "output"
    source_dir = matter_root / "source"
    dest = output_dir / "CASE_THEORY.md"

    findings = _collect_compliance(output_dir)
    bias = _collect_bias(output_dir)
    matrix = _collect_matrix(output_dir)
    contradictions = _collect_contradictions(output_dir)
    processed = _collect_processed_exhibits(output_dir)
    all_media = _collect_source_media(source_dir)

    by_severity: Counter[str] = Counter(f.severity for f in findings)
    by_exhibit: dict[str, Counter[str]] = defaultdict(Counter)
    for f in findings:
        by_exhibit[f.exhibit][f.severity] += 1

    lines: list[str] = [
        "# Case Theory - Preliminary Synthesis",
        "",
        f"> **{HEADER}**  -  Matter root: `{matter_root}`",
        "> This is a preliminary synthesis from a partial run. Counsel must",
        "> verify every flag against the footage and sworn statements.",
        "",
        "## 1. Coverage",
        "",
        f"- Media files in `source/`: **{len(all_media)}**",
        f"- Exhibits with a master report: **{len(processed)}**",
        f"- Still to process: **{len(all_media) - len(processed)}**",
        "",
        "## 2. Aggregate procedural-compliance flags",
        "",
        f"- Critical: {by_severity.get('critical', 0)}",
        f"- High: {by_severity.get('high', 0)}",
        f"- Medium: {by_severity.get('medium', 0)}",
        f"- Low: {by_severity.get('low', 0)}",
        "",
        "### Per-exhibit rollup",
        "",
        "| Exhibit | Critical | High | Medium | Low |",
        "|---------|----------|------|--------|-----|",
    ]
    for ex, sev in sorted(by_exhibit.items()):
        lines.append(
            f"| {ex} | {sev.get('critical', 0)} | {sev.get('high', 0)} | "
            f"{sev.get('medium', 0)} | {sev.get('low', 0)} |"
        )
    lines += ["", "## 3. Critical / high findings (across all exhibits)", ""]
    if not any(f.severity in ("critical", "high") for f in findings):
        lines.append("_None recorded yet._")
    else:
        lines.append("| Severity | Exhibit | Time | Category | Detail |")
        lines.append("|----------|---------|------|----------|--------|")
        order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        for f in sorted(findings, key=lambda x: order.get(x.severity, 9)):
            if f.severity not in ("critical", "high"):
                continue
            detail = (f.detail or "").replace("|", "\\|")
            lines.append(
                f"| {f.severity} | {f.exhibit} | {f.timestamp} | "
                f"{f.category} | {detail} |"
            )

    lines += ["", "## 4. Power dynamics and interruptions", ""]
    if not bias:
        lines.append("_No bias summaries available._")
    else:
        lines.append("| Exhibit | Officer talk (s) | Subject talk (s) | "
                     "Officer Q-ratio | Interruptions |")
        lines.append("|---------|------------------|------------------|"
                     "-----------------|---------------|")
        for ex, data in bias:
            summary = data.get("summary", {})
            interruptions = data.get("interruptions", [])
            lines.append(
                f"| {ex} | {summary.get('officer_talk_seconds', 0)} | "
                f"{summary.get('subject_talk_seconds', 0)} | "
                f"{summary.get('officer_question_ratio', 0)} | "
                f"{len(interruptions)} |"
            )

    lines += ["", "## 5. Evidence matrix - category totals", ""]
    if not matrix:
        lines.append("_No matrix entries recorded yet._")
    else:
        for cat, n in sorted(matrix.items(), key=lambda kv: -kv[1]):
            lines.append(f"- `{cat}`: {n}")

    lines += ["", "## 6. Top contradictions vs sworn corpus", ""]
    high_contra = [
        c for c in contradictions
        if float(c.get("similarity") or 0) >= 60
    ][:25]
    if not high_contra:
        lines.append("_No contradictions scored >= 60 yet._")
    else:
        lines.append("| Exhibit | Time | Score | Transcript | Sworn excerpt |")
        lines.append("|---------|------|-------|------------|---------------|")
        for c in high_contra:
            t = (c.get("transcript_utterance") or "").replace("|", "\\|")
            s = (c.get("sworn_statement_excerpt") or "").replace("|", "\\|")
            lines.append(
                f"| {c['_exhibit']} | {c.get('start','')} | "
                f"{c.get('similarity','')} | {t} | {s} |"
            )

    lines += ["", "## 6b. Deep contradictions register", ""]
    deep_md = output_dir / "DEEP_CONTRADICTIONS.md"
    deep_csv = output_dir / "DEEP_CONTRADICTIONS.csv"
    if deep_csv.is_file():
        deep_rows = _read_csv(deep_csv)
        by_kind: Counter[str] = Counter(r.get("kind", "") for r in deep_rows)
        lines.append(f"Total deep findings: **{len(deep_rows)}**")
        for k in ("DATE_MISMATCH", "IDENTITY_VARIANT",
                  "PROCEDURAL_CLAIM_UNSUPPORTED", "SEQUENCE_MISMATCH"):
            lines.append(f"- {k}: {by_kind.get(k, 0)}")
        lines.append("")
        lines.append(f"Full register: [`DEEP_CONTRADICTIONS.md`]({deep_md.name})")
        lines.append("")
        # Show top 20 highest-severity rows inline
        sev_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        top = sorted(deep_rows, key=lambda r: sev_order.get(r.get("severity", "low"), 9))[:20]
        if top:
            lines.append("### Top deep findings")
            lines.append("")
            lines.append("| Severity | Kind | Source | Detail |")
            lines.append("|----------|------|--------|--------|")
            for r in top:
                detail = (r.get("detail") or "").replace("|", "\\|")
                lines.append(
                    f"| {r.get('severity','')} | {r.get('kind','')} | "
                    f"{r.get('source','')} | {detail} |"
                )
    else:
        lines.append("_No deep contradictions register yet - run `batch_process.py` "
                     "or `python scripts/deep_contradictions.py --output-dir <output>`._")

    lines += ["", "## 6c. QPS competency & decision-making findings", ""]
    comp_md = output_dir / "COMPETENCY_FINDINGS.md"
    comp_csv = output_dir / "COMPETENCY_FINDINGS.csv"
    if comp_csv.is_file():
        comp_rows = _read_csv(comp_csv)
        by_kind: Counter[str] = Counter(r.get("kind", "") for r in comp_rows)
        lines.append(f"Total competency findings: **{len(comp_rows)}**")
        for k in ("BWC_COMPLIANCE_GAP", "RUSH_TO_JUDGMENT", "ESCALATION_FAILURE",
                  "IDENTITY_MIX_UP", "MENTAL_HEALTH_UNCONSIDERED",
                  "CHARGE_CONFUSION", "DV_HANDLING_FAILURE",
                  "CONTRADICTORY_OFFICERS", "IGNORED_EXCULPATION",
                  "SUPERVISOR_ABSENT", "UNCERTAINTY"):
            n = by_kind.get(k, 0)
            if n:
                lines.append(f"- {k}: {n}")
        lines.append("")
        lines.append(f"Full register: [`COMPETENCY_FINDINGS.md`]({comp_md.name})")
        lines.append("")
        sev_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        top = sorted(comp_rows, key=lambda r: sev_order.get(r.get("severity", "low"), 9))[:15]
        if top:
            lines.append("### Top competency findings")
            lines.append("")
            lines.append("| Severity | Kind | Exhibit | Time | Detail |")
            lines.append("|----------|------|---------|------|--------|")
            for r in top:
                detail = (r.get("detail") or "").replace("|", "\\|")
                lines.append(
                    f"| {r.get('severity','')} | {r.get('kind','')} | "
                    f"{r.get('exhibit','')} | {r.get('timestamp','')} | {detail} |"
                )
    else:
        lines.append("_No competency findings register yet - run batch_process.py._")

    lines += ["", "## 6d. Cross-officer triangulation + tampering tally", ""]
    tri_md = output_dir / "TRIANGULATION.md"
    tamper_md = output_dir / "TAMPERING_TALLY.md"
    if tri_md.is_file():
        lines.append(f"Full event matrix: [`TRIANGULATION.md`]({tri_md.name})")
    if tamper_md.is_file():
        # Extract the totals header from TAMPERING_TALLY.md
        try:
            text = tamper_md.read_text(encoding="utf-8")
            m = re.search(r"Aggregate tampering score across all exhibits: \*\*(\d+)\*\*", text)
            if m:
                lines.append(f"Aggregate tampering score: **{m.group(1)}**")
        except Exception:
            pass
        lines.append(f"Per-camera tally: [`TAMPERING_TALLY.md`]({tamper_md.name})")
    if not (tri_md.is_file() or tamper_md.is_file()):
        lines.append("_Triangulation not yet run._")
    lines.append("")

    lines += ["", "## 7. Suggested cross-examination lines", ""]
    suggestions = _cross_ex_suggestions(findings)
    if not suggestions:
        lines.append("_None yet - no flagged categories with enough data._")
    else:
        lines.extend(suggestions)

    lines += ["", "## 8. Outstanding media", ""]
    outstanding = [m for m in all_media if m.stem not in processed]
    if not outstanding:
        lines.append("_All media in source/ processed._")
    else:
        total_mb = sum(m.stat().st_size for m in outstanding) / (1 << 20)
        lines.append(f"{len(outstanding)} files, ~{total_mb:,.0f} MB:")
        lines.append("")
        for m in outstanding:
            size_mb = m.stat().st_size / (1 << 20)
            lines.append(f"- `{m.name}` ({size_mb:.0f} MB)")

    lines += [
        "",
        "---",
        "",
        "### Verification checklist",
        "",
        "- [ ] Every CRITICAL flag watched against the footage",
        "- [ ] Every HIGH flag watched against the footage",
        "- [ ] False-positive flags on civilian-recorded video marked N/A",
        "- [ ] Top 10 contradictions compared against the *full* sworn statement",
        "- [ ] Officer / subject role inferences corrected on the bias CSV",
        "- [ ] Suggested cross-ex lines accepted / rejected / refined",
        "",
    ]
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return dest


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--matter-root", required=True)
    args = ap.parse_args()
    out = render(Path(args.matter_root))
    print(f"Case theory written to {out}")
