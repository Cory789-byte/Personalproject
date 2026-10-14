import zipfile,re,html,os
T=lambda p:html.unescape(''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p)))
esc=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
class Doc:
    def __init__(s,F):
        s.F=F; z=zipfile.ZipFile(F); s.items=[(i,z.read(i.filename)) for i in z.infolist()]; z.close()
        s.x=dict((i.filename,d) for i,d in s.items)['word/document.xml'].decode()
    def paras(s): return re.findall(r'<w:p[ >].*?</w:p>',s.x,re.S)
    def para(s,key,contains=None):
        ps=[p for p in s.paras() if T(p).startswith(key) and (contains is None or contains in T(p))]
        assert len(ps)==1,(key,len(ps)); return ps[0]
    def rep(s,key,old,new,contains=None):
        p=s.para(key,contains)
        ts=re.findall(r'(<w:t[^>]*>)([^<]*)(</w:t>)',p)
        hits=[t for t in ts if old in html.unescape(t[1])]
        assert len(hits)==1,(key,old[:60],len(hits))
        o=hits[0]; nt=html.unescape(o[1]); assert nt.count(old)==1; nt=nt.replace(old,new)
        np_=p.replace(o[0]+o[1]+o[2],'<w:t xml:space="preserve">'+esc(nt)+'</w:t>',1)
        assert s.x.count(p)==1; s.x=s.x.replace(p,np_)
    def delete(s,key,contains=None):
        p=s.para(key,contains); assert s.x.count(p)==1; s.x=s.x.replace(p,'')
    def save(s):
        out=s.F+'.tmp'
        with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as w:
            for i,d in s.items: w.writestr(i, s.x.encode() if i.filename=='word/document.xml' else d)
        os.replace(out,s.F)

CAUSAL='1(b), 1(d), 1(f) to 1(h), 1(k) and 1(l); 2(a) to 2(i), 2(l) and 2(m); and 3(b) to 3(f)'
# ================= 9A =================
d=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx')
# --- nested list of stressors
d.rep('List of stressors.','Each is pleaded below by dated particulars, lettered in date order; the causal particulars are identified at the head of each stressor, and the other particulars are context. An index of the particulars is at Part 3 of the Schedule enclosed with the Appellant\'s letter; it adds no stressor.',
 "Under each stressor, the individual events and issues relied on as causes are listed by number, date, short title and brief description; they are particulars of that stressor, not separate stressors. The other particulars pleaded below are context, or the employer's record of how the matters were handled, and are not listed as causes. An index of all the particulars is at Part 3 of the Schedule enclosed with the Appellant's letter; it adds no stressor.")
d.rep('Database access removed and not restored;','Particulars 1(a) to 1(l); causal particulars 1(b), 1(d), 1(f) to 1(h), 1(k) and 1(l).','Particulars 1(a) to 1(l); the causal particulars are listed below.')
d.rep('Pay wrong in four fortnights; Payroll','Payroll\'s direction of 3 May 2024 not actioned at 13 May, still awaited on 21 May, lodged 28 May and recorded "Part Completed"; a paid leave request declined twice, with the Respondent acknowledging that the attachments were present. Particulars 2(a) to 2(o); causal particulars 2(a) to 2(i) and 2(l) to 2(n).',
 "Payroll's direction of 3 May 2024 not actioned while the Appellant was asking about it, and still awaited on 21 May; a paid leave request declined twice, with the Respondent acknowledging that the attachments were present. Particulars 2(a) to 2(o); the causal particulars are listed below.",contains='Particulars 2(a) to 2(o)')
d.rep('A seven-hour break rostered in that role','the fatigue enquiry answered after 23 days with a refusal; the roster decision recorded on 10 May 2024; no fatigue risk management at the Switchboard before 30 June 2024; and the Respondent\'s own review finding that the rostering was unreasonable management action. Particulars 3(a) to 3(h); causal particulars 3(b) to 3(h).',
 "the fatigue enquiry answered after 23 days with a refusal; the fatigue toolkit raised without feedback; no fatigue risk management at the Switchboard before 30 June 2024; and the Respondent's own review finding that the rostering was unreasonable management action. Particulars 3(a) to 3(h); the causal particulars are listed below.",contains='Particulars 3(a) to 3(h)')
SUB={'1':[
 ('1(b)','18 July 2023 to 18 June 2024','Database access and the restricted correction process','Operators\' access to the database removed and not restored; corrections only through the Coordinator (Tuesdays and every second Monday) or the Manager, and after-hours requests left to wait.'),
 ('1(d)','23 August 2023 to 17 May 2024','Notification of variable office hours','The Manager stated that her hours would vary; no fixed office hours stated to staff for approximately nine months.'),
 ('1(f)','15 April 2024','After hours on call process changed','A new on-call process, effective the day it was notified; no listed record of consultation.'),
 ('1(g)','19 April 2024','Data entry process changed','A new checking process for data entry, introduced following data entry errors.'),
 ('1(h)','2 to 9 May 2024','Misdirected calls and the MASPER response','Nine occasions of calls reaching the wrong team, including a MET-call enquiry; the Manager\'s first reply after 5 days, 18 hours and 14 minutes; a new process sent to staff on 9 May.'),
 ('1(k)','15 to 20 May 2024','Respiratory directory error and requests for correction','Two high-importance requests from the Integrated Respiratory Service, with no response alleged; the Appellant\'s escalation to the Manager at 2:05 pm on 20 May; her reply at 4:30 pm, two hours after her stated office hours.'),
 ('1(l)','15 to 21 May 2024','Office hours request and the retraction response','The Appellant\'s written request for the Manager\'s office hours at 1:15 pm; the Director\'s request that he retract it, 5 hours and 8 minutes later.')],
 '2':[
 ('2(a)','9 February 2024','Seven hours recorded instead of eight','Shift under-recorded; the fortnight topped up from the Appellant\'s RDO balance.'),
 ('2(b)','20 February to 1 March 2024','Processing of paid pandemic leave','The material provided four times; two declines; final approval after ten days; the Respondent pleads that the attachments were present.'),
 ('2(c)','28 February 2024','Second shift recorded as seven hours','Shift under-recorded; the fortnight again topped up from the RDO balance.'),
 ('2(d)','fortnight beginning 18 March 2024','Overtime recorded as ordinary shifts','Too many ordinary shifts recorded, reducing wages; one shift needed to be overtime.'),
 ('2(e)','30 March 2024','Public holiday claim submitted late','On Payroll\'s later account, the public holiday claim was submitted late.'),
 ('2(f)','fortnight beginning 1 April 2024','Hours above the contracted fortnight','Hours over the contracted 76, again requiring overtime.'),
 ('2(g)','8 April to 1 May 2024','Pay enquiry and public holiday review','The Appellant\'s pay enquiry, his follow-up after more than two weeks, and a refusal on 1 May with the public holiday review still open.'),
 ('2(h)','3 May 2024','Payroll directed four fortnight corrections','Payroll, copying the Appellant, directed the Manager to submit an AVAC for each of four fortnights.'),
 ('2(i)','10 to 13 May 2024','Follow-up found no correction','The Appellant followed up; Payroll replied that nothing had been corrected and referred him back to the line manager.'),
 ('2(l)','21 May 2024','Manager awaited Payroll confirmation','The Manager wrote that she was still waiting for payroll confirmation.'),
 ('2(m)','28 May 2024','Validation request','The Manager asked the Appellant to sign a validation form for claims older than three months.')],
 '3':[
 ('3(b)','17 to 18 March 2024','Consecutive shifts and the seven-hour break','Rostered to finish at 23:00 and start at 06:00 on the Monday: seven hours, against ten or eight by written agreement; no swap alleged; on the Appellant\'s account, about 16 hours\' work, 4 of travel and 4 of sleep.'),
 ('3(c)','19 March 2024','Sick leave after the consecutive shifts','The next day recorded as the Appellant\'s own sick leave (7.60 hours); the Respondent says no fatigue leave was due.'),
 ('3(d)','8 April to 1 May 2024','Fatigue enquiry and refusal','The fatigue enquiry answered after 23 days with a refusal relying on the 2020 agreement, with a note that he could end it "going forward".'),
 ('3(e)','16 to 26 April 2024','Roster line error and proposed alternatives','A roster line error acknowledged; no contact about alternative shifts alleged.'),
 ('3(f)','1 to 8 May 2024','Fatigue toolkit raised and HR advice awaited','The Appellant raised the fatigue toolkit without feedback; the Director said HR advice was being sought.')]}
tbl=[t for t in re.findall(r'<w:tbl>.*?</w:tbl>',d.x,re.S) if 'The conditions in which the work was carried on' in t]; assert len(tbl)==1; tbl=tbl[0]
rows=re.findall(r'<w:tr[ >].*?</w:tr>',tbl,re.S); assert len(rows)==4
tmpl=rows[1]
def mkrow(vals):
    cells=re.findall(r'<w:tc>.*?</w:tc>',tmpl,re.S); out=tmpl
    for c,v in zip(cells,vals):
        nc=re.sub(r'<w:t[^>]*>[^<]*</w:t>','<w:t xml:space="preserve">'+esc(v)+'</w:t>',c).replace('<w:b/>','<w:b w:val="0"/>')
        out=out.replace(c,nc,1)
    return out
def theme(r):
    r=r.replace('<w:tcMar>','<w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/><w:tcMar>')
    cells=re.findall(r'<w:tc>.*?</w:tc>',r,re.S)
    r=r.replace(cells[2],cells[2].replace('<w:b w:val="0"/>','<w:b/>'),1)
    return r
new=rows[0]
for k,r in zip(['1','2','3'],rows[1:]):
    new+=theme(r)+''.join(mkrow(v) for v in SUB[k])
ntbl=tbl.replace(''.join(rows),new); assert ''.join(rows) in tbl
d.x=d.x.replace(tbl,ntbl)
# --- reclassification: scope notes and titles
d.rep('Scope of Stressor 2.','Particulars 2(a) to 2(i) and 2(l) to 2(n) identify the entitlement and correction events before the certified injury date. Particular 2(j) records a completed claim in the same period, and particular 2(k) the related HR follow-up; both are context. Particular 2(o) records a later correction of the earlier error, not an additional cause arising in 2025.',
 "Particulars 2(a) to 2(i), 2(l) and 2(m) identify the entitlement and correction events the Appellant experienced before the certified injury date, and are the causal particulars. Particular 2(j) records a completed claim in the same period, and is context. Particulars 2(k), 2(n) and 2(o) are the record of how the concern and the corrections were handled, including when the corrections were finally made; they are relied on as proof of how long the matters at 2(a) to 2(m) remained unresolved, not as separate causes.")
d.rep('Scope of Stressor 3.','The causal particulars are 3(b) to 3(h). Particular 3(a) is pleaded as context, not as a separate cause.',
 "The causal particulars are 3(b) to 3(f). Particular 3(a) is pleaded as context, not as a separate cause. Particulars 3(g) and 3(h) are the employer's internal record of how the fatigue concern was being handled; they are relied on as proof of the matters at 3(d) to 3(f), not as separate causes.")
d.rep('2(k) HR follow-up about rostering (20 May 2024).','2(k) HR follow-up about rostering (20 May 2024).','2(k) HR follow-up about rostering - record only (20 May 2024).')
d.rep('2(n) Three corrections reached a payslip','2(n) Three corrections reached a payslip (5 June 2024).','2(n) Three corrections reached a payslip - record of when corrected (5 June 2024).')
d.rep('2(n) Three corrections reached a payslip','and the 1 April shift was amended to overtime.','and the 1 April shift was amended to overtime. This particular is relied on as the record of how long the matters at 2(c), 2(e) and 2(f) remained uncorrected, not as a separate cause.')
d.rep('2(o) Later correction of the 9 February shift','2(o) Later correction of the 9 February shift (30 June to 2 July 2025).','2(o) Later correction of the 9 February shift - record of when corrected (30 June to 2 July 2025).')
d.rep('2(o) Later correction of the 9 February shift','That was 425 days after Payroll\'s direction of 3 May 2024 (the amendment itself being dated 30 June 2025); after the date of injury;',
 "The amendment was 423 days, and the pay date 425 days, after Payroll's direction of 3 May 2024; both were after the date of injury;")
d.rep('3(g) Risk rating and roster decision recorded','3(g) Risk rating and roster decision recorded (10 May 2024).','3(g) Risk rating and roster decision recorded - internal record (10 May 2024).')
d.rep('3(h) HR follow-up with the fatigue guideline','3(h) HR follow-up with the fatigue guideline (20 May 2024).','3(h) HR follow-up with the fatigue guideline - internal record (20 May 2024).')
d.rep('The myHR submissions report records a claim with process number 16450619','[¶¶ 203 to 204]',
 '[¶¶ 203 to 204] The Appellant was not told at the time that the claim had been submitted, or its process reference; that status is relied on as the record of the claim, not as something known to him then.')
d.rep('On 8 May 2024 at 9:08 am the Director replied','[¶ 217]',
 '[¶ 217] The employer\'s internal record of how that concern was being handled is at 3(g) and 3(h); the email of 10 May 2024 records that the Appellant was "not yet aware" of the roster decision. [¶ 221]')
# --- C.4 and 5B
d.rep('4. Section 32(5)(a) - working conditions','To the extent those circumstances are not management action and were a significant contributing factor, the injury did not arise out of management action, and section 32(5)(a) does not exclude it (paragraphs 6 and 7 below).',
 'Any such circumstances found to have contributed to the disorder must be taken into account in deciding whether the injury as a whole arose out of, or in the course of, reasonable management action taken in a reasonable way, within section 32(5)(a) (paragraph 7 below).')
d.rep('5B.',"5B. Section 32(5)(b) - the injury did not arise from the Appellant's expectation or perception of management action. ","5B. Section 32(5)(b). ")
p=d.para('5B.'); body=T(p)[len('5B. Section 32(5)(b). '):]
d.rep('5B.',body,"The Appellant's pleaded and medical case is that the disorder arose from the actual workplace circumstances and events identified in Part B.2, which the Respondent has admitted, rather than from an expectation or perception of reasonable management action being taken against him. That causal issue is for the Commission to decide on the evidence.")
# --- Orders: one operative path under s 558(1)(c)
d.rep('2. That the decision of the Respondent dated 24 October 2024','be set aside.','be set aside, and that another decision be substituted under section 558(1)(c) of the Act: that the Appellant\'s application for compensation is accepted.')
d.delete('3. That it be declared that the Appellant sustained an injury')
d.delete("4. That the Appellant's application for compensation be accepted")
for old,new in [('5. Such further or other order','3. Such further or other order'),('6. That the Respondent pay','4. That the Respondent pay')]:
    p=d.para(old); ts=re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p)
    tgt=old[:3] if old[:3] in ts[0] else None
    if ts[0].strip()==old[:2]:
        d.x=d.x.replace(p,p.replace('>'+ts[0]+'<','>'+ts[0].replace(old[:1],new[:1],1)+'<',1))
    else:
        d.rep(old,old,new)
# --- Costs of the hearing
d.rep('4. That the Respondent pay',"costs of the appeal under section 558(3)","costs of the hearing under section 558(3)")
d.rep('2. If the appeal is allowed, the Appellant will seek an order','pay his costs of the appeal,','pay his costs of the hearing,')
p=d.para('3. The Appellant will contend that the amounts under section 191(2)(a)')
d.rep('3. The Appellant will contend that the amounts under section 191(2)(a)',
 'having regard to the work involved (a record of 303 facts, 298 of them admitted; the documents at Annexure A to the notice to admit; non-party disclosure under rule 64G; two notices to admit facts and a notice to admit documents; and the four outlines served by the Respondent) and to the importance, difficulty and complexity of an appeal about a psychological injury under section 32(5)(a), which requires each pleaded circumstance to be classified, each management action assessed for reasonableness, and the whole weighed.',
 "having regard to the work involved in the hearing and to its importance, difficulty and complexity: an appeal about a psychological injury under section 32(5)(a), heard on a record of 303 facts, 298 of them admitted, and the documents at Annexure A to the notice to admit, against the evidence of the Respondent's four witnesses, which requires each pleaded circumstance to be classified, each management action assessed for reasonableness, and the whole weighed. The non-party disclosure under rule 64G, the two notices to admit facts and the notice to admit documents are relied on only as showing the work involved in, and the complexity of, the hearing, not as costs recoverable in themselves.")
d.save()
# ================= ELECTION =================
e=Doc('2026-10_REQUEST_election_and_directions_FINAL.docx')
e.rep('4.','whether it disputes the authenticity of each of the ten documents','whether it maintains its dispute as to the authenticity of each of the ten documents',contains='authenticity')
e.rep('4.','that remain outstanding, and on what ground;','that remain outstanding and, if so, on what ground;',contains='authenticity')
e.rep('4.','The Appellant asks that any document whose authenticity is not disputed by that date be taken to be authentic and received at the hearing.',
 'The Appellant asks that any dispute not so maintained cease to be in issue, so that the document is taken to be authentic for the hearing, without affecting any question of relevance or weight; or that the Commission make such other order about authenticity as it considers appropriate.',contains='authenticity')
e.rep('5.','1(b), 1(d), 1(f) to 1(h), 1(k) and 1(l); 2(a) to 2(i) and 2(l) to 2(n); and 3(b) to 3(h)',CAUSAL,contains='causal particular')
e.rep('5.','The other particulars are context, and no answer is sought on them.','The other particulars are context, or the record of how the matters were handled, and no answer is sought on them.',contains='causal particular')
e.save()
# ================= LETTER =================
l=Doc('2026-10_LETTER_to_Registry_FINAL.docx')
l.rep('The application.','the Respondent has admitted 298 of the 303 facts','the Respondent has admitted, to the extent recorded in its response of 8 September 2026, 298 of the 303 facts')
l.rep("The Respondent's notified case",'that was admitted on 8 September 2026 (fact 303).',"that was admitted on 8 September 2026 (fact 303). That admission concerns paragraph 27; it does not dispose of the more specific explanations pleaded elsewhere in the Respondent's statement.")
l.rep('The documents.','whether it disputes the authenticity of each of the ten outstanding documents and on what ground; and that, if it does not, they be taken to be authentic and received at hearing.',
 'whether it maintains its dispute as to the authenticity of each of the ten outstanding documents and, if so, on what ground; that any dispute not so maintained cease to be in issue, so that the document is taken to be authentic for the hearing, without affecting any question of relevance or weight; or that the Commission make such other order about authenticity as it considers appropriate.')
l.rep('Schedule, Part 3:','The causal particulars are 1(b), 1(d), 1(f) to 1(h), 1(k) and 1(l); 2(a) to 2(i) and 2(l) to 2(n); and 3(b) to 3(h). The others, 1(a), 1(c), 1(e), 1(i), 1(j), 2(j), 2(k), 2(o) and 3(a), are context and are not relied on as separate causes.',
 'The causal particulars are '+CAUSAL+'; they are also listed, with their dates and descriptions, under each stressor in the list of stressors in the Second Amended Form 9A. Particulars 1(a), 1(c), 1(e), 1(i), 1(j), 2(j) and 3(a) are context. Particulars 2(k), 2(n), 2(o), 3(g) and 3(h) are the record of how the matters were handled and when the corrections were made; they are relied on as proof, not as separate causes.')
for key,old,new in [('The Director followed up with HR and attached the fatigue guideline','; related context.','; record only.'),
                    ('Payroll identified adjustments for 28 February','1 April.','1 April; record of when corrected.'),
                    ('Payroll identified a later amendment and pay date','evidence of the earlier correction history.','record of when corrected.'),
                    ('The Director recorded his fatigue concerns','undisclosed roster decision.','undisclosed roster decision; internal record.'),
                    ('The Director followed up her earlier query and attached the guideline','the guideline.','the guideline; internal record.')]:
    l.rep(key,old,new)
l.save()
print('ok')
