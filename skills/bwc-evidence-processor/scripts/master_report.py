"""Render a single human-readable master report in Markdown.

Consolidates: integrity, compliance findings, bias summary, matrix highlights,
contradictions, and a table of flagged passages.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

HEADER = "MACHINE-GENERATED - UNVERIFIED"


def _read_csv(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    text = path.read_text().splitlines()
    if text and text[0].startswith("#"):
        text = text[1:]
    return list(csv.DictReader(text))


def render(
    out_dir: Path,
    stem: str,
    source_name: str,
) -> Path:
    out_dir = Path(out_dir)
    dest = out_dir / f"{stem}.master_report.md"

    integrity_path = out_dir / f"{stem}.integrity.json"
    bias_summary_path = out_dir / f"{stem}.bias_summary.json"
    compliance_path = out_dir / f"{stem}.compliance.csv"
    matrix_path = out_dir / f"{stem}.evidence_matrix.csv"
    contradictions_path = out_dir / f"{stem}.contradictions.csv"

    lines: list[str] = [
        f"# Master Evidence Analysis - {source_name}",
        "",
        f"> **{HEADER}** — investigative aide only. Every finding must be",
        "> verified by counsel before any forensic, procedural, or tactical",
        "> use. Nothing below is a legal conclusion.",
        "",
        "## 1. File integrity",
        "",
    ]

    if integrity_path.is_file():
        integ = json.loads(integrity_path.read_text())
        fmt = integ.get("format", {})
        lines += [
            f"- SHA-256: `{integ.get('sha256', '')}`",
            f"- Container: {fmt.get('format_long_name', fmt.get('format_name', ''))}",
            f"- Duration (container): {fmt.get('duration', '')} s",
            f"- Size: {fmt.get('size', '')} bytes",
            f"- Scene cuts detected: {len(integ.get('scene_cuts', []))}",
            f"- Black frame intervals: {len(integ.get('black_frames', []))}",
            f"- Freeze intervals: {len(integ.get('freeze_frames', []))}",
        ]
        anomalies = integ.get("anomalies") or []
        if anomalies:
            lines.append("- Anomaly flags:")
            for a in anomalies:
                lines.append(f"  - {a}")
        lines.append("")
    else:
        lines.append("_Integrity report not produced._\n")

    lines += ["## 2. Procedural compliance findings", ""]
    compliance = _read_csv(compliance_path)
    if compliance:
        by_sev = {"critical": [], "high": [], "medium": [], "low": []}
        for r in compliance:
            by_sev.setdefault(r.get("severity", "low"), []).append(r)
        for sev in ("critical", "high", "medium", "low"):
            rows = by_sev.get(sev) or []
            if not rows:
                continue
            lines.append(f"### {sev.upper()} ({len(rows)})")
            lines.append("")
            lines.append("| Time | Category | Detail |")
            lines.append("|------|----------|--------|")
            for r in rows:
                detail = (r.get("detail") or "").replace("|", "\\|")
                cat = r.get("category", "")
                lines.append(f"| {r.get('timestamp_hms','')} | {cat} | {detail} |")
            lines.append("")
    else:
        lines.append("_No compliance findings recorded._\n")

    lines += ["## 3. Bias and power dynamics", ""]
    if bias_summary_path.is_file():
        bs = json.loads(bias_summary_path.read_text())
        summary = bs.get("summary", {})
        interruptions = bs.get("interruptions", [])
        lines.append("| Metric | Value |")
        lines.append("|--------|-------|")
        for k, v in summary.items():
            lines.append(f"| {k.replace('_', ' ')} | {v} |")
        lines.append("")
        lines.append(f"- Interruptions detected: **{len(interruptions)}**")
        if interruptions:
            lines.append("")
            lines.append("| At | By | Over | Overlap (s) | Interrupter text |")
            lines.append("|----|----|------|-------------|------------------|")
            for it in interruptions[:40]:
                text = (it.get("interrupter_text") or "").replace("|", "\\|")
                lines.append(
                    f"| {it['at']:.2f} | {it['by_role']} | {it['over_role']} | "
                    f"{it['overlap_seconds']} | {text} |"
                )
        lines.append("")
    else:
        lines.append("_Bias summary not produced._\n")

    lines += ["## 4. Evidence matrix highlights", ""]
    matrix = _read_csv(matrix_path)
    if matrix:
        lines.append(f"Total flagged utterances: **{len(matrix)}**")
        lines.append("")
        lines.append("| Time | Category | Matter ref | Utterance |")
        lines.append("|------|----------|------------|-----------|")
        for r in matrix[:80]:
            ut = (r.get("utterance") or "").replace("|", "\\|")
            lines.append(
                f"| {r.get('timestamp_hms','')} | {r.get('category','')} | "
                f"{r.get('matter_ref','')} | {ut} |"
            )
        lines.append("")
    else:
        lines.append("_No matrix rows recorded._\n")

    lines += ["## 5. Contradictions vs. sworn corpus", ""]
    contras = _read_csv(contradictions_path)
    if contras:
        lines.append("| Time | Similarity | Transcript | Sworn excerpt |")
        lines.append("|------|------------|------------|----------------|")
        for r in contras[:60]:
            t = (r.get("transcript_utterance") or "").replace("|", "\\|")
            s = (r.get("sworn_statement_excerpt") or "").replace("|", "\\|")
            lines.append(
                f"| {r.get('start','')} | {r.get('similarity','')} | {t} | {s} |"
            )
        lines.append("")
    else:
        lines.append("_No contradictions register produced._\n")

    lines += [
        "---",
        "",
        "### Verification checklist",
        "",
        "- [ ] SHA-256 matches hash on disclosure receipt",
        "- [ ] Container duration matches the real-time elapsed footage",
        "- [ ] Scene cuts correspond to visible camera/recorder changes, not edits",
        "- [ ] Each CRITICAL compliance flag confirmed against footage",
        "- [ ] Each inducement flag reviewed for context (tone, pause, response)",
        "- [ ] Each contradiction compared against the full sworn statement",
        "- [ ] Officer/subject role inferences corrected where wrong",
        "- [ ] Low-confidence words (see word_review.csv) relistened to",
        "- [ ] All matrix rows signed-off in `human_verified` column",
        "",
    ]

    dest.write_text("\n".join(lines) + "\n")
    return dest
