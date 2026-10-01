exec(open('edit_change95.py').read())
import html,re
d=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx')
R=d.rep
# 1 fact 180/181
R("The Respondent does not allege that agreement under clause 6.2 of the Award was obtained, or that a ballot of affected employees was conducted, before it. [¶¶ 180 to 181]",
  "The Respondent does not allege that a ballot of affected employees was conducted before it. [¶ 181] Nor does it allege that agreement under clause 6.2 of the Award was obtained before the rostering of the Appellant's shifts on 17 and 18 March 2024 (Stressor 3(b)). [¶ 180]")
R("that agreement under clause 6.2 of the Award was obtained, or a ballot conducted, before that change.",
  "that a ballot of affected employees was conducted before that change; that agreement under clause 6.2 of the Award was obtained before the rostering of 17 and 18 March 2024.")
# 2 fact 272 period
R("is alleged before 30 June 2024. [¶ 272]","is alleged over the period 1 December 2023 to 30 June 2024. [¶ 272]")
R("as a consequence of any employee complaint at any time before 30 June 2024 [¶ 272]","as a consequence of any employee complaint over the period 1 December 2023 to 30 June 2024 [¶ 272]")
# 3 facts 269-272 at p22 and 5.6
R("The Respondent does not allege that any fatigue risk assessment was conducted, that fatigue risk management training was provided, that fatigue risk management assessment was implemented at the Switchboard, or that any change was made to the operating procedures of the Switchboard as a consequence of any employee complaint, at any time before 30 June 2024. [¶¶ 269 to 272]",
  "The Respondent does not allege that any fatigue risk assessment was conducted in respect of the Appellant's position, that fatigue risk management training was provided to the Appellant, or that fatigue risk management assessment was implemented at the Switchboard, at any time before 30 June 2024 [¶¶ 269 to 271], or that any change was made to the operating procedures of the Switchboard as a consequence of any employee complaint over the period 1 December 2023 to 30 June 2024. [¶ 272]")
R("that any fatigue risk assessment was conducted, that any fatigue risk management training was provided, or that fatigue risk management assessment was implemented at the Switchboard, before 30 June 2024;",
  "that any fatigue risk assessment was conducted in respect of the Appellant's position, that any fatigue risk management training was provided to the Appellant, or that fatigue risk management assessment was implemented at the Switchboard, before 30 June 2024;")
# 4 1(i)
R("On 13 May 2024 the Appellant lodged a corrupt conduct complaint regarding clinical risks. The Ethical Standards Unit formally determined this constituted a Public Interest Disclosure (Admitted Fact: Form 24, para 20, admitted 18 February 2026).",
  "On 13 May 2024 the Appellant lodged a complaint. On 24 December 2024 the Ethical Standards Unit determined that it constituted a Public Interest Disclosure (paragraph 20 of the Appellant's first notice to admit facts, admitted 18 February 2026).")
# 5 psychiatrist quote
R('Major Depressive Disorder with anxiety state"; that fluoxetine was increased to two capsules "from today" and Seroquel 25 mg commenced at night,',
  'Major Depressive Disorder with anxiety state …"; that fluoxetine was increased to two capsules "from today" and Seroquel 25 mg commenced, at half a tablet for three nights and then one tablet at night,')
# 6 code counts
R("records eight codes on 17 March 2024, eleven on 18 March and sixteen entries on 19 March","records eight entries on 17 March 2024, eleven on 18 March and sixteen on 19 March")
R("The codes on the shift of 17 March 2024.","The codes on 17 March 2024.")
R("for that day (Tab 31) records eight codes:","for that day (Tab 31) records eight entries:")
R("The codes on the shift of 18 March 2024.","The codes on 18 March 2024.")
R("The register records eleven codes that day:","The register records eleven entries that day:")
R("Six of those fell between 06:00 and 14:00: a Code Grey, three adult MET calls (one cancelled within a minute) and two Neonatal MET calls.",
  "Six of those entries fell between 06:00 and 14:00: a Code Grey, two adult MET calls, an entry cancelling the second of them a minute later, and two Neonatal MET calls.")
# 7 smaller
R("a MET call at 14:38 on the shift of 18 March,","a MET call at 14:38 on 18 March,")
R("he had been awake and working for about sixteen hours.","he had been awake for about sixteen hours.")
R("non-clinical. [¶ 265]","non-clinical. [¶ 263]")
R("the Manager's first reply after 5 days, 18 hours and 14 minutes;","the Manager's reply after 5 days, 18 hours and 14 minutes;")
R("The Manager's first reply was sent on 9 May at 9:20 am,","The Manager's reply was sent on 9 May at 9:20 am,")
R("nine occasions in all, the Manager's first reply after five days,","nine occasions in all, the Manager's reply after five days,")
R("to the Manager's first reply, 9 May 2024 at 9:20 am","to the Manager's reply, 9 May 2024 at 9:20 am")
R('"still I am waiting payroll confirmation".','"still I am waiting [sic] payroll confirmation".')
R('please sign and return to be as soon as possible','please sign and return to be [sic] as soon as possible')
R('"premature exposure to the workplace is more likely result in significant deterioration"','"premature exposure to the workplace is more likely [sic] result in significant deterioration"')
R("On 8 August 2023 he confirmed that he would work","On 8 August 2023 the Appellant confirmed that he would work")
R("On 29 August 2023 she sent HR Policy E12,","On 29 August 2023 the Director sent HR Policy E12,")
R("Tab 8A is the cover page only. The following passages are from the disclosed guideline.","Tab 8A is the cover page only. Passages from the disclosed guideline are set out below, after the employer's statements on implementation.")
R("Neither the list nor the outlines names a medical","Neither the list nor the outlines name a medical")
R("a Senior Consultant, Human Resources wrote","a Senior Consultant, Human Resources, wrote")
R("fell on a Monday, the first shift of the working week. [¶ 227]","fell on a Monday. [¶ 227]")
R("the Monday early shift, the first shift of the working week [¶ 227],","the Monday early shift [¶ 227],")
R("On 1 May she replied that the fatigue payment for 18 March would not be processed, and that payroll was still reviewing his public holiday entitlements. [¶¶ 247, 255]",
  "On 1 May she replied that the fatigue payment for 18 March would not be processed [¶ 247]; the review decision records that payroll was, as at 1 May 2024, still reviewing his public holiday entitlements. [¶ 255]")
R("The Respondent admits the contents of Review Decision 69983 and says no finding in it binds the Commission because the hearing is de novo (a fresh hearing). [¶ 295] That is accepted,",
  "The Respondent admits the contents of Review Decision 69983 and says that they are not relevant because the hearing is de novo (a fresh hearing). [¶ 295] It follows that no finding in the decision binds the Commission. That is accepted,")
R("documents at Tabs M1 to M4 and M7 to M9,","documents at Tabs M1 to M5 and M7 to M9 (Tab M6, the treating psychiatrist's clinical records, to be served on receipt),")
R("were addressed to the Manager and Dr Wong [¶¶ 56, 59]","were addressed to the Manager and copied to Dr Wong [¶¶ 56, 59]")
R("Particulars: paragraphs 16, 21 to 22, 25, 55, 69, 73, 90, 93, 99, 105 to 110, 142, 150 to 153, 166, 180 to 181,","Particulars: paragraphs 55, 69, 73, 90, 93, 99, 105 to 110, 142, 150 to 153, 180 to 181,")
R("Emergency codes are received at the Switchboard, categorised by the operator by the type of emergency, and paged to the response group for that category within the time the procedure allows. [¶ 8]",
  "The position receives emergency response notifications and distributes them to the appropriate response groups, dependent on the category of emergency, as per emergency code procedures, strictly adhering to protocols and timeframes. [¶ 8]")
R("Each emergency code at Logan Hospital is received at the Switchboard, categorised by the operator by the type of emergency, and paged to the response group for that category within the time the procedure allows. [¶ 8]",
  "The position receives emergency response notifications and distributes them to the appropriate response groups, dependent on the category of emergency, as per emergency code procedures, strictly adhering to protocols and timeframes. [¶ 8]")
R("both were after the date of injury; after the Respondent's review decision of 24 October 2024; and after this appeal was commenced.","both were after the date of injury, after the Respondent's review decision of 24 October 2024, and after this appeal was commenced.")
# 2(m) row in list of stressors
T=lambda p:html.unescape(''.join(m[1] for m in re.findall(TRX,p)))
rows=[r for r in re.findall(r'<w:tr[ >].*?</w:tr>',d.x,re.S) if T(r).startswith('2(m)28 May 2024Validation request')]
assert len(rows)==1,len(rows); r=rows[0]
nr=r.replace('>28 May 2024<','>28 to 30 May 2024<',1).replace('>Validation request<','>Validation request and partly completed AVAC<',1)
nr=nr.replace('>The Manager asked the Appellant to sign a validation form for claims older than three months.<','>The Manager asked the Appellant to sign a validation form for claims older than three months; the AVAC lodged that day was recorded "Part Completed" on 30 May.<',1)
assert nr.count('28 to 30 May 2024')==1 and 'Part Completed' in nr, 'row'
d.x=d.x.replace(r,nr,1)
d.save(); print("ok")
