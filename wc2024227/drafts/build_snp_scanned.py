# -*- coding: utf-8 -*-
"""Flatten the SNP bundle into a single image-only PDF with a scanner pass."""
import datetime, io, random
import pypdfium2 as pdfium, pikepdf
from PIL import Image, ImageChops, ImageFilter
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas as _canvas

SRC = 'out/SNP_supporting_statement_two_periods_11SEP2026.pdf'
OUT = 'out/SNP_supporting_statement_two_periods_11SEP2026_SCANNED.pdf'
AUTHOR = 'Cory Shepherd'
TITLE = 'Supporting statement - two applications for sick leave without pay'
DPI = 200


def scanner_pass(im, seed):
    rnd = random.Random(seed)
    im = im.convert('L')
    # platen tone: paper never scans pure white, ink never pure black
    im = im.point(lambda v: max(9, min(247, int(9 + v * 0.945))))
    # optical softness of the lens
    im = im.filter(ImageFilter.GaussianBlur(0.35))
    # sheet-feed skew
    im = im.rotate(rnd.uniform(-0.26, 0.26), resample=Image.BICUBIC,
                   expand=False, fillcolor=242)
    w, h = im.size
    # sensor noise
    noise = Image.effect_noise((w, h), 8).point(lambda v: int(128 + (v - 128) * 0.30))
    im = ImageChops.add(im, noise, scale=1, offset=-128)
    # lid shadow falling away from the binding edge
    grad = Image.linear_gradient('L').rotate(270, expand=True).resize((w, h))
    grad = grad.point(lambda v: 255 - int((255 - v) * 0.06))
    im = ImageChops.multiply(im, grad)
    # faint edge darkening where the sheet lifts off the glass
    edge = Image.new('L', (w, h), 255)
    band = max(3, int(w * 0.006))
    for x in range(band):
        val = 255 - int((band - x) / band * 26)
        for col in (x, w - 1 - x):
            edge.paste(val, (col, 0, col + 1, h))
    for y in range(band):
        val = 255 - int((band - y) / band * 26)
        for row in (y, h - 1 - y):
            edge.paste(val, (0, row, w, row + 1))
    im = ImageChops.multiply(im, edge)
    return im


pdf = pdfium.PdfDocument(SRC)
pages = []
for i in range(len(pdf)):
    im = pdf[i].render(scale=DPI / 72.0).to_pil()
    im = scanner_pass(im, 1000 + i)
    buf = io.BytesIO()
    im.save(buf, 'JPEG', quality=78, optimize=True)
    buf.seek(0)
    pages.append(buf)
pdf.close()

c = _canvas.Canvas(OUT, pagesize=A4)
PW, PH = A4
for buf in pages:
    c.drawImage(ImageReader(buf), 0, 0, PW, PH, preserveAspectRatio=False)
    c.showPage()
c.save()

now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=10)
stamp = now.strftime("D:%Y%m%d%H%M%S+10'00'")
p = pikepdf.open(OUT, allow_overwriting_input=True)
if '/Metadata' in p.Root: del p.Root['/Metadata']
for k in ('/PieceInfo', '/Names', '/AcroForm', '/OpenAction', '/AA',
          '/StructTreeRoot', '/MarkInfo', '/Lang'):
    if k in p.Root: del p.Root[k]
for pg in p.pages:
    for k in ('/Metadata', '/PieceInfo', '/Annots', '/AA'):
        if k in pg.obj: del pg.obj[k]
for k in list(dict(p.docinfo)): del p.docinfo[k]
p.docinfo['/Author'] = AUTHOR
p.docinfo['/Title'] = TITLE
p.docinfo['/CreationDate'] = stamp
p.docinfo['/ModDate'] = stamp
p.save(OUT, linearize=False, fix_metadata_version=False,
       object_stream_mode=pikepdf.ObjectStreamMode.generate)
print('built', OUT)
