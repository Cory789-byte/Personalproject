#!/usr/bin/env python3
"""WC/2024/227 - Letters to Dr Krishnaiah and Dr Hawes asking whether they will give evidence.
Metadata stripped."""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
HD=ParagraphStyle('HD',fontName='Helvetica-Bold',fontSize=9,leading=11.5,textColor=colors.HexColor('#333333'),spaceAfter=1)
HD2=ParagraphStyle('HD2',parent=HD,fontName='Helvetica',spaceAfter=12)
B=ParagraphStyle('B',fontName='Helvetica',fontSize=10,leading=13.4,spaceAfter=7)
BB=ParagraphStyle('BB',parent=B,fontName='Helvetica-Bold')
def P(t,s=B): return Paragraph(t,s)
def build(story,out):
    buf=io.BytesIO()
    d=BaseDocTemplate(buf,pagesize=A4,leftMargin=24*mm,rightMargin=24*mm,topMargin=18*mm,bottomMargin=18*mm)
    d.addPageTemplates([PageTemplate(id='n',frames=[Frame(24*mm,18*mm,A4[0]-48*mm,A4[1]-36*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
    d.build(story); buf.seek(0)
    pdf=pikepdf.open(buf); n=len(pdf.pages)
    try: del pdf.Root.Metadata
    except (AttributeError,KeyError): pass
    with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
    try: del pdf.Root.Metadata
    except (AttributeError,KeyError): pass
    for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
    pdf.save(out,linearize=True); print("built",out,n,"page(s)")
def head(to):
    return [P("CORY LEA SHEPHERD",HD),
            P("15 Edmond Street, Coomera QLD 4209 &nbsp;|&nbsp; coryshepherd1@hotmail.com &nbsp;|&nbsp; 0422 438 627",HD2),
            P(to,B), Spacer(1,3*mm), P("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; September 2026",B), Spacer(1,3*mm)]
COMMON=[
 P("The appeal is a hearing before the Queensland Industrial Relations Commission. Under the Commission's "
   "Workers' Compensation Appeal Guide, all evidence is given orally and there are no witness statements or "
   "affidavits. The Guide also states that \"presenting a medical report on its own cannot be considered without "
   "having the expert witness give evidence orally to support that document and being available for "
   "cross-examination by the other party\".",B),
 P("I am not asking you to prepare a report, to review any material, or to express any opinion in advance. I am "
   "asking only whether you are able to attend to give evidence about your own treatment of me and your own "
   "records.",B),
 P("Two practical matters. The Commission allows expert witnesses to give evidence by telephone or video rather "
   "than in person. And the Commission can issue an attendance notice requiring attendance on a fixed date and "
   "time, which some practitioners prefer because it fixes the commitment and formalises the request; conduct "
   "money is payable to expert witnesses at the applicable rate, and I will pay it.",B),
]
TAIL=[P("Could you please let me know by <b>Friday 2 October 2026</b> whether you are willing to attend, and if so "
        "whether you would prefer to be given an attendance notice. If it is easier, your practice manager can "
        "reply on your behalf.",B),
      P("I am grateful for your time.",B), Spacer(1,10*mm),
      P("Yours sincerely,",B), Spacer(1,12*mm),
      P("<b>Cory Lea Shepherd</b>",B)]
# ---- Krishnaiah ----
s=head("Dr Ravikumar Bangalore Krishnaiah<br/>Mind and Memory Service<br/>Shop 6, Upper floor, 21 Coomera Grand Drive, Upper Coomera QLD 4209<br/>ravikumar@mindandmemoryservice.com.au")
s+=[P("Dear Dr Krishnaiah,",B),
    P("<b>Queensland Industrial Relations Commission &ndash; WC/2024/227 &ndash; my workers' compensation appeal</b>",BB),
    P("Thank you for your email of 5 September 2026, and for offering to provide me with my records. I have "
      "requested them separately and I understand your position about medico-legal work. I am writing about a "
      "different and much smaller question.",B),
    P("On 9 September 2026 I filed with the Commission a list of the witnesses I may call at the hearing of my "
      "appeal. You are named on that list as my treating psychiatrist, together with my general practitioner "
      "Dr Peter Hawes.",B)]
s+=COMMON
s+=[P("What that would involve is your evidence of your own treatment: when I first attended, on 24 October 2024; "
      "what you recorded at that time; the diagnosis you made and have maintained; the treatment you have "
      "provided; and the contents of your report of 13 February 2025, which was prepared for QSuper and which I "
      "have identified to the other party as a treating record. You would then be asked questions by the "
      "Respondent's representative.",B)]
s+=TAIL
build(s,"out/LETTER_Dr_Krishnaiah_attendance_SEP2026.pdf")
# ---- Hawes ----
s=head("Dr Peter Hawes<br/>Our Medical Ashmore<br/>566 Olsen Avenue, Ashmore QLD 4214<br/>admin@ourmedicalashmore.com.au")
s+=[P("Dear Dr Hawes,",B),
    P("<b>Queensland Industrial Relations Commission &ndash; WC/2024/227 &ndash; my workers' compensation appeal</b>",BB),
    P("You may recall that you saw me on 1 July 2024 and issued the work capacity certificate for my workers' "
      "compensation claim, and that you issued further certificates on 11 August and 8 September 2024. WorkCover "
      "rejected the claim and I have appealed to the Queensland Industrial Relations Commission. The appeal is a "
      "fresh hearing.",B),
    P("On 9 September 2026 I filed with the Commission a list of the witnesses I may call at the hearing. You are "
      "named on that list as my treating general practitioner at the date of injury, together with my treating "
      "psychiatrist Dr Ravikumar Bangalore Krishnaiah.",B)]
s+=COMMON
s+=[P("What that would involve is your evidence of your own treatment: the consultation of 1 July 2024 and what "
      "you recorded; the work capacity certificates you issued and their contents; the referral to a psychiatrist "
      "recorded on the certificate of 8 September 2024; and the conversation with WorkCover recorded as having "
      "taken place on 2 September 2024. You would then be asked questions by the Respondent's representative.",B)]
s+=TAIL
build(s,"out/LETTER_Dr_Hawes_attendance_SEP2026.pdf")
