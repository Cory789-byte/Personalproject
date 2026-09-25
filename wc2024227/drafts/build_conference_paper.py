#!/usr/bin/env python3
"""WC/2024/227 - Appellant's conference paper for the second s 552A conference: what is settled, what can be
closed at the conference, and questions for the Respondent arising from its outlines of evidence of
24 September 2026, each set against the admitted facts. States facts, not motives. Metadata stripped."""
import io, sys, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.platypus import Image as RLImage

DATE = sys.argv[1] if len(sys.argv) > 1 else "[date of conference]"

B  = ParagraphStyle('B', fontName='Helvetica', fontSize=9.2, leading=11.8, spaceAfter=4)
T  = ParagraphStyle('T', parent=B, fontName='Helvetica-Bold', fontSize=10.5, leading=13, spaceAfter=2)
H  = ParagraphStyle('H', parent=B, fontName='Helvetica-Bold', spaceBefore=4, spaceAfter=2)
L  = ParagraphStyle('L', parent=B, leftIndent=6*mm, firstLineIndent=-4*mm, spaceAfter=2)
C  = ParagraphStyle('C', parent=B, fontSize=8.1, leading=10.0, spaceAfter=0)
CB = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')
N  = ParagraphStyle('N', parent=B, fontSize=8.2, leading=10.2)
def P(t, s=B): return Paragraph(t, s)
def SIG():
    i = RLImage('assets/SIGNATURE_CoryShepherd.png', width=26*mm, height=13.4*mm); i.hAlign = 'LEFT'; return i

W = A4[0] - 40*mm
def table(rows, widths, bold_first_col=False):
    data = [[P(c, CB) for c in rows[0]]] + [[P(c, CB if (bold_first_col and j == 0) else C) for j, c in enumerate(r)] for r in rows[1:]]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#888888')),
                           ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EEEEEE')),
                           ('VALIGN', (0,0), (-1,-1), 'TOP'),
                           ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
                           ('TOPPADDING', (0,0), (-1,-1), 2), ('BOTTOMPADDING', (0,0), (-1,-1), 2)]))
    return t

CLOSE = [["", "Matter", "What would close it"],
 ["A", "The ten documents not yet admitted or confirmed (Tabs 1, 5, 17 to 19, 21, 22, 23, 24 and 31)",
  "An agreed list of documents to be tendered without further proof, once Metro South Health provides its copies. The contents of all of them except Tab 31 are already admitted"],
 ["B", "Facts 228 to 231: the 2024 Emergency Code Register entries for 17 to 19 March 2024",
  "Production of the MET call spreadsheet that Metro South Health, in its letter of 5 June 2026, states \"is available for the period 17-18 March 2024\" (fact 268)"],
 ["C", "The medical evidence",
  "The Respondent to indicate whether it requires Dr Krishnaiah and Dr Hawes to attend for cross-examination"],
 ["D", "SOFC [27]: the management action said to be reasonable",
  "The Respondent to identify the action or actions relied on. Fact 303 admits that SOFC [27] does not identify them"],
]

Q = [["", "Question for the Respondent", "The admitted record"],
 ["1", "Does the Respondent maintain that no directives were issued without consultation or assessment "
       "(SOFC [11]; outline of Ms Taylor)?",
  "Ms Taylor's email of 15 April 2024: \"This new process is effective from today\" (facts 49 to 53; Tab 6, confirmed "
  "23 September 2026). A further new process from 19 April 2024 (fact 54). No clause 6.2 agreement or ballot is "
  "alleged (facts 180, 181). The Chief Executive's letter of 5 June 2026: fatigue risk assessment at the switchboard "
  "\"occurred after 30 June 2024\" (fact 264; Tab 20, confirmed)"],
 ["2", "Does the Respondent maintain that the 2020 eight-hour agreement applied to the shifts of 17 and 18 March 2024 "
       "(SOFC [22(e)]; outlines of Ms Taylor, Ms Reese and Ms Wright)?",
  "Metro South Health Human Resources, 7 July 2026: the agreement \"is only applied where staff initiated shift swaps "
  "have occurred\" (fact 225). No swap is alleged (fact 234). The employer confirmed a \"change to your employment "
  "contract and adjustments in your working hours\" since 17 June 2020 (fact 20); no review or re-confirmation of the agreement is alleged (fact 21); the Review Unit "
  "found \"uncertainty\" whether it applied (fact 254). The break was seven hours, less than eight on any view "
  "(facts 226, 258, 259)"],
 ["3", "Which management action does the Respondent say was reasonable in respect of the break of 17 to 18 March 2024?",
  "The Respondent's review decision: \"the rostering of these two shifts amounted to unreasonable management action\" "
  "(fact 260). Payroll's advice, in the outline of Ms Wright: \"a rostering practice issue for the line manager\". "
  "SOFC [27] identifies no action (fact 303)"],
 ["4", "Does the Respondent maintain that the break of 17 to 18 March 2024 was \"not intentional or repeated\" in the "
       "sense that no other rostering error affected the Appellant (SOFC [22(a)]; outline of Ms Taylor)?",
  "Ms Taylor, 7 August 2023: \"your rostered Monday 7th... this was an oversight\" (fact 156); Ms Reese, 8 August 2023: "
  "\"a rostering error\" (fact 28); Ms Reese, 26 April 2024: Ms Taylor \"was working to fix this error\" (facts 211, "
  "212); Ms Reese to Human Resources, 10 May 2024: \"I acknowledge there has been a few rostering errors made by Chloe "
  "with regards to Cory's line in past rosters\" (fact 220)"],
 ["5", "Does the Respondent maintain that on 13 to 15 May 2024 the Appellant failed to follow the on-call notification "
       "process (SOFC [16(b)]; outline of Ms Taylor)?",
  "Ms Taylor's email of 15 April 2024: contact her \"through switch/office or mobile\" (fact 163). Her email of 14 May "
  "2024: \"either through switch or my office/mobile\" (facts 164, 165). It is not alleged that the Appellant was told, "
  "before 14 May 2024, that notifying his unavailability by telephoning the Switchboard did not comply (fact 166)"],
 ["6", "Does the Respondent maintain that the Appellant's email of 15 May 2024 was an accusation "
       "(outline of Ms Reese)?",
  "Ms Taylor's email of 23 August 2023, \"What's Chloe's Hours?!\": start \"between 6-9am\", finish \"2-5pm\" "
  "(facts 71, 72; Tab 30, confirmed). No fixed hours stated to May 2024 (fact 73). Ms Reese, 21 May 2024: \"I will follow up on the issues raised\" (fact 79). Ms Taylor published "
  "her hours on 17 May 2024 (facts 81 to 84)"],
 ["7", "Who exercised the delegated power to decide the Special Pandemic Leave application, process 15480560?",
  "SOFC [14] states the attachments were present. Ms Taylor had noted the statutory declaration \"was sufficient "
  "evidence\" (fact 138) and declined the application twice (facts 116, 118, 123). It was approved by Ms Taylor as "
  "reviewer on 29 February and Ms Reese as manager on 1 March 2024 (facts 120, 121). The power was sub-delegated to "
  "Band 9 and could not be sub-delegated further (facts 127, 128); it is not alleged that Ms Taylor or Ms Reese held "
  "it (facts 129 to 131)"],
 ["8", "Does the Respondent maintain that pay errors were \"remedied in a timely manner\" and that there are no "
       "outstanding underpayments (SOFC [20(c)], [20(f)]; outline of Ms Wright)?",
  "Payroll asked the line manager for AVACs on 3 May 2024 (facts 183 to 190). On 13 May payroll could not see that any "
  "had been corrected (facts 192, 193). The AVAC was submitted on 28 May 2024 (fact 297), with claims \"older than 3 "
  "months\" (fact 197), and is recorded as \"Part Completed\" (fact 203). Two AVAC process numbers cited by payroll do "
  "not appear in the myHR report (fact 210)"],
]

s = [P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", N),
     P("WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator", T),
     P("<b>Appellant's conference paper</b> &nbsp;|&nbsp; Conference under section 552A of the <i>Industrial Relations "
       f"Act 2016</i> &nbsp;|&nbsp; {DATE}", B),
     P("This paper is provided for the purposes of the conference. Fact numbers are those of the Appellant's notice to "
       "admit facts of 28 August 2026, as answered by the Respondent on 8 September 2026. Tab numbers are those of "
       "Annexure A to that notice. \"SOFC\" is the Respondent's amended statement of facts and contentions dated "
       "13 May 2026.", N),

     P("1. What is settled", H),
     P("The Respondent admitted 298 of the 303 facts. The other five were not admitted, and none was denied. 29 of "
       "the 39 documents annexed to the notices are admitted or confirmed. No admission has been withdrawn. The "
       "Respondent has served outlines of evidence for four lay witnesses and no medical or expert evidence.", B),

     P("2. What can be closed at this conference", H),
     table(CLOSE, [8*mm, 58*mm, W - 66*mm]),
     Spacer(1, 3*mm),

     P("3. Questions arising from the Respondent's outlines of evidence of 24 September 2026", H),
     P("Each question below arises where a passage in the Respondent's outlines sits beside a fact the Respondent "
       "has admitted. The Appellant asks the Respondent to indicate its position on each, so that the issues for any "
       "hearing can be confined to those genuinely in dispute.", B),
     table(Q, [8*mm, 62*mm, W - 70*mm]),
     Spacer(1, 3*mm),

     KeepTogether([
       P("4. The Appellant's position", H),
       P("On the admitted record, the Appellant considers that the primary facts are settled and that the matters "
         "remaining are the application of the law to those facts and the medical evidence. The Appellant invites "
         "the Respondent to consider its position on the admitted record. If the matter does not resolve, the "
         "Appellant is ready to proceed to a hearing on the issues that remain.", B),
       Spacer(1, 1*mm), SIG(),
       P("<b>Cory Lea Shepherd</b><br/>Appellant, self-represented", B)]),
]

buf = io.BytesIO()
d = BaseDocTemplate(buf, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=11*mm, bottomMargin=11*mm)
d.addPageTemplates([PageTemplate(id='n', frames=[Frame(20*mm, 11*mm, A4[0]-40*mm, A4[1]-22*mm,
                    leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
d.build(s); buf.seek(0)
pdf = pikepdf.open(buf); n = len(pdf.pages)
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out = "out/CONFERENCE_PAPER_s552A_Appellant.pdf"; pdf.save(out, linearize=True); print("built", out, n, "page(s)")
