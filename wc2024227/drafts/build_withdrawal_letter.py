"""Build the Form 29 / r 64G withdrawal letter PDF from the txt draft.
House style mirrors drafts/SEND_31JUL/build_letters.py. The txt's DRAFT preamble
and the trailing NOTES block are excluded — only the letter between the two
rule lines is rendered. Metadata scrubbed on the way out."""
import re, subprocess
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, HRFlowable)

SRC = "/home/user/Personalproject/wc2024227/drafts/WITHDRAWAL_Form29_and_64G_DRAFT.txt"
OUT = "/home/user/Personalproject/wc2024227/drafts/out/WITHDRAWAL_Form29_and_64G_WC2024227.pdf"

INK = colors.HexColor("#111111")
MUTE = colors.HexColor("#555555")
RULE = colors.HexColor("#999999")

S = {
 "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=12.5, leading=16,
                         textColor=INK, spaceAfter=2),
 "sub":   ParagraphStyle("sub", fontName="Helvetica", fontSize=9.6, leading=13,
                         textColor=MUTE, spaceAfter=8),
 "meta":  ParagraphStyle("meta", fontName="Helvetica", fontSize=9.0, leading=13,
                         textColor=INK),
 "body":  ParagraphStyle("body", fontName="Helvetica", fontSize=10.0, leading=14.4,
                         textColor=INK, alignment=TA_JUSTIFY, spaceAfter=8),
 "item":  ParagraphStyle("item", fontName="Helvetica", fontSize=10.0, leading=14.4,
                         textColor=INK, leftIndent=22, firstLineIndent=-22,
                         alignment=TA_JUSTIFY, spaceAfter=8),
 "sig":   ParagraphStyle("sig", fontName="Helvetica", fontSize=10.0, leading=14.4,
                         textColor=INK, spaceAfter=2),
}

FOOT = "Cory Lea Shepherd · WC/2024/227 · Withdrawal — Form 29 Notice of Non-Party Disclosure and application of 23 June 2026"


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build():
    text = open(SRC, encoding="utf-8").read()
    # letter = between the first and second rule lines
    parts = re.split(r"^-{20,}\s*$", text, flags=re.M)
    header_block, letter = parts[0], parts[1]

    # To/Cc/Subject block from the preamble
    meta_lines = []
    for ln in header_block.split("\n"):
        if re.match(r"^(TO:|CC:|SUBJECT:|\s{6,})", ln):
            meta_lines.append(ln.rstrip())

    flow = [Paragraph("Withdrawal of the application of 23 June 2026 and the outstanding "
                      "items of the Form 29 Notice of Non-Party Disclosure", S["title"]),
            Paragraph("WC/2024/227 — Shepherd v Workers' Compensation Regulator", S["sub"])]
    if meta_lines:
        flow.append(Paragraph("<br/>".join(esc(l).replace("  ", "&nbsp;&nbsp;")
                                           for l in meta_lines), S["meta"]))
        flow.append(Spacer(1, 5))
    flow.append(HRFlowable(width="100%", thickness=0.8, color=RULE, spaceAfter=6))

    buf, mode = [], "body"

    def flush():
        nonlocal buf, mode
        if buf:
            txt = " ".join(x.strip() for x in buf).strip()
            if txt:
                flow.append(Paragraph(esc(txt), S[mode]))
        buf, mode = [], "body"

    for ln in letter.split("\n"):
        s = ln.strip()
        if not s:
            flush(); continue
        if re.match(r"^\d+\.\s", s):
            flush(); mode = "item"; buf = [s]; continue
        if s in ("Yours sincerely",) or s.startswith("Cory Lea Shepherd") or \
           s.startswith("Appellant (self-represented)"):
            flush(); flow.append(Paragraph(esc(s), S["sig"])); continue
        buf.append(s)
    flush()

    def deco(canv, doc):
        canv.saveState()
        canv.setFont("Helvetica", 7.2)
        canv.setFillColor(MUTE)
        canv.drawString(18*mm, 12*mm, FOOT)
        canv.drawRightString(192*mm, 12*mm, "Page %d" % doc.page)
        canv.setStrokeColor(RULE); canv.setLineWidth(0.4)
        canv.line(18*mm, 15*mm, 192*mm, 15*mm)
        canv.restoreState()

    raw = "/tmp/_withdrawal_raw.pdf"
    doc = BaseDocTemplate(raw, pagesize=A4,
                          leftMargin=18*mm, rightMargin=18*mm,
                          topMargin=16*mm, bottomMargin=20*mm,
                          title="Withdrawal — WC/2024/227",
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
