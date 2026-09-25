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
REPLY_BY = sys.argv[2] if len(sys.argv) > 2 else "Thursday 1 October 2026"

B  = ParagraphStyle('B', fontName='Helvetica', fontSize=9.2, leading=11.8, spaceAfter=4)
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
     P(f"Could the Respondent please produce the following, to the extent not already disclosed, by {REPLY_BY}. "
       "Emails are sought in their native form (for example .msg), showing the full header, sender, every recipient "
       "and the time sent:", B),

     P("A. The email of 15 May 2024 at 1:15 pm (facts 74 to 79)", H),
     P("(a)&nbsp;&nbsp;the complete email chain with the subject \"Office Hours and Departmental Directives\", from 15 to "
       "31 May 2024, including every reply to it and every forward of it (including to Ms Taylor or to LBH_HR);", L),
     P("(b)&nbsp;&nbsp;the email of Ms Reese to the Appellant of 15 May 2024 at 4:12 pm referred to in her outline, or "
       "confirmation whether such an email exists;", L),
     P("(c)&nbsp;&nbsp;the Human Resources advice on which Ms Reese and Ms Taylor say, in their outlines, they acted in "
       "relation to that email, and any record (including any file note, email, Teams message or call record) of the "
       "contact on 15 May 2024 between Ms Taylor and Ms Pritchard, between Ms Taylor and Ms Reese, and between Ms Reese "
       "and Mr Punch, including who made each contact and its time;", L),
     P("(d)&nbsp;&nbsp;the call records for 15 May 2024 of the work mobile telephones, and the desk or DECT extensions, "
       "used by Ms Reese, Ms Taylor, Mr Punch and Ms Pritchard, for the calls referred to in the outlines of Ms Reese and "
       "Ms Taylor and in Ms Reese's response to the Respondent of July 2025 (Ms Taylor's call to Human Resources, her "
       "call to Ms Reese, and Ms Reese's call to Mr Punch), showing for each call which telephone placed it and which received it, the time it was placed and its duration. This "
       "includes the outgoing records of the telephone that placed each call and, where the system records them, the "
       "incoming records of the telephone that received it, as held by Metro South Health (including its carrier's "
       "itemised billing). The records are sought in the form issued by the carrier or the telephone system (the original "
       "PDF or export), without alteration other than the redaction of unrelated entries, with each redaction marked;", L),
     P("(e)&nbsp;&nbsp;the delivery and read records (message trace) of the email forwarded by LBH_HR on 15 May 2024 at "
       "3:41 pm to Mr Punch, Ms McGinley and Ms McNamee (the Respondent's disclosure of 11 June 2026, page 7), showing "
       "when it was received and opened by each;", L),
     P("(f)&nbsp;&nbsp;the notes of that time to which Ms Reese refers in her response to the Respondent of July 2025 "
       "(\"I have looked back at my notes regarding this time\"), so far as they concern 15 to 21 May 2024;", L),
     P("(g)&nbsp;&nbsp;any record of when, and by which account, that email was removed from the shared Switchboard inbox "
       "or from the server (paragraph 16(b)(vii) of the amended statement of facts and contentions);", L),
     P("(h)&nbsp;&nbsp;the email or other document relied on for the statements that the Appellant \"declined\" (Ms Reese's "
       "outline) or \"refused\" (Ms Taylor's outline) to retract that email, including the communication by which Ms Taylor "
       "was told so, with its time;", L),
     P("(i)&nbsp;&nbsp;any message-recall record for that email, including any recall result report;", L),

     P("B. Other documents referred to in the outlines", H),
     P("(j)&nbsp;&nbsp;the Human Resources advice that Ms Taylor says, in her outline, confirmed that the agreement of "
       "17 June 2020 continued to apply;", L),
     P("(k)&nbsp;&nbsp;the records of Ms Taylor's appointments, acting and permanent, as Switchboard Manager, Logan "
       "Hospital, with their dates;", L),
     P("(l)&nbsp;&nbsp;the Technical Support advice on the break of 17 to 18 March 2024 referred to in Ms Wright's outline, "
       "with the query escalated to Technical Support;", L),
     P("(m)&nbsp;&nbsp;the review of the Appellant's pay for the fortnight including 30 March 2024 referred to in Ms Earl's "
       "outline, and the record of its correction; and", L),
     P("(n)&nbsp;&nbsp;the review of the attachment history of leave request 15480560 referred to in Ms Earl's outline.", L),

     P("C. The documents still to be confirmed (your email of 24 September 2026)", H),
     P("Your email of 24 September 2026 confirmed Tabs 6, 20, 30 and 30A and said that the Regulator has asked Metro "
       "South Health for copies of the documents at (o) to (u) below. Tab numbers are those of Annexure A to my notices "
       "of 28 August 2026. Could the Respondent please provide Metro South Health's copy of each, or confirm the "
       "authenticity of the copy served, by the same date:", B),
     P("(o)&nbsp;&nbsp;Tab 1: Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital;", L),
     P("(p)&nbsp;&nbsp;Tab 5: email, Ms Taylor to the Appellant, \"Approved - Permanent Full Time FTE\", 27 September 2023, 1:52 pm;", L),
     P("(q)&nbsp;&nbsp;Tabs 17 to 19: movement forms of 27 February, 17 April and 9 June 2026, each approved by Mr Hughes;", L),
     P("(r)&nbsp;&nbsp;Tab 21: the email of Ms L Forrest, Senior Consultant, Human Resources, Logan and Beaudesert Health "
       "Service, to the Appellant, 7 July 2026, \"Cory Shepherd ECC further information\". Your email describes this "
       "document as an email from me. The document sought is Ms Forrest's email as she sent it, showing its sender, "
       "every recipient and its time, and not any copy forwarded by me;", L),
     P("(s)&nbsp;&nbsp;Tab 22: Consultation Paper, Proposed Rosters for Switchboard Services, Logan Hospital, signed by "
       "Mr Hughes on 12 November 2024;", L),
     P("(t)&nbsp;&nbsp;Tab 23: Consultation outcome, Proposed Rosters for Switchboard Services, Logan Hospital, signed by "
       "Mr Hughes on 12 December 2024;", L),
     P("(u)&nbsp;&nbsp;Tab 31: \"2024 Emergency Code Register.xlsx\", March 2024 sheet, entries for 16 to 20 March 2024 (see "
       "Metro South Health's letter of 5 June 2026 stating that \"a spreadsheet of recorded MET calls is available for "
       "the period 17-18 March 2024\"); and", L),
     P("(v)&nbsp;&nbsp;Tab 24: email, Mr H Moran, Together Queensland, to Ms C Jeffrey, Ms P Conaghan and the Appellant, "
       "3 November 2025. Could the Respondent please say whether it maintains its dispute of the authenticity of this "
       "document.", L),

     Spacer(1, 1*mm),
     P("The documents are sought so that matters capable of being settled from the records are settled before the "
       "hearing, without the Commission's time being taken up with them, and in the interests of the efficient conduct "
       "of the appeal. The records will establish these matters directly, rather than through recollection or "
       "second-hand accounts given more than two years after the events. Where a record settles a matter, it need not "
       "be contested at the hearing, which will confine the issues and shorten the hearing. A statement that a record "
       "is not held serves the same purpose.", B),
     P("I ask for a response by " + REPLY_BY + " because these documents may bear on the course I propose to the "
       "Commission under direction 5 of the Further Directions Order (3). The documents at (o) to (u) have been "
       "outstanding since my letter of 9 September 2026.", B),
     P("So that each item can be closed, could the Respondent please answer item by item, stating for each whether "
       "the document is produced, has already been disclosed (identifying where), or is not held. Where a document is not "
       "held, could the Respondent please say whether it existed and, if so, when it ceased to be held.", B),
     P("If it is quicker, the Respondent may instead confirm by email the facts those records would show: for (c) and "
       "(d), the time of each call or contact and who made it; for (e), when the email was received and opened by each "
       "recipient; for (g), the date, time and account by which the email was removed; and for (i), the date and time "
       "of any recall. A confirmation of that kind, identifying its source, would be of equal assistance.", B),
     P("Some of the records at (d), (e), (g) and (i) may be subject to routine deletion. Pending the Respondent's response, I ask "
       "that the Respondent request Metro South Health to preserve them.", B),
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
