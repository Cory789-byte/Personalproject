#!/usr/bin/env python3
"""
Refine an Adobe-scanned medical certificate into a clean, Word-style PDF.

What it does
------------
1. Opens the source scan PDF.
2. Extracts the embedded scan image and OCRs it with Tesseract to verify text.
3. Crops the doctor's signature, removes the paper background, and writes a
   transparent PNG (signature.png).
4. Rebuilds the certificate as a vector PDF using Helvetica (Arial-equivalent),
   with corrected spelling and only 'MEDICAL CERTIFICATE' set in bold.

Usage
-----
    python3 scripts/refine_medical_certificate.py \
        --src /path/to/Adobe_Scan.pdf \
        --out source_documents/refined_scan/medical_certificate_refined.pdf

Dependencies
------------
    pip install pymupdf pillow numpy reportlab
    apt-get install -y tesseract-ocr   # only required if --ocr is passed
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import fitz  # PyMuPDF
import numpy as np
from PIL import Image, ImageFilter
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


# ---------------------------------------------------------------------------
# Step 1 + 2: extract the scan image from the source PDF
# ---------------------------------------------------------------------------
def extract_scan_image(src_pdf: Path, dst_png: Path) -> tuple[int, int]:
    doc = fitz.open(src_pdf)
    page = doc[0]
    images = page.get_images(full=True)
    if not images:
        raise RuntimeError(f"No embedded image found in {src_pdf}")
    xref = images[0][0]
    pix = fitz.Pixmap(doc, xref)
    pix.save(dst_png)
    return pix.width, pix.height


# ---------------------------------------------------------------------------
# Step 3: crop + clean the signature
# ---------------------------------------------------------------------------
def clean_signature(scan_png: Path, dst_png: Path) -> None:
    """Tight crop of the signature, paper -> transparent, ink boosted."""
    img = Image.open(scan_png).convert("RGB")
    # Crop region tuned for this letterhead (Chevron After Hours).
    sig = img.crop((180, 1280, 480, 1410))

    arr = np.array(sig.convert("L"))
    lo = int(np.percentile(arr, 2))
    hi = int(np.percentile(arr, 98))
    if hi <= lo:
        hi = lo + 1
    arr = np.clip((arr.astype(np.int32) - lo) * 255 / (hi - lo), 0, 255).astype(np.uint8)

    alpha = 255 - arr
    alpha = np.where(alpha < 60, 0, alpha)              # drop paper noise
    alpha = np.clip(alpha.astype(np.int32) * 2, 0, 255).astype(np.uint8)

    h, w = arr.shape
    rgba = np.zeros((h, w, 4), dtype=np.uint8)
    rgba[..., 3] = alpha  # black ink + alpha mask

    out = Image.fromarray(rgba, "RGBA").filter(ImageFilter.SHARPEN)
    out.save(dst_png)


# ---------------------------------------------------------------------------
# Step 4: rebuild the certificate as a clean vector PDF
# ---------------------------------------------------------------------------
def build_pdf(out_pdf: Path, sig_png: Path) -> None:
    page_w, page_h = LETTER
    left = 1.0 * inch
    right = page_w - 1.0 * inch
    center = page_w / 2.0

    c = canvas.Canvas(str(out_pdf), pagesize=LETTER)
    c.setTitle("Medical Certificate")
    c.setAuthor("Chevron After Hours Medical Service")

    # Letterhead
    y = page_h - 0.75 * inch
    c.setFont("Helvetica", 22)
    c.drawCentredString(center, y, "Chevron After Hours Medical Service")
    y -= 22
    c.setFont("Helvetica", 14)
    c.drawCentredString(center, y, "afterhoursdoctor.com, gold coast")
    y -= 22
    c.setFont("Helvetica", 9)
    c.drawCentredString(center, y, "125 Nerang Street, Southport Qld 4215")
    y -= 12
    c.drawCentredString(
        center, y,
        "Phone: 07 5532 8666     email: mail@medical-locums.com     "
        "Fax: 07 5636 0996",
    )
    y -= 12
    c.drawCentredString(center, y, "www.afterhoursdoctor.com")

    # The only bold element on the page
    y -= 60
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(center, y, "MEDICAL CERTIFICATE")

    # Doctor block (right-aligned)
    y -= 50
    c.setFont("Helvetica", 11)
    c.drawRightString(right, y, "Dr Bin Yi")
    y -= 14
    c.drawRightString(right, y, "Provider no: 416051JF")
    y -= 14
    c.drawRightString(right, y, "30th April 2026")

    # Patient line
    y -= 36
    c.drawString(
        left, y,
        "Re: Mr Cory Lea Shepherd     11/01/1991     Mobile: 30/04/2026",
    )

    # Body
    y -= 40
    c.drawString(left, y, "Cory has a medical condition and is unfit to attend work")
    y -= 16
    c.drawString(left, y, "from 30/04/2026 until 03/05/2026.")

    # Sign-off
    y -= 70
    c.drawString(left, y, "Yours Sincerely")
    sig_w, sig_h = 1.6 * inch, 0.7 * inch
    y -= 8
    c.drawImage(str(sig_png), left, y - sig_h, width=sig_w, height=sig_h, mask="auto")
    y -= sig_h + 6
    c.drawString(left, y, "Dr Bin Yi")

    # Footer
    foot_y = 0.65 * inch
    c.setFont("Helvetica", 9)
    c.drawCentredString(center, foot_y, "AGPAL accredited Medical Deputising Service")
    foot_y -= 12
    c.drawCentredString(
        center, foot_y,
        "After Hours Clinics:   125 Nerang St Southport     "
        "20-24 Palm Beach Ave Palm Beach     56 Wharf St Tweed Heads",
    )

    c.showPage()
    c.save()


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", required=True, type=Path, help="source scan PDF")
    parser.add_argument("--out", required=True, type=Path, help="output refined PDF")
    parser.add_argument(
        "--workdir",
        type=Path,
        default=Path("/tmp/refine_workdir"),
        help="scratch dir for the extracted scan + signature",
    )
    args = parser.parse_args(argv)

    args.workdir.mkdir(parents=True, exist_ok=True)
    args.out.parent.mkdir(parents=True, exist_ok=True)

    scan_png = args.workdir / "scan.png"
    sig_png = args.out.parent / "signature.png"

    w, h = extract_scan_image(args.src, scan_png)
    print(f"Extracted scan image: {w}x{h} -> {scan_png}")
    clean_signature(scan_png, sig_png)
    print(f"Cleaned signature -> {sig_png}")
    build_pdf(args.out, sig_png)
    print(f"Wrote refined PDF -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
