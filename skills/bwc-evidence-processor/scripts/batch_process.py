"""Matter-level batch orchestrator.

Walks a source directory tree, classifies each file, and processes the whole
matter end-to-end:

  1. extract_documents.py on every PDF / DOCX / XLSX / TXT / RTF
     -> builds a combined plain-text corpus that doubles as the sworn_corpus
  2. process_video.py on every MP4 / MOV / MKV / WAV / MP3 / M4A / WebM
  3. Emits a matter-wide master index with counts, severity rollup, flagged
     passages across every exhibit

Supports:
  - resume (skips files whose primary artefact already exists)
  - progress logging per file
  - graceful per-file failure (one corrupt file doesn't abort the batch)

Expected directory layout:

  <matter_root>/
    source/           <- disclosed files (any nesting)
    output/           <- artefacts
    sworn/            <- optional: existing sworn corpus TXT to merge in
    config/           <- matter_<ID>.json

Usage:

  python batch_process.py \
      --matter-root /path/to/matter \
      --matter-config config/matter_<ID>.json \
      --model small.en --device auto
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _path_helper import ensure_tools_on_path  # noqa: E402

ensure_tools_on_path()

VIDEO_EXT = {".mp4", ".mov", ".mkv", ".avi", ".webm", ".m4v", ".mpg", ".mpeg"}
AUDIO_EXT = {".wav", ".mp3", ".m4a", ".flac", ".ogg", ".aac", ".wma"}
DOC_EXT = {".pdf", ".docx", ".xlsx", ".xls", ".txt", ".rtf", ".md"}


def classify(p: Path) -> str:
    ext = p.suffix.lower()
    if ext in VIDEO_EXT:
        return "video"
    if ext in AUDIO_EXT:
        return "audio"
    if ext in DOC_EXT:
        return "document"
    return "other"


def walk(source: Path) -> dict[str, list[Path]]:
    buckets: dict[str, list[Path]] = {"video": [], "audio": [], "document": [], "other": []}
    for p in sorted(source.rglob("*")):
        if p.is_file():
            buckets[classify(p)].append(p)
    return buckets


def already_done(media: Path, out_dir: Path) -> bool:
    return (out_dir / f"{media.stem}.master_report.md").is_file()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--matter-root", required=True)
    ap.add_argument("--matter-config", default=None)
    ap.add_argument("--model", default="small.en")
    ap.add_argument("--language", default="en")
    ap.add_argument("--device", default="auto")
    ap.add_argument("--ocr", action="store_true")
    ap.add_argument("--no-resume", action="store_true",
                    help="Reprocess files even if artefacts already exist")
    ap.add_argument("--videos-only", action="store_true")
    ap.add_argument("--docs-only", action="store_true")
    args = ap.parse_args()

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from extract_documents import process_directory as extract_docs
    import process_video  # noqa: F401 - imported for side-effect checks

    root = Path(args.matter_root).resolve()
    source = root / "source"
    out_dir = root / "output"
    sworn_dir = root / "sworn"
    out_dir.mkdir(parents=True, exist_ok=True)
    sworn_dir.mkdir(parents=True, exist_ok=True)

    if not source.is_dir():
        print(f"ERROR: source directory not found: {source}", file=sys.stderr)
        return 2

    t0 = time.time()
    print(f"== Matter root: {root}")
    buckets = walk(source)
    summary = {k: len(v) for k, v in buckets.items()}
    print(f"== File counts: {summary}")

    # ---- Stage A: documents -> corpus ----
    corpus_path = sworn_dir / "corpus.txt"
    if not args.videos_only and buckets["document"]:
        print(f"\n== Extracting {len(buckets['document'])} documents")
        doc_out = out_dir / "documents"
        try:
            extract_docs(source, doc_out, corpus_path)
        except Exception:
            traceback.print_exc()

    # Merge any pre-existing sworn text files in sworn/ into the corpus too
    for sp in sworn_dir.glob("*.txt"):
        if sp.resolve() == corpus_path.resolve():
            continue
        with corpus_path.open("a", encoding="utf-8") as f:
            f.write(f"\n===== {sp} (pre-existing sworn) =====\n")
            f.write(sp.read_text(encoding="utf-8", errors="replace"))

    # ---- Stage B: videos + audio -> full pipeline ----
    media_files = [] if args.docs_only else buckets["video"] + buckets["audio"]
    print(f"\n== Processing {len(media_files)} media files")
    per_file_log: list[dict] = []

    for i, m in enumerate(media_files, 1):
        label = f"[{i}/{len(media_files)}] {m.relative_to(source)}"
        if not args.no_resume and already_done(m, out_dir):
            print(f"{label}  SKIP (already processed)")
            per_file_log.append({"file": str(m), "status": "skipped"})
            continue

        cmd = [
            sys.executable,
            str(Path(__file__).with_name("process_video.py")),
            "--input", str(m),
            "--output-dir", str(out_dir),
            "--model", args.model,
            "--language", args.language,
            "--device", args.device,
        ]
        if args.matter_config:
            cmd += ["--matter-config", args.matter_config]
        if corpus_path.is_file():
            cmd += ["--sworn-corpus", str(corpus_path)]
        if args.ocr:
            cmd += ["--ocr"]

        print(f"{label}  RUN")
        start = time.time()
        try:
            import subprocess
            r = subprocess.run(cmd, capture_output=False)
            status = "ok" if r.returncode == 0 else f"exit_{r.returncode}"
        except Exception as e:
            status = f"error:{e}"
        dur = round(time.time() - start, 1)
        print(f"{label}  DONE in {dur}s ({status})")
        per_file_log.append({"file": str(m), "status": status, "seconds": dur})

    # ---- Stage C: matter-wide master index ----
    print("\n== Building matter-wide master index")
    build_matter_index(root, out_dir, buckets, per_file_log, time.time() - t0)

    print(f"\n== Batch complete in {round(time.time() - t0, 1)}s")
    return 0


def _read_csv(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if text and text[0].startswith("#"):
        text = text[1:]
    return list(csv.DictReader(text))


def build_matter_index(
    root: Path,
    out_dir: Path,
    buckets: dict[str, list[Path]],
    per_file_log: list[dict],
    seconds: float,
) -> Path:
    dest = out_dir / "MATTER_INDEX.md"
    total_compliance: dict[str, int] = {}
    total_matrix = 0
    total_contradictions = 0
    highlights: list[tuple[str, str, str, str]] = []  # severity, file, time, detail

    for comp in out_dir.glob("*.compliance.csv"):
        for r in _read_csv(comp):
            sev = r.get("severity", "low")
            total_compliance[sev] = total_compliance.get(sev, 0) + 1
            if sev in ("critical", "high"):
                highlights.append((sev, comp.stem.removesuffix(".compliance"),
                                   r.get("timestamp_hms", ""),
                                   f"{r.get('category','')}: {r.get('detail','')}"))
    for mat in out_dir.glob("*.evidence_matrix.csv"):
        total_matrix += len(_read_csv(mat))
    for c in out_dir.glob("*.contradictions.csv"):
        total_contradictions += len(_read_csv(c))

    lines = [
        "# Matter Master Index",
        "",
        f"> **MACHINE-GENERATED - UNVERIFIED**  -  Root: `{root}`",
        f"> Processed in {round(seconds, 1)}s.",
        "",
        "## File counts",
        "",
        "| Kind | Count |",
        "|------|-------|",
        f"| Video | {len(buckets['video'])} |",
        f"| Audio | {len(buckets['audio'])} |",
        f"| Document | {len(buckets['document'])} |",
        f"| Other (skipped) | {len(buckets['other'])} |",
        "",
        "## Aggregate findings across exhibits",
        "",
        f"- Compliance findings: {sum(total_compliance.values())}",
    ]
    for sev in ("critical", "high", "medium", "low"):
        if sev in total_compliance:
            lines.append(f"  - {sev}: {total_compliance[sev]}")
    lines += [
        f"- Evidence-matrix rows: {total_matrix}",
        f"- Contradictions vs corpus: {total_contradictions}",
        "",
        "## Critical / high severity highlights",
        "",
    ]
    if highlights:
        lines += ["| Exhibit | Time | Severity | Detail |",
                  "|---------|------|----------|--------|"]
        for sev, exhibit, ts, detail in sorted(highlights,
                                               key=lambda x: (x[0] != "critical", x[1])):
            detail = detail.replace("|", "\\|")
            lines.append(f"| {exhibit} | {ts} | {sev} | {detail} |")
    else:
        lines.append("_None recorded._")
    lines += [
        "",
        "## Per-exhibit master reports",
        "",
    ]
    for rep in sorted(out_dir.glob("*.master_report.md")):
        lines.append(f"- [{rep.stem}]({rep.name})")

    lines += [
        "",
        "## Processing log",
        "",
        "| File | Status | Seconds |",
        "|------|--------|---------|",
    ]
    for entry in per_file_log:
        lines.append(
            f"| {entry['file']} | {entry.get('status','')} | "
            f"{entry.get('seconds','')} |"
        )
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return dest


if __name__ == "__main__":
    raise SystemExit(main())
