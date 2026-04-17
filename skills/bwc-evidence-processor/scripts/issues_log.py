"""Master issues log.

Consolidates every flag from every analyzer into a single, timestamped,
verifiable register. Each row is a single issue with:

  - exhibit
  - start_seconds, end_seconds
  - timestamp_hms  (within-video)
  - absolute_datetime  (if integrity creation_time available)
  - severity
  - kind          which analyzer raised it
  - category / detail
  - evidence (utterance / statement excerpt)
  - video_path    absolute path to the source file
  - vlc_command   ready-to-paste VLC seek command
  - ffplay_command ready-to-paste ffplay seek command
  - explorer_uri  file:// URI you can paste into Explorer
  - human_verified (empty)
  - notes (empty)

Sort: severity (critical first) then absolute time.

Outputs:
  ISSUES_LOG.csv   - importable spreadsheet
  ISSUES_LOG.md    - readable with one heading per issue
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path


HEADER = "MACHINE-GENERATED - UNVERIFIED"

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "": 4}


@dataclass
class Issue:
    exhibit: str
    start_seconds: float
    end_seconds: float
    severity: str
    kind: str
    category: str
    detail: str
    evidence: str
    counter_evidence: str = ""


def _load_json(p: Path) -> dict | None:
    if not p.is_file():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return None


def _read_csv(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if text and text[0].startswith("#"):
        text = text[1:]
    return list(csv.DictReader(text))


def _hms_to_seconds(hms: str) -> float:
    if not hms:
        return 0.0
    m = re.match(r"^(\d+):([0-5]?\d):([0-5]?\d(?:\.\d+)?)$", hms.strip())
    if m:
        h, mi, s = m.groups()
        return int(h) * 3600 + int(mi) * 60 + float(s)
    try:
        return float(hms)
    except Exception:
        return 0.0


def _hms(s: float) -> str:
    s_int = int(s)
    h, rem = divmod(s_int, 3600)
    m, sec = divmod(rem, 60)
    ms = int((s - s_int) * 1000)
    return f"{h:02d}:{m:02d}:{sec:02d}.{ms:03d}"


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


def _load_integrity(output_dir: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for p in sorted(output_dir.glob("*.integrity.json")):
        d = _load_json(p) or {}
        out[p.stem.removesuffix(".integrity")] = d
    return out


def _load_source_paths(source_dir: Path) -> dict[str, Path]:
    """Map stem -> absolute source file."""
    out: dict[str, Path] = {}
    if not source_dir.is_dir():
        return out
    for p in source_dir.rglob("*"):
        if p.is_file() and p.suffix.lower() in {
            ".mp4", ".mov", ".mkv", ".avi", ".webm",
            ".wav", ".mp3", ".m4a",
        }:
            out[p.stem] = p.resolve()
    return out


def _collect(output_dir: Path) -> list[Issue]:
    issues: list[Issue] = []

    # 1. Per-exhibit compliance CSVs
    for p in sorted(output_dir.glob("*.compliance.csv")):
        exhibit = p.stem.removesuffix(".compliance")
        for r in _read_csv(p):
            issues.append(Issue(
                exhibit=exhibit,
                start_seconds=float(r.get("start") or 0),
                end_seconds=float(r.get("end") or 0),
                severity=r.get("severity", "").lower(),
                kind="procedural_compliance",
                category=r.get("category", ""),
                detail=r.get("detail", ""),
                evidence=r.get("utterance", ""),
            ))

    # 2. Deep contradictions
    for r in _read_csv(output_dir / "DEEP_CONTRADICTIONS.csv"):
        exhibit = r.get("related_exhibit") or r.get("source") or "<matter>"
        issues.append(Issue(
            exhibit=exhibit,
            start_seconds=0.0, end_seconds=0.0,
            severity=r.get("severity", "").lower(),
            kind="deep_contradiction",
            category=r.get("kind", ""),
            detail=r.get("detail", ""),
            evidence=r.get("evidence", ""),
            counter_evidence=r.get("counter_evidence", ""),
        ))

    # 3. Competency findings
    for r in _read_csv(output_dir / "COMPETENCY_FINDINGS.csv"):
        start = _hms_to_seconds(r.get("timestamp", ""))
        issues.append(Issue(
            exhibit=r.get("exhibit", "<matter>"),
            start_seconds=start, end_seconds=start,
            severity=r.get("severity", "").lower(),
            kind="qps_competency",
            category=r.get("kind", ""),
            detail=r.get("detail", ""),
            evidence=r.get("utterance", ""),
        ))

    # 4. Integrity anomalies (from each integrity.json)
    for p in sorted(output_dir.glob("*.integrity.json")):
        data = _load_json(p) or {}
        stem = p.stem.removesuffix(".integrity")
        for a in data.get("anomalies") or []:
            issues.append(Issue(
                exhibit=stem,
                start_seconds=0.0, end_seconds=0.0,
                severity="medium",
                kind="integrity_anomaly",
                category="container",
                detail=str(a),
                evidence="",
            ))
        for t in data.get("scene_cuts") or []:
            issues.append(Issue(
                exhibit=stem,
                start_seconds=float(t),
                end_seconds=float(t),
                severity="medium",
                kind="integrity_anomaly",
                category="scene_cut",
                detail=f"Scene cut detected at {_hms(float(t))}",
                evidence="",
            ))
        for interval in data.get("black_frames") or []:
            if isinstance(interval, (list, tuple)) and len(interval) >= 2:
                s, d = float(interval[0]), float(interval[1])
                issues.append(Issue(
                    exhibit=stem,
                    start_seconds=s, end_seconds=s + d,
                    severity="high",
                    kind="integrity_anomaly",
                    category="black_frames",
                    detail=f"Black-frame interval {d:.2f}s at {_hms(s)}",
                    evidence="",
                ))
        for interval in data.get("freeze_frames") or []:
            if isinstance(interval, (list, tuple)) and len(interval) >= 2:
                s, d = float(interval[0]), float(interval[1])
                issues.append(Issue(
                    exhibit=stem,
                    start_seconds=s, end_seconds=s + d,
                    severity="high",
                    kind="integrity_anomaly",
                    category="freeze_frames",
                    detail=f"Freeze interval {d:.2f}s at {_hms(s)}",
                    evidence="",
                ))

    # 5. Validation FAIL / WARN rows
    for r in _read_csv(output_dir / "VALIDATION_REPORT.csv"):
        if r.get("status", "").upper() in ("FAIL", "WARN"):
            issues.append(Issue(
                exhibit=r.get("exhibit", "<matter>"),
                start_seconds=0.0, end_seconds=0.0,
                severity="critical" if r.get("status", "").upper() == "FAIL" else "medium",
                kind="validation",
                category=r.get("target", ""),
                detail=r.get("detail", ""),
                evidence="",
            ))

    return issues


def _seek_commands(video: Path | None, start: float) -> tuple[str, str, str]:
    """Return (vlc, ffplay, explorer_uri) for a given source + seek time."""
    if video is None:
        return "", "", ""
    v = str(video).replace("\\", "/")
    ts = max(0.0, float(start))
    vlc = f'vlc --start-time={ts:.3f} "{video}"'
    ffplay = f'ffplay -ss {ts:.3f} -autoexit "{video}"'
    explorer = f"file:///{v}"
    return vlc, ffplay, explorer


def build(matter_root: Path) -> tuple[Path, Path]:
    matter_root = Path(matter_root).resolve()
    output_dir = matter_root / "output"
    source_dir = matter_root / "source"
    integrity = _load_integrity(output_dir)
    sources = _load_source_paths(source_dir)
    issues = _collect(output_dir)

    # Apply suppressions from corrections.json if present
    try:
        import sys as _sys
        _sys.path.insert(0, str(Path(__file__).resolve().parent))
        from corrections import MatterCorrections  # type: ignore
        mc = MatterCorrections.load(matter_root)
        before = len(issues)
        issues = [
            i for i in issues
            if not mc.is_suppressed(
                i.exhibit, i.kind, i.category, _hms(i.start_seconds)
            )
        ]
        suppressed = before - len(issues)
        if suppressed:
            print(f"   {suppressed} issues suppressed by corrections.json")
    except Exception:
        pass

    # Sort by severity then absolute time
    def sort_key(i: Issue):
        integ = integrity.get(i.exhibit) or {}
        tags = (integ.get("format") or {}).get("tags") or {}
        base = _parse_creation(tags.get("creation_time", ""))
        abs_time = (base + timedelta(seconds=i.start_seconds)).timestamp() if base else i.start_seconds
        return (SEVERITY_ORDER.get(i.severity, 9), abs_time, i.exhibit)
    issues.sort(key=sort_key)

    csv_path = output_dir / "ISSUES_LOG.csv"
    md_path = output_dir / "ISSUES_LOG.md"

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        f.write(f"# {HEADER}\n")
        w = csv.writer(f)
        w.writerow([
            "row", "exhibit", "kind", "category", "severity",
            "start_seconds", "end_seconds",
            "timestamp_hms", "absolute_datetime",
            "detail", "evidence", "counter_evidence",
            "video_path",
            "vlc_command", "ffplay_command", "explorer_uri",
            "notes", "human_verified",
        ])
        for n, i in enumerate(issues, 1):
            integ = integrity.get(i.exhibit) or {}
            tags = (integ.get("format") or {}).get("tags") or {}
            base = _parse_creation(tags.get("creation_time", ""))
            abs_dt = (base + timedelta(seconds=i.start_seconds)).isoformat() if base else ""
            vpath = sources.get(i.exhibit)
            vlc, ffplay, exp = _seek_commands(vpath, i.start_seconds)
            w.writerow([
                n, i.exhibit, i.kind, i.category, i.severity,
                f"{i.start_seconds:.3f}", f"{i.end_seconds:.3f}",
                _hms(i.start_seconds), abs_dt,
                i.detail, i.evidence, i.counter_evidence,
                str(vpath) if vpath else "",
                vlc, ffplay, exp,
                "", "",
            ])

    # MD view grouped by severity
    by_sev: dict[str, list[Issue]] = defaultdict(list)
    for i in issues:
        by_sev[i.severity or "low"].append(i)

    md_lines: list[str] = [
        "# Master Issues Log",
        "",
        f"> **{HEADER}**  -  Matter: `{matter_root}`",
        f"> Total issues: {len(issues)}  "
        f"(critical {len(by_sev.get('critical', []))}, "
        f"high {len(by_sev.get('high', []))}, "
        f"medium {len(by_sev.get('medium', []))}, "
        f"low {len(by_sev.get('low', []))}).",
        "",
        "Every row has a VLC / ffplay seek command you can paste into a",
        "shell to open the exact moment. Copy the command, paste, verify.",
        "",
    ]
    for sev in ("critical", "high", "medium", "low"):
        items = by_sev.get(sev) or []
        if not items:
            continue
        md_lines.append(f"## {sev.upper()}  ({len(items)})")
        md_lines.append("")
        for i in items:
            integ = integrity.get(i.exhibit) or {}
            tags = (integ.get("format") or {}).get("tags") or {}
            base = _parse_creation(tags.get("creation_time", ""))
            abs_dt = (base + timedelta(seconds=i.start_seconds)).strftime("%Y-%m-%d %H:%M:%S %Z").strip() if base else ""
            vpath = sources.get(i.exhibit)
            vlc, ffplay, exp = _seek_commands(vpath, i.start_seconds)
            md_lines.append(
                f"### {i.exhibit} at {_hms(i.start_seconds)}  -  "
                f"{i.kind} / {i.category}"
            )
            md_lines.append("")
            if abs_dt:
                md_lines.append(f"- **Absolute time**: {abs_dt}")
            md_lines.append(f"- **Severity**: {i.severity}")
            md_lines.append(f"- **Detail**: {i.detail}")
            if i.evidence:
                md_lines.append(f"- **Evidence**: _\"{i.evidence}\"_")
            if i.counter_evidence:
                md_lines.append(f"- **Counter**: _\"{i.counter_evidence}\"_")
            if vpath:
                md_lines.append(f"- **Video**: `{vpath}`")
                md_lines.append(f"- **Seek (VLC)**: `{vlc}`")
                md_lines.append(f"- **Seek (ffplay)**: `{ffplay}`")
                md_lines.append(f"- **File URI**: {exp}")
                md_lines.append(
                    f"- **Extract frame**: "
                    f"`python scripts\\frame_extract.py --video \"{vpath}\" "
                    f"--timestamp {i.start_seconds:.3f} --output "
                    f"output\\frames\\{i.exhibit}_{int(i.start_seconds)}.png --zoom 2 --ocr`"
                )
            md_lines.append("- **human_verified**:  ___  **notes**: ___")
            md_lines.append("")
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    return csv_path, md_path


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--matter-root", required=True)
    args = ap.parse_args()
    csvp, mdp = build(Path(args.matter_root))
    print(f"{csvp}")
    print(f"{mdp}")
