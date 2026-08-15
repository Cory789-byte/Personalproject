#!/usr/bin/env python3
"""WC/2024/227 — Notice to Admit Facts, extracted for the clinician pack.

Produces the full Notice (the 50 facts) together with the Respondent's Response, so the clinician
can see what was asked and what was answered — with items 20 and 26 to 31 withheld.

Those items are withheld because they are LITIGATION content, not clinical content:
  · item 20  — the Ethical Standards Unit determination (protected-disclosure territory)
  · items 26 to 31 — the appellant's own complaint about the disclosure of intimate
    medical particulars in the appeal
Neither bears on diagnosis, mechanism or capacity. Each is replaced by a visible notation so the
extract is transparent on its face and nothing appears concealed.
"""
import io, pikepdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

SRC = "../documents/2026-02-18_Form24_Response_and_email_communication.pdf"
OUT = "out/ATTACHMENT_1_Notice_and_Response_EXTRACT.pdf"
PH = 792.0                      # letter height, points

# Bands measured from the page-3 text layer (pdftotext -bbox, y from page top).
# Converted to reportlab coordinates (y from page bottom) at build time.
BANDS = [
    # (x0, top_y_from_page_top, x1, bottom_y_from_page_top, label)
    (98.0, 206.0, 470.0, 264.0,
     "Item 20 — not provided: not relevant to the medical questions"),
    (98.0, 478.0, 470.0, 750.0,
     "Items 26 to 31 — not provided: not relevant to the medical questions"),
    # item 21: clear line 1 and redraw it without the parenthetical
    (103.0, 264.0, 470.0, 281.5, ""),
]

buf = io.BytesIO()
c = canvas.Canvas(buf, pagesize=letter)
for x0, top, x1, bottom, label in BANDS:
    y = PH - bottom
    h = bottom - top
    c.setFillColor(colors.white)
    c.setStrokeColor(colors.white)
    c.rect(x0, y, x1 - x0, h, stroke=0, fill=1)
    if label:
        c.setFillColor(colors.HexColor('#666666'))
        c.setFont('Helvetica-Oblique', 8.5)
        c.drawString(x0 + 4, y + h - 13, label)
# item 21, line 1, redrawn without the parenthetical
c.setFillColor(colors.black)
c.setFont('Helvetica', 10)
c.drawString(104.9, PH - 277.5, "On ")
c.setFont('Helvetica-Bold', 10)
c.drawString(121.6, PH - 277.5, "15 May 2024")
c.setFont('Helvetica', 10)
c.drawString(183.6, PH - 277.5, ", Director")

c.showPage()
c.save()
buf.seek(0)

pdf = pikepdf.open(SRC, allow_overwriting_input=True)
ov = pikepdf.open(buf)
pdf.pages[2].add_overlay(ov.pages[0])          # page 3 of the Notice

with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
    meta.clear()
    meta["dc:title"] = "WC/2024/227 — Notice to Admit Facts and Respondent's Response (extract)"
    meta["dc:creator"] = ["Cory Lea Shepherd"]
pdf.save(OUT, linearize=True)
print("built", OUT, "pages:", len(pdf.pages))
