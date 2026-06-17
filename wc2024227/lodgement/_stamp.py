#!/usr/bin/env python3
"""Stamp a matter footer + 'Page X of Y' onto each page of a PDF.
Usage: _stamp.py input.pdf "Form label" output.pdf"""
import sys, subprocess, re, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

inp, label, outp = sys.argv[1], sys.argv[2], sys.argv[3]

# page count
info = subprocess.check_output(['pdfinfo', inp]).decode()
pages = int(re.search(r'Pages:\s+(\d+)', info).group(1))

W, H = A4
overlay = inp + '.ovl.pdf'
c = canvas.Canvas(overlay, pagesize=A4)
matter = "WC/2024/227  —  Shepherd v Workers' Compensation Regulator"
for i in range(1, pages + 1):
    c.setFont('Times-Roman', 8)
    c.setFillGray(0.35)
    # thin rule above footer
    c.setStrokeGray(0.6); c.setLineWidth(0.4)
    c.line(1.8 * 28.35, 1.4 * 28.35, W - 1.8 * 28.35, 1.4 * 28.35)
    c.drawString(1.8 * 28.35, 1.0 * 28.35, matter)
    c.drawRightString(W - 1.8 * 28.35, 1.0 * 28.35, f"{label}  —  Page {i} of {pages}")
    c.showPage()
c.save()

subprocess.check_call(['qpdf', '--overlay', overlay, '--', inp, outp])
os.remove(overlay)
print(f"stamped {pages}pp -> {outp}")
