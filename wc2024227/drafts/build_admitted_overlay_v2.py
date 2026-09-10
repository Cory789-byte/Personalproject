# -*- coding: utf-8 -*-
"""Chronology with the medical overlaid. BLACK = admitted fact, verbatim from the
served Form 24. BLUE = medical, verbatim from the Appellant's schedule of medical
documents served 9 September 2026. RED = joining words, not evidence."""
import json, re, html
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle)

FACTS = json.load(open('/tmp/claude-0/-home-user/8fe4427c-5b17-5553-9846-1607963b3b30/scratchpad/served_facts.json'))
NOT_ADMITTED = {154, 228, 229, 230, 231}
RED, BLUE = '#B00020', '#0B4F9E'
USED = []

def T(n):
    assert n not in NOT_ADMITTED, n
    USED.append(n)
    t = html.escape(re.sub(r'\s+', ' ', FACTS[str(n)].strip()), quote=False)
    return '%s <font size="6.5" color="#8A8A8A">[%d]</font>' % (t, n)

def M(tag, t):   # medical, from the served schedule
    return '<font color="%s">%s <font size="6.5" color="#7794B8">[%s]</font></font>' % (
        BLUE, html.escape(t, quote=False), tag)

def R(t):
    return '<font color="%s">%s</font>' % (RED, html.escape(t, quote=False))

def row(items):
    return ' '.join(it if isinstance(it, str) else T(it) for it in items)

ROWS = [
 ('17 June 2020',        [17, 21, 22]),
 ('18 July 2023',        [39, 40, 45, 43, 44, R('As to restoration of access:'), 55]),
 ('7–8 August 2023',     [26, 28]),
 ('23 August 2023',      [71, 72, 73]),
 ('31 August 2023',      [30, 31, 32]),
 ('4 September 2023',    [33, 34]),
 ('27 September 2023',   [37, 38]),
 ('16 November 2023',    [M('M1','General-practice records, Our Medical Ashmore: the entry of 16 November 2023 (Dr Nanayakkara) recording poor sleep with shift work, that the Appellant could not do shifts without a good sleep, no psychological illness such as depression or psychosis, and mood good, with melatonin and temazepam prescribed.')]),
 ('20 February 2024',   [136]),
 ('21 February 2024',   [137, 138, R('The pleaded answer:'), 132, 133, 135,
                         R('As to whether that was required of anyone else:'), 142]),
 ('17–18 March 2024',   [284, 227, R('As to how those shifts arose:'), 234, 180]),
 ('15 April 2024\n12:39 pm', [49, 51, 50, 53, R('As to consultation before it issued:'), 273]),
 ('16–26 April 2024',    [211, 212, 213]),
 ('1 May 2024\n1:18 pm', [214, 215, 216, R('And on the same day:'), 247]),
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
 ('16 May 2024',         [M('M1','The referral letter of 16 May 2024 (Dr Zhao), renewing a referral to a psychiatrist, Dr Amini, for "ongoing care and management", which lists among the past-medical-history items "26/10/2022 ADHD" and "26/10/2022 Anxiety", and lists the medications then current, none of which is an antidepressant or an anxiolytic.')]),
 ('17 May 2024\n9:30 am',[81, 83, 84, 88]),
 ('20 May 2024\n11:03 am',[91, 92, 93]),
 ('20 May 2024\n2:05 pm',[94, 96, 97, 98, 99]),
 ('20 May 2024\n4:07 pm',[222, 223]),
 ('20 May 2024\n4:30 pm',[100, 101, 102, 103, 104,
                          R('As to that discussion, and as to any answer to the Respiratory Service:'), 105, 106, 107]),
 ('21 May 2024\n12:33 pm',[195]),
 ('21 May 2024\n2:53 pm',[79, 80]),
 ('28 May 2024\n8:36 am',[196, 197, R('The employer’s own system records this:'), 200, 201, 210]),
 ('18 June 2024\n8:58 am',[85, 86, 87,
                           M('M2','The work capacity certificates of Dr Peter Hawes record the stated date of injury as 18 June 2024.')]),
 ('28 June 2024',        [M('M1','28 June 2024 (Dr Slawinski) recording "stress at work" and "upset by people not following rules", reason for visit anxiety.')]),
 ('1 July 2024',         [M('M1','1 July 2024 (Dr Hawes) recording "work stress", "been there 5 years", that "they withhold pay at times, no overtime- not processed, manipulate his roster- so he works lates then earlies", and "causing anxiety".'),
                          M('M2','That the Appellant was first seen for this injury on 1 July 2024; certification of no functional capacity for any type of work over the period 1 July to 6 October 2024. Review Decision 69983 records that the certificate of 1 July 2024 indicated "there was no pre-existing factor or condition", and that "This was maintained in all later work capacity certificates".')]),
 ('2 September 2024',    [M('M9','The Respondent’s own review recorded Dr Hawes’s statement to WorkCover of 2 September 2024 that work events were the sole cause.')]),
 ('8 September 2024',    [M('M2','The referral to a psychiatrist recorded on 8 September 2024.')]),
 ('24 October 2024\n11:45 am', [M('M3','That on the morning of 24 October 2024, at the first consultation, the treating psychiatrist told the Appellant, and confirmed in writing at 11:45 am that day, that he was "suffering from psychological injury of Major Depressive Disorder with anxiety state"; that fluoxetine was increased to two capsules "from today" and Seroquel 25 mg commenced at night, "to restore basic needs- sleep, eating and routine".')]),
 ('24 October 2024',     [253, 258, 259, R('And found:'), 260]),
 ('',                    [R('And concluded:'), 261, 262]),
 ('13 February 2025',    [M('M4','Diagnosis: Major Depressive Disorder with anxious distress (DSM-5 296.23). The treating clinician’s account of origin: "workplace stress stemming from issues with management and rostering"; that the issues "began approximately one year ago when a new manager was appointed"; pay "withheld or delayed for up to five months at a time, leading to significant financial stress".')]),
 ('3 July 2026',         [M('M8','Employee Capability Checklist completed by Dr Day Hong Ma: current capacity and restrictions, and the continuing effect of the injury, including "symptom exacerbation on exposure to the identified workplace stressors".')]),
]

BODY  = ParagraphStyle('B', fontName='Times-Roman', fontSize=9.4, leading=13.2, alignment=4)
DATE  = ParagraphStyle('D', fontName='Times-Bold', fontSize=8.5, leading=11.2, textColor=colors.HexColor('#333333'))
TITLE = ParagraphStyle('T', fontName='Times-Bold', fontSize=16.5, leading=20, spaceAfter=4)
SUB   = ParagraphStyle('S', fontName='Times-Roman', fontSize=8.5, leading=12.2,
                       textColor=colors.HexColor('#444444'), spaceAfter=3)
NOTE  = ParagraphStyle('N', parent=SUB, fontName='Times-Italic')

def furniture(c, d):
    c.saveState(); c.setFont('Times-Roman', 7.5); c.setFillColor(colors.HexColor('#777777'))
    c.drawString(18*mm, 12*mm, 'WC/2024/227  –  Shepherd v Workers’ Compensation Regulator')
    c.drawRightString(A4[0]-18*mm, 12*mm, 'Page %d' % c.getPageNumber()); c.restoreState()

doc = BaseDocTemplate('out/STORY/THE_OVERLAY_v2_February_to_July.pdf', pagesize=A4,
                      leftMargin=18*mm, rightMargin=18*mm, topMargin=18*mm, bottomMargin=20*mm,
                      title='The overlay: admitted facts and the medical', author='')
doc.addPageTemplates([PageTemplate('n', [Frame(18*mm, 20*mm, A4[0]-36*mm, A4[1]-38*mm, id='f')], onPage=furniture)])

st = [Paragraph('THE OVERLAY — THE ADMITTED FACTS AND THE MEDICAL', TITLE),
      Paragraph('WC/2024/227 – Cory Lea Shepherd v Workers’ Compensation Regulator', SUB),
      Spacer(1, 4),
      Paragraph(
        '<b>Black</b> is the text of a fact <b>admitted by the Respondent on 8 September 2026</b> in answer to the '
        'notice to admit facts served on 28 August 2026, word for word, with its number in that notice in brackets. '
        'Admissions are for this proceeding only, under rule 49 of the <i>Industrial Relations (Tribunals) Rules 2011</i>. '
        '<font color="%s">Blue is the medical, word for word from the Appellant’s schedule of medical documents served '
        '9 September 2026, with its tab in brackets; it is relied upon for the existence and wording of the document, '
        'and for clinical opinion only through the oral evidence of its author.</font> '
        '<font color="%s">Dates in the left column, and words in red, are navigation only. They are not evidence.</font> '
        'No word of the Appellant’s own account appears in this document.' % (BLUE, RED), SUB),
      Spacer(1, 6),
      Paragraph('<b>THE POSITION</b>', DATE),
      Paragraph(row([13, 2, 8, 5, 3]), BODY),
      Spacer(1, 7)]

rows = [[Paragraph(d.replace('\n','<br/>'), DATE), Paragraph(row(items), BODY)] for d, items in ROWS]
tbl = Table(rows, colWidths=[26*mm, A4[0]-36*mm-26*mm-4*mm], hAlign='LEFT')
tbl.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(0,-1),0), ('LEFTPADDING',(1,0),(1,-1),4),
    ('RIGHTPADDING',(0,0),(-1,-1),0), ('TOPPADDING',(0,0),(-1,-1),5),
    ('BOTTOMPADDING',(0,0),(-1,-1),5),
    ('LINEBEFORE',(1,0),(1,-1),0.5,colors.HexColor('#D6D6D6'))]))
st += [tbl, Spacer(1, 8),
       Paragraph('%d admitted facts are reproduced above. The Respondent admitted 298 of the 303 facts in the '
                 'notice; none of the five not admitted appears here. The medical entries are the documents at '
                 'Tabs M1 to M9 of the schedule served on 9 September 2026, each already held by the Respondent '
                 'at the item of its amended List of Documents dated 14 August 2026 stated in that schedule.'
                 % len(set(USED)), NOTE)]
doc.build(st)
print('facts:', len(set(USED)), '| not-admitted:', set(USED) & NOT_ADMITTED)
