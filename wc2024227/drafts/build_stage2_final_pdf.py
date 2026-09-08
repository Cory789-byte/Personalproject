"""Final Stage 2 referral PDF, in the style of the filed Stage 1 response
(RESPONSE_Stage1_Dispute_and_Leave_MSH-INJ-5795.pdf). Source of truth is
Cory's co-edited docx; three finishing changes are applied:
  1. The union placeholder section is removed and Arrangements renumbered 5->4
     (his standing instruction: if the union section is not completed, remove
     it and proceed).
  2. "That date has passed" -> "That date has been reached" (true whether sent
     on 10 August or after), and the cl 1.11.5 words set in quotation marks
     (they are the clause's verbatim text, quoted that way in the Stage 1
     notice).
  3. The DRAFT banner and To/Cc/Attachments block become the filed-style
     header; metadata scrubbed on the way out.
"""
import re, subprocess, zipfile, html
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, HRFlowable)

SRC = "/tmp/stage2_up/up.docx"
OUT = "/home/user/Personalproject/wc2024227/drafts/out/REFERRAL_Stage2_cl1.11.2b_MSH-INJ-5795.pdf"

# ---- extract paragraphs from the co-edited docx ----
z = zipfile.ZipFile(SRC)
xml = z.read("word/document.xml").decode()
text = html.unescape(re.sub(r"<[^>]+>", "", xml.replace("</w:p>", "\n")))
paras = [t.strip() for t in text.split("\n") if t.strip()]

# ---- finishing changes ----
out_paras = []
skip = False
for t in paras:
    if t.startswith("DRAFT FOR REVIEW"):
        continue
    if t.startswith(("To: ", "Cc: ", "Attachments: ", "Subject: ", "Dear Human Resources")):
        continue  # re-rendered in the header block
    if t.startswith("4  Union representation"):
        skip = True
        continue
    if skip:
        skip = False  # skip exactly the one bracketed paragraph after the heading
        continue
    if t.startswith("5  Arrangements"):
        t = "4  Arrangements"
    if "That date has passed" in t:
        t = t.replace(
            "That date has passed; the dispute remains unresolved; and this is that referral.",
            "That date has been reached, the dispute remains unresolved, and this is that referral.")
        t = t.replace(
            "Clause 1.11.5 provides that no party shall act in a manner unreasonably or intentionally delay the timely resolution of a dispute.",
            "Clause 1.11.5 provides that “no party shall act in a manner unreasonably or intentionally delay the timely resolution of a dispute”.")
    out_paras.append(t)

# ---- styles (house) ----
INK = colors.HexColor("#111111")
MUTE = colors.HexColor("#555555")
RULE = colors.HexColor("#999999")

S = {
 "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=13, leading=16.5,
                         textColor=INK, spaceAfter=3),
 "ref":   ParagraphStyle("ref", fontName="Helvetica", fontSize=8.8, leading=12,
                         textColor=MUTE, spaceAfter=2),
 "h1":    ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=10.4, leading=13.5,
                         textColor=INK, spaceBefore=13, spaceAfter=5),
 "body":  ParagraphStyle("body", fontName="Helvetica", fontSize=9.3, leading=13.4,
                         textColor=INK, alignment=TA_JUSTIFY, spaceAfter=7),
 "item":  ParagraphStyle("item", fontName="Helvetica", fontSize=9.3, leading=13.4,
                         textColor=INK, leftIndent=20, firstLineIndent=-20,
                         alignment=TA_JUSTIFY, spaceAfter=6),
 "sig":   ParagraphStyle("sig", fontName="Helvetica", fontSize=9.3, leading=13.4,
                         textColor=INK, spaceAfter=2),
 "schedh": ParagraphStyle("schedh", fontName="Helvetica-Bold", fontSize=8.8, leading=12,
                          textColor=MUTE, spaceBefore=14, spaceAfter=3),
 "sched": ParagraphStyle("sched", fontName="Helvetica", fontSize=8.4, leading=12,
                         textColor=MUTE, alignment=TA_JUSTIFY, spaceAfter=4),
}

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

flow = [
 Paragraph("Referral to Stage 2 — clause 1.11.2(b): attendance, roster, leave and pay from 26 June 2026", S["title"]),
 Paragraph("Cory Lea Shepherd, AO3 Switchboard Services, Logan Hospital · MSH-INJ-5795 · CLM-317073 · 10 August 2026", S["ref"]),
 Paragraph("To: LBH Human Resources · Copies: Ms Chloe Taylor, Manager, Switchboard Services; Mr Scott Hughes, Director, Corporate Services; LBH Injury Management; Mr Heath Moran and Ms Emily Petering, Together Queensland", S["ref"]),
 Paragraph("Attachments: (1) Notice of dispute, 3 August 2026; (2) Ms Taylor’s letter, 4 August 2026; (3) my response of 4 August 2026 (sent 5 August 2026)", S["ref"]),
 Spacer(1, 3),
 HRFlowable(width="100%", thickness=0.8, color=RULE, spaceAfter=8),
 Paragraph("Dear Human Resources team,", S["body"]),
]

in_sched = False
for t in out_paras:
    if t.startswith("Instruments and policies relied on"):
        in_sched = True
        flow.append(HRFlowable(width="100%", thickness=0.5, color=RULE, spaceBefore=10, spaceAfter=4))
        flow.append(Paragraph(esc(t), S["schedh"]))
        continue
    if in_sched:
        flow.append(Paragraph(esc(t), S["sched"]))
        continue
    if re.match(r"^\d\s\s", t):
        flow.append(Paragraph(esc(t), S["h1"]))
    elif re.match(r"^\d\.\d", t):
        flow.append(Paragraph(esc(t), S["item"]))
    elif t in ("Yours sincerely,",) or t.startswith("Cory Lea Shepherd") or \
         t.startswith("AO3, Switchboard") or "coryshepherd1@hotmail.com" in t:
        flow.append(Paragraph(esc(t), S["sig"]))
    else:
        flow.append(Paragraph(esc(t), S["body"]))

FOOT = "C Shepherd · MSH-INJ-5795 · Referral to Stage 2 — clause 1.11.2(b) · 10 August 2026"

def deco(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 7.2)
    canv.setFillColor(MUTE)
    canv.drawString(18*mm, 12*mm, FOOT)
    canv.drawRightString(192*mm, 12*mm, "Page %d" % doc.page)
    canv.setStrokeColor(RULE); canv.setLineWidth(0.4)
    canv.line(18*mm, 15*mm, 192*mm, 15*mm)
    canv.restoreState()

raw = "/tmp/_stage2_raw.pdf"
doc = BaseDocTemplate(raw, pagesize=A4,
                      leftMargin=18*mm, rightMargin=18*mm,
                      topMargin=16*mm, bottomMargin=20*mm,
                      title="Referral to Stage 2 - clause 1.11.2(b)",
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
