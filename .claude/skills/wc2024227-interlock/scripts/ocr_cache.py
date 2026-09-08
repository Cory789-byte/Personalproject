#!/usr/bin/env python3
"""Build/refresh the OCR cache for documents with no usable text layer.

Why this exists: 31 documents in this matter return nothing to pdftotext. They were therefore
INVISIBLE to grep, and every session that needed one had to render it with pdftoppm and read the
images again. That is why things in this repo were repeatedly called "missing" while sitting on
disk. This script OCRs them ONCE into index/ocr/, and build_index.py then folds that text into
FULLTEXT.txt so a single grep reaches the whole matter.

Cache key = sha1 of the file bytes, so a re-run is free and an edited file re-OCRs automatically.

Run:  python3 scripts/ocr_cache.py [repo_root]
"""
import os, sys, subprocess, hashlib, tempfile, json

ROOT = sys.argv[1] if len(sys.argv) > 1 else "/home/user/Personalproject/wc2024227"
CACHE = os.path.join(ROOT, "index", "ocr")
os.makedirs(CACHE, exist_ok=True)
SKIP_DIRS = {"index", ".git"}
DPI = "200"

def sha1(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def needs_ocr(path):
    """True if pdftotext yields under 100 chars per page."""
    try:
        n = 0
        info = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=60).stdout
        for line in info.splitlines():
            if line.startswith("Pages:"):
                n = int(line.split()[1])
        if not n:
            return False, 0
        t = subprocess.run(["pdftotext", "-layout", path, "-"],
                           capture_output=True, text=True, timeout=300).stdout
        return (len(t.strip()) / n) < 100, n
    except Exception:
        return False, 0

def ocr(path, npages):
    """Render each page and OCR it. Returns list of page texts."""
    pages = []
    with tempfile.TemporaryDirectory() as td:
        stem = os.path.join(td, "p")
        subprocess.run(["pdftoppm", "-r", DPI, "-gray", "-png", path, stem],
                       capture_output=True, timeout=1800)
        imgs = sorted(f for f in os.listdir(td) if f.endswith(".png"))
        for img in imgs:
            r = subprocess.run(["tesseract", os.path.join(td, img), "stdout", "--psm", "6"],
                               capture_output=True, text=True, timeout=300)
            pages.append(r.stdout)
    return pages

done = skipped = 0
manifest = {}
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in sorted(filenames):
        if not fn.lower().endswith(".pdf"):
            continue
        full = os.path.join(dirpath, fn)
        rel = os.path.relpath(full, ROOT)
        need, npages = needs_ocr(full)
        if not need:
            continue
        key = sha1(full)
        out = os.path.join(CACHE, key + ".json")
        if os.path.exists(out):
            skipped += 1
            manifest[rel] = key
            continue
        print(f"OCR  {rel}  ({npages}pp)", flush=True)
        pages = ocr(full, npages)
        json.dump({"path": rel, "pages": pages}, open(out, "w"), ensure_ascii=False)
        manifest[rel] = key
        done += 1

json.dump(manifest, open(os.path.join(CACHE, "_map.json"), "w"), indent=1)
print(f"\nOCR complete. newly processed: {done}, already cached: {skipped}, total: {len(manifest)}")
