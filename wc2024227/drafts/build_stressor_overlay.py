#!/usr/bin/env python3
"""WC/2024/227 - THE STRESSOR OVERLAY.

The three stressors, built only from the facts the Respondent answered on 8 September 2026,
with the role description placed at each point where a duty bears on what follows, and the
2024 Emergency Code Register carried in red as material still to be admitted.

Facts are pulled from build_form24_second.py with the renumber pass applied, so every number
is the number on the served Form 24 and no text is retyped.
"""
import io, re, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer

src = open('build_form24_second.py').read()
_blk = src[src.index('R_TAYLOR ='):src.index('\n]\n', src.index('FACTS = ')) + 2]
_end = "del _n, _new, _L, _relab, _prev"
_ren = src[src.index('import re as _re'):src.index(_end) + len(_end)]
_g = {}; exec(_blk, _g, _g); exec(_ren, _g, _g)
F = {f[0]: re.sub(r'\s+', ' ', f[1]).strip() for f in _g['FACTS'] if not isinstance(f[0], str)}
assert len(F) == 308, len(F)
PENDING = {154, 228, 229, 230, 231}

BLUE = colors.HexColor('#123f8c'); GREY = colors.HexColor('#6b6b6b'); RED = colors.HexColor('#9b1c1c')
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=15.5, spaceAfter=2)
H2  = ParagraphStyle('H2', fontName='Helvetica', fontSize=8.4, leading=10.5, textColor=GREY, spaceAfter=4)
KEY = ParagraphStyle('KEY', fontName='Helvetica', fontSize=7.6, leading=9.4, spaceAfter=2)
STR = ParagraphStyle('STR', fontName='Helvetica-Bold', fontSize=11, leading=13.5, spaceBefore=9,
                     spaceAfter=3)
SUB = ParagraphStyle('SUB', fontName='Helvetica-Bold', fontSize=9, leading=11.5, spaceBefore=6,
                     spaceAfter=2.5, textColor=colors.HexColor('#1a1a1a'))
POS = ParagraphStyle('POS', fontName='Helvetica', fontSize=8.0, leading=9.9, leftIndent=4*mm,
                     textColor=BLUE, spaceAfter=1.2)
ADM = ParagraphStyle('ADM', fontName='Helvetica', fontSize=8.0, leading=9.9, leftIndent=4*mm,
                     spaceAfter=1.2)
PEN = ParagraphStyle('PEN', fontName='Helvetica', fontSize=8.0, leading=9.9, leftIndent=4*mm,
                     textColor=RED, spaceAfter=1.2)
NOTE= ParagraphStyle('NOTE', fontName='Helvetica-Oblique', fontSize=7.6, leading=9.4,
                     leftIndent=4*mm, textColor=RED, spaceAfter=3)
def P(t, s): return Paragraph(t, s)

def block(ns, role=False):
    out = []
    for n in ns:
        if n in PENDING:
            out.append(P(f"<b>[{n}]</b> {F[n]}", PEN))
        elif role:
            out.append(P(f"<b>THE POSITION &mdash; [{n}]</b> {F[n]}", POS))
        else:
            out.append(P(f"<b>[{n}]</b> {F[n]}", ADM))
    return out

REGISTER_NOTE = (
 "[TO BE ADMITTED &mdash; the four paragraphs above are the 2024 Emergency Code Register, a "
 "Metro South Hospital and Health Service workbook kept at Logan Hospital Switchboard and "
 "produced at Tab 31. They were not admitted on 8 September 2026 and no reason was given; the "
 "authenticity of Tab 31 is disputed on the Form 25 while the contents of the other tabs are "
 "admitted. Metro South Health has stated in writing that \"a spreadsheet of recorded MET calls "
 "is available for the period 17-18 March 2024\" (admitted, paragraph 268 at 1(j) above). The Respondent "
 "was asked to produce it on 9 September 2026 and replied on 10 September 2026 seeking until "
 "25 September 2026.]")
BOOK_NOTE = (
 "[NOT ADMITTED &mdash; and not pressed. Item 37 of the Respondent's amended List of Documents "
 "holds a photograph of the Communication Book.]")

DOC = [
 ("THE POSITION", None, None),
 (None, "The role description, and the shift arrangement recorded for the position",
  [("role", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), ("f", [14, 15, 16])]),

 ("STRESSOR 1 &ndash; THE CONDITIONS OF THE WORK, AND WHAT FOLLOWED WHAT WAS RAISED", None, None),
 (None, "1(a) &nbsp;The directory, and the means of correcting it",
  [("role", [6, 7]), ("f", list(range(39, 49))), ("f", [54, 55])]),
 (None, "1(b) &nbsp;The after-hours arrangement, and how the manager was to be reached",
  [("role", [3, 4]), ("f", list(range(49, 54))), ("f", [273]), ("f", list(range(111, 114))), ("f", list(range(162, 167)))]),
 (None, "1(c) &nbsp;The emergency notifications, 2 to 9 May 2024",
  [("role", [8, 5, 10]), ("f", list(range(56, 70)))]),
 (None, "1(d) &nbsp;The Integrated Respiratory Service, and the recommendation of 20 May 2024",
  [("role", [9]), ("f", list(range(89, 111)))]),
 (None, "1(e) &nbsp;The hours of the manager to whom the position reports",
  [("role", [3, 4]), ("f", list(range(70, 89)))]),
 (None, "1(f) &nbsp;The Communication Book",
  [("role", [9, 12]), ("f", list(range(143, 155))), ("note", BOOK_NOTE)]),
 (None, "1(g) &nbsp;The hours sought, and the matters raised in August and September 2023",
  [("f", list(range(26, 39))), ("f", list(range(155, 162)))]),
 (None, "1(h) &nbsp;The special pandemic leave application of February 2024",
  [("f", list(range(114, 143)))]),
 (None, "1(i) &nbsp;The union delegate, and the consultation on rosters",
  [("f", list(range(167, 182)))]),
 (None, "1(j) &nbsp;What the employer says of its own systems and records",
  [("role", [12]), ("f", list(range(263, 273)))]),

 ("STRESSOR 2 &ndash; THE PAY", None, None),
 (None, "2(a) &nbsp;The correction, and who could make it",
  [("role", [2, 13]), ("f", list(range(182, 211)))]),

 ("STRESSOR 3 &ndash; THE ROSTER AND FATIGUE", None, None),
 (None, "3(a) &nbsp;The roster line, and what was written about it",
  [("role", [2, 13]), ("f", list(range(211, 224)))]),
 (None, "3(b) &nbsp;The shifts of 17 and 18 March 2024, and the agreement of 17 June 2020",
  [("f", list(range(17, 26))), ("f", list(range(224, 228))),
   ("f", [228, 229, 230, 231]), ("note", REGISTER_NOTE), ("f", list(range(232, 242)))]),
 (None, "3(c) &nbsp;The request of 8 April 2024, the delay, and the refusal of 1 May 2024",
  [("f", list(range(242, 257)))]),
 (None, "3(d) &nbsp;The Respondent's own review decision of 24 October 2024",
  [("f", list(range(257, 263)))]),

 ("THE RECORD, AND WHAT THE RESPONDENT DOES NOT ALLEGE", None, None),
 (None, "4(a) &nbsp;What was provided, and what the Respondent lists",
  [("f", list(range(274, 283)))]),
 (None, "4(b) &nbsp;Facts already admitted in this proceeding on 18 February 2026",
  [("f", list(range(283, 305)))]),
 (None, "4(c) &nbsp;Matters the Respondent does not allege",
  [("f", list(range(305, 309)))]),
]

s = [P("THE STRESSOR OVERLAY &ndash; THE POSITION, THE THREE STRESSORS, AND THE ADMITTED FACTS", H1),
     P("WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator.", H2),
     P("<b>Black</b> is the text of a fact the Respondent admitted on 8 September 2026 in answer to "
       "the notice to admit facts served 28 August 2026, word for word and in full, with its number "
       "on that notice in brackets. Admissions are for this proceeding only, under rule 49 of the "
       "Industrial Relations (Tribunals) Rules 2011. "
       "<font color='#123f8c'><b>Blue</b> is the same, where the fact is the text of the role "
       "description for the position; it is placed at each point where the duty bears on what "
       "follows; where a duty bears at more than one point, the same paragraph is placed again.</font> "
       "<font color='#9b1c1c'><b>Red is material still to be admitted</b>, carried here so the gap "
       "is visible, with its status in square brackets beneath it.</font> "
       "Headings and dates are navigation only and are not evidence. No word of the Appellant's own "
       "account appears in this document.", KEY),
     Spacer(1, 2*mm)]

for stress, sub, parts in DOC:
    if stress:
        s.append(P(stress, STR)); continue
    s.append(P(sub, SUB))
    for kind, payload in parts:
        if kind == "note":
            s.append(P(payload, NOTE))
        else:
            s.extend(block(payload, role=(kind == "role")))

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
out = "INTERNAL/2026-09-12_STRESSOR_OVERLAY_position_stressors_admitted_facts.pdf"
pdf.save(out, linearize=True)

used = []
for _, _, parts in DOC:
    if not parts: continue
    for kind, payload in parts:
        if kind != "note": used += payload
seen = sorted(set(used))
missing = [i for i in range(1, 309) if i not in seen]
dupes = sorted({x for x in used if used.count(x) > 1})
print(f"built {out} - {n} page(s); {len(seen)} of 308 facts placed")
print("missing:", missing if missing else "none")
print("placed twice (role lines repeated by design):", dupes)
