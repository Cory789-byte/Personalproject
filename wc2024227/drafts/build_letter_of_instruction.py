"""Build the Report B letter of instruction PDF from its markdown source.

House style mirrors drafts/SEND_31JUL/build_letters.py (reportlab, A4, metadata
scrubbed on the way out). Source is markdown:
  - a line wholly wrapped in **...** starting with "N." or "Re:" is a heading
  - '> ' opens a blockquote
  - '- ' opens a bullet item
  - **bold** renders inline; *italic* renders inline
"""
import re, subprocess
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, HRFlowable)

SRC = "/home/user/Personalproject/wc2024227/drafts/out/CEILING_SET/01_Letter_of_Instruction_Report_B.md"
OUT = "/home/user/Personalproject/wc2024227/drafts/out/CEILING_SET/01_Letter_of_Instruction_Report_B.pdf"

INK = colors.HexColor("#111111")
MUTE = colors.HexColor("#555555")
RULE = colors.HexColor("#999999")

S = {
 "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=12.5, leading=16,
                         textColor=INK, spaceAfter=2),
 "sub":   ParagraphStyle("sub", fontName="Helvetica", fontSize=9.6, leading=13,
                         textColor=MUTE, spaceAfter=8),
 "meta":  ParagraphStyle("meta", fontName="Helvetica", fontSize=9.0, leading=13,
                         textColor=INK, spaceAfter=2),
 "h1":    ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=10.2, leading=13.5,
                         textColor=INK, spaceBefore=12, spaceAfter=4),
 "body":  ParagraphStyle("body", fontName="Helvetica", fontSize=9.2, leading=13.2,
                         textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6),
 "quote": ParagraphStyle("quote", fontName="Helvetica", fontSize=9.4, leading=13.4,
                         textColor=INK, leftIndent=16, rightIndent=12, spaceBefore=2,
                         spaceAfter=8, borderPadding=(4, 4, 4, 8)),
 "item":  ParagraphStyle("item", fontName="Helvetica", fontSize=9.2, leading=13.0,
                         textColor=INK, leftIndent=18, firstLineIndent=-11,
                         alignment=TA_JUSTIFY, spaceAfter=5),
 "sig":   ParagraphStyle("sig", fontName="Helvetica", fontSize=9.2, leading=13.2,
                         textColor=INK, spaceAfter=2),
 "encl":  ParagraphStyle("encl", fontName="Helvetica", fontSize=8.6, leading=12,
                         textColor=MUTE, spaceBefore=8, spaceAfter=2),
}

FOOT = "Cory Lea Shepherd · WC/2024/227 · Letter of instruction — medico-legal report on causation (Report B)"


def esc(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\*A-Za-z0-9])\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    return t


def is_heading(s):
    return bool(re.match(r"^\*\*(\d+\.\s+.+|Re:.+|LETTER OF INSTRUCTION.*|QIRC matter.*)\*\*$", s))


def build():
    lines = open(SRC, encoding="utf-8").read().split("\n")
    flow = []

    # Title = first two ** lines
    flow.append(Paragraph(esc(lines[0].strip().strip("*")), S["title"]))
    flow.append(Paragraph(esc(lines[1].strip().strip("*")), S["sub"]))

    i = 2
    # address / date block until the "Re:" heading
    head = []
    while i < len(lines) and not lines[i].strip().startswith("**Re:"):
        if lines[i].strip():
            head.append(lines[i].rstrip())
        i += 1
    if head:
        flow.append(Paragraph("<br/>".join(esc(h) for h in head), S["meta"]))
        flow.append(Spacer(1, 4))

    buf, mode = [], "body"

    def flush():
        nonlocal buf, mode
        if not buf:
            return
        txt = " ".join(x.strip() for x in buf).strip()
        buf = []
        if txt:
            flow.append(Paragraph(esc(txt), S[mode]))
        mode = "body"

    while i < len(lines):
        s = lines[i].strip()
        i += 1

        if not s:
            flush(); continue

        if s == "---":
            flush()
            flow.append(HRFlowable(width="100%", thickness=0.7, color=RULE,
                                   spaceBefore=4, spaceAfter=4))
            continue

        if is_heading(s):
            flush()
            flow.append(Paragraph(esc(s.strip("*")), S["h1"]))
            continue

        if s.startswith("> "):
            flush(); mode = "quote"; buf = [s[2:]]
            flush(); continue

        if s.startswith("- "):
            flush(); mode = "item"; buf = [s[2:]]
            flush(); continue

        if s.startswith("Enclosures:"):
            flush()
            flow.append(Paragraph(esc(s), S["encl"]))
            continue

        if s in ("Yours sincerely,",) or s.startswith("Cory Lea Shepherd") or \
           s.startswith("Appellant (self-represented)") or s.startswith("[phone]"):
            flush()
            flow.append(Paragraph(esc(s), S["sig"]))
            continue

        buf.append(s)

    flush()

    def deco(canv, doc):
        canv.saveState()
        canv.setFont("Helvetica", 7.0)
        canv.setFillColor(MUTE)
        canv.drawString(18*mm, 12*mm, FOOT)
        canv.drawRightString(192*mm, 12*mm, "Page %d" % doc.page)
        canv.setStrokeColor(RULE); canv.setLineWidth(0.4)
        canv.line(18*mm, 15*mm, 192*mm, 15*mm)
        canv.restoreState()

    raw = "/tmp/_loi_raw.pdf"
    doc = BaseDocTemplate(raw, pagesize=A4,
                          leftMargin=18*mm, rightMargin=18*mm,
                          topMargin=16*mm, bottomMargin=20*mm,
                          title="Letter of instruction — WC/2024/227",
                          author="", subject="", creator="", producer="")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=deco)])
    doc.build(flow)

    subprocess.run(["qpdf", "--empty", "--pages", raw, "1-z", "--", OUT], check=True)
    import pikepdf
    with pikepdf.open(OUT, allow_overwriting_input=True) as p:
        if p.trailer.get("/Info"):
            del p.trailer["/Info"]
        if "/Metadata" in p.Root:
            del p.Root["/Metadata"]
        p.save(OUT)
    print("built", OUT)


build()
