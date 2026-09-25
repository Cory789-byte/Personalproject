#!/usr/bin/env python3
"""WC/2024/227 - Letter to the Registry under direction 5 of FDO(3): directions complete, state of the
facts and documents, request for a second s 552A conference, and a schedule of the ten documents still
to be confirmed. Metadata stripped."""
import io, sys, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.platypus import Image as RLImage

DATE = sys.argv[1] if len(sys.argv) > 1 else "1 October 2026"   # HELD for 1 Oct: update with the Regulator's response first
RESPOND_BY = sys.argv[2] if len(sys.argv) > 2 else "15 October 2026"
from datetime import datetime as _dt
EXPIRED = _dt.strptime(DATE, "%d %B %Y") >= _dt(2026, 9, 30)  # send only after 4.00 pm if dated 30 September

B  = ParagraphStyle('B', fontName='Helvetica', fontSize=9.2, leading=11.4, spaceAfter=3.5)
H  = ParagraphStyle('H', parent=B, fontName='Helvetica-Bold', spaceBefore=3, spaceAfter=2, keepWithNext=1)
L  = ParagraphStyle('L', parent=B, leftIndent=8*mm, firstLineIndent=-6*mm, spaceAfter=1.2)
C  = ParagraphStyle('C', parent=B, fontSize=7.9, leading=9.4, spaceAfter=0)
CB = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')
N  = ParagraphStyle('N', parent=B, fontSize=8.2, leading=10.2)
def P(t, s=B): return Paragraph(t, s)
def SIG():
    i = RLImage('assets/SIGNATURE_CoryShepherd.png', width=30*mm, height=15.5*mm); i.hAlign = 'LEFT'; return i

W = A4[0] - 44*mm
def table(rows, widths):
    data = [[P(c, CB) for c in rows[0]]] + [[P(c, C) for c in r] for r in rows[1:]]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#888888')),
                           ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EEEEEE')),
                           ('VALIGN', (0,0), (-1,-1), 'TOP'),
                           ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
                           ('TOPPADDING', (0,0), (-1,-1), 2), ('BOTTOMPADDING', (0,0), (-1,-1), 2)]))
    return t

HDR = ["Tab", "Document", "Held by", "Admitted facts referring to it", "Issue in the Respondent's pleading"]
A = [HDR,
 ["1", "Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital",
  "Metro South Health. Supplied by it to the Appellant as Attachment 2 to its request for medical information of 31 July 2026 (Mr Hughes)",
  "Facts 1 to 13",
  "The duties of the position, including the database (fact 6), the emergency response process (fact 8) and continuous 24-hour, 7-day shift work (facts 2, 13). SOFC [11], [22]"],
 ["5", "Email, Ms Taylor to the Appellant, \"Approved - Permanent Full Time FTE\", 27 September 2023, 1:52 pm",
  "Metro South Health", "Fact 38",
  "The change to full-time hours from 16 October 2023, and whether the 2020 agreement continued to apply after it. SOFC [22(e)]; facts 252, 254"],
 ["17 to 19", "Movement forms, 27 February, 17 April and 9 June 2026, each approved by Mr Hughes as delegate",
  "Metro South Health", "Facts 14, 15",
  "Each records the Appellant as a \"Continuous Shift Worker\". SOFC [22(d)]"],
 ["21", "Email, Ms L Forrest, Senior Consultant, Human Resources, Logan and Beaudesert Health Service, to the Appellant, 7 July 2026",
  "Metro South Health", "Facts 224, 225",
  "The scope of the 2020 eight-hour agreement: \"only applied where staff initiated shift swaps have occurred\". SOFC [22(e)]"],
 ["22", "Consultation Paper - Proposed Rosters for Switchboard Services, Logan Hospital, November 2024",
  "Metro South Health", "Facts 169 to 175",
  "Roster negotiations from 22 July 2021, and the August 2024 realignment of the reporting line (fact 170). SOFC [19], [22]"],
 ["23", "Consultation outcome - Proposed Rosters for Switchboard Services, Logan Hospital, December 2024",
  "Metro South Health", "Facts 167, 168, 176, 177",
  "The outcome of that consultation. SOFC [19], [22]"],
 ["31", "\"2024 Emergency Code Register.xlsx\", March 2024 sheet, entries for 16 to 20 March 2024",
  "Metro South Health. Its letter of 5 June 2026 (K-LM26/729, Items 1 and 2) states that \"a spreadsheet of recorded MET calls is available for the period 17-18 March 2024\" (fact 268)",
  "Facts 228 to 231 not admitted. Fact 268 admitted",
  "The emergency calls recorded on the shifts either side of the break of 17 to 18 March 2024. SOFC [22(a)], [22(f)]"],
]
Bp = [HDR,
 ["24", "Email, Mr H Moran, Organiser, Together Queensland, to Ms C Jeffrey, Ms P Conaghan and the Appellant, 3 November 2025",
  "Together Queensland; each recipient. Ms Conaghan is on the Appellant's list of witnesses",
  "Facts 178, 179", "The Appellant's endorsement as a workplace delegate. SOFC [17]"],
]
widths = [13*mm, 43*mm, 38*mm, 22*mm, W - 116*mm]

s = [P("<b>CORY LEA SHEPHERD</b><br/>15 Edmond Street, Coomera QLD 4209 &nbsp;|&nbsp; coryshepherd1@hotmail.com &nbsp;|&nbsp; 0417 400 227", B),
     Spacer(1, 2*mm),
     P("The Registrar<br/>Queensland Industrial Relations Commission<br/>By email: qirc.registry@qirc.qld.gov.au", B),
     Spacer(1, 2*mm),
     P(f"Dated {DATE}", B),
     Spacer(1, 2*mm),
     P("<b>WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator</b><br/>"
       "<b>Direction 5 of the Further Directions Order (3) dated 19 August 2026: request for a second conference</b>", B),
     Spacer(1, 1*mm),
     P("Dear Registrar,", B),

     P("1. The directions", H),
     P("I filed my list of witnesses and served my outlines of evidence, and my schedule of medical documents relied upon, "
       "on 9 September 2026. The Respondent filed its list of witnesses and served outlines of evidence for four lay "
       "witnesses on 24 September 2026." + (" The time for its material under directions 3 and 4 expired at 4.00 pm on "
       "30 September 2026, and it has not served any expert report." if EXPIRED else ""), B),

     P("2. Request", H),
     P("In accordance with direction 5, I ask that the matter be listed for a second conference under section 552A of "
       "the <i>Workers' Compensation and Rehabilitation Act 2003</i>. I propose the following agenda, for the Commission's "
       "consideration:", B),
     P("(a)&nbsp;&nbsp;an agreed list of documents to be tendered without further proof, including the ten documents in "
       "the attached schedule;", L),
     P("(b)&nbsp;&nbsp;any facts or documents the parties can agree in writing, so that evidence on them may be dispensed "
       "with under rule 48 of the <i>Industrial Relations (Tribunals) Rules 2011</i>;", L),
     P("(c)&nbsp;&nbsp;the management action on which the Respondent relies under section 32(5), identified action by "
       "action, with the evidence relied on for each;", L),
     P("(d)&nbsp;&nbsp;the medical evidence: which medical propositions remain in dispute, which reports can be received "
       "by agreement, and which medical witnesses are required to give oral evidence;", L),
     P("(e)&nbsp;&nbsp;the documents referred to in the Respondent's outlines of evidence, which I requested from the "
       "Respondent by letter of 25 September 2026; and", L),
     P("(f)&nbsp;&nbsp;arrangements for the hearing of the issues that remain, including witnesses and estimated length, "
       "and whether, if the parties agree, any issue can be decided on agreed documents.", L),

     P("3. The admissions and documents", H),
     P("On 8 September 2026 the Respondent answered my notices to admit facts and documents of 28 August 2026. It "
       "admitted 298 of the 303 facts and the authenticity of 25 of the 39 documents. On 24 September 2026 it confirmed "
       "four more documents and asked Metro South Health for nine others. The ten that remain are listed in the attached "
       "schedule. I first raised them with the Respondent by letter of 9 September 2026.", B),

     P("4. Questions for the Respondent", H),
     P("I have today provided the Respondent with an issues paper setting out questions arising from its outlines of "
       "evidence and the admissions, for discussion at the conference. I can provide it to the Commission if it would "
       "assist.", B),

     KeepTogether([
       P("I would be assisted by any direction the Commission considers appropriate. If the matter does not resolve, I am "
         "ready to proceed to a hearing on the issues that remain.", B),
       P("A copy of this letter is provided to the Respondent.", B),
       P("Yours faithfully,", B), Spacer(1, 1*mm), SIG(), Spacer(1, 1*mm),
       P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented", B)]),
     PageBreak(),
     P(f"<b>WC/2024/227 &ndash; Schedule to the letter of {DATE}: the ten documents that remain to be confirmed</b>", B),
     P("Tab numbers are those of Annexure A to the Appellant's notices of 28 August 2026. Fact numbers are those of the "
       "Form 24 notice as answered on 8 September 2026. \"SOFC\" is the Respondent's amended statement of facts and "
       "contentions dated 13 May 2026. The 29 other documents annexed to the notices have been admitted (8 September 2026) "
       "or confirmed (24 September 2026: Tabs 6, 20, 30 and 30A).", N),
     Spacer(1, 1*mm),
     P("<b>Part A &ndash; the nine documents the Respondent has asked Metro South Health to provide (24 September 2026)</b>", N),
     table(A, widths),
     Spacer(1, 4*mm),
     KeepTogether([P("<b>Part B &ndash; the one document whose authenticity remains disputed and is not sought from Metro South Health</b>", N),
                   table(Bp, widths)]),
]

buf = io.BytesIO()
d = BaseDocTemplate(buf, pagesize=A4, leftMargin=22*mm, rightMargin=22*mm, topMargin=10*mm, bottomMargin=10*mm)
d.addPageTemplates([PageTemplate(id='n', frames=[Frame(22*mm, 10*mm, A4[0]-44*mm, A4[1]-20*mm,
                    leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
d.build(s); buf.seek(0)
pdf = pikepdf.open(buf); n = len(pdf.pages)
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out = "out/HELD_UNTIL_REGULATOR_RESPONSE/LETTER_TO_REGISTRY_direction5.pdf"; pdf.save(out, linearize=True); print("built", out, n, "page(s)")
