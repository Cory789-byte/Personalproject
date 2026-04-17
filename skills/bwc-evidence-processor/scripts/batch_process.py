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
import threading
import time
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _path_helper import ensure_tools_on_path  # noqa: E402

ensure_tools_on_path()


def _make_lock():
    return threading.Lock()

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
    ap.add_argument("--limit", type=int, default=0,
                    help="Process at most N media files this run (0 = no limit)")
    ap.add_argument("--only-containing", default=None,
                    help="Process only media whose filename contains this substring")
    ap.add_argument("--gpu-workers", type=int, default=0,
                    help="Number of parallel workers using --device cuda "
                         "(Quadro P400: keep at 1 max due to 2GB VRAM)")
    ap.add_argument("--cpu-workers", type=int, default=1,
                    help="Number of parallel workers using --device cpu "
                         "(1-2 is usually optimal; Whisper is already multi-threaded)")
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
    if args.only_containing:
        media_files = [m for m in media_files if args.only_containing.lower() in m.name.lower()]
    if args.limit and len(media_files) > args.limit:
        # Prefer unprocessed files first, then smallest -> largest
        media_files.sort(key=lambda m: (already_done(m, out_dir), m.stat().st_size))
        media_files = media_files[: args.limit]
    # Filter out already-processed files if resume is on
    if not args.no_resume:
        pre = len(media_files)
        media_files = [m for m in media_files if not already_done(m, out_dir)]
        skipped = pre - len(media_files)
        if skipped:
            print(f"== Skipping {skipped} already-processed files (resume)")

    total = len(media_files)
    print(f"== Processing {total} media files")
    per_file_log: list[dict] = []

    # Decide worker plan. If user didn't set --gpu-workers explicitly but passed
    # --device cuda, give them 1 GPU worker. Likewise for cpu.
    gpu_workers = args.gpu_workers
    cpu_workers = args.cpu_workers
    if args.device == "cuda" and gpu_workers == 0 and cpu_workers == 1:
        gpu_workers, cpu_workers = 1, 0
    total_workers = max(1, gpu_workers + cpu_workers)

    # Sort: largest first so big files go to GPU workers when they become free.
    media_files.sort(key=lambda m: -m.stat().st_size)

    worker_devices: list[str] = (["cuda"] * gpu_workers) + (["cpu"] * cpu_workers)
    if not worker_devices:
        worker_devices = [args.device or "cpu"]
    print(f"== Worker plan: {gpu_workers} GPU + {cpu_workers} CPU "
          f"= {total_workers} concurrent (sorted largest-first)")

    log_lock = _make_lock()

    def run_one(i: int, m: Path, device: str) -> dict:
        label = f"[{i}/{total}] {m.relative_to(source)} ({device})"
        cmd = [
            sys.executable,
            str(Path(__file__).with_name("process_video.py")),
            "--input", str(m),
            "--output-dir", str(out_dir),
            "--model", args.model,
            "--language", args.language,
            "--device", device,
        ]
        if args.matter_config:
            cmd += ["--matter-config", args.matter_config]
        if corpus_path.is_file():
            cmd += ["--sworn-corpus", str(corpus_path)]
        if args.ocr:
            cmd += ["--ocr"]

        with log_lock:
            print(f"{label}  RUN")
        start = time.time()
        import subprocess
        try:
            r = subprocess.run(cmd, capture_output=True, text=True)
            status = "ok" if r.returncode == 0 else f"exit_{r.returncode}"
            tail = (r.stderr or "")[-400:] if r.returncode != 0 else ""
        except Exception as e:
            status = f"error:{e}"
            tail = str(e)[-400:]
        dur = round(time.time() - start, 1)
        with log_lock:
            print(f"{label}  DONE in {dur}s ({status})")
            if tail:
                print(f"    stderr tail: {tail}")
        return {"file": str(m), "status": status, "seconds": dur, "device": device}

    if total_workers <= 1:
        # Serial path (preserves tidy live output)
        device = worker_devices[0]
        for i, m in enumerate(media_files, 1):
            per_file_log.append(run_one(i, m, device))
    else:
        # Parallel path using a thread pool (subprocesses do the heavy lifting)
        from concurrent.futures import ThreadPoolExecutor, as_completed
        # Assign device per worker slot by round-robin within the pool.
        # ThreadPoolExecutor does not expose slot indices, so we mimic it
        # with a queue of available device tokens.
        import queue
        dev_q: "queue.Queue[str]" = queue.Queue()
        for d in worker_devices:
            dev_q.put(d)

        def worker(idx_file):
            i, m = idx_file
            dev = dev_q.get()
            try:
                return run_one(i, m, dev)
            finally:
                dev_q.put(dev)

        indexed = list(enumerate(media_files, 1))
        with ThreadPoolExecutor(max_workers=total_workers) as pool:
            for res in pool.map(worker, indexed):
                per_file_log.append(res)

    # ---- Stage C: matter-wide master index + case theory ----
    print("\n== Building matter-wide master index")
    build_matter_index(root, out_dir, buckets, per_file_log, time.time() - t0)

    print("== Building case theory synthesis")
    try:
        from case_theory import render as render_case_theory
        render_case_theory(root)
    except Exception:
        traceback.print_exc()

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
