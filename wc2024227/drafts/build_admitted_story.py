# -*- coding: utf-8 -*-
"""Builds the workplace narrative using ONLY the text of facts admitted by the
Respondent on 8 September 2026. Black text is verbatim from the served Form 24.
Red text is joining words, added for readability, and is not evidence."""
import json, re, html
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, KeepTogether

FACTS = json.load(open('/tmp/claude-0/-home-user/8fe4427c-5b17-5553-9846-1607963b3b30/scratchpad/served_facts.json'))
NOT_ADMITTED = {154, 228, 229, 230, 231}
RED = '#B00020'

def fact(n):
    t = FACTS[str(n)].strip()
    return html.escape(re.sub(r'\s+', ' ', t), quote=False)

def R(t):  # joining words
    return '<font color="%s">%s</font>' % (RED, html.escape(t, quote=False))

def F(n):  # an admitted fact, verbatim, with its number
    assert n not in NOT_ADMITTED, 'fact %d was not admitted' % n
    USED.add(n)
    return '%s <font size="6.5" color="#8A8A8A">[%d]</font>' % (fact(n), n)

USED = set()

# ---------------------------------------------------------------- the narrative
# Each entry: ('H', heading) or ('P', [pieces])   pieces are F(n) / R('...')
S = []
H = lambda t: S.append(('H', t))
P = lambda *p: S.append(('P', ' '.join(p)))

H('I.  The position')
P(F(1), F(13), F(2))
P(R('The duties included these:'), F(8), F(5), F(10))
P(F(7), F(6), F(12), F(9))
P(R('And the reporting line:'), F(3), F(4))

H('II.  The hours, and what was asked for')
P(F(26), F(30), F(31), F(32))
P(R('The following week:'), F(33), F(34), F(35))
P(R('And in September:'), F(37), F(38))

H('III.  The database is closed')
P(F(39), F(40), F(45), F(43), F(44))
P(R('As to restoration of access:'), F(55))

H('IV.  The manager’s hours')
P(F(71), F(72), F(70))

H('V.  15 April 2024: the new process')
P(F(49), F(51), F(50), F(52), F(53))
P(R('As to consultation before it issued:'), F(273))

H('VI.  May 2024: what was reported')
P(F(56), F(57), F(58))
P(R('Then again, five days later.'), F(59), F(60), F(61), F(62))
P(R('The manager answered the doctors the next morning.'), F(65), F(64))
P(R('Fifty-five minutes after that, she wrote to the operators.'), F(66), F(67))
P(R('Two further matters.'), F(68), F(69))

H('VII.  The Integrated Respiratory Service')
P(F(89), F(90))
P(R('The reminder came five days later.'), F(91), F(92), F(93))
P(R('Three hours after the reminder, the Appellant wrote to the manager.'), F(94), F(96), F(97), F(98))
P(R('The reply came that afternoon.'), F(100), F(101), F(102), F(103), F(104))
P(R('As to that discussion, and as to any answer to the Respiratory Service:'), F(105), F(106), F(107))

H('VIII.  The roster, and what Human Resources was told')
P(F(211), F(212), F(213))
P(R('The Appellant wrote again.'), F(214), F(215), F(216))
P(R('A week later the team leader replied, and then wrote to Human Resources.'), F(217), F(218))
P(F(219), F(220), F(221))
P(R('Ten days after that, she followed up.'), F(222), F(223))

H('IX.  The pay')
P(F(183), F(185), F(186), F(187), F(188), F(190))
P(R('Ten days later, payroll wrote again.'), F(193))
P(R('The manager replied the week after.'), F(195))
P(R('The employer’s own system records this.'), F(200), F(201), F(210))
P(R('The pleaded position:'), F(207), F(208))

H('X.  15 May 2024')
P(F(74), F(75))
P(R('The reply came that evening.'), F(76), F(77))
P(R('The Appellant answered within the hour.'), F(78))
P(R('Two days later the manager wrote to the team.'), F(81), F(82), F(83), F(84), F(88))
P(R('Six days after his email, the team leader replied.'), F(79), F(80))

H('XI.  17–18 March 2024, and the Regulator’s own finding')
P(F(17), F(21), F(22))
P(R('The employer’s pleaded answer:'), F(226))
P(R('The Regulator’s delegate recorded this.'), F(258), F(259), F(260))
P(R('And concluded:'), F(261), F(262))

H('XII.  What is not alleged, and what does not exist')
P(F(269), F(270), F(271), F(272))
P(R('The health service answered the notice of non-party disclosure in these terms:'), F(263), F(265), F(264))
P(F(266), F(267))
P(R('And as to one record:'), F(268))

# ---------------------------------------------------------------- render
BODY = ParagraphStyle('B', fontName='Times-Roman', fontSize=10.5, leading=15.5,
                      spaceAfter=7, alignment=4, textColor=colors.black)
HEAD = ParagraphStyle('H', fontName='Times-Bold', fontSize=11, leading=14,
                      spaceBefore=13, spaceAfter=5, textColor=colors.HexColor(RED))
TITLE = ParagraphStyle('T', fontName='Times-Bold', fontSize=17, leading=21, spaceAfter=4)
SUB = ParagraphStyle('S', fontName='Times-Roman', fontSize=9, leading=13, spaceAfter=3,
                     textColor=colors.HexColor('#444444'))

def furniture(c, d):
    c.saveState()
    c.setFont('Times-Roman', 7.5); c.setFillColor(colors.HexColor('#777777'))
    c.drawString(22*mm, 12*mm, 'WC/2024/227  –  Shepherd v Workers’ Compensation Regulator')
    c.drawRightString(A4[0]-22*mm, 12*mm, 'Page %d' % c.getPageNumber())
    c.restoreState()

doc = BaseDocTemplate('out/STORY/THE_WORKPLACE_IN_ADMITTED_FACTS.pdf', pagesize=A4,
                      leftMargin=22*mm, rightMargin=22*mm, topMargin=20*mm, bottomMargin=20*mm,
                      title='The workplace, in admitted facts', author='')
doc.addPageTemplates([PageTemplate('n', [Frame(22*mm, 20*mm, A4[0]-44*mm, A4[1]-40*mm, id='f')],
                                   onPage=furniture)])

story = [Paragraph('THE WORKPLACE, IN ADMITTED FACTS', TITLE),
         Paragraph('WC/2024/227 – Cory Lea Shepherd v Workers’ Compensation Regulator', SUB),
         Spacer(1, 5)]
story.append(Paragraph(
  'Every sentence in <b>black</b> is the text of a fact <b>admitted by the Respondent on 8 September 2026</b> '
  'in answer to the notice to admit facts served on 28 August 2026, reproduced word for word, with its '
  'number in the notice shown in brackets. The admissions are made for this proceeding only, under rule 49 '
  'of the <i>Industrial Relations (Tribunals) Rules 2011</i>. '
  '<font color="%s">Words in red are joining words only. They are not evidence, they are not admitted, '
  'and nothing turns on them.</font> No word of the Appellant’s own account appears in this document.'
  % RED, SUB))
story.append(Spacer(1, 8))

for kind, txt in S:
    if kind == 'H':
        story.append(Paragraph(txt.upper(), HEAD))
    else:
        story.append(Paragraph(txt, BODY))

story.append(Spacer(1, 10))
story.append(Paragraph(
  '<i>%d admitted facts are reproduced above. The Respondent admitted 298 of the 303 facts in the notice. '
  'None of the five facts not admitted appears in this document.</i>' % len(USED), SUB))

doc.build(story)
print('facts used:', len(USED))
print('any not-admitted used:', USED & NOT_ADMITTED)
