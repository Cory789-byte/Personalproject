"""Builds the two standalone letters that force a response under a power:

  1. FWA_REQUEST_cl10.3.txt          -> clause 10.3.2 flexible working request (21-day clock)
  2. DISPUTE_NOTICE_cl1.11_STAGE1.txt -> clause 1.11.2(a) Stage 1 dispute notice

Same house style as build_alloc_pdf.py. Metadata scrubbed on the way out.
"""
import re, subprocess, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, HRFlowable)

BASE = "/home/user/Personalproject/wc2024227/drafts/SEND_31JUL"
OUTD = "/home/user/Personalproject/wc2024227/drafts/out"

INK = colors.HexColor("#111111")
MUTE = colors.HexColor("#555555")
RULE = colors.HexColor("#999999")

S = {
 "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=13.5, leading=17,
                         textColor=INK, spaceAfter=2),
 "sub":   ParagraphStyle("sub", fontName="Helvetica", fontSize=10, leading=13,
                         textColor=MUTE, spaceAfter=8),
 "meta":  ParagraphStyle("meta", fontName="Helvetica", fontSize=8.8, leading=12.5,
                         textColor=INK),
 "h1":    ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=10.2, leading=13,
                         textColor=INK, spaceBefore=13, spaceAfter=5),
 "h2":    ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=9.2, leading=12,
                         textColor=INK, spaceBefore=9, spaceAfter=3),
 "body":  ParagraphStyle("body", fontName="Helvetica", fontSize=9.1, leading=12.8,
                         textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6),
 "quote": ParagraphStyle("quote", fontName="Helvetica-Oblique", fontSize=8.9, leading=12.4,
                         textColor=INK, leftIndent=14, rightIndent=10, spaceAfter=6),
 "item":  ParagraphStyle("item", fontName="Helvetica", fontSize=9.1, leading=12.8,
                         textColor=INK, leftIndent=16, firstLineIndent=-11,
                         alignment=TA_JUSTIFY, spaceAfter=5),
 "sig":   ParagraphStyle("sig", fontName="Helvetica", fontSize=9.1, leading=12.8,
                         textColor=INK, spaceAfter=2),
}

DOCS = [
 dict(src="FWA_REQUEST_cl10.3.txt",
      out="REQUEST_Change_in_the_way_I_work_cl10.3_MSH-INJ-5795.pdf",
      title="Request for a change in the way I work",
      sub="Clause 10.3.2, Certified Agreement (No. 12) 2025 &#183; s 27, Industrial Relations Act 2016 (Qld)",
      foot="Cory Lea Shepherd · MSH-INJ-5795 · Request under clause 10.3.2 — decision due within 21 days (cl 10.3.6)"),
 dict(src="DISPUTE_NOTICE_cl1.11_STAGE1.txt",
      out="NOTICE_OF_DISPUTE_cl1.11_Stage1.pdf",
      title="Notice of dispute — Stage 1",
      sub="Clause 1.11.2(a), Certified Agreement (No. 12) 2025",
      foot="Cory Lea Shepherd · Notice of dispute under clause 1.11 — Stage 1"),
 dict(src="NOTICE_OF_APPOINTMENTS_AND_COSTS.txt",
      out="NOTICE_Appointments_and_Costs_MSH-INJ-5795.pdf",
      title="Notice of medical appointments arranged, and of costs",
      sub="Request for Medical Information dated 31 July 2026 &#183; MSH-INJ-5795",
      foot="Cory Lea Shepherd · MSH-INJ-5795 · Notice of medical appointments arranged, and of costs"),
 dict(src="LETTER_CONFLICT_AND_INFORMATION.txt",
      out="LETTER_Conflict_and_Information_Handling_MSH-INJ-5795.pdf",
      title="Conflict of interest, delegation, and the handling of my personal information",
      sub="Section 89, Public Sector Act 2022 &#183; Code of Conduct clause 1.2",
      foot="Cory Lea Shepherd · MSH-INJ-5795 · Conflict of interest, delegation and information handling"),
 dict(src="PROPOSAL_RETURN_TO_WORK.txt",
      out="PROPOSAL_Return_to_Work_MSH-INJ-5795.pdf",
      title="Proposal for Return to Work",
      sub="Accompanying the Response to the Request for Medical Information &#183; MSH-INJ-5795",
      foot="Cory Lea Shepherd · MSH-INJ-5795 · Proposal for Return to Work"),
]


def esc(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)


def build(spec):
    lines = open("%s/%s" % (BASE, spec["src"]), encoding="utf-8").read().split("\n")
    flow = [Paragraph(spec["title"], S["title"]),
            Paragraph(spec["sub"], S["sub"])]

    # the To/Cc/Date/Subject block is everything before the first rule
    i = 0
    head = []
    while i < len(lines) and not lines[i].startswith("------"):
        if lines[i].strip():
            head.append(lines[i].rstrip())
        i += 1
    # drop the title lines already rendered above
    head = [h for h in head if not h.startswith(("REQUEST FOR", "NOTICE OF DISPUTE",
                                                 "NOTICE OF MEDICAL", "Request for Medical",
                                                 "CONFLICT OF INTEREST", "Section 89,",
                                                 "PROPOSAL FOR RETURN", "Accompanying the Response",
                                                 "Clause 10.3.2,", "Section 27,",
                                                 "Clause 1.11.2(a),"))]
    if head:
        flow.append(Paragraph("<br/>".join(esc(h).replace("  ", "&nbsp;&nbsp;") for h in head),
                              S["meta"]))
        flow.append(Spacer(1, 5))
    flow.append(HRFlowable(width="100%", thickness=0.8, color=RULE, spaceAfter=2))

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
        ln = lines[i]
        s = ln.strip()
        i += 1

        if ln.startswith("------"):
            flush(); continue
        if not s:
            flush(); continue

        if re.match(r"^\d+\.\s+[A-Z]", s):
            flush(); flow.append(Paragraph(esc(s), S["h1"])); continue
        if re.match(r"^\d+\.\d+\s+[A-Z]", s):
            flush(); flow.append(Paragraph(esc(s), S["h2"])); continue

        if re.match(r"^\([a-z0-9]+\)\s", s):
            flush(); mode = "item"; buf = [s]
            while i < len(lines) and lines[i].strip() and \
                    not re.match(r"^\(", lines[i].strip()) and lines[i].startswith("    "):
                buf.append(lines[i]); i += 1
            flush(); continue

        if ln.startswith('     "') or ln.startswith("     “"):
            flush(); mode = "quote"; buf = [s]
            while i < len(lines) and lines[i].strip() and lines[i].startswith("     "):
                buf.append(lines[i]); i += 1
            flush(); continue

        if s in ("Yours sincerely,",) or s.startswith("Cory Lea Shepherd") or \
           s.startswith("AO3, Switchboard") or "coryshepherd1@hotmail.com" in s:
            flush(); flow.append(Paragraph(esc(s), S["sig"])); continue

        buf.append(s)

    flush()

    def deco(canv, doc):
        canv.saveState()
        canv.setFont("Helvetica", 7.2)
        canv.setFillColor(MUTE)
        canv.drawString(18*mm, 12*mm, spec["foot"])
        canv.drawRightString(192*mm, 12*mm, "Page %d" % doc.page)
        canv.setStrokeColor(RULE); canv.setLineWidth(0.4)
        canv.line(18*mm, 15*mm, 192*mm, 15*mm)
        canv.restoreState()

    raw = "/tmp/_letter_raw.pdf"
    out = "%s/%s" % (OUTD, spec["out"])
    doc = BaseDocTemplate(raw, pagesize=A4,
                          leftMargin=18*mm, rightMargin=18*mm,
                          topMargin=16*mm, bottomMargin=20*mm,
                          title=spec["title"], author="", subject="", creator="", producer="")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=deco)])
    doc.build(flow)

    subprocess.run(["qpdf", "--empty", "--pages", raw, "1-z", "--", out], check=True)
    import pikepdf
    with pikepdf.open(out, allow_overwriting_input=True) as p:
        p.trailer.get("/Info") and p.trailer.__delitem__("/Info")
        if "/Metadata" in p.Root:
            del p.Root["/Metadata"]
        p.save(out)
    print("built", out)


for spec in DOCS:
    build(spec)
