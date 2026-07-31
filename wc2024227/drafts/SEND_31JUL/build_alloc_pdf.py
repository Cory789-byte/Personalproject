import re, subprocess
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, HRFlowable, KeepTogether)

SRC = "/home/user/Personalproject/wc2024227/drafts/SEND_31JUL/RFMI_ALLOCATION_AND_PROPOSAL.txt"
OUT = "/home/user/Personalproject/wc2024227/drafts/out/RFMI_Response_and_Allocation_MSH-INJ-5795.pdf"
RAW = "/tmp/_alloc_raw.pdf"

INK = colors.HexColor("#111111")
MUTE = colors.HexColor("#555555")
RULE = colors.HexColor("#999999")
BAND = colors.HexColor("#EDEDED")

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
 "arrow": ParagraphStyle("arrow", fontName="Helvetica-Bold", fontSize=9.0, leading=12.6,
                         textColor=INK, leftIndent=18, firstLineIndent=-9,
                         spaceAfter=5),
 "qref":  ParagraphStyle("qref", fontName="Helvetica-Bold", fontSize=9.1, leading=12.8,
                         textColor=INK, spaceBefore=5, spaceAfter=2),
 "cellL": ParagraphStyle("cellL", fontName="Helvetica", fontSize=8.2, leading=10.6, textColor=INK),
 "cellB": ParagraphStyle("cellB", fontName="Helvetica-Bold", fontSize=8.2, leading=10.6, textColor=INK),
}

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

ALLOC = [
 ("1(a)", "Date of first diagnosis", "Answered openly; clinical context from the psychiatrist"),
 ("1(b)", "Clinical basis for the causal link", "Withdrawal requested — a psychiatrist question, and in issue in the appeal"),
 ("1(c)", "Self-report v clinical assessment; other reports held", "Consented to — Dr Ma, as to his own assessment and his own file"),
 ("1(d)", "Foreseeable risk; controls medically necessary", "Dr Ma and the psychiatrist — a psychiatric risk assessment"),
 ("2",    "Following directions; performance and conduct discussions", "Health Service — threshold question"),
 ("3",    "Fitness under the existing reporting arrangements", "Health Service — risk assessment, then treating psychiatrist"),
 ("4",    "Restrictions, adjustments, duration and review date", "Dr Ma (GP)"),
 ("5",    "Meaning of “complaint handling”", "Health Service — already answered, then Dr Ma"),
 ("6",    "Requirements of the role without modification", "Health Service — identify genuine occupational requirements, then GP"),
 ("7",    "“Working memory affected under stress”", "Treating psychiatrist"),
 ("8",    "Tasks and environments that exacerbate the condition", "Dr Ma and the psychiatrist — a psychiatric question"),
 ("9",    "If unable to accommodate, whether safe return is possible", "Health Service — onus is the employer’s"),
]

def alloc_table():
    data = [[Paragraph("Q", S["cellB"]), Paragraph("SUBJECT", S["cellB"]),
             Paragraph("PROPOSED RESPONDENT", S["cellB"])]]
    for q, subj, who in ALLOC:
        data.append([Paragraph(esc(q), S["cellB"]),
                     Paragraph(esc(subj), S["cellL"]),
                     Paragraph(esc(who), S["cellL"])])
    t = Table(data, colWidths=[14*mm, 74*mm, 74*mm], repeatRows=1)
    st = [("VALIGN", (0,0), (-1,-1), "TOP"),
          ("BACKGROUND", (0,0), (-1,0), BAND),
          ("LINEBELOW", (0,0), (-1,0), 0.6, RULE),
          ("LINEBELOW", (0,1), (-1,-2), 0.25, colors.HexColor("#DDDDDD")),
          ("BOX", (0,0), (-1,-1), 0.6, RULE),
          ("TOPPADDING", (0,0), (-1,-1), 3.5),
          ("BOTTOMPADDING", (0,0), (-1,-1), 3.5),
          ("LEFTPADDING", (0,0), (-1,-1), 5),
          ("RIGHTPADDING", (0,0), (-1,-1), 5)]
    for i, (q, _, who) in enumerate(ALLOC, start=1):
        if who.startswith("Health Service"):
            st.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F6F6F6")))
    t.setStyle(TableStyle(st))
    return t

lines = open(SRC, encoding="utf-8").read().split("\n")
flow = []

# header block
flow.append(Paragraph("Response and Proposed Allocation of Questions", S["title"]))
flow.append(Paragraph("Request for Medical Information dated 31 July 2026", S["sub"]))
meta = ("<b>Employee:</b> Cory Lea Shepherd, AO3, Switchboard Services, Logan Hospital<br/>"
        "<b>Reference:</b> MSH-INJ-5795 &#183; CLM-317073<br/>"
        "<b>Request signed by:</b> Mr Scott Hughes, Director, Corporate Services, LBHS &#8212; 31 July 2026<br/>"
        "<b>Response date:</b> ______________________")
flow.append(Paragraph(meta, S["meta"]))
flow.append(Spacer(1, 5))
flow.append(HRFlowable(width="100%", thickness=0.8, color=RULE, spaceAfter=2))

i = 0
# skip source header up to first separator
while i < len(lines) and not lines[i].startswith("------"):
    i += 1

buf, mode = [], "body"
in_table = False

def flush():
    global buf, mode
    if not buf:
        return
    txt = " ".join(x.strip() for x in buf).strip()
    buf = []
    if not txt:
        return
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

    if s == "IN SUMMARY" or re.match(r"^PART \d+", s):
        flush()
        flow.append(Paragraph(esc(s), S["h1"]))
        continue

    if re.match(r"^\d+\.\d+\s+[A-Z]", s):
        flush()
        flow.append(Paragraph(esc(s), S["h2"]))
        continue

    # the ASCII allocation table -> real table
    if s.startswith("Q") and "SUBJECT" in s and "RESPONDENT" in s:
        flush()
        flow.append(Spacer(1, 2))
        flow.append(alloc_table())
        flow.append(Spacer(1, 6))
        # consume the ASCII rows: skip to the paragraph after the table block
        while i < len(lines) and not lines[i].strip().startswith("Of the nine questions"):
            i += 1
        continue

    if s.startswith("→") or s.startswith("→"):
        flush()
        mode = "arrow"
        buf = [s]
        # continuation lines
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^\s*(→|→|\(|PART|\d+\.\d+)", lines[i]) and lines[i].startswith("    "):
            buf.append(lines[i]); i += 1
        flush()
        continue

    if re.match(r"^\([a-z0-9]+\)\s", s) or re.match(r"^[0-9]+\.\s", s):
        flush()
        mode = "item"
        buf = [s]
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^\s*(\(|→|→|PART|\d+\.\d+|Q\d)", lines[i].strip()) and lines[i].startswith("    "):
            buf.append(lines[i]); i += 1
        flush()
        continue

    if re.match(r"^Q\d\(?[a-d]?\)?\s{2,}", s):
        flush()
        mode = "qref"
        buf = [s]
        while i < len(lines) and lines[i].strip() and lines[i].startswith("       "):
            buf.append(lines[i]); i += 1
        flush()
        continue

    if ln.startswith("    “") or ln.startswith('    "'):
        flush()
        mode = "quote"
        buf = [s]
        while i < len(lines) and lines[i].strip() and lines[i].startswith("    "):
            buf.append(lines[i]); i += 1
        flush()
        continue

    buf.append(s)

flush()

def deco(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 7.2)
    canv.setFillColor(MUTE)
    canv.drawString(18*mm, 12*mm, "Cory Lea Shepherd · MSH-INJ-5795 · Response to Request for Medical Information of 31 July 2026")
    canv.drawRightString(192*mm, 12*mm, "Page %d" % doc.page)
    canv.setStrokeColor(RULE); canv.setLineWidth(0.4)
    canv.line(18*mm, 15*mm, 192*mm, 15*mm)
    canv.restoreState()

doc = BaseDocTemplate(RAW, pagesize=A4,
                      leftMargin=18*mm, rightMargin=18*mm,
                      topMargin=16*mm, bottomMargin=20*mm,
                      title="Response and Proposed Allocation of Questions",
                      author="", subject="", creator="", producer="")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=deco)])
doc.build(flow)

subprocess.run(["qpdf", "--empty", "--pages", RAW, "1-z", "--", OUT], check=True)
import pikepdf
with pikepdf.open(OUT, allow_overwriting_input=True) as p:
    p.trailer.get("/Info") and p.trailer.__delitem__("/Info")
    if "/Metadata" in p.Root:
        del p.Root["/Metadata"]
    p.save(OUT)
print("built", OUT)
