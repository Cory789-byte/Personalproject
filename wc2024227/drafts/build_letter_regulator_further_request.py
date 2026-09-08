#!/usr/bin/env python3
"""WC/2024/227 - Further request to the Regulator on the documents not admitted: produce or confirm from
its own or Metro South Health's copy, or admit authenticity of the copy served, failing which non-party
disclosure. To be sent if the dispute is maintained after the request of 9 September 2026. Metadata stripped."""
import io, sys, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.platypus import Image as RLImage

DATE = sys.argv[1] if len(sys.argv)>1 else "21 September 2026"
REPLY_BY = sys.argv[2] if len(sys.argv)>2 else "Friday 25 September 2026"

B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.4, leading=12.2, spaceAfter=5)
HB  = ParagraphStyle('HB', parent=B, fontName='Helvetica-Bold', spaceAfter=2)
C   = ParagraphStyle('C', parent=B, fontSize=8.4, leading=10.4, spaceAfter=0)
CB  = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')
def P(t,s=B): return Paragraph(t,s)
def SIG():
    i=RLImage('assets/SIGNATURE_CoryShepherd.png', width=30*mm, height=15.5*mm); i.hAlign='LEFT'; return i

rows=[["Tab","Document","Contents admitted at","Copy known to be held"],
 ["31","Screen capture, \"2024 Emergency Code Register.xlsx\", March 2024 sheet, entries 16 to 20 March 2024","Facts 228 to 231 not admitted. Fact 268 admits Metro South Health's statement that \"a spreadsheet of recorded MET calls is available for the period 17-18 March 2024\"","Metro South Health (letter of 5 June 2026, K-LM26/729, Items 1 and 2)"],
 ["1","Role description, AO3 Switchboard Services, Logan Hospital","Facts 1 to 13","Metro South Health production of June 2026, Item 6"],
 ["5","Email, Ms Taylor to the Appellant, 27 September 2023, 1:52 pm, \"Approved - Permanent Full Time FTE\"","Fact 38","Metro South Health"],
 ["6","Email, Ms Taylor to Logan Switch, 15 April 2024, 12:39 pm, \"Afterhours Oncall Process - Switchboard\"","Facts 49, 68, 163","Respondent's amended List of Documents, attachment to item 25"],
 ["17 to 19","Movement forms, 27 February, 17 April and 9 June 2026, approved by Mr Hughes","Facts 14 to 16","Metro South Health"],
 ["20","Letter, Metro South Health to Commissioner Dwyer, 5 June 2026, K-LM26/729","Facts 263 to 268","The Commission's file"],
 ["21","Email, Ms Forrest to the Appellant, 7 July 2026","Fact 224","Metro South Health"],
 ["22","Consultation Paper - Proposed Rosters for Switchboard Services, November 2024","Facts 169 to 175","Metro South Health"],
 ["23","Consultation outcome - Proposed Rosters for Switchboard Services, December 2024","Facts 167, 176","Metro South Health"],
 ["30","Email, Ms Taylor to Logan Switch, 23 August 2023, 2:18 pm, \"What's Chloe's Hours?!\"","Facts 71, 72; quoted in Review Decision 69983 (fact 70)","Metro South Health; the Respondent's claim file"],
 ["30A","Email, Ms Taylor to Logan Switch, 18 June 2024, 8:58 am, \"Good morning Team.\"","Facts 85 to 87","Metro South Health"],
]
data=[[P(c,CB) for c in rows[0]]]+[[P(c,C) for c in r] for r in rows[1:]]
W=A4[0]-44*mm
t=Table(data,colWidths=[14*mm,W-14*mm-46*mm-42*mm,46*mm,42*mm],repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#888888')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),
                       ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))

s=[P("<b>CORY LEA SHEPHERD</b><br/>15 Edmond Street, Coomera QLD 4209 &nbsp;|&nbsp; coryshepherd1@hotmail.com",B),
   Spacer(1,2*mm),
   P("Ms Renee Matheson<br/>Senior Appeals Officer, Workers' Compensation Regulator<br/>150 Mary Street, Brisbane QLD 4000<br/>By email: Renee.Matheson@oir.qld.gov.au",B),
   Spacer(1,2*mm),
   P(f"Dated {DATE}",B),
   Spacer(1,2*mm),
   P("<b>WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator</b><br/>"
     "<b>Further request: the documents not admitted on 8 September 2026</b>",B),
   Spacer(1,1*mm),
   P("Dear Ms Matheson,",B),
   P("I refer to the Respondent's responses of 8 September 2026 to the Form 24 and Form 25 notices, to my request of "
     "9 September 2026 concerning the facts and documents not admitted, and to the position as it now stands. The "
     "documents concerned are set out in the schedule to this letter. The contents of each, other than Tab 31, were admitted in the "
     "Form 24 response at the facts noted; what is disputed is the authenticity of the copy served from my records.",B),
   P("At the mention on 7 August 2026 the Commissioner indicated that, for a document held by Metro South Health, the "
     "starting point is to ask the Regulator to make inquiries and produce it, and that non-party disclosure follows "
     "only if the Regulator does not. This letter is that step, put as a choice so that the matter can be closed "
     "without an application.",B),
   P("For each document in the schedule, could the Regulator please, by " + REPLY_BY + ", do one of the following:",B),
   P("(a) produce the Regulator's or Metro South Health's copy of the document, or confirm the authenticity of the copy "
     "served by reference to that copy; or",B),
   P("(b) admit, under rule 49, the authenticity of the copy served at that tab of Annexure A, so that it may be tendered "
     "without further proof of what it is.",B),
   P("If neither is done for any document by that date, I will seek that document by notice of non-party disclosure to "
     "Metro South Health limited to the documents named in the schedule, and I will refer to this correspondence if the "
     "question of the costs of that step arises.",B),
   P("The documents are listed in the schedule on the following page. No request is made in respect of fact 154 or "
     "Tab 24. For Tab 31, the request is for the spreadsheet of recorded MET calls for 17 to 18 March 2024 referred to "
     "in the letter of 5 June 2026 and for the March 2024 sheet of the workbook from which it is drawn, in native format "
     "and as printed.",B),
   P("Yours faithfully,",B), Spacer(1,1*mm), SIG(), Spacer(1,1*mm),
   P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented",B),
   PageBreak(),
   P("<b>WC/2024/227 &ndash; Schedule to the letter of " + DATE + ": the documents not admitted on 8 September 2026</b>",B),
   Spacer(1,2*mm), t]

buf=io.BytesIO()
d=BaseDocTemplate(buf,pagesize=A4,leftMargin=22*mm,rightMargin=22*mm,topMargin=11*mm,bottomMargin=11*mm)
d.addPageTemplates([PageTemplate(id='n',frames=[Frame(22*mm,11*mm,A4[0]-44*mm,A4[1]-22*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
d.build(s); buf.seek(0)
pdf=pikepdf.open(buf); n=len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="out/LETTER_TO_REGULATOR_further_request_documents_not_admitted.pdf"; pdf.save(out,linearize=True); print("built",out,n,"page(s)")
