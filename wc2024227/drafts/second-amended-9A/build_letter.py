from letter_content import *
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
body=ParagraphStyle('b',fontName='Helvetica',fontSize=8.7,leading=10.8,spaceAfter=3)
small=ParagraphStyle('s',parent=body,fontSize=8.6,leading=10.6,spaceAfter=1,leftIndent=8)
h=ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=10.5,leading=13,spaceBefore=6,spaceAfter=3)
t=ParagraphStyle('t',fontName='Helvetica-Bold',fontSize=11,leading=13,spaceAfter=3)
esc=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
S=[]
S.append(Paragraph(esc(DATE),body))
for l in TO: S.append(Paragraph(esc(l),ParagraphStyle('to',parent=body,spaceAfter=0)))
S.append(Spacer(1,3)); S.append(Paragraph(esc(CC),body)); S.append(Spacer(1,2))
S.append(Paragraph(esc(TITLE),t)); S.append(Paragraph('<b>'+esc(SUBJECT)+'</b>',body)); S.append(Spacer(1,4))
for b,txt in BODY: S.append(Paragraph('<b>'+esc(b)+'</b> '+esc(txt),body))
for l in CLOSE: S.append(Paragraph(esc(l),body))
S.append(PageBreak()); S.append(Paragraph(esc(SCHEDULE_TITLE),t))
from reportlab.platypus import Table,TableStyle
cell=ParagraphStyle('c',fontName='Helvetica',fontSize=7.6,leading=9.2)
cellb=ParagraphStyle('cb',parent=cell,fontName='Helvetica-Bold')
data=[[Paragraph(esc(h),cellb) for h in SCHEDULE_COLS]]
for r in SCHEDULE_ROWS: data.append([Paragraph(esc(str(v)),cell) for v in r])
W=A4[0]-36*mm
tbl=Table(data,colWidths=[W*0.05,W*0.36,W*0.11,W*0.10,W*0.18,W*0.20],repeatRows=1)
ts=[('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E9E9E9')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]
for i,r in enumerate(SCHEDULE_ROWS,start=1):
    if r[4]==C: ts.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#F3F7F3')))
    elif r[3]==D: ts.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#FBF5EE')))
tbl.setStyle(TableStyle(ts)); S.append(tbl)
S.append(Spacer(1,6)); S.append(Paragraph(esc(SCHEDULE_NOTE),body))
def deco(c,d):
    c.saveState(); c.setFont('Helvetica',7.5); c.setFillColor(colors.HexColor('#555555'))
    c.drawString(18*mm,A4[1]-12*mm,"WC/2024/227  |  Shepherd v Workers' Compensation Regulator  |  Letter to the Industrial Registry")
    c.drawRightString(A4[0]-18*mm,10*mm,f"Page {d.page}"); c.restoreState()
doc=SimpleDocTemplate('2026-10_LETTER_to_Registry_leave_to_amend_and_documents.pdf',pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=16*mm,bottomMargin=14*mm,title='Letter to the Industrial Registry WC/2024/227')
doc.build(S,onFirstPage=deco,onLaterPages=deco); print('pdf built')
