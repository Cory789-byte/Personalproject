import zipfile,re
def rep(x,a,b,n=1):
    c=x.count(a); assert c==n,(a[:90],c,n); return x.replace(a,b)
esc=lambda s: s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def edit(p,fn):
    z=zipfile.ZipFile(p); infos=z.infolist(); files={i.filename:z.read(i.filename) for i in infos}; z.close()
    files['word/document.xml']=fn(files['word/document.xml'].decode()).encode()
    zo=zipfile.ZipFile(p,'w',zipfile.ZIP_DEFLATED)
    for i in infos: zo.writestr(i,files[i.filename])
    zo.close()
def para_of(x,key):
    i=x.find(key); assert i>0,key; s=x.rfind('<w:p>',0,i); e=x.find('</w:p>',i)+6; return s,e
def f9a(x):
    # 1. 1(i) trimmed; Taylor-outline sentence moved to 1(l)
    x=rep(x,'1(i) The complaint of 13 May 2024, and the days that followed - chronology only (13 to 21 May 2024). ','1(i) The complaint of 13 May 2024 - chronology only (13 May 2024). ')
    old=("The content is not set out. The Respondent's disclosure of 11 June 2026 (Schedule, Part 2) contains, in this order: the complaint form, dated 13 May 2024 (pp 9 to 10); the Appellant's email of 15 May 2024 at 3:35 pm to the Ethical Standards Unit, the complaints mailbox and LBH_HR (p 8); a forward of that email by LBH_HR at 3:41 pm the same day to three Human Resources officers (p 7); and an email of 16 May 2024 at 11:43 am from one of those officers to the Director and Ms Smith, copied to three others, attaching the complaint form (p 7). The same bundle contains the Appellant's email of 15 May 2024 at 1:15 pm (p 6) and the Director's reply at 6:23 pm asking him to retract it (p 5), pleaded at 1(l). [¶¶ 74 to 77] The Respondent's outline of Ms Taylor's evidence, served 24 September 2026, states that, acting on HR's advice, she removed the email of 15 May 2024 from the shared Switchboard inbox. On 21 May 2024 at 2:53 pm the Director asked which changes or directives had concerned him. [¶¶ 79 to 80]")
    x=rep(x,esc(old).replace('&amp;','&amp;') if False else old.replace("'","'"),"The content is not set out. It is pleaded for chronology only; no cause of the injury and no motive is alleged in connection with it.")
    x=rep(x,'At 7:09 pm the Appellant replied that "Requesting clarity on business hours is a reasonable question". [¶ 78]'.replace('"','&quot;') if '&quot;Requesting' in x else 'At 7:09 pm the Appellant replied that "Requesting clarity on business hours is a reasonable question". [¶ 78]',
          ('At 7:09 pm the Appellant replied that "Requesting clarity on business hours is a reasonable question". [¶ 78] The Respondent\'s outline of Ms Taylor\'s evidence, served 24 September 2026, states that, acting on HR\'s advice, she removed the email of 15 May 2024 from the shared Switchboard inbox.'))
    # 2. 2(j) to context
    x=rep(x,'2(j) A completed AVAC recorded (15 to 16 May 2024). ','2(j) A completed AVAC recorded - context only (15 to 16 May 2024). ')
    x=rep(x,'Particulars 2(a) to 2(j) and 2(l) to 2(n) identify the entitlement and correction events before the certified injury date. Particular 2(k) is the related HR follow-up.',
          'Particulars 2(a) to 2(i) and 2(l) to 2(n) identify the entitlement and correction events before the certified injury date. Particular 2(j) records a completed claim in the same period, and particular 2(k) the related HR follow-up; both are context.')
    x=rep(x,'causal particulars 2(a) to 2(j) and 2(l) to 2(n).','causal particulars 2(a) to 2(i) and 2(l) to 2(n).')
    # 6. Neville passage shortened
    s,e=para_of(x,'Where the framework came from. ')
    p=x[s:e]
    runs=re.findall(r'<w:r>.*?</w:r>',p,re.S); assert len(runs)==2
    newtext=('The guideline\'s references list "Queensland Ombudsman (2006). The Neville Report". [p 31, section 12] Queensland Health\'s fatigue risk management policy followed that report, and the resource pack of December 2018 and the 2021 guideline that replaced it apply the system to every "worker" of a Hospital and Health Service, including "An employee" [pp 29 to 30, section 10; p 30, section 11]; the Switchboard is where the codes are received and paged. [¶ 8]')
    r2=re.sub(r'<w:t[^>]*>.*?</w:t>','<w:t>'+esc(newtext).replace('"','&quot;' if '&quot;' in runs[1] else '"')+'</w:t>',runs[1],flags=re.S)
    x=x[:s]+p.replace(runs[1],r2)+x[e:]
    # 7. C.3 gloss removed; continuing effect only
    x=rep(x,'records symptom exacerbation on exposure to the identified workplace stressors: exposure to the same stressors, two years on, producing the same symptoms. That record is consistent with the stressors pleaded at Part B.2 being a significant contributing factor to the injury, and it is relied on for that purpose and for continuing effect. No aggravation is claimed.',
          'records symptom exacerbation on exposure to the identified workplace stressors. It is relied on for the continuing effect of the injury only, not as a cause. No aggravation is claimed.')
    return x
def flet(x):
    # 1. Part 2 row and Part 3 row for 1(i); outlines row now points at 1(l)
    x=rep(x,'the emails of 15 May 2024 at 1:15 pm and 6:23 pm, the emails of 15 and 16 May 2024 concerning the complaint of 13 May 2024, and the complaint form','the emails of 15 May 2024 at 1:15 pm and 6:23 pm, and documents concerning the complaint of 13 May 2024')
    x=rep(x,'>Stressor 1(i), for dates, senders and recipients only<','>Stressors 1(e) and 1(l); for 1(i), the date of the complaint only<')
    x=rep(x,'>1(i), 2(n) to 2(o), 3(c); Stressor 3 agreement and pleaded-answer paragraphs; Part C, paragraph 5A<','>1(l), 2(n) to 2(o), 3(c); Stressor 3 agreement and pleaded-answer paragraphs; Part C, paragraph 5A<')
    x=rep(x,'>13 to 21 May 2024<','>13 May 2024<')
    x=rep(x,'>The complaint of 13 May 2024, and the days that followed<','>The complaint of 13 May 2024<')
    x=rep(x,'>Complaint and distribution chronology; context only, with no separate causal allegation.<','>Date of the complaint; chronology only, with no causal allegation.<')
    # 2. 2(j)
    x=rep(x,'2(a) to 2(j) and 2(l) to 2(n)','2(a) to 2(i) and 2(l) to 2(n)')
    x=rep(x,'The others, 1(a), 1(c), 1(e), 1(i), 1(j), 2(k), 2(o) and 3(a), are context','The others, 1(a), 1(c), 1(e), 1(i), 1(j), 2(j), 2(k), 2(o) and 3(a), are context')
    x=rep(x,'>Process 16328886 was submitted and completed; its relation to the errors needs identification.<','>Process 16328886 was submitted on 15 May and completed on 16 May; context only.<')
    # 4. duplicate no-expert sentence
    x=rep(x,' Neither the list nor the outlines names a medical or expert witness, and no expert report has been served as at 30 September 2026.','')
    # 5. note moved under Part 1; enclosure line to the letter body
    s,e=para_of(x,'The Appellant asked the Respondent on 9 September 2026')
    note=x[s:e]; x=x[:s]+x[e:]
    note=rep(note,' This letter accompanies the Appellant\'s election and requested directions. Enclosure: Second Amended Statement of Facts and Contentions (Form 9A).','')
    s2,_=para_of(x,'Schedule, Part 2: other documents relied on')
    x=x[:s2]+note+x[s2:]
    s3,_=para_of(x,'Cory Lea Shepherd, Appellant (self-represented)')
    encl=note.replace(re.search(r'<w:t>.*?</w:t>',note,re.S).group(0),'<w:t>'+esc('This letter accompanies the Appellant\'s election and requested directions. Enclosure: Second Amended Statement of Facts and Contentions (Form 9A).')+'</w:t>')
    x=x[:s3]+encl+x[s3:]
    # 8. naming in Part 3
    for a,b in [('>Reese followed up with HR and attached the fatigue guideline; related context.<','>The Director followed up with HR and attached the fatigue guideline; related context.<'),
                ('>The Appellant sought action on the toolkit; Reese said she was awaiting advice.<','>The Appellant sought action on the toolkit; the Director said she was awaiting advice.<'),
                ('>Reese recorded personal fatigue concerns, a moderate rating and an undisclosed roster decision.<','>The Director recorded his fatigue concerns, a moderate rating and an undisclosed roster decision.<'),
                ('>Reese followed up her earlier query and attached the guideline.<','>The Director followed up her earlier query and attached the guideline.<')]:
        x=rep(x,a,b)
    return x
def freq(x):
    x=rep(x,'2(a) to 2(j) and 2(l) to 2(n)','2(a) to 2(i) and 2(l) to 2(n)')
    x=rep(x,'that it either particularise it under 5 below or be confined at any hearing to the explanations in its outlines of evidence.','that it particularise it under 5 below.')
    return x
edit('2026-10_SECOND_AMENDED_9A_FINAL.docx',f9a); edit('2026-10_LETTER_to_Registry_FINAL.docx',flet); edit('2026-10_REQUEST_election_and_directions_FINAL.docx',freq)
print('done')
