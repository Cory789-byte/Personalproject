#!/usr/bin/env python3
"""WC/2024/227 - Tab 32: the documents Metro South Health enclosed with its letter of
5 June 2026 to Commissioner Dwyer (K-LM26/729, Annexure A Tab 20), Items 6 and 13.
Stitched behind a one-page index. No document is annotated, highlighted or altered,
other than identification headers and page numbers. Metadata stripped.
Run from wc2024227/drafts:  python3 build_tab32.py
"""
import io, os, pikepdf
import pymupdf as fitz
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

SRC = "../documents/disclosure-2026-06_MSH_production"
OUT_DIR = "out/TAB32"
OUT = f"{OUT_DIR}/WC2024227_Tab32_MSH_enclosures_ManagerRole_and_Delegation.pdf"

PARTS = [
    ("32A", "Role Description, Manager Switchboard Services, Logan Hospital (AO4), "
            "RD 30478699. Enclosed by Metro South Health under Item 6",
     "as at 2021", "Item 6 Role description Switchboard manager as at 2021.pdf"),
    ("32B", "Instrument of Human Resource Sub-Delegation, COVID-19 Pandemic Event - Paid "
            "Special Pandemic Leave, signed by Ms N Cridland, A/Health Service Chief Executive. "
            "Enclosed under Item 13. (The same instrument is at Tab 29, admitted 8 September 2026.)",
     "signed 23 Nov 2022; effective 5 Dec 2022",
     "item 13 delegation-hr-covid-directive-special-and-pandemic-leave-51222.pdf"),
]

H1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=12.5, leading=16, spaceAfter=3)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.6, leading=11.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=6)
B = ParagraphStyle('B', fontName='Helvetica', fontSize=9, leading=12.4, spaceAfter=4)
C = ParagraphStyle('C', fontName='Helvetica', fontSize=8.2, leading=11)
CH = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
P = lambda t, s=C: Paragraph(t, s)

srcs = [(tab, d, dt, pikepdf.open(os.path.join(SRC, f))) for tab, d, dt, f in PARTS]

def index_pdf():
    rows = [[P("Tab", CH), P("Document", CH), P("Date", CH), P("Pages", CH), P("At", CH)]]
    at = 2
    for tab, d, dt, sp in srcs:
        n = len(sp.pages)
        rows.append([P(tab), P(d), P(dt), P(str(n)), P(f"{at}-{at+n-1}" if n > 1 else str(at))])
        at += n
    t = Table(rows, colWidths=[12*mm, 104*mm, 30*mm, 13*mm, 19*mm], repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#999999')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dddddd')), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4), ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5)]))
    st = [P("Tab 32 - documents enclosed with Metro South Health's letter of 5 June 2026", H1),
          P("WC/2024/227 &middot; Shepherd v Workers' Compensation Regulator &middot; supplementary "
            "to Annexure A to the notices of 28 August 2026", SUB),
          P("By its letter of 5 June 2026 to Commissioner Dwyer, reference K-LM26/729 (Annexure A, "
            "Tab 20, confirmed by the Respondent on 24 September 2026), Metro South Hospital and "
            "Health Service enclosed the documents below in response to the notice of non-party "
            "disclosure: under Item 6, \"the attached Role Description for Manager of Switchboard "
            "Services\"; and under Item 13, the HR delegation for Paid Special Pandemic Leave signed "
            "23 November 2022.", B),
          Spacer(1, 2*mm), t, Spacer(1, 4*mm),
          P("Each document is reproduced as produced by Metro South Health. No document has been "
            "annotated, highlighted or altered, other than identification headers and page numbers.", B)]
    buf = io.BytesIO()
    doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                          topMargin=16*mm, bottomMargin=16*mm)
    doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(16*mm, 16*mm, A4[0]-32*mm, A4[1]-32*mm)])])
    doc.build(st); buf.seek(0)
    return pikepdf.open(buf)

os.makedirs(OUT_DIR, exist_ok=True)
pdf = pikepdf.new()
idx = index_pdf()
assert len(idx.pages) == 1, "index must be one page"
pdf.pages.extend(idx.pages)
starts = []
for tab, d, dt, sp in srcs:
    starts.append((tab, d, len(pdf.pages)))
    pdf.pages.extend(sp.pages)
with pdf.open_outline() as ol:
    ol.root.append(pikepdf.OutlineItem("Tab 32 - Index", 0))
    for tab, d, at in starts:
        ol.root.append(pikepdf.OutlineItem(f"Tab {tab} - {d[:70]}", at))
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
tmp = OUT + ".tmp"
pdf.save(tmp)

# identification header (tab + page within tab) and bundle page numbers
doc = fitz.open(tmp)
total = doc.page_count
bounds = [(tab, at) for tab, _, at in starts] + [(None, total)]
label = {}
for (tab, a), (_, b) in zip(bounds, bounds[1:]):
    for i in range(a, b):
        label[i] = f"WC/2024/227  -  Tab {tab}  -  page {i-a+1} of {b-a}"
for i, pg in enumerate(doc):
    r = pg.rect
    if i in label:
        w = fitz.get_text_length(label[i], fontname="helv", fontsize=8)
        pg.draw_rect(fitz.Rect(10, 4, 18 + w, 18), color=None, fill=(1, 1, 1), overlay=True)
        pg.insert_textbox(fitz.Rect(14, 6, r.width - 14, 20), label[i], fontname="helv",
                          fontsize=8, color=(0.25, 0.25, 0.25), align=0)
    ft = f"Tab 32  -  Page {i+1} of {total}"
    fw = fitz.get_text_length(ft, fontname="helv", fontsize=8)
    pg.draw_rect(fitz.Rect(r.width - 18 - fw, r.height - 19, r.width - 10, r.height - 4),
                 color=None, fill=(1, 1, 1), overlay=True)
    pg.insert_text((r.width - 14 - fw, r.height - 8), ft, fontname="helv", fontsize=8, color=(0.25, 0.25, 0.25))
doc.set_metadata({})
doc.save(OUT, garbage=3, deflate=True)
doc.close(); os.remove(tmp)
print(OUT, total, "pages")
for tab, d, at in starts: print(f"  {tab} starts at page {at+1}")
