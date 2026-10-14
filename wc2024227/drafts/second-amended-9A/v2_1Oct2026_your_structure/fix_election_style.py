import zipfile,re,html,os
F='2026-10_REQUEST_election_and_directions_FINAL.docx'
z=zipfile.ZipFile(F); items=[(i,z.read(i.filename)) for i in z.infolist()]; z.close()
x=dict((i.filename,d) for i,d in items)['word/document.xml'].decode()
esc=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
RP='<w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>{b}<w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr>'
def run(t,b): return '<w:r>'+RP.format(b='<w:b/>' if b else '<w:b w:val="0"/>')+'<w:t xml:space="preserve">'+esc(t)+'</w:t></w:r>'
NUM='<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:t>{n}.</w:t><w:tab/></w:r>'
T=lambda p:html.unescape(''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p)))
SPEC={'2':["That, at the opening of the conference, the Respondent state whether it maintains the contention in paragraph 27 of its amended statement of facts and contentions of 13 May 2026",[]],
 '3':["That the proposed Second Amended Statement of Facts and Contentions (Form 9A) enclosed with the Appellant's letter be considered for the purposes of the application for leave",["bears the onus of proof","It adds no new stressor or allegation"]],
 '4':["That the Respondent state, by 4.00 pm on a date fixed by the Commission, whether it maintains its dispute as to the authenticity of each of the ten documents at Annexure A to the Appellant's notice to admit documents served 28 August 2026 that remain outstanding",["cease to be in issue"]],
 '5':["That the Respondent state, for each causal particular in the proposed Second Amended Form 9A,",[]],
 '6':["That, if leave is granted and the Second Amended Form 9A is filed, the Respondent have leave to file and serve an amended statement of facts and contentions,",["within 14 days after that filing"]]}
for n,(lead,phr) in SPEC.items():
    ps=[p for p in re.findall(r'<w:p[ >].*?</w:p>',x,re.S) if re.match(r'^%s\.That'%n,T(p))]
    assert len(ps)==1,n; p=ps[0]; full=T(p)[len(n)+1:]
    assert full.startswith(lead),(n,full[:80]); rest=full[len(lead):]
    segs=[(lead,True)]; cur=rest
    # split rest on bold phrases in order of appearance
    marks=sorted([(cur.index(q),q) for q in phr])
    pos=0
    for i,q in marks:
        segs.append((cur[pos:i],False)); segs.append((q,True)); pos=i+len(q)
    segs.append((cur[pos:],False))
    ppr=re.search(r'<w:pPr>.*?</w:pPr>',p,re.S).group(0)
    np_='<w:p>'+ppr+NUM.format(n=n)+''.join(run(t,b) for t,b in segs if t)+'</w:p>'
    assert T(np_)==T(p),n
    x=x.replace(p,np_)
with zipfile.ZipFile(F+'.tmp','w',zipfile.ZIP_DEFLATED) as w:
    for it,d in items: w.writestr(it, x.encode() if it.filename=='word/document.xml' else d)
os.replace(F+'.tmp',F); print('ok')
