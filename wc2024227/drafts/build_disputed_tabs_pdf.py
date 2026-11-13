#!/usr/bin/env python3
"""Render DISPUTED-TABS-line-by-line-v-admissions.md to an internal PDF."""
import io, re, os, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer)

SRC = os.path.join(os.path.dirname(__file__), "..", "skill", "references",
                   "DISPUTED-TABS-line-by-line-v-admissions.md")
OUT = os.path.join(os.path.dirname(__file__), "INTERNAL", "DISPUTED_TABS_v_ADMISSIONS_14SEP2026.pdf")

REPL = {"⭐":"*", "⛔":"[!]", "⚠":"[caution]", "⇒":"=>", "️":"", "→":"->", "★":"*",
        "—":" - ", "–":"-", "…":"...", "\u2018":"'", "\u2019":"'", "\u201c":'"', "\u201d":'"',
        "¶":"\u00b6", "×":"x", "≈":"~"}
def clean(t):
    for k,v in REPL.items(): t = t.replace(k,v)
    t = t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(?!\s)(.+?)\*", r"<i>\1</i>", t)
    try: t.encode("latin-1")
    except UnicodeEncodeError:
        t = t.encode("latin-1", "replace").decode("latin-1")
    return t

H1 = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=12.5, leading=15, spaceBefore=10, spaceAfter=4)
H2 = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=10.5, leading=13, spaceBefore=8, spaceAfter=3)
BODY = ParagraphStyle('b', fontName='Helvetica', fontSize=8.6, leading=11.4, spaceAfter=2.5)
QUOTE = ParagraphStyle('q', parent=BODY, textColor=colors.HexColor('#444444'), leftIndent=5*mm, fontSize=8.0)
CELL = ParagraphStyle('c', fontName='Helvetica', fontSize=7.8, leading=10)
CELLH = ParagraphStyle('ch', parent=CELL, fontName='Helvetica-Bold')

story = [Paragraph("THE FOURTEEN DISPUTED TABS AGAINST THE ADMISSIONS", H1),
         Paragraph("WC/2024/227 · internal working document · 14 September 2026 · "
                   "<b>NOT FOR SERVICE OR FILING</b>", QUOTE), Spacer(1,4)]

lines = open(SRC).read().splitlines()
i=0; W=180*mm
while i < len(lines):
    ln = lines[i]
    if ln.startswith("| "):
        rows=[]
        while i < len(lines) and lines[i].startswith("|"):
            cells=[c.strip() for c in lines[i].strip().strip("|").split("|")]
            if not set("".join(cells)) <= set("-: "):
                rows.append(cells)
            i+=1
        n=len(rows[0])
        if n==2: widths=[W*0.44, W*0.56]
        elif n==3: widths=[W*0.10, W*0.45, W*0.45]
        else: widths=[W/n]*n
        data=[[Paragraph(clean(c), CELLH if r==0 else CELL) for c in row] for r,row in enumerate(rows)]
        t=Table(data, colWidths=widths, repeatRows=1)
        t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#aaaaaa')),
                               ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eef1f6')),
                               ('VALIGN',(0,0),(-1,-1),'TOP'),
                               ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
                               ('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
        story += [t, Spacer(1,3)]
        continue
    if ln.startswith("# "): story.append(Paragraph(clean(ln[2:]), H1))
    elif ln.startswith("## "): story.append(Paragraph(clean(ln[3:]), H2))
    elif ln.startswith("> "): story.append(Paragraph(clean(ln[2:]), QUOTE))
    elif ln.strip()=="---": story.append(Spacer(1,6))
    elif ln.strip(): story.append(Paragraph(clean(ln), BODY))
    i+=1

buf=io.BytesIO()
SimpleDocTemplate(buf, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm,
                  topMargin=13*mm, bottomMargin=13*mm).build(story)
buf.seek(0)
pdf = pikepdf.open(buf)
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save(OUT, linearize=True)
import pikepdf as _; print("built", OUT, len(pikepdf.open(OUT).pages), "pages")
