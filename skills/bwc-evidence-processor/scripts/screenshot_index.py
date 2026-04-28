"""Group per-screenshot analyses into a categorised SCREENSHOT_INDEX.md.

Reads every `<id>.screenshot.json` produced by `screenshot_analysis.py`,
aggregates by primary category, secondary tag, participant, and engaged
statute, and writes a Markdown index with one section per category. Each
row links the local file path so counsel can open the underlying image.

Pure aggregation — no Claude calls. Cheap to re-run as new screenshots
are added.

Run:
    python scripts/screenshot_index.py \
        --analyses C:/Evidence/CO-25-2722/output/screenshot_analysis \
        --output   C:/Evidence/CO-25-2722/output/SCREENSHOT_INDEX.md
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

HEADER = "MACHINE-GENERATED - UNVERIFIED"

CATEGORY_LABELS: dict[str, str] = {
    "comm.whatsapp": "WhatsApp messages and call logs",
    "comm.sms": "SMS / iMessage / RCS",
    "comm.email": "Email",
    "comm.dm": "Direct messages (Instagram / FB / X / etc.)",
    "comm.call_log": "Phone call logs and voicemail",
    "social.public": "Public social media posts",
    "social.story": "Ephemeral stories / status posts",
    "doc.court": "Court documents (orders, applications, affidavits)",
    "doc.legal": "Other legal documents",
    "doc.financial": "Financial documents",
    "doc.medical": "Medical records",
    "doc.gov": "Government documents",
    "scene.injury": "Photographs of injuries",
    "scene.property": "Photographs of damaged or interfered-with property",
    "scene.location": "Photographs of relevant locations",
    "web.news": "News articles / web pages",
    "web.profile": "Online profiles",
    "app.location": "Location / mapping app screenshots",
    "app.payment": "Payment-app screenshots",
    "meta.system": "Phone system info (settings, screen-time)",
    "unclear": "Could not be reliably categorised",
}

PRIORITY_RANK = {"H": 3, "M": 2, "L": 1}
CONFIDENCE_RANK = {"high": 3, "medium": 2, "low": 1}


def _load(analyses_dir: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for p in sorted(analyses_dir.glob("*.screenshot.json")):
        try:
            out.append(json.loads(p.read_text(encoding="utf-8")))
        except Exception as e:
            print(f"  ! {p.name}: {e}", file=sys.stderr)
    return out


def _md_escape(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def _by_category(records: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    out: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in records:
        cat = (r.get("analysis") or {}).get("primary_category", "unclear")
        out[cat].append(r)
    return dict(out)


def _earliest_timestamp(record: dict[str, Any]) -> str:
    times = (record.get("analysis") or {}).get("temporal") or []
    vals = [t.get("value", "") for t in times if t.get("value")]
    vals.sort()
    return vals[0] if vals else ""


def _participant_strings(record: dict[str, Any]) -> list[str]:
    parts = (record.get("analysis") or {}).get("participants") or []
    out: list[str] = []
    for p in parts:
        label = p.get("label", "") or ""
        ident = p.get("identifier", "") or ""
        if label and ident:
            out.append(f"{label} ({ident})")
        elif label:
            out.append(label)
        elif ident:
            out.append(ident)
    return out


def _statute_counter(records: list[dict[str, Any]]) -> Counter[str]:
    c: Counter[str] = Counter()
    for r in records:
        for s in (r.get("analysis") or {}).get("statutory_engagement") or []:
            cit = s.get("citation", "")
            if cit:
                c[cit] += 1
    return c


def _participant_counter(records: list[dict[str, Any]]) -> Counter[str]:
    c: Counter[str] = Counter()
    for r in records:
        for p in (r.get("analysis") or {}).get("participants") or []:
            label = p.get("label", "")
            if label:
                c[label] += 1
    return c


def _tag_counter(records: list[dict[str, Any]]) -> Counter[str]:
    c: Counter[str] = Counter()
    for r in records:
        for t in (r.get("analysis") or {}).get("secondary_tags") or []:
            c[t] += 1
    return c


def _row_priority(r: dict[str, Any]) -> int:
    return PRIORITY_RANK.get((r.get("analysis") or {}).get("priority", "L"), 1)


def render(records: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("# SCREENSHOT INDEX")
    lines.append("")
    lines.append(f"> **{HEADER}.** Counsel must verify every citation against the")
    lines.append("> screenshot itself before relying on any item.")
    lines.append("")

    total = len(records)
    parse_errors = sum(1 for r in records if r.get("parse_error"))
    auth_concerns = sum(
        1 for r in records if (r.get("analysis") or {}).get("authentication_concerns")
    )
    redaction_required = sum(
        1
        for r in records
        if any(
            (p.get("redaction_required"))
            for p in (r.get("analysis") or {}).get("participants") or []
        )
    )
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Screenshots indexed:** {total}")
    lines.append(f"- **Parse errors:** {parse_errors}")
    lines.append(f"- **Authentication concerns flagged:** {auth_concerns}")
    lines.append(f"- **Records requiring third-party redaction:** {redaction_required}")
    lines.append("")

    cats = _by_category(records)
    lines.append("## Category counts")
    lines.append("")
    lines.append("| Category | Count | Label |")
    lines.append("|----------|-------|-------|")
    for cat in sorted(cats, key=lambda c: -len(cats[c])):
        lines.append(
            f"| `{cat}` | {len(cats[cat])} | {CATEGORY_LABELS.get(cat, '—')} |"
        )
    lines.append("")

    stat = _statute_counter(records)
    lines.append("## Most-engaged statutes")
    lines.append("")
    lines.append("| Citation | Engagement count |")
    lines.append("|----------|------------------|")
    for cit, n in stat.most_common(40):
        lines.append(f"| {cit} | {n} |")
    lines.append("")

    parts = _participant_counter(records)
    lines.append("## Participants by frequency")
    lines.append("")
    lines.append("| Participant | Appearances |")
    lines.append("|-------------|-------------|")
    for p, n in parts.most_common(40):
        lines.append(f"| {_md_escape(p)} | {n} |")
    lines.append("")

    tags = _tag_counter(records)
    lines.append("## Secondary tag distribution")
    lines.append("")
    lines.append("| Tag | Count |")
    lines.append("|-----|-------|")
    for t, n in tags.most_common():
        lines.append(f"| `{t}` | {n} |")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## By category")
    lines.append("")
    for cat in sorted(cats, key=lambda c: -len(cats[c])):
        rows = sorted(
            cats[cat],
            key=lambda r: (-_row_priority(r), _earliest_timestamp(r) or "9999"),
        )
        lines.append(f"### `{cat}` — {CATEGORY_LABELS.get(cat, '—')} ({len(rows)})")
        lines.append("")
        lines.append("| File | Date | Participants | Priority | Tags | Statutes engaged | Authentication concerns |")
        lines.append("|------|------|--------------|----------|------|------------------|-------------------------|")
        for r in rows:
            analysis = r.get("analysis") or {}
            ts = _earliest_timestamp(r) or "—"
            partics = "; ".join(_participant_strings(r)) or "—"
            prio = analysis.get("priority", "L")
            tag_list = ", ".join(f"`{t}`" for t in analysis.get("secondary_tags", []))
            stats = "; ".join(
                s.get("citation", "") for s in analysis.get("statutory_engagement", [])
            )
            concerns = "; ".join(analysis.get("authentication_concerns", []))
            file_link = (
                f"[{_md_escape(r.get('drive_path', r.get('name', '')))}]"
                f"({Path(r.get('local_path', '')).as_posix()})"
            )
            lines.append(
                "| {fn} | {ts} | {parts} | {prio} | {tags} | {stats} | {auth} |".format(
                    fn=file_link,
                    ts=_md_escape(ts),
                    parts=_md_escape(partics),
                    prio=prio,
                    tags=tag_list,
                    stats=_md_escape(stats),
                    auth=_md_escape(concerns),
                )
            )
        lines.append("")
        lines.append(f"<details><summary>Per-screenshot detail ({len(rows)})</summary>")
        lines.append("")
        for r in rows:
            analysis = r.get("analysis") or {}
            lines.append(f"#### `{r.get('record_id', '?')}` — {_md_escape(r.get('name', ''))}")
            lines.append("")
            lines.append(f"- **Path:** `{r.get('local_path', '')}`")
            lines.append(f"- **Priority:** {analysis.get('priority', 'L')}")
            lines.append(
                f"- **Source:** {_md_escape((analysis.get('source_detection') or {}).get('platform', ''))}"
            )
            partics = analysis.get("participants") or []
            if partics:
                lines.append("- **Participants:**")
                for p in partics:
                    redact = " — REDACTION REQUIRED" if p.get("redaction_required") else ""
                    lines.append(
                        f"  - {_md_escape(p.get('label', ''))} "
                        f"({_md_escape(p.get('identifier', ''))})"
                        f"{redact}"
                    )
            transcript = analysis.get("content_transcript") or []
            if transcript:
                lines.append("- **Transcript:**")
                for t in transcript:
                    speaker = t.get("speaker", "") or "—"
                    txt = (t.get("text", "") or "").strip()
                    ts = t.get("timestamp", "") or ""
                    lines.append(f"  - **{_md_escape(speaker)}**"
                                 f"{f' [{_md_escape(ts)}]' if ts else ''}: {_md_escape(txt)}")
            stats = analysis.get("statutory_engagement") or []
            if stats:
                lines.append("- **Statutory engagement:**")
                for s in stats:
                    lines.append(
                        f"  - **{_md_escape(s.get('citation', ''))}** "
                        f"({_md_escape(s.get('interpretive_step', ''))}, "
                        f"{s.get('confidence', 'low')}): "
                        f"{_md_escape(s.get('element_engaged', ''))} — "
                        f"{_md_escape(s.get('interpretive_reasoning', ''))}"
                    )
                    if s.get("alternative_construction"):
                        lines.append(
                            f"    - *Alternative:* {_md_escape(s.get('alternative_construction', ''))}"
                        )
            ac = analysis.get("authentication_concerns") or []
            if ac:
                lines.append("- **Authentication concerns:**")
                for c in ac:
                    lines.append(f"  - {_md_escape(c)}")
            pp = analysis.get("privilege_publication_concerns") or []
            if pp:
                lines.append("- **Privilege / publication concerns:**")
                for c in pp:
                    lines.append(f"  - {_md_escape(c)}")
            notes = (analysis.get("notes") or "").strip()
            if notes:
                lines.append(f"- **Notes:** {_md_escape(notes)}")
            lines.append("")
        lines.append("</details>")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Group per-screenshot analyses into SCREENSHOT_INDEX.md"
    )
    parser.add_argument("--analyses", required=True, help="Directory of *.screenshot.json files")
    parser.add_argument("--output", required=True, help="Output path for SCREENSHOT_INDEX.md")
    args = parser.parse_args()

    analyses_dir = Path(args.analyses).resolve()
    records = _load(analyses_dir)
    if not records:
        raise SystemExit(f"No *.screenshot.json files found in {analyses_dir}")
    print(f"Loaded {len(records)} records")

    out = render(records)
    out_path = Path(args.output).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out, encoding="utf-8")
    print(f"Wrote {out_path} ({len(out):,} chars)")


if __name__ == "__main__":
    main()
