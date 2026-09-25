#!/usr/bin/env python3
"""WC/2024/227 - Request to the Regulator for the documents referred to in its outlines of evidence of
24 September 2026, and the records of the email of 15 May 2024 at 1:15 pm (facts 74 to 79). Sent with the
direction 5 letter and paper. No reason given for any item; no claim about what the records will show.
Metadata stripped. Usage: build_letter_regulator_outline_documents.py ["1 October 2026"] ["Thursday 15 October 2026"]"""
import io, sys, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, KeepTogether
from reportlab.platypus import Image as RLImage

DATE = sys.argv[1] if len(sys.argv) > 1 else "25 September 2026"
REPLY_BY = sys.argv[2] if len(sys.argv) > 2 else "Thursday 15 October 2026"

B  = ParagraphStyle('B', fontName='Helvetica', fontSize=9.0, leading=11.5, spaceAfter=4)
H  = ParagraphStyle('H', parent=B, fontName='Helvetica-Bold', spaceBefore=3, spaceAfter=3, keepWithNext=1)
L  = ParagraphStyle('L', parent=B, leftIndent=8*mm, firstLineIndent=-6*mm, spaceAfter=2)
def P(t, s=B): return Paragraph(t, s)
def SIG():
    i = RLImage('assets/SIGNATURE_CoryShepherd.png', width=30*mm, height=15.5*mm); i.hAlign = 'LEFT'; return i

s = [P("<b>CORY LEA SHEPHERD</b><br/>15 Edmond Street, Coomera QLD 4209 &nbsp;|&nbsp; coryshepherd1@hotmail.com", B),
     Spacer(1, 2*mm),
     P("Ms Renee Matheson<br/>Senior Appeals Officer, Workers' Compensation Regulator<br/>By email: Renee.Matheson@oir.qld.gov.au", B),
     Spacer(1, 2*mm),
     P(f"Dated {DATE}", B),
     Spacer(1, 2*mm),
     P("<b>WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator</b><br/>"
       "<b>Request: documents referred to in the Respondent's outlines of evidence of 24 September 2026</b>", B),
     Spacer(1, 1*mm),
     P("Dear Ms Matheson,", B),
     P("I refer to the Respondent's outlines of evidence of 24 September 2026. The outlines refer to a number of "
       "documents and records that, as far as I am aware, have not been disclosed. At the mention on 7 August 2026 the "
       "Commissioner indicated that, for a document held by Metro South Health, the starting point is to ask the "
       "Regulator. I ask accordingly.", B),
     P(f"Could the Respondent please produce the following, to the extent not already disclosed, by {REPLY_BY}:", B),

     P("A. The email of 15 May 2024 at 1:15 pm (facts 74 to 79)", H),
     P("(a)&nbsp;&nbsp;the complete email chain with the subject \"Office Hours and Departmental Directives\", from 15 to "
       "31 May 2024, including every reply to it and every forward of it (including to Ms Taylor or to LBH_HR);", L),
     P("(b)&nbsp;&nbsp;the email of Ms Reese to the Appellant of 15 May 2024 at 4:12 pm referred to in her outline, or "
       "confirmation whether such an email exists;", L),
     P("(c)&nbsp;&nbsp;the Human Resources advice on which Ms Reese and Ms Taylor say, in their outlines, they acted in "
       "relation to that email, and any record (including any file note, email, Teams message or call record) of the "
       "contact on 15 May 2024 between Ms Taylor and Ms Pritchard, between Ms Taylor and Ms Reese, and between Ms Reese "
       "and Mr Punch, including the time of each;", L),
     P("(d)&nbsp;&nbsp;the call records for 15 May 2024 of the work mobile telephones, and the desk or DECT extensions, "
       "used by Ms Reese, Ms Taylor, Mr Punch and Ms Pritchard, for the calls referred to in the outlines of Ms Reese and "
       "Ms Taylor and in Ms Reese's response to the Respondent of July 2025 (Ms Taylor's call to Human Resources, her "
       "call to Ms Reese, and Ms Reese's call to Mr Punch), showing the time each call was made and its duration. The "
       "records are sought in the form issued by the carrier or the telephone system (the original PDF or export), "
       "without alteration other than the redaction of unrelated entries, with each redaction marked;", L),
     P("(e)&nbsp;&nbsp;the delivery and read records (message trace) of the email forwarded by LBH_HR on 15 May 2024 at "
       "3:41 pm to Mr Punch, Ms McGinley and Ms McNamee (the Respondent's disclosure of 11 June 2026, page 7), showing "
       "when it was received and opened by each;", L),
     P("(f)&nbsp;&nbsp;the notes of that time to which Ms Reese refers in her response to the Respondent of July 2025 "
       "(\"I have looked back at my notes regarding this time\"), so far as they concern 15 to 21 May 2024;", L),
     P("(g)&nbsp;&nbsp;any record of when, and by which account, that email was removed from the shared Switchboard inbox;", L),
     P("(h)&nbsp;&nbsp;any message-recall record for that email, including any recall result report;", L),

     P("B. Other documents referred to in the outlines", H),
     P("(i)&nbsp;&nbsp;the Human Resources advice that Ms Taylor says, in her outline, confirmed that the agreement of "
       "17 June 2020 continued to apply;", L),
     P("(j)&nbsp;&nbsp;the attachment \"Rostered shifts Cory S. past 8 months.xlsx\" to Ms Reese's email to Ms Taylor of "
       "7 August 2023 at 5:11 pm (fact 159);", L),
     P("(k)&nbsp;&nbsp;the records of Ms Taylor's appointments, acting and permanent, as Switchboard Manager, Logan "
       "Hospital, with their dates;", L),
     P("(l)&nbsp;&nbsp;the Technical Support advice on the break of 17 to 18 March 2024 referred to in Ms Wright's outline, "
       "with the query escalated to Technical Support;", L),
     P("(m)&nbsp;&nbsp;the review of the Appellant's pay for the fortnight including 30 March 2024 referred to in Ms Earl's "
       "outline, and the record of its correction; and", L),
     P("(n)&nbsp;&nbsp;the review of the attachment history of leave request 15480560 referred to in Ms Earl's outline.", L),

     Spacer(1, 1*mm),
     P("If any of these documents is not held, or has already been disclosed, I would be grateful to be told so, "
       "identifying the disclosure.", B),
     KeepTogether([P("Yours faithfully,", B), Spacer(1, 1*mm), SIG(), Spacer(1, 1*mm),
                   P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented", B)]),
     ]

buf = io.BytesIO()
d = BaseDocTemplate(buf, pagesize=A4, leftMargin=22*mm, rightMargin=22*mm, topMargin=12*mm, bottomMargin=12*mm)
d.addPageTemplates([PageTemplate(id='n', frames=[Frame(22*mm, 12*mm, A4[0]-44*mm, A4[1]-24*mm,
                                                       leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
d.build(s); buf.seek(0)
pdf = pikepdf.open(buf); n = len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out = "out/LETTER_TO_REGULATOR_documents_in_outlines.pdf"; pdf.save(out, linearize=True); print("built", out, n, "page(s)")
