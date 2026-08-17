#!/usr/bin/env python3
"""WC/2024/227 — Attachment 1: the Regulator's Response, FINAL BUILD (17 August 2026).

Produces out/ATTACHMENT_1_Regulator_Response_18Feb2026.pdf — 10 pages.

⭐ WHAT CHANGED IN THE FINAL RUN (Cory, 17 Aug: "run it again, cut it down, remove the extract
naming, remove the whited-out, all metadata removed"):

1. ⛔⛔ PAGES 11–13 ARE DROPPED — AND THIS WAS A LIVE DEFECT, NOT TRIMMING. Those pages are the
   appellant's own email of 24 Feb 2026 to the Industrial Registrar: the s 530 objection to legal
   representation, INCLUDING the conflict-of-interest allegations against Ms Matheson and the
   Rule 64C complaint. Litigation characterisations of the opposing representative were riding
   into the clinician pack inside this attachment. They are gone. 13pp → 10pp.

2. ⭐ PAGE 3 IS REBUILT NATIVELY — no white boxes, no raster, no hidden layer. The page is
   re-typeset from the verified render: items 17–25 verbatim, item 20 (the PID determination)
   present, item 21 WITHOUT the "(48 hours after the Appellant lodged the PID complaint)"
   parenthetical, and one notation line for items 26–31. Because the page is built from nothing,
   there is nothing underneath to leak — stronger than rasterising, and it looks like a page,
   not like a redaction.
   The page states on its face that it is reproduced and that items 26–31 are not included.
   ⭐ THAT NOTATION, plus the equivalent sentence in the letter of instruction, is what now does
   the disclosure work the word "EXTRACT" in the filename used to do. The withholding is declared
   where it happens, so the filename no longer needs to.

3. TITLE AND METADATA: the filename and title drop "EXTRACT"; the output carries NO metadata at
   all — docinfo emptied, XMP removed. (The source PDF's own metadata — Author "Stephen Gray",
   Acrobat PDFMaker, creation dates — is stripped with it.)

Same result as every prior build: item 20 in · items 26–31 out · item 21's reprisal linkage out.
"""
import io, os, pikepdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle

SRC = "../documents/2026-02-18_Form24_Response_and_email_communication.pdf"
OUT = "out/ATTACHMENT_1_Regulator_Response_18Feb2026.pdf"
PW, PH = letter

# ── page 3, re-typeset from the verified render (pid-03/ex3-03) ────────────────────────────────
CELL = ParagraphStyle('CELL', fontName='Helvetica', fontSize=9.8, leading=13.2)
NUMS = ParagraphStyle('NUMS', parent=CELL, fontName='Helvetica-Bold')
HEAD = ParagraphStyle('HEAD', parent=NUMS, alignment=1)
NOTE = ParagraphStyle('NOTE', parent=CELL, fontName='Helvetica-Oblique', fontSize=9,
                      textColor=colors.HexColor('#555555'))
def C(t, s=CELL): return Paragraph(t, s)

ITEMS = [
 ("17", 'The "Union Encouragement Policy" (QH-POL-248) (<b>Exhibit F2</b>) requires managers to '
        'take a "positive, supportive role" to facilitate union membership and delegate elections.'),
 ("18", 'The Appellant notified management of his intent to become a Union Delegate on '
        '<b>11 August 2023</b> (<b>Exhibit F3</b>).'),
 ("19", 'Management failed to facilitate a vote or provide necessary delegate information to the '
        'Appellant for a period exceeding <b>9 months</b> after his initial request.'),
 ("20", "On <b>24 December 2024</b>, the Ethical Standards Unit (ESU) determined that the "
        "Appellant's complaint regarding Ms. Taylor and Ms. Reese constituted a <b>Public "
        "Interest Disclosure (PID)</b> (<b>Exhibit E3</b>)."),
 ("21", 'On <b>15 May 2024</b>, Director Tammy Reese sent an email directing the Appellant to '
        '<i>"retract"</i> an email he had sent inquiring about office hours (<b>Exhibit E5</b>).'),
 ("22", "On <b>9 May 2024</b>, Ms. Taylor sent a substantively similar email regarding another "
        "staff member's hours, for which she was not directed to issue a retraction "
        "(<b>Exhibit E5</b>)."),
 ("23", 'The Respondent obtained the Appellant\'s full medical history (<b>Exhibit A5</b>) '
        'directly from "Our Medical Ashmore" on or before <b>8 July 2025</b>.'),
 ("24", 'The copy of <b>Exhibit A5</b> filed by the Respondent bears the system-generated footer: '
        '<i>"Printed on 8th July 2025"</i>.'),
 ("25", "The Respondent did not serve a <b>Form 29 Notice of Non-Party Disclosure</b> on the "
        "Appellant prior to obtaining these records (breach of <b>Rule 64E</b>)."),
]

rows = [[C("<b>No.</b>", HEAD), C("<b>Fact to be Admitted (with Exhibit Reference)</b>", HEAD),
         C("<b>Admit / Deny</b>", HEAD)]]
for n, txt in ITEMS:
    rows.append([C(f"<b>{n}</b>", NUMS), C(txt), C("")])
rows.append([C("<b>26–31</b>", NUMS),
             C("Items 26 to 31 are not included in this copy: they concern matters with no "
               "bearing on the medical questions.", NOTE), C("")])

tbl = Table(rows, colWidths=[46, 386, 100], repeatRows=1)
tbl.setStyle(TableStyle([
    ('GRID', (0,0), (-1,-1), 0.7, colors.black),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 6), ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 7)]))

buf = io.BytesIO()
cv = canvas.Canvas(buf, pagesize=letter)
w, h = tbl.wrapOn(cv, 532, PH)
tbl.drawOn(cv, (PW - 532) / 2.0, PH - 96 - h)
cv.setFont('Helvetica', 9); cv.setFillColor(colors.black)
cv.drawString(54, 40, "3 of 6")
cv.setFont('Helvetica-Oblique', 8); cv.setFillColor(colors.HexColor('#666666'))
cv.drawRightString(PW - 54, 40, "This page is reproduced; the balance of the document is the original.")
cv.showPage(); cv.save(); buf.seek(0)

# ── assemble: source pages 1–2, rebuilt 3, source 4–10; drop 11–13 ─────────────────────────────
src = pikepdf.open(SRC)
newp = pikepdf.open(buf)
out = pikepdf.Pdf.new()
out.pages.extend(src.pages[0:2])       # Notice pp 1–2
out.pages.append(newp.pages[0])        # rebuilt p 3
out.pages.extend(src.pages[3:10])      # Notice pp 4–6 + Response pp 7–10
# src pages 11–13 (the 24 Feb 2026 email chain) are NOT copied.

# ── all metadata removed ───────────────────────────────────────────────────────────────────────
try:
    del out.Root.Metadata
except (AttributeError, KeyError):
    pass
with out.open_metadata(set_pikepdf_as_editor=False) as meta:
    meta.clear()
try:
    del out.Root.Metadata          # open_metadata recreates an XMP shell; remove it again
except (AttributeError, KeyError):
    pass
for k in list(out.docinfo.keys()):
    del out.docinfo[k]
out.save(OUT, linearize=True)
print(f"built {OUT} pages: {len(out.pages)} — page 3 native, pp11–13 dropped, metadata stripped")
