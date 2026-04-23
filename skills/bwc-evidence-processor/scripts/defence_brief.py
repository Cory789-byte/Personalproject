"""Synthesise per-document defence analyses into a single DEFENCE_BRIEF.md.

Reads every `<record_id>.analysis.json` produced by `defence_analysis.py`,
aggregates the findings by charge, procedural rule, witness, and
asymmetric theme, and produces a structured Markdown brief for counsel.

The aggregation is deterministic (tables, rankings, counts) — the Claude
API call is used only for the *narrative* sections (case theory, theme
essays, cross-examination priorities), grounded in the aggregated
structured data so the model cannot invent facts.

Sections produced:
    1. Matter summary (counts, priorities, top witnesses)
    2. Aggregated key facts (chronology)
    3. Elements-undermined matrix (per charge)
    4. Procedural issues register (ranked)
    5. Credit points by witness (ranked by frequency × confidence)
    6. Asymmetric investigation — five themes, each with supporting docs
    7. Ranked cross-examination priorities (narrative, generated)
    8. Open questions and missing evidence (narrative, generated)

Run:
    python scripts/defence_brief.py \
        --analyses C:/Evidence/CO-25-2722/output/defence_analysis \
        --output   C:/Evidence/CO-25-2722/output/DEFENCE_BRIEF.md \
        --framework prompts/qld_defence_framework.md
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

HEADER = "MACHINE-GENERATED - UNVERIFIED"
MODEL = "claude-opus-4-7"
MAX_TOKENS = 16000

THEME_LABELS = {
    "activation": "Activation asymmetry (BWC / evidence-recording timing)",
    "power_use": "Power-use asymmetry (arrest, search, force, detention)",
    "charging": "Charging asymmetry (charges vs recorded conduct)",
    "witness": "Witness asymmetry (investigative effort distribution)",
    "recording": "Recording asymmetry (running sheets, property logs, radio)",
}

PRIORITY_WEIGHT = {"H": 3, "M": 2, "L": 1}
CONFIDENCE_WEIGHT = {"high": 3, "medium": 2, "low": 1}


def _load_analyses(analyses_dir: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for p in sorted(analyses_dir.glob("*.analysis.json")):
        try:
            out.append(json.loads(p.read_text(encoding="utf-8")))
        except Exception as e:
            print(f"  ! {p.name}: {e}", file=sys.stderr)
    return out


def _priority_score(record: dict[str, Any]) -> int:
    analysis = record.get("analysis", {}) or {}
    return PRIORITY_WEIGHT.get(analysis.get("priority", "L"), 1)


def _aggregate(records: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(records)
    priority_counts: Counter[str] = Counter()
    key_facts: list[tuple[str, str, str, str, str]] = []
    elements: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    procedural: list[dict[str, Any]] = []
    witnesses: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    themes: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)

    for rec in records:
        analysis = rec.get("analysis") or {}
        if not isinstance(analysis, dict):
            continue
        priority_counts[analysis.get("priority", "L")] += 1
        src = rec.get("drive_path") or rec.get("name") or rec.get("record_id", "")
        for kf in analysis.get("key_facts") or []:
            key_facts.append(
                (
                    kf.get("date", "") or "",
                    kf.get("fact", ""),
                    kf.get("citation", ""),
                    kf.get("confidence", "low"),
                    src,
                )
            )
        for el in analysis.get("elements_undermined") or []:
            elements[el.get("charge", "Unspecified charge")].append({**el, "source": src})
        for pi in analysis.get("procedural_issues") or []:
            procedural.append({**pi, "source": src})
        for cp in analysis.get("credit_points") or []:
            witnesses[cp.get("witness", "Unknown witness")].append({**cp, "source": src})
        for th in analysis.get("asymmetric_themes") or []:
            themes[th.get("theme", "")].append({**th, "source": src})

    key_facts.sort(key=lambda r: (r[0] or "9999-99-99", r[4]))

    proc_ranked = sorted(
        procedural,
        key=lambda p: -CONFIDENCE_WEIGHT.get(p.get("confidence", "low"), 1),
    )

    witness_ranked = sorted(
        (
            (
                w,
                items,
                sum(CONFIDENCE_WEIGHT.get(i.get("confidence", "low"), 1) for i in items),
            )
            for w, items in witnesses.items()
        ),
        key=lambda t: -t[2],
    )

    return {
        "total": total,
        "priority_counts": dict(priority_counts),
        "key_facts": key_facts,
        "elements": dict(elements),
        "procedural": proc_ranked,
        "witnesses": witness_ranked,
        "themes": {k: v for k, v in themes.items()},
    }


def _render_structured_markdown(agg: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# DEFENCE BRIEF — CO-25-2722")
    lines.append("")
    lines.append(f"> **{HEADER}.** This brief was produced by the defence pipeline from")
    lines.append("> disclosure documents and defence-side evidence. Every finding cites")
    lines.append("> the originating document. **Counsel must verify every citation**")
    lines.append("> against the primary source before relying on any item.")
    lines.append("")
    lines.append("## 1. Matter summary")
    lines.append("")
    pc = agg["priority_counts"]
    lines.append(f"- **Documents analysed:** {agg['total']}")
    lines.append(
        f"- **Priority distribution:** H={pc.get('H', 0)}, M={pc.get('M', 0)}, L={pc.get('L', 0)}"
    )
    lines.append(f"- **Witnesses surfaced:** {len(agg['witnesses'])}")
    lines.append(f"- **Procedural issues flagged:** {len(agg['procedural'])}")
    lines.append(f"- **Charges addressed:** {len(agg['elements'])}")
    lines.append("")
    lines.append("## 2. Chronology of key facts")
    lines.append("")
    lines.append("| Date | Fact | Citation | Confidence | Source |")
    lines.append("|------|------|----------|------------|--------|")
    for date, fact, citation, conf, src in agg["key_facts"][:500]:
        d = (date or "—").replace("|", "\\|")
        f = fact.replace("|", "\\|").replace("\n", " ")
        c = citation.replace("|", "\\|")
        s = src.replace("|", "\\|")
        lines.append(f"| {d} | {f} | {c} | {conf} | {s} |")
    if len(agg["key_facts"]) > 500:
        lines.append("")
        lines.append(f"*…{len(agg['key_facts']) - 500} further rows omitted; see per-doc analyses.*")
    lines.append("")
    lines.append("## 3. Elements undermined — matrix by charge")
    lines.append("")
    if not agg["elements"]:
        lines.append("*No charge-element undermining findings recorded.*")
    else:
        for charge, items in sorted(agg["elements"].items()):
            lines.append(f"### {charge}")
            lines.append("")
            lines.append("| Element | How undermined | Citation | Confidence | Source |")
            lines.append("|---------|----------------|----------|------------|--------|")
            for it in items:
                element = (it.get("element", "") or "").replace("|", "\\|")
                how = (it.get("how", "") or "").replace("|", "\\|").replace("\n", " ")
                cit = (it.get("citation", "") or "").replace("|", "\\|")
                conf = it.get("confidence", "low")
                src = (it.get("source", "") or "").replace("|", "\\|")
                lines.append(f"| {element} | {how} | {cit} | {conf} | {src} |")
            lines.append("")
    lines.append("## 4. Procedural issues register")
    lines.append("")
    lines.append("| Rule | Breach | Citation | Confidence | Source |")
    lines.append("|------|--------|----------|------------|--------|")
    for it in agg["procedural"]:
        rule = (it.get("rule", "") or "").replace("|", "\\|")
        breach = (it.get("breach", "") or "").replace("|", "\\|").replace("\n", " ")
        cit = (it.get("citation", "") or "").replace("|", "\\|")
        conf = it.get("confidence", "low")
        src = (it.get("source", "") or "").replace("|", "\\|")
        lines.append(f"| {rule} | {breach} | {cit} | {conf} | {src} |")
    lines.append("")
    lines.append("## 5. Credit points by witness")
    lines.append("")
    for witness, items, score in agg["witnesses"]:
        lines.append(f"### {witness} — weighted score {score}")
        lines.append("")
        lines.append("| Point | Citation | Confidence | Source |")
        lines.append("|-------|----------|------------|--------|")
        for it in items:
            point = (it.get("point", "") or "").replace("|", "\\|").replace("\n", " ")
            cit = (it.get("citation", "") or "").replace("|", "\\|")
            conf = it.get("confidence", "low")
            src = (it.get("source", "") or "").replace("|", "\\|")
            lines.append(f"| {point} | {cit} | {conf} | {src} |")
        lines.append("")
    lines.append("## 6. Asymmetric investigation — five themes")
    lines.append("")
    for theme_key, label in THEME_LABELS.items():
        items = agg["themes"].get(theme_key, [])
        lines.append(f"### {label}")
        lines.append("")
        if not items:
            lines.append("*No supporting documents found for this theme.*")
            lines.append("")
            continue
        for it in items:
            support = (it.get("support", "") or "").strip()
            cf = (it.get("counterfactual", "") or "").strip()
            conf = it.get("confidence", "low")
            src = it.get("source", "") or ""
            lines.append(f"- **Support:** {support}")
            lines.append(f"  - **Counterfactual (what should have happened):** {cf}")
            lines.append(f"  - **Confidence:** {conf} — **Source:** {src}")
        lines.append("")
    return "\n".join(lines)


def _narrative_prompt(agg: dict[str, Any]) -> str:
    """Condense the aggregate into a prompt Claude can reason over."""
    compact = {
        "totals": {
            "documents": agg["total"],
            "priority_counts": agg["priority_counts"],
        },
        "top_charges": {
            charge: [
                {k: v for k, v in it.items() if k in {"element", "how", "confidence", "source"}}
                for it in items[:20]
            ]
            for charge, items in agg["elements"].items()
        },
        "top_procedural": [
            {k: v for k, v in it.items() if k in {"rule", "breach", "confidence", "source"}}
            for it in agg["procedural"][:40]
        ],
        "top_witnesses": [
            {
                "witness": w,
                "score": score,
                "points": [
                    {k: v for k, v in it.items() if k in {"point", "confidence", "source"}}
                    for it in items[:15]
                ],
            }
            for w, items, score in agg["witnesses"][:10]
        ],
        "themes": {
            theme_key: [
                {
                    k: v
                    for k, v in it.items()
                    if k in {"support", "counterfactual", "confidence", "source"}
                }
                for it in agg["themes"].get(theme_key, [])[:25]
            ]
            for theme_key in THEME_LABELS
        },
    }
    return json.dumps(compact, ensure_ascii=False, indent=2)


def generate_narrative(framework: str, agg: dict[str, Any]) -> str:
    try:
        import anthropic  # type: ignore
    except ImportError:
        return (
            "> Narrative sections skipped — the `anthropic` package is not installed.\n"
            "> Run `pip install anthropic` and re-run with ANTHROPIC_API_KEY set."
        )

    client = anthropic.Anthropic()
    instruction = (
        "You are synthesising the aggregated defence findings into two narrative "
        "sections for the brief: (a) ranked cross-examination priorities grouped "
        "by witness, and (b) open questions and missing evidence.\n\n"
        "Ground every claim in the JSON summary provided. If the summary does not "
        "support a claim, do not make it. Use Markdown headings and bullet lists. "
        "Cite sources using the `source` field verbatim. Do not invent facts, "
        "dates, names, or citations. Do not give tactical or strategic advice — "
        "surface material only. Every section must carry the MACHINE-GENERATED - "
        "UNVERIFIED caveat.\n\n"
        "AGGREGATED FINDINGS (JSON):\n"
        f"{_narrative_prompt(agg)}"
    )

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        system=[
            {
                "type": "text",
                "text": framework,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": instruction}],
    )
    text = next((b.text for b in response.content if b.type == "text"), "")
    return text


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Synthesise per-document defence analyses into DEFENCE_BRIEF.md"
    )
    parser.add_argument(
        "--analyses", required=True, help="Directory of *.analysis.json files"
    )
    parser.add_argument("--output", required=True, help="Output path for DEFENCE_BRIEF.md")
    parser.add_argument(
        "--framework",
        required=True,
        help="Path to prompts/qld_defence_framework.md (used for narrative synthesis)",
    )
    parser.add_argument(
        "--skip-narrative",
        action="store_true",
        help="Skip Claude-generated narrative sections (structured-only output)",
    )
    args = parser.parse_args()

    analyses_dir = Path(args.analyses).resolve()
    records = _load_analyses(analyses_dir)
    if not records:
        raise SystemExit(f"No *.analysis.json files found in {analyses_dir}")

    print(f"Loaded {len(records)} analyses")
    agg = _aggregate(records)
    structured = _render_structured_markdown(agg)

    if args.skip_narrative:
        narrative = "*Narrative synthesis skipped (--skip-narrative).*"
    elif not os.environ.get("ANTHROPIC_API_KEY"):
        narrative = "*Narrative synthesis skipped — ANTHROPIC_API_KEY not set.*"
    else:
        framework = Path(args.framework).read_text(encoding="utf-8")
        print("Generating narrative synthesis via Claude...")
        narrative = generate_narrative(framework, agg)

    full = (
        structured
        + "\n\n## 7. Ranked cross-examination priorities & open questions\n\n"
        + f"> **{HEADER}.** The following sections are Claude-synthesised and must "
        "be verified against §§2–6 before use.\n\n"
        + narrative
        + "\n"
    )

    out_path = Path(args.output).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(full, encoding="utf-8")
    print(f"Wrote {out_path} ({len(full):,} chars)")


if __name__ == "__main__":
    main()
