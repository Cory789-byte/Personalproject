import zipfile,re
def rep(x,a,b,n=1):
    c=x.count(a); assert c==n,(a[:80],c,n); return x.replace(a,b)
esc=lambda s: s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def strip_comments(files):
    out={}
    for name,d in files.items():
        if name=='word/comments.xml' or name.startswith('word/commentsExtended') or name.startswith('word/commentsIds') or name.startswith('word/commentsExtensible'): continue
        if name=='word/document.xml':
            t=d.decode()
            t=re.sub(r'<w:commentRangeStart [^>]*/>|<w:commentRangeEnd [^>]*/>','',t)
            t=re.sub(r'<w:r>(?:(?!</w:r>).)*?<w:commentReference [^>]*/>(?:(?!</w:r>).)*?</w:r>','',t,flags=re.S)
            t=re.sub(r'<w:commentReference [^>]*/>','',t); d=t.encode()
        if name=='word/_rels/document.xml.rels':
            d=re.sub(rb'<Relationship [^>]*Target="comments[^"]*"[^>]*/>',b'',d)
        if name=='[Content_Types].xml':
            d=re.sub(rb'<Override [^>]*PartName="/word/comments[^"]*"[^>]*/>',b'',d)
        out[name]=d
    return out
def process(path,fn):
    z=zipfile.ZipFile(path); infos=z.infolist(); files={i.filename:z.read(i.filename) for i in infos}; z.close()
    newdoc=fn(files['word/document.xml'].decode()).encode()
    files['word/document.xml']=newdoc
    files=strip_comments(files)
    zo=zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED)
    for i in infos:
        if i.filename in files: zo.writestr(i,files[i.filename])
    zo.close()
    t=zipfile.ZipFile(path).read('word/document.xml').decode(); assert 'commentReference' not in t and 'commentRange' not in t
def row_with(x,first):
    for m in re.finditer(r'<w:tr>.*?</w:tr>',x,re.S):
        cells=[re.sub(r'<[^>]+>','',c) for c in re.findall(r'<w:tc>.*?</w:tc>',m.group(0),re.S)]
        if cells and cells[0]==first: return m
    raise AssertionError(first)
def f9a(x):
    m=row_with(x,'1(k)'); x=x[:m.start()]+x[m.end():]
    m=row_with(x,'1(n)'); x=x[:m.start()]+x[m.end():]
    m=row_with(x,'1(j)'); r=m.group(0)
    r=rep(r,'>13 May 2024<','>13 to 15 May 2024<')
    r=rep(r,'>On call roster circulated<','>On-call roster and absence notification instructions<')
    r=rep(r,'>The roster was circulated on the first day of the fortnight it covered.<','>Roster circulated on the first day of the fortnight it covered; notification of unavailability channelled through the manager from 14 May.<')
    x=x[:m.start()]+r+x[m.end():]
    x=rep(x,'1(j) On call roster circulated (13 May 2024). ','1(j) On-call roster and absence notification instructions (13 to 15 May 2024). ')
    x=rep(x,'<w:t xml:space="preserve">1(k) Absence notification instructions (14 to 15 May 2024). </w:t>','<w:t xml:space="preserve"></w:t>')
    i=x.find('1(n) Manager absence notification (18 June 2024). '); s=x.rfind('<w:p>',0,i); e=x.find('</w:p>',i)+6
    para=x[s:e]; x=x[:s]+x[e:]
    para=rep(para,'1(n) Manager absence notification (18 June 2024). ','The Manager\'s notice of 18 June 2024. ')
    h=x.find('>Supporting records and overlap with the other themes<'); assert h>0; he=x.find('</w:p>',h)+6
    x=x[:he]+para+x[he:]
    assert x.count('1(k)')==0, x.count('1(k)')
    x=x.replace('1(l)','1(k)'); x=x.replace('1(m)','1(l)')
    x=rep(x,'and 1(j) to 1(n)','and 1(j) to 1(l)',2)
    assert '1(m)' not in x and '1(n)' not in x
    x=rep(x,'That email was written in July 2026 and describes the practice then stated; its application to March 2024 is a contention for determination.','Its application to March 2024 is a contention for determination.')
    a='The Respondent does not allege that those consecutive shifts arose from a staff-initiated shift swap. [¶ 234]'
    x=rep(x,a,a+esc(' So, on the admitted record: the minimum break was ten hours, or eight by written agreement [¶ 285]; on 7 July 2026 the employer\'s Human Resources wrote that the 8-hour agreement "is only applied where staff initiated shift swaps have occurred" [¶¶ 224 to 225]; no swap is alleged [¶ 234]; the break was seven hours [¶ 284]; and the review decision found the rostering of the two shifts to be unreasonable management action [¶ 260].'))
    x=rep(x,'terminated his employment on the basis of abandonment of employment, while he held continuous medical certificates;','terminated his employment on the basis of abandonment of employment, following certificates of no functional capacity from 1 July to 6 October 2024;')
    return x
def flet(x):
    x=rep(x,'(Stressor 1(n))','(Stressor 1, supporting records)',x.count('(Stressor 1(n))') or 1)
    a='they be received at hearing subject to proof.</w:t></w:r></w:p>'
    assert x.count(a)==1; e=x.find(a)+len(a)
    newp=('<w:p><w:pPr><w:spacing w:before="0" w:after="80" w:line="264" w:lineRule="auto"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:b/><w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr><w:t xml:space="preserve">'+esc("The Respondent's section 32(5) contention. ")+'</w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr><w:t>'
      +esc("Paragraph 27 of the Respondent's amended statement of facts and contentions of 13 May 2026 contends that any management action was reasonable management action taken in a reasonable way. The Respondent admitted on 8 September 2026 that paragraph 27 does not identify, by particular, date, document or cross-reference, the management action relied upon (fact 303). The Second Amended Form 9A now sets out each particular by date. The Appellant asks that the Respondent be directed to state, for each particular, whether it contends that it was management action and, if so, the facts relied on to say it was reasonable and taken in a reasonable way (item 4 of the election), so that the issues for the conference and any hearing are identified.")
      +'</w:t></w:r></w:p>')
    return x[:e]+newp+x[e:]
def freq(x):
    x=rep(x,'at which the directions requested at 2 and 3 below may be dealt with','at which the directions requested at 2 to 4 below may be dealt with')
    x=rep(x,'<w:t>5.</w:t>','<w:t>6.</w:t>')
    x=rep(x,'<w:t>4.</w:t>','<w:t>5.</w:t>')
    i=x.find('<w:t>5.</w:t>'); s=x.rfind('<w:p>',0,i)
    item=('<w:p><w:pPr><w:spacing w:before="0" w:after="140" w:line="264" w:lineRule="auto"/><w:ind w:left="440" w:hanging="440"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:t>4.</w:t><w:tab/></w:r><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:b/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:t>'
      +esc('That the Respondent state, for each particular in the list of stressors in the Second Amended Form 9A,')
      +'</w:t></w:r><w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:t xml:space="preserve">'
      +esc(' whether it contends that the particular was management action and, if so, the facts on which it relies to say that the action was reasonable and taken in a reasonable way, by the date fixed for any amended statement of facts and contentions under 5 below. Paragraph 27 of its amended statement of 13 May 2026 does not identify the management action relied upon (fact 303, admitted 8 September 2026).')
      +'</w:t></w:r></w:p>')
    return x[:s]+item+x[s:]
process('2026-10_SECOND_AMENDED_9A_FINAL.docx',f9a)
process('2026-10_LETTER_to_Registry_FINAL.docx',flet)
process('2026-10_REQUEST_election_and_directions_FINAL.docx',freq)
print('done')
