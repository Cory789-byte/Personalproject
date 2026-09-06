#!/usr/bin/env python3
"""WC/2024/227 - Directions 1 and 2 of the Further Directions Order (3): witness list (file+serve)
and the covering letter to the Industrial Registry. Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Table, TableStyle, Spacer

HD  = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.6, leading=11, textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2 = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=10)
CT  = ParagraphStyle('CT', fontName='Helvetica-Bold', fontSize=12.5, leading=15.5, alignment=1, spaceAfter=3)
CS  = ParagraphStyle('CS', fontName='Helvetica', fontSize=9.2, leading=12, alignment=1, spaceAfter=10)
PARTY=ParagraphStyle('PARTY', fontName='Helvetica-Bold', fontSize=10.5, leading=13, alignment=1, spaceAfter=1)
ROLE =ParagraphStyle('ROLE', fontName='Helvetica', fontSize=9, leading=11.5, alignment=1, spaceAfter=6)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.6, leading=12.6, spaceAfter=6)
SUB = ParagraphStyle('S', fontName='Helvetica-Oblique', fontSize=8.2, leading=10.6, textColor=colors.HexColor('#555555'), spaceAfter=6)
C   = ParagraphStyle('C', parent=B, fontSize=9.2, leading=11.8, spaceAfter=0)
CB  = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')
def P(t,s=B): return Paragraph(t,s)

def doc(story, out, land=False):
    buf=io.BytesIO()
    d=BaseDocTemplate(buf,pagesize=A4,leftMargin=22*mm,rightMargin=22*mm,topMargin=16*mm,bottomMargin=16*mm)
    d.addPageTemplates([PageTemplate(id='n',frames=[Frame(22*mm,16*mm,A4[0]-44*mm,A4[1]-32*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
    d.build(story); buf.seek(0)
    pdf=pikepdf.open(buf); n=len(pdf.pages)
    try: del pdf.Root.Metadata
    except (AttributeError,KeyError): pass
    with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
    try: del pdf.Root.Metadata
    except (AttributeError,KeyError): pass
    for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
    pdf.save(out,linearize=True); print("built",out,n,"page(s)")
    return n

def heading():
    return [P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",CT),
            P("Workers' Compensation and Rehabilitation Act 2003 &nbsp;|&nbsp; Matter No. WC/2024/227",CS),
            P("CORY LEA SHEPHERD",PARTY), P("Appellant",ROLE),
            P("v",ROLE),
            P("WORKERS' COMPENSATION REGULATOR",PARTY), P("Respondent",ROLE)]

# ---------------- 1. WITNESS LIST ----------------
W=[("1","Cory Lea Shepherd","Appellant"),
   ("2","Dr Ravikumar Bangalore Krishnaiah","Consultant Psychiatrist, Mind and Memory Service &ndash; the Appellant's treating psychiatrist"),
   ("3","Dr Peter Hawes","General Practitioner, Our Medical Ashmore &ndash; the Appellant's treating general practitioner at the date of injury"),
   ("4","Ms Carolyn Jeffrey","Administration Officer, Switchboard Services, Logan Hospital"),
   ("5","Mr Cory Harrison-Jones","Formerly an Administration Officer, Switchboard Services, Logan Hospital"),
   ("6","Ms Patricia Conaghan","Administration Officer, Switchboard Services, Logan Hospital")]
s=heading()
s+=[Spacer(1,4*mm),
    P("APPELLANT'S LIST OF NAMES OF ALL WITNESSES",CT),
    P("Filed in the Industrial Registry and served on the Respondent pursuant to direction 1 of the "
      "Further Directions Order (3) dated 19 August 2026",CS),
    Spacer(1,2*mm),
    P("The Appellant will call the following witnesses at the hearing.",B)]
rows=[[Paragraph("No.",CB),Paragraph("Name",CB),Paragraph("Capacity",CB)]]
for n,nm,cap in W: rows.append([Paragraph(n,C),Paragraph("<b>"+nm+"</b>",C),Paragraph(cap,C)])
t=Table(rows,colWidths=[12*mm,58*mm,A4[0]-44*mm-70*mm],repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),
 ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
s.append(t)
s+=[Spacer(1,4*mm),
    P("Witnesses 2 and 3 are expert witnesses within the meaning of Part 4.11 of the Workers' "
      "Compensation Appeal Guide. The Appellant may apply under Part 6 of that Guide for attendance "
      "notices requiring the attendance of any of the witnesses listed above.",B),
    Spacer(1,10*mm),
    P("Dated &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; September 2026",B),
    Spacer(1,10*mm),
    P("__________________________________",B),
    P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented",B)]
doc(s,"out/WITNESS_LIST_SERVE_9SEP2026.pdf")

# ---------------- 2. COVERING LETTER TO THE REGISTRY ----------------
s=[P("CORY LEA SHEPHERD",HD), P("15 Edmond Street, Coomera QLD 4209 &nbsp;|&nbsp; coryshepherd1@hotmail.com",HD2),
   P("The Industrial Registrar<br/>Queensland Industrial Relations Commission<br/>qirc.registry@qirc.qld.gov.au",B),
   Spacer(1,3*mm),
   P("Dated &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; September 2026",B),
   Spacer(1,3*mm),
   P("<b>WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator</b><br/>"
     "<b>Direction 1 of the Further Directions Order (3) dated 19 August 2026</b>",B),
   Spacer(1,2*mm),
   P("Dear Registrar,",B),
   P("In accordance with direction 1 of the Further Directions Order (3) dated 19 August 2026, I file "
     "and serve the Appellant's list of names of all witnesses.",B),
   P("In accordance with direction 2, I have today served on the Respondent, and have not filed, an "
     "outline of the evidence to be given by each lay witness (one A4 page per witness), together with "
     "a schedule of the medical documents relied upon and the pages of those documents. No report has "
     "been prepared for the purposes of this proceeding. The reports and records of the treating "
     "practitioners named at items 2 and 3 of the witness list are identified in that schedule and "
     "served with it.",B),
   P("For completeness, and so that the position is clear on the record: the Appellant does not "
     "presently propose to call Ms Chloe Taylor or Ms Tammy Reese. Their evidence is material to the "
     "matters pleaded, and the Appellant proceeds on the basis that the Respondent will call them. If "
     "the Respondent's list filed by 30 September 2026 does not name them, the Appellant will seek "
     "attendance notices and will write to the Commission at that time.",B),
   P("The Appellant may also apply for attendance notices in respect of the witnesses named at items "
     "2 to 6, and will do so sufficiently in advance of the hearing.",B),
   P("Yours faithfully,",B), Spacer(1,8*mm),
   P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented",B)]
doc(s,"out/COVERING_LETTER_REGISTRY_9SEP2026.pdf")
