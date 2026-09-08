#!/usr/bin/env python3
"""Build index/SCANNED_DOCUMENTS.md - the catalogue of documents that had no text layer.

These 31 documents were invisible to grep and had to be re-rendered by every session that needed
them. ocr_cache.py now OCRs them once; build_index.py folds the text into FULLTEXT.txt; and this
script writes a human-readable catalogue so you can tell at a glance what each one IS without
opening it.

Run:  python3 scripts/ocr_cache.py && python3 scripts/build_index.py && python3 scripts/build_scanned_catalogue.py
"""
import os, sys, json, re

ROOT = sys.argv[1] if len(sys.argv) > 1 else "/home/user/Personalproject/wc2024227"
CACHE = os.path.join(ROOT, "index", "ocr")
OUT = os.path.join(ROOT, "index", "SCANNED_DOCUMENTS.md")

mp = os.path.join(CACHE, "_map.json")
if not os.path.exists(mp):
    sys.exit("no OCR cache - run scripts/ocr_cache.py first")
m = json.load(open(mp))

def clean(t):
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

def headline(pages):
    """First meaningful lines of page 1 - enough to identify the document."""
    if not pages:
        return ""
    lines = [l.strip() for l in clean(pages[0]).splitlines() if l.strip()]
    return " · ".join(lines[:6])[:400]

entries = []
for rel, key in sorted(m.items()):
    f = os.path.join(CACHE, key + ".json")
    if not os.path.exists(f):
        continue
    d = json.load(open(f))
    pages = d.get("pages", [])
    chars = sum(len(p) for p in pages)
    entries.append((rel, len(pages), chars, headline(pages), key))

with open(OUT, "w", encoding="utf-8") as o:
    o.write("# SCANNED DOCUMENTS — the ones that used to be invisible to grep\n\n")
    o.write("> These documents return **nothing** to `pdftotext`. They have now been OCR'd once\n")
    o.write("> into `index/ocr/` and their text is folded into `index/FULLTEXT.txt`, tagged\n")
    o.write("> `[OCR]`. **You can now grep for them like anything else.**\n>\n")
    o.write("> ⚠ **OCR is machine reading and it makes mistakes.** Use it to FIND the document and\n")
    o.write("> the passage. Before any quotation goes into a filing, a letter, or an expert\n")
    o.write("> instruction, open the source PDF and verify the words. The interlock rule is\n")
    o.write("> unchanged: the index tells you where to look; it is not authority.\n>\n")
    o.write("> Regenerate after adding documents:\n")
    o.write("> `python3 scripts/ocr_cache.py && python3 scripts/build_index.py && python3 scripts/build_scanned_catalogue.py`\n\n")
    o.write(f"**{len(entries)} documents · {sum(e[1] for e in entries)} pages · "
            f"{sum(e[2] for e in entries):,} characters recovered**\n\n")
    o.write("| Document | Pages | What page 1 says |\n|---|---|---|\n")
    for rel, np, chars, head, key in entries:
        o.write(f"| `{rel}` | {np} | {head.replace('|', '/')} |\n")
    o.write("\n---\n\n## Full first-page text, per document\n\n")
    for rel, np, chars, head, key in entries:
        d = json.load(open(os.path.join(CACHE, key + ".json")))
        o.write(f"### `{rel}`\n*{np} pages · OCR cache `{key[:12]}`*\n\n```\n")
        o.write(clean(d["pages"][0])[:2500] if d["pages"] else "")
        o.write("\n```\n\n")
        if np > 1:
            o.write(f"*Pages 2–{np}: grep `index/FULLTEXT.txt` for "
                    f"`>>> {rel} :: page N`*\n\n")
print(f"wrote {OUT}: {len(entries)} documents")
