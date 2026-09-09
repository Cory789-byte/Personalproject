#!/usr/bin/env python3
"""WC/2024/227 — the two disclosure lists against the pleading, as a document.

The Respondent's amended List of Documents (Form 23) of 14 August 2026, 52 items, mapped onto the
Amended Statement of Facts and Contentions filed 7 April 2026, against what the Appellant holds.

⛔ Working document. Not for service and not for filing. It is the working paper behind an
inspection request, not the request itself.

Output: out/DISCLOSURE_COMPARED_BY_9A_WC2024227.pdf
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether)
import pikepdf

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
OUT = "out/DISCLOSURE_COMPARED_BY_9A_WC2024227.pdf"
DATE = "9 September 2026"

HD  = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.2, leading=10.4,
                     textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2 = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=9)
TT  = ParagraphStyle('TT', fontName='Helvetica-Bold', fontSize=12.5, leading=15.5, spaceAfter=3)
WARN= ParagraphStyle('WARN', fontName='Helvetica-Bold', fontSize=7.6, leading=9.8,
                     textColor=colors.HexColor('#8a2010'), spaceAfter=6)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=7.8, leading=10, spaceAfter=5)
PART= ParagraphStyle('PART', fontName='Helvetica-Bold', fontSize=9.4, leading=12,
                     spaceBefore=7, spaceAfter=3)
SEC = ParagraphStyle('SEC', fontName='Helvetica-Bold', fontSize=8.2, leading=10.5,
                     spaceBefore=5, spaceAfter=2)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=7.2, leading=9.1, spaceAfter=0)
CB  = ParagraphStyle('CB', parent=C, fontName='Helvetica-Bold')
CG  = ParagraphStyle('CG', parent=C, textColor=colors.HexColor('#8a2010'),
                     fontName='Helvetica-Bold')

W = A4[0] - 30*mm

SHAPE = [
 ("Total items on the Respondent's list", "52"),
 ("Items that are the Appellant's own emails to WorkCover (items 12&ndash;16, 18&ndash;30, 32&ndash;36)", "about 25"),
 ("Items sourced from the employer (17, 31, 37, 38, 39, 41, 43)", "7"),
 ("&mdash; of those, obtained through witness conferencing in July 2025 (37, 38, 39, 41)", "4"),
 ("Notices of non-party disclosure (40, 42, 43)", "3"),
 ("Insurer file and miscellaneous (44&ndash;52)", "9"),
 ("Rosters", "none"),
 ("Emergency-code or paging material", "none"),
 ("Rosters held by the Appellant", "91"),
]

# (limb, [(their item, their description, held?, where)])
LIMBS = [
 ("Stressor 1(a) &mdash; the directives and the workflow", [
  ("25", "Email: After hours on call process", 1, "Annexure A Tab 6"),
  ("27", "Email: MASPER process &ndash; 09/05/2024", 1, "Annexure A Tab 8B"),
  ("21", "Email: Respiratory nurse educators &ndash; 15 to 20/05/2024", 1, "Annexure A Tab 11"),
  ("38", "Email C Taylor to Switch &ndash; Manager on call hours &ndash; 17/05/2024", 1, "Annexure A Tab 9"),
  ("39", "Email chain C Taylor &amp; APP &ndash; updating doc: respiratory nurse educators &ndash; 20/05/2024", 1, "Annexure A Tab 11"),
  ("26", "Email: Task change switchboard &ndash; 19/04/2024", 0, "not held"),
  ("39", "Email C Taylor to A McNamee &ndash; background to request hours &ndash; 17/05/24", 0, "not held"),
 ]),
 ("Stressor 1(b) &mdash; the Communication Book", [
  ("37", "Email C Taylor to T Reese &ndash; Comms book &ndash; 06/06/2023", 1, "Annexure A Tab 1B"),
  ("37", "Email C Taylor to Switch &ndash; Comms book &ndash; 06/06/2023", 1, "Annexure A Tab 1B, beneath"),
  ("37", "<b>Photo comms book &ndash; 20/05/2024</b>", 0, "not held"),
  ("37", "Email C Taylor to C Jeffrey &ndash; Comms book &ndash; 21/05/2024", 0, "not held"),
 ]),
 ("Stressor 1(c) &mdash; August and September 2023", [
  ("37", "Email chain APP &amp; T Reese &ndash; increase hours &ndash; 07 to 08/09/2023", 1, "Annexure A Tabs 2, 3"),
  ("37", "Email C Taylor to APP &ndash; acknowledge increase in hours", 1, "Annexure A Tab 5"),
  ("37", "<b>Email T Reese to C Taylor &ndash; roster and comms with APP &ndash; 07/08/23</b>", 0, "not held"),
  ("37", "Email chain C Taylor &amp; APP &ndash; Request discussion on rostering &ndash; 14 to 15/11/23", 0, "not held"),
 ]),
 ("Stressor 1(d) &mdash; pandemic leave, February to March 2024", [
  ("30", "Screenshots &ndash; myHR leave and issues", 1, "Annexure A Tabs 15, 28"),
  ("40, 42", "Notices of non-party disclosure, Queensland Health payroll", 1, "Annexure A Tabs 15, 28, 29"),
 ]),
 ("Stressor 1(e) and 1(f) &mdash; 13 to 21 May 2024", [
  ("38", "Email APP to parties &ndash; Request C Taylor hours &amp; directives &ndash; 15/05/2024", 1, "Annexure A Tab 9A"),
  ("38", "Email T Reese to APP &ndash; Request retract email &ndash; 15/05/2024", 1, "Annexure A Tab 9A"),
  ("38", "Email APP to T Reese &ndash; response &ndash; 15/05/2024", 1, "Annexure A Tab 9A"),
  ("38", "Email T Reese to APP &ndash; confirm retract and follow up &ndash; 21/05/2024", 1, "Annexure A Tab 9B"),
  ("41", "Email HR to T Reese &ndash; Complaint &ndash; 16/05/2024", 2, "partly &ndash; exhibit CS-4 is the Respondent's disclosure of 11 June 2026 of the 15&ndash;16 May correspondence"),
 ]),
 ("Stressor 1(g) &mdash; industrial representation", [
  ("19", "Email Appellant to WorkCover regarding union, 4 attachments", 1, "Annexure A Tab 24; exhibits CS-2, CS-3"),
 ]),
 ("Stressor 2 &mdash; remuneration", [
  ("13, 15", "Emails to WorkCover re pay issues, including the chain of 03 to 13/05/2024", 1, "Annexure A Tabs 12, 13"),
  ("40, 42", "Payroll notices of non-party disclosure", 1, "Annexure A Tab 15"),
  ("23", "Email: Request for review and adjustment of payment &ndash; 08/04/2024 to 23/08/2024", 0, "the full chain not held"),
  ("39", "<b>Email C Taylor to M Pritchard &ndash; validation of claims older than 3 months &ndash; 04/09/24</b>", 0, "not held &mdash; Tab 14 is the 28 May 2024 version"),
 ]),
 ("Stressor 3 &mdash; rostering and fatigue management", [
  ("38", "Email chain APP &amp; T Reese &ndash; roster concerns &ndash; 08/05/24", 1, "Annexure A Tab 7"),
  ("38", "Email chain T Reese to HR &ndash; request assistance &ndash; 10 and 20/05/24", 1, "Annexure A Tabs 8, 8A"),
  ("39", "Texts C Taylor &amp; APP &ndash; public holiday rostering &ndash; 04/04/2023", 1, "List item 8 &ndash; the text messages, with the roster board image of 4 April 2023"),
  ("39", "Email C Taylor to T Reese &ndash; APP urgent leave &ndash; 14/01/2024", 0, "not held"),
  ("43", "Partial non-party disclosure from Metro South Health, with objection", 1, "Annexure A Tab 20"),
  ("&mdash;", "<b>No roster of any kind appears on the Respondent's list</b>", 1, "<b>91 rosters held</b>, PP17 (22 Jan 2024) to PP27 (23 Jun 2024) unbroken"),
  ("&mdash;", "<b>No emergency-code or paging material appears on the Respondent's list</b>", 2, "Annexure A Tab 31 held &mdash; the screen capture only"),
 ]),
 ("Medical", [
  ("7", "Workers' compensation medical certificates, Dr P Hawes, 1 Jul, 11 Aug, 8 Sep 2024", 1, "Tab M2"),
  ("8", "Workers' compensation medical certificate, Dr K Pang, 7 Aug 2024", 1, "Tab M2"),
  ("9", "Email Dr Krishnaiah &ndash; noting injury and medication, 24/10/2024", 1, "Tab M3"),
  ("10", "Report of Mind &amp; Memory Service, 13/02/2025", 1, "Tab M4"),
  ("11", "Practice records, Our Medical Ashmore", 1, "Tab M1"),
  ("&mdash;", "No clinical records of Dr Krishnaiah appear on the Respondent's list", 2, "requested 5 Sep 2026, not yet received &ndash; Tab M6"),
 ]),
 ("Conduct after 18 June 2024", [
  ("&mdash;", "<b>Nothing on the abandonment, the separation date or the reinstatement</b>", 1, "show cause 26/09/2024, confirmation 09/10/2024, replies of 9 and 11/10/2024, Form 12 stamped 25/10/2024"),
  ("17", "Email Employer to WorkCover, letter of 15/08/2024 with 8 attachments", 0, "not held"),
  ("31", "Email Employer to WorkCover, letter of 06/09/2024 with 9 attachments", 0, "not held"),
 ]),
]

INSPECT = [
 ("1", "37", "Photo comms book &ndash; 20/05/2024"),
 ("2", "37", "Email C Taylor to C Jeffrey &ndash; Comms book &ndash; 21/05/2024"),
 ("3", "37", "Email T Reese to C Taylor &ndash; roster and comms with APP &ndash; 07/08/23"),
 ("4", "37", "Email chain C Taylor &amp; APP &ndash; Request discussion on rostering &ndash; 14 to 15/11/23"),
 ("5", "39", "Email C Taylor to A McNamee &ndash; background to request hours &ndash; 17/05/24"),
 ("6", "39", "Email C Taylor to M Pritchard &ndash; validation of claims older than 3 months &ndash; 04/09/24"),
 ("7", "41", "Email HR to T Reese &ndash; Complaint &ndash; 16/05/2024"),
 ("8", "26", "Email: Task change switchboard &ndash; 19/04/2024"),
 ("9", "17, 31", "Employer letters to WorkCover of 15/08/2024 (8 attachments) and 06/09/2024 (9 attachments)"),
]

MARK = {1: ("held", C), 0: ("NOT HELD", CG), 2: ("in part", CB)}


def grid(t, head_bg='#EDEDED'):
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.35, colors.HexColor('#9a9a9a')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(head_bg)),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 3.5), ('RIGHTPADDING', (0, 0), (-1, -1), 3.5),
        ('TOPPADDING', (0, 0), (-1, -1), 2.2), ('BOTTOMPADDING', (0, 0), (-1, -1), 2.2)]))
    return t


story = [
 Paragraph("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION", HD),
 Paragraph("Matter No. WC/2024/227 &nbsp;·&nbsp; Cory Lea Shepherd (Appellant) v Workers' "
           "Compensation Regulator (Respondent)", HD2),
 Paragraph("THE TWO LISTS OF DOCUMENTS, AGAINST THE PLEADING", TT),
 Paragraph(f"Working document &nbsp;·&nbsp; {DATE}", B),
 Paragraph("⛔ NOT FOR SERVICE AND NOT FOR FILING. This is the working paper behind an inspection "
           "request; it is not the request.", WARN),
 Paragraph("The Respondent's amended List of Documents (Form 23) dated 14 August 2026, 52 items, "
           "set against the Amended Statement of Facts and Contentions filed 7 April 2026 and "
           "against the documents the Appellant holds. The Respondent's list is organised by "
           "provenance &mdash; Jurisdictional, Court, Medical Certificates, Medical, Factual, "
           "Insurer File, Miscellaneous &mdash; and not by the pleading.", B),

 Paragraph("1.  The composition of the Respondent's list", PART),
 grid(Table([[Paragraph("&nbsp;", CB), Paragraph("Count", CB)]] +
            [[Paragraph(a, C), Paragraph(b, CB)] for a, b in SHAPE],
            colWidths=[W-26*mm, 26*mm], repeatRows=1)),
 Paragraph("About half of the Respondent's list is material the Appellant himself sent to WorkCover "
           "between July and September 2024. The contemporaneous workplace record it holds came "
           "through witness conferencing with Ms Reese and Ms Taylor in July 2025 and through two "
           "payroll notices of non-party disclosure.", B),
]

story.append(Paragraph("2.  Limb by limb", PART))
for limb, rows in LIMBS:
    data = [[Paragraph("Item", CB), Paragraph("On the Respondent's list", CB),
             Paragraph("Held?", CB), Paragraph("Where, or the position", CB)]]
    for it, desc, st, where in rows:
        lab, style = MARK[st]
        data.append([Paragraph(it, C), Paragraph(desc, C), Paragraph(lab, style),
                     Paragraph(where, C)])
    t = grid(Table(data, colWidths=[13*mm, W-13*mm-16*mm-58*mm, 16*mm, 58*mm], repeatRows=1))
    story.append(KeepTogether([Paragraph(limb, SEC), t]) if len(rows) <= 5
                 else Paragraph(limb, SEC))
    if len(rows) > 5:
        story.append(t)
    story.append(Spacer(1, 1.5*mm))

story += [
 Paragraph("3.  The Respondent's list offers inspection on its face", PART),
 Paragraph("The Form 23 states: <i>&ldquo;You may inspect the documents in the schedule as follows: "
           "Address: 347 Ann Street, Brisbane QLD 4000. Times: Please contact us to make an "
           "appropriate time.&rdquo;</i> Each document below is on the Respondent's own schedule and "
           "is therefore already offered for inspection. No notice and no application is required, "
           "and there is no objection to overcome.", B),
 Paragraph("4.  The inspection list &mdash; nine items, all from the Respondent's own schedule", PART),
 grid(Table([[Paragraph("&nbsp;", CB), Paragraph("Item", CB), Paragraph("Document", CB)]] +
            [[Paragraph(a, CB), Paragraph(b, C), Paragraph(c, C)] for a, b, c in INSPECT],
            colWidths=[9*mm, 15*mm, W-24*mm], repeatRows=1)),
 Paragraph("An inspection request is ordinary correspondence. It does not disturb the request of "
           "9 September 2026, which has its own reply date of Friday 18 September 2026, and the "
           "Respondent's own material falls due on 30 September 2026.", B),
 Spacer(1, 4*mm),
 Paragraph("Prepared " + DATE + " &nbsp;·&nbsp; Cory Lea Shepherd, Appellant, self-represented "
           "&nbsp;·&nbsp; working document", HD),
]


def foot(cv, doc):
    cv.saveState(); cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#666666'))
    cv.drawString(15*mm, 10*mm, f"WC/2024/227 · the two lists of documents against the pleading · working document · {DATE}")
    cv.drawRightString(A4[0]-15*mm, 10*mm, f"Page {cv.getPageNumber()}")
    cv.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm,
                      topMargin=13*mm, bottomMargin=15*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[
    Frame(15*mm, 15*mm, W, A4[1]-28*mm, leftPadding=0, rightPadding=0,
          topPadding=0, bottomPadding=0)], onPage=foot)])
doc.build(story)

p = pikepdf.open(OUT, allow_overwriting_input=True)
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(p.docinfo.keys()): del p.docinfo[k]
for pg in p.pages:
    for k in ('/Metadata', '/PieceInfo', '/Annots'):
        if k in pg.obj: del pg.obj[k]
p.save(OUT + '.tmp', linearize=True); os.replace(OUT + '.tmp', OUT)
chk = pikepdf.open(OUT)
clean = (not dict(chk.docinfo)) and '/Metadata' not in chk.Root
print(f"built {OUT} — {len(chk.pages)} pages, {sum(len(r) for _, r in LIMBS)} mapped rows, "
      f"{'clean' if clean else 'METADATA SURVIVED'}")
if not clean: raise SystemExit("metadata survived")
