"""Feedback loop: extract human_verified corrections from CSVs and
fold them into the matter corrections + vocabulary files.

How to use:

  1. Open any of the CSVs under <matter_root>/output/ (ISSUES_LOG,
     COMPETENCY_FINDINGS, DEEP_CONTRADICTIONS, *.compliance.csv,
     *.bias.csv) in Excel or a text editor.
  2. In the human_verified column, write one of the following:
         true              row confirmed - no change
         false_positive    row is noise - suppress it next run
         role:OFFICER      (bias CSVs only) force OFFICER role for this segment
         role:SUBJECT      force SUBJECT role
         speaker:Const Easthope   label that speaker by name
         correct:"I cautioned"  -> "Caution delivered"
                           word or phrase correction to apply upstream
     Add the feedback to the "notes" column if you prefer - both
     columns are read.
  3. Save the CSV.
  4. Run:

        python scripts/learn.py --matter-root C:\\Evidence\\CO-25-2722

     The script reads every CSV, parses your feedback, updates
     <matter_root>/config/vocabulary.json and corrections.json, and
     prints a summary of what changed.

Next batch run: process_video.py picks up the vocabulary + corrections
automatically. Mishears get swapped, false positives get suppressed,
role overrides are applied. Each pass of feedback makes the pipeline
meaningfully sharper.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Iterator

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corrections import MatterCorrections  # noqa: E402


def _iter_csv(path: Path) -> Iterator[dict]:
    if not path.is_file():
        return iter(())
    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if text and text[0].startswith("#"):
        text = text[1:]
    return iter(csv.DictReader(text))


FEEDBACK_FIELDS = ("human_verified", "notes", "Human_Verified")


def _feedback(row: dict) -> list[str]:
    """Return every non-empty feedback string across accepted columns."""
    out: list[str] = []
    for fld in FEEDBACK_FIELDS:
        v = (row.get(fld) or "").strip()
        if v and v.lower() != "true":
            out.append(v)
    return out


def _apply_row_feedback(
    mc: MatterCorrections,
    exhibit: str,
    row: dict,
    kind_hint: str,
    counts: dict,
) -> None:
    for v in _feedback(row):
        low = v.lower().strip()
        if low in ("false_positive", "false positive", "fp", "noise"):
            rule = {"exhibit": exhibit}
            if row.get("category"):
                rule["category"] = row["category"]
            if row.get("kind"):
                rule["kind"] = row["kind"]
            elif kind_hint:
                rule["kind"] = kind_hint
            ts = row.get("timestamp") or row.get("timestamp_hms") or ""
            if ts:
                rule["timestamp"] = ts
            mc.add_suppression(**rule)
            counts["suppressions"] = counts.get("suppressions", 0) + 1
            continue

        m = re.match(r"^role\s*[:=]\s*(OFFICER|SUBJECT|UNKNOWN)\s*$", v, re.IGNORECASE)
        if m:
            idx_raw = row.get("index") or row.get("segment_index") or row.get("row")
            if not idx_raw:
                continue
            mc.add_role_override(exhibit, int(idx_raw), m.group(1).upper())
            counts["role_overrides"] = counts.get("role_overrides", 0) + 1
            continue

        m = re.match(r"^speaker\s*[:=]\s*(.+)$", v, re.IGNORECASE)
        if m:
            idx_raw = row.get("index") or row.get("segment_index") or row.get("row")
            if idx_raw:
                mc.add_speaker_label(exhibit, int(idx_raw), m.group(1).strip())
                counts["speaker_labels"] = counts.get("speaker_labels", 0) + 1
                mc.add_name(m.group(1).strip())
            continue

        # correct:"wrong" -> "right"   OR   correct: wrong -> right
        m = re.match(
            r"^correct\s*[:=]\s*\"?(.+?)\"?\s*(?:->|=>|to)\s*\"?(.+?)\"?$",
            v, re.IGNORECASE,
        )
        if m:
            mc.add_word_correction(m.group(1).strip(), m.group(2).strip())
            counts["word_corrections"] = counts.get("word_corrections", 0) + 1
            continue


def _exhibit_from_filename(path: Path, suffix: str) -> str:
    name = path.name
    if name.endswith(suffix):
        return name[: -len(suffix)]
    return path.stem


def run(matter_root: Path, dry_run: bool = False) -> dict:
    matter_root = Path(matter_root).resolve()
    output_dir = matter_root / "output"
    mc = MatterCorrections.load(matter_root)
    counts: dict = {}

    # Per-exhibit CSVs
    for p in sorted(output_dir.glob("*.compliance.csv")):
        exhibit = _exhibit_from_filename(p, ".compliance.csv")
        for row in _iter_csv(p):
            _apply_row_feedback(mc, exhibit, row, "procedural_compliance", counts)
    for p in sorted(output_dir.glob("*.bias.csv")):
        exhibit = _exhibit_from_filename(p, ".bias.csv")
        for row in _iter_csv(p):
            _apply_row_feedback(mc, exhibit, row, "bias", counts)
    for p in sorted(output_dir.glob("*.word_review.csv")):
        exhibit = _exhibit_from_filename(p, ".word_review.csv")
        for row in _iter_csv(p):
            _apply_row_feedback(mc, exhibit, row, "word_review", counts)
    for p in sorted(output_dir.glob("*.contradictions.csv")):
        exhibit = _exhibit_from_filename(p, ".contradictions.csv")
        for row in _iter_csv(p):
            _apply_row_feedback(mc, exhibit, row, "contradiction", counts)
    for p in sorted(output_dir.glob("*.evidence_matrix.csv")):
        exhibit = _exhibit_from_filename(p, ".evidence_matrix.csv")
        for row in _iter_csv(p):
            _apply_row_feedback(mc, exhibit, row, "evidence_matrix", counts)

    # Matter-wide CSVs (issues_log / deep / competency / engagement)
    for name, kind in [
        ("ISSUES_LOG.csv", "issue"),
        ("DEEP_CONTRADICTIONS.csv", "deep_contradiction"),
        ("COMPETENCY_FINDINGS.csv", "qps_competency"),
        ("EVIDENCE_ENGAGEMENT.csv", "evidence_engagement"),
    ]:
        p = output_dir / name
        for row in _iter_csv(p):
            exhibit = row.get("exhibit") or "<matter>"
            _apply_row_feedback(mc, exhibit, row, kind, counts)

    if not dry_run:
        mc.save()
    return counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--matter-root", required=True)
    ap.add_argument("--dry-run", action="store_true",
                    help="Report what would change without writing")
    args = ap.parse_args()
    counts = run(Path(args.matter_root), dry_run=args.dry_run)
    if not counts:
        print("No feedback found in any CSV. Add human_verified entries first.")
        return 0
    print("Corrections ingested:")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    cfg = Path(args.matter_root) / "config"
    print(f"\nSaved to:")
    print(f"  {cfg / 'vocabulary.json'}")
    print(f"  {cfg / 'corrections.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
