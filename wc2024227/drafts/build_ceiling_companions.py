"""Render the two companion markdown docs (source-package guide; the ceiling
explanation) to clean A4 PDFs via Chromium headless. Compact md->html covering
headings, bold/italic, tables, lists, blockquote, hr, inline code."""
import re, subprocess, html, os

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
DST = "/home/user/Personalproject/wc2024227/drafts/out/CEILING_SET"

DOCS = [
    ("01b_Source_Package_Guide_Report_B.md", "01b_Source_Package_Guide_Report_B.pdf"),
    ("01c_Why_Report_B_Is_The_Ceiling.md",   "01c_Why_Report_B_Is_The_Ceiling.pdf"),
]

CSS = """
@page { size: A4; margin: 18mm 18mm 20mm 18mm; }
* { box-sizing: border-box; }
body { font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif; color:#111;
       font-size: 10pt; line-height: 1.45; }
h1 { font-size: 15pt; margin: 0 0 4pt; }
h2 { font-size: 12pt; margin: 16pt 0 4pt; border-bottom:1px solid #ccc; padding-bottom:2pt; }
h3 { font-size: 10.5pt; margin: 12pt 0 3pt; }
p  { margin: 0 0 7pt; text-align: justify; }
ul, ol { margin: 0 0 8pt 0; padding-left: 20pt; }
li { margin: 0 0 4pt; }
em { font-style: italic; }
strong { font-weight: 700; }
blockquote { margin: 6pt 0 8pt; padding: 4pt 10pt; border-left: 3px solid #999;
             background:#f6f6f6; color:#222; }
hr { border: none; border-top: 1px solid #bbb; margin: 10pt 0; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 9pt; }
th, td { border: 1px solid #bbb; padding: 4pt 6pt; text-align: left; vertical-align: top; }
th { background: #eee; }
code { font-family: 'SFMono-Regular', Consolas, monospace; font-size: 8.6pt;
       background:#f0f0f0; padding:0 2px; border-radius:2px; }
.docfoot { color:#777; font-size:8pt; margin-top:14pt; border-top:1px solid #ddd; padding-top:5pt; }
"""


def inline(t):
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\*\w])\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"`([^`]+?)`", r"<code>\1</code>", t)
    return t


def render_table(rows):
    out = ["<table>"]
    for ri, r in enumerate(rows):
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        tag = "th" if ri == 0 else "td"
        out.append("<tr>" + "".join("<%s>%s</%s>" % (tag, inline(c), tag) for c in cells) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


def md_to_html(md):
    lines = md.split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1; continue
        if s == "---":
            out.append("<hr>"); i += 1; continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            lvl = min(len(m.group(1)), 3)
            out.append("<h%d>%s</h%d>" % (lvl, inline(m.group(2)), lvl)); i += 1; continue
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:\-|]+\|?\s*$", lines[i+1].strip()):
            rows = [s]
            i += 2  # skip the separator row
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip()); i += 1
            out.append(render_table(rows)); continue
        if s.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip()); i += 1
            out.append("<blockquote>%s</blockquote>" % inline(" ".join(buf))); continue
        if re.match(r"^\d+\.\s+", s):
            out.append("<ol>")
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                out.append("<li>%s</li>" % inline(re.sub(r"^\s*\d+\.\s+", "", lines[i]))); i += 1
            out.append("</ol>"); continue
        if s.startswith("- "):
            out.append("<ul>")
            while i < len(lines) and lines[i].strip().startswith("- "):
                out.append("<li>%s</li>" % inline(lines[i].strip()[2:])); i += 1
            out.append("</ul>"); continue
        out.append("<p>%s</p>" % inline(s)); i += 1
    return "\n".join(out)


for src, out in DOCS:
    md = open(os.path.join(DST, src), encoding="utf-8").read()
    body = md_to_html(md)
    page = "<!doctype html><html><head><meta charset='utf-8'><style>%s</style></head><body>%s<div class='docfoot'>WC/2024/227 · Report B ceiling set · internal working document — not for service</div></body></html>" % (CSS, body)
    htmlpath = "/tmp/_" + out.replace(".pdf", ".html")
    open(htmlpath, "w", encoding="utf-8").write(page)
    dst = os.path.join(DST, out)
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", "--print-to-pdf=" + dst, htmlpath],
                   check=True, capture_output=True)
    import pikepdf
    with pikepdf.open(dst, allow_overwriting_input=True) as p:
        if p.trailer.get("/Info"):
            del p.trailer["/Info"]
        if "/Metadata" in p.Root:
            del p.Root["/Metadata"]
        p.save(dst)
    print("built", dst)
