"""Phone-friendly summary of the matter findings.

Produces MOBILE_SUMMARY.md - a short (under 30 KB) plain-text summary
designed to read well on a phone screen. Strips tables, uses short
bullet lists, shows only CRITICAL / HIGH severity findings, and keeps
context tight.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


HEADER = "MACHINE-GENERATED - UNVERIFIED"


def _read_csv(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if text and text[0].startswith("#"):
        text = text[1:]
    return list(csv.DictReader(text))


def _truncate(text: str, n: int = 180) -> str:
    text = (text or "").replace("\n", " ").strip()
    return text if len(text) <= n else text[: n - 1] + "..."


def build(matter_root: Path) -> Path:
    matter_root = Path(matter_root).resolve()
    output_dir = matter_root / "output"
    dest = output_dir / "MOBILE_SUMMARY.md"

    # Count exhibits processed
    master_reports = list(output_dir.glob("*.master_report.md"))
    processed = len(master_reports)

    compliance = []
    for p in output_dir.glob("*.compliance.csv"):
        for r in _read_csv(p):
            r["_exhibit"] = p.stem.removesuffix(".compliance")
            compliance.append(r)
    critical_compliance = [r for r in compliance if r.get("severity") == "critical"]
    high_compliance = [r for r in compliance if r.get("severity") == "high"]

    competency = _read_csv(output_dir / "COMPETENCY_FINDINGS.csv")
    competency_crit = [r for r in competency if r.get("severity") == "critical"]
    competency_high = [r for r in competency if r.get("severity") == "high"]

    deep = _read_csv(output_dir / "DEEP_CONTRADICTIONS.csv")
    deep_crit = [r for r in deep if r.get("severity") == "critical"]
    deep_high = [r for r in deep if r.get("severity") == "high"]

    engagement = _read_csv(output_dir / "EVIDENCE_ENGAGEMENT.csv")
    ev_critical = [r for r in engagement if r.get("severity") == "critical"]
    ev_high = [r for r in engagement if r.get("severity") == "high"]

    tally_md = output_dir / "TAMPERING_TALLY.md"
    tampering_total = "unknown"
    top_cameras: list[str] = []
    if tally_md.is_file():
        text = tally_md.read_text(encoding="utf-8", errors="replace")
        import re as _re
        m = _re.search(r"Aggregate tampering score across all exhibits: \*\*(\d+)\*\*", text)
        if m:
            tampering_total = m.group(1)
        # Grab top 3 non-empty rows of per-camera table
        rows = [l for l in text.splitlines()
                if l.startswith("| ") and "**" in l]
        top_cameras = rows[:3]

    validation = _read_csv(output_dir / "VALIDATION_REPORT.csv")
    chain_fails = [r for r in validation
                   if r.get("target") == "chain_of_custody"
                   and r.get("status") == "FAIL"]

    lines: list[str] = [
        "# Matter Summary (mobile)",
        "",
        f"> {HEADER}",
        f"> Matter: {matter_root.name}",
        "",
        "## Coverage",
        "",
        f"- Exhibits processed: **{processed}**",
        f"- Chain-of-custody FAILs: **{len(chain_fails)}** "
        f"{'(review immediately)' if chain_fails else '(all PASS)'}",
        "",
        "## Severity snapshot",
        "",
        f"- Compliance (critical/high): **{len(critical_compliance)} / {len(high_compliance)}**",
        f"- Competency (critical/high): **{len(competency_crit)} / {len(competency_high)}**",
        f"- Deep contradictions (critical/high): **{len(deep_crit)} / {len(deep_high)}**",
        f"- Evidence engagement (critical/high): **{len(ev_critical)} / {len(ev_high)}**",
        f"- Aggregate tampering score: **{tampering_total}**",
        "",
    ]

    if critical_compliance:
        lines += ["## CRITICAL compliance flags", ""]
        for r in critical_compliance[:15]:
            lines.append(
                f"- {r.get('_exhibit', '')} @ {r.get('timestamp_hms', '')}"
                f" - {r.get('category', '')}: {_truncate(r.get('detail', ''))}"
            )
        if len(critical_compliance) > 15:
            lines.append(f"- ... and {len(critical_compliance) - 15} more")
        lines.append("")

    if ev_critical:
        lines += ["## CRITICAL evidence engagement", ""]
        for r in ev_critical[:15]:
            lines.append(
                f"- {r.get('exhibit', '')} @ {r.get('timestamp', '')}"
                f" - {r.get('kind', '')}: {_truncate(r.get('offered_text', ''))}"
            )
        lines.append("")

    if competency_crit:
        lines += ["## CRITICAL competency flags", ""]
        for r in competency_crit[:15]:
            lines.append(
                f"- {r.get('exhibit', '')} @ {r.get('timestamp', '')}"
                f" - {r.get('kind', '')}: {_truncate(r.get('detail', ''))}"
            )
        lines.append("")

    if top_cameras:
        lines += ["## Most-flagged cameras", ""]
        lines += top_cameras
        lines.append("")

    lines += [
        "---",
        "",
        "For detail see on phone via Google Drive:",
        "- CASE_THEORY.md",
        "- NARRATIVE_LOG.md",
        "- ISSUES_LOG.md",
        "- TAMPERING_TALLY.md",
        "- TRIANGULATION.md",
        "",
        "_All output is machine-generated. Counsel must verify._",
        "",
    ]
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return dest


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--matter-root", required=True)
    args = ap.parse_args()
    p = build(Path(args.matter_root))
    print(p)
