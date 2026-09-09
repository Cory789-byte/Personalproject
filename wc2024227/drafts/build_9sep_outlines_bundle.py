#!/usr/bin/env python3
"""WC/2024/227 — the three outlines of evidence, stitched into one PDF for the Respondent.

⛔ DIRECTION 2 MATERIAL ONLY. Serve on the Respondent. DO NOT FILE in the Industrial Registry.
The list of witnesses is NOT in this bundle: it is a direction 1 document, it is filed in the
Registry, and it stays a separate one-page file so the two directions never travel together.

The four documents are reproduced page for page exactly as served, with nothing added to their
pages, so any page taken out of this bundle is the served document. Only the contents page in
front of them is new.

Run build_9sep_final.py first; this reads its output.
"""
import io, os
import pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

F = "out/FINAL_9SEP2026"
OUT = "out/OUTLINES_OF_EVIDENCE_9SEP2026.pdf"

HD = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.6, leading=11,
                    textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2 = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=12)
TITLE = ParagraphStyle('TITLE', fontName='Helvetica-Bold', fontSize=13, leading=16.5, spaceAfter=4)
WARN = ParagraphStyle('WARN', fontName='Helvetica-Bold', fontSize=9.4, leading=12.6,
                      textColor=colors.HexColor('#8a2010'), spaceAfter=8)
B = ParagraphStyle('B', fontName='Helvetica', fontSize=9.4, leading=12.6, spaceAfter=6)
C = ParagraphStyle('C', parent=B, fontSize=9.0, leading=11.6, spaceAfter=0)
CB = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')

# file, description, direction
DOCS = [
    (f"{F}/2_REGULATOR/Outline_of_Evidence_Cory_Lea_Shepherd_WC2024227.pdf",
     "Outline of evidence &ndash; Mr Cory Lea Shepherd (Appellant)",
     "Direction 2 &ndash; served, not filed"),
    (f"{F}/2_REGULATOR/Outline_of_Evidence_Cory_Harrison-Jones_WC2024227.pdf",
     "Outline of evidence &ndash; Mr Cory Harrison-Jones",
     "Direction 2 &ndash; served, not filed"),
    (f"{F}/2_REGULATOR/Outline_of_Evidence_Patricia_Conaghan_WC2024227.pdf",
     "Outline of evidence &ndash; Ms Patricia Conaghan",
     "Direction 2 &ndash; served, not filed"),
]

# work out the page each document starts on (contents page is page 1)
srcs, start, page = [], [], 2
for path, desc, direction in DOCS:
    if not os.path.exists(path):
        raise SystemExit(f"missing: {path} — run build_9sep_final.py first")
    pdf = pikepdf.open(path)
    srcs.append(pdf)
    start.append(page)
    page += len(pdf.pages)
total = page - 1

rows = [[Paragraph("Page", CB), Paragraph("Document", CB), Paragraph("Direction", CB)]]
for (path, desc, direction), p, pdf in zip(DOCS, start, srcs):
    n = len(pdf.pages)
    label = str(p) if n == 1 else f"{p}&ndash;{p+n-1}"
    rows.append([Paragraph(label, C), Paragraph(desc, C), Paragraph(direction, C)])

W = A4[0] - 44*mm
t = Table(rows, colWidths=[16*mm, W - 16*mm - 58*mm, 58*mm], repeatRows=1)
t.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#999999')),
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EEEEEE')),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
]))

story = [
    Paragraph("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", HD),
    Paragraph("Matter No. WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' "
              "Compensation Regulator (Respondent)", HD2),
    Paragraph("APPELLANT'S OUTLINES OF EVIDENCE", TITLE),
    Paragraph("Served on the Respondent under direction 2 of the Further Directions Order (3) dated "
              "19 August 2026, one A4 page per witness.", B),
    Paragraph("Direction 2 material. Served on the Respondent and not filed in the Industrial Registry. "
              "The Appellant's list of names of all witnesses is a direction 1 document and is filed in the "
              "Registry as a separate one-page document; it is not part of this bundle.", WARN),
    Spacer(1, 3*mm),
    t,
    Spacer(1, 5*mm),
    Paragraph("Each document is reproduced exactly as served. The outlines state the topics on which "
              "each witness will give oral evidence; they are not statements of evidence and are not "
              "verified. No expert report has been prepared for the purposes of this proceeding: the "
              "treating material relied upon is identified in the Appellant's schedule of medical "
              "documents, served with this bundle.", B),
    Spacer(1, 8*mm),
    Paragraph("Dated 9 September 2026", B),
    Paragraph("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented", B),
]

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=22*mm, rightMargin=22*mm,
                      topMargin=16*mm, bottomMargin=16*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[
    Frame(22*mm, 16*mm, A4[0]-44*mm, A4[1]-32*mm, leftPadding=0, rightPadding=0,
          topPadding=0, bottomPadding=0)])])
doc.build(story)
buf.seek(0)
cover = pikepdf.open(buf)
if len(cover.pages) != 1:
    raise SystemExit(f"contents page ran to {len(cover.pages)} pages; it must be one")

out = pikepdf.Pdf.new()
for pg in cover.pages:
    out.pages.append(pg)
for pdf in srcs:
    for pg in pdf.pages:
        out.pages.append(pg)

# `total` already counts the contents page: page numbering started the first document at 2
if len(out.pages) != total:
    raise SystemExit(f"page count {len(out.pages)} does not match the contents page ({total})")

try:
    del out.Root.Metadata
except (AttributeError, KeyError):
    pass
with out.open_metadata(set_pikepdf_as_editor=False) as m:
    m.clear()
try:
    del out.Root.Metadata
except (AttributeError, KeyError):
    pass
for k in list(out.docinfo.keys()):
    del out.docinfo[k]
for pg in out.pages:
    for k in ('/Metadata', '/PieceInfo', '/Annots'):
        if k in pg.obj:
            del pg.obj[k]
out.save(OUT, linearize=True)

# put it where the emails attach from, and mirror it into the numbered folder
import shutil
for dest in (f"{F}/2_REGULATOR/Outlines_of_Evidence_WC2024227.pdf",
             "out/SEND_9SEP2026/06_OUTLINES_OF_EVIDENCE.pdf",
             "out/SEND_9SEP2026/TO_MATHESON_9SEP2026/06_OUTLINES_OF_EVIDENCE.pdf"):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copy2(OUT, dest)

chk = pikepdf.open(OUT)
clean = (not dict(chk.docinfo)) and '/Metadata' not in chk.Root and \
        not any('/Annots' in p.obj for p in chk.pages)
print(f"built {OUT} — {len(chk.pages)} pages, {'clean' if clean else 'METADATA SURVIVED'}")
for (path, desc, _), p in zip(DOCS, start):
    print(f"  page {p:>2}  {os.path.basename(path)}")
if not clean:
    raise SystemExit("metadata survived — do not serve")
