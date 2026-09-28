"""Finalise WC/2024/227 (v3): three separate documents — Second Amended 9A, Registry letter + schedule, election/request page.
Source of the 9A text: the previous FINAL DOCX (paragraph structure parsed by formatting signature) + the explicit edits below.
"""
import json,re,sys,zipfile,os,html
from xml.sax.saxutils import escape
SP='/tmp/claude-0/-home-user/6625dff5-a18f-544c-a62c-8ea1e8b9d28c/scratchpad'
V2=SP+'/before/2026-10_SECOND_AMENDED_9A_FINAL.docx'   # template (header/settings) and text source
OUT_DOCX='2026-10_SECOND_AMENDED_9A_FINAL.docx'
OUT_PDF='2026-10_SECOND_AMENDED_9A_FINAL.pdf'
LET_PDF='2026-10_LETTER_to_Registry_FINAL.pdf'
LET_DOCX='2026-10_LETTER_to_Registry_FINAL.docx'
REQ_PDF='2026-10_REQUEST_election_and_directions_FINAL.pdf'
REQ_DOCX='2026-10_REQUEST_election_and_directions_FINAL.docx'

# ---------- 1. load blocks from the previous FINAL docx ----------
x=zipfile.ZipFile(V2).read('word/document.xml').decode()
body=x[x.index('<w:body>'):]
T=lambda s: html.unescape(''.join(re.findall(r'<w:t(?: [^>]*)?>(.*?)</w:t>',s,flags=re.S)))
items=re.findall(r'(<w:tbl>.*?</w:tbl>|<w:p>.*?</w:p>|<w:p/>)',body,flags=re.S)
blocks=[]
for k,it in enumerate(items):
    if it.startswith('<w:tbl>'):
        rows=[[T(c) for c in re.findall(r'<w:tc>.*?</w:tc>',r,flags=re.S)] for r in re.findall(r'<w:tr(?:>|<w:trPr>).*?</w:tr>',it,flags=re.S)]
        blocks.append({'k':k,'kind':'table','rows':rows,'label':'','body':' '.join(' '.join(r) for r in rows),'pb':False}); continue
    ppr=re.search(r'<w:pPr>(.*?)</w:pPr>',it,flags=re.S); ppr=ppr.group(1) if ppr else ''
    rr=[]
    for r in re.findall(r'<w:r>(.*?)</w:r>',it,flags=re.S):
        if '<w:br/>' in r: rr.append({'t':'\n','b':False}); continue
        rr.append({'t':T(r),'b':'<w:b/>' in r,'sz':(re.search(r'<w:sz w:val="(\d+)"',r) or [None,None])[1]})
    text=''.join(r['t'] for r in rr); sz=rr[0].get('sz') if rr else None
    if not text.strip(): continue
    if 'w:fill="F2F2F2"' in ppr: kind='callout'
    elif 'w:fill="E9E9E9"' in ppr: kind='stressor'
    elif 'pBdr><w:bottom' in ppr: kind='part'
    elif '<w:ind ' in ppr: kind='particulars'
    elif '<w:jc w:val="center"/>' in ppr: kind='title' if sz=='28' else 'subtitle'
    elif '\n' in text: kind='signature'
    elif sz=='22' and rr[0]['b'] and len(rr)==1: kind='section'
    else: kind='body'
    label=rr[0]['t'].strip() if kind in('body','callout') and rr[0]['b'] and len(rr)>1 else ''
    bodytxt=text[len(rr[0]['t']):].strip() if label else text.strip()
    b={'k':k,'kind':kind,'label':label,'body':bodytxt,'pb':'pageBreakBefore' in ppr}
    if kind=='signature': b['lines']=[l.strip() for l in text.split('\n') if l.strip()]
    blocks.append(b)
print('loaded',len(blocks),'blocks')

# ---------- 1b. the edits (each asserted against the exact current text) ----------
def find(pred):
    m=[b for b in blocks if b['kind']!='table' and pred(b)]
    assert len(m)==1, ('expected exactly one block', len(m))
    return m[0]
def sub(b,old,new):
    assert b['body'].count(old)==1, ('old text not found exactly once', old[:60])
    b['body']=b['body'].replace(old,new)
# E1  1.3 — "renews a referral" -> "referred"
b13=find(lambda b: b['label'].startswith('1.3 '))
sub(b13,'renews a referral to a psychiatrist, Dr Amini,','referred the Appellant to a psychiatrist, Dr Amini,')
# E2  1.6 — name the treating psychiatrist
b16=find(lambda b: b['label'].startswith('1.6 '))
sub(b16,'the treating psychiatrist told the Appellant,','the treating psychiatrist, Dr Ravikumar Bangalore Krishnaiah, told the Appellant,')
# E3  (withdrawn on instruction 27 Sep 2026: no aggravation plea; the injury is pleaded under s 32(1) only)
# E4  B.4 table — restore the 15 May 1:15 pm request row (antecedent of the two "That request" rows)
tb=[b for b in blocks if b['kind']=='table']; assert len(tb)==1; tb=tb[0]
rows=tb['rows']; assert rows[0]==['Interval','Length','Where pleaded','Facts'], rows[0]
pos=[i for i,r in enumerate(rows) if r[0].startswith('That request to the hours being stated')]; assert len(pos)==1; pos=pos[0]
assert rows[pos-1][0].startswith('The shift of 9 February 2024'), rows[pos-1][0]
assert not any('1:15 pm' in r[0] for r in rows)
rows.insert(pos,["The Appellant's request for the Manager's office hours, 15 May 2024 at 1:15 pm, to the Director's request to retract it, 6:23 pm the same day",'5 hours, 8 minutes','Stressor 1(i)','¶¶ 74, 76'])
tb['body']=' '.join(' '.join(r) for r in rows)
# E4b particulars under the table — add 76
pt=find(lambda b: b['kind']=='particulars' and b['body'].startswith('Particulars: paragraphs 55, 62 to 64, 73 to 74, 79, 81,'))
sub(pt,'73 to 74, 79, 81,','73 to 74, 76, 79, 81,')
# E5  Part F.3 — condensed
f3=find(lambda b: b['label'].startswith('3. The Appellant will contend that the amounts under section 191(2)(a)') or b['body'].startswith('The Appellant will contend that the amounts under section 191(2)(a)') or (b['label']=='3.' and 'section 191(2)(a) are inadequate' in b['body']))
old_f3=(f3['label']+' '+f3['body']).strip()
assert '1.5 times' in old_f3 and 'section 191(3)' in old_f3, old_f3[:80]
f3['label']='3.'
f3['body']=("The Appellant will contend that the amounts under section 191(2)(a) are inadequate and will seek, for any period in which he is legally represented, "
 "up to 1.5 times those amounts under section 191(3), having regard to the work involved (a record of 303 facts, 298 of them admitted; the documents at Annexure A to the notice to admit; "
 "non-party disclosure under rule 64G; two notices to admit facts and a notice to admit documents; and the four outlines served by the Respondent) and to the importance, difficulty and complexity "
 "of an appeal about a psychological injury under section 32(5)(a), which requires each pleaded circumstance to be classified, each management action assessed for reasonableness, and the whole weighed.")
print('F.3 words: before',len(old_f3.split()),'after',len((f3['label']+' '+f3['body']).split()))

def ins_after(pred,text):
    idx=[i for i,b in enumerate(blocks) if b['kind']!='table' and pred(b)]
    assert len(idx)==1, ('anchor not unique', len(idx))
    blocks.insert(idx[0]+1,{'k':None,'kind':'body','label':'','body':text,'pb':False})
def app(pred,text,must_end=None):
    b=find(pred)
    if must_end: assert b['body'].endswith(must_end), b['body'][-80:]
    b['body']=b['body'].rstrip()+' '+text
# E6 Part A — the statutory basis stated
app(lambda b: b['label'].startswith('Appellant: Cory Lea Shepherd') or b['body'].startswith('Appellant: Cory Lea Shepherd'),
    'The injury arose out of, or in the course of, that employment, and the employment was a significant contributing factor to it: section 32(1) of the Act.',
    must_end='not from a single event on that day.')
# E7 each stressor starts on a new page
for b in blocks:
    if b['kind']=='stressor': b['pb']=True
# E8 Stressor 1(k): the rostering concern recurred (facts from 3(a),(b))
ins_after(lambda b: b['body'].startswith('On 8 August 2023 he had confirmed that he would work the replacement shift'),
 'The rostering concern raised in August 2023 recurred, and the employer\'s own documents record it. On 26 April 2024 the Director wrote that the Manager "was working to fix this error" [¶¶ 211 to 212]; on 10 May 2024 she wrote to Human Resources that the Appellant\'s concern was about how the Manager was rostering the team and its effect on staff fatigue [¶ 218], acknowledged "a few rostering errors made by Chloe with regards to Cory\'s line in past rosters" [¶ 220], and stated that his roster would not be considered [¶ 221]; and on 18 February 2026 the Respondent admitted that the Director stated on 7 August 2023 that there had been a rostering error that was accidentally made [¶ 287]. These facts are pleaded at Stressor 3(a) and (b) and are repeated here because they bear on this stressor.')
# E9 Stressor 1(l): who submitted claims; the two pleaded errors
ins_after(lambda b: b['body'].startswith('So the request was made on 20 February 2024 and finally approved on 1 March 2024'),
 'Two matters are repeated here from Stressors 2 and 3. The myHR submissions report records the Manager as the initiator of each of the five Attendance Variation and Allowance Claims made for the Appellant between 1 February and 31 May 2024, and the Appellant as the initiator of none [¶¶ 198 to 201]; the special pandemic leave request was the submission he was required to make himself [¶¶ 132, 140 to 142]. The Respondent pleads human error in the handling of that request [¶¶ 133 to 135] and human error in the rostering of 17 and 18 March 2024 [¶ 226], events less than a month apart.')
# E10 Stressor 1(m): Payroll's direction unactioned (facts from 2(c),(e))
ins_after(lambda b: b['body'].startswith('The Respondent does not allege that any fatigue risk assessment was conducted, that any fatigue risk management training was provided'),
 'Payroll\'s direction of 3 May 2024 to correct four fortnights had not been actioned on 13 May [¶¶ 192 to 193] and was still awaited on 21 May [¶¶ 194 to 195]; that sequence is pleaded at Stressor 2(c) and (e) and is repeated here as part of the conditions in which the work was carried on.')
# E11 Stressor 2(a): the function, the full-time contract, the August 2023 shift
app(lambda b: b['label'].startswith('(a) The basis of the entitlement.'),
 'The function is admitted to be critical to patient safety [¶ 289]. The Appellant moved to full-time hours from 16 October 2023 on the Manager\'s written approval [¶¶ 37 to 38], and the review decision records the employer confirming the change to his employment contract and working hours [¶¶ 18 to 20]; the contracted 76 hours a fortnight against which Payroll measured the corrections is that arrangement [¶ 189]. In August 2023 a shift not worked because of a rostering error had been replaced by an additional shift [¶¶ 28 to 29]. These facts are pleaded at Stressors 1(k) and 3(a) and are repeated here.')
# E12 Stressor 2 "So the pay sequence": the 23 days
app(lambda b: b['body'].startswith('So the pay sequence was this.'),
 'The enquiry of 8 April 2024 was also the fatigue enquiry pleaded at Stressor 3(j); no response to it is alleged between 9 April and 1 May, and it was answered after 23 days [¶¶ 249 to 250].')
# E13 Stressor 2(h): the employer's statements on complaints and procedures
app(lambda b: b['label'].startswith('(h) The Respondent\'s pleaded answer to this stressor.') and '300 to 302' in b['body'],
 'The employer\'s letter of 5 June 2026 states that there were no consequential changes to operating procedures over the period requested [¶ 266] and how employee complaints were managed [¶ 267], and the Respondent does not allege any change to the operating procedures of the Switchboard as a consequence of any employee complaint before 30 June 2024 [¶ 272]; those facts are pleaded at Stressors 1(m) and 3(l) and are repeated here.')
# E14 Stressor 3(d): the fortnight of 18 March; the function
app(lambda b: b['label'].startswith('(d) The shifts of 17 and 18 March 2024.'),
 'Payroll later recorded that the fortnight commencing 18 March 2024 had too many ordinary shifts and that one of the shifts needed to be overtime [¶ 188], as pleaded at Stressor 2(e)(i). The break was rostered in a function the Respondent admits is critical to patient safety [¶ 289].')
# E15 B.6.5 dated
b65=find(lambda b: b['label'].startswith('6.5 '))
assert b65['body'].count('No medical or expert evidence is notified.')==1
b65['body']=b65['body'].replace('No medical or expert evidence is notified.','No medical or expert evidence has been notified as at 30 September 2026.')

# ===== change 44 =====
def ins_before(pred,block):
    idx=[i for i,b in enumerate(blocks) if b['kind']!='table' and pred(b)]; assert len(idx)==1,('anchor',len(idx))
    blocks.insert(idx[0],block)
def find_body(prefix):
    return find(lambda b: (b.get('body','') or '').startswith(prefix))
# 1. s 32(5)(b): contention 5B and question 6
c5a=find(lambda b: b['label'].startswith('5A. '))
i5a=blocks.index(c5a)
blocks.insert(i5a+1,{'k':None,'kind':'body','label':'5B. Section 32(5)(b) - the injury did not arise from the Appellant\'s expectation or perception of management action.','body':'The circumstances relied on in Part B.2 are events and documents admitted by the Respondent, and the intervals between them are arithmetic on admitted dates and times. They are not the Appellant\'s expectation or perception of reasonable management action being taken against him. The Appellant contends that section 32(5)(b) has no application to the injury proved on that record.','pb':False})
q5=find(lambda b: b['label']=='5.' and (b.get('body','') or '').startswith('Does section 32(5)(a) of the Act exclude'))
blocks.insert(blocks.index(q5)+1,{'k':None,'kind':'body','label':'6.','body':'Does section 32(5)(b) of the Act exclude the injury, that is, did it arise out of, or in the course of, the Appellant\'s expectation or perception of reasonable management action being taken against him, rather than out of the admitted circumstances themselves?','pb':False})
# 2. date ranges in the stressor headings; list of stressors table before the summary
for b in blocks:
    if b['kind']=='stressor':
        if b['body'].startswith('STRESSOR 1'): b['body']='STRESSOR 1 - THE CONDITIONS IN WHICH THE WORK WAS CARRIED ON (18 JULY 2023 TO 18 JUNE 2024)'
        elif b['body'].startswith('STRESSOR 2'): b['body']='STRESSOR 2 - REMUNERATION (5 FEBRUARY 2024 TO 5 JUNE 2024; CORRECTIONS TO 2 JULY 2025)'
        elif b['body'].startswith('STRESSOR 3'): b['body']='STRESSOR 3 - THE ROSTER AND FATIGUE (7 AUGUST 2023 TO 1 MAY 2024; THE SHIFTS OF 17 AND 18 MARCH 2024)'
summ=find(lambda b: b['kind']=='callout' and b['label'].startswith('In summary'))
isum=blocks.index(summ)
blocks.insert(isum,{'k':None,'kind':'body','label':'List of stressors.','body':'Set out in the form required by Part 4.8 of the Workers\' Compensation Appeal Guide. Each stressor is pleaded in full below; the summary that follows the list gives the admissions on which each rests.','pb':False})
blocks.insert(isum+1,{'k':None,'kind':'table','label':'','pb':False,'cols':[0.06,0.20,0.20,0.54],'rows':[
 ['No.','Date or date range','Title','Description'],
 ['1','18 July 2023 to 18 June 2024','The conditions in which the work was carried on','Database access removed and not restored; changes to process effective the day they were notified, with no listed record of consultation; emergency calls misdirected and the directory not corrected; the manager\'s office hours not stated for nine months.'],
 ['2','5 February 2024 to 5 June 2024; corrections to 2 July 2025','Remuneration','Pay wrong in four fortnights; Payroll\'s direction of 3 May 2024 not actioned at 13 May, still awaited on 21 May, lodged 28 May and recorded "Part Completed"; a paid leave entitlement declined twice on attachments the Respondent admits were present.'],
 ['3','7 August 2023 to 1 May 2024; the shifts of 17 and 18 March 2024','The roster and fatigue','A seven-hour break rostered in that role against a minimum of ten hours, or eight by an agreement applying only to staff-initiated swaps; the fatigue enquiry answered after 23 days with a refusal; no fatigue risk management at the Switchboard before 30 June 2024; the Respondent\'s own review finding of unreasonable management action.']]})
blocks[isum+1]['body']=' '.join(' '.join(r) for r in blocks[isum+1]['rows'])
# 3. worker within s 11, Part A
pa=find(lambda b: (b.get('body','') or '').startswith('Appellant: Cory Lea Shepherd'))
sub(pa,'classification AO3, a continuous shift working role. [¶¶ 1 to 4, 13]','classification AO3, a continuous shift working role. [¶¶ 1 to 4, 13] The Appellant was a worker within the meaning of section 11 of the Act.')
# 4. B.1: section title; 1.6 wording; 1.7+1.8 merged; 1.9 moved to 3.1; renumber; cross-references
sec1=find(lambda b: b['kind']=='section' and (b.get('body','') or '').startswith('1. The starting point'))
sec1['body']='1. The starting point - the role, and the medical record'
b16=find(lambda b: b['label'].startswith('1.6 '))
sub(b16,'it records how the injury certified as anxiety and stress on 1 July 2024 had become a depressive disorder by 24 October 2024.','it records the diagnosis made on 24 October 2024 of the condition first certified on 1 July 2024.')
b17=find(lambda b: b['label'].startswith('1.7 ')); b18=find(lambda b: b['label'].startswith('1.8 ')); b19=find(lambda b: b['label'].startswith('1.9 '))
b17['label']='1.7 The report of 13 February 2025, its footer, and the author\'s position.'
b17['body']=('Diagnosis: Major Depressive Disorder with anxious distress (DSM-5 296.23). The report states the severity, the effect on functioning and the treatment (fluoxetine increased to three capsules daily; quetiapine 25 mg at night). '
 'The treating clinician records the origin as "workplace stress stemming from issues with management and rostering", records that pay was "withheld or delayed for up to five months at a time" as a source of financial stress, and states that "premature exposure to the workplace is more likely result in significant deterioration". [Tab M4; Respondent\'s item 10.] '
 'The stressors recorded in that report match matters admitted on 8 September 2026: management and rostering, and the night-shift line; the shorter break; and pay withheld or delayed from the 5 February 2024 fortnight, uncorrected at 13 May, "claims older than 3 months" on 28 May, a claim effective 30 March recorded "Part Completed" on 30 May, and the two February claims absent from the myHR report. '
 'The report bears a footer reading "for the only reason of clinical information and not for medico-legal use". The author\'s emails of 5 and 8 September 2026 state of his records "You can use them according to the need to support your legal issues", and identify the report of 13 February 2025 as "the report that captures the relevant information you have requested" on the matters in issue. [Tab M5.] '
 'The report is not relied on to say which of the individual events pleaded at Part B.2 caused the injury, or how much each contributed. Nothing after 24 October 2024 is relied on as a cause of the injury.')
# particulars block sits after 1.7 already; remove 1.8 and 1.9 blocks
blocks.remove(b18); blocks.remove(b19)
b31=find(lambda b: b['label'].startswith('3.1 '))
b31['body']=b31['body'].rstrip()+' The Employee Capability Checklist completed by Dr Day Hong Ma on 3 July 2026 records current capacity and restrictions and the continuing effect of the injury, including "symptom exacerbation on exposure to the identified workplace stressors" [Tab M7]; it is relied on for the effect of the injury and for capacity only, not for cause.'
b110=find(lambda b: b['label'].startswith('1.10 ')); b110['label']='1.8 '+b110['label'][5:]
b111=find(lambda b: b['label'].startswith('1.11 ')); b111['label']='1.9 '+b111['label'][5:]
b12=find(lambda b: b['label'].startswith('1.2 ')); sub(b12,'(paragraph 1.10)','(paragraph 1.8)')
f2=find(lambda b: b['label']=='2.' and 'section 191(2): (a)' in (b.get('body','') or '')); sub(f2,'paragraph B.1.11','paragraph B.1.9')
# the s 32(1) "not the only one" sentence: leave in 1.2 (it is one sentence) and make sure Part C.3 carries it
c3=find(lambda b: b['label'].startswith('3. Injury under section 32(1)'))
if 'not the only one' not in c3['body']: c3['body']=c3['body'].rstrip()+' Section 32(1) requires that employment be a significant contributing factor, not the only one.'
# 5. 1(g) call-load sentence qualified
g=find_body('The console took about 270 to 440 calls on an eight-hour shift')
g['body']='In April 2025 the console took between 269 and 444 calls on an eight-hour shift (Stressor 3(h)(v) below); the Appellant\'s evidence is that the load in May 2024 was of the same order. Emergency codes were received and paged through it throughout the day (Stressor 3(h)).'
# 6. 3(h)(iv) condensed; guideline definitions paragraph condensed
hiv=find(lambda b: b['label'].startswith('(h)(iv)'))
hiv['body']='Sick leave of 7.60 hours was taken that day. [¶ 235] The register records sixteen codes on 19 March 2024, six of them between 06:00 and 14:00: a Paediatric MET call, a simulation, and four adult MET calls, one of which, at 11:34 to Ward 2I bed 20, is annotated "CALLED VIA SWITRCHBOARD" [sic].'
d178=find_body('The guideline defines fatigue as')
d178['body']='The guideline defines fatigue as "A state of impaired physical and/or mental performance and lowered alertness arising as a result or combination of physical and mental work, health and psychosocial factors or inadequate restorative sleep", a fatigue risk management system as "An integrated set of management practices and procedures for monitoring and managing the risks posed to health, safety and wellbeing by fatigue", and "Defences in depth" as a "Hazard identification and risk control model that applies a series of layered mechanisms to minimise the occurrence of fatigue related incidents". [Guideline, glossary, p 29]'
# 7. Stressor 2 medical link: the eight words
ml2=find(lambda b: b['kind']=='callout' and b['label'].startswith('The medical link - Stressor 2'))
sub(ml2,"Tab M4 records the treating psychiatrist's later history of delayed pay as a source of financial stress.","Tab M4 records the treating psychiatrist's later history that pay was \"withheld or delayed for up to five months at a time\", as a source of financial stress.")
print('change 44 edits applied; blocks now',len(blocks))
for b in blocks:
    if b['kind']=='body' and b['body'].startswith('Dated:'): b['body']='Dated: 30 September 2026'
final=blocks
banned=['reprisal','retaliat','suppress','fraud','conspir','hostile','punish','capricious','will give evidence','$']
alltext=' '.join((b['label']+' '+b['body']) for b in final)
print('banned words present:',[w for w in banned if w.lower() in alltext.lower()])
json.dump(final,open(SP+'/final_blocks_v3.json','w'),indent=0)

# ---------- 2. DOCX ----------
def E(s): return escape(s).replace('"','&quot;')
def run(t,b=False,i=False,sz=20):
    return f'<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>{"<w:b/>" if b else ""}{"<w:i/>" if i else ""}<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/></w:rPr><w:t xml:space="preserve">{E(t)}</w:t></w:r>'
def P(ppr,runs): return f'<w:p><w:pPr>{ppr}</w:pPr>{runs}</w:p>'
LINE='<w:spacing w:before="{b}" w:after="{a}" w:line="264" w:lineRule="auto"/>'
BOX='<w:pBdr><w:top w:val="single" w:sz="4" w:space="4" w:color="BFBFBF"/><w:left w:val="single" w:sz="4" w:space="4" w:color="BFBFBF"/><w:bottom w:val="single" w:sz="4" w:space="4" w:color="BFBFBF"/><w:right w:val="single" w:sz="4" w:space="4" w:color="BFBFBF"/></w:pBdr>'
def docx_par(b):
    k=b['kind']
    if k=='title': return P(LINE.format(b=0,a=80)+'<w:jc w:val="center"/>',run(b['body'],True,sz=28))
    if k=='subtitle': return P(LINE.format(b=0,a=200)+'<w:jc w:val="center"/>',run(b['body'],sz=18))
    if k=='part':
        pb='<w:pageBreakBefore/>' if b['pb'] else ''
        return P('<w:keepNext/>'+pb+'<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="808080"/></w:pBdr>'+LINE.format(b=240,a=100),run(b['body'],True,sz=24))
    if k=='stressor': return P('<w:keepNext/>'+('<w:pageBreakBefore/>' if b.get('pb') else '')+'<w:shd w:val="clear" w:color="auto" w:fill="E9E9E9"/>'+LINE.format(b=0 if b.get('pb') else 200,a=100),run(b['body'],True,sz=22))
    if k=='section': return P('<w:keepNext/>'+LINE.format(b=180,a=80),run(b['body'],True,sz=22))
    if k=='callout':
        rr=(run(b['label']+' ',True) if b['label'] else '')+run(b['body'])
        return P(BOX+'<w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/>'+LINE.format(b=80,a=140),rr)
    if k=='particulars': return P(LINE.format(b=0,a=100)+'<w:ind w:left="284"/>',run(b['body'],i=True,sz=18))
    if k=='table':
        def tc(txt,bold=False,shade=None):
            sh=f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>' if shade else ''
            return f'<w:tc><w:tcPr>{sh}</w:tcPr><w:p><w:pPr><w:spacing w:after="0"/></w:pPr>{run(txt,bold,sz=17)}</w:p></w:tc>'
        rows=['<w:tr><w:trPr><w:tblHeader/></w:trPr>'+''.join(tc(c,True,'E9E9E9') for c in b['rows'][0])+'</w:tr>']
        for r in b['rows'][1:]: rows.append('<w:tr>'+''.join(tc(c) for c in r)+'</w:tr>')
        grid='<w:tblGrid>'+''.join(f'<w:gridCol w:w="{int(9638*f)}"/>' for f in (b.get('cols') or [0.49,0.20,0.17,0.14]))+'</w:tblGrid>'
        return '<w:tbl><w:tblPr><w:tblW w:w="9638" w:type="dxa"/><w:tblBorders><w:top w:val="single" w:sz="4"/><w:left w:val="single" w:sz="4"/><w:bottom w:val="single" w:sz="4"/><w:right w:val="single" w:sz="4"/><w:insideH w:val="single" w:sz="4"/><w:insideV w:val="single" w:sz="4"/></w:tblBorders></w:tblPr>'+grid+''.join(rows)+'</w:tbl><w:p><w:pPr><w:spacing w:after="60"/></w:pPr></w:p>'
    if k=='signature':
        rr=run(b['lines'][0],True)+'<w:r><w:br/></w:r>'+run(b['lines'][1])
        return P(LINE.format(b=120,a=80),rr)
    rr=(run(b['label']+' ',True) if b['label'] else '')+run(b['body'])
    return P(LINE.format(b=0,a=100),rr)
src=zipfile.ZipFile(V2)
docxml=src.read('word/document.xml').decode()
head=docxml[:docxml.index('<w:body>')+len('<w:body>')]
sect=re.search(r'<w:sectPr.*?</w:sectPr>',docxml,flags=re.S).group(0)
sect=re.sub(r'<w:pgMar[^>]*/>','<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="567" w:footer="567" w:gutter="0"/>',sect)
newxml=head+''.join(docx_par(b) for b in final)+sect+'</w:body></w:document>'
names=src.namelist(); order=['[Content_Types].xml','_rels/.rels']+sorted(n for n in names if n not in('[Content_Types].xml','_rels/.rels'))
with zipfile.ZipFile(OUT_DOCX,'w',zipfile.ZIP_DEFLATED) as z:
    for n in order:
        data=newxml.encode('utf8') if n=='word/document.xml' else src.read(n)
        if n=='word/header1.xml': data=data.replace(b'w:sz w:val="15"',b'w:sz w:val="16"')
        if n=='word/settings.xml' and b'<w:zoom ' in data and b'w:percent' not in data: data=data.replace(b'<w:zoom ',b'<w:zoom w:percent="100" ')
        z.writestr(n,data)
print('docx written',OUT_DOCX)

# ---------- 3. PDF (shared stylesheet) ----------
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
FD='/usr/share/fonts/truetype/liberation/'
pdfmetrics.registerFont(TTFont('Arial',FD+'LiberationSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold',FD+'LiberationSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Italic',FD+'LiberationSans-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Arial-BoldItalic',FD+'LiberationSans-BoldItalic.ttf'))
addMapping('Arial',0,0,'Arial');addMapping('Arial',1,0,'Arial-Bold');addMapping('Arial',0,1,'Arial-Italic');addMapping('Arial',1,1,'Arial-BoldItalic')
GREY=colors.HexColor('#808080')
ST={
 'title':ParagraphStyle('title',fontName='Arial-Bold',fontSize=14,leading=17,alignment=1,spaceAfter=4),
 'subtitle':ParagraphStyle('subtitle',fontName='Arial',fontSize=9,leading=11.5,alignment=1,spaceAfter=10),
 'part':ParagraphStyle('part',fontName='Arial-Bold',fontSize=12,leading=15,spaceBefore=12,spaceAfter=5,keepWithNext=1),
 'stressor':ParagraphStyle('stressor',fontName='Arial-Bold',fontSize=11,leading=14,spaceBefore=10,spaceAfter=5,backColor=colors.HexColor('#E9E9E9'),borderPadding=(3,3,3,3),keepWithNext=1),
 'section':ParagraphStyle('section',fontName='Arial-Bold',fontSize=11,leading=14,spaceBefore=9,spaceAfter=4,keepWithNext=1),
 'body':ParagraphStyle('body',fontName='Arial',fontSize=10,leading=12.6,spaceAfter=4.5),
 'callout':ParagraphStyle('callout',fontName='Arial',fontSize=10,leading=12.6,backColor=colors.HexColor('#F2F2F2'),borderColor=colors.HexColor('#BFBFBF'),borderWidth=0.5,borderPadding=(5,5,5,5),spaceBefore=6,spaceAfter=11,leftIndent=3,rightIndent=3),
 'particulars':ParagraphStyle('particulars',fontName='Arial-Italic',fontSize=9,leading=11.5,leftIndent=14,spaceAfter=5),
 'signature':ParagraphStyle('signature',fontName='Arial',fontSize=10,leading=13,spaceBefore=6),
}
esc=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
TC=ParagraphStyle('tc',fontName='Arial',fontSize=8.5,leading=10.5); TCB=ParagraphStyle('tcb',parent=TC,fontName='Arial-Bold')
def pdf_par(b):
    k=b['kind']
    if k=='table':
        data=[[Paragraph(esc(c),TCB) for c in b['rows'][0]]]+[[Paragraph(esc(c),TC) for c in r] for r in b['rows'][1:]]
        W=A4[0]-40*mm; fr=b.get('cols') or [0.49,0.20,0.17,0.14]; tb=Table(data,colWidths=[W*f for f in fr],repeatRows=1)
        tb.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E9E9E9')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
        return [tb,Spacer(1,6)]
    if k=='signature': return Paragraph('<b>'+esc(b['lines'][0])+'</b><br/>'+esc(b['lines'][1]),ST['signature'])
    if k=='part' and b['pb']: return [PageBreak(),Paragraph(esc(b['body']),ST['part'])]
    if k=='stressor' and b.get('pb'): return [PageBreak(),Paragraph(esc(b['body']),ST['stressor'])]
    txt=('<b>'+esc(b['label'])+'</b> ' if b['label'] else '')+esc(b['body'])
    return Paragraph(txt,ST[k])
def deco_factory(headtext):
    def deco(c,d):
        c.saveState(); c.setFont('Arial',7.5); c.setFillColor(GREY)
        c.drawString(20*mm,A4[1]-11*mm,headtext); c.drawRightString(A4[0]-20*mm,9*mm,f"Page {d.page}")
        c.setStrokeColor(colors.HexColor('#BFBFBF')); c.setLineWidth(0.4); c.line(20*mm,A4[1]-12.5*mm,A4[0]-20*mm,A4[1]-12.5*mm)
        c.restoreState()
    return deco
story=[]
for b in final:
    x=pdf_par(b); story.extend(x if isinstance(x,list) else [x])
doc=SimpleDocTemplate(OUT_PDF,pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=20*mm,bottomMargin=18*mm,title='Second Amended Form 9A WC/2024/227',author='Cory Lea Shepherd')
d=deco_factory("WC/2024/227  |  Shepherd v Workers' Compensation Regulator  |  Second Amended Statement of Facts and Contentions (Form 9A)")
doc.build(story,onFirstPage=d,onLaterPages=d)
import fitz
n9a=fitz.open(OUT_PDF).page_count; print('9A pdf pages',n9a)

# ---------- 4. Letter (same stylesheet) ----------
import importlib,letter_content as L; importlib.reload(L)
note=L.SCHEDULE_NOTE.replace('{PAGES}',str(n9a))
LB=ParagraphStyle('lb',parent=ST['body'],fontSize=9,leading=11,spaceAfter=3)
LT=ParagraphStyle('lt',fontName='Arial-Bold',fontSize=11,leading=13.5,spaceAfter=3)
LS=ParagraphStyle('ls',fontName='Arial-Bold',fontSize=9,leading=11,spaceAfter=4)
cell=ParagraphStyle('c',fontName='Arial',fontSize=8,leading=9.8); cellb=ParagraphStyle('cb',parent=cell,fontName='Arial-Bold')
S=[Paragraph(esc(L.DATE),LB)]
for l in L.TO: S.append(Paragraph(esc(l),ParagraphStyle('to',parent=LB,spaceAfter=0)))
S+= [Spacer(1,2),Paragraph(esc(L.CC),LB),Spacer(1,1),Paragraph(esc(L.TITLE),LT),Paragraph(esc(L.SUBJECT),LS)]
for b,txt in L.BODY: S.append(Paragraph('<b>'+esc(b)+'</b> '+esc(txt),LB))
S.append(Paragraph(esc(L.CLOSE[0]),LB)); S.append(Spacer(1,6)); S.append(Paragraph('<b>'+esc(L.CLOSE[1])+'</b>',LB))
S.append(PageBreak()); S.append(Paragraph(esc(L.SCHEDULE_TITLE),LT))
data=[[Paragraph(esc(h),cellb) for h in L.SCHEDULE_COLS]]
for r in L.SCHEDULE_ROWS: data.append([Paragraph(esc(str(v)),cell) for v in r])
W=A4[0]-34*mm
tbl=Table(data,colWidths=[W*0.05,W*0.36,W*0.11,W*0.10,W*0.18,W*0.20],repeatRows=1)
ts=[('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E9E9E9')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]
for i,r in enumerate(L.SCHEDULE_ROWS,start=1):
    if r[4]==L.C: ts.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#F3F7F3')))
    elif r[3]==L.D: ts.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#FBF5EE')))
tbl.setStyle(TableStyle(ts)); S.append(tbl); S.append(Spacer(1,8)); S.append(Paragraph(esc(note),LB))
docL=SimpleDocTemplate(LET_PDF,pagesize=A4,leftMargin=17*mm,rightMargin=17*mm,topMargin=16*mm,bottomMargin=14*mm,title='Letter to the Industrial Registry WC/2024/227',author='Cory Lea Shepherd')
dl=deco_factory("WC/2024/227  |  Shepherd v Workers' Compensation Regulator  |  Letter to the Industrial Registry, with schedule of documents")
docL.build(S,onFirstPage=dl,onLaterPages=dl)
nl=fitz.open(LET_PDF).page_count; print('letter pdf pages',nl)

# letter DOCX
def lrun(t,b=False,sz=19): return run(t,b,sz=sz)
def lp(text,lead='',bold=False,after=80,keep=False):
    k='<w:keepNext/>' if keep else ''
    return P(k+LINE.format(b=0,a=after),(lrun(lead+' ',True) if lead else '')+lrun(text,bold))
body=[lp(L.DATE)]+[lp(l,after=0) for l in L.TO]+[lp(''),lp(L.CC),lp(L.TITLE,bold=True),lp(L.SUBJECT,bold=True,after=120)]
for b,t in L.BODY: body.append(lp(t,lead=b))
body.append(lp(L.CLOSE[0],after=200)); body.append(lp(L.CLOSE[1],bold=True))
body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>'); body.append(lp(L.SCHEDULE_TITLE,bold=True,after=120))
def tc(t,b=False,shade=None):
    sh=f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>' if shade else ''
    return f'<w:tc><w:tcPr>{sh}</w:tcPr><w:p><w:pPr><w:spacing w:after="0"/></w:pPr>{lrun(t,b,sz=16)}</w:p></w:tc>'
rows=['<w:tr><w:trPr><w:tblHeader/></w:trPr>'+''.join(tc(h,True,'E9E9E9') for h in L.SCHEDULE_COLS)+'</w:tr>']
for r in L.SCHEDULE_ROWS:
    shade='F3F7F3' if r[4]==L.C else ('FBF5EE' if r[3]==L.D else None)
    rows.append('<w:tr>'+''.join(tc(str(v),False,shade) for v in r)+'</w:tr>')
grid='<w:tblGrid>'+''.join(f'<w:gridCol w:w="{w}"/>' for w in (480,3450,1050,960,1730,1960))+'</w:tblGrid>'
body.append('<w:tbl><w:tblPr><w:tblW w:w="9630" w:type="dxa"/><w:tblBorders><w:top w:val="single" w:sz="4"/><w:left w:val="single" w:sz="4"/><w:bottom w:val="single" w:sz="4"/><w:right w:val="single" w:sz="4"/><w:insideH w:val="single" w:sz="4"/><w:insideV w:val="single" w:sz="4"/></w:tblBorders></w:tblPr>'+grid+''.join(rows)+'</w:tbl>')
body.append(lp('')); body.append(lp(note))
ldoc=f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>{''.join(body)}<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1000" w:right="1134" w:bottom="900" w:left="1134" w:header="567" w:footer="567" w:gutter="0"/></w:sectPr></w:body></w:document>'''
ct='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>'''
rels='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>'''
with zipfile.ZipFile(LET_DOCX,'w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml',ct); z.writestr('_rels/.rels',rels); z.writestr('word/document.xml',ldoc)
print('letter docx written')

# ---------- 4b. Request page (order register) ----------
import request_content as R; importlib.reload(R)
RC=ParagraphStyle('rc',fontName='Arial',fontSize=10,leading=13,alignment=1,spaceAfter=2)
RCB=ParagraphStyle('rcb',parent=RC,fontName='Arial-Bold')
RCI=ParagraphStyle('rci',parent=RC,fontName='Arial-Italic')
RB=ParagraphStyle('rb',fontName='Arial',fontSize=10,leading=12.6,spaceAfter=5)
RN=ParagraphStyle('rn',parent=RB,leftIndent=22,firstLineIndent=-22)
Q=[Paragraph(esc(R.COURT),RCB),Paragraph(esc(R.ACT),RCI),Spacer(1,8)]
for a,b in R.PARTIES:
    Q.append(Paragraph(esc(a),RC))
    if b: Q.append(Paragraph(esc(b),RCI))
    Q.append(Spacer(1,3))
Q+=[Spacer(1,4),Paragraph(esc(R.MATTER),RCI),Spacer(1,6),Paragraph(esc(R.HEAD1),RCB),Spacer(1,3),Paragraph(esc(R.HEAD2),RCB),Spacer(1,10),Paragraph(esc(R.PREAMBLE),RB),Spacer(1,2)]
for n,(b,rest) in enumerate(R.ITEMS,1): Q.append(Paragraph(f'{n}.&nbsp;&nbsp;&nbsp;<b>{esc(b)}</b>{esc(rest)}',RN))
Q+=[Spacer(1,6),Paragraph(esc(R.NOTE.replace('{PAGES}',str(n9a))),ParagraphStyle('rnote',parent=RB,fontSize=9,leading=11.5)),Spacer(1,10),Paragraph(esc(R.DATED),RB),Spacer(1,14),Paragraph('<b>'+esc(R.SIGN[0])+'</b><br/>'+esc(R.SIGN[1]),RB)]
docR=SimpleDocTemplate(REQ_PDF,pagesize=A4,leftMargin=21*mm,rightMargin=21*mm,topMargin=18*mm,bottomMargin=16*mm,title='Election under direction 5 and directions requested WC/2024/227',author='Cory Lea Shepherd')
dr=deco_factory("WC/2024/227  |  Shepherd v Workers' Compensation Regulator  |  Election under direction 5 and directions requested")
docR.build(Q,onFirstPage=dr,onLaterPages=dr)
nr=fitz.open(REQ_PDF).page_count; print('request pdf pages',nr)
def rp(text,bold=False,italic=False,center=False,after=60,sz=20,ind=None):
    jc='<w:jc w:val="center"/>' if center else ''
    indx=f'<w:ind w:left="{ind}" w:hanging="{ind}"/>' if ind else ''
    return P(LINE.format(b=0,a=after)+indx+jc,run(text,bold,italic,sz))
RB_=[rp(R.COURT,True,center=True),rp(R.ACT,italic=True,center=True,after=160)]
for a,b in R.PARTIES:
    RB_.append(rp(a,center=True,after=0))
    if b: RB_.append(rp(b,italic=True,center=True,after=60))
RB_+=[rp(R.MATTER,italic=True,center=True,after=120),rp(R.HEAD1,True,center=True,after=60),rp(R.HEAD2,True,center=True,after=200),rp(R.PREAMBLE,after=120)]
for n,(b,rest) in enumerate(R.ITEMS,1):
    RB_.append(P(LINE.format(b=0,a=140)+'<w:ind w:left="440" w:hanging="440"/>',run(f'{n}.\t',sz=20)+run(b,True)+run(rest)))
RB_+=[rp(R.NOTE.replace('{PAGES}',str(n9a)),after=200,sz=18),rp(R.DATED,after=280),rp(R.SIGN[0],True,after=0),rp(R.SIGN[1])]
rdoc=f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>{''.join(RB_)}<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="1247" w:bottom="1000" w:left="1247" w:header="567" w:footer="567" w:gutter="0"/></w:sectPr></w:body></w:document>'''
with zipfile.ZipFile(REQ_DOCX,'w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml',ct); z.writestr('_rels/.rels',rels); z.writestr('word/document.xml',rdoc)
print('request docx written')

