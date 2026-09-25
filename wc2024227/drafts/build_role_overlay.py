#!/usr/bin/env python3
"""WC/2024/227 - THE ROLE OVERLAY.

The position as the role description states it, and against each duty, the facts the
Respondent admitted on 8 September 2026, in full and word for word.

Facts are the 303 paragraphs of the notice to admit facts served 28 August 2026 as the
Respondent answered them on 8 September 2026, read from
documents/regulator-response-2026-09-08/SERVED_303_facts_and_verdicts.json via served_facts.py.
Not from build_form24_second.py, which is a working draft and has moved on from what was served.

INTERNAL working document. No characterisation; every black and blue line is the text
of a document. Red is navigation only and is not evidence.
"""
import io, re, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, KeepTogether

from served_facts import FACT, NOT_ADMITTED, TOTAL   # the 303 facts as served and answered
assert TOTAL == 303

BLUE = colors.HexColor('#123f8c'); GREY = colors.HexColor('#6b6b6b'); RED = colors.HexColor('#8a2b2b')
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=15.5, spaceAfter=2)
H2  = ParagraphStyle('H2', fontName='Helvetica', fontSize=8.4, leading=10.5, textColor=GREY, spaceAfter=5)
KEY = ParagraphStyle('KEY', fontName='Helvetica', fontSize=7.7, leading=9.6, spaceAfter=2)
SEC = ParagraphStyle('SEC', fontName='Helvetica-Bold', fontSize=9.6, leading=12,
                     spaceBefore=8, spaceAfter=3, textColor=colors.HexColor('#1a1a1a'))
DUTY= ParagraphStyle('DUTY', fontName='Helvetica', fontSize=8.4, leading=10.6, leftIndent=4*mm,
                     spaceAfter=2)
LEAD= ParagraphStyle('LEAD', fontName='Helvetica-Bold', fontSize=8.1, leading=10, leftIndent=4*mm,
                     textColor=BLUE, spaceBefore=2, spaceAfter=1.5)
ADM = ParagraphStyle('ADM', fontName='Helvetica', fontSize=8.0, leading=9.9, leftIndent=4*mm,
                     textColor=BLUE, spaceAfter=1.2)
NAV = ParagraphStyle('NAV', fontName='Helvetica-Oblique', fontSize=7.8, leading=9.6, leftIndent=4*mm,
                     textColor=RED, spaceAfter=4)
def P(t, s): return Paragraph(t, s)
def facts(ns):
    out = []
    for n in ns:
        mark = ' <b>[NOT ADMITTED]</b>' if n in NOT_ADMITTED else ''
        out.append(P(f"<b>[{n}]</b> {FACT[n]}{mark}", ADM))
    return out
def duties(ns):
    return [P(f"<b>[{n}]</b> {FACT[n]}", DUTY) for n in ns]

# (section heading, duty fact numbers, admitted fact numbers, navigation line)
S = [
("A. &nbsp;The position", [1, 2, 3, 4, 13, 14, 15, 16], [],
 "The role description was provided to the Appellant in 2026. The contemporaneous anchors for the "
 "period in issue are the documents at B to H below."),

("B. &nbsp;The duty to keep the information accurate", [6, 7],
 [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 54, 55, 89, 90, 91, 92, 94, 95, 96, 97, 98, 100, 101,
  102, 103, 104, 105, 106, 107, 109, 110],
 "The duty to ensure the information held within Switchboard Services is accurate and current is a "
 "key responsibility of the position. From 18 July 2023 the access required to perform it was held "
 "by others, and the Respondent does not allege it was restored before 18 June 2024."),

("C. &nbsp;The duty to distribute emergency notifications within protocol timeframes", [8],
 [49, 50, 51, 52, 53, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
 "The duty is expressed in terms of protocols and timeframes. The nine occasions reported by the "
 "MASPER Registrar fell while the after-hours arrangement of 15 April 2024 was in force, and the "
 "Respondent does not allege the Switchboard was told of them before 10:15 am on 9 May 2024."),

("D. &nbsp;The duty to hold call queues to a minimum under high volume", [5, 10],
 [227, 228, 229, 230, 231, 267, 268],
 "The emergency load carried on the two shifts of 17 and 18 March 2024 is the material the "
 "Respondent has not admitted. Metro South Health has stated that a spreadsheet of recorded MET "
 "calls is available for that period. This is the outstanding item in the request of 9 September 2026."),

("E. &nbsp;The mandatory requirement of continuous shift work over a 24/7 period", [2, 13],
 [211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 232, 233, 234,
  235, 236, 237, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 257, 258, 259, 260],
 "The position is a continuous shift working role. The two shifts of 17 and 18 March 2024 produced "
 "a break the Respondent's own review decision measures at seven hours and finds to be unreasonable "
 "management action."),

("F. &nbsp;Reporting to the Switchboard Manager, and the named contact for the position", [3, 4],
 [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 162, 163, 164, 165, 166],
 "The position reports to one manager and names one contact. Both the process for notifying "
 "unavailability and the after-hours process required that contact to be reached."),

("G. &nbsp;The duty to exercise judgement where procedures are not defined", [9, 11],
 [143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154],
 "Two documented occasions on which judgement was exercised within the scope of the role: the "
 "Communication Book entry of 6 June 2023, and the recommendation of 20 May 2024 at section B above."),

("H. &nbsp;The duty to follow occupational health and safety policies and procedures", [12],
 [263, 264, 265, 266, 269, 270, 271, 272, 273],
 "The duty is to follow the policies and procedures relating to the work being undertaken. The "
 "employer has stated in writing what did and did not exist for this position over the period."),

("I. &nbsp;What the Respondent does not allege about the Appellant's performance of the role", [],
 [300, 301, 302, 303],
 "Four negatives, each tied to the pleading as presently constituted."),
]

s = [P("THE ROLE OVERLAY &ndash; THE POSITION, AND THE ADMITTED FACTS", H1),
     P("WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator.", H2),
     P("<b>Black</b> is the text of the role description for the position of Administration Officer, "
       "Switchboard Services, Logan Hospital, word for word, with the number of the fact admitting it "
       "in brackets. <font color='#123f8c'><b>Blue</b> is the text of a fact admitted by the "
       "Respondent on 8 September 2026 in answer to the notice to admit facts served 28 August 2026, "
       "word for word and in full, with its number on that notice in brackets. Admissions are for this "
       "proceeding only, under rule 49 of the Industrial Relations (Tribunals) Rules 2011.</font> "
       "<font color='#8a2b2b'><b>Red is navigation only. It is not evidence.</b></font> No word of the "
       "Appellant's own account appears in this document.", KEY),
     P("⛔ <b>INTERNAL working document.</b> Five facts were not admitted and are marked where they "
       "appear. Nothing in the notice was denied.", KEY),
     Spacer(1, 2*mm)]

for head, ds, fs, nav in S:
    s.append(P(head, SEC))
    if ds:
        s.append(P("The role description states:", LEAD))
        s.extend(duties(ds))
    if fs:
        s.append(P("The Respondent admitted on 8 September 2026:", LEAD))
        s.extend(facts(fs))
    s.append(P(nav, NAV))

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                      topMargin=12*mm, bottomMargin=12*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[
    Frame(15*mm, 11*mm, A4[0]-30*mm, A4[1]-23*mm, leftPadding=0, rightPadding=0,
          topPadding=0, bottomPadding=0)])])
doc.build(s); buf.seek(0)
pdf = pikepdf.open(buf)
n = len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out = "INTERNAL/2026-09-12_ROLE_OVERLAY_the_position_and_the_admitted_facts.pdf"
pdf.save(out, linearize=True)
used = sorted({x for _, _, fs, _ in S for x in fs} | {x for _, ds, _, _ in S for x in ds})
print(f"built {out} - {len(S)} sections, {len(used)} facts, {n} page(s)")
