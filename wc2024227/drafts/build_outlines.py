#!/usr/bin/env python3
"""WC/2024/227 - Outlines of evidence, direction 2 of the Further Directions Order (3).

⛔ ONE A4 PAGE PER WITNESS (direction 2). Each outline is checked against that limit at
build time and the build FAILS if any runs to two pages.

SERVE on the Respondent by 4.00 pm 9 September 2026. DO NOT FILE in the Industrial Registry.
All metadata stripped.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer

HD   = ParagraphStyle('HD', fontName='Helvetica-Bold', fontSize=8.6, leading=11,
                      textColor=colors.HexColor('#333333'), spaceAfter=1)
HD2  = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=5)
TITLE= ParagraphStyle('TITLE', fontName='Helvetica-Bold', fontSize=11.5, leading=14, spaceAfter=2)
SUB  = ParagraphStyle('SUB', fontName='Helvetica-Oblique', fontSize=7.8, leading=10,
                      textColor=colors.HexColor('#555555'), spaceAfter=5)
INTRO= ParagraphStyle('INTRO', fontName='Helvetica', fontSize=9.2, leading=11.8, spaceAfter=4)
ITEM = ParagraphStyle('ITEM', parent=INTRO, leftIndent=9*mm, firstLineIndent=-9*mm, spaceAfter=3.4)
FOOT = ParagraphStyle('FOOT', parent=SUB, spaceBefore=5)
def P(t, s=INTRO): return Paragraph(t, s)

HEADER = ("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",
          "Matter No. WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' "
          "Compensation Regulator (Respondent)")
SERVED = ("Served pursuant to direction 2 of the Further Directions Order (3) dated 19 August 2026. "
          "Not filed in the Industrial Registry.")
TAIL_W = ("This outline is a summary of the evidence the witness is expected to give. It is not a "
          "statement of the witness and is not signed by the witness.")
TAIL_A = ("This outline states the topics on which the Appellant will give oral evidence. It is not "
          "a statement of evidence and is not verified.")

OUTLINES = [
 ("OUTLINE_00_SHEPHERD", "OUTLINE OF EVIDENCE &ndash; MR CORY LEA SHEPHERD (APPELLANT)", TAIL_A,
  "The Appellant will give evidence of the following.",
  [("Employment.", "Commenced at Logan Hospital Switchboard in [MONTH] 2019; permanent from "
    "3 March 2021; a continuous shift worker; full time from 16 October 2023."),
   ("The role.", "Receiving emergency response notifications and distributing them to the correct "
    "response groups per emergency code procedures, \"strictly adhering to protocols and "
    "timeframes\"; maintaining the contact and paging numbers on which emergency paging depends; "
    "keeping \"call queues to minimum at all times\"; the systems operated concurrently and the "
    "call and emergency-code volume across a shift."),
   ("The database and the contact book.", "That from 18 July 2023 operators could no longer correct "
    "entries; that corrections went to Ms Stibbard or Ms Taylor; that the Contact &amp; Number "
    "Changes book was removed from the operators' room; and what that meant when a number was "
    "wrong, including overnight, at weekends and on public holidays."),
   ("The directives.", "The after-hours on-call arrangement of 15 April 2024, the data-entry "
    "process of 19 April 2024 and the call-routing change of 9 May 2024; that he was not consulted "
    "before any of them; and what each required of him."),
   ("Ms Taylor's presence and hours.", "His observation of when she was and was not present across "
    "2023&ndash;2024; that her office hours were not known to the operators; and his request of "
    "15 May 2024 that she state them to the department."),
   ("What happened at the console.", "What he observed when contact details were wrong &mdash; "
    "calls for emergency responses and for medical teams reaching the wrong destination between "
    "2 and 8 May 2024, and delays to urgent results reaching treating staff &mdash; and what he did "
    "on each occasion."),
   ("The communication book.", "The entry he wrote on or about 6 June 2023 about updating on-call "
    "contact numbers; its removal; and what was said to him afterwards, and in front of whom."),
   ("August&ndash;September 2023.", "The concerns raised in writing on 7 August 2023, the meeting "
    "that followed, and the responses of Ms Taylor and Ms Reese."),
   ("Special pandemic leave, February 2024.", "Being unwell with COVID-19; how many times he "
    "submitted the request and what he attached; the reasons given for each decline; and the "
    "approval given on the same material."),
   ("13 and 15 May 2024.", "That he made a complaint on 13 May 2024, later determined to be a "
    "public interest disclosure (content not set out); that on 15 May 2024 he was directed to "
    "retract the email in which he had asked about office hours; and his knowledge of the email of "
    "9 May 2024 in which Ms Taylor asked another person to confirm her hours."),
   ("Union representation.", "When and to whom he expressed interest in becoming the Switchboard "
    "delegate; what followed; and his endorsement on or about 3 November 2025."),
   ("Pay.", "The public holidays he was not rostered to work between February and April 2024 and "
    "the difference that made to his pay compared with colleagues; the errors Payroll identified "
    "on 3 May 2024; and when they were corrected."),
   ("The rostering pattern.", "That rostering errors affecting his line recurred across successive "
    "roster periods, not once; when he identified them and to whom; and the acknowledgement in "
    "Ms Reese's email of 10 May 2024 of \"a few rostering errors made by Chloe with regards to "
    "Cory's line in past rosters\"."),
   ("17 and 18 March 2024.", "Where he lived and his travel time each way; finishing at 23:00 on "
    "17 March and commencing at 06:00 on 18 March; the rest actually available to him after travel; "
    "the sleep he obtained; performing the duties at paragraph 2 in that condition on 18 March; and "
    "the sick leave taken on 19 March 2024."),
   ("Fatigue &mdash; what he raised, and what was never in place.", "The fatigue and rostering "
    "concerns he raised and when; sending the fatigue toolkit to Ms Taylor for review and receiving "
    "no response; his request of 8 April 2024 and the refusal given on 1 May 2024; and that at no "
    "time before 30 June 2024 was he given fatigue risk management training, or a fatigue or "
    "psychosocial risk assessment of his rostering, or any fatigue management process at the "
    "Switchboard."),
   ("After 18 June 2024.", "Meetings scheduled while he was on certified leave; that his employment "
    "was ended under abandonment provisions while he held current medical certificates; and that he "
    "was subsequently reinstated."),
   ("Onset and effect.", "The symptoms he experienced and when; the effect on his sleep, health and "
    "daily functioning across the period; the onset date of 18 June 2024; attending his general "
    "practitioner and lodging his application on 1 July 2024; and his treatment since. He offers no "
    "clinical or diagnostic opinion."),
   ("Documents.", "He will identify and produce the rosters and payslips for the relevant periods; "
    "his emails and messages with his line manager and the Director; the leave and payroll records "
    "produced by the employer; the role description; and the letter of Metro South Hospital and "
    "Health Service of 5 June 2026 (ref K-LM26/729)."),
  ]),

 ("OUTLINE_01_JEFFREY", "OUTLINE OF EVIDENCE &ndash; MS CAROLYN JEFFREY", TAIL_W,
  "Ms Jeffrey is employed by Metro South Hospital and Health Service as [position] at Logan "
  "Hospital Switchboard. She has worked in that department since [month/year] and worked alongside "
  "the Appellant throughout the period [month/year] to [month/year].",
  [("", "Before Ms Chloe Taylor and Ms Ellen Stibbard came into the Switchboard department, "
    "operators could access and update the database used by the Switchboard directly; a "
    "Communication Book was kept in the operators' room in which staff recorded changes to contact "
    "and paging numbers and matters for handover; and operators made changes to medical contact "
    "numbers as those changes arose."),
   ("", "After Ms Taylor and Ms Stibbard came into the department, four changes were made to the "
    "way the Switchboard operated: the switchboard process was changed; operators' access to the "
    "database was restricted; the Communication Book was removed from the operators' room; and "
    "responsibility for updating contact and paging numbers was taken from operators."),
   ("", "Ms Jeffrey was a recipient of the email sent by Ms Stibbard to the Switchboard team on "
    "18 July 2023, in which Ms Stibbard stated that while she was fixing the database she would be "
    "\"removing everyone's access to the database\", that anyone wanting an entry amended was to "
    "contact her directly, and that a request made after hours would \"have to wait until either "
    "Chloe or myself are back\"."),
   ("", "After access to the database was restricted, operators could not correct an inaccurate "
    "entry themselves and had to wait for Ms Stibbard or Ms Taylor. [Ms Jeffrey to describe the "
    "practical effect she observed on the accuracy of contact and paging numbers.]"),
   ("", "Ms Jeffrey saw the entry that was removed from the Communication Book on or about 6 June "
    "2023. [She will say what the entry said, and that it was written by the Appellant &mdash; to "
    "be confirmed with the witness before service.]"),
   ("", "[Ms Jeffrey to describe what she saw and heard at the time the entry was removed and "
    "immediately afterwards, including anything said by Ms Taylor and by the Appellant.]"),
   ("", "From about [month/year] Ms Jeffrey observed changes in the Appellant at work. "
    "[Observations only &mdash; for example attendance, participation in handover, appearance, "
    "engagement with colleagues. No opinion as to diagnosis or cause.]"),
   ("", "In the period in which Ms Jeffrey worked alongside the Appellant she did not at any time "
    "hear him say anything hostile about Ms Taylor or about any other member of staff."),
   ("", "Ms Jeffrey provided a written statement to WorkCover Queensland on or about 18 July 2024 "
    "and a further statement on or about 1 August 2024, each of which is listed in the Respondent's "
    "amended List of Documents dated 14 August 2026."),
  ]),

 ("OUTLINE_02_HARRISONJONES", "OUTLINE OF EVIDENCE &ndash; MR CORY HARRISON-JONES", TAIL_W,
  "Mr Harrison-Jones was employed at Logan Hospital Switchboard from [month/year] to [month/year] "
  "as [position]. He is no longer employed by Metro South Hospital and Health Service. He worked "
  "alongside the Appellant during that period.",
  [("", "A function of the Switchboard was to hold and maintain accurate contact and paging numbers "
    "for medical staff, including on-call doctors, so that calls and emergency notifications could "
    "be directed to the correct person."),
   ("", "Over a period of approximately three months Mr Harrison-Jones observed the Appellant "
    "working to obtain and record updates to medical doctor contact numbers. The updates for "
    "[ward/unit] were consistently missed on [day of the week]. The Appellant raised this and "
    "continued to seek the updates over that period."),
   ("", "Mr Harrison-Jones was a recipient of the email sent by Ms Stibbard to the Switchboard team "
    "on 18 July 2023 stating that she would be removing everyone's access to the database and that "
    "changes were to be sent to her directly."),
   ("", "After access was restricted, operators could not correct an entry themselves and had to "
    "wait for Ms Stibbard or Ms Taylor to make the change."),
   ("", "On or about [date] Mr Harrison-Jones was present in the Switchboard room at the "
    "commencement of a shift. The Appellant had arrived and was reading the handover. He had not "
    "yet signed on."),
   ("", "Ms Taylor came into the room and asked the Appellant whether he had taken the reminder "
    "out. [Mr Harrison-Jones to describe the sequence &mdash; who spoke first, whether Ms Taylor "
    "spoke while the Appellant was speaking, and what each of them said.]"),
   ("", "Mr Harrison-Jones heard Ms Taylor raise her voice. [He is to describe the manner and "
    "volume, and the Appellant's response, from his own observation.]"),
   ("", "In the period in which Mr Harrison-Jones worked alongside the Appellant he did not at any "
    "time hear him say anything hostile about Ms Taylor or about any other member of staff."),
  ]),

 ("OUTLINE_03_CONAGHAN", "OUTLINE OF EVIDENCE &ndash; MS PATRICIA CONAGHAN", TAIL_W,
  "Ms Conaghan is employed by Metro South Hospital and Health Service as [position] at Logan "
  "Hospital Switchboard. She has worked in that department since [month/year] and worked alongside "
  "the Appellant throughout the period [month/year] to [month/year].",
  [("", "On 7 August 2023 the Appellant wrote to Ms Taylor, Ms Reese, Ms Conaghan and Ms Smith "
    "recording that Ms Conaghan and the Appellant each wished to take on an additional two shifts "
    "per fortnight. Ms Conaghan will confirm that she and the Appellant sought those additional "
    "hours."),
   ("", "Following the changes made to the Switchboard process, urgent pathology results for "
    "clinical staff were delayed in reaching the treating team. [Ms Conaghan to describe what she "
    "observed &mdash; what the process was before, what it became, and the delay that resulted.]"),
   ("", "Between 2 and 8 May 2024 there were occasions on which calls were connected to the wrong "
    "medical team, including calls concerning emergency responses. [Ms Conaghan to describe what "
    "she observed at the console during that period.]"),
   ("", "During that period operators had no means of correcting an incorrect entry in the "
    "directory themselves."),
   ("", "Ms Conaghan was not consulted about the change to after-hours on-call arrangements "
    "notified by Ms Taylor to the Switchboard on 15 April 2024, and was not asked to vote on that "
    "change."),
   ("", "Ms Conaghan was not consulted about, and was not balloted in relation to, changes to the "
    "Switchboard roster before [date]."),
   ("", "[If applicable: Ms Conaghan to describe any changes she observed in the Appellant at work "
    "over the period, limited to her own observation.]"),
   ("", "Ms Conaghan was endorsed as a workplace delegate of Together Queensland on or about "
    "3 November 2025, at the same time as the Appellant and Ms Jeffrey."),
  ]),
]

fails = []
for stem, title, tail, intro, items in OUTLINES:
    s = [P(HEADER[0], HD), P(HEADER[1], HD2), P(title, TITLE), P(SERVED, SUB), P(intro)]
    for i, (lead, body) in enumerate(items, start=1):
        txt = f"<b>{i}.</b>&nbsp;&nbsp;" + (f"<b>{lead}</b> " if lead else "") + body
        s.append(P(txt, ITEM))
    s.append(Spacer(1, 2*mm))
    s.append(P(tail, FOOT))
    buf = io.BytesIO()
    doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=17*mm, rightMargin=17*mm,
                          topMargin=14*mm, bottomMargin=14*mm)
    doc.addPageTemplates([PageTemplate(id='n', frames=[
        Frame(17*mm, 14*mm, A4[0]-34*mm, A4[1]-28*mm, leftPadding=0, rightPadding=0,
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
    out = f"out/{stem}.pdf"
    pdf.save(out, linearize=True)
    flag = "OK" if n == 1 else f"⛔ {n} PAGES - EXCEEDS DIRECTION 2"
    if n != 1: fails.append(stem)
    print(f"built {out} - {len(items)} items, {n} page(s)  {flag}")

if fails:
    raise SystemExit(f"\n⛔ DIRECTION 2 BREACH: {', '.join(fails)} exceed one A4 page. Compress before serving.")
print("\nAll outlines fit one A4 page. SERVE on the Respondent; DO NOT FILE.")
