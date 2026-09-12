# -*- coding: utf-8 -*-
"""Strict chronology version. Same verified admitted facts, re-ordered by date,
with a left date column. Black = verbatim admitted fact. Red = joining words only."""
import json, re, html
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)

FACTS = json.load(open('/tmp/claude-0/-home-user/8fe4427c-5b17-5553-9846-1607963b3b30/scratchpad/served_facts.json'))
NOT_ADMITTED = {154, 228, 229, 230, 231}
RED = '#B00020'
USED = []

def T(n):
    assert n not in NOT_ADMITTED, n
    USED.append(n)
    t = html.escape(re.sub(r'\s+', ' ', FACTS[str(n)].strip()), quote=False)
    return '%s <font size="6.5" color="#8A8A8A">[%d]</font>' % (t, n)

def joined(items):
    out = []
    for it in items:
        out.append(('<font color="%s">%s</font>' % (RED, html.escape(it[1], quote=False)))
                   if isinstance(it, tuple) else T(it))
    return ' '.join(out)

# (date column, [facts / ('r', red joining words)])
ROWS = [
 ('17 June 2020',        [17, 21, 22]),
 ('18 July 2023',        [39, 40, 45, 43, 44, ('r','As to restoration of access:'), 55]),
 ('7–8 August 2023',     [26, 27, 28, 29]),
 ('23 August 2023',      [71, 72, 70, 73]),
 ('31 August 2023',      [30, 31, 32]),
 ('4 September 2023',    [33, 34, 35]),
 ('27 September 2023',   [37, 38]),
 ('15 April 2024\n12:39 pm', [49, 51, 50, 52, 53, ('r','As to consultation before it issued:'), 273]),
 ('16–26 April 2024',    [211, 212, 213]),
 ('1 May 2024\n1:18 pm', [214, 215, 216]),
 ('3 May 2024',          [183, 185, 186, 187, 188, 190]),
 ('3 May 2024\n3:06 pm', [56, 57, 58]),
 ('8 May 2024\n9:08 am', [217]),
 ('8 May 2024\n5:28 pm', [59, 60, 61, 62]),
 ('9 May 2024\n9:20 am', [65, 64]),
 ('9 May 2024\n10:15 am',[66, 67]),
 ('10 May 2024\n2:08 pm',[218, 219, 220, 221]),
 ('13 May 2024\n8:21 am',[193]),
 ('15 May 2024\n11:47 am',[89, 90]),
 ('15 May 2024\n1:15 pm',[74, 75]),
 ('15 May 2024\n6:23 pm',[76, 77]),
 ('15 May 2024\n7:09 pm',[78]),
 ('17 May 2024\n9:30 am',[81, 83, 84, 88]),
 ('20 May 2024\n11:03 am',[91, 92, 93]),
 ('20 May 2024\n2:05 pm',[94, 96, 97, 98, 99]),
 ('20 May 2024\n4:07 pm',[222, 223]),
 ('20 May 2024\n4:30 pm',[100, 101, 102, 103, 104,
                          ('r','As to that discussion, and as to any answer to the Respiratory Service:'),
                          105, 106, 107]),
 ('21 May 2024\n12:33 pm',[195]),
 ('21 May 2024\n2:53 pm',[79, 80]),
 ('28 May 2024\n8:36 am',[196, 197, ('r','The employer’s own system records this:'), 200, 201, 210]),
 ('18 June 2024\n8:58 am',[85, 86, 87]),
 ('24 October 2024',     [258, 259, ('r','And found:'), 260]),
 ('',                    [('r','And concluded:'), 261, 262]),
]

# ------------------------------------------------------------------ render
BODY  = ParagraphStyle('B', fontName='Times-Roman', fontSize=9.6, leading=13.6, alignment=4)
DATE  = ParagraphStyle('D', fontName='Times-Bold', fontSize=8.6, leading=11.4,
                       textColor=colors.HexColor('#333333'))
TITLE = ParagraphStyle('T', fontName='Times-Bold', fontSize=17, leading=21, spaceAfter=4)
SUB   = ParagraphStyle('S', fontName='Times-Roman', fontSize=8.6, leading=12.4,
                       textColor=colors.HexColor('#444444'), spaceAfter=3)
NOTE  = ParagraphStyle('N', parent=SUB, fontName='Times-Italic')

def furniture(c, d):
    c.saveState()
    c.setFont('Times-Roman', 7.5); c.setFillColor(colors.HexColor('#777777'))
    c.drawString(18*mm, 12*mm, 'WC/2024/227  –  Shepherd v Workers’ Compensation Regulator')
    c.drawRightString(A4[0]-18*mm, 12*mm, 'Page %d' % c.getPageNumber())
    c.restoreState()

doc = BaseDocTemplate('out/STORY/THE_TWENTY_DAYS_admitted_chronology.pdf', pagesize=A4,
                      leftMargin=18*mm, rightMargin=18*mm, topMargin=18*mm, bottomMargin=20*mm,
                      title='The chronology, in admitted facts', author='')
doc.addPageTemplates([PageTemplate('n', [Frame(18*mm, 20*mm, A4[0]-36*mm, A4[1]-38*mm, id='f')],
                                   onPage=furniture)])

st = [Paragraph('THE CHRONOLOGY, IN ADMITTED FACTS', TITLE),
      Paragraph('WC/2024/227 – Cory Lea Shepherd v Workers’ Compensation Regulator', SUB),
      Spacer(1, 4),
      Paragraph(
        'Every sentence in <b>black</b> is the text of a fact <b>admitted by the Respondent on 8 September 2026</b> '
        'in answer to the notice to admit facts served on 28 August 2026, reproduced word for word, with its number '
        'in that notice in brackets. Admissions are made for this proceeding only, under rule 49 of the '
        '<i>Industrial Relations (Tribunals) Rules 2011</i>. '
        '<font color="%s">Dates in the left column, and words in red, are navigation only. They are not evidence '
        'and are not admitted.</font> No word of the Appellant’s own account appears in this document.' % RED, SUB),
      Spacer(1, 6)]

# the position, as a header block rather than a chapter
st.append(Paragraph('<b>THE POSITION</b>', DATE))
st.append(Paragraph(joined([13, 2, 8, 5, 3]), BODY))
st.append(Spacer(1, 7))

rows = []
for d, items in ROWS:
    rows.append([Paragraph(d.replace('\n', '<br/>'), DATE), Paragraph(joined(items), BODY)])
tbl = Table(rows, colWidths=[26*mm, A4[0]-36*mm-26*mm-4*mm], hAlign='LEFT')
tbl.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (0,-1), 0),
    ('LEFTPADDING', (1,0), (1,-1), 4),
    ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LINEBEFORE', (1,0), (1,-1), 0.5, colors.HexColor('#D6D6D6')),
]))
st.append(tbl)
st.append(Spacer(1, 8))
st.append(Paragraph(
  '%d admitted facts are reproduced above. The Respondent admitted 298 of the 303 facts in the notice. '
  'None of the five facts not admitted appears in this document.' % len(set(USED)), NOTE))

doc.build(st)
print('facts used:', len(set(USED)), '| not-admitted used:', set(USED) & NOT_ADMITTED)
