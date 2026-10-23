"""Render the Second Amended 9A DOCX to PDF with reportlab (soffice unavailable in this container)."""
import zipfile,re,html,sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
src,out=sys.argv[1],sys.argv[2]
x=zipfile.ZipFile(src).read('word/document.xml').decode()
paras=re.findall(r'<w:p[ >].*?</w:p>',x,flags=re.S)
body=ParagraphStyle('b',fontName='Helvetica',fontSize=9.2,leading=12,spaceAfter=4)
head=ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=10.5,leading=13,spaceBefore=7,spaceAfter=3)
title=ParagraphStyle('t',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=6)
call=ParagraphStyle('c',fontName='Helvetica',fontSize=9.2,leading=12,backColor=colors.HexColor('#F2F2F2'),borderPadding=4,spaceBefore=4,spaceAfter=8,leftIndent=2,rightIndent=2)
story=[]
for i,p in enumerate(paras):
    runs=re.findall(r'<w:r>(.*?)</w:r>',p,flags=re.S)
    s=''
    for r in runs:
        t=''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',r))
        t=html.unescape(t).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
        if '<w:b/>' in r: t=f'<b>{t}</b>'
        s+=t
    if not s.strip():
        continue
    if i==0: st=title
    elif 'w:sz w:val="21"' in p or re.match(r'<b>(PART [A-E]|STRESSOR [123])',s): st=head
    elif 'Callout' in p: st=call
    else: st=body
    if 'w:shd w:fill="E9E9E9"' in p: st=ParagraphStyle('hs',parent=head,backColor=colors.HexColor('#E9E9E9'))
    story.append(Paragraph(s,st))
def deco(c,d):
    c.saveState(); c.setFont('Helvetica',7.5); c.setFillColor(colors.HexColor('#555555'))
    c.drawString(18*mm,A4[1]-12*mm,"Queensland Industrial Relations Commission  |  WC/2024/227  |  Shepherd v Workers' Compensation Regulator")
    c.drawRightString(A4[0]-18*mm,10*mm,f"Page {d.page}"); c.restoreState()
doc=SimpleDocTemplate(out,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=18*mm,bottomMargin=16*mm,title='Second Amended Form 9A WC/2024/227')
doc.build(story,onFirstPage=deco,onLaterPages=deco)
print('built',out)
