#!/usr/bin/env python3
"""WC/2024/227 — Notice to Admit Facts, extracted for the clinician pack.

Produces the full Notice (the 50 facts) together with the Respondent's Response, so the clinician
can see what was asked and what was answered — with items 26 to 31 withheld.

Items 26 to 31 are withheld because they are the appellant's own complaint about the disclosure
of intimate medical particulars in the appeal. They bear on nothing clinical. They are replaced by
a visible notation so the extract is transparent on its face and nothing appears concealed.

⭐ ITEM 20 (the Ethical Standards Unit determination) IS NOW INCLUDED — Cory's instruction,
16 August. It is an accepted fact and it belongs in the occupational history.
⛔ Item 21's parenthetical — "48 hours after the Appellant lodged the PID complaint" — REMAINS
removed. The retraction direction of 15 May 2024 stays visible; the temporal linkage does not.
"""
import io, pikepdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

SRC = "../documents/2026-02-18_Form24_Response_and_email_communication.pdf"
OUT = "out/ATTACHMENT_1_Regulator_Response_18Feb2026_EXTRACT.pdf"
PH = 792.0                      # letter height, points

# Bands measured from the page-3 text layer (pdftotext -bbox, y from page top).
# Converted to reportlab coordinates (y from page bottom) at build time.
BANDS = [
    # (x0, top_y_from_page_top, x1, bottom_y_from_page_top, label)
    # ⭐ Item 20 (the Ethical Standards Unit determination) is NO LONGER WITHHELD — Cory's
    #    instruction, 16 Aug: it is an accepted fact and belongs in the occupational history.
    #    The letter of instruction states it as a bare fact in Part B2, so the attachment must
    #    show it; a letter that states a fact the attachment blanks out is worse than either.
    (98.0, 478.0, 470.0, 750.0,
     "Items 26 to 31 — not provided: not relevant to the medical questions"),
    # ⛔ item 21 STILL has line 1 cleared and redrawn without the parenthetical. The retraction
    #    direction stays visible; the "48 hours after the Appellant lodged the PID complaint"
    #    linkage does not. The PID goes in as a bare fact, not as the first element of a
    #    reprisal argument put to a treating psychiatrist.
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
# ══════════════════════════════════════════════════════════════════════════════════════════
# ⛔⛔⛔ REAL REDACTION — 16 August 2026.
# A white rectangle drawn over text HIDES it; it does not REMOVE it. Verified: pdftotext on the
# earlier build recovered "Lomotil", "Proctosedyl", the full sentence structure of items 26–31,
# and — worse — item 21's stripped parenthetical, "…hours after the Appellant lodged the PID
# complaint)". Anyone with a text extractor, or a copy-paste, had all of it.
# ⇒ Page 3 is therefore RASTERISED: the page is rendered to an image and the image replaces the
#   page, so the text layer on that page ceases to exist. That is what redaction means.
# ⚠ Page 3 is consequently not selectable or searchable. That is the correct trade and it is what
#   a properly redacted exhibit looks like.
# ══════════════════════════════════════════════════════════════════════════════════════════
import os, subprocess, tempfile, img2pdf

tmp = tempfile.mkdtemp()
staged = os.path.join(tmp, "staged.pdf")
pdf.save(staged, linearize=True)
pdf.close()

subprocess.run(["pdftoppm", "-r", "200", "-png", "-f", "3", "-l", "3",
                staged, os.path.join(tmp, "p")], check=True)
png = [f for f in sorted(os.listdir(tmp)) if f.startswith("p") and f.endswith(".png")][0]
raster_pdf = os.path.join(tmp, "raster.pdf")
with open(raster_pdf, "wb") as fh:
    fh.write(img2pdf.convert(os.path.join(tmp, png),
                             layout_fun=img2pdf.get_fixed_dpi_layout_fun((200, 200))))

final = pikepdf.open(staged)
rast  = pikepdf.open(raster_pdf)
final.pages[2] = rast.pages[0]                 # replace page 3 with its rasterised self
with final.open_metadata(set_pikepdf_as_editor=False) as meta:
    meta.clear()
    meta["dc:title"] = "WC/2024/227 — Response of the Workers' Compensation Regulator (extract)"
    meta["dc:creator"] = ["Cory Lea Shepherd"]
final.save(OUT, linearize=True)
print("built", OUT, "pages:", len(final.pages), "— page 3 rasterised, text layer removed")
