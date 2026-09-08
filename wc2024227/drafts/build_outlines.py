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
HD2  = ParagraphStyle('HD2', parent=HD, fontName='Helvetica', spaceAfter=3)
TITLE= ParagraphStyle('TITLE', fontName='Helvetica-Bold', fontSize=11.5, leading=14, spaceAfter=2)
SUB  = ParagraphStyle('SUB', fontName='Helvetica-Oblique', fontSize=7.8, leading=10,
                      textColor=colors.HexColor('#555555'), spaceAfter=3)
INTRO= ParagraphStyle('INTRO', fontName='Helvetica', fontSize=8.25, leading=8.85, spaceAfter=1.1)
ITEM = ParagraphStyle('ITEM', parent=INTRO, leftIndent=8.5*mm, firstLineIndent=-8.5*mm, spaceAfter=1.5)
FOOT = ParagraphStyle('FOOT', parent=SUB, spaceBefore=1)
def P(t, s=INTRO): return Paragraph(t, s)

HEADER = ("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",
          "Matter No. WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' "
          "Compensation Regulator (Respondent)")
SERVED = ("Served pursuant to direction 2 of the Further Directions Order (3) dated 19 August 2026. "
          "Not filed in the Industrial Registry.")
TAIL_W = ("This outline is a summary of the evidence the witness is expected to give. It is not a "
          "statement of the witness and is not signed by the witness.")
TAIL_A = ("This outline states the topics on which I will give oral evidence. It is not a statement "
          "of evidence and is not verified.")

OUTLINES = [
 ("OUTLINE_00_SHEPHERD", "OUTLINE OF EVIDENCE &ndash; MR CORY LEA SHEPHERD (APPELLANT)", TAIL_A,
  "I will give evidence of the following. Paragraph references are to the notice to admit facts "
  "served 28 August 2026 (the Notice). The events at topics 2 to 7 are established by the facts admitted on "
  "8 September 2026; my evidence on them is what they were from the console and their effect on me.",
  [("Employment and the role.", "I commenced at Logan Hospital Switchboard on 25 March 2019 as a "
    "casual, became permanent from 3 March 2021 and full time from 16 October 2023, as a continuous "
    "shift worker. The Switchboard is the hospital's communications hub: in a Code Blue or MET call it is the "
    "Switchboard that activates and pages the response team, and an error or delay at the console is an error or "
    "delay in the emergency response. Between 15 and 50 emergency codes go out in 24 hours; some 200 to 300 calls a "
    "shift, many from people distressed, frightened or in crisis; urgent results relayed doctor to doctor; and "
    "complaints from the public, clinicians and staff arrive at the console first, to the operator on duty, and "
    "those my manager did not action came back to me. The standing condition of the role over the period: I was "
    "held responsible for what went wrong anywhere in that system, while the means of correcting it, the directory, "
    "the on-call roster, my own roster and my pay, were held by others. My background: safety advisor on Manus "
    "Island, and earlier a nursing student. "
    "<i>[Notice &para;&para; 1&ndash;16, 26&ndash;48, 182&ndash;223]</i>"),
   ("Sleep and fatigue.", "My sleep on rotating shifts across 2023 and 2024 and the melatonin and "
    "temazepam prescribed on 16 November 2023. The shifts of 17 and 18 March 2024: my travel time each way, "
    "finishing at 23:00 and starting at 06:00, and the rest and sleep actually available; that on the "
    "evening of 17 March I handled a MET call and, four minutes later, a Code Blue to the same bed, then "
    "a further MET call; that 18 March was a Monday day shift, which carries the week's peak call volume "
    "and on which the queue is rarely cleared, and that between 06:00 and 14:00 I handled a Code Grey, "
    "three MET calls and two neonatal MET calls, in that state, while answering that queue of urgent handover, "
    "distressed callers and complaints; and the sick leave of 19 March; that those shifts were not a "
    "staff-initiated swap, the only case in which, by Ms Forrest's email of 7 July 2026, the 8-hour "
    "agreement applied; and that the copy I hold of the roster published for that fortnight, 18 to 31 "
    "March 2024, contains no line for me. That when I raised fatigue, neither my manager nor the Director applied any "
    "fatigue protocol to my roster: no fatigue risk assessment was made, no FRMS register was kept, "
    "and the toolkit at clause 10.4.1 of the Operations Manual, sent to Ms Taylor, had no "
    "response; my request of 8 April 2024 and the refusal of 1 May 2024; and that Metro South has since "
    "stated in writing that the fatigue risk assessment records and register entries requested \"do not "
    "exist\", that FRMS training applied only to clinical staff, and that fatigue management "
    "assessment at the Switchboard began only after 30 June 2024. "
    "<i>[&para;&para; 17&ndash;25, 211&ndash;256, 263&ndash;268]</i>"),
   ("Rostering: lates then earlies.", "The pattern on my roster line of late shifts followed by "
    "early shifts, and of nights, days off, then nights again, raised on 16 April 2024; that rostering errors on my line recurred across successive roster periods; "
    "and Ms Reese's acknowledgement of 10 May 2024 of \"a few "
    "rostering errors made by Chloe with regards to Cory's line in past rosters\"; and that I was not told my roster "
    "proposal would not be considered, and learned of Ms Reese's email of 10 May 2024 saying so only from the "
    "Respondent's disclosure in July 2025. "
    "<i>[&para;&para; 211&ndash;223]</i>"),
   ("Pay and entitlements.", "The public holidays I was not rostered between February and April "
    "2024 and the difference to my pay. The loop: on 8 April 2024 I asked Ms Taylor to review my "
    "pay; on 9 April she directed me to raise the older dates through MyHR payroll enquiries; Payroll "
    "told me the payments had to be processed by my manager, which I relayed to her on 24 April; on "
    "3 May Payroll wrote to her, copying me, to \"submit an AVAC to correct these shifts for each "
    "fortnight\"; when I followed up with Payroll on 10 May, Payroll on 13 May told me to \"speak to "
    "your Line Manager\"; on 21 May she was still \"waiting payroll confirmation\"; on 28 May I was "
    "asked to sign a validation of claims older than three months. That under the payroll process "
    "only my manager could submit the AVAC. The February 2024 special pandemic leave application: "
    "what I attached, the two declines, and the approval on the same material; and the effect on me of going "
    "without those payments over those months. "
    "<i>[&para;&para; 114&ndash;142, 182&ndash;210, 242&ndash;246]</i>"),
   ("The database, the misdirected calls, and what I could not fix.", "That from 18 July 2023 "
    "operators could no longer correct database entries and the Contact &amp; Number Changes book "
    "was removed, so a wrong number waited on Ms Stibbard or Ms Taylor and after hours had to "
    "\"wait until either Chloe or myself are back\"; the directives of 15 April, 19 April and 9 May "
    "2024, and that I was not consulted before any of them. That from 15 April 2024, when Ms Taylor "
    "notified the department that she and Ms Stibbard had placed themselves on after-hours call, "
    "departments and clinicians ringing during my shifts with pager and phone updates asked for "
    "her, and on many occasions neither they nor I could have the update or issue resolved during "
    "the shift. The MASPER Registrar's \"Switchboard issues\" emails to Ms Taylor of 3 May 2024 at "
    "3:06 pm and 8 May at 5:28 pm, nine calls reaching the wrong team, including the MET call team "
    "ringing because \"switchboard could not tell them where VHUB was\"; that her first response came "
    "on 9 May at 9:20 am, five days and eighteen hours after the first, asking Dr Wong for her business "
    "hours because they were \"not provided on the rosters\" and that her phone was \"switched off\"; "
    "and at 10:15 am telling the team of "
    "\"many ongoing issues\" about calls \"transferred to the wrong medical teams\"; the Integrated Respiratory Service writing on 15 and 20 May 2024 that \"we "
    "can not help patients or other clinical staff\"; and that on each occasion the delay built up while the "
    "correction waited on someone else. "
    "<i>[&para;&para; 39&ndash;113]</i>"),
   ("Ms Taylor's hours: the question, the retraction request, and the answer.", "That neither I "
    "nor the department knew her office hours; my email of 15 May 2024 at 1:15 pm asking her to share them; Ms Reese's reply that evening asking me to retract it, which I did; that two days later, on 17 May "
    "2024 at 9:30 am, Ms Taylor sent the whole department an email stating \"Otherwise my hours are from 06:30-14:30\", the very information I "
    "had asked for; and Ms Reese's reply of 21 May 2024 asking me to identify the directives I was "
    "concerned about. "
    "<i>[&para;&para; 70&ndash;88]</i>"),
   ("The complaints, and what followed them.", "The communication book entry of 6 June 2023 and its "
    "removal; my email of 16 June 2023 recording no consultation on major changes; the concerns I raised "
    "on 7 August 2023 and the responses; my complaint of 13 May 2024, later determined to be a public "
    "interest disclosure (content not set out); my interest in becoming the Switchboard union delegate "
    "and what followed; and that, on Metro South's own statements, no safety assessment, investigation or change "
    "of procedure followed any complaint I made "
    "about misdirected calls, directory accuracy or fatigue before 30 June 2024, which is what Dr Hawes "
    "recorded on 1 July 2024 as \"they don't listen to his complaints\". What I said on these matters is "
    "in my emails; I never said anything hostile about Ms Taylor or any other member of staff. "
    "<i>[&para;&para; 143&ndash;181, 266&ndash;267, 287&ndash;294]</i>"),
   ("My health before June 2024.", "That before 18 June 2024 I had never been diagnosed with or "
    "treated for depression. My general practitioner's record of 16 November 2023 notes poor sleep "
    "with shift work, that I could not do shifts without a good sleep, no psychological illness "
    "such as depression or psychosis, and mood good. The ADHD and anxiety noted in my history in "
    "October 2022, and the psychiatrist referral to Dr Amini renewed on 16 May 2024 for which no appointment could "
    "be obtained. "
    "<i>[General-practice records disclosed by the Respondent]</i>"),
   ("Onset, presentation and diagnosis.", "That I last worked a shift on 3 June 2024. My symptoms from about 18 June 2024 and their effect on "
    "sleep, concentration, self-care and relationships, and on my capacity for work, from being "
    "certified unfit from 1 July 2024 to returning on reduced hours and the restrictions recorded in "
    "the Employee Capability Checklist of 3 July 2026. Attending Dr Slawinski "
    "on 28 June 2024, whose note records \"stress at work\" and \"upset by people not following "
    "rules\", and Dr Hawes on 1 July 2024, whose note records \"work stress\", that \"they withhold "
    "pay at times, no overtime- not processed, manipulate his roster- so he works lates then "
    "earlies\". Dr Hawes's certificates of 1 July and 8 September 2024 and his psychiatrist "
    "referral. My first consultation with Dr Krishnaiah on 24 October 2024, on that referral, when I "
    "was told I had major depressive disorder with anxiety state, confirmed by the practice in writing "
    "at 11:45 am that day, my fluoxetine increased and quetiapine added at night; his written report "
    "of 13 February 2025; and my treatment since. The matters at paragraphs 2 to 7 above, and their "
    "effect on me as each occurred and as they accumulated, are the matters I reported to each doctor, as their records show. I offer no clinical or diagnostic opinion."),
   ("After 18 June 2024, and documents.", "Meetings scheduled while I was on certified leave; my "
    "employment ended under abandonment provisions in October 2024 while I held current certificates, "
    "and my later reinstatement; my return on reduced hours and the leave since; that my Queensland "
    "Health email was restricted, so I cannot produce my work emails myself. Documents: rosters and "
    "payslips; my emails and messages with my line manager and the Director; the employer's leave and "
    "payroll records; and Metro South Health's letter of 5 June 2026 (ref K-LM26/729)."),
  ]),

 ("OUTLINE_02_HARRISONJONES", "OUTLINE OF EVIDENCE &ndash; MR CORY HARRISON-JONES", TAIL_W,
  "Mr Harrison-Jones worked at Logan Hospital Switchboard during 2023 as a temporary part-time "
  "operator alongside the Appellant. He is no longer employed by Metro South Hospital and Health "
  "Service. He is expected to give evidence of the following.",
  [("", "That a function of the Switchboard was to hold and maintain accurate contact and paging "
    "numbers for medical staff, including on-call doctors, so that calls and emergency "
    "notifications could be directed to the correct person."),
   ("", "What he observed over a period of approximately three months of the Appellant working to "
    "obtain and record updates to medical contact numbers; the updates that were repeatedly missed; "
    "and that the Appellant raised the matter and continued to seek those updates."),
   ("", "That he was a recipient of the email sent by Ms Stibbard to the Switchboard team on "
    "18 July 2023 stating that she would be removing everyone's access to the database and that "
    "changes were to be sent to her directly."),
   ("", "That after access was restricted operators could not correct an entry themselves and had "
    "to wait for Ms Stibbard or Ms Taylor to make the change."),
   ("", "An occasion on which he was present in the Switchboard room at the commencement of a "
    "shift, when the Appellant had arrived and was reading the handover and had not yet signed on: "
    "what Ms Taylor said to the Appellant about the removal of a reminder, the sequence in which "
    "each of them spoke, and the manner and volume in which it was said, from his own observation."),
   ("", "That he did not at any time hear the Appellant say anything hostile about Ms Taylor or "
    "about any other member of staff."),
  ]),

 ("OUTLINE_03_CONAGHAN", "OUTLINE OF EVIDENCE &ndash; MS PATRICIA CONAGHAN", TAIL_W,
  "Ms Conaghan is an Administration Officer in Switchboard Services at Logan Hospital and has "
  "worked in that department alongside the Appellant. She is expected to give evidence of the "
  "following.",
  [("", "That she and the Appellant each sought an additional two shifts per fortnight, as recorded "
    "in his email of 7 August 2023 to Ms Taylor, Ms Reese, Ms Conaghan and Ms Smith."),
   ("", "What she observed of urgent pathology results for clinical staff being delayed in reaching "
    "the treating team following the changes made to the Switchboard process: what the process was "
    "before, what it became, and the delay that resulted."),
   ("", "What she observed at the console between 2 and 8 May 2024 of calls being connected to the "
    "wrong medical team, including calls concerning emergency responses."),
   ("", "That during that period operators had no means of correcting an incorrect entry in the "
    "directory themselves."),
   ("", "That she was not consulted about the change to after-hours on-call arrangements notified "
    "by Ms Taylor to the Switchboard on 15 April 2024, and was not asked to vote on that change."),
   ("", "That she was not consulted about, and was not balloted in relation to, changes to the "
    "Switchboard roster."),
   ("", "Any change she observed in the Appellant at work over the period, from her own "
    "observation. She offers no opinion as to diagnosis or cause."),
   ("", "That she did not at any time hear the Appellant say anything hostile about Ms Taylor or "
    "about any other member of staff."),
  ]),
]

fails = []
for stem, title, tail, intro, items in OUTLINES:
    s = [P(HEADER[0], HD), P(HEADER[1], HD2), P(title, TITLE), P(SERVED, SUB), P(intro)]
    for i, (lead, body) in enumerate(items, start=1):
        txt = f"<b>{i}.</b>&nbsp;&nbsp;" + (f"<b>{lead}</b> " if lead else "") + body
        s.append(P(txt, ITEM))
    s.append(P(tail, FOOT))
    buf = io.BytesIO()
    doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm,
                          topMargin=11*mm, bottomMargin=11*mm)
    doc.addPageTemplates([PageTemplate(id='n', frames=[
        Frame(15*mm, 8*mm, A4[0]-30*mm, A4[1]-16*mm, leftPadding=0, rightPadding=0,
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
