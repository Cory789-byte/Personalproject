import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle, PageBreak

H0=PS('h0',fontName='Helvetica-Bold',fontSize=15,leading=18,spaceAfter=3)
H1=PS('h1',fontName='Helvetica-Bold',fontSize=11.6,leading=14.5,spaceBefore=13,spaceAfter=5)
H2=PS('h2',fontName='Helvetica-Bold',fontSize=9.8,leading=12.5,spaceBefore=8,spaceAfter=3)
B=PS('b',fontName='Helvetica',fontSize=9.1,leading=12.3,spaceAfter=6)
BL=PS('bl',fontName='Helvetica',fontSize=9.1,leading=12.3,spaceAfter=4,leftIndent=8*mm,firstLineIndent=-4.5*mm)
SM=PS('sm',fontName='Helvetica',fontSize=8,leading=10.1)
SMB=PS('smb',fontName='Helvetica-Bold',fontSize=8,leading=10.1)
WARN=PS('w',fontName='Helvetica-Bold',fontSize=9.1,leading=12.3,spaceAfter=6,textColor=colors.HexColor('#8B0000'))

def tbl(rows,w,hdr=True):
    t=Table(rows,colWidths=w,repeatRows=1 if hdr else 0)
    st=[('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5)]
    if hdr: st.append(('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8e8e8')))
    t.setStyle(TableStyle(st)); return t

s=[]
s.append(P('THE MASTER POSITION — BOTH TRACKS',H0))
s.append(P('Cory Shepherd · WC/2024/227 (appeal) and MSH-INJ-5795 (employment) · as at 4 September 2026',SM))
s.append(Spacer(1,6))
s.append(P('⛔ INTERNAL WORKING DOCUMENT. IT CROSSES BOTH TRACKS BY DESIGN AND MUST NEVER BE SERVED, SENT OR ATTACHED. Employment vocabulary does not enter the appeal; appeal vocabulary does not enter correspondence with Human Resources, Payroll or the union. This document exists so that one file carries the whole picture; every outward document is drawn from it, none is this.',WARN))

s.append(P('1. THE POSITION IN ONE PARAGRAPH',H1))
s.append(P('Strong on the merits in both tracks, critical on cash, and now funnelled into one undecided application and one unwritten report. In the appeal the factual record is close to unanswerable and the Respondent has pleaded no particular of its only defence; what remains is causation, which the psychiatric report decides. In the employment matter no instrument for the exclusion has ever been identified and no decision has ever been made; the accrued long service leave balance is confirmed but locked until 29 September on the employer\'s figure, the recreation and sick balances are now spent, and the only mechanism that can pay anything before then is special leave, which has been neither granted nor refused since 28 July.',B))

s.append(P('2. THE THREE POINTS WHERE THE TRACKS JOIN',H1))
s.append(P('<b>(a) The 91-day window.</b> 21 June to 20 September 2024 is both the period the workers\' compensation application was lodged (1 July 2024) and rejected (13 September 2024), and 91 of the 186 days Payroll has excluded from long service leave. If the appeal succeeds and the injury is accepted, that period is compensable absence rather than leave without pay and eligibility reverts to 28 June 2026 — already passed. The appeal is worth nine weeks of long service leave as well as compensation.',BL))
s.append(P('<b>(b) The baseline.</b> The employer approved full-time continuous shift work on 27 September 2023 ("I am very pleased to advise you that this has been approved"), into a role whose mandatory requirement is a 24/7 roster. That single fact answers the Respondent\'s pre-existing-condition point in the appeal and the fitness question in the employment matter. It is already served as facts 26–38 of the Form 24.',BL))
s.append(P('<b>(c) The Employee Capability Checklist of 3 July 2026.</b> The spine of the employment case — "usual switchboard operational duties remain suitable" — and also the document naming the injury, its onset of 18 June 2024 and the stressors.',BL))

s.append(P('3. TRACK A — THE APPEAL, WC/2024/227',H1))
s.append(P('3.1 What is established beyond argument',H2))
rows=[[P('<b>Fact</b>',SMB),P('<b>Source</b>',SMB)],
 [P('A 7-hour break between the shifts of 17 and 18 March 2024',SM),P('Admitted 18 Feb 2026 ¶1; pleaded again SOFC ¶22(a)',SM)],
 [P('The Award requires 10 hours, or 8 by written agreement',SM),P('Admitted 18 Feb 2026 ¶3',SM)],
 [P('A prior rostering error — "accidentally made by Chloe"',SM),P('Admitted 18 Feb 2026 ¶5. Contradicts "not repeated" at SOFC ¶22(a)',SM)],
 [P('The rostering "amounted to unreasonable management action … in direct contradiction to the award and the 8-hour agreement"',SM),P('Review Decision 69983, 24 Oct 2024 — the Respondent\'s own delegate. Contents admitted 18 Feb ¶37, ¶44',SM)],
 [P('"you sustained a personal injury of a psychological nature"; employment "a significant contributing factor" to factors 2, 3 and 4',SM),P('Review Decision 69983, Conclusion',SM)],
 [P('No fatigue risk management training or assessment existed for Switchboard before 30 June 2024 — "the requested documents do not exist"',SM),P('Letter of Ms N Cridland, Chief Executive, to Commissioner Dwyer, 5 June 2026, K-LM26/729',SM)],
 [P('Ms Reese, 10 May 2024: "I acknowledge there has been a few rostering errors made by Chloe"; risk "at best … 11 which is moderate"; "Cory\'s roster will not be considered, however Cory is not yet aware of this"',SM),P('Respondent\'s own disclosure, July 2025',SM)],
 [P('The 8-hour agreement "is only applied where staff initiated shift swaps have occurred"',SM),P('Ms L Forrest, Senior Consultant HR, 7 July 2026. The Respondent does not allege the March shifts arose from a swap (fact 234)',SM)],
 [P('Paragraph 27 identifies no action, date, document or cross-reference for the reasonable-management-action contention',SM),P('Form 24 fact 308',SM)]]
s.append(tbl(rows,[95*mm,75*mm]))

s.append(P('3.2 The machinery now running',H2))
s.append(P('Served on the Respondent on 28 August 2026: a Form 24 notice to admit facts (<b>308 facts</b>, sections A–S), a Form 25 notice to admit documents (<b>39 tabs</b>), Annexure A (<b>133 pages</b>) and a Part B summary of 15 composite limbs. Composition of the 308: 213 verbatim quotations of documents the Respondent disclosed, filed or authored; 39 facts about what its pleading does not allege; 22 about its own admissions of 18 February 2026; 9 of arithmetic; 6 about its own List of Documents; 19 short inferences anchored to a tab. Twenty-four of the 39 tabs are the Respondent\'s own material or Metro South\'s production under its own notices.',B))
s.append(P('<b>Responses fall due 11 September 2026.</b> Under r 49(2) silence for 14 days is deemed admission; under r 49(3) withdrawal of a deemed admission requires leave. ⛔ Do not chase her. His interest is in her doing nothing. If an extension is sought, grant one, in writing, to a stated date.',B))
s.append(P('3.3 What remains contested',H2))
s.append(P('Causation — untouched by any admission, and decided by the psychiatric report. The medical history entry of 26 October 2022, which is the Respondent\'s answer to the clean-baseline pleading and the only fact it has volunteered. The June 2020 eight-hour agreement, which is its only affirmative defence to the break.',B))
s.append(P('3.4 The exposure that is his, not hers',H2))
s.append(P('The Amended Form 9A. Its headings — "Hostile", "Reprisal", "Suppression", "Immediate Reprisal", "Flagrant" — hand the Respondent its ¶11 denial for free and sit one sentence from s 32(5)(b). "Independent Review Office (IRO)" does not exist. And five paragraphs tag facts as "Admitted" that are not admitted in the form pleaded, the response numbering having drifted from the notice numbering after row 26. <b>Fix before the outlines are served on 9 September.</b>',B))
s.append(P('<b>⭐ The paragraph 1.2 substitution.</b> Drop the assertion of a "clean psychiatric baseline", which pleads against a document the Respondent says exists. Replace it with the employer\'s own approval of full-time continuous shift work on 27 September 2023 into a role requiring a 24/7 roster. A lower bar, a stronger fact, entirely theirs, and already served as facts 26–38.',B))

s.append(PageBreak())
s.append(P('4. TRACK B — THE EMPLOYMENT MATTER, MSH-INJ-5795',H1))
s.append(P('4.1 What the employer now concedes',H2))
rows=[[P('<b>Conceded</b>',SMB),P('<b>Where</b>',SMB)],
 [P('Employment commenced 25 March 2019',SM),P('Payroll, 4 Sep 2026; deed recital B',SM)],
 [P('Long service leave eligibility would ordinarily arise 25 March 2026',SM),P('Payroll (G Strachan), 4 Sep 2026',SM)],
 [P('Accrued balance <b>342.5518 hours</b> — 9.01 weeks, $15,229.85 gross at $44.46',SM),P('LSL audit calculator, 4 Sep 2026',SM)],
 [P('Employment is "Permanent Full-time (76 hours per fortnight)"',SM),P('RFMI signed by Mr S Hughes, 31 July 2026',SM)],
 [P('Fit with restrictions; "usual switchboard operational duties remain suitable"',SM),P('Employee Capability Checklist, 3 July 2026, on Metro South\'s own form',SM)],
 [P('"I am required to process leave on your behalf"; recreation balance 41.21 hrs; undertaking to apply it',SM),P('Ms C Taylor, Stage 1 acknowledgement, 4 August 2026',SM)],
 [P('The cl 1.11.2(a) 24-hour Stage 1 timeframe "will not be achieved"',SM),P('Same letter',SM)]]
s.append(tbl(rows,[95*mm,75*mm]))
s.append(P('4.2 What has never happened',H2))
for t in ['No instrument authorising the direction not to attend has ever been identified. Asked in the Stage 1 process on 4 August 2026 and repeatedly since.',
 'No written decision returning him to work, or declining to, has ever been issued.',
 'The application for special leave on full pay under Directive 12/24 cl 6.1, made 28 July and 5 August 2026, has been neither granted nor refused.',
 'The workplace psychosocial risk assessment sought under EB12 cl 7.2 on 28 July 2026 has not been conducted.',
 'The task-by-task match of the role description against the capability checklist, sought the same day, has not been produced.',
 'Stage 1 was notified 3 August 2026; the seven days allowed expired 10 August; no outcome has ever been communicated.']:
    s.append(P('· '+t,BL))
s.append(P('4.3 The leave coding',H2))
s.append(P('Each "Sick Leave – No Pay" entry is a discrete daily request, separately entered on his behalf and separately approved — the record shows them individually, including 03.08.2026 and <b>04.08.2026</b>, each marked APPROVED. The second was entered on the very day Ms Taylor identified the paying alternative in writing and undertook to apply it. On that day four courses were open: annual leave (requested 3 July), recreation leave (identified by her), special leave on full pay (requested the next morning), and, within the same category, paid sick leave, of which he held a balance. The course entered was the only one of the four producing no payment. Section 6 of HR Policy C13 permits leave on an employee\'s behalf only where his written request is held; there is no written request for sick leave without pay, and on 31 August he confirmed he was not applying for personal leave.',B))
s.append(P('<b>He never declined payment.</b> On 5 August he declined only that the absence be funded from his own accrued recreation leave, and asked in the same sentence for special leave on full pay, which under Directive 12/24 is not debited from any leave account.',B))
s.append(P('4.4 The long service leave calculation, and the deed',H2))
rows=[[P('<b>Window excluded</b>',SMB),P('<b>Days</b>',SMB),P('<b>Status</b>',SMB)],
 [P('18 May – 10 June 2022',SM),P('23',SM),P('Query only. The record shows scattered days — 8, 17, 18 May and 15, 16, 18, 19 June — two of them outside the stated window',SM)],
 [P('<b>21 June – 20 September 2024</b>',SM),P('<b>91</b>',SM),P('<b>DISPUTED.</b> The deed reserved these absences (cl 6) rather than characterising them, and cl 7 reserves his rights over any clause 6 management action. It is also the workers\' compensation period. Two independent attacks',SM)],
 [P('13 December 2024 – 23 February 2025',SM),P('72',SM),P('ACCEPTED. Clause 4 of the deed, verbatim',SM)]]
s.append(tbl(rows,[45*mm,14*mm,111*mm]))
s.append(P('186 days total; 25 March 2026 plus 186 gives 27 September (they state 29 September). Remove the 91-day window and eligibility falls on <b>28 June 2026</b> — already passed by 68 days.',B))
s.append(P('⚠ The deed does <b>not</b> contain the words "continuity of service preserved". Clause 1 says he is reinstated to his Employment with an effective date of 20 September 2024, "despite any documents that the Health Service may require the Applicant to execute (for example, for payroll purposes)". Use that; do not quote the other. Clause 8 releases only claims arising from the Dismissal and excludes common law personal injury and statutory workers\' compensation; the 2026 conduct is not released at all. Clause 12 permits disclosure to enforce the deed. Clause 10 binds him against adverse comment about officers in relation to the matters the deed recites.',B))
s.append(P('4.5 Money',H2))
s.append(P('No wages since 13 July 2026. Three pay days at nil: 29 July, 12 August, 26 August. At 76 hours and $44.46 a fortnight is $3,378.96 gross; the wages claim to 30 August is about $11,800 gross before shift penalties, superannuation and leave accrual. On 4 September an ad hoc payment was processed under <b>PRN 24973005</b> for the fortnight 6–17 July, drawn from his own sick and recreation balances. PRN <b>24926366</b> (17–30 August, processed at 0.5 FTE) is due on 9 September. <b>His balances are now spent</b>, so the ad hoc mechanism cannot produce another payment — it pays only what has been coded, and nothing remains to code. Long service leave is locked until 29 September on their figure. <b>Special leave is the only remaining mechanism.</b>',B))
s.append(P('4.6 The alarm',H2))
s.append(P('<b>30 August 2026 · AWOL_NP · "Absent Without Leave" · 7.60 hours · APPROVED.</b> The only entry of that type in 439 rows spanning five and a half years, and the last entry on the record. It falls on the final day of the fortnight Ms Taylor said on 31 August she had processed as "S/L and A/L in lieu of S/L" under 24926366. Unauthorised absence is the predicate for abandonment, and in October 2024 this employer converted absence into termination for abandonment, backdated. Abandonment protection was sought under EB12 cl 6.1 on 28 July 2026.',B))

s.append(PageBreak())
s.append(P('5. THE VERIFICATION LOG — WHAT WAS TESTED AND CORRECTED',H1))
s.append(P('Recorded so that dead lines are not re-run and corrected propositions are not repeated.',B))
rows=[[P('<b>Believed</b>',SMB),P('<b>Corrected to</b>',SMB)],
 [P('The deed says reinstatement "with continuity of service preserved"',SM),P('Those words are not in it. Clause 1 gives an effective date of 20 September 2024 and says reinstatement takes effect despite payroll documentation',SM)],
 [P('The 2026 "Sick Leave – No Pay" coding pushed the long service leave date out',SM),P('It does not. The calculator accrues continuously 23.02.2025–04.09.2026. Only three historical windows are excluded. Do not repeat the proposition — it is in sent correspondence',SM)],
 [P('The served Form 24 contains 290 facts',SM),P('308. The 290-fact file is a superseded build. Cite the 308 numbering',SM)],
 [P('Four pay days had passed at nil',SM),P('Three — 29 July, 12 August, 26 August',SM)],
 [P('HR Policy C7 places the paid special-leave discretion with the chief executive',SM),P('It does not. C7 is keyed to the superseded Directive 05/17 and its paid provisions are category-specific. Cite Directive 12/24 alone',SM)],
 [P('The leave record proves escalating absence before the injury',SM),P('It shows the opposite — 1.73 sick days per month before full-time, 1.64 in the eight months before onset, and 2023 as the heaviest pre-injury year. ⛔ Never deploy it on causation. It is useful only for post-reinstatement deterioration (1.64 → 4.44 per month) and for the fact that 18 June – 20 September 2024 shows zero sick leave against 532 hours of other leave',SM)]]
s.append(tbl(rows,[62*mm,108*mm]))

s.append(P('6. THE STANDING DISCIPLINES',H1))
for t in ['<b>State the chronology, never the motive.</b> Motive is not an element, it raises the standard of persuasion against him, and the dated sequence produces the inference on its own.',
 '<b>Never open the s 32(5)(b) door.</b> Injuries connected to a worker\'s expectation or perception of reasonable management action are not compensable. The Respondent has not pleaded it. Words like punishment, hostile, capricious and reprisal hand it over from his own side.',
 '<b>The firewall.</b> Employment vocabulary never enters the appeal package; appeal vocabulary never enters correspondence with Human Resources, Payroll, the union or the treating practice. One factual sentence about the claim and its rejection is the most that ever crosses.',
 '<b>The agreement, not the deed.</b> Refer to "the agreement under which I was reinstated in February 2025". Never name it, never attach it. Clause 12 permits disclosure to enforce it if that ever becomes necessary — that is his call.',
 '<b>General protections and reprisal stay reserved.</b> Both require pleading a prohibited reason, which is motive, which is the door the appeal is built to keep shut.',
 '<b>Every produced document has its metadata stripped</b> before it leaves the file.']:
    s.append(P('· '+t,BL))

s.append(P('7. THE CALENDAR',H1))
rows=[[P('<b>Date</b>',SMB),P('<b>What falls</b>',SMB)],
 [P('Fri 4 Sep',SM),P('The AWOL query and the long service leave calculation reply',SM)],
 [P('Mon 8 Sep',SM),P('Last working day before the directions deadline',SM)],
 [P('<b>Wed 9 Sep</b>',SM),P('<b>Direction 1</b> — witness list filed and served, 4pm. <b>Direction 2</b> — outlines of evidence served, and any expert report unless varied. PRN 24926366 paid',SM)],
 [P('<b>Fri 11 Sep</b>',SM),P('<b>Form 24 and Form 25 responses fall due. Silence is deemed admission on 308 facts and 39 documents</b>',SM)],
 [P('Wed 23 Sep',SM),P('Pay day. Expert report date if direction 2 is varied',SM)],
 [P('Tue 29 Sep',SM),P('Long service leave eligibility on the employer\'s figure',SM)],
 [P('Wed 30 Sep',SM),P('The Respondent\'s witness list and outlines under directions 3 and 4',SM)],
 [P('Early Oct',SM),P('The direction 5 election — the Appellant\'s to make',SM)]]
s.append(tbl(rows,[24*mm,146*mm]))

s.append(P('8. WHAT TO DO, IN ORDER',H1))
for n,t in [('1','<b>The two emails today</b> — the AWOL query first, on its own, so it draws its own written answer; then the reply on the calculation, opening with genuine thanks for the ad hoc payment.'),
 ('2','<b>The Stage 2 notice to the Chief Executive</b>, with matter 6 corrected and the continuity wording removed. Special leave now leads it, because with the balances spent it is arithmetically the only mechanism that can pay anything before 29 September.'),
 ('3','<b>Replace Form 9A paragraph 1.2</b> before the outlines are served, and fix the five false "Admitted Fact" tags and the "IRO" reference.'),
 ('4','<b>Witness list and outlines by 4pm Wednesday 9 September.</b> Free, hard-edged, unaffected by everything else.'),
 ('5','<b>The direction 2 variation</b> if Dr Krishnaiah cannot confirm a delivery date. The gate is met on what is presently known.'),
 ('6','<b>Verify the accrual treatment of accepted-claim absence</b> before the appeal–long-service-leave argument is put to anyone.'),
 ('7','<b>Do not chase the Respondent about the Form 24.</b> Silence is the outcome sought.')]:
    s.append(P(f'<b>{n}.</b>&nbsp;&nbsp;{t}',BL))
s.append(Spacer(1,6))
s.append(P('The through-line has not changed: state the dates, point at their own documents, never say why. What has changed is that it is working — money moved on 4 September for the first time in eight weeks, and it moved because the ask was specific, anchored to an instrument, and addressed to a named person.',B))

buf=io.BytesIO()
doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=18*mm,rightMargin=18*mm,topMargin=15*mm,bottomMargin=14*mm,title='',author='')
doc.build(s); buf.seek(0)
out=pikepdf.open(buf)
with out.open_metadata() as md:
    for k in list(md): del md[k]
for k in list(out.docinfo.keys()): del out.docinfo[k]
r=out.Root
for k in ('/Metadata','/PieceInfo','/Lang'):
    if k in r: del r[k]
for pg in out.pages:
    for k in ('/Metadata','/PieceInfo'):
        if k in pg.obj: del pg.obj[k]
out.save('out/MASTER_POSITION_both_tracks_4SEP2026_INTERNAL.pdf',fix_metadata_version=False)
print('pages',len(out.pages))
