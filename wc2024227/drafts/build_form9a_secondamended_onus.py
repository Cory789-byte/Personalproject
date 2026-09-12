#!/usr/bin/env python3
"""WC/2024/227 - SECOND AMENDED FORM 9A.

Same architecture as the Amended Form 9A filed 7 April 2026 - Part A, Part B (1 baseline,
2 stressors 1/2/3, 3 subsequent conduct), Part C contentions, Part D orders - with:
  * the role description opening each stressor at the duty it engages;
  * the 303 admitted paragraphs overlaid in blue;
  * red for material not yet admitted or not supported by the notice;
  * ⭐ the onus ACCEPTED as resting on the Appellant (Guide 7.3; Prizeman), not contested.

Facts via served_facts.py - the 303 as served 28 August 2026 and answered 8 September 2026.
⛔ DRAFT. Leave to amend required; not before 30 September 2026, and not less than 7 days
before the hearing (Appeal Guide Part 4.6).
"""
import io, os, pikepdf
SERVE = bool(os.environ.get('SERVE'))
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from served_facts import FACT as F, NOT_ADMITTED, TOTAL
assert TOTAL == 303

BLUE = colors.HexColor('#123f8c'); GREY = colors.HexColor('#6b6b6b'); RED = colors.HexColor('#9b1c1c')
H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=12.5, leading=15, spaceAfter=2)
H2  = ParagraphStyle('H2', fontName='Helvetica', fontSize=8.2, leading=10.2, textColor=GREY, spaceAfter=4)
KEY = ParagraphStyle('KEY', fontName='Helvetica', fontSize=7.5, leading=9.2, spaceAfter=2)
PART= ParagraphStyle('PART', fontName='Helvetica-Bold', fontSize=10.5, leading=13, spaceBefore=9, spaceAfter=3)
SEC = ParagraphStyle('SEC', fontName='Helvetica-Bold', fontSize=9, leading=11.2, spaceBefore=5, spaceAfter=2)
PLD = ParagraphStyle('PLD', fontName='Helvetica', fontSize=8.3, leading=10.4, leftIndent=4*mm, spaceAfter=2)
SUBP= ParagraphStyle('SUBP', parent=PLD, leftIndent=8*mm, spaceAfter=1.5)
ADM = ParagraphStyle('ADM', fontName='Helvetica', fontSize=7.9, leading=9.7, leftIndent=12*mm,
                     textColor=BLUE, spaceAfter=1.1)
DUTY= ParagraphStyle('DUTY', parent=ADM, leftIndent=8*mm, spaceBefore=1)
PEN = ParagraphStyle('PEN', parent=ADM, textColor=RED)
NOTE= ParagraphStyle('NOTE', fontName='Helvetica-Oblique', fontSize=7.6, leading=9.3,
                     leftIndent=8*mm, textColor=RED, spaceAfter=3)
PART_REF = ParagraphStyle('PART_REF', fontName='Helvetica-Oblique', fontSize=7.8, leading=9.6,
                          leftIndent=8*mm, spaceAfter=2.5)
def P(t, s): return Paragraph(t, s)
def _collapse(ns):
    ns = sorted(set(ns)); out=[]; i=0
    while i < len(ns):
        j=i
        while j+1 < len(ns) and ns[j+1]==ns[j]+1: j+=1
        out.append(str(ns[i]) if j==i else f"{ns[i]} to {ns[j]}")
        i=j+1
    return ", ".join(out)
def q(ns, st=ADM):
    if SERVE:
        if not ns: return []
        pend = [n for n in ns if n in NOT_ADMITTED]
        adm  = [n for n in ns if n not in NOT_ADMITTED]
        if not adm:
            return [P("Particulars: paragraphs " + _collapse(pend) +
                      " of the notice to admit facts served 28 August 2026.", PART_REF)]
        txt = "Particulars: paragraphs " + _collapse(adm) + \
              " of the notice to admit facts served 28 August 2026, admitted 8 September 2026."
        if pend:
            txt += " Paragraph" + ("s " if len(pend)>1 else " ") + _collapse(pend) + \
                   " of that notice " + ("are" if len(pend)>1 else "is") + " not admitted."
        return [P(txt, PART_REF)]
    out=[]
    for n in ns:
        stl = PEN if n in NOT_ADMITTED else st
        tag = ' <b>[NOT YET ADMITTED]</b>' if n in NOT_ADMITTED else ''
        out.append(P(f"<b>[{n}]</b> {F[n]}{tag}", stl))
    return out
def duty(ns):
    if SERVE:
        return [P("Duty engaged: paragraphs " + _collapse(ns) + " of that notice (the role description).",
                  PART_REF)]
    return [P("<b>Duty engaged &mdash; the role description states:</b>", DUTY)] + \
           [P(f"<b>[{n}]</b> {F[n]}", DUTY) for n in ns]
_P_orig = P
def P(t, st):
    if SERVE and st is NOTE: return None
    return _P_orig(t, st)

s=[P("SECOND AMENDED STATEMENT OF FACTS AND CONTENTIONS (FORM 9A)" if SERVE else
     "SECOND AMENDED STATEMENT OF FACTS AND CONTENTIONS (FORM 9A) &ndash; DRAFT", H1),
 P("WC/2024/227 &ndash; Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator "
   "(Respondent). Section 550(4), Workers' Compensation and Rehabilitation Act 2003.", H2)]
if SERVE:
    s += [P("Particulars are given by reference to the paragraph numbers of the Appellant's notice to "
            "admit facts served on the Respondent on 28 August 2026, to which the Respondent responded "
            "on 8 September 2026.", KEY)]
else:
    s += [P("<b>Black</b> is pleaded text. <font color='#123f8c'><b>Blue</b> is a paragraph admitted by the "
      "Respondent on 8 September 2026, word for word, with its number on the notice served 28 August "
      "2026. 298 of 303 admitted; five not admitted; none denied. Rule 49, for this proceeding only.</font> "
      "<font color='#9b1c1c'><b>Red is not yet admitted, or not supported by the notice and to be "
      "proved otherwise.</b></font>", KEY),
     P("⛔ <b>DRAFT.</b> Leave required; not before 30 September 2026, and not less than seven days "
      "before the hearing. ⭐ <b>The onus is accepted as resting on the Appellant</b> &mdash; see Part C.1.", KEY)]
s += [
 Spacer(1,2*mm),

 P("PART A", PART),
 P("Appellant: Cory Lea Shepherd. Employer: State of Queensland (Queensland Health) &ndash; Logan "
   "Hospital Switchboard. Role: Administration Officer, Switchboard Services, classification AO3, a "
   "continuous shift working role.", PLD),
 P("<b>Injury:</b> major depressive disorder with anxious distress (DSM-5 296.23), diagnosed by "
   "the Appellant's treating psychiatrist on 24 October 2024.", PLD),
 P("<b>The injury is a diagnosed medical condition arising from the Appellant's employment over "
   "the course of conduct pleaded at Part B.2 below, between approximately June 2023 and June 2024. "
   "It is not pleaded as arising from an event occurring on a single day.</b> The date of injury "
   "recorded on the work capacity certificates of the treating general practitioner is 18 June 2024. "
   "That date is the practitioner's and is a matter for the medical evidence; the Appellant asserts "
   "no date of onset of his own.", PLD)]
s += q([1,2,3,4,13,14,15,16])

s += [P("PART B &mdash; MATERIAL FACTS", PART),
 P("The documentary facts identified below have been admitted to the extent recorded in the "
   "Respondent's response of 8 September 2026. Those admissions provide evidence from which the "
   "Commission is invited to determine the nature, reasonableness and causal significance of the "
   "relevant circumstances.", PLD),
 P("<b>1. &nbsp;Baseline &mdash; the medical record</b>", SEC),
 P("1.1 &nbsp;The Switchboard receives emergency response notifications and distributes them to the "
   "response groups by category of emergency, and maintains the contact and paging information by "
   "which that is done.", PLD)]
s += duty([8,7,5,10])
s += [P("[⚠ THE MEDICAL IS NOT IN THE NOTICE &mdash; <b>no paragraph of the 303 refers to any medical "
   "record, practitioner, referral, certificate or diagnosis.</b> Everything at 1.2 to 1.10 is proved "
   "from the schedule of medical documents served 9 September 2026 (Tabs M1 to M9) and, as to clinical "
   "opinion, by the oral evidence of its author (Appeal Guide 7.6.5). The pinpoints carried in the "
   "Amended Form 9A of 7 April 2026 (\"Form 24, Para 34/36/38/39\") refer to the SUPERSEDED notice of "
   "February 2026 and must not be carried forward.]", NOTE),

 P("1.2 &nbsp;<b>Prior health.</b> Before 18 June 2024 the Appellant had not been diagnosed with or "
   "treated for depression. The general-practice record of 16 November 2023 (Dr Nanayakkara) records "
   "poor sleep with shift work, that the Appellant could not do shifts without a good sleep, "
   "\"no psychological illness such as depression or psychosis\", and mood good, with melatonin and "
   "temazepam prescribed that day. <b>[Tab M1 &mdash; general-practice records, Our Medical Ashmore, "
   "1 January 2023 to 1 July 2024, obtained by the Respondent under the Form 29 signed 4 July 2025; "
   "Respondent\'s item 11.]</b> Relied upon as the contemporaneous record that shift work was affecting "
   "the Appellant\'s sleep, and of what was prescribed for it, before any claim or proceeding. Its "
   "clinical significance is a matter for the treating doctors. Private entries unrelated to the injury "
   "are redacted on the extracted pages and marked as such.", SUBP)]
s += q([2,13,214,218] + list(range(263,266)) + list(range(269,272)))

s += [P("1.3 &nbsp;<b>The referral of 16 May 2024.</b> The referral letter of 16 May 2024 (Dr Zhao) "
   "renews a referral to a psychiatrist, Dr Amini, for \"ongoing care and management\". It lists the "
   "past medical history as the history-list items \"26/10/2022 ADHD\" and \"26/10/2022 Anxiety\", and "
   "lists the medications then current, <b>which include no antidepressant, no anxiolytic and no other "
   "psychotropic medication</b>. <b>[Tab M1.]</b> It was written the day after the email of "
   "15 May 2024 at 6:23 pm asking the Appellant to retract his email of that afternoon. That sequence "
   "is pleaded as to date only; no connection between the two is alleged. No appointment with the "
   "psychiatrist was obtained on that referral.", SUBP)]
s += q([76,77])

s += [P("1.4 &nbsp;<b>Deterioration and first presentation.</b> The Appellant last worked a shift "
   "on 3 June 2024. On days in May 2024 and in the first week of June 2024 he drove to work, was "
   "unable to enter the building, and reported himself unfit from the car park. The date of injury "
   "recorded on the certificates is 18 June 2024. On 28 June 2024 (Dr Slawinski) the record shows \"stress at work\" and "
   "\"upset by people not following rules\", reason for visit anxiety. On 1 July 2024 (Dr Hawes) the "
   "record shows \"work stress\", \"been there 5 years\", that \"they withhold pay at times, no "
   "overtime- not processed, manipulate his roster- so he works lates then earlies\", and \"causing "
   "anxiety\". <b>[Tab M1.]</b> The events those records name are the matters admitted on "
   "8 September 2026 and pleaded at Part B.2 below. The records are relied upon as the contemporaneous "
   "record of what was reported, before any claim decision, dismissal or proceeding; not as a finding "
   "of fact as to mechanism.", SUBP),

 P("1.5 &nbsp;<b>Certification.</b> The work capacity certificates of Dr Hawes dated 1 July, "
   "11 August and 8 September 2024, and of Dr Ki Pang dated 7 August 2024, state the date of injury as "
   "18 June 2024, that the Appellant was first seen for this injury on 1 July 2024, and certify no "
   "functional capacity continuously from 1 July to 6 October 2024. The referral to a psychiatrist is "
   "recorded on the certificate of 8 September 2024. Review Decision 69983 records at page 17 that the "
   "certificate of 1 July 2024 indicated \"there was no pre-existing factor or condition\", and that "
   "\"This was maintained in all later work capacity certificates\". <b>[Tab M2; Respondent\'s items 7 "
   "and 8.]</b> The medication box is unticked on each certificate.", SUBP),

 P("1.6 &nbsp;<b>Diagnosis, 24 October 2024.</b> At the first consultation, on the referral, the "
   "treating psychiatrist told the Appellant, and confirmed in writing at 11:45 am that day, that he "
   "was \"suffering from psychological injury of Major Depressive Disorder with anxiety state\"; that "
   "fluoxetine was increased to two capsules \"from today\" and Seroquel 25 mg commenced at night, "
   "\"to restore basic needs- sleep, eating and routine\". The Appellant\'s email of 5:12 pm that day "
   "reads \"I have finally been able to see a psychiatrist today\". <b>[Tab M3; Respondent\'s item 9.]</b> "
   "Read with 1.5, it records the progression from the injury certified as anxiety and stress on "
   "1 July 2024 to a depressive disorder by 24 October 2024.", SUBP),

 P("1.7 &nbsp;<b>The report of 13 February 2025.</b> Diagnosis: Major Depressive Disorder with "
   "anxious distress (DSM-5 296.23). Severity, functional effect and treatment (fluoxetine increased to "
   "three capsules daily; quetiapine 25 mg at night). The treating clinician records the origin as "
   "\"workplace stress stemming from issues with management and rostering\"; that the issues \"began "
   "approximately one year ago when a new manager was appointed\"; that pay was \"withheld or delayed "
   "for up to five months at a time, leading to significant financial stress\"; and that \"premature "
   "exposure to the workplace is more likely result in significant deterioration\". <b>[Tab M4; "
   "Respondent\'s item 10.]</b> The stressors so recorded correspond to matters admitted on 8 September "
   "2026: management and rostering, and the night-shift line; the shorter break; and pay withheld or "
   "delayed from the 5 February 2024 fortnight, uncorrected at 13 May, \"claims older than 3 months\" on "
   "28 May, a claim effective 30 March recorded \"Part Completed\" on 30 May, and the two February "
   "claims absent from the myHR report.", SUBP)]
s += q([211,212,220,258,259,260,193,196,197,203,210])
s += [P("1.8 &nbsp;<b>The report\'s footer, and the author\'s position.</b> The report bears a footer "
   "reading \"for the only reason of clinical information and not for medico-legal use\". The author\'s "
   "emails of 5 and 8 September 2026 state of his records \"You can use them according to the need to "
   "support your legal issues\", and identify the report of 13 February 2025 as \"the report that "
   "captures the relevant information you have requested\" on the matters in issue. <b>[Tab M5.]</b> The "
   "report is not relied upon for attribution among the individual events pleaded at Part B.2, nor for "
   "any matter after 24 October 2024 as a cause of the injury.", SUBP),

 P("1.9 &nbsp;<b>Current capacity.</b> The Employee Capability Checklist completed by Dr Day Hong Ma "
   "on 3 July 2026 records current capacity and restrictions and the continuing effect of the injury, "
   "including \"symptom exacerbation on exposure to the identified workplace stressors\". <b>[Tab M6.]</b> "
   "Relied upon for effect and capacity only, not for causation; it post-dates 1 July 2024.", SUBP),

 P("1.10 &nbsp;<b>Outstanding, and the finding in the decision under appeal.</b> The clinical records "
   "of the treating psychiatrist from 24 October 2024 were offered by the practice on 5 September 2026 "
   "and have been requested; they are not yet received and will be served on receipt. On the medical "
   "evidence then before it, the Respondent\'s review of 24 October 2024 found that the Appellant "
   "\"sustained a personal injury of a psychological nature\" and stated: \"Having regard to the medical "
   "evidence, I am satisfied your employment was <b>a significant contributing factor</b> to the "
   "psychological injury\". The claim was rejected under section 32(5), not section 32(1). "
   "<b>[Tabs M7 and M9.]</b> The hearing is de novo and that finding does not bind the Commission; it is "
   "relied upon as an admitted document.", SUBP)]
s += q([261,262])

import form9a_content as C

def cite(ns):
    if not ns: return ""
    pend=[n for n in ns if n in NOT_ADMITTED]; adm=[n for n in ns if n not in NOT_ADMITTED]
    parts=[]
    if adm:  parts.append(("&para;&para; " if len(adm)>1 else "&para; ") + _collapse(adm))
    if pend: parts.append(("&para;&para; " if len(pend)>1 else "&para; ") + _collapse(pend) + " not admitted")
    col = '#9b1c1c' if (pend and not adm) else '#123f8c'
    return f" <font size=\"6.4\" color=\"{col}\">[{'; '.join(parts)}]</font>"

def render(stressor, title):
    out=[P(f"<b>{title}</b>", SEC)]
    for letter, heading, dfacts, items in stressor:
        if dfacts and not SERVE:
            out += [P(f"<b>({letter}) &nbsp;{heading}</b>", SUBP)] + duty(dfacts)
            first_done = True
        else:
            first_done = False
        for sent, fs in items:
            lead = "" if first_done else f"<b>({letter}) &nbsp;{heading}.</b> "
            out.append(P(lead + sent + cite(fs), SUBP))
            first_done = True
            if not SERVE and fs:
                out += q(fs)
    return out

s += [P("<b>2. &nbsp;Causative stressors (composite course, June 2023 &ndash; June 2024)</b>", SEC)]
s += render(C.S1, "STRESSOR 1 &mdash; THE CONDITIONS IN WHICH THE WORK WAS CARRIED ON")
s += [P("[⚠ NOT IN THE NOTICE &mdash; none of the 303 paragraphs refers to the Ethical Standards Unit, "
   "a public interest disclosure, or a complaint of 13 May 2024. Stressor 1(n) is to be proved from "
   "the Unit's determination and the Respondent's response of 18 February 2026 at Annexure A, Tab 27, "
   "or carried into a further notice to admit.]", NOTE)]
s += render(C.S2, "STRESSOR 2 &mdash; REMUNERATION")
s += render(C.S3, "STRESSOR 3 &mdash; THE ROSTER AND FATIGUE")
s += [P("[⚠ NOT ADMITTED &mdash; the distance, the travel time, the four hours of sleep and the "
   "sixteen hours of wakefulness at Stressor 3(e) are the Appellant's own evidence and are not the "
   "subject of any paragraph of the notice; paragraph 251 admits only that the review decision "
   "records his submission of 9 August 2024 in those terms. The 2024 Emergency Code Register at "
   "Stressor 3(h) was produced at Tab 31; production was requested on 9 September 2026 and the reply "
   "of 10 September 2026 seeks until 25 September 2026.]", NOTE)]


s += [P("<b>3. &nbsp;Subsequent conduct, and the contemporaneous record</b>", SEC),
 P("<b>3.1 &nbsp;Conduct after the injury.</b> Meetings were scheduled while the Appellant held "
   "current medical certificates. His employment was ended under abandonment provisions in "
   "October 2024 while those certificates were current, and he was reinstated to his employment with "
   "an effective date of 20 September 2024, the reinstatement taking effect despite any payroll "
   "documentation. These matters are pleaded as context only, in accordance with Stressor 1(q) above.", SUBP),
 P("<b>3.2 &nbsp;What the Appellant provided to WorkCover Queensland, and when.</b> The Respondent's "
   "amended List of Documents of 14 August 2026 records that the Appellant provided to WorkCover "
   "Queensland, at item 12, an email of 12 July 2024 with an attachment described as \"Event overview "
   "- undated\"; at item 14, an email of 18 July 2024 with an attachment described as \"Witness "
   "statement - Carolyn Jeffrey\"; at item 25, an email of 29 August 2024 described as regarding the "
   "after hours on call change, with an attachment described as \"Email: After hours on call "
   "process\"; at item 26, an email of 30 August 2024 described as regarding failure to consult, with "
   "an attachment described as \"Email: Task change switchboard - 19/04/2024\"; and at item 27, an "
   "email of 30 August 2024 described as regarding failure to consult, with an attachment described "
   "as \"Email: MASPER process - 09/05/2024\". It further records, at item 16, an email from "
   "Ms Carolyn Jeffrey to WorkCover Queensland of 1 August 2024 described as a follow up statement. "
   "The documents at items 25, 26 and 27 are the three directives pleaded at Stressor 1(e) and Stressor 1(g) above. "
   "They were provided by the Appellant to WorkCover Queensland in August 2024, before any decision "
   "on his claim and more than two years before this pleading.", SUBP),
 P("<b>3.3 &nbsp;The particulars bundle of 11 August 2026.</b> The Respondent's amended statement of "
   "facts and contentions states at paragraph 11 that it does not admit the allegations in Stressor "
   "1(a) of the Appellant's statement \"because there are no particulars or details to respond to\". "
   "On 11 August 2026 the Appellant served a bundle titled \"Stressor 1(a) - Particulars support "
   "bundle\", comprising 30 pages and six tabs, each stating a particular of that stressor and "
   "enclosing the documents recording it.", SUBP)]
s += q(list(range(274,283)))

s += [P("<b>4. &nbsp;The intervals</b>", SEC),
 P("The following intervals are computed from dates and times admitted by the Respondent. They are "
   "matters of arithmetic and do not depend on the truth of any statement recorded in a document.", PLD),
 P("<b>4.1</b> &nbsp;Between the MASPER Registrar's first report of 3 May 2024 at 3:06 pm and the "
   "first reply of 9 May 2024 at 9:20 am: <b>five days, eighteen hours and fourteen minutes</b>. Her "
   "second report was sent on the fifth calendar day after the first; the reply was sent on the sixth.", SUBP),
 P("<b>4.2</b> &nbsp;Between the first email of the Integrated Respiratory Service of 15 May 2024 at "
   "11:47 am and its second of 20 May 2024 at 11:03 am: <b>the fifth calendar day</b>. Between that "
   "first email and the Appellant's escalation of 20 May 2024 at 2:05 pm: <b>five days, two hours and "
   "eighteen minutes</b>. Between the Service's second email and that escalation: <b>three hours and "
   "two minutes</b>. Between the escalation and the reply at 4:30 pm: <b>two hours and twenty-five "
   "minutes</b>, that reply being sent two hours after the conclusion of the office hours stated to "
   "all Switchboard staff on 17 May 2024.", SUBP),
 P("<b>4.3</b> &nbsp;Between the Appellant's fatigue enquiry of 8 April 2024 and the response of "
   "1 May 2024: <b>23 days</b>, during which the Respondent does not allege that any response was "
   "made.", SUBP),
 P("<b>4.4</b> &nbsp;Between the third submission of the special pandemic leave request at 11:07:28 "
   "on 29 February 2024 and its approval at 11:21:03 the same morning: <b>thirteen minutes and "
   "thirty-five seconds</b>. Between the creation of the draft on 20 February 2024 and the final "
   "approval on 1 March 2024: <b>ten days, four hours, forty minutes and twenty seconds</b>.", SUBP),
 P("<b>4.5</b> &nbsp;Between the removal of database access on 18 July 2023 and 18 June 2024: "
   "<b>eleven months</b>, during which the Respondent does not allege that access was restored. "
   "Between 23 August 2023 and 17 May 2024: <b>nine months</b>, during which the Respondent does not "
   "allege that fixed office hours were stated to the Switchboard staff.", SUBP)]
s += q([62,63,64,92,97,98,102,103,124,125,249])

s += [P("<b>5. &nbsp;Matters the Respondent does not allege, and documents it does not list</b>", SEC),
 P("The following are admitted as to the state of the Respondent's amended statement of facts and "
   "contentions of 13 May 2026 and its amended List of Documents of 14 August 2026. They are not "
   "admissions as to the truth of the contents of any document, and the qualification in the "
   "Respondent's letter of 8 September 2026 does not reach them.", PLD),
 P("<b>5.1 &nbsp;As to the directory and the changes to process.</b> That access to the database was "
   "restored to the Appellant before 18 June 2024; that any document records consultation with "
   "Switchboard operators before the change communicated on 15 April 2024; that agreement under "
   "clause 6.2 of the Award was obtained, or a ballot conducted, before that change.", SUBP),
 P("<b>5.2 &nbsp;As to what followed the reports at the console.</b> That any communication was sent "
   "to Logan Switch or the Switchboard staff about the occasions reported on 3 and 8 May 2024 before "
   "10:15 am on 9 May 2024; that any response was made to the Integrated Respiratory Service before "
   "20 May 2024, or before 2:05 pm on that day; that any document created on 20 May 2024 records the "
   "discussion referred to in the reply of that afternoon; that any communication was sent by either "
   "named person to that Service on that day; that the contact-details document was amended on or "
   "before 20 May 2024; that the Switchboard staff were notified of the modifications made to it on "
   "22 February 2024; or that the Appellant was rostered to work after 2:05 pm on 20 May 2024.", SUBP),
 P("<b>5.3 &nbsp;As to the office hours.</b> That fixed office hours were stated to the Switchboard "
   "staff at any time between 23 August 2023 and 17 May 2024.", SUBP),
 P("<b>5.4 &nbsp;As to the Communication Book.</b> That the entry removed, or its author, is "
   "identified; that the removed page has been located or that any copy of it exists; that any entry "
   "made by the Appellant remains in the book; or that the book ceased to be in the possession of "
   "Metro South Health during the Appellant's employment. The book, and any page or entry from it, is "
   "not listed in the List of Documents.", SUBP),
 P("<b>5.5 &nbsp;As to the special pandemic leave.</b> That either person recorded in the leave "
   "history was a Band 9 delegate at any relevant time; the identity of the person who exercised the "
   "sub-delegated power in respect of Process Reference 15480560; or that any other Switchboard "
   "employee was required to submit such a request personally through myHR in February 2024.", SUBP),
 P("<b>5.6 &nbsp;As to the roster and fatigue.</b> That the Switchboard Manager got in touch with the "
   "Appellant about alternative shifts after the meeting of 16 April 2024; that the fatigue toolkit "
   "was reviewed or feedback given before 18 June 2024; that the consecutive shifts of 17 and "
   "18 March 2024 arose from a staff-initiated shift swap; that any response was made to the fatigue "
   "enquiry between 9 April and 1 May 2024; that any fatigue risk assessment was conducted, that any "
   "fatigue risk management training was provided, or that fatigue risk management assessment was "
   "implemented at the Switchboard, before 30 June 2024; or that any change was made to the operating "
   "procedures of the Switchboard as a consequence of any employee complaint over the period "
   "1 December 2023 to 30 June 2024.", SUBP),
 P("<b>5.7 &nbsp;As to the Appellant's performance and conduct.</b> That he was subject to any "
   "disciplinary process, or that his work performance was the subject of any formal performance "
   "management process, before 18 June 2024; nor does the Respondent describe any communication with "
   "him before that date as a warning. Paragraph 27 of its statement of facts and contentions does "
   "not identify, by particular, date, document or cross-reference, the management action relied upon "
   "for the contention in that paragraph.", SUBP)]
s += q([16,21,22,25,55,69,73,90,93,99,105,106,107,108,109,110,129,130,131,142,150,151,152,153,154,166,180,181,213,216,234,250,269,270,271,272,273,300,301,302,303])


s += [P("PART C &mdash; CONTENTIONS", PART),
 P("<b>1. &nbsp;⭐ The onus, accepted.</b> The Appellant accepts that he bears the onus of proving "
   "every element of his case on the balance of probabilities, including that his injury did not "
   "arise out of, or in the course of, reasonable management action taken in a reasonable way "
   "(Workers' Compensation Appeal Guide, Part 7.3; <i>Prizeman v Q-COMP</i> [2005] ICQ 43, where "
   "Hall P held that the onus is on the worker to establish that management action was unreasonable "
   "or taken in an unreasonable way, and that in the absence of evidence to support that assertion "
   "management action must be considered reasonable). The Appellant does not contend that the "
   "Respondent bears that onus, and the contrary contention in the Amended Form 9A filed 7 April 2026 "
   "is withdrawn.", PLD),
 P("<b>2. &nbsp;How the onus is discharged.</b> <i>Prizeman</i> presumes reasonableness only in the "
   "absence of evidence. The evidence is now on the record and is not in dispute. In particular the "
   "Respondent admits, as to its own documents and its own pleading: that access to the database was "
   "removed and is not alleged to have been restored before 18 June 2024; that no document recording "
   "consultation with Switchboard operators before the change of 15 April 2024 is listed; that nine "
   "occasions of misdirected calls were reported by a clinician and nothing is alleged to have been "
   "sent to the Switchboard about them for six days; that no document of the discussion of 20 May "
   "2024, no communication to the Integrated Respiratory Service, and no amendment to the "
   "contact-details document is listed; that the fatigue records do not exist, that the training "
   "applied only to health practitioners and clinical assistants, that fatigue assessment at the "
   "Switchboard began only after 30 June 2024, and that there were no consequential changes to "
   "operating procedures; and that complaints were managed solely by email or verbally with the "
   "complainant.", PLD),
 P("<b>3. &nbsp;Compensable injury &mdash; section 32(1).</b> The Appellant sustained a personal "
   "injury of a psychological nature arising out of, or in the course of, his employment, employment "
   "being <b>a significant contributing factor</b>. The injury is the diagnosed condition identified at "
   "Part A, arising from the course of conduct pleaded at Part B.2 and not from an event on a single "
   "day. The Respondent's own review decision so finds.", PLD),
 P("<b>4. &nbsp;Section 32(5)(a), first limb &mdash; circumstances that are not management "
   "action.</b> The following circumstances pleaded in Stressor 1 are not action taken by or on "
   "behalf of the employer against the worker. They are the state in which the work was required to "
   "be performed: (i) the position was required to keep the contact and paging information accurate "
   "while the means of amending it was held by others (Stressor 1(a) to (c)); (ii) emergency response "
   "notifications reached the wrong medical team on nine occasions reported by a clinician, and the "
   "Switchboard was not told of them for six days (Stressor 1(g)); (iii) a clinical service was unable to "
   "assist patients or other clinical staff because a directory entry was wrong, and the entry is not "
   "alleged to have been amended (Stressor 1(h)); and (iv) complaints arriving at the console were, on the "
   "employer's own statement, managed solely by email or verbally with the complainant, with no "
   "consequential change to operating procedures (Stressor 1(p)). One decision was taken, on 18 July 2023, "
   "for a stated project reason. What followed is the condition of the system, and the exclusion in "
   "subsection (5) does not reach it.", PLD),
 P("<b>5. &nbsp;Section 32(5)(a), second limb &mdash; where the circumstances are management action, "
   "it was not taken in a reasonable way.</b> If and to the extent that the following are management "
   "action: (i) the change notified on 15 April 2024 was effective the day it was notified, with no "
   "document of prior consultation, against clause 3.2 of the certified agreement, which requires "
   "contribution to decision-making not only in appearance but in fact and a genuine opportunity to "
   "influence the outcome before a final decision is made (Stressor 1(e), Stressor 1(f)); (ii) the remuneration "
   "correction was returned across four fortnights to the only person able to submit it, and the "
   "claim submitted on 28 May 2024 remains recorded as Part Completed, while neither claim reference "
   "identified by Payroll appears in the report at all (Stressor 2(c) to (e)); (iii) the special pandemic "
   "leave application was declined twice on reasons which do not correspond, the second of which the "
   "Respondent concedes was wrong on its own review (Stressor 1(l)); (iv) the fatigue enquiry of 8 April 2024 "
   "drew no response for 23 days (Stressor 3(j)); and (v) the Appellant's roster was decided upon and the "
   "decision expressly withheld from him (Stressor 3(b)). The intervals at Part B.4 and the matters at Part "
   "B.5 are relied upon.", PLD),

 P("<b>6. &nbsp;<i>Delaney</i>.</b> Where multiple management actions form a course of conduct, "
   "their reasonableness may be evaluated in context and as a whole. That evaluation must "
   "nevertheless first identify the circumstances that constitute management action. Operational "
   "conditions that are not management action do not become management action merely because they "
   "occurred alongside management decisions.", PLD),
 P("<b>7. &nbsp;<i>Mahaffey</i>.</b> The presence of reasonable management action among the "
   "circumstances contributing to an injury does not necessarily enliven the exclusion where an "
   "unreasonable management action, or a circumstance that is not management action, also had a "
   "sufficient causal connection to the disorder. The rostering of the shifts on 17 and 18 March "
   "2024 was found in the review decision to constitute unreasonable management action. The "
   "Appellant relies upon the medical and contemporaneous evidence to establish its contribution as "
   "part of the pleaded course of causative circumstances.", PLD),
 P("<b>8. &nbsp;The effect of the admissions.</b> The admissions are made for this proceeding "
   "under rule 49 and are relied upon as evidence of the existence and terms of the documents "
   "admitted, and of the matters the Respondent's statement of facts and contentions and List of "
   "Documents do not contain. The Appellant does not contend that any admission determines the "
   "reasonableness of any conduct; that is a matter for the Commission.", PLD),
 P("<b>9. &nbsp;The hearing de novo.</b> The Respondent says no finding in Review Decision 69983 "
   "binds the Commission. That is accepted, and it applies to the whole of the decision. The "
   "conclusion under appeal is a conclusion of that decision, reached upon the findings recorded in "
   "it.", PLD),
 P("<b>10. &nbsp;The Respondent's pleaded case.</b> Paragraph 27 of the amended statement of facts "
   "and contentions does not identify, by particular, date, document or cross-reference, the "
   "management action relied upon. No disciplinary process, formal performance management or "
   "communication described as a warning before 18 June 2024 is alleged.", PLD)]
s += q([238,295,300,301,302,303])

s += [P("PART D &mdash; ORDERS SOUGHT", PART),
 P("1. The appeal be allowed. 2. The decision of the Respondent dated 24 October 2024 be set aside. "
   "3. It be declared that the Appellant sustained an injury within the meaning of section 32 of the "
   "Workers' Compensation and Rehabilitation Act 2003. 4. The Appellant's application for "
   "compensation be accepted. 5. Costs reserved.", PLD)]

s = [x for x in s if x is not None]
buf=io.BytesIO()
doc=BaseDocTemplate(buf,pagesize=A4,leftMargin=16*mm,rightMargin=16*mm,topMargin=12*mm,bottomMargin=12*mm)
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(15*mm,11*mm,A4[0]-30*mm,A4[1]-23*mm,
    leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)])])
doc.build(s); buf.seek(0)
pdf=pikepdf.open(buf); n=len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out = ("out/FORM9A_SECOND_AMENDED_FOR_FILING.pdf" if SERVE else
       "INTERNAL/2026-09-12_FORM9A_SECOND_AMENDED_original_architecture_onus_accepted.pdf")
pdf.save(out,linearize=True)
print(f"built {out} - {n} page(s)")
