#!/usr/bin/env python3
"""Stamp a matter footer + 'Page X of Y' onto each page of a PDF.
Usage: _stamp.py input.pdf "Form label" output.pdf [sign]
Pass a 4th arg "sign" to add a per-page deponent/witness signing footer
(QIRC affidavits: each page is signed by the deponent and the witness,
rr 50-57 Industrial Relations (Tribunals) Rules 2011)."""
import sys, subprocess, re, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

inp, label, outp = sys.argv[1], sys.argv[2], sys.argv[3]
sign = len(sys.argv) > 4 and sys.argv[4] == "sign"

# page count
info = subprocess.check_output(['pdfinfo', inp]).decode()
pages = int(re.search(r'Pages:\s+(\d+)', info).group(1))

W, H = A4
cm = 28.35
dots = "…" * 22
overlay = inp + '.ovl.pdf'
c = canvas.Canvas(overlay, pagesize=A4)
matter = "WC/2024/227  —  Shepherd v Workers' Compensation Regulator"
for i in range(1, pages + 1):
    c.setStrokeGray(0.6); c.setLineWidth(0.4)
    if sign:
        # per-page signing band (deponent + witness), above the matter line
        c.line(1.8 * cm, 1.9 * cm, W - 1.8 * cm, 1.9 * cm)
        c.setFont('Times-Roman', 8); c.setFillGray(0.15)
        c.drawString(1.8 * cm, 1.45 * cm, f"Deponent: {dots}")
        c.drawRightString(W - 1.8 * cm, 1.45 * cm, f"Witness (JP / C.dec / Lawyer): {dots}")
        c.setFont('Times-Roman', 7); c.setFillGray(0.4)
        c.drawString(1.8 * cm, 0.78 * cm, matter)
        c.drawRightString(W - 1.8 * cm, 0.78 * cm, f"{label}  —  Page {i} of {pages}")
    else:
        c.line(1.8 * cm, 1.4 * cm, W - 1.8 * cm, 1.4 * cm)
        c.setFont('Times-Roman', 8); c.setFillGray(0.35)
        c.drawString(1.8 * cm, 1.0 * cm, matter)
        c.drawRightString(W - 1.8 * cm, 1.0 * cm, f"{label}  —  Page {i} of {pages}")
    c.showPage()
c.save()

subprocess.check_call(['qpdf', '--overlay', overlay, '--', inp, outp])
os.remove(overlay)
print(f"stamped {pages}pp -> {outp}")
