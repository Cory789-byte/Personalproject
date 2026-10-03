# change 53: event-by-event architecture. Each stressor keeps its theme; every lettered item is one dated
# event or issue, in date order; analysis items become unlettered headings; nothing is removed.
import re, copy
LBL=re.compile(r'^\(([a-z])\)(?:\(([ivx]+)\))?\s+(.*)$')

def _groups(blocks, s, e):
    g={}; order=[]; cur=None
    for i in range(s+1,e):
        m=LBL.match(blocks[i]['label'] or '')
        if m:
            key=m.group(1)+('('+m.group(2)+')' if m.group(2) else '')
            cur=key; g[key]=[]; order.append(key)
        assert cur is not None, ('block before first lettered item', i, blocks[i]['body'][:60])
        g[cur].append(blocks[i])
    return g, order

def _title(b):
    return LBL.match(b['label']).group(3)

def _relabel(grp, new):          # new = '(c)' or '' (unlettered)
    grp=[copy.deepcopy(x) for x in grp]
    t=_title(grp[0]); grp[0]['label']=(new+' '+t) if new else t
    return grp

def _stressor(blocks, n):
    s=[i for i,b in enumerate(blocks) if b['kind']=='stressor' and b['body'].startswith('STRESSOR %d -'%n)]
    assert len(s)==1; s=s[0]
    e=[i for i,b in enumerate(blocks) if i>s and b['kind']=='callout' and b['label'].startswith('The medical link - Stressor %d'%n)]
    return s, e[0]

def _rebuild(blocks, n, spec):
    s,e=_stressor(blocks,n)
    g,order=_groups(blocks,s,e)
    used=[]; out=[]
    for item in spec:
        kind=item[0]
        if kind=='set' or kind=='close':
            out+= _relabel(g[item[1]],''); used.append(item[1])
        elif kind=='ev':
            new, key = item[1], item[2]
            out+= _relabel(g[key],'('+new+')'); used.append(key)
            for ch in item[3] if len(item)>3 else []:          # run-in groups merged into this event
                out+= _relabel(g[ch],''); used.append(ch)
            for ch in item[4] if len(item)>4 else []:          # child groups: ('h(i)','(e)(i)') or ('l(i)','')
                out+= _relabel(g[ch[0]],ch[1]); used.append(ch[0])
        elif kind=='block':
            out.append(item[1])
    assert sorted(used)==sorted(order), ('groups used', sorted(set(order)-set(used)), sorted(set(used)-set(order)))
    nin=sum(1 for i in range(s+1,e)); nout=sum(1 for b in out if b.get('k','x') is not None or b['kind']!='body' or b['label']!='')
    blocks[s+1:e]=out
    return s

def _sub(b, old, new, count=1):
    assert b['body'].count(old)==count, ('not found as expected', old[:70], b['body'].count(old))
    b['body']=b['body'].replace(old,new)

def _find(blocks, pred):
    m=[b for b in blocks if b['kind']!='table' and pred(b)]
    assert len(m)==1, ('expected one', len(m)); return m[0]

def apply(blocks):
    fb=lambda pre: _find(blocks, lambda b: b['body'].startswith(pre))
    # ---------- text of cross-references, fixed before the blocks move ----------
    _sub(fb('The Appellant was referred') if False else _find(blocks, lambda b: 'request to retract at Stressor 1(i)' in b['body']),'request to retract at Stressor 1(i)','request to retract at Stressor 1(b)')
    _sub(_find(blocks, lambda b:'Each of (b) to (h) below is pleaded against that duty.' in b['body']),'Each of (b) to (h) below is pleaded against that duty.','Each of (a) and (c) to (e) below is pleaded against that duty.')
    _sub(_find(blocks, lambda b:'The duty at (a) remained on the position' in b['body']),'The duty at (a) remained on the position','The duty pleaded at the head of this stressor remained on the position')
    b=_find(blocks, lambda b:'is the procedure pleaded at (c) above.' in b['body'])
    _sub(b,'is the procedure pleaded at (c) above.','is the procedure pleaded at (a) below.')
    _sub(b,'is pleaded at (g) and (h) below.','is pleaded at (d) and (e) below.')
    b=_find(blocks, lambda b:'(Stressor 3(h)(v) below)' in b['body'])
    _sub(b,'(Stressor 3(h)(v) below)','(Stressor 3(e)(v) below)'); _sub(b,'(Stressor 3(h)).','(Stressor 3(e)).')
    _sub(_find(blocks, lambda b:'These facts are pleaded at Stressor 3(a) and (b) and are repeated' in b['body']),'Stressor 3(a) and (b)','Stressor 3(b) and (h)')
    _sub(_find(blocks, lambda b:'that sequence is pleaded at Stressor 2(c) and (e)' in b['body']),'Stressor 2(c) and (e)','Stressor 2(d)')
    _sub(_find(blocks, lambda b:'asking him to retract it (p 5), pleaded at (i) above.' in b['body']),'pleaded at (i) above.','pleaded at (b) above.')
    b=_find(blocks, lambda b:'The matters at (j), (k), (l) and (n) above' in b['body'])
    _sub(b,'The matters at (j), (k), (l) and (n) above','The matters at (g) to (j) above')
    _sub(b,'The circumstances relied on as causes in Stressor 1 are those at (a) to (i) and (m).','The circumstances relied on as causes in Stressor 1 are the duty and the function pleaded at the head of this stressor, and those at (a) to (f).')
    _sub(_find(blocks, lambda b:'These facts are pleaded at Stressors 1(k) and 3(a) and are repeated' in b['body']),'Stressors 1(k) and 3(a)','Stressors 1(h), 3(a) and 3(b)')
    _sub(_find(blocks, lambda b:'the fatigue enquiry pleaded at Stressor 3(j)' in b['body']),'Stressor 3(j)','Stressor 3(g)')
    _sub(_find(blocks, lambda b:'repeated on purpose from Stressor 1(l).' in b['body']),'Stressor 1(l)','Stressor 1(i)')
    for b in [x for x in blocks if 'pleaded at Stressors 1(m) and 3(l)' in x['body']]:
        _sub(b,'Stressors 1(m) and 3(l)','Stressors 1(f) and 3(i)')
    _sub(_find(blocks, lambda b:'as pleaded at Stressor 2(e)(i). The break' in b['body']),'Stressor 2(e)(i)','Stressor 2(a)')
    _sub(_find(blocks, lambda b:'Beyond the matters at (g) and (i) above' in b['body']),'(g) and (i) above','(a) and (f) above')
    _sub(_find(blocks, lambda b:'pleaded at Stressor 1(e) and Stressor 1(g) above' in b['body']),'Stressor 1(e) and Stressor 1(g)','Stressor 1(c) and Stressor 1(d)')
    _sub(_find(blocks, lambda b:'contains the gaps identified at Stressor 1(h)' in b['body']),'Stressor 1(h)','Stressor 1(e)')
    _sub(_find(blocks, lambda b:'entitlement in Stressor 2(f)' in b['body']),'Stressor 2(f)','Stressor 2(b)')
    # intervals table (Part B.4): every cell naming a stressor is mapped explicitly
    T=[b for b in blocks if b['kind']=='table' and b is not None and b.get('rows') and b['rows'][0][0].startswith('Interval')]
    assert len(T)==1; T=T[0]
    CELL={'Stressor 1(g)':'Stressor 1(d)','Stressor 1(h)':'Stressor 1(e)','Stressor 3(j)':'Stressor 3(g)',
          'Stressor 1(l), 2(f)':'Stressor 1(i), 2(b)','Stressor 1(b)':'Stressor 1(a)','Stressor 1(i)':'Stressor 1(b)',
          'Stressor 2(e)(i)':'Stressor 2(a)','Stressor 2(e)(i); Part B.1.4':'Stressor 2(a); Part B.1.4',
          'Stressor 2(e)(i), 3(j)':'Stressor 2(a), 3(g)',
          "Stressor 3(d) to (g); the Review Unit's own finding at 3(m)":"Stressor 3(a), (c) and (d), with the standard at the head of Stressor 3; the Review Unit's own finding under Stressor 3"}
    for r in T['rows'][1:]:
        for j,c in enumerate(r):
            if 'Stressor' in c:
                assert c in CELL, ('unmapped cell', c); r[j]=CELL[c]
    T['body']=' '.join(' '.join(r) for r in T['rows'])

    # ---------- Stressor 3(a): the agreement, in the order: signed; part-time; full-time; the emails; the Manager; the rest ----------
    s3,e3=_stressor(blocks,3)
    ag=[i for i in range(s3,e3) if blocks[i]['label'].startswith('(g) The agreement of 17 June 2020')]; assert len(ag)==1; ag=ag[0]
    blocks[ag]['label']='(g) The agreement of 17 June 2020, the changes to the Appellant\'s hours that followed, and the agreement\'s scope.'
    old_hr=blocks[ag]['body']
    assert old_hr.startswith('By email of 7 July 2026 a Senior Consultant, Human Resources wrote')
    nb=lambda t: {'k':None,'kind':'body','label':'','body':t,'pb':False}
    blocks[ag]['body']='On 17 June 2020 the Appellant signed an agreement allowing an 8-hour break between shifts. [¶ 17]'
    seq=[
     ('The change to part-time.','Since 17 June 2020 there has been a change to the Appellant\'s employment contract and adjustments in his working hours, as the employer confirmed. [¶ 20] He later became a part-time employee. In August 2023 he sought additional hours under clause 11.7 of the applicable agreement, headed "Additional Permanent Hours for Part-time Employees" [¶¶ 26 to 27], and Payroll was, as at 1 May 2024, still reviewing his entitlements "regarding public holidays not required arising while you were a part-time employee". [¶ 255]'),
     ('The change to full-time.','On 31 August 2023 he applied in writing to increase his hours to a full-time rotational roster. [¶ 30] On 27 September 2023 the Manager approved his application for "Permanent Fulltime hours", with full-time hours to commence from 16 October 2023. [¶¶ 37 to 38] The review decision records his submission that the 8-hour agreement "was no longer fit for purpose since your transition from casual employment to full-time" [¶ 18], and that "since your commencement, you have signed new terms and working arrangements as a full-time employee". [¶ 19]'),
     ('The emails.','On 1 May 2024 the Manager wrote that the request for fatigue payment for 18 March 2024 would not be processed "due to the existing 8-hour agreement signed by you on 17 June 2020", noting that he was able to terminate the agreement going forward; that email is pleaded at (g) below. [¶¶ 247 to 248] The review decision records the employer\'s response of 6 September 2024 as confirming "you did not formally rescind the 8-hour agreement signed by you on 17 June 2020 and the change to your employment contract and adjustments in your working hours did not automatically invalidate the agreement". [¶ 252] '+old_hr),
     ('The Manager and the agreement.','The review decision records that Ms Sandra Johnstone was the Switchboard Line Manager as at 8 December 2021, that Ms Danielle Cook was the "previous Switchboard Manager", and that "Ms Taylor was subsequently appointed to the Switchboard Manager role". [¶¶ 23 to 24] The Respondent does not allege that Ms Taylor was the Switchboard Manager on 17 June 2020. [¶ 25]'),
     ('The rest of the record on the agreement.','The Respondent does not allege that the agreement was reviewed, re-executed or re-confirmed at any time between 17 June 2020 and 18 March 2024 [¶ 21], or that the Appellant was informed, at any time before 1 May 2024, that it could be terminated by him. [¶ 22] The review decision found "uncertainty between you and the employer regarding whether the 8-hour agreement continued to apply" [¶ 254], and found the rostering of the two shifts to be "in direct contradiction to the award and the 8-hour agreement". [¶ 260]'),
    ]
    for k,(lb,t) in enumerate(seq):
        x=nb(t); x['label']=lb; blocks.insert(ag+1+k, x)
    # the general sentence in the shifts item now points to (a), where ¶¶ 17 to 25 are pleaded one by one
    _sub(_find(blocks, lambda b: b['body'].startswith('The review decision records the Appellant\'s submission that the 8-hour agreement "was no longer fit for purpose" since his transition')),
         'The review decision records the Appellant\'s submission that the 8-hour agreement "was no longer fit for purpose" since his transition, and the surrounding matters as to that agreement. [¶¶ 17 to 25]',
         'The agreement of 17 June 2020, the Appellant\'s submission that it "was no longer fit for purpose" after his transition, and the surrounding matters as to it are pleaded at (a) above. [¶¶ 17 to 25]')

    # ---------- the three stressors, rebuilt ----------
    seqhead={'k':None,'kind':'body','label':'Matters raised, and the responses.','pb':False,
             'body':'The matters at (g) to (j) below are the matters the Appellant raised and the responses he received, in date order. They are pleaded as sequence, not as separate causes within Stressor 1; the paragraph at the end of this stressor says so.'}
    _rebuild(blocks,1,[('set','a'),('set','d'),
        ('ev','a','b',['c']),('ev','b','i'),('ev','c','e',['f']),('ev','d','g'),('ev','e','h'),('ev','f','m'),
        ('block',seqhead),
        ('ev','g','j'),('ev','h','k'),('ev','i','l'),('ev','j','n'),
        ('close','o')])
    _rebuild(blocks,2,[('set','a'),
        ('ev','a','e(i)'),('ev','b','f'),('ev','c','b'),('ev','d','c',['d','e']),('ev','e','g'),
        ('close','h')])
    _rebuild(blocks,3,[('set','f'),('set','k'),
        ('ev','a','g'),('ev','b','a'),('ev','c','d'),('ev','d','e'),
        ('ev','e','h',[],[('h(i)','(e)(i)'),('h(ii)','(e)(ii)'),('h(iii)','(e)(iii)'),('h(iv)','(e)(iv)'),('h(v)','(e)(v)')]),
        ('ev','f','i'),('ev','g','j'),('ev','h','b'),
        ('ev','i','l',[],[('l(i)',''),('l(ii)','')]),
        ('close','c'),('close','m'),('close','n')])

    # ---------- the list of stressors: one row per event, under each theme ----------
    L=_find(blocks, lambda b: b['label']=='List of stressors.')
    L['body']=('Set out in the form required by Part 4.8 of the Workers\' Compensation Appeal Guide. Each stressor is a course of conduct; the lettered items under it are the individual events and issues within it, in date order, and each is pleaded in full below under the same letter. '
               'Stressor 1(g) to (j) are pleaded as sequence only and are not separate causes. The summary that follows the list gives the admissions on which each stressor rests.')
    LT=blocks[blocks.index(L)+1]; assert LT['kind']=='table' and LT['rows'][0][0]=='No.'
    th={r[0]:r for r in LT['rows'][1:]}; assert sorted(th)==['1','2','3']
    R=[LT['rows'][0], th['1'],
     ['1(a)','18 July 2023; not restored to 18 June 2024','Database access removed','Operators\' access to the database and the contact-changes book removed; changes to go to the Coordinator on her working days, or to the Manager; access not restored.'],
     ['1(b)','23 August 2023 to 21 May 2024','The Manager\'s office hours','No fixed office hours stated for nine months; the request of 15 May 2024 for them met by a request to retract it; hours stated on 17 May 2024.'],
     ['1(c)','15 April to 14 May 2024','Changes to process','The after-hours on-call process changed effective the day it was notified; a further data-entry process; unavailability notifications redirected; no record of consultation listed.'],
     ['1(d)','2 to 9 May 2024','Misdirected emergency calls','Nine occasions of calls, including a MET-call enquiry, sent to the wrong medical team; no communication to staff for five days; a new process on 9 May.'],
     ['1(e)','15 to 20 May 2024','The Integrated Respiratory Service entry','A clinical service reported twice that a wrong directory entry meant it could not help patients or staff; the Appellant escalated on 20 May.'],
     ['1(f)','18 July 2023 to 30 June 2024','The employer\'s own account of its systems','No fatigue risk management documents; no change to operating procedures from any complaint; complaints managed by email or verbally; Payroll\'s direction of 3 May 2024 still awaited on 21 May.'],
     ['1(g) to (j)','6 June 2023 to 21 May 2024','Matters raised, and the responses','Sequence only, not separate causes: the Communication Book; the matters raised in August and September 2023; the special pandemic leave application; the complaint of 13 May 2024 and the days that followed.'],
     th['2'],
     ['2(a)','9 February 2024 to 2 July 2025','Each incorrect shift, and its correction','Shifts of 9 and 28 February recorded as seven hours instead of eight; the fortnights from 18 March and 1 April recorded as ordinary hours where overtime was required; the last correction paid on 2 July 2025.'],
     ['2(b)','20 February to 1 March 2024','Paid Special Pandemic Leave','Declined twice and approved on the third submission, on attachments the Respondent admits were present.'],
     ['2(c)','As at 1 May 2024','Public holidays not required to be worked','Payroll still reviewing entitlements to public holidays not required arising while the Appellant was a part-time employee.'],
     ['2(d)','3 to 30 May 2024','The correction sought','Payroll\'s direction of 3 May 2024 to correct four fortnights not actioned at 13 May, still awaited on 21 May, lodged 28 May and recorded "Part Completed".'],
     ['2(e)','20 May 2024','Rostering practices raised with Human Resources','The Director followed up with Human Resources on the rostering concerns, attaching the fatigue guideline.'],
     th['3'],
     ['3(a)','Signed 17 June 2020; relied on 1 May 2024','The 8-hour agreement, and the changes in hours','Signed at a time the Respondent does not allege the Manager held that role; the Appellant\'s move to part-time and then to full-time hours from 16 October 2023; never reviewed; applying, on the employer\'s email of 7 July 2026, only to staff-initiated swaps.'],
     ['3(b)','7 August to 27 September 2023','Rostering errors, and the Appellant\'s proposals','A rostering oversight acknowledged; the application for full-time rotational hours, with a draft roster and full availability; full-time hours approved.'],
     ['3(c)','17 and 18 March 2024','Consecutive shifts','Rostered to finish at 23:00 and start at 06:00, in a function admitted to be critical to patient safety; no staff-initiated swap alleged.'],
     ['3(d)','17 and 18 March 2024','The rest between the shifts','Seven hours between the rostered finish and start; less than five hours with travel, on the Appellant\'s response of 9 August 2024.'],
     ['3(e)','17 to 19 March 2024','The emergency workload','The emergency codes received and paged on each shift, and the ordinary call load.'],
     ['3(f)','19 March 2024','The leave of 19 March 2024','Sick leave of 7.60 hours taken; fatigue leave said not to apply because no overtime was worked.'],
     ['3(g)','8 April to 1 May 2024','The fatigue enquiry','Answered after 23 days with a refusal relying on the 2020 agreement.'],
     ['3(h)','16 April to 21 May 2024','Rostering errors acknowledged, and the decision withheld','The Director acknowledged rostering errors, and recorded to Human Resources that the Appellant\'s roster "will not be considered" while he was "not yet aware of this".'],
     ['3(i)','To 30 June 2024','No fatigue risk management at the Switchboard','No fatigue risk assessment, training or framework implemented at the Switchboard before 30 June 2024, on the employer\'s own account.'],
    ]
    LT['rows']=R; LT['body']=' '.join(' '.join(r) for r in R)
    return blocks
