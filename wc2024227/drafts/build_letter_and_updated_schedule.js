// WC/2024/227 - Letter to the Regulator: matters that may be agreed before the section 552A conference, enclosing the
// Schedule of 1 October 2026 reproduced and updated. Word output in the style of the 1 October 2026 package: A4,
// Times New Roman 11, 2 cm margins, grey (#D9D9D9) 0.5 pt table borders, centred "Page N" footer.
// The schedule text is the 1 October 2026 text (from the as-sent PDF) except where marked UPDATED below.
// Ask, never allege. No metadata findings, no motive, no costs.
//
// Usage (from wc2024227/drafts): node build_letter_and_updated_schedule.js ["19 October 2026"] ["Friday 30 October 2026"]
// Writes the .docx files and stripped .pdf copies (needs soffice and python3.13 with pikepdf).
const fs = require('fs');
const { execFileSync } = require('child_process');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, BorderStyle, AlignmentType,
        Footer, PageNumber, ImageRun } = require('docx');

const DATE = process.argv[2] || '19 October 2026';
const REPLY_BY = process.argv[3] || 'Friday 30 October 2026';
const OUT = 'out/PRECONF_22OCT2026';
const FONT = 'Times New Roman', SZ = 22;

// **bold** and ~~italic~~ inside a string
function runs(s) {
  const out = [], re = /(\*\*[^*]+\*\*|~~[^~]+~~)/g;
  let last = 0, m;
  while ((m = re.exec(s))) {
    if (m.index > last) out.push(new TextRun({ text: s.slice(last, m.index), font: FONT, size: SZ }));
    const t = m[0].slice(2, -2);
    out.push(new TextRun({ text: t, font: FONT, size: SZ, bold: m[0][0] === '*', italics: m[0][0] === '~' }));
    last = m.index + m[0].length;
  }
  if (last < s.length) out.push(new TextRun({ text: s.slice(last), font: FONT, size: SZ }));
  return out;
}
const P = (s, o = {}) => new Paragraph({
  children: runs(s), alignment: o.align || AlignmentType.JUSTIFIED, keepNext: !!o.keepNext,
  pageBreakBefore: !!o.pageBreakBefore, spacing: { line: 264, before: o.before || 0, after: o.after === undefined ? 80 : o.after } });
const L = (s, after = 0) => P(s, { align: AlignmentType.LEFT, after });
const H = (s, o = {}) => P(`**${s}**`, { after: 120, keepNext: true, ...o });
const AFTER_TABLE = 340;

const B = { style: BorderStyle.SINGLE, size: 4, color: 'D9D9D9' };
function table(widths, header, rows, boldFirst = false, keep = false) {
  const row = (cells, hdr, last) => new TableRow({ tableHeader: hdr, cantSplit: true, children: cells.map((c, i) =>
    new TableCell({ width: { size: widths[i], type: WidthType.DXA }, borders: { top: B, bottom: B, left: B, right: B },
      margins: { top: 70, bottom: 70, left: 80, right: 80 },
      children: [new Paragraph({ children: runs(hdr || (boldFirst && i === 0) ? `**${c}**` : c),
                                 keepNext: keep && !last, spacing: { line: 240, after: 0 } })] })) });
  const total = widths.reduce((a, b) => a + b, 0);
  if (total !== 9638) throw new Error(`table width ${total}`);
  return new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: widths,
    borders: { top: B, bottom: B, left: B, right: B, insideHorizontal: B, insideVertical: B },
    rows: [row(header, true, false), ...rows.map((r, i) => row(r, false, i === rows.length - 1))] });
}

// ---------------------------------------------------------------- Schedule, Part 1 (1 Oct 2026 text; UPDATED columns)
// Position now: "Admitted" only for the 8 Sep admissions; documents the Respondent later confirmed carry its own word,
// "veracity". "Tender proposed" because no agreement to tender, or on admissibility, has been given (letter item 2).
const A = ['Admitted', '-', '-', 'Admitted; tender proposed'];
const VC = 'Veracity confirmed; tender proposed';
const C24 = ['Disputed', 'Confirmed by the Respondent', '-', VC];
const MSH = 'Referred by the Respondent to Metro South for copies';
const C12 = ['Disputed', MSH, 'Copy provided; confirmed', VC];
const part1 = [
  ['1A', 'Stibbard to the Switchboard team, "Hello & Update"', '18 Jul 2023, 12:56 pm', ...A],
  ['1B', 'Taylor to Reese, "Fwd: Communication Book Update", with her email to Logan Switch of 9:57 am that day', '6 Jun 2023, 4:05 pm', ...A],
  ['2', '"Increase of hours and Workplace issues" chain and Reese\'s replies', '7-10 Aug 2023', ...A],
  ['3', 'Reese attaching HR Policy E12; emails of 4 and 8 Sep 2023', '29 Aug-8 Sep 2023', ...A],
  ['4', '"Request to Increase Working Hours to Full Time Rotational Roster"; emails of 7 Aug 2023 1:43 pm and 5:11 pm', '7 and 31 Aug 2023', ...A],
  ['7', '"Roster Concerns" chain', '26 Apr-8 May 2024', ...A],
  ['8', 'Reese to Pritchard "FW: Roster Concerns"; Reese to LBH_HR attaching qh-gdl-401-3.3', '10 and 20 May 2024', ...A],
  ['8A', 'Cover page, Fatigue risk management systems implementation guideline QH-GDL-401-3.3:2021', '2021', ...A],
  ['8B', 'MASPER emails (Taylor to Kwok and Wong; "MASPER process") and issue logs', '9 May 2024 (logs 2-8 May)', ...A],
  ['8C', 'Stibbard, "Switchboard After Hours On Call Manager PP24"', '13 May 2024, 4:29 pm', ...A],
  ['9', 'Taylor, "Switchboard Manager - On call and Hours."', '17 May 2024, 9:30 am', ...A],
  ['9A', '"Office Hours and Departmental Directives" chain (1:15 pm, 6:23 pm, 7:09 pm)', '15 May 2024', ...A],
  ['9B', 'Reese, "RE: Office Hours and Departmental Directives"', '21 May 2024, 2:53 pm', ...A],
  ['10', 'Taylor, "Sick leave 14.05.24", and its forwarding to Reese', '14-15 May 2024 (first email 14 May, 12:08 pm)', ...A],
  ['11', 'Marriott (Integrated Respiratory Service) to Logan Switch; the Appellant to Taylor; Taylor\'s reply', '15 and 20 May 2024', ...A],
  ['12', '"Corey Shepherd 388372 Pay issues" thread', '3-13 May 2024', ...A],
  ['13', 'Same thread, Taylor to the Appellant', '21 May 2024, 12:33 pm', ...A],
  ['14', 'Taylor, "Validation of Claims older than 3 months - Please sign"', '28 May 2024, 8:36 am', ...A],
  ['15', 'myHR submissions report (MSH Item 11)', '1 Feb-31 May 2024', ...A],
  ['16', 'QH Leave Takings Report (MSH Item 15)', '19 Mar 2024', ...A],
  ['25', 'Review Decision 69983', '24 Oct 2024', ...A],
  ['26', 'Appellant\'s first notice to admit facts', 'before 18 Feb 2026', ...A],
  ['27', 'Respondent\'s response to that notice', '18 Feb 2026', ...A],
  ['28', 'myHR leave request history, Process Reference 15480560 (MSH Item 11)', '20 Feb-1 Mar 2024', ...A],
  ['29', 'Instrument of Human Resource Sub-Delegation, Paid Special Pandemic Leave (MSH Item 13)', 'eff. 5 Dec 2022', ...A],
  ['6', 'Taylor, "Afterhours Oncall Process - Switchboard" (Stressor 1(f))', '15 Apr 2024, 12:39 pm', ...C24],
  ['20', 'Metro South to Commissioner Dwyer, K-LM26/729, signed by the Chief Executive (supporting records under Stressors 1 and 3)', '5 Jun 2026', ...C24],
  ['30', 'Taylor, "What\'s Chloe\'s Hours?!" (Stressor 1(d))', '23 Aug 2023, 2:18 pm', ...C24],
  ['30A', 'Taylor, "Good morning Team." (Stressor 1, supporting records)', '18 Jun 2024, 8:58 am', ...C24],
  ['1', 'Role description, Administration Officer, Switchboard Services (AO3), Logan Hospital', 'undated', ...C12],
  ['5', 'Taylor, "Approved - Permanent Full Time FTE"', '27 Sep 2023, 1:52 pm', ...C12],
  ['17', 'Movement form, approved by Mr Hughes as delegate, recording "Continuous Shift Worker"', '27 Feb 2026', ...C12],
  ['18', 'Movement form, approved by Mr Hughes, recording "Continuous Shift Worker"', '17 Apr 2026', ...C12],
  ['19', 'Movement form, approved by Mr Hughes, recording "Continuous Shift Worker"', '9 Jun 2026', ...C12],
  ['21', 'Forrest, Senior Consultant Human Resources, to the Appellant, stating that the 8-hour agreement "is only applied where staff initiated shift swaps have occurred"', '7 Jul 2026', ...C12],
  ['22', 'Consultation Paper, Proposed Rosters for Switchboard Services, signed by Mr Hughes 12 Nov 2024', 'Nov 2024', ...C12],
  ['23', 'Consultation outcome, Proposed Rosters, signed by Mr Hughes 12 Dec 2024', 'Dec 2024', ...C12],
  ['31', 'Screen capture, "2024 Emergency Code Register.xlsx", March 2024 sheet, entries 16-20 Mar 2024 (Stressors 3(b) and 3(c))', 'Mar 2024',
   'Disputed', MSH, 'Spreadsheet provided; confirmed', 'Veracity of the spreadsheet confirmed; tender proposed. Facts 228-231 not admitted (see the table after Part 1)'],
  ['24', 'Moran, Organiser, Together Queensland, to Jeffrey, Conaghan and the Appellant, "Switchboard Roster Feedback - For Delegates"', '3 Nov 2025',
   'Disputed', 'Not mentioned', 'Not mentioned', 'Outstanding; contents admitted (178-179)'],
];
if (part1.length !== 39) throw new Error(`Part 1 has ${part1.length} rows`);
if (part1.filter(r => r[6] !== 'Outstanding; contents admitted (178-179)').length !== 38) throw new Error('count');

const part1Intro =
  'The 39 documents at Annexure A to the notices to admit served 28 August 2026 are the documents from which the facts ' +
  'in Part B of the proposed Second Amended Form 9A are drawn. On 8 September 2026 the Respondent admitted the ' +
  'authenticity of 25 of them and disputed 14. By email of 24 September 2026 it confirmed four of the 14 "upon further ' +
  'review of the appeal file", stated that it had "requested copies of these documents to be disclosed from MSH" for ' +
  'nine others, and did not mention the fourteenth. ' +
  // UPDATED from here
  'By email of 12 October 2026 it provided disclosure copies of those nine documents, Tab 31 as the spreadsheet ' +
  '"2024 Emergency Code Register_16 to 20 March 2024.xlsx", and stated: "The regulator confirms the veracity of the ' +
  'attached documents." Thirty-eight of the 39 documents are therefore admitted or confirmed; the fourteenth, Tab 24, ' +
  'has not been addressed. The facts recorded in 13 of the 14 were admitted on 8 September 2026 to the extent set out ' +
  'in Part B; the exception is the register at Tab 31, from which facts 228 to 231 were not admitted. The table after ' +
  'Part 1 identifies, by row of that spreadsheet, the entries that facts 228 to 231 record.';

const part1Note = // UPDATED
  'The Appellant asked the Respondent on 9 September 2026 to confirm the ten outstanding documents. The copies of Tabs ' +
  '1, 5, 17 to 19, 21 to 24 and 31 came from the Appellant\'s own records; Tabs 17 to 19, 22 and 23 bear the signature ' +
  'of the employer\'s Director, Corporate Services. On 12 October 2026 the Respondent provided its own copy of each of ' +
  'the ten except Tab 24. Tab 24 is a Together Queensland document, which the emails of 24 September and 12 October ' +
  '2026 do not address.';

// ---------------------------------------------------------------- UPDATED: Tab 32 and facts 228 to 231
const tab32Intro =
  '**Documents at Tab 32 (provided to the Respondent on 7 October 2026).** Metro South Health enclosed both documents ' +
  'with its letter of 5 June 2026 (Tab 20). In answer to the Appellant\'s request under rule 49 of the ~~Industrial ' +
  'Relations (Tribunals) Rules 2011~~, the Respondent stated by email of 16 October 2026: "The Regulator confirms the ' +
  'veracity of these documents."';
const tab32 = [
  ['32A', 'Role Description, Manager Switchboard Services, Logan Hospital (AO4), RD 30478699 (Item 6)', 'eff. June 2020', 'Confirmed by the Respondent', VC],
  ['32B', 'Instrument of Human Resource Sub-Delegation, COVID-19 Pandemic Event - Paid Special Pandemic Leave (Item 13); the same instrument as Tab 29', 'signed 23 Nov 2022', 'Confirmed by the Respondent', 'Admitted (as Tab 29); tender proposed'],
];

const factsIntro =
  '**Facts 228 to 231 and the spreadsheet provided on 12 October 2026.** The rows are those of the sheet "MARCH 2024" ' +
  'in the spreadsheet, which has the columns DATE, TIME, CODE AND LOCATION, PAGER and EXTRA INFORMATION.';
const facts = [
  ['228', 'A register titled "2024 Emergency Code Register" records, for 17 March 2024, eight entries, including "MET CALL WARD 2H BED 7" at 19:16, "CODE BLUE WARD 2H BED 7" at 19:20 and "MET CALL WARD 2Q BED 5" at 21:16. (Annexure A, Tab 31)',
   'Rows 9 to 16 are the eight entries for 17 March 2024. The three entries quoted are rows 14, 15 and 16.'],
  ['229', 'That register records, for 18 March 2024: "CODE GREY QAS TRIAGE AIRLOCK" at 8:48; "MET CALL WARD 6A BED 8" at 9:20; "MET CALL WARD 3DR BED 14" at 11:31; "CANCELLED MET CALL WARD 3DR BED 14" at 11:32; "NEONATAL MET CALL THEATRE 2" at 11:35; and "NEONATAL MET CALL BIRTH SUITES 5" at 13:09. (Annexure A, Tab 31)',
   'Rows 17 to 22, in the order quoted.'],
  ['230', 'Six of the entries recorded in that register for 18 March 2024 bear times between 6:00 and 14:00.',
   'Rows 17 to 22. Row 17 is the first entry for 18 March 2024; the next entry, row 23, is at 14:38.'],
  ['231', 'That register records, for 19 March 2024 at 11:34, "MET CALL WARD 2I BED 20" with the notation "CALLED VIA SWITRCHBOARD" [sic]. (Annexure A, Tab 31)',
   'Row 33. The notation is in column E, "EXTRA INFORMATION".'],
];

// ---------------------------------------------------------------- Schedule, Part 2 (1 Oct 2026 text, unchanged)
const part2 = [
  ['The Respondent\'s outlines of the evidence of Ms Taylor, Ms Reese, Ms Wright and Ms Earl', '1(l), 2(n) to 2(o), 3(c); Stressor 3 agreement and pleaded-answer paragraphs; Part C, paragraph 5A', 'Served by the Respondent on 24 September 2026; available to the Commission on request. An outline is not evidence.'],
  ['The spreadsheet of recorded MET calls for 17 and 18 March 2024', 'Stressor 3(b)', 'Metro South Health states that it is available [¶ 268].'],
  ['The Logan Hospital emergency code procedures referred to in the role description', 'Stressor 3, the emergency-code context', 'Referred to in the role description [¶ 8] (Tab 1).'],
  ['The documents recording the advice of Human Resources on the 8-hour agreement', 'Referred to in the outlines (first row)', 'The outlines of Ms Taylor and Ms Reese refer to them; neither identifies them.'],
  ['The Communication Book', 'Stressor 1(a); Part B.5.4', 'Not listed in the Respondent\'s amended List of Documents of 14 August 2026; paragraph 154 of the notice was not admitted.'],
  ['The Respondent\'s disclosure of July 2025 headed "Disclosure from witness conferencing - Qld Health Payroll" (24 pages): the email of Ms Christensen, Manager Service Delivery, Payroll, to the Respondent of 11 July 2025, and Payslips 01 to 07, including Payslip 06 (pay date 5 June 2024) and Payslip 07 (pay date 2 July 2025)', '2(n) to 2(o); Part B.4', 'Disclosed by the Respondent in July 2025.'],
  ['The Respondent\'s disclosure of 11 June 2026 (10 pages): the leave-form walkthrough for Process Reference 15480560, the emails of 15 May 2024 at 1:15 pm and 6:23 pm, and documents concerning the complaint of 13 May 2024', 'Stressors 1(e) and 1(l); for 1(i), the date of the complaint only', 'Disclosed by the Respondent on 11 June 2026.'],
  ['Queensland Health\'s Code Blue procedure 001443 (Royal Brisbane and Women\'s Hospital, version 5, April 2020)', 'Stressor 3, the emergency-code context: the types of Code Blue and the role of Switchboard Services', 'Public document.'],
  ['The Queensland Ombudsman\'s Neville Report (June 2006) and its 2011 update, and the Coroner\'s findings of 12 September 2008', 'Stressor 3, the framework history: the origin of the fatigue framework', 'Public documents.'],
  ['The monthly call statistics for April 2025', 'Stressor 1, the operating conditions; Stressor 3(b), the ordinary-call-load paragraph', 'The Appellant\'s own record and evidence (Part B preamble).'],
  ['Queensland Health Fatigue Risk Management Systems Implementation Guideline QH-GDL-401-3.3:2021 (the full disclosed guideline)', 'Stressor 3(h) and the supporting fatigue records; the quotations from the guideline', 'Disclosed in full with the 20 May 2024 email chain on 14 July 2025. Tab 8A at Annexure A is the cover page only.'],
];

// ---------------------------------------------------------------- Schedule, Part 3 (1 Oct 2026 text, unchanged)
const part3Intro =
  '**Schedule, Part 3: index of the dated particulars in the proposed Second Amended Form 9A (index only; not additional ' +
  'stressors).** The three stressors are pleaded, with their particulars, in the proposed Second Amended Form 9A; this ' +
  'index adds no stressor or particular. The causal particulars are 1(b), 1(d), 1(f) to 1(h), 1(k) and 1(l); 2(a) to ' +
  '2(i), 2(l) and 2(m); and 3(b) to 3(f); they are also listed, with their dates and descriptions, under each stressor in ' +
  'the list of stressors in the proposed Second Amended Form 9A. Particulars 1(a), 1(c), 1(e), 1(i), 1(j), 2(j) and 3(a) ' +
  'are context. Particulars 2(k), 2(n), 2(o), 3(g) and 3(h) are the record of how the matters were handled and when the ' +
  'corrections were made; they are relied on as proof, not as separate causes.';
const part3 = [
  ['1(a)', 'on or around 6 June 2023', 'Removal of the Communication Book entry', 'Entry removed and management response recorded; context only.'],
  ['1(b)', '18 July 2023 to 18 June 2024', 'Database access and the restricted correction process', 'Operators lost access; amendments were channelled through specified staff.'],
  ['1(c)', '7 August to 16 October 2023', 'Roster concerns and the move to full time', 'Roster error, responses and application for increased hours; context only.'],
  ['1(d)', '23 August 2023 to 17 May 2024', 'Notification of variable office hours', 'Variable hours were stated; no intervening statement of fixed hours is alleged.'],
  ['1(e)', '20 February to 1 March 2024', 'Pandemic leave submissions', 'Two declines and three submissions; context here and entitlement issue in 2(b).'],
  ['1(f)', '15 April 2024', 'After hours on call process changed', 'New process was stated to take effect that day.'],
  ['1(g)', '19 April 2024', 'Data entry process changed', 'The review decision records a new checking process following data entry errors.'],
  ['1(h)', '2 to 9 May 2024', 'Misdirected calls and the MASPER response', 'Two reports recorded nine occasions before a revised process was communicated.'],
  ['1(i)', '13 May 2024', 'The complaint of 13 May 2024', 'Date of the complaint; chronology only, with no causal allegation.'],
  ['1(j)', '13 to 15 May 2024', 'On-call roster and absence notification instructions', 'Roster circulated on the first day of the fortnight it covered; notification of unavailability channelled through the manager from 14 May; context only.'],
  ['1(k)', '15 to 20 May 2024', 'Respiratory directory error and requests for correction', 'Repeated requests, the Appellant’s escalation and management reply.'],
  ['1(l)', '15 to 21 May 2024', 'Office hours request and the retraction response', 'Request for clarity, retraction request, hours clarification and follow-up.'],
  ['2(a)', '9 February 2024', 'Seven hours recorded instead of eight', 'The fortnight beginning 5 February was topped up from the RDO balance.'],
  ['2(b)', '20 February to 1 March 2024', 'Processing of paid pandemic leave', 'Three submissions and two declines before final approval.'],
  ['2(c)', '28 February 2024', 'Second shift recorded as seven hours', 'The fortnight beginning 19 February was also topped up from the RDO balance.'],
  ['2(d)', 'fortnight beginning 18 March 2024', 'Overtime recorded as ordinary shifts', 'Payroll identified too many ordinary shifts and a need for overtime coding.'],
  ['2(e)', '30 March 2024', 'Public holiday claim submitted late', 'Payroll later described the 30 March public holiday claim as submitted late; relied on as Payroll\'s later account, not as an admission.'],
  ['2(f)', 'fortnight beginning 1 April 2024', 'Hours above the contracted fortnight', 'Payroll identified a further requirement for overtime coding.'],
  ['2(g)', '8 April to 1 May 2024', 'Pay enquiry and public holiday review', 'Enquiry, acknowledgment, follow-up and response; public holiday review remained open.'],
  ['2(h)', '3 May 2024', 'Payroll directed four fortnight corrections', 'Payroll directed the manager to submit an AVAC for each affected fortnight.'],
  ['2(i)', '10 to 13 May 2024', 'Follow-up found no correction', 'The Appellant followed up; Payroll referred him back to the line manager.'],
  ['2(j)', '15 to 16 May 2024', 'A completed AVAC recorded', 'Process 16328886 was submitted on 15 May and completed on 16 May; context only.'],
  ['2(k)', '20 May 2024', 'HR follow-up about rostering', 'The Director followed up with HR and attached the fatigue guideline; record only.'],
  ['2(l)', '21 May 2024', 'Manager awaited Payroll confirmation', 'The manager said she was still waiting for confirmation.'],
  ['2(m)', '28 to 30 May 2024', 'Validation request and partly completed AVAC', 'Validation sought; process 16450619 was recorded as "Part Completed".'],
  ['2(n)', '5 June 2024', 'Three corrections reached a payslip', 'Payroll identified adjustments for 28 February, 30 March and 1 April; record of when corrected.'],
  ['2(o)', '30 June to 2 July 2025', 'Later correction of the 9 February shift', 'Payroll identified a later amendment and pay date; record of when corrected.'],
  ['3(a)', '7 August to 4 September 2023', 'Earlier roster error and proposed roster', 'Rest was offered after an acknowledged error; the Appellant proposed increased hours; context only.'],
  ['3(b)', '17 to 18 March 2024', 'Consecutive shifts and the seven-hour break', 'Rostered interval, travel, rest and workload relied on in their operational context.'],
  ['3(c)', '19 March 2024', 'Sick leave after the consecutive shifts', 'The record shows 7.60 hours of approved sick leave; the fatigue entitlement is disputed.'],
  ['3(d)', '8 April to 1 May 2024', 'Fatigue enquiry and refusal', 'Acknowledged on 9 April; substantive response and refusal after 23 days.'],
  ['3(e)', '16 to 26 April 2024', 'Roster line error and proposed alternatives', 'Error acknowledged after the meeting; no subsequent contact about alternatives is alleged.'],
  ['3(f)', '1 to 8 May 2024', 'Fatigue toolkit raised and HR advice awaited', 'The Appellant sought action on the toolkit; the Director said she was awaiting advice.'],
  ['3(g)', '10 May 2024', 'Risk rating and roster decision recorded', 'The Director recorded his fatigue concerns, a moderate rating and an undisclosed roster decision; internal record.'],
  ['3(h)', '20 May 2024', 'HR follow-up with the fatigue guideline', 'The Director followed up her earlier query and attached the guideline; internal record.'],
];

function schedule(pageBreakBefore = false) {
  return [
    P(`**WC/2024/227 - Schedule to the Appellant's letter of 1 October 2026, updated to ${DATE}**`,
      { after: 80, keepNext: true, pageBreakBefore }),
    P('The schedule is reproduced as provided on 1 October 2026. Only Part 1 is updated: its introduction, the new ' +
      'column "12 Oct 2026", the column "Position now" and the note after the table; two tables are added after it, for ' +
      'the documents at Tab 32 and for facts 228 to 231. Parts 2 and 3 are unchanged.', { after: 120 }),
    H('Schedule, Part 1: the 39 documents at Annexure A (notices to admit served 28 August 2026) and their status'),
    P(part1Intro, { after: 120 }),
    table([560, 2340, 1200, 1000, 1540, 1300, 1698],
          ['Tab', 'Document', 'Date', '8 Sep 2026', '24 Sep 2026', '12 Oct 2026', 'Position now'], part1),
    P(part1Note, { before: AFTER_TABLE }),
    P(tab32Intro, { before: 120, after: 120, keepNext: true }),
    table([600, 4400, 1300, 1500, 1838], ['Tab', 'Document', 'Date', '16 Oct 2026', 'Position now'], tab32),
    P(factsIntro, { before: AFTER_TABLE, after: 120, keepNext: true }),
    table([700, 5300, 3638], ['Fact', 'The fact as served on 28 August 2026 (not admitted on 8 September 2026)',
                              'Rows of the sheet "MARCH 2024" in the spreadsheet provided on 12 October 2026'], facts, false, true),
    H('Schedule, Part 2: other documents relied on in the proposed Second Amended Form 9A that are not at Annexure A',
      { before: AFTER_TABLE }),
    table([4432, 2122, 3084], ['Document', 'Relied on at', 'Status or source'], part2),
    P(part3Intro, { before: AFTER_TABLE, after: 120, keepNext: true }),
    table([640, 1926, 1926, 5146], ['No.', 'Date or date range', 'Particular', 'Brief description'], part3, true),
  ];
}

// ---------------------------------------------------------------- The letter
function letter() {
  const sig = new Paragraph({ spacing: { before: 120, after: 0 }, children: [new ImageRun({ type: 'png',
    data: fs.readFileSync('assets/SIGNATURE_CoryShepherd.png'), transformation: { width: 170, height: 89 } })] });
  return [
    L(DATE, 80),
    L('Ms Renee Matheson'), L('Senior Appeals Officer'), L('Workers\' Compensation Regulatory Services'),
    L('Office of Industrial Relations'), L('Renee.Matheson@oir.qld.gov.au', 80),
    L(''),
    P('**WC/2024/227 - Cory Lea Shepherd v Workers\' Compensation Regulator**', { align: AlignmentType.LEFT }),
    P('**Matters that may be agreed before the section 552A conference; the Schedule of 1 October 2026, updated**',
      { after: 120 }),
    P('Dear Ms Matheson,'),
    P('Thank you for your emails of 12 and 16 October 2026 confirming the veracity of the documents at Tabs 1, 5, 17 to ' +
      '19, 21 to 23 and 31 of Annexure A and of the documents at Tab 32, and for your email of 19 October 2026 with ' +
      'counsel\'s availability for the conference.'),
    P('**The documents.** With those confirmations, 38 of the 39 documents at Annexure A to the notices to admit served ' +
      'on 28 August 2026 are admitted or confirmed; Tab 24 is the only one outstanding. The Schedule to my letter of ' +
      `1 October 2026 is enclosed, updated to ${DATE}. Part 1 shows the position of each document, and two short ` +
      'tables follow it: the documents at Tab 32, and the entries in the spreadsheet you provided on 12 October 2026 ' +
      'that facts 228 to 231 record. Parts 2 and 3 are unchanged.'),
    P('**Matters that may be agreed.** So that the conference can be used efficiently, and without delaying it, could ' +
      `the Respondent please indicate its position on the following matters by 4.00 pm on ${REPLY_BY}? Any matter ` +
      'that is agreed can then simply be noted at the conference.'),
    P('**1. Facts 228 to 231.** These facts, which were not admitted on 8 September 2026, record entries in the ' +
      'Emergency Code Register for 17, 18 and 19 March 2024. The same entries appear in the spreadsheet "2024 Emergency ' +
      'Code Register_16 to 20 March 2024.xlsx" that you provided on 12 October 2026 and whose veracity the Respondent ' +
      'has confirmed; the table after Part 1 of the Schedule identifies them by row. Now that the spreadsheet is ' +
      'confirmed, does the Respondent admit facts 228 to 231?'),
    P('**2. Tender.** Does the Respondent agree that the 38 documents at Annexure A that are admitted or confirmed, and ' +
      'the document at Tab 32A, may be tendered at any hearing without further proof, either in the form at Annexure A ' +
      'or, for the nine documents you provided on 12 October 2026, in that form? Could the Respondent also say whether ' +
      'it maintains its dispute as to the authenticity of the copy at Tab 24 and, if it does, on what ground?'),
    P('**3. Relevance and admissibility.** Your letter of 8 September 2026 and your email of 16 October 2026 reserve ' +
      'the right to object to the relevance or admissibility of any fact or document at the hearing. So that any such ' +
      'objection can be identified at the conference rather than at the hearing, could the Respondent please identify ' +
      'any admitted fact, and any document at Annexure A or Tab 32A, whose relevance or admissibility it intends to ' +
      'dispute, and the ground?'),
    P('As the proposed Second Amended Form 9A states (Part C, paragraph 8), the admissions are relied on as evidence ' +
      'that the documents admitted exist and of what they say, and as evidence of what the Respondent\'s statement of ' +
      'facts and contentions and List of Documents do not contain; the Appellant does not contend that any admission ' +
      'decides whether any conduct was reasonable. Agreeing to tender, or confirming that no objection is taken to ' +
      'relevance or admissibility, would not require the Respondent to accept the truth of any statement in a ' +
      'document. The weight of each document, and whether any conduct was reasonable management action taken in a ' +
      'reasonable way, remain matters for the Commission.'),
    P('**4. Section 32(1).** Review Decision 69983 states, under the heading "Conclusion", that the Appellant ' +
      '"sustained a personal injury of a psychological nature" and that the "injury arose out of employment, to the ' +
      'extent that it arose out of factors 2, 3 and 4, where employment was a significant contributing factor" (facts ' +
      '261 and 262, admitted); the claim was rejected under section 32(5) of the Act. The Appellant accepts that the ' +
      'hearing is de novo and that no finding in the decision binds the Commission; the question is whether these ' +
      'matters can be agreed. Does the Respondent agree that, to that extent, the elements of section 32(1) are not in ' +
      'issue, so that the issue for any hearing is confined to section 32(5)?'),
    P('**5. Leave.** Does the Respondent consent to leave to file the proposed Second Amended Statement of Facts and ' +
      'Contentions provided on 1 October 2026? If it intends to amend its own statement of facts and contentions in ' +
      'response, how much time does it seek? Once facts 228 to 231 are admitted, I may then provide a completed version ' +
      'of the proposed statement, with any changes from the version provided on 1 October 2026 noted. Any change will ' +
      'add no new stressor or allegation.'),
    P('**6. Paragraph 27.** At the conference I will ask which management action the Respondent relies on for the ' +
      'contention in paragraph 27 of its amended statement of facts and contentions (fact 303), so that the issues for ' +
      'any hearing can be identified.'),
    P('To the extent these matters are not agreed, I will ask the Commission at the conference to deal with them and, ' +
      'if necessary, to make directions or to list the matter for mention.'),
    P('Yours sincerely,', { after: 0, keepNext: true }),
    sig,
    P('**Cory Lea Shepherd, Appellant (self-represented)**', { align: AlignmentType.LEFT, after: 200 }),
    P(`Enclosure: Schedule to the Appellant's letter of 1 October 2026, updated to ${DATE} (Parts 1 to 3).`,
      { align: AlignmentType.LEFT }),
  ];
}

function doc(children, title) {
  return new Document({
    creator: 'Cory Lea Shepherd', lastModifiedBy: 'Cory Lea Shepherd', title,
    styles: { default: { document: { run: { font: FONT, size: SZ } } } },
    sections: [{
      properties: { page: { size: { width: 11906, height: 16838 },
                            margin: { top: 1134, bottom: 1134, left: 1134, right: 1134, header: 709, footer: 709 } } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
        children: [new TextRun({ children: ['Page ', PageNumber.CURRENT], font: FONT, size: SZ })] })] }) },
      children,
    }],
  });
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const both = [...letter(), ...schedule(true)];
  const files = [
    [`${OUT}/LETTER_TO_REGULATOR_with_updated_Schedule_DRAFT.docx`, both,
     'WC/2024/227 - Letter to the Regulator with the updated Schedule'],
    [`${OUT}/SCHEDULE_of_1Oct2026_updated_DRAFT.docx`, schedule(), 'WC/2024/227 - Schedule of 1 October 2026, updated'],
  ];
  for (const [path, children, title] of files) {
    fs.writeFileSync(path, await Packer.toBuffer(doc(children, title)));
    console.log('built', path);
  }
  // PDF copies: LibreOffice conversion, then every metadata field stripped (pikepdf, python3.13).
  const tmp = fs.mkdtempSync(require('os').tmpdir() + '/sched-');
  execFileSync('soffice', ['--headless', '--convert-to', 'pdf', '--outdir', tmp, ...files.map(f => f[0])], { stdio: 'ignore' });
  const strip = 'import pikepdf,sys\nsrc,dst=sys.argv[1:3]\npdf=pikepdf.open(src)\n' +
    'for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]\n' +
    'if "/Metadata" in pdf.Root: del pdf.Root.Metadata\n' +
    'pdf.save(dst, linearize=True)\nprint("built", dst, len(pdf.pages), "pages")';
  for (const [path] of files) {
    const base = path.split('/').pop().replace(/\.docx$/, '.pdf');
    console.log(execFileSync('python3.13', ['-c', strip, `${tmp}/${base}`, `${OUT}/${base}`]).toString().trim());
  }
  fs.rmSync(tmp, { recursive: true, force: true });
})();
