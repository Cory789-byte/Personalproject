#!/usr/bin/env python3
"""WC/2024/227 - PDF of the diarised mention transcript with the speaker corrections. INTERNAL.
Renders ../documents/transcripts/TRANSCRIPT_diarised_prosody.md. Metadata stripped."""
import io, re, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle

H1=ParagraphStyle('H1',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceBefore=8,spaceAfter=4)
H2=ParagraphStyle('H2',fontName='Helvetica-Bold',fontSize=10.5,leading=13,spaceBefore=8,spaceAfter=3,textColor=colors.HexColor('#222222'))
B =ParagraphStyle('B',fontName='Helvetica',fontSize=8.6,leading=10.9,spaceAfter=3)
SPK=ParagraphStyle('SPK',fontName='Helvetica-Bold',fontSize=8.6,leading=10.9,spaceBefore=4,spaceAfter=1)
C =ParagraphStyle('C',fontName='Helvetica',fontSize=7.4,leading=9.2,spaceAfter=0)
CB=ParagraphStyle('CB',parent=C,fontName='Helvetica-Bold')
W=A4[0]-32*mm

def esc(t):
    t=t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
    t=re.sub(r'`(.+?)`',r'<i><font color="#777777">\1</font></i>',t)
    t=re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)',r'<i>\1</i>',t)
    t=t.replace('⛔','[!]').replace('⚠','[!]').replace('⭐','*').replace('⇒','=>').replace('—','&#8212;').replace('–','&#8211;')
    return t

src=open('../documents/transcripts/TRANSCRIPT_diarised_prosody.md').read().splitlines()
story=[]; tbl=[]
def flush():
    global tbl
    if not tbl: return
    rows=[[c.strip() for c in r.strip().strip('|').split('|')] for r in tbl if not re.match(r'^\s*\|[\s:|-]+\|\s*$',r)]
    if rows:
        n=max(len(r) for r in rows)
        rows=[r+['']*(n-len(r)) for r in rows]
        data=[[Paragraph(esc(c),CB if i==0 else C) for c in r] for i,r in enumerate(rows)]
        t=Table(data,colWidths=[W/n]*n,repeatRows=1)
        t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#999999')),
            ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),2.5),('RIGHTPADDING',(0,0),(-1,-1),2.5),
            ('TOPPADDING',(0,0),(-1,-1),1.5),('BOTTOMPADDING',(0,0),(-1,-1),1.5)]))
        story.append(t); story.append(Spacer(1,3*mm))
    tbl=[]

for ln in src:
    s=ln.rstrip()
    if s.startswith('|'): tbl.append(s); continue
    flush()
    if not s.strip(): continue
    if s.startswith('## '): story.append(Paragraph(esc(s[3:]),H2))
    elif s.startswith('# '): story.append(Paragraph(esc(s[2:]),H1))
    elif s.startswith('---'): story.append(Spacer(1,2*mm))
    elif re.match(r'^\*\*\d+:\d+\.\d+\s+[A-Z]',s): story.append(Paragraph(esc(s),SPK))
    elif s.startswith('> '): story.append(Paragraph(esc(s[2:]),B))
    else: story.append(Paragraph(esc(s),B))
flush()

def footer(cv,doc):
    cv.saveState(); cv.setFont('Helvetica',7); cv.setFillColor(colors.HexColor('#666666'))
    cv.drawString(16*mm,9*mm,"WC/2024/227 · Mention of 7 August 2026 · diarised transcript with corrections · INTERNAL")
    cv.drawRightString(A4[0]-16*mm,9*mm,"Page %d"%doc.page); cv.restoreState()
buf=io.BytesIO()
d=BaseDocTemplate(buf,pagesize=A4,leftMargin=16*mm,rightMargin=16*mm,topMargin=13*mm,bottomMargin=13*mm)
d.addPageTemplates([PageTemplate(id='n',frames=[Frame(16*mm,13*mm,W,A4[1]-26*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer)])
d.build(story); buf.seek(0)
pdf=pikepdf.open(buf); n=len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="../documents/transcripts/MENTION_7AUG2026_TRANSCRIPT_diarised_CORRECTED.pdf"
pdf.save(out,linearize=True); print("built",out,n,"page(s)")
