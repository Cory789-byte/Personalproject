import zipfile,re,html,os
F='2026-10_SECOND_AMENDED_9A_FINAL.docx'
z=zipfile.ZipFile(F); items=[(i,z.read(i.filename)) for i in z.infolist()]; z.close()
x=dict((i.filename,d) for i,d in items)['word/document.xml'].decode()
T=lambda p:html.unescape(''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p)))
esc=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def para(key,nth=0,contains=None):
    ps=[p for p in re.findall(r'<w:p[ >].*?</w:p>',x,re.S) if T(p).startswith(key) and (contains is None or contains in T(p))]
    assert len(ps)>nth,(key,len(ps)); return ps[nth]
def body_edit(key,pairs,nth=0,contains=None,append=None):
    global x
    p=para(key,nth,contains)
    runs=re.findall(r'<w:r>.*?</w:r>|<w:r .*?</w:r>',p,re.S)
    body=[r for r in runs if '<w:t' in r and '<w:b/>' not in r]
    assert len(body)==1,(key,len(body))
    r=body[0]; t=html.unescape(re.search(r'<w:t[^>]*>([^<]*)</w:t>',r).group(1))
    for a,b in pairs:
        assert t.count(a)==1,(key,a[:50],t.count(a)); t=t.replace(a,b)
    if append: t=t.rstrip()+' '+append
    nr=re.sub(r'<w:t[^>]*>[^<]*</w:t>','<w:t xml:space="preserve">'+esc(t)+'</w:t>',r)
    np_=p.replace(r,nr); assert x.count(p)==1; x=x.replace(p,np_)
def delete(key,nth=0,contains=None):
    global x
    p=para(key,nth,contains); assert x.count(p)==1; x=x.replace(p,'')

# --- Gap 1: MASPER reply attributed to the Manager (fact 65); rec 5 merged
body_edit('The first reply was sent on 9 May',[(
 'The first reply was sent on 9 May at 9:20 am, and asked Dr Wong,',
 "The Manager's first reply was sent on 9 May at 9:20 am, five days, eighteen hours and fourteen minutes after the first email. [¶¶ 62 to 64] It was sent to the Registrar and Dr Wong, and asked Dr Wong,")])
delete('That reply was sent five days, eighteen hours')
body_edit('So the sequence at the console',[('a first reply after five days','the Manager\'s first reply after five days')])
body_edit("MASPER Registrar's first report",[('to the first reply,','to the Manager\'s first reply,')])
# --- Gap 2: respiratory - the escalation went to the Manager and the reply was hers (facts 94, 96, 100, 102 to 103)
body_edit('At 2:05 pm, from the Logan Switch',[(
 'within the office hours stated to all Switchboard staff on 17 May 2024, the Appellant wrote identifying',
 'within the office hours the Manager had stated to all Switchboard staff on 17 May 2024, the Appellant wrote to the Manager identifying')])
body_edit('The Respondent does not allege that the Appellant was rostered to work after 2:05',[
 ('The reply at 4:30 pm stated:',"The Manager's reply at 4:30 pm stated:"),
 ('two hours after the conclusion of the office hours stated to all Switchboard staff on 17 May 2024.','two hours after the conclusion of the office hours she had stated to all Switchboard staff on 17 May 2024.')])
body_edit('So the sequence was: the Service',[('and the reply two hours and twenty-five minutes after that, two hours after the stated office hours had ended.',
 "and the Manager's reply two hours and twenty-five minutes after that, two hours after the office hours she had stated had ended.")])
body_edit('The escalation to the reply at 4:30 pm',[('The escalation to the reply at 4:30 pm, two hours after the office hours stated',"The escalation to the Manager's reply at 4:30 pm, two hours after the office hours she had stated")])
# --- Rec 1: pleaded answer stated once (C.10); stressors cross-refer
body_edit('Context and the Respondent',[(
 "The Respondent does not allege that the Appellant was subject to any disciplinary process, or that his work performance was the subject of any formal performance management process, before 18 June 2024, nor does it describe any communication with him before that date as a warning. [¶¶ 300 to 302] Paragraph 27 of its amended statement of facts and contentions does not identify the management action relied upon. [¶ 303]",
 "The Respondent's pleaded answer, including paragraph 27 of its statement, is at Part C, paragraph 10. [¶¶ 300 to 303]")])

p=para("The Respondent's pleaded answer to this stressor.",0,'The employer\'s letter of 5 June 2026 states')
old=T(p)[len("The Respondent's pleaded answer to this stressor. "):]
body_edit("The Respondent's pleaded answer to this stressor.",[(old,
 "The Respondent's pleaded answer, including paragraph 27 of its statement, is at Part C, paragraph 10 [¶¶ 238, 300 to 303]. The employer's letter of 5 June 2026 on operating procedures and complaint handling is pleaded at Stressor 1, supporting records [¶¶ 266 to 267, 272].")],contains="The employer's letter of 5 June 2026 states")
p=para("The Respondent's pleaded answer to this stressor.",0,'Beyond the agreement')
old=T(p)[len("The Respondent's pleaded answer to this stressor. "):]
body_edit("The Respondent's pleaded answer to this stressor.",[(old,
 "Beyond the agreement and the sick-leave matters at 3(c), the Respondent's pleaded answer, including paragraph 27 of its statement, is at Part C, paragraph 10 [¶¶ 238, 300 to 303]; its account of how complaints were handled is pleaded at Stressor 1, supporting records [¶¶ 267, 272].")],contains='Beyond the agreement')
# --- Rec 2: 5 June letter in full once (Stressor 3); Stressor 1 keeps its own sentences
p=para('By letter of 5 June 2026, reference K-LM26/729',0,'The requested fatigue risk management documents' if False else 'spreadsheet of recorded MET calls')
old=T(p)
body_edit('By letter of 5 June 2026, reference K-LM26/729',[(old,
 "By letter of 5 June 2026, reference K-LM26/729, signed by the Chief Executive and addressed to the Commission, Metro South Health stated that \"there have been no 'consequential' changes to operating procedures over the period requested\" [¶ 266], and that \"All employee complaints relating to Logan Hospital Switchboard operational errors are made directly to the Line Manager of Switch Board and managed solely via email or verbally with the complainant.\" [¶ 267] Its statements on fatigue risk management and on the record of MET calls are pleaded at Stressor 3 [¶¶ 263 to 265, 268].")],contains='spreadsheet of recorded MET calls')
p=para('The Respondent does not allege that any fatigue risk assessment was conducted, that any fatigue risk management training')
body_edit('The Respondent does not allege that any fatigue risk assessment was conducted, that any fatigue risk management training',[(T(p),
 "The Respondent does not allege that any change was made to the operating procedures of the Switchboard as a consequence of any employee complaint at any time before 30 June 2024 [¶ 272]; its position on fatigue risk management before that date is pleaded at Stressor 3, supporting fatigue records [¶¶ 269 to 271].")])
# --- Rec 3: merge the two guideline paragraphs
body_edit('So the guideline treated',[(
 "The Chief Executive's letter states that fatigue risk management assessment at the Switchboard was implemented after 30 June 2024 and that the mandatory training \"only applies to health practitioners and clinical assistants\". [¶¶ 264 to 265]",
 "It is the guideline the Director sent to Human Resources on 20 May 2024 [¶¶ 222 to 223], ten days after she and the Manager had assessed the fatigue risk of the Appellant's roster as moderate [¶ 219]; the Chief Executive's letter states that fatigue risk management assessment at the Switchboard was implemented only \"after 30 June 2024\" and that the mandatory training \"only applies to health practitioners and clinical assistants\". [¶¶ 264 to 265]")])
delete('The guideline the Director sent to Human Resources on 20 May 2024 is the guideline')
# --- Rec 4: 1(e) intervals stated once (in the "So" paragraph)
body_edit('It records the Appellant as having submitted the request on three',[(
 ' The approval followed the third submission by thirteen minutes and thirty-five seconds; the interval from draft to final approval was ten days, four hours, forty minutes and twenty seconds. [¶¶ 124 to 125]','')])
# --- Rec 6: pointer sentence
delete('The agreement of 17 June 2020, the Appellant')
# --- Rec 7: fourth explanation of repetition
delete('The medical case as a whole')
# --- Rec 8: C.11 folded into 5A
body_edit('5A. The Respondent\'s notified evidence is consistent',[(
 'Those matters are relied on to the extent established by the admissions; silence in an outline is not a further admission.',
 'By particular, the outlines give no account of the dated events at Stressor 1(b), 1(f), 1(h) and 1(k), or at Stressor 3(e) to 3(h). On those particulars the facts are admitted, and the questions are whether each was management action, whether any management action was reasonable and taken in a reasonable way, and whether it contributed to the injury. Those matters are relied on to the extent established by the admissions; silence in an outline is not a further admission.')])
delete('11. The particulars on which the Respondent')
# --- Order fix in 1(c): 8 Aug and 8 Sep sentences placed in date order
body_edit('On 8 August 2023 at 4:15 pm',[],append="On 8 August 2023 he confirmed that he would work the replacement shift and was looking to pick up another. [¶ 29]")
body_edit('On 4 September 2023 he confirmed',[],append="On 8 September 2023 the Director wrote that she was \"glad to hear things seem to be going well with Chloe\" and glad that he had applied for the additional shifts through the recent EOI. [¶ 36]")
delete('On 8 August 2023 he had confirmed')
out=F+'.tmp'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as w:
    for i,d in items: w.writestr(i, x.encode() if i.filename=='word/document.xml' else d)
os.replace(out,F); print('ok')
