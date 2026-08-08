#!/usr/bin/env python3
"""Build a full-text index of every document in the matter, so that any
proposition can be searched across the WHOLE repo instead of across the files
someone happened to remember.

Writes two artefacts into wc2024227/index/:
  FULLTEXT.txt   - every extractable page, with a >>> FILE :: PAGE marker line
                   before each page, so a grep hit tells you exactly where to look
  MANIFEST.tsv   - one row per document: path, pages, chars extracted, status

Status values that matter:
  NO_TEXT_LAYER  - pdftotext returns nothing. These are the dangerous ones:
                   a grep will silently miss them. They must be rendered with
                   `pdftoppm -r 150 -png` and read as images.
  THIN           - under 100 chars/page. Probably scanned; treat as NO_TEXT_LAYER.

Run:  python3 scripts/build_index.py [repo_root]
"""
import os, subprocess, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "/home/user/Personalproject/wc2024227"
OUT = os.path.join(ROOT, "index")
os.makedirs(OUT, exist_ok=True)
SKIP_DIRS = {"index", ".git"}

def pages_of(path):
    try:
        out = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=60).stdout
        for line in out.splitlines():
            if line.startswith("Pages:"):
                return int(line.split()[1])
    except Exception:
        pass
    return 0

def text_of(path):
    """One call per file. pdftotext separates pages with a form feed, so we can
    keep page granularity without paying for N subprocess launches."""
    try:
        r = subprocess.run(["pdftotext", "-layout", path, "-"],
                           capture_output=True, text=True, timeout=300)
        return r.stdout.split("\f")
    except Exception:
        return []

rows, total_pages, no_text = [], 0, []
with open(os.path.join(OUT, "FULLTEXT.txt"), "w", encoding="utf-8", errors="replace") as ft:
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in sorted(filenames):
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, ROOT)
            ext = fn.lower().rsplit(".", 1)[-1] if "." in fn else ""
            if ext == "pdf":
                n = pages_of(full); total_pages += n
                chars = 0
                for i, t in enumerate(text_of(full), start=1):
                    if t.strip():
                        ft.write(f"\n>>> {rel} :: page {i}\n{t}")
                        chars += len(t)
                per = chars / n if n else 0
                status = "OK" if per >= 100 else ("NO_TEXT_LAYER" if chars == 0 else "THIN")
                if status != "OK":
                    no_text.append(rel)
                rows.append((rel, n, chars, status))
            elif ext in ("md", "txt", "tsv", "csv", "json", "py"):
                try:
                    t = open(full, encoding="utf-8", errors="replace").read()
                except Exception:
                    continue
                ft.write(f"\n>>> {rel} :: text\n{t}")
                rows.append((rel, 0, len(t), "OK"))

with open(os.path.join(OUT, "MANIFEST.tsv"), "w", encoding="utf-8") as m:
    m.write("path\tpages\tchars\tstatus\n")
    for r in sorted(rows):
        m.write("\t".join(str(x) for x in r) + "\n")

print(f"indexed {len(rows)} files, {total_pages} PDF pages")
print(f"{len(no_text)} documents have NO usable text layer and MUST be rendered:")
for r in no_text:
    print("  ⛔", r)
