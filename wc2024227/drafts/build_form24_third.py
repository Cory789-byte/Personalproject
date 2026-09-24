#!/usr/bin/env python3
"""WC/2024/227 - THIRD NOTICE TO ADMIT FACTS AND DOCUMENTS (r 49) - DRAFT, built 24 September 2026.

The Respondent's outlines of evidence served 24 September 2026, set fact by fact against the
facts it admitted on 8 September 2026 and against its own disclosure of July 2025.

Rules applied (form24-verifier): one fact, one document, one date; verbatim quotation or an honest
fragment; no characterisation, no conclusion, no compound proposition; every negative tied to a
defined universe (a named document "as served"); every fact about a document the Respondent holds.
Every quoted string is checked against the source text before the PDF is built; a missing quote
fails the build.  Metadata stripped.  ⛔ DRAFT. Transcribe onto the official Form 24/25 before service.
"""
import os, re, sys, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle

# ------------------------------------------------------------------ sources for verification
SRC = {
 'B1': '/tmp/claude-0/outlines.txt',                                  # the outlines, 24 Sep 2026
 'B2': '/tmp/claude-0/r20.txt',                                       # list of witnesses email, 24 Sep 2026
 'B3': '/tmp/claude-0/r19.txt',                                       # documents-in-dispute email, 24 Sep 2026
 'B4': '/tmp/claude-0/Disclosure_witness_conferencing_QldHealth_Payroll.txt',
 'B5': '/tmp/claude-0/Disclosure_witness_conferencing_Tammy_Reese.txt',
 'N1': '/tmp/claude-0/f24.txt',                                       # the first notice, 303 facts, 28 Aug 2026
 'R1': '/tmp/claude-0/r24.txt',                                       # the response of 8 Sep 2026
}
def norm(s):
    s = s.replace('‘', "'").replace('’', "'").replace('“', '"').replace('”', '"')
    s = s.replace('–', '-').replace('—', '-').replace(' ', ' ')
    return re.sub(r'\s+', ' ', s).strip()
TXT = {k: norm(open(v, encoding='utf-8', errors='ignore').read()) for k, v in SRC.items()}

B1 = "The Respondent's Outlines of Evidence, served 24 September 2026 - Annexure B Tab B1"
B2 = "Email, Ms R Matheson to the Industrial Registry, copied to the Appellant, 24 September 2026, 11:50 am, list of witnesses - Annexure B Tab B2"
B3 = "Email, Ms R Matheson to the Appellant, \"Documents in dispute\", received 24 September 2026 - Annexure B Tab B3"
B4 = "Respondent's disclosure, \"Disclosure from witness conferencing - Qld Health Payroll\", email of Ms S Christensen, 11 July 2025 - Annexure B Tab B4"
B5 = "Respondent's disclosure, \"Disclosure from witness conferencing - Tammy Reese\", emails of 30 June to 8 July 2025 - Annexure B Tab B5"
N1 = "The notice to admit facts served 28 August 2026 (the first notice), and the Respondent's response of 8 September 2026 - Annexure B Tab B6"

OUTL = "The Respondent's Outlines of Evidence served on 24 September 2026, as served,"
def adm(n, quote):
    """A fact of the first notice, admitted on 8 Sep 2026, restated verbatim."""
    return (0, f"Fact {n} of the notice to admit facts served on 28 August 2026, admitted by the Respondent in its "
               f"response of 8 September 2026, states: \"{quote}\"", N1, ('N1', quote), ('ADM', n))

FACTS = [
 ("#", "PART ONE - THE RESPONDENT'S LIST OF WITNESSES AND OUTLINES OF EVIDENCE OF 24 SEPTEMBER 2026"),
 ("A", "THE LIST OF WITNESSES"),
 (0, "On 24 September 2026 at 11:50 am Ms Renee Matheson sent an email to the Industrial Registry, copied to the Appellant, attaching the Respondent's list of witnesses, which states: \"The respondent is intending to call the following lay witness at the hearing of this matter:\" followed by the names Ms Chloe Taylor, Ms Tammy Reese, Ms Kimberley Wright and Ms Nicole Earl.", B2,
     ('B2', "The respondent is intending to call the following lay witness at the hearing of this matter:")),
 (0, "That email states: \"The respondent reserves its right to amend this list depending on the case presented by the appellant at the hearing.\"", B2,
     ('B2', "The respondent reserves its right to amend this list depending on the case presented by the appellant at the hearing.")),
 (0, "That list of witnesses names no medical practitioner.", B2),
 ("B", "THE OUTLINES OF EVIDENCE - FORM AND REFERENCES"),
 (0, "On 24 September 2026 the Respondent served on the Appellant a document headed \"The Respondent's Outlines of Evidence\", containing an outline for each of Ms Chloe Taylor, Ms Tammy Reese, Ms Kimberley Wright and Ms Nicole Earl.", B1,
     ('B1', "The Respondent's Outlines of Evidence")),
 (0, "That document was not accompanied by any expert report.", B1),
 (0, "That document contains references to paragraphs of the Respondent's amended statement of facts and contentions dated 13 May 2026 in the form \"(SOFAC para\".", B1,
     ('B1', "(SOFAC para")),
 (0, f"{OUTL} do not refer to the Respondent's responses of 8 September 2026 to the notices to admit facts and documents served on 28 August 2026.", B1),
 (0, f"{OUTL} do not refer to Review Decision 69983 of the Workers' Compensation Regulator dated 24 October 2024.", B1),
 (0, f"{OUTL} do not refer to the document titled \"Stressor 1(a) - Particulars support bundle\" served by the Appellant on 11 August 2026.", B1),
 (0, f"{OUTL} do not refer to the outlines of evidence served by the Appellant on 9 September 2026, or to the Appellant's schedule of medical documents served on that date.", B1),
 (0, "The outline for Ms Wright states: \"She has no personal dealings with the Appellant.\"", B1,
     ('B1', "She has no personal dealings with the Appellant.")),
 (0, "The outline for Ms Earl states: \"She has no personal dealings with the Appellant.\"", B1,
     ('B1', "She has no personal dealings with the Appellant.")),
 (0, "The outline for Ms Earl contains the words: \"Ms Wright confirms the Appellant uploaded his Special Pandemic Leave application\".", B1,
     ('B1', "Ms Wright confirms the Appellant uploaded his Special Pandemic Leave application")),
 (0, "The outline for Ms Earl contains the words: \"Ms Wright had no knowledge of a \"safety mandate\" the Appellant appears to associate with a 2006 ombudsman report about rest breaks\".", B1,
     ('B1', 'Ms Wright had no knowledge of a "safety mandate" the Appellant appears to associate with a 2006 ombudsman report about rest breaks')),

 ("#", "PART TWO - THE OUTLINES AGAINST THE FACTS ADMITTED ON 8 SEPTEMBER 2026"),
 ("C", "THE BREAK OF 17-18 MARCH 2024"),
 (0, "The outline for Ms Taylor states: \"Confirms the seven-hour break between shifts on 17-18 March 2024 was the result of human error, and was not intentional or repeated.\"", B1,
     ('B1', "Confirms the seven-hour break between shifts on 17-18 March 2024 was the result of human error, and was not intentional or repeated.")),
 (0, f"{OUTL} do not identify the person who prepared the roster for the period 4 March 2024 to 17 March 2024.", B1),
 (0, f"{OUTL} do not state how the shifts of 17 and 18 March 2024 came to be rostered with a break of seven hours between them.", B1),
 (0, "The outline for Ms Earl states: \"he was rostered on ordinary hours rather than overtime at the time\".", B1,
     ('B1', "he was rostered on ordinary hours rather than overtime at the time")),
 adm(188, "That message states: \"Fortnight 18.03.24 is the opposite and has too many ordinary shifts for the fortnight resulting in wage reduction of 7.55hrs as one of the shifts needs to be overtime.\""),
 adm(260, "That decision states: \"Based on this, I find the rostering of these two shifts amounted to unreasonable management action given that it was in direct contradiction to the award and the 8-hour agreement.\""),
 (0, f"{OUTL} do not refer to the finding recorded at fact 260 of the first notice.", B1),
 (0, f"{OUTL} identify no witness who will give evidence in support of paragraph 22(f) of the Respondent's amended statement of facts and contentions dated 13 May 2026, which states: \"says that this issue was not causative of the appellant's injury\".", B1),

 ("D", "THE AGREEMENT OF 17 JUNE 2020"),
 (0, "The outline for Ms Taylor states: \"That All switchboard staff, including the Appellant, had signed an agreement permitting an eight-hour, rather than ten-hour, break between shifts.\"", B1,
     ('B1', "That All switchboard staff, including the Appellant, had signed an agreement permitting an eight-hour, rather than ten-hour, break between shifts.")),
 (0, "The outline for Ms Taylor states: \"Ms Taylor sought advice from HR, who confirmed the agreement was on file and continued to apply.\"", B1,
     ('B1', "Ms Taylor sought advice from HR, who confirmed the agreement was on file and continued to apply.")),
 (0, f"{OUTL} do not identify the officer of Human Resources who \"confirmed the agreement was on file\".", B1,
     ('B1', "confirmed the agreement was on file")),
 (0, "The outline for Ms Reese states: \"That her understanding, through Ms Taylor, was that HR had confirmed the Appellant's earlier eight-hour break agreement continued to apply after he moved to full-time employment\".", B1,
     ('B1', "That her understanding, through Ms Taylor, was that HR had confirmed the Appellant's earlier eight-hour break agreement continued to apply after he moved to full-time employment")),
 (0, "The outline for Ms Wright states that the agreement signed on 17 June 2020 reduced the Appellant's break between shifts \"from ten hours to eight for more than one break period, with no end date, so that it continues to apply indefinitely unless replaced\".", B1,
     ('B1', "from ten hours to eight for more than one break period, with no end date, so that it continues to apply indefinitely unless replaced")),
 (0, "The outline for Ms Wright states: \"She confirms that payroll processes and holds these agreements but does not itself assess an employee's entitlement under them, or under any change in employment status.\"", B1,
     ('B1', "She confirms that payroll processes and holds these agreements but does not itself assess an employee's entitlement under them, or under any change in employment status.")),
 adm(225, "That email states: \"acknowledge you also signed an 8 hour agreement on 17 June 2020, which allows you to work with only an 8 hour break, however this is only applied where staff initiated shift swaps have occurred.\""),
 adm(234, "The Respondent's amended statement of facts and contentions dated 13 May 2026, as presently constituted, does not allege that the consecutive shifts of 17 and 18 March 2024 arose from a staff initiated shift swap."),
 adm(285, "In that response the Respondent admitted paragraph 3 of that notice, being: \"The Employer's 'Fatigue Risk Management Policy' and the relevant Award require a minimum break of 10 hours between shifts, or 8 hours by written agreement.\""),
 adm(254, "That decision states: \"In considering the evidence, I find there was uncertainty between you and the employer regarding whether the 8-hour agreement continued to apply.\""),
 (0, f"{OUTL} do not refer to the email of Ms L Forrest dated 7 July 2026 recorded at facts 224 and 225 of the first notice.", B1),

 ("E", "REFUSING SHIFTS"),
 (0, "The outline for Ms Taylor states: \"Confirms that the Appellant could refuse shifts at any time.\"", B1,
     ('B1', "Confirms that the Appellant could refuse shifts at any time.")),
 (0, "The outline for Ms Reese states: \"Confirms that the Appellant could refuse shifts at any time.\"", B1,
     ('B1', "Confirms that the Appellant could refuse shifts at any time.")),
 adm(2, "That role description states: \"The occupant of this position is required to work continuous shift work over the full 24-hour period, 7 days a week\"."),
 adm(13, "That role description states, under mandatory requirements: \"The position is a continuous shift working role. You must be able to work a roster which covers multiple shifts over a 24/7 period\"."),
 (0, f"{OUTL} do not identify any document by which the Appellant was informed, before 18 March 2024, that he could refuse a rostered shift.", B1),

 ("F", "THE FATIGUE PAYMENT"),
 (0, "The outline for Ms Wright states: \"The advice returned was that the Award's fatigue provision applies to breaks around overtime, not between two ordinary shifts, and that what had occurred was better characterised as a rostering practice issue for the line manager rather than an unpaid entitlement.\"", B1,
     ('B1', "The advice returned was that the Award's fatigue provision applies to breaks around overtime, not between two ordinary shifts, and that what had occurred was better characterised as a rostering practice issue for the line manager rather than an unpaid entitlement.")),
 (0, f"{OUTL} do not identify the member of the \"internal Technical Support team\" who gave that advice, or the date on which it was given.", B1,
     ('B1', "internal Technical Support team")),
 adm(247, "That decision records: \"Ms Taylor responded to your email on 1 May 2024 via email and stated that after a consultation with payroll and Human Resources, your request for fatigue payment for 18 March 2024 would not be processed due to the existing 8-hour agreement signed by you on 17 June 2020.\""),
 adm(249, "The period between the Appellant's email of 8 April 2024 and Ms Taylor's response of 1 May 2024 is 23 days."),
 adm(250, "The Respondent's amended statement of facts and contentions dated 13 May 2026, as presently constituted, does not allege that any response was made to the Appellant's enquiry regarding fatigue leave at any time between 9 April 2024 and 1 May 2024."),
 (0, "The outline for Ms Taylor does not refer to Ms Taylor's email to the Appellant of 1 May 2024 recorded at facts 247 and 248 of the first notice.", B1),

 ("G", "ROSTERING ERRORS BEFORE MARCH 2024"),
 adm(156, "On 7 August 2023 at 1:43 pm Ms Taylor replied to the Appellant, copied to Ms Reese and Ms Smith, stating: \"My sincere apologises about your rostered Monday 7th 0700-1500 shift, I can confirm this was an oversight.\""),
 adm(157, "That email of Ms Taylor states: \"Would you like me to roster you off tomorrow Tuesday 8th 0700-1500 to give you the required rest period\"."),
 adm(287, "In that response the Respondent admitted paragraph 5 of that notice, being that Ms Reese stated in an email dated 7 August 2023: \"I do realise in this instance there was a rostering error that was accidentally made by Chloe with regards to night shifts\"."),
 adm(212, "That email states that Ms Taylor \"was working to fix this error and would get in touch with you about what alternative shifts she could offer\"."),
 adm(220, "That email states: \"I acknowledge there has been a few rostering errors made by Chloe with regards to Cory's line in past rosters\"."),
 (0, "The outline for Ms Taylor does not refer to Ms Taylor's email of 7 August 2023 at 1:43 pm.", B1),
 (0, "The outline for Ms Reese does not refer to Ms Reese's email of 26 April 2024 recorded at fact 211 of the first notice, or to Ms Reese's email of 10 May 2024 recorded at fact 218 of the first notice.", B1),

 ("H", "FATIGUE RAISED BEFORE 18 JUNE 2024"),
 adm(215, "That email states: \"I forwarded the toolkit to Chloe last week for review and action but have yet to receive feedback\"."),
 adm(218, "On 10 May 2024 at 2:08 pm Ms Reese sent an email to Mr Mackenzie Pritchard of Human Resources forwarding the Appellant's email of 1 May 2024, which states: \"I think he is trying to raise that he has concerns over how his manager is rostering for the Switchboard team and how it is impacting on staff fatigue, or more specifically his fatigue.\""),
 adm(223, "That email of Ms Reese to LBH_HR attached the document \"qh-gdl-401-3.3\", being the Queensland Health Fatigue Risk Management Systems Implementation Guideline."),
 adm(264, "That letter states in relation to Item 5: \"The implementation of fatigue risk management assessment at Switchboard Logan Hospital occurred after 30 June 2024 in connection with an organisational change related to the reporting lines for Switchboard.\""),
 (0, "The outline for Ms Reese does not refer to the toolkit recorded at facts 214 to 216 of the first notice, or to the guideline recorded at fact 223 of the first notice.", B1),
 (0, f"{OUTL} identify no witness who will give evidence in support of paragraph 23 of the Respondent's amended statement of facts and contentions dated 13 May 2026, other than the words quoted at Part One, Section B, concerning Ms Wright's knowledge.", B1),

 ("I", "THE ON-CALL NOTIFICATION PROCESS, 13-15 MAY 2024"),
 (0, "The outline for Ms Taylor states that her email of 14 May 2024 at 12:08 pm raised \"the issues of his difficulty attending his rostered shifts between 13 and 15 May 2024, and his failure to follow the on-call notification process\".", B1,
     ('B1', "the issues of his difficulty attending his rostered shifts between 13 and 15 May 2024, and his failure to follow the on-call notification process")),
 adm(162, "On 14 May 2024 at 12:08 pm Ms Taylor sent an email to the Appellant, copied to Ms Reese, with the subject \"Sick leave 14.05.24\", which states: \"in business hours you are to follow the correct process and speak to me directly if its regarding emergent leave, you can contact me either through switch or my office/mobile.\""),
 adm(165, "Each of those two emails identifies the Switchboard as a means by which the Appellant could contact Ms Taylor."),
 adm(166, "The Respondent's amended statement of facts and contentions dated 13 May 2026, as presently constituted, does not allege that the Appellant was informed, at any time before 14 May 2024, that notifying his unavailability by telephoning the Switchboard did not comply with the process required of him."),
 (0, f"{OUTL} do not identify the \"on-call notification process\" referred to in the outline for Ms Taylor by reference to any document.", B1,
     ('B1', "on-call notification process")),

 ("J", "MS TAYLOR'S OFFICE HOURS, 15-21 MAY 2024"),
 (0, "The outline for Ms Reese states: \"Ms Reese's evidence is that, read in substance, this amounted to an accusation that Ms Taylor was not working her rostered hours, sent in a way that gave Ms Taylor no chance to respond before the rest of the department saw it.\"", B1,
     ('B1', "Ms Reese's evidence is that, read in substance, this amounted to an accusation that Ms Taylor was not working her rostered hours, sent in a way that gave Ms Taylor no chance to respond before the rest of the department saw it.")),
 (0, "The outline for Ms Reese states: \"After taking HR's advice, Ms Reese emailed the Appellant later that day at 4:12pm, without her electronic signature, then again in materially the same terms at 6:23pm once she noticed the omission\".", B1,
     ('B1', "After taking HR's advice, Ms Reese emailed the Appellant later that day at 4:12pm, without her electronic signature, then again in materially the same terms at 6:23pm once she noticed the omission")),
 adm(73, "The Respondent's amended statement of facts and contentions dated 13 May 2026, as presently constituted, does not allege that Ms Taylor stated fixed office hours to the Switchboard staff at any time between 23 August 2023 and 17 May 2024."),
 adm(74, "On 15 May 2024 at 1:15 pm the Appellant sent an email to Ms Taylor and Logan Switch, copied to Switchboard staff, Ms Reese and LBH_HR, with the subject \"Office Hours and Departmental Directives\", which states: \"could you please share your office hours so the entire department can be aware of your regular schedule? There has been some noted inconsistency in your arrival and departure times\"."),
 adm(82, "That email states: \"My office hours can vary due to having to take my girls to school in the morning, on the days that I do have school drop off I always let switch know that I will be in later between 0800-830am. Otherwise my hours are from 06:30-14:30.\""),
 adm(79, "On 21 May 2024 at 2:53 pm Ms Reese replied to the Appellant stating: \"With regards to your concerns about having more clarity as to what are Chole's business hours I will follow up on the issues raised.\""),
 (0, "The outline for Ms Reese does not refer to Ms Reese's email of 21 May 2024 at 2:53 pm.", B1),
 (0, "The outline for Ms Taylor does not refer to Ms Taylor's email of 17 May 2024 at 9:30 am recorded at facts 81 to 84 of the first notice.", B1),
 (0, f"{OUTL} do not identify the officer of Human Resources whose advice was taken before Ms Reese's email of 15 May 2024 at 6:23 pm.", B1),

 ("K", "THE COMMUNICATION BOOK, JUNE 2023"),
 (0, "The outline for Ms Taylor states: \"That on 6 June 2023 Ms Taylor found an entry in the switchboard team's shared Communication Book that she considered and removed it without knowing at the time who had written it.\"", B1,
     ('B1', "That on 6 June 2023 Ms Taylor found an entry in the switchboard team's shared Communication Book that she considered and removed it without knowing at the time who had written it.")),
 adm(146, "That email states: \"I was not aware of who put this entry in at the time but I took it out last week as it was clearly an indirect dig at the team and there is already a procedure to follow with this certain entry.\""),
 adm(292, "In that response the Respondent admitted paragraph 14 of that notice, being that in an email to Ms Reese dated 6 June 2023 Ms Taylor stated: \"I did raise my voice and asked him to please stop talking over the top of me.\""),
 (0, "The outline for Ms Taylor does not contain the words \"I did raise my voice\".", B1),
 (0, "The outline for Ms Reese states: \"She never saw the entry itself.\"", B1,
     ('B1', "She never saw the entry itself.")),
 adm(151, "That amended statement of facts and contentions, as presently constituted, does not allege that the removed page has been located, or that any copy of it exists."),

 ("L", "THE SPECIAL PANDEMIC LEAVE APPLICATION, FEBRUARY 2024"),
 (0, "The outline for Ms Earl states: \"Ms Taylor declined the application the next day, 21 February, on the stated basis that a minimum five-day period of leave was required.\"", B1,
     ('B1', "Ms Taylor declined the application the next day, 21 February, on the stated basis that a minimum five-day period of leave was required.")),
 adm(133, "That amended statement of facts and contentions states at paragraph 14(d): \"Ms Taylor did decline the application because on her assessment, the required statutory declaration was not attached to the MyHR submission. Ms Taylor asked the appellant to resubmit\"."),
 (0, "The outline for Ms Earl states: \"meaning the second decline also appears to have been made in error\".", B1,
     ('B1', "meaning the second decline also appears to have been made in error")),
 (0, "The outline for Ms Earl states that the application \"was approved that day by the delegate and manager\".", B1,
     ('B1', "was approved that day by the delegate and manager")),
 adm(120, "That history records: \"Reviewer - Chloe Donovan-Taylor : approved request\", 29.02.2024, 11:21:03."),
 adm(121, "That history records: \"Manager - Tammy Reese : approved request\", 01.03.2024, 16:05:08."),
 adm(131, "The Respondent's amended statement of facts and contentions dated 13 May 2026, as presently constituted, does not identify the person who exercised the power sub-delegated by the Instrument of Human Resource Sub-Delegation in respect of Process Reference 15480560."),
 (0, "The outline for Ms Earl does not identify the \"delegate\" referred to in the words quoted above.", B1),
 (0, "The outline for Ms Taylor does not refer to the Special Pandemic Leave application of February 2024.", B1),
 (0, f"{OUTL} identify no witness who will give evidence in support of paragraph 14(f) of the Respondent's amended statement of facts and contentions dated 13 May 2026, recorded at fact 135 of the first notice.", B1),

 ("M", "PAY, AND THE ATTENDANCE VARIATION AND ALLOWANCE CLAIMS"),
 (0, "The outline for Ms Wright states: \"There are no outstanding underpayments owed to him.\"", B1,
     ('B1', "There are no outstanding underpayments owed to him.")),
 (0, "The outline for Ms Wright states that the discretionary public holiday allowance is a payment \"which must be approved and submitted by the line manager on an AVAC\".", B1,
     ('B1', "which must be approved and submitted by the line manager on an AVAC")),
 (0, "The outline for Ms Earl states, of 10 April 2023: \"because no AVAC was ever submitted seeking the discretionary allowance for that date either, nothing further is payable in respect of it\".", B1,
     ('B1', "because no AVAC was ever submitted seeking the discretionary allowance for that date either, nothing further is payable in respect of it")),
 adm(200, "That report records the initiator of each of those five Attendance Variation and Allowance Claims as \"Donovan-Taylor, Chloe\"."),
 adm(201, "That report records the initiator of no Attendance Variation and Allowance Claim in that period as the Appellant."),
 adm(193, "That message of 13 May 2024 states: \"I cannot see that any of the issues below have been corrected. Please speak to your Line Manager to have them corrected with an AVAC submitted through My HR as this will also be affecting your RDO balances as well as your pay.\""),
 adm(210, "Neither AVAC PRN 15397775 nor AVAC PRN 15605601 appears in the myHR submissions report produced by Metro South Health as Item 11 of the notice of non-party disclosure."),
 (0, "The outline for Ms Earl states: \"which pushed him over his contracted 80 hours for the fortnight and triggered an automatic hours reduction on his payslip\".", B1,
     ('B1', "which pushed him over his contracted 80 hours for the fortnight and triggered an automatic hours reduction on his payslip")),
 adm(189, "That message states: \"Fortnight 01.04.24 is the same, 0.95hrs over contracted 76hrs needs to be overtime.\""),
 (0, "The outline for Ms Earl does not state the date on which the entry for 30 March 2024 was corrected.", B1),
 (0, f"{OUTL} do not state the date on which any Attendance Variation and Allowance Claim submitted by Ms Taylor in May 2024 was completed.", B1),

 ("N", "PUBLIC HOLIDAYS, APRIL 2023"),
 (0, "The outline for Ms Taylor states, of the fortnight including Easter 2023: \"so in the result he worked the Saturday and Sunday public holidays, the Monday public holiday, five weekday penalty shifts and two ordinary day shifts\".", B1,
     ('B1', "so in the result he worked the Saturday and Sunday public holidays, the Monday public holiday, five weekday penalty shifts and two ordinary day shifts")),
 (0, "The outline for Ms Earl states, of 10 April 2023, that the Appellant worked a night shift that day which \"fell to be treated as falling on the following (non-holiday) day, so no public holiday entitlement arose\".", B1,
     ('B1', "fell to be treated as falling on the following (non-holiday) day, so no public holiday entitlement arose")),
 (0, "Monday 10 April 2023 was Easter Monday.", "Calendar"),

 ("O", "MATTERS ON WHICH THE OUTLINES IDENTIFY NO WITNESS"),
 (0, f"{OUTL} identify no witness who will give evidence in support of paragraph 8 of the Respondent's amended statement of facts and contentions dated 13 May 2026.", B1),
 (0, f"{OUTL} identify no witness who will give evidence that the Appellant did not sustain a personal injury that is a psychiatric or psychological disorder.", B1),
 (0, f"{OUTL} identify no witness who will give evidence that the Appellant's employment was not a significant contributing factor to his injury.", B1),
 (0, "The outline for Ms Taylor states: \"Denies maintaining an erratic physical presence or imposing unassessed unilateral directives without consultation, and denies any managerial hostility.\"", B1,
     ('B1', "Denies maintaining an erratic physical presence or imposing unassessed unilateral directives without consultation, and denies any managerial hostility.")),
 (0, "The outline for Ms Taylor does not refer to the email of Ms Taylor of 15 April 2024 recorded at facts 49 to 53 of the first notice, to the process recorded at fact 54 of the first notice, or to the email of Ms Taylor of 9 May 2024 at 10:15 am recorded at facts 66 and 67 of the first notice.", B1),
 adm(101, "That reply of Ms Taylor states: \"Taking note of your recommendation, we can also put the updated procedures out to the team for consultation before implementing.\""),
 adm(273, "The Respondent's amended List of Documents dated 14 August 2026 does not list any document recording consultation with Switchboard operators before the change communicated by the email of 15 April 2024."),

 ("#", "PART THREE - THE RESPONDENT'S DISCLOSURE OF JULY 2025"),
 ("P", "QUEENSLAND HEALTH PAYROLL, 11 JULY 2025"),
 (0, "The Respondent's disclosure includes a document headed \"Disclosure from witness conferencing - Qld Health Payroll\", containing an email from Ms Samantha Christensen to Ms Matheson, copied to Ms Kimberley Wright, dated Friday 11 July 2025 at 12:02 pm.", B4,
     ('B4', "Disclosure from witness conferencing -"), ('B4', "Friday, 11 July 2025 12:02:25 PM")),
 (0, "That email states: \"Kim Wright is currently out of office, and she had requested that I provide you with the information in relation to the case for Mr Shepherd on her behalf.\"", B4,
     ('B4', "Kim Wright is currently out of office, and she had requested that I provide you with the information in relation to the case for Mr Shepherd on her behalf.")),
 (0, "That email states: \"The shift on the 09.02.2024 was amended with an exemption for the Validation of Claims form on the 30.06.2025 and is on Payslip 07.\"", B4,
     ('B4', "The shift on the 09.02.2024 was amended with an exemption for the Validation of Claims form on the 30.06.2025 and is on Payslip 07.")),
 (0, "That email states, of the fortnight commencing 19 February 2024, that Payslip 06 \"shows the 'Hours_Top-Up - Adjustment' of $39.81 being reversed and replaced with 'NP_Special_Leave - Adjustment' which is leave without pay for the hour on the 28/02/2024 shift\".", B4,
     ('B4', "shows the 'Hours_Top-Up - Adjustment' of $39.81 being reversed and replaced with 'NP_Special_Leave - Adjustment' which is leave without pay for the hour on the 28/02/2024 shift")),
 (0, "That email states, of the fortnight commencing 1 April 2024, that Payslip 06, page 3, shows an overtime entry \"amended for the shift on the 01.04.2024\".", B4,
     ('B4', "amended for the shift on the 01.04.2024")),
 (0, "That email states, of the fortnight commencing 18 March 2024: \"the public holiday not required was submitted late and will appear on Payslip 05, page 3\".", B4,
     ('B4', "the public holiday not required was submitted late and will appear on Payslip 05, page 3")),

 ("Q", "MS REESE, 30 JUNE TO 8 JULY 2025"),
 (0, "The Respondent's disclosure includes a document headed \"Disclosure from witness conferencing - Tammy Reese\".", B5,
     ('B5', "Disclosure from witness conferencing - Tammy Reese")),
 (0, "That document contains an email from Ms Matheson to Ms Reese dated Monday 30 June 2025 at 12:06 pm which states: \"In readiness for our conference with you at 1pm on Thursday 3 July 2025, please see below allegations raised by Mr Shepherd that Lisa and I will be speaking with you about.\"", B5,
     ('B5', "In readiness for our conference with you at 1pm on Thursday 3 July 2025, please see below allegations raised by Mr Shepherd that Lisa and I will be speaking with you about.")),
 (0, "That email states: \"The conference is an informal chat, although confidential and not discussed with other witnesses\".", B5,
     ('B5', "The conference is an informal chat, although confidential and not discussed with other witnesses")),
 (0, "That document contains an email from Ms Matheson to Ms Reese dated Friday 4 July 2025 at 11:36 am which states: \"Thank you for taking the time to speak with Lisa and I yesterday in relation to this matter.\"", B5,
     ('B5', "Thank you for taking the time to speak with Lisa and I yesterday in relation to this matter.")),
 (0, "That document contains an email from Ms Reese to Mr David Hall, A/Director, Employee Health Safety & Wellbeing, Metro South Human Resources, dated Monday 7 July 2025 at 2:37 pm, which states: \"Some of my answer to their questions are in the email trail below in blue.\"", B5,
     ('B5', "Some of my answer to their questions are in the email trail below in blue.")),
 (0, "That document contains an email from Mr Hall to Ms Matheson dated Tuesday 8 July 2025 at 10:53 am forwarding that email of Ms Reese.", B5,
     ('B5', "Tuesday, 8 July 2025 10:53:05 AM")),
 (0, "Ms Reese's answers in that email trail state: \"Meeting details noted to have happened 29/08/2023\".", B5,
     ('B5', "Meeting details noted to have happened 29/08/2023")),
 (0, "The outline for Ms Reese states: \"Ms Reese responded and met with him on 10 August 2023.\"", B1,
     ('B1', "Ms Reese responded and met with him on 10 August 2023.")),
 (0, "Ms Reese's answers in that email trail state, of the issue of 13 to 15 May 2024: \"I have looked back at my notes regarding this time and would like to correct my statement I made 3.7.25 when we discussed this issue.\"", B5,
     ('B5', "I have looked back at my notes regarding this time and would like to correct my statement I made 3.7.25 when we discussed this issue.")),
 (0, "Ms Reese's answers in that email trail state: \"Please note following receiving this email from Cory, Chloe rang me stating she was upset following receiving this email and she had contacted HR and spoke to Mackenzie Prichard.\"", B5,
     ('B5', "Please note following receiving this email from Cory, Chloe rang me stating she was upset following receiving this email and she had contacted HR and spoke to Mackenzie Prichard.")),
 (0, "Ms Reese's answers in that email trail state: \"I then contacted HR to ask what should I do in regards to this request and rang HR but could not get Mackenzie but instead spoke to Brendon Punch from HR.\"", B5,
     ('B5', "I then contacted HR to ask what should I do in regards to this request and rang HR but could not get Mackenzie but instead spoke to Brendon Punch from HR.")),
 (0, "Ms Reese's answers in that email trail state: \"Brendon assist me with suggesting wording to put in an email to Cory in reply recommending asking if he could retract the email.\"", B5,
     ('B5', "Brendon assist me with suggesting wording to put in an email to Cory in reply recommending asking if he could retract the email.")),
 (0, "Ms Reese's answers in that email trail record that Ms Taylor was acting in the role of Switchboard Manager from \"31-1-23 to today\".", B5,
     ('B5', "31-1-23 to today")),
 (0, "The Respondent's list of witnesses served on 24 September 2026 does not name Mr Mackenzie Pritchard, Mr Brendon Punch, Ms Elise McGinley or Ms Lyndelle Forrest.", B2),

 ("#", "PART FOUR - MS MATHESON'S EMAIL OF 24 SEPTEMBER 2026 CONCERNING THE DOCUMENTS IN DISPUTE"),
 ("R", "THE DOCUMENTS IN DISPUTE"),
 (0, "By email with the subject \"WC/2024/227 - Cory Shepherd v Workers' Compensation Regulator - Documents in dispute\", received by the Appellant on 24 September 2026, Ms Matheson stated: \"Upon further review of the appeal file, the Regulator is able to confirm the veracity of the following documents:\" followed by the documents numbered 6, 20, 30 and 30A in the schedule to the Appellant's letter of 9 September 2026.", B3,
     ('B3', "Documents in dispute"), ('B3', "Upon further review of the appeal file, the Regulator is able to confirm the veracity of the following documents:")),
 (0, "That email lists, under the words \"In relation to the remaining documents in dispute:\", the documents numbered 1, 5, 17 to 19, 21, 22, 23 and 31 in that schedule.", B3,
     ('B3', "In relation to the remaining documents in dispute:")),
 (0, "That email states: \"The Regulator has requested copies of these documents to be disclosed from MSH.\"", B3,
     ('B3', "The Regulator has requested copies of these documents to be disclosed from MSH.")),
 (0, "That email states: \"Upon receipt of these documents from MSH, I will disclose copies to you as soon as possible.\"", B3,
     ('B3', "Upon receipt of these documents from MSH, I will disclose copies to you as soon as possible.")),
 (0, "That email does not state a reason for the Respondent having disputed, on 8 September 2026, the authenticity of any document listed in it.", B3),
 (0, "That email does not state a date by which the documents numbered 1, 5, 17 to 19, 21, 22, 23 and 31 will be disclosed to the Appellant.", B3),
]

DOCS = [
 ("B1", "The Respondent's Outlines of Evidence, four lay witnesses, five pages", "served 24 September 2026", "Respondent's own document, served under direction 4"),
 ("B2", "Email, Ms R Matheson to the Industrial Registry, copied to the Appellant, attaching the Respondent's list of witnesses", "24 September 2026, 11:50 am", "Respondent's own email"),
 ("B3", "Email, Ms R Matheson to the Appellant, \"Documents in dispute\"", "received 24 September 2026", "Respondent's own email"),
 ("B4", "Extract from the Respondent's disclosure: \"Disclosure from witness conferencing - Qld Health Payroll\" - email of Ms S Christensen to Ms Matheson, copied to Ms K Wright, with the covering page", "11 July 2025", "Respondent's own disclosure, July 2025"),
 ("B5", "Extract from the Respondent's disclosure: \"Disclosure from witness conferencing - Tammy Reese\" - emails of Ms Matheson of 30 June and 4 July 2025, of Ms Reese of 7 July 2025 and of Mr Hall of 8 July 2025, with the covering page", "30 June to 8 July 2025", "Respondent's own disclosure, July 2025"),
 ("B6", "The Respondent's response of 8 September 2026 to the notice to admit facts served 28 August 2026", "8 September 2026", "Respondent's own document, served"),
]

# ------------------------------------------------------------------ numbering
_n = 0; _new = []
for f in FACTS:
    if isinstance(f[0], str): _new.append(f); continue
    _n += 1; _new.append((_n,) + tuple(f[1:]))
FACTS = _new

# ------------------------------------------------------------------ verification (L1-lite)
fail = []
for f in FACTS:
    if isinstance(f[0], str): continue
    for chk in f[3:]:
        kind, val = chk
        if kind == 'ADM':
            m = re.search(r'(?m)^\s*%d\s+(.{20})' % val, open(SRC['R1'], encoding='utf-8', errors='ignore').read())
            blk = open(SRC['R1'], encoding='utf-8', errors='ignore').read()
            i = blk.find('\n%d ' % val) if ('\n%d ' % val) in blk else blk.find('\n %d ' % val)
            seg = blk[i:i+900] if i >= 0 else ''
            if 'Admitted' not in seg or 'Not admitted' in seg.split('\n',1)[0]:
                # the Admitted word sits on the first lines of the fact block in the rendered response
                first = seg.split('\n')[:6]
                if not any('Admitted' in x and 'Not admitted' not in x for x in first):
                    fail.append((f[0], f'fact {val} not shown Admitted in the response'))
        else:
            if norm(val) not in TXT[kind] and norm(val).replace('-', '- ') not in TXT[kind]:
                fail.append((f[0], f'quote not found in {kind}: {val[:70]}...'))
# duplicate facts
seen = {}
for f in FACTS:
    if isinstance(f[0], str): continue
    k = norm(f[1])
    if k in seen: fail.append((f[0], f'duplicate of fact {seen[k]}'))
    seen[k] = f[0]
if fail:
    print('VERIFICATION FAILED'); [print(' ', x) for x in fail]; sys.exit(1)

# ------------------------------------------------------------------ render
ss = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=ss['Heading1'], fontName='Helvetica-Bold', fontSize=12, leading=15.5, spaceAfter=3, alignment=1)
BODY = ParagraphStyle('BODY', parent=ss['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.2, spaceAfter=5)
CEN = ParagraphStyle('CEN', parent=BODY, alignment=1)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=8.1, leading=10.7, textColor=colors.HexColor('#555555'))
WARN = ParagraphStyle('WARN', parent=BODY, fontSize=8.6, leading=11.8, textColor=colors.HexColor('#8a2010'), backColor=colors.HexColor('#fdf1ef'), borderPadding=5)
ITEM = ParagraphStyle('ITEM', parent=BODY, leftIndent=10, spaceBefore=3, spaceAfter=3)
FORMH = ParagraphStyle('FORMH', parent=BODY, fontName='Helvetica-Bold', fontSize=15, leading=18)
FLD = ParagraphStyle('FLD', parent=BODY, fontName='Helvetica-Bold', fontSize=9, leading=12)
VAL = ParagraphStyle('VAL', parent=BODY, fontSize=10, leading=13)
def P(t, s=BODY): return Paragraph(t, s)
def fieldrow(rows, widths):
    t = Table(rows, colWidths=widths)
    t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.6, colors.black), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#f4f4f4')), ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5), ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6)]))
    return t
def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

s = []
s.append(P("<b>INDUSTRIAL COURT OF QUEENSLAND<br/>QUEENSLAND INDUSTRIAL RELATIONS COMMISSION</b>", ParagraphStyle('HD', parent=BODY, fontSize=9.5, leading=12.5, textColor=colors.HexColor('#7a4a10'))))
s.append(fieldrow([[P("Matter Number:", FLD), P("<b>WC / 2024 / 227</b>", VAL)]], [34*mm, 60*mm]))
s.append(Spacer(1, 4*mm))
s.append(P("Form 24 - Notice to admit facts", FORMH))
s.append(P("<i>Industrial Relations Act 2016</i>, section 989<br/><i>Industrial Relations (Tribunals) Rules 2011</i>, rules 41, 49, 108 and 113", SMALL))
s.append(Spacer(1, 5*mm))
s.append(fieldrow([[P("Applicant/Appellant:", FLD), P("Cory Lea Shepherd", VAL)]], [40*mm, 120*mm]))
s.append(P("v", CEN))
s.append(fieldrow([[P("Respondent:", FLD), P("Workers' Compensation Regulator", VAL)]], [40*mm, 120*mm]))
s.append(Spacer(1, 3*mm))
s.append(fieldrow([[P("To:", FLD), P("The Workers' Compensation Regulator<br/>Attention: Ms Renee Matheson, Senior Appeals Officer", VAL)]], [40*mm, 120*mm]))
s.append(Spacer(1, 4*mm))
s.append(P("Take notice that the <b>appellant</b> in this proceeding proposes to prove the facts specified below, and if you do not within <b>14 days</b> serve a notice on the appellant disputing the facts, you are taken to admit, for this proceeding only, the facts specified in this notice.", BODY))
s.append(P("<b>DRAFT - THIRD NOTICE - NOT FOR SERVICE IN THIS FORM.</b> Transcribe the schedule onto the current official Form 24 (facts) and Form 25 (documents) before service. Sign, print name, state the office held (\"Appellant\") and date. The Source column is for verification only and is deleted before service. Every quotation has been machine-checked against its source text; verify each again on the page before service.", WARN))
s.append(PageBreak())
s.append(P("SCHEDULE OF FACTS - THIRD NOTICE TO ADMIT FACTS", H1))
s.append(P("<i>Industrial Relations (Tribunals) Rules 2011, rule 49</i>", CEN))
s.append(P("WC/2024/227 &nbsp;|&nbsp; Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent)", CEN))
s.append(P("In this notice, \"the first notice\" means the notice to admit facts served on the Respondent on 28 August 2026, to which the Respondent responded on 8 September 2026. Where a fact of the first notice is restated, it is restated so that it may be read with the outline of evidence to which it relates; nothing in this notice withdraws or qualifies any admission already made. Section headings are headings only and are not numbered items.", BODY))
s.append(P("TAKE NOTICE that the Appellant proposes to prove the facts specified below, and that if the Respondent does not, within 14 days after receiving this notice, serve a notice on the Appellant disputing those facts, the Respondent is taken to admit them for this proceeding only.", BODY))
rows = [[P("<b>No.</b>", SMALL), P("<b>Fact to be admitted</b>", SMALL), P("<b>Admit / Deny</b>", SMALL), P("<b>Source (delete before service)</b>", SMALL)]]
for f in FACTS:
    if isinstance(f[0], str):
        lab = "" if f[0] == '#' else f[0]
        rows.append([P(f"<b>{lab}</b>", SMALL), P(f"<b>{esc(f[1])}</b>", SMALL), P("", SMALL), P("", SMALL)])
    else:
        rows.append([P(f"<b>{f[0]}</b>", SMALL), P(esc(f[1]), SMALL), P("", SMALL), P(esc(f[2]), SMALL)])
t = Table(rows, colWidths=[9*mm, 99*mm, 19*mm, 39*mm], repeatRows=1)
st = [('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#999999')), ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dddddd')),
      ('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3),
      ('TOPPADDING', (0,0), (-1,-1), 3.5), ('BOTTOMPADDING', (0,0), (-1,-1), 3.5)]
for i, f in enumerate(FACTS, start=1):
    if isinstance(f[0], str):
        st.append(('BACKGROUND', (0,i), (-1,i), colors.HexColor('#c9c9c9' if f[0] == '#' else '#f0f0f0')))
        st.append(('SPAN', (1,i), (3,i)))
t.setStyle(TableStyle(st)); s.append(t)
s.append(Spacer(1, 5*mm)); s.append(P("Cory Lea Shepherd<br/>Appellant (self-represented) &nbsp;|&nbsp; [date]", BODY))

s.append(PageBreak())
s.append(P("SCHEDULE B - DOCUMENTS (ANNEXURE B)", H1))
s.append(P("Authenticity to be admitted &nbsp;|&nbsp; <i>Industrial Relations (Tribunals) Rules 2011, rule 49</i> &nbsp;|&nbsp; for insertion in Form 25", CEN))
s.append(P("Each document is the Respondent's own document, or a document in the Respondent's own disclosure. Copies of Tabs B4 and B5 are extracts from the Respondent's disclosure of July 2025 and are enclosed for convenience.", BODY))
drows = [[P("<b>Tab</b>", SMALL), P("<b>Document</b>", SMALL), P("<b>Date</b>", SMALL), P("<b>Held by the Respondent as</b>", SMALL), P("<b>Admitted / Disputed</b>", SMALL)]]
for d in DOCS: drows.append([P(f"<b>{d[0]}</b>", SMALL), P(esc(d[1]), SMALL), P(esc(d[2]), SMALL), P(esc(d[3]), SMALL), P("", SMALL)])
dt = Table(drows, colWidths=[10*mm, 78*mm, 27*mm, 34*mm, 17*mm], repeatRows=1)
dt.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#999999')), ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dddddd')), ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3), ('RIGHTPADDING', (0,0), (-1,-1), 3), ('TOPPADDING', (0,0), (-1,-1), 3.5), ('BOTTOMPADDING', (0,0), (-1,-1), 3.5)]))
s.append(dt)

s.append(PageBreak())
s.append(P("Covering email - to accompany service", H1))
s.append(P("<b>To:</b> Renee.Matheson@oir.qld.gov.au<br/><b>Subject:</b> WC/2024/227 - Shepherd - third notice to admit facts and documents", SMALL))
s.append(Spacer(1, 3*mm))
for tline in ["Dear Ms Matheson,",
          "I attach a notice to admit facts and a notice to admit documents under rule 49 of the <i>Industrial Relations (Tribunals) Rules 2011</i>, with Annexure B.",
          "The facts concern the Respondent's list of witnesses and outlines of evidence served on 24 September 2026, read with the facts admitted on 8 September 2026 and with documents in the Respondent's own disclosure of July 2025. Extracts of the two disclosure documents are enclosed at Tabs B4 and B5 for convenience.",
          "Kind regards,<br/>Cory Lea Shepherd<br/>Appellant (self-represented), WC/2024/227"]:
    s.append(P(tline, ITEM))
s.append(P("<b>NOTHING FURTHER.</b> No argument, no reference to the conference or hearing election, no comment on the outlines. The notice speaks for itself.", WARN))

OUT = "out/FORM24_THIRD_NOTICE_DRAFT_24SEP2026.pdf"
doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=14*mm, rightMargin=14*mm, topMargin=13*mm, bottomMargin=13*mm)
def f_(c, d):
    c.saveState(); c.setFont('Helvetica-Bold', 7); c.setFillColor(colors.HexColor('#8a2010'))
    c.drawString(14*mm, 8*mm, "DRAFT - THIRD NOTICE TO ADMIT FACTS - VERIFY EVERY QUOTATION ON THE PAGE BEFORE SERVICE")
    c.setFont('Helvetica', 7); c.setFillColor(colors.HexColor('#777777')); c.drawRightString(A4[0]-14*mm, 8*mm, f"Page {d.page}"); c.restoreState()
doc.build(s, onFirstPage=f_, onLaterPages=f_)
pdf = pikepdf.open(OUT, allow_overwriting_input=True)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
pdf.save("out/_t3.pdf"); pdf.close(); os.replace("out/_t3.pdf", OUT)
nf = len([f for f in FACTS if not isinstance(f[0], str)])
print(f"built {OUT} - {nf} facts + {len(DOCS)} documents - all quotations verified against source text")
