import sys, re, pymupdf
doc = pymupdf.open(sys.argv[1])
items = []; cur = None
def start(kind, x, page):
    global cur
    cur = {"kind": kind, "x": round(x), "page": page, "reg": "", "ital": "", "bold": ""}
    items.append(cur)
for pno, page in enumerate(doc, 1):
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                t = s["text"]; f = s["font"]
                if f.startswith("SymbolMT") and t.strip() == "•":
                    start("bullet", s["bbox"][0], pno); continue
                if "Bold" in f:
                    if cur is None or cur["kind"] != "head" or cur["page"] != pno:
                        start("head", s["bbox"][0], pno)
                    cur["bold"] += t; continue
                if cur is None or cur["kind"] == "head":
                    start("para", s["bbox"][0], pno)
                if "Italic" in f: cur["ital"] += t
                elif f.startswith("Arial"): pass
                else: cur["reg"] += t
def stats(t):
    return {
      "apos_straight": t.count("'"), "apos_curly": t.count("’") + t.count("‘"),
      "dq_straight": t.count('"'), "dq_curly": t.count("“") + t.count("”"),
      "endash": t.count("–"), "hyphen_spaced": len(re.findall(r" - ", t)),
    }
for i, it in enumerate(items, 1):
    txt = (it["bold"] or "") + it["reg"]
    st = stats(txt + it["ital"])
    flags = []
    if re.search(r"\bThat [A-Z]", it["reg"]): flags.append("That+Capital")
    if re.search(r"\.\s*,", it["reg"]): flags.append("'.,' splice")
    if re.search(r"characteriz", it["reg"]): flags.append("US -ize")
    if re.search(r"characteris|recognis|organis|authoris", it["reg"]): flags.append("AU -ise")
    if re.search(r"Tanny|Wight|Kimberly\b", txt): flags.append("name typo")
    if "  " in it["reg"]: flags.append("double space")
    tag = it["ital"].strip()
    print(f"{i:02d} p{it['page']} {it['kind']:6s} x={it['x']:3d} tag={'Y' if tag else '-'} {st} {flags}\n    {txt.strip()[:150]!r}{(' || ' + tag) if tag else ''}")
