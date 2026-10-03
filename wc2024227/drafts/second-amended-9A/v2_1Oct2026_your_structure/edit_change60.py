import zipfile,re,copy
def rep(x,a,b,n=1):
    c=x.count(a); assert c==n,(a[:90],c,n); return x.replace(a,b)
esc=lambda s: s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def load(p):
    z=zipfile.ZipFile(p); infos=z.infolist(); files={i.filename:z.read(i.filename) for i in infos}; z.close(); return infos,files
def save(p,infos,files):
    zo=zipfile.ZipFile(p,'w',zipfile.ZIP_DEFLATED)
    for i in infos: zo.writestr(i,files[i.filename])
    zo.close()
def settexts(xml,texts):
    ts=list(re.finditer(r'<w:t(?: [^>]*)?>([^<]*)</w:t>',xml)); assert len(ts)==len(texts),(len(ts),len(texts))
    out=xml
    for m,t in reversed(list(zip(ts,texts))):
        out=out[:m.start()]+'<w:t xml:space="preserve">'+esc(t)+'</w:t>'+out[m.end():]
    return out
NINE='9A'
# ---------------- 9A ----------------
p9='2026-10_SECOND_AMENDED_9A_FINAL.docx'; infos,files=load(p9); x=files['word/document.xml'].decode()
# capture the 35-row table for the letter, then collapse to 3 rows
i=x.find('>No.<'); ts=x.rfind('<w:tbl>',0,i); te=x.find('</w:tbl>',i)+8; tbl=x[ts:te]
rows=re.findall(r'<w:tr>.*?</w:tr>',tbl,re.S); assert len(rows)==36
index_tbl=tbl
hdr=rows[0]; hdr3=settexts(hdr,['No.','Date or date range','Title','Description'])
tmpl=rows[1]
R3=[['1','18 July 2023 to 18 June 2024; context from 6 June 2023','The conditions in which the work was carried on',
     'Database access removed and not restored; changes to process made effective the day they were notified, with no listed record of consultation; emergency calls misdirected and a directory entry not corrected; fixed office hours not stated for approximately nine months, and the written request for them met with a request to retract. Particulars 1(a) to 1(l); causal particulars 1(b), 1(d), 1(f) to 1(h), 1(k) and 1(l).'],
    ['2','9 February to 5 June 2024; later correction to 2 July 2025','Remuneration',
     'Pay wrong in four fortnights; Payroll\'s direction of 3 May 2024 not actioned at 13 May, still awaited on 21 May, lodged 28 May and recorded "Part Completed"; a paid leave request declined twice, with the Respondent acknowledging that the attachments were present. Particulars 2(a) to 2(o); causal particulars 2(a) to 2(j) and 2(l) to 2(n).'],
    ['3','17 March to 20 May 2024; context from 7 August 2023','The roster and fatigue',
     'A seven-hour break rostered in that role against a minimum of ten hours, or eight by written agreement, with no staff-initiated swap alleged; sick leave the next day; the fatigue enquiry answered after 23 days with a refusal; the roster decision recorded on 10 May 2024; no fatigue risk management at the Switchboard before 30 June 2024; and the Respondent\'s own review finding that the rostering was unreasonable management action. Particulars 3(a) to 3(h); causal particulars 3(b) to 3(h).']]
new_rows=[hdr3]+[settexts(tmpl,r) for r in R3]
pre=tbl[:tbl.find('<w:tr>')]; post=tbl[tbl.rfind('</w:tr>')+7:]
x=x[:ts]+pre+''.join(new_rows)+post+x[te:]
# list intro
x=rep(x,'List of stressors and dated particulars. </w:t>','List of stressors. </w:t>')
x=rep(x,'WC/2024/227 - Cory Lea Shepherd v Workers\' Compensation Regulator. The list identifies the individual events and issues under the three themes for the purposes of Part 4.8 of the Workers\' Compensation Appeal Guide. Descriptions identify material already pleaded as context only or as later evidence; those entries do not add causes of injury.',
       esc('WC/2024/227 - Cory Lea Shepherd v Workers\' Compensation Regulator. Set out for the purposes of Part 4.8 of the Workers\' Compensation Appeal Guide. There are three stressors. Each is pleaded below by dated particulars, lettered in date order; the causal particulars are identified at the head of each stressor, and the other particulars are context. An index of the particulars is at Part 3 of the Schedule enclosed with the Appellant\'s letter; it adds no stressor.'))
# 1(j) to context
x=rep(x,'The causal particulars are 1(b), 1(d), 1(f) to 1(h), and 1(j) to 1(l). Particulars 1(a), 1(c), 1(e) and 1(i) preserve','The causal particulars are 1(b), 1(d), 1(f) to 1(h), 1(k) and 1(l). Particulars 1(a), 1(c), 1(e), 1(i) and 1(j) preserve')
x=rep(x,'The matters at 1(a), 1(c), 1(e) and 1(i), and at paragraph 3 below','The matters at 1(a), 1(c), 1(e), 1(i) and 1(j), and at paragraph 3 below')
x=rep(x,'are those at 1(b), 1(d), 1(f) to 1(h), and 1(j) to 1(l),','are those at 1(b), 1(d), 1(f) to 1(h), 1(k) and 1(l),')
x=rep(x,'1(j) On-call roster and absence notification instructions (13 to 15 May 2024). ','1(j) On-call roster and absence notification instructions - context only (13 to 15 May 2024). ')
# 3(a) to context
x=rep(x,'The seven-hour roster is relied on even if the eight-hour agreement applied.','The seven-hour roster is relied on even if the eight-hour agreement applied. The causal particulars are 3(b) to 3(h). Particular 3(a) is pleaded as context, not as a separate cause.')
m=re.search(r'3\(a\) Earlier roster error and proposed roster \(7 August to 4 September 2023\)\. ',x); assert m
x=rep(x,'3(a) Earlier roster error and proposed roster (7 August to 4 September 2023). ','3(a) Earlier roster error and proposed roster - context only (7 August to 4 September 2023). ')
# Part D back to Part B.2 circumstances
x=rep(x,'Which of the particulars in the list of stressors, and the circumstances pleaded in Part B.2, are management action','Which of the circumstances pleaded in Part B.2 are management action')
x=rep(x,'In respect of each particular or circumstance that is management action, was that action reasonable','In respect of those circumstances that are management action, was that action reasonable')
# C.11 after C.10's particulars paragraph
k=x.find('Particulars: paragraphs 238, 295, 300 to 303 of the notice to admit facts served 28 August 2026, admitted 8 September 2026.'); assert k>0
ke=x.find('</w:p>',k)+6
c11=('<w:p><w:pPr><w:spacing w:before="0" w:after="100" w:line="264" w:lineRule="auto"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:b/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:t xml:space="preserve">11. </w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:b w:val="0"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:t>'
   +esc('The particulars on which the Respondent\'s notified evidence gives no account. Read with paragraph 5A, the Respondent\'s outlines of 24 September 2026 give no account of the dated events at Stressor 1(b), 1(f), 1(h) and 1(k), or at Stressor 3(e) to 3(h). As to Stressor 3(b), they describe the seven-hour break as "the result of human error" and, on the advice returned within payroll, "a rostering practice issue for the line manager". As to Stressor 2(b), they describe the second decline as one that "appears to have been made in error". On those particulars the facts are admitted, and the questions are whether each was management action, whether any management action was reasonable and taken in a reasonable way, and whether it contributed to the injury.')
   +'</w:t></w:r></w:p>')
x=x[:ke]+c11+x[ke:]
files['word/document.xml']=x.encode(); save(p9,infos,files)

# ---------------- Letter ----------------
pl='2026-10_LETTER_to_Registry_FINAL.docx'; infos,files=load(pl); y=files['word/document.xml'].decode()
# remove old s32(5) paragraph
m=re.search(r'<w:p>(?:(?!</w:p>).)*?The Respondent\'s section 32\(5\) contention\. (?:(?!</w:p>).)*?</w:p>',y,re.S); assert m; y=y[:m.start()]+y[m.end():]
# Direction 5 date line
y=rep(y,'and asks that the application below be dealt with at or before it.','and asks that the application below be dealt with at or before it. This election is made on 1 October 2026, the day after the time for the Respondent\'s list of witnesses, outlines of evidence and expert reports under directions 3 and 4 expired.')
# four-point block after "The Respondent's evidence."
a='are those of the treating practitioners (items 7 to 11).</w:t></w:r></w:p>'
assert y.count(a)==1; e=y.find(a)+len(a)
def lp(label,body): return ('<w:p><w:pPr><w:spacing w:before="0" w:after="80" w:line="264" w:lineRule="auto"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:b/><w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr><w:t xml:space="preserve">'+esc(label)+'</w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr><w:t xml:space="preserve">'+esc(body)+'</w:t></w:r></w:p>')
block=lp('The Respondent\'s notified case as at 30 September 2026. ',
 '(1) Its review decision of 24 October 2024 found that the Appellant sustained a personal injury of a psychological nature, arising out of employment to the extent it arose out of factors 2, 3 and 4, where employment was a significant contributing factor (facts 261 and 262); the claim was rejected under section 32(5). (2) Paragraph 27 of its amended statement of facts and contentions, which contends that any management action was reasonable management action taken in a reasonable way, does not identify the management action relied upon; that was admitted on 8 September 2026 (fact 303). (3) It has named no medical or expert witness and served no expert report. (4) Its outlines of evidence state that the seven-hour break of 17 to 18 March 2024 was "the result of human error" and, on the advice returned within payroll, "a rostering practice issue for the line manager"; and that the second decline of the paid Special Pandemic Leave request "appears to have been made in error". The Appellant asks that, at the opening of the conference, the Respondent be asked to state its position on paragraph 27 in light of those matters: whether it maintains it, will particularise it, or seeks time (items 2 and 5 of the election).')
y=y[:e]+block+y[e:]
# documents paragraph mentions Part 3
y=rep(y,'Part 2 lists the other documents the pleading relies on.','Part 2 lists the other documents the pleading relies on; Part 3 indexes the dated particulars of the Second Amended Form 9A and adds no stressor.')
# page counts that can no longer be verified
y=rep(y,'The combined package is 33 pages.','The combined package exceeds 30 pages.')
y=rep(y,'This letter accompanies the Appellant\'s election and requested directions (one page). Enclosure: Second Amended Statement of Facts and Contentions (Form 9A), 27 pages.','This letter accompanies the Appellant\'s election and requested directions. Enclosure: Second Amended Statement of Facts and Contentions (Form 9A).')
# Schedule Part 3: the index table, context marked
idx=index_tbl
idx=rep(idx,'>Event or issue<','>Particular<')
idx=rep(idx,'>Roster circulated on the first day of the fortnight it covered; notification of unavailability channelled through the manager from 14 May.<','>Roster circulated on the first day of the fortnight it covered; notification of unavailability channelled through the manager from 14 May; context only.<')
r3a=[r for r in re.findall(r'<w:tr>.*?</w:tr>',idx,re.S) if re.sub(r'<[^>]+>','',r).startswith('3(a)')][0]
last_t=list(re.finditer(r'<w:t(?: [^>]*)?>([^<]*)</w:t>',r3a))[-1]
nr=r3a[:last_t.start()]+'<w:t xml:space="preserve">'+esc(last_t.group(1).rstrip('.')+'; context only.')+'</w:t>'+r3a[last_t.end():]
idx=idx.replace(r3a,nr)
head=lp('Schedule, Part 3: index of the dated particulars in the Second Amended Form 9A (index only; not additional stressors). ',
 'The three stressors are pleaded, with their particulars, in the Second Amended Form 9A; this index adds no stressor or particular. The causal particulars are 1(b), 1(d), 1(f) to 1(h), 1(k) and 1(l); 2(a) to 2(j) and 2(l) to 2(n); and 3(b) to 3(h). The others, 1(a), 1(c), 1(e), 1(i), 1(j), 2(k), 2(o) and 3(a), are context and are not relied on as separate causes.')
sp=y.rfind('<w:sectPr>'); assert sp>0
y=y[:sp]+head+idx+'<w:p/>'+y[sp:]
files['word/document.xml']=y.encode(); save(pl,infos,files)

# ---------------- Election ----------------
pe='2026-10_REQUEST_election_and_directions_FINAL.docx'; infos,files=load(pe); z=files['word/document.xml'].decode()
z=rep(z,'at which the directions requested at 2 to 4 below may be dealt with','at which the directions requested at 2 to 6 below may be dealt with')
# rewrite the particulars item (currently 4)
z=rep(z,'That the Respondent state, for each particular in the list of stressors in the Second Amended Form 9A,','That the Respondent state, for each causal particular in the Second Amended Form 9A,')
z=rep(z,' whether it contends that the particular was management action and, if so, the facts on which it relies to say that the action was reasonable and taken in a reasonable way, by the date fixed for any amended statement of facts and contentions under 5 below. Paragraph 27 of its amended statement of 13 May 2026 does not identify the management action relied upon (fact 303, admitted 8 September 2026).',
        esc(' namely 1(b), 1(d), 1(f) to 1(h), 1(k) and 1(l); 2(a) to 2(j) and 2(l) to 2(n); and 3(b) to 3(h), whether it contends that the particular was management action and, if so, the facts on which it relies to say that the action was reasonable and taken in a reasonable way, by the date fixed for any amended statement of facts and contentions under 6 below. The other particulars are context, and no answer is sought on them.'))
# insert new item 2 after item 1
paras=list(re.finditer(r'<w:p>.*?</w:p>',z,re.S))
i1=[m for m in paras if 'That the appeal be listed for a second conference' in m.group(0)][0]
item2_src=[m for m in paras if 'That the Respondent state, for each causal particular' in m.group(0)][0].group(0)
item2=re.sub(r'<w:t>\d\.</w:t>','<w:t>2.</w:t>',item2_src,count=1)
runs=re.findall(r'<w:r>.*?</w:r>',item2,re.S); assert len(runs)==3
item2=item2.replace(runs[1],re.sub(r'<w:t[^>]*>.*?</w:t>','<w:t>'+esc('That, at the opening of the conference, the Respondent state whether it maintains the contention in paragraph 27 of its amended statement of facts and contentions of 13 May 2026,')+'</w:t>',runs[1],flags=re.S))
item2=item2.replace(runs[2],re.sub(r'<w:t[^>]*>.*?</w:t>','<w:t xml:space="preserve">'+esc(' having regard to its notified case as at 30 September 2026: (a) its review decision found that the Appellant sustained a personal injury of a psychological nature and that employment was a significant contributing factor, to the extent stated, and the claim was rejected under section 32(5) (facts 261 and 262); (b) paragraph 27 does not identify the management action relied upon (fact 303, admitted 8 September 2026); (c) it has named no medical or expert witness and served no expert report; and (d) its outlines of evidence describe the seven-hour break of 17 to 18 March 2024 as "the result of human error" and "a rostering practice issue for the line manager", and the second decline of the paid Special Pandemic Leave request as one that "appears to have been made in error"; and, if it maintains the contention, that it either particularise it under 5 below or be confined at any hearing to the explanations in its outlines of evidence.')+'</w:t>',runs[2],flags=re.S))
z=z[:i1.end()]+item2+z[i1.end():]
# renumber all items in document order 1..7
nums=list(re.finditer(r'<w:t>(\d)\.</w:t>',z)); assert len(nums)==7,len(nums)
for n,m in reversed(list(enumerate(nums,1))): z=z[:m.start()]+'<w:t>%d.</w:t>'%n+z[m.end():]
# enclosure note without unverifiable counts
z=rep(z,'with the schedule of the documents relied on and their status (five pages in all); and the Second Amended Statement of Facts and Contentions (Form 9A) (27 pages).','with the schedule of the documents relied on and their status and an index of the particulars; and the Second Amended Statement of Facts and Contentions (Form 9A).')
files['word/document.xml']=z.encode(); save(pe,infos,files)
print('done')
