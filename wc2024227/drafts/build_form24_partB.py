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
_ren = src[src.index('import re as _re'):src.index('_L, _relab')+len('_L, _relab')]
g = {}; exec(_blk, g, g); exec(_ren, g, g)
SEC = {}
cur = None
for f in g['FACTS']:
    if isinstance(f[0], str): cur = f[0]; SEC[cur] = []
    else: SEC[cur].append(f[0])
def rng(*letters):
    ns = sorted(n for L in letters for n in SEC.get(L, []))
    if not ns: return "-"
    spans, lo, prev = [], ns[0], ns[0]
    for n in ns[1:]:
        if n == prev + 1: prev = n; continue
        spans.append((lo, prev)); lo = prev = n
    spans.append((lo, prev))
    parts = [f"{a}&ndash;{b}" if a != b else str(a) for a, b in spans]
    return parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " and " + parts[-1]

# limb, heading, composite (2-3 sentences, fact not conclusion), source sections
ITEMS = [
 ("Prelim.", "The role, and the hours the Appellant sought and obtained",
  "<b>The role.</b> The role description for Administration Officer, Switchboard Services, Logan "
  "Hospital states that the occupant \"is required to work continuous shift work over the full "
  "24-hour period, 7 days a week\", and under mandatory requirements that \"The position is a "
  "continuous shift working role. You must be able to work a roster which covers multiple shifts "
  "over a 24/7 period\". Its key responsibilities include maintaining the Omnivista database, "
  "maintaining pager registers with \"accurate and current information\", participating in the "
  "emergency response process \"strictly adhering to protocols and timeframes\", maintaining \"call "
  "queues to minimum at all times\", and \"The ability to multitask and operate under pressure, "
  "particularly where high volume call traffic is concerned\". On 18 February 2026 the Respondent "
  "admitted that \"Maintaining accurate contact details for medical staff is a critical function of "
  "the Switchboard to ensure effective clinical handover and patient safety\". The Respondent does "
  "not allege that the Appellant ceased to be a continuous shift worker at any time before 18 June "
  "2024, and three movement forms approved by Mr Scott Hughes as delegate on 27 February, 17 April "
  "and 9 June 2026 each record his shift arrangements as \"Continuous Shift Worker\".<br/><br/>"
  "<b>The hours.</b> On 7 August 2023 at 12:21 pm the Appellant asked Ms Taylor, Ms Reese, Ms "
  "Conaghan and Ms Smith to \"formally adhoc an additional 2 shifts per fortnight\", setting out "
  "clause 11.7 of the applicable agreement. On 31 August 2023 he gave Ms Taylor a written "
  "application headed \"Request to Increase Working Hours to Full Time Rotational Roster\", which "
  "records his willingness to take on additional night shifts \"and advocacy to become a union "
  "representative for the switchboard department\" in the same sentence. On 4 September 2023 he "
  "wrote to Ms Reese confirming he was \"able and willing to work any roster that is presented to "
  "me, including the current schedule with full 24-hour availability\" and had \"no issues with "
  "shift work\", attaching a draft roster he had prepared. On 27 September 2023 at 1:52 pm Ms "
  "Taylor advised him the application \"has been approved\" and that she was \"happy to commence "
  "Full-time hours from the 16th October 2023\" - 51 days after the first request.",
  ("A", "C", "S")),

 ("1(a)", "The database, the directives, the stated hours, and the two accumulations",
  "<b>The database.</b> On 18 July 2023 Ms Stibbard, describing her role as \"a project role\" and "
  "\"a temporary position\", wrote: \"While I am fixing up the database and all of its entries, I "
  "will be removing everyone's access to the database.\" She stated her own hours as \"every Tuesday "
  "and second Monday, 8:00 - 16:00\", directed that entries be requested from her directly, that an "
  "urgent entry needed on a day she was absent go to Ms Taylor, and that a request made \"after "
  "hours (overnights, on the weekend or public holiday)\" would \"have to wait until either Chloe or "
  "myself are back\"; she also removed the Contact &amp; Number Changes book from the room. On the "
  "Respondent's pleadings that access was not restored before 18 June 2024, and it is not alleged "
  "that the role description was amended at any time after 18 July 2023. A month earlier, on 16 "
  "June 2023, the Appellant had written raising \"No consultation of the team members or the "
  "department when making major changes\".<br/><br/>"
  "<b>The directives, and the hours.</b> On 15 April 2024 at 12:39 pm Ms Taylor notified Logan "
  "Switch that she and Ms Stibbard had added themselves to after-hours on call, \"effective from "
  "today\", directing that \"Process during office hours remains the same, please contact myself "
  "through switch/office or mobile unless otherwise advised\", and signing as \"A/Switchboard "
  "Manager\". Review Decision 69983 records that on 19 April 2024 she emailed the team imposing a "
  "new data-entry process \"due to errors being made with respect to data entry\". On the "
  "Respondent's pleadings the only statement of her hours then before the team was the range that "
  "decision records her as noting in an email of 23 August 2023 - a start \"between 6:00 to 9:00 "
  "am\" and a finish \"between 2:00 to 5:00 pm\" - and it is not alleged that she stated fixed office "
  "hours at any time between 23 August 2023 and 17 May 2024. She did so on 17 May 2024 at 9:30 am, "
  "32 days after the on-call notification, stating that her hours \"can vary\", that on school "
  "drop-off days she would be in \"between 0800-830am\", and \"Otherwise my hours are from "
  "06:30-14:30\"; she undertook to \"advise of any change to my office hours for the week\" and "
  "directed that \"regardless of my start/finish times next week you are to please contact me "
  "through the day/afterhours either via switch, office or mobile\".<br/><br/>"
  "<b>The MASPER accumulation.</b> On 3 May 2024 at 3:06 pm Vivian Kwok, MASPER Registrar, emailed "
  "Ms Taylor, copied to Dr Pan Jane Wong, listing five occasions on 2 and 3 May 2024 on which a "
  "call went to a number other than the one sought, including at 14:46 when the \"MET call team "
  "called x5290 asking where MET call was located 'VHUB' - switchboard could not tell them where "
  "VHUB was. Had to be redirected by MASPER\". On 8 May 2024 at 5:28 pm she reported four more, on "
  "5, 7 and 8 May, twice \"incorrectly put through to MASPER\" - nine occasions in all, the second "
  "email sent on the fifth calendar day after the first. Those occasions fell while the on-call "
  "arrangement notified on 15 April 2024 was in force. The Respondent does not allege that any "
  "communication was sent to Logan Switch or the Switchboard staff about them between 3 and 9 May "
  "2024. Ms Taylor replied to the Registrar on 9 May 2024 at 9:20 am, asking the Registrar to "
  "confirm her own business hours because they were \"not provided on the rosters\", and told Logan "
  "Switch at 10:15 am that day - six calendar days after the first report - that \"There have been "
  "many ongoing issues raised by the MASPER and the medical department about calls being "
  "transferred to the wrong medical teams\", directing that \"all calls that switch transfer to the "
  "MASPER phone #5223 are being introduced\".<br/><br/>"
  "<b>The request for hours and consultation.</b> On 15 May 2024 at 1:15 pm the Appellant wrote to "
  "Ms Taylor and Logan Switch, copied to the Switchboard staff, Ms Reese and LBH_HR, recording "
  "\"some noted inconsistency in your arrival and departure times\", asking her to \"share your "
  "office hours so the entire department can be aware of your regular schedule\", and asking that "
  "\"any directives and changes within the department is made in consultation with the team\". At "
  "6:23 pm Ms Reese replied, copied to Ms Taylor and marked of High importance, stating the email "
  "\"did not demonstrate our iCARE2 value of Respect and did not comply with our Code of conduct\" "
  "and asking him to retract it; at 7:09 pm he replied that \"Requesting clarity on business hours "
  "is a reasonable question, especially when no one in the department can provide a definitive "
  "answer\". On 21 May 2024 at 2:53 pm Ms Reese wrote that she \"will follow up on the issues "
  "raised\" and asked \"was there one or more particular changes and/or directives where you had "
  "concerns about consultation and communication?\"<br/><br/>"
  "<b>The escalation of 17 May 2024.</b> The Respondent pleads at paragraph 16(b)(iv) that \"Ms "
  "Taylor then raised this as an issue with Ms Reese at 1:20 pm\". The email sent at 1:20 pm on 17 "
  "May 2024 was to Ms Adriana McNamee. It records that on each of 13, 14 and 15 May 2024 the "
  "Appellant notified his unavailability by telephoning the Switchboard, states of the call of 13 "
  "May 2024 \"I told him I am more than happy to cover his shift and if he was unwell, it would be "
  "preferred for him not to come into work\", and states \"I sent an email (attached) to advise Cory "
  "again of the call process and a query about his leave. I also sent a follow up text, advised by "
  "the last HR rep\". No document recording that Ms McNamee sought the Appellant's account of those "
  "matters has been identified or disclosed in the Respondent's disclosed material presently before "
  "the Commission.<br/><br/>"
  "<b>The respiratory directory.</b> On 15 May 2024 at 11:47 am Ms Sue Marriott, Administration "
  "Officer, Integrated Respiratory Service, wrote to Logan Switch, marked of High importance: \"We "
  "are not Respiratory Medical OPD and we do not have any doctors working out of this area.\" The "
  "Respondent does not allege that any response was made before 20 May 2024. On the fifth calendar "
  "day after, at 11:03 am on 20 May 2024, she wrote again, marked of High importance, recording "
  "that \"we continue to get calls put through to us for Respiratory Medical Outpatients\"; the "
  "Respondent does not allege that any response was made to that email before 2:05 pm that day. At "
  "2:05 pm - three hours and two minutes after the second request, five days, two hours and "
  "eighteen minutes after the first, and within the office hours Ms Taylor had stated three days "
  "earlier - the Appellant wrote, marked of High importance, that \"switchboard staff may not be "
  "aware of the clinics due to modifications to the Document: Outpatients Department - Clinic "
  "contact Details. on the 22nd of February 2024. I recommend a modification and review of the "
  "document.\" Ms Taylor replied at 4:30 pm, two hours and twenty-five minutes later and two hours "
  "after her own stated hours had ended: \"Thank you for bringing this to my attention however this "
  "task was being actioned. I had discussed with Richard this morning about the update of "
  "outpatients respiratory/medical\", adding \"Taking note of your recommendation, we can also put "
  "the updated procedures out to the team for consultation before implementing.\" Mr Richard Parry "
  "was among the recipients of Ms Stibbard's on-call roster email of 13 May 2024 and of Ms Taylor's "
  "email of 17 May 2024 on hours. No document created on 20 May 2024 recording that discussion, and "
  "no document recording any communication from Ms Taylor or Mr Parry to Ms Marriott or the "
  "Integrated Respiratory Service that day, has been identified or disclosed in the Respondent's "
  "disclosed material presently before the Commission; nor does the Respondent allege that the "
  "document was amended on or before 20 May 2024, or that the Switchboard staff were notified of "
  "the 22 February 2024 modifications.", ("D", "E")),

 ("1(a)", "The notification of unavailability, 13 to 15 May 2024",
  "Ms Taylor's email of 15 April 2024 states that during office hours the Appellant was to contact "
  "her \"through switch/office or mobile\". Her email of 14 May 2024 at 12:08 pm, sent to the "
  "Appellant and copied to Ms Reese under the subject \"Sick leave 14.05.24\", states: \"in business "
  "hours you are to follow the correct process and speak to me directly if its regarding emergent "
  "leave, you can contact me either through switch or my office/mobile.\" Each of those two emails "
  "identifies the Switchboard as a means by which the Appellant could contact Ms Taylor. On 13, 14 "
  "and 15 May 2024 the Appellant notified his unavailability for his rostered shift by telephoning "
  "the Switchboard; the first of those notifications preceded Ms Taylor's email of 14 May 2024, and "
  "the second and third followed it. The Respondent's amended statement of facts and contentions, "
  "as presently constituted, does not allege that the Appellant was informed, at any time before 14 "
  "May 2024, that notifying his unavailability by telephoning the Switchboard did not comply with "
  "the process required of him.", ("I",)),

 ("1(b)", "The communication book",
  "On 6 June 2023 at 4:05 pm Ms Taylor emailed Ms Reese under the subject \"Fwd: Communication "
  "Book Update\", stating: \"I was not aware of who put this entry in at the time but I took it "
  "out last week as it was clearly an indirect dig at the team and there is already a procedure to "
  "follow with this certain entry\", and \"I just feel like it's being used as a 'burn book' more "
  "than a professional tool that switchboard can use to communicate\". The Respondent pleads at "
  "paragraph 12(a) that it \"admits that the Ms Taylor did remove pages from the Communication "
  "Book on or around 6 June 2023\".<br/><br/>"
  "In its response to the Appellant's notice to admit facts, signed and served by Ms Renee "
  "Matheson, Senior Appeals Officer, on 18 February 2026, the Respondent admitted \"that Ms Taylor "
  "removed a page from the workplace communications book\", but did not admit that the page "
  "contained the Appellant's handwriting, on the stated ground \"because the respondent does not "
  "have a copy of the page\". It admitted that in an email to Ms Reese dated 6 June 2023 Ms Taylor "
  "stated: \"I did raise my voice and asked him to please stop talking over the top of me.\" It also "
  "admitted that maintaining accurate contact details is \"a critical function of the Switchboard to "
  "ensure effective clinical handover and patient safety\", adding \"and says that there was a "
  "procedure in place for this to occur\", and denied a related paragraph on the stated ground "
  "\"because there was already a procedure in place\".", ("G", "S")),

 ("1(c)", "The matters raised in August and September 2023",
  "On 7 August 2023 at 12:21 pm the Appellant wrote asking that he be given \"some space\" and that "
  "further communication stop. Ms Taylor replied at 1:43 pm, copied to Ms Reese and Ms Smith: \"My "
  "sincere apologises about your rostered Monday 7th 0700-1500 shift, I can confirm this was an "
  "oversight\", and offered to roster him off the following day \"to give you the required rest "
  "period\". At 3:13 pm Ms Reese replied that \"As Chloe is your current line manager and as such "
  "you are required to continue to communicate with Chloe for work related issues, shift concerns, "
  "leave, etc.\" At 5:11 pm Ms Reese wrote to Ms Taylor attaching \"Rostered shifts Cory S. past 8 "
  "months.xlsx\" and asking her to send \"your recent communication with Cory about contacting "
  "yourself about missed shifts, as I could not find a copy of this email\". On 29 August 2023 at "
  "6:57 pm Ms Reese sent HR Policy E12 and set out how a grievance could be submitted; on 4 "
  "September 2023 the Appellant replied that he had \"spoken to Chloe\" and they were \"seemingly on "
  "the path to working in a beneficial way\". The Appellant did not submit a grievance under that "
  "policy in 2023.", ("H",)),

 ("1(d)", "The Special Pandemic Leave application",
  "The myHR leave request history for Process Reference 15480560 records the Appellant creating a "
  "draft at 11:24:48 on 20 February 2024 and submitting it at 11:41:27; \"Reviewer - Chloe "
  "Donovan-Taylor : declined request\" at 12:23:43 on 21 February; a second submission at 06:07:32 "
  "on 28 February; a second decline at 09:06:07 on 29 February; a third submission at 11:07:28 that "
  "day; \"Reviewer - Chloe Donovan-Taylor : approved request\" at 11:21:03, thirteen minutes and "
  "thirty-five seconds later; and \"Manager - Tammy Reese : approved request\" at 16:05:08 on 1 "
  "March 2024 - ten days, four hours and forty minutes after the draft. The Respondent pleads that "
  "Ms Taylor declined it \"because on her assessment, the required statutory declaration was not "
  "attached\", that \"a review indicates that in fact, the attachments were present on the "
  "appellant's submission\", and that this was \"a matter of human error by Ms Taylor\". Review "
  "Decision 69983 records Ms Taylor as having \"requested that you send it to her so she could "
  "submit it in MyHR\", and as having \"noted the statutory declaration you provided was sufficient "
  "evidence\". The Instrument of Human Resource Sub-Delegation effective 5 December 2022 "
  "sub-delegates \"the power to approve/not approve paid Special Pandemic Leave ... to a Band 9 "
  "delegate\" and states: \"This Instrument does not permit the further sub-delegation of the powers "
  "outlined in (a) above.\" The Respondent does not allege that Ms Taylor or Ms Reese was a Band 9 "
  "delegate, does not identify who exercised that power in respect of this process reference, and "
  "does not allege that any other Switchboard employee was required to submit such a request "
  "personally through myHR in February 2024.", ("F",)),

 ("1(g)", "The union delegate and the roster consultation",
  "On 18 February 2026 the Respondent admitted \"that the Appellant sent a text to Ms Taylor at "
  "5.03pm that he was 'just putting his hand up'\", saying this was not a formal notification, and "
  "admitted that the Union Encouragement Policy QH-POL-248 \"says words to that effect\", the effect "
  "pleaded being that it \"requires managers to take a 'positive, supportive role' to facilitate "
  "union membership and delegate elections\". The Appellant was endorsed as a workplace delegate on "
  "or about 3 November 2025, approximately thirty-one months after he expressed that interest in "
  "April 2023. The Consultation outcome of December 2024 states that under clause 6.2 of the Award "
  "\"agreement between MSH and the union, or MSH and the majority of employees affected must occur "
  "prior to changes to a shift roster\", agreement being \"consent from the majority (50+1%) of "
  "affected employees\" cast by online ballot; the Consultation Paper records that negotiation of a "
  "new roster commenced on 22 July 2021 and that the proposal was \"intended to introduce a more "
  "equitable roster\" including \"Redistribution of nights for greater equity based on FTE\". "
  "Seventeen employees were balloted in December 2024 and the rosters took effect 20 January 2025. "
  "The Respondent does not allege that agreement under clause 6.2 was obtained before the rostering "
  "of the shifts of 17 and 18 March 2024, or that a ballot was conducted before the on-call change "
  "of 15 April 2024.", ("J",)),

 ("2(a)", "The pay corrections",
  "On 3 May 2024 Ms Elaine Grant of Queensland Health Payroll wrote to Ms Taylor, copied to the "
  "Appellant, identifying incorrect payments across the fortnights commencing 5 February, 19 "
  "February, 18 March and 1 April 2024, naming AVAC PRN 15397775 and AVAC PRN 15605601, and asking "
  "her to \"submit an AVAC to correct these shifts for each fortnight so Cory is paid corrected and "
  "his RDO balance will then be amended\". On 13 May 2024 at 8:21 am Payroll wrote to the Appellant: "
  "\"I cannot see that any of the issues below have been corrected. Please speak to your Line "
  "Manager to have them corrected with an AVAC submitted through My HR.\" The myHR submissions "
  "report for 1 February to 31 May 2024 records seven submissions, five of them Attendance "
  "Variation and Allowance Claims, the initiator of each of those five being \"Donovan-Taylor, "
  "Chloe\" and none being the Appellant; process numbers in that report increase as submission dates "
  "increase, and neither PRN 15397775 nor PRN 15605601 appears in it although each falls between "
  "process numbers that do. The Respondent pleads that \"any discrepancies or errors were remedied "
  "in a timely manner\" and that \"there are no outstanding underpayments for the appellant\".",
  ("K",)),

 ("2(b)", "The delay in correcting the pay",
  "Payroll's instruction of 3 May 2024 was followed on 21 May 2024 at 12:33 pm by Ms Taylor's email "
  "to the Appellant: \"I am still I am waiting payroll confirmation about a few of these payroll "
  "issues and as soon as I do get that confirmation, I will submit an AVAC for next pay run.\" On 28 "
  "May 2024 at 8:36 am she wrote asking him to sign a \"Validation of claims older than 3 months\" "
  "so she could \"escalate for delegate approval\". The Respondent admitted on 18 February 2026 "
  "\"the fact that Ms Taylor submitted the AVAC on 28 May 2024\", and pleads the same at paragraph "
  "21(c). The myHR report records that submission, process number 16450619, with an effective date "
  "of 30 March 2024, a processing date of 30 May 2024, and a status of \"Part Completed\", every "
  "other Attendance Variation and Allowance Claim in the period being recorded as \"Completed\".",
  ("K",)),

 ("3(a)", "The break of 17 and 18 March 2024",
  "The Appellant was rostered to finish at 23:00 on 17 March 2024 and to commence at 06:00 on 18 "
  "March 2024, a break of 7 hours, which the Respondent admitted on 18 February 2026 and pleads at "
  "paragraph 22(a) as \"a 7-hour break (rather than an 8-hour break)\" that was \"a result of human "
  "error and not intentional or repeated\". It pleads at paragraph 22(e) that \"in June 2020, the "
  "Appellant signed an agreement allowing an 8-hour break between shifts\", and at 22(b) that \"the "
  "appellant could refuse shifts at anytime\". By email of 7 July 2026 Ms Forrest stated that the "
  "8-hour agreement \"is only applied where staff initiated shift swaps have occurred\"; the "
  "Respondent does not allege that the shifts of 17 and 18 March 2024 arose from a staff initiated "
  "shift swap. The Leave Takings Report for 19 March 2024 records the Leave Category as \"Sick\", "
  "7.60 hours, status \"APPROVED\"; the Respondent pleads that the leave \"was paid leave\" and that "
  "under clause 18.10 of the Award the Appellant \"is not entitled to fatigue leave, because he was "
  "not performing overtime\".", ("M",)),

 ("3(b)", "The roster concerns, the employer's knowledge, and what was not in place",
  "<b>What was known.</b> On 26 April 2024 at 1:52 pm Ms Reese wrote to the Appellant about roster "
  "concerns he had raised at a meeting on 16 April 2024, recording that Ms Taylor \"was working to "
  "fix this error and would get in touch with you about what alternative shifts she could offer\" "
  "and that \"I asked Chloe to follow upon what should be the interpretation of this section with "
  "HR\". On 1 May 2024 at 1:18 pm the Appellant wrote citing the Operations Manual fatigue toolkit "
  "and recording \"I forwarded the toolkit to Chloe last week for review and action but have yet to "
  "receive feedback\". On 8 May 2024 Ms Reese replied that she was \"following up with regards to "
  "these with HR for further advice\". On 10 May 2024 at 2:08 pm she forwarded the matter to Mr "
  "Mackenzie Pritchard of Human Resources, writing that the Appellant \"has concerns over how his "
  "manager is rostering for the Switchboard team and how it is impacting on staff fatigue, or more "
  "specifically his fatigue\", that on the Roster Risk assessment Matrix \"we say at best there "
  "would be a rating of 11 which is moderate\", and - the admission - \"I acknowledge there has been "
  "a few rostering errors made by Chloe with regards to Cory's line in past rosters\". On 20 May "
  "2024 at 4:07 pm she followed up with LBH_HR, attaching the Queensland Health Fatigue Risk "
  "Management Systems Implementation Guideline.<br/><br/>"
  "<b>What was not in place.</b> By letter of 5 June 2026, reference K-LM26/729, signed by Ms "
  "Noelle Cridland as Chief Executive, Metro South Health stated that the requested fatigue "
  "training documents \"do not exist\" because \"Mandatory Fatigue Risk Management System training "
  "only applies to health practitioners and clinical assistants\", that \"The implementation of "
  "fatigue risk management assessment at Switchboard Logan Hospital occurred after 30 June 2024\", "
  "that \"there have been no 'consequential' changes to operating procedures over the period "
  "requested\", and that employee complaints about operational errors \"are made directly to the "
  "Line Manager of Switch Board and managed solely via email or verbally with the complainant\".",
  ("L", "O")),

 ("3(c)", "The fatigue leave request, the delay, and the refusal",
  "Review Decision 69983 records that the Appellant emailed Ms Taylor on 8 April 2024 requesting a "
  "review of his payment and noting that the Award \"stipulated in part 5 section 15 that unless "
  "there was a mutual agreement of regular rosters, employees were entitled to a minimum 10-hour "
  "break\". On 9 April 2024 Ms Taylor replied that she \"also escalated your enquiry regarding "
  "fatigue leave to Human Resources to confirm policies around this\", and asked him to raise "
  "concerns \"as soon as they arise so she could action them sooner\". On 24 April 2024 he wrote "
  "that it had been \"more than 2 weeks without any response\". On 1 May 2024 - 23 days after the "
  "request - she refused it \"due to the existing 8-hour agreement signed by you on 17 June 2020\", "
  "noting \"However, she noted you are able to terminate this agreement going forward.\" The "
  "Respondent does not allege that any response was made between 9 April and 1 May 2024.<br/><br/>"
  "The agreement was signed on 17 June 2020. That decision records the employer's response of 6 "
  "September 2024 as confirming there had been a \"change to your employment contract and "
  "adjustments in your working hours\" since, and finds: \"In considering the evidence, I find there "
  "was uncertainty between you and the employer regarding whether the 8-hour agreement continued to "
  "apply.\" It records the Appellant's 9 August 2024 response that the 7-hour break \"did not "
  "include travel time\" and that with it \"your break between shifts would have been less than 5 "
  "hours\", and records that \"The employer did not mention your shift on 18 March 2024.\" It also "
  "records Ms Sandra Johnstone as Switchboard Line Manager as at 8 December 2021 and Ms Danielle "
  "Cook as the \"previous Switchboard Manager\", with \"Ms Taylor was subsequently appointed to the "
  "Switchboard Manager role\". The Respondent does not allege that the agreement was reviewed, "
  "re-executed or re-confirmed between 17 June 2020 and 18 March 2024, that the Appellant was told "
  "before 1 May 2024 that he could terminate it, or that Ms Taylor was the Switchboard Manager on "
  "17 June 2020.", ("N", "B")),

 ("3(d)", "The Review Decision",
  "Review Decision 69983 of 24 October 2024 records that the employer's own response included an "
  "Award extract stating that employees \"must be provided with a break of not less than 10 hours "
  "between the termination of one shift and the commencement of another shift, and 8 hours applied "
  "instead of 10 only in specific circumstances\". It states that the break \"equated to 7 hours\", "
  "that \"Even if you were allowed to leave early on 17 March 2024 as suggested by the employer, "
  "you left a maximum of 30 minutes early, which meant you still did not receive a minimum 8-hour "
  "break\", and that \"Based on this, I find the rostering of these two shifts amounted to "
  "unreasonable management action given that it was in direct contradiction to the award and the "
  "8-hour agreement.\" Under the heading \"Conclusion\" it states that \"you sustained a personal "
  "injury of a psychological nature\" and that \"your injury arose out of employment, to the extent "
  "that it arose out of factors 2, 3 and 4, where employment was a significant contributing "
  "factor\". The Respondent admitted the contents of that decision on 18 February 2026.", ("Q",)),

 ("General", "The Appellant's contemporaneous account, and the documents the Respondent lists",
  "The Respondent pleads at paragraph 11 of its amended statement of facts and contentions: \"The "
  "respondent does not admit the allegations in stressor 1(a) of the appellants statement, because "
  "there are no particulars or details to respond to.\" On 11 August 2026 the Appellant served on "
  "the Respondent a bundle titled \"Stressor 1(a) - Particulars support bundle\", comprising 30 "
  "pages and six tabs, each stating a particular of Stressor 1(a) and enclosing the documents "
  "recording it. The Respondent's amended List of Documents dated 14 August 2026 lists the emails "
  "the Appellant sent to WorkCover Queensland between 12 July and 30 August 2024, including the "
  "attachments described as \"Event overview\", \"Witness statement - Carolyn Jeffrey\", \"Email: "
  "After hours on call process\", \"Email: Task change switchboard - 19/04/2024\" and \"Email: MASPER "
  "process - 09/05/2024\", and a follow up statement from Ms Jeffrey dated 1 August 2024.",
  ("R",)),

 ("General", "The matters not done, and the matters not alleged",
  "The Respondent's amended statement of facts and contentions dated 13 May 2026, as presently "
  "constituted, does not allege that any fatigue risk assessment was conducted, or any fatigue risk "
  "management training provided to the Appellant, or fatigue risk management assessment implemented "
  "at Logan Hospital Switchboard, at any time before 30 June 2024; nor that any change was made to "
  "the operating procedures of the Switchboard as a consequence of any employee complaint between "
  "1 December 2023 and 30 June 2024. Nor does it allege that the Appellant was subject to any "
  "disciplinary process, or to any formal performance management process, at any time before 18 "
  "June 2024, or describe any communication with him before that date as a warning or as part of "
  "such a process. Paragraph 27 of that statement does not identify, by particular, date, document "
  "or cross-reference, the management action relied upon for the contention in that paragraph. No "
  "document recording consultation with Switchboard operators before the change communicated by the "
  "email of 15 April 2024 has been identified or disclosed in the Respondent's disclosed material "
  "presently before the Commission.", ("P", "T")),
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

t = Table(rows, colWidths=[14*mm, 129*mm, 26*mm], repeatRows=1, splitInRow=1)
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
