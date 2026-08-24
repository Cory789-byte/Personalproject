#!/usr/bin/env python3
"""WC/2024/227 - PART B: summary schedule of composite facts, one per stressor limb.

Served WITH the itemised schedule, not instead of it. Each composite is expressly
additive, so a denial of a composite costs nothing: the itemised facts still stand
and are still deemed admitted after 14 days.

Paragraph cross-references are computed from the itemised schedule at build time.
"""
import io, json, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer)

OUT = "out/FORM24_PART_B_SUMMARY.pdf"

# ---- pull the itemised schedule and index it by section letter ----
src = open('build_form24_second.py').read()
_blk = src[src.index('R_TAYLOR ='):src.index('\n]\n', src.index('FACTS = ['))+2]
_ren = src[src.index('_SRC = {'):src.index('_L, _relab')+len('_L, _relab')]
g = {}; exec(_blk, g, g); exec(_ren, g, g)
SEC = {}
cur = None
for f in g['FACTS']:
    if isinstance(f[0], str): cur = f[0]; SEC[cur] = []
    else: SEC[cur].append(f[0])
def rng(*letters):
    ns = sorted(n for L in letters for n in SEC.get(L, []))
    return f"{ns[0]}&ndash;{ns[-1]}" if ns else "-"

# limb, heading, composite (2-3 sentences, fact not conclusion), source sections
ITEMS = [
 ("1(a)", "The database, the directives, and the two accumulations",
  "From 18 July 2023 the Appellant's access to the Switchboard database was removed and, on the "
  "Respondent's pleadings, was not restored before 18 June 2024, while the duties requiring that "
  "access remained assigned to him. During that period the Respondent issued the changes of "
  "15 April 2024, 9 May 2024 and 17 May 2024 to the Switchboard team by email. Between 2 and "
  "8 May 2024 the MASPER Registrar reported nine occasions of misrouted calls to Ms Taylor, and "
  "between 15 and 20 May 2024 the Integrated Respiratory Service twice reported that calls "
  "continued to be misdirected to it.", ("D", "E")),
 ("1(b)", "The communication book",
  "On 6 June 2023 Ms Taylor removed a page from the workplace communication book. In an email to "
  "Ms Reese of the same day she stated: \"I did raise my voice and asked him to please stop "
  "talking over the top of me.\" Both facts were admitted by the Respondent on 18 February 2026.",
  ("R",)),
 ("1(c)", "The matters raised in August and September 2023",
  "On 7 August 2023 the Appellant raised rostering and workplace matters in writing with Ms Taylor "
  "and Ms Reese. Ms Taylor replied the same day acknowledging a rostering oversight, Ms Reese "
  "replied the same day directing him to continue communicating with Ms Taylor, and on 29 August "
  "2023 Ms Reese sent him HR Policy E12. The Appellant did not submit a grievance under that "
  "policy in 2023.", ("G",)),
 ("1(d)", "The Special Pandemic Leave application",
  "The myHR history for Process Reference 15480560 records the Appellant submitting the request on "
  "three occasions between 20 and 29 February 2024, Ms Taylor declining it twice as \"Reviewer\", "
  "then approving it thirteen minutes after the third submission, and Ms Reese approving it as "
  "\"Manager\" on 1 March 2024. The Respondent pleads that a review indicates the attachments were "
  "in fact present and that the decline was \"a matter of human error by Ms Taylor\". The "
  "sub-delegation instrument of 5 December 2022 confines the power to approve or not approve paid "
  "Special Pandemic Leave to a Band 9 delegate and does not permit further sub-delegation.",
  ("F",)),
 ("1(g)", "The union delegate and the roster consultation",
  "In April 2023 the Appellant notified Ms Taylor by text that he was \"just putting his hand up\" "
  "in relation to the role of union delegate, which the Respondent admitted on 18 February 2026. "
  "He was endorsed as a workplace delegate on or about 3 November 2025. The Union Encouragement "
  "Policy QH-POL-248 requires managers to take a \"positive, supportive role\" in relation to "
  "delegate elections.", ("I",)),
 ("2(a)", "The pay corrections",
  "On 3 May 2024 Queensland Health Payroll wrote to Ms Taylor, copied to the Appellant, "
  "identifying incorrect payments across four fortnights and asking that an AVAC be submitted to "
  "correct them. The myHR submissions report for 1 February to 31 May 2024 records five Attendance "
  "Variation and Allowance Claims for the Appellant in that period, the initiator of each being "
  "\"Donovan-Taylor, Chloe\", and none being the Appellant.", ("J",)),
 ("2(b)", "The delay in correcting the pay",
  "Payroll's instruction of 3 May 2024 was followed by Ms Taylor's email of 21 May 2024 stating "
  "she was still awaiting payroll confirmation, and by the submission of an AVAC on 28 May 2024. "
  "The Respondent admitted on 18 February 2026 that the AVAC was submitted on 28 May 2024.",
  ("J",)),
 ("3(a)", "The break of 17 and 18 March 2024",
  "The Appellant was rostered to finish at 23:00 on 17 March 2024 and to commence at 06:00 on "
  "18 March 2024, a break of 7 hours. The Respondent admitted that fact on 18 February 2026 and "
  "pleads it at paragraph 22(a) of its statement of facts and contentions as \"a 7-hour break "
  "(rather than an 8-hour break)\" resulting from \"human error\".", ("L",)),
 ("3(b)", "The minimum break, and what was not in place",
  "The Award and the employer's Fatigue Risk Management Policy require a minimum break of 10 hours "
  "between shifts, or 8 hours by written agreement, which the Respondent admitted on 18 February "
  "2026. The Respondent does not allege that any fatigue risk assessment was conducted, or any "
  "fatigue risk management training provided to the Appellant, at any time before 30 June 2024, "
  "and Metro South Health stated on 5 June 2026 that implementation at Logan Hospital Switchboard "
  "occurred after 30 June 2024.", ("K", "N")),
 ("3(c)", "The fatigue leave request and its refusal",
  "The Appellant requested fatigue payment on 8 April 2024. Ms Taylor escalated the enquiry to "
  "Human Resources on 9 April 2024 and refused it on 1 May 2024, 23 days after the request, on the "
  "basis of an agreement he had signed on 17 June 2020, adding that he was \"able to terminate "
  "this agreement going forward\". The Respondent's own response of 6 September 2024 confirms "
  "there had been a \"change to your employment contract and adjustments in your working hours\" "
  "since that agreement was signed.", ("M", "B")),
 ("3(d)", "The Review Decision",
  "Review Decision 69983 of 24 October 2024 states that the break \"equated to 7 hours\", that the "
  "Appellant \"still did not receive a minimum 8-hour break\", and that \"the rostering of these "
  "two shifts amounted to unreasonable management action\". The Respondent admitted the contents "
  "of that decision on 18 February 2026.", ("P",)),
]

H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=14, leading=17, spaceAfter=3)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=8.8, leading=11.6,
                     textColor=colors.HexColor('#555555'), spaceAfter=6)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.3, leading=12.6, spaceAfter=5)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.8, leading=11.8)
CB  = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')
REF = ParagraphStyle('REF', parent=C, fontSize=8, textColor=colors.HexColor('#555555'),
                     spaceBefore=2)
def P(t, s=C): return Paragraph(t, s)

st = [P("Form 24 &ndash; Notice to admit facts &nbsp;&middot;&nbsp; PART B: SUMMARY SCHEDULE", H1),
      P("WC/2024/227 &middot; Shepherd v Workers' Compensation Regulator", SUB),
      P("<b>This Part is served with, and in addition to, the itemised schedule in Part A. It does "
        "not replace it and does not derogate from it.</b> Each fact below is a composite of facts "
        "already specified in Part A, and the paragraphs of Part A that specify them are identified "
        "against each. It is provided so that the respondent may, if it wishes, admit a limb as a "
        "whole rather than paragraph by paragraph. A response to a fact in this Part is not a "
        "response to any fact in Part A, and the facts in Part A are unaffected by it.", B),
      Spacer(1, 2*mm)]

rows = [[P("<b>Limb</b>", CB), P("<b>Fact to be admitted</b>", CB), P("<b>Admit / Deny</b>", CB)]]
for limb, head, body, secs in ITEMS:
    cell = [P(f"<b>{head}</b>", CB), P(body, C),
            P(f"Specified in Part A at paragraphs {rng(*secs)}.", REF)]
    rows.append([P(f"<b>{limb}</b>"), cell, P("", C)])

t = Table(rows, colWidths=[14*mm, 129*mm, 26*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.7, colors.black),
    ('VALIGN', (0,0), (-1,-1), 'TOP'), ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#ececec')),
    ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('TOPPADDING', (0,0), (-1,-1), 5), ('BOTTOMPADDING', (0,0), (-1,-1), 5)]))
st.append(t)
st.append(Spacer(1, 6*mm))
st.append(P("Signature: ______________________ &nbsp;&nbsp; Print name: Cory Lea Shepherd &nbsp;&nbsp; "
            "Title of office held: Appellant (self-represented) &nbsp;&nbsp; Date: ____ / ____ / ________", B))

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=14*mm, rightMargin=14*mm,
                      topMargin=14*mm, bottomMargin=14*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(14*mm, 14*mm, A4[0]-28*mm, A4[1]-28*mm)])])
doc.build(st); buf.seek(0)
pdf = pikepdf.open(buf)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save(OUT, linearize=True)
print(f"built {OUT} - {len(ITEMS)} composite facts, {len(pdf.pages)} pages")
