# Formatting only: stressor-table compaction and selective bold. No text changes.
exec(open('edit_change68.py').read().split("CAUSAL=")[0])
def boldify_rpr(rpr):
    if rpr is None: return '<w:rPr><w:b/></w:rPr>'
    if '<w:b w:val="0"/>' in rpr: return rpr.replace('<w:b w:val="0"/>','<w:b/>')
    if '<w:b/>' in rpr: return rpr
    m=re.search(r'<w:rFonts[^>]*/>',rpr)
    if m: return rpr[:m.end()]+'<w:b/>'+rpr[m.end():]
    return rpr.replace('<w:rPr>','<w:rPr><w:b/>',1)
def bold(d,phrase):
    for r in re.findall(r'<w:r>(?:(?!</w:r>).)*?<w:t[^>]*>[^<]*</w:t></w:r>',d.x,re.S):
        m=re.search(r'(<w:rPr>.*?</w:rPr>)?\s*<w:t[^>]*>([^<]*)</w:t>',r,re.S)
        t=html.unescape(m.group(2))
        if phrase in t:
            rpr=m.group(1); i=t.index(phrase)
            def run(s,rp): return '' if not s else '<w:r>'+(rp or '')+'<w:t xml:space="preserve">'+esc(s)+'</w:t></w:r>'
            new=run(t[:i],rpr)+run(phrase,boldify_rpr(rpr))+run(t[i+len(phrase):],rpr)
            assert d.x.count(r)>=1; d.x=d.x.replace(r,new,1); return
    raise AssertionError('not found: '+phrase)
E=Doc('2026-10_REQUEST_election_and_directions_FINAL.docx')
for q in ['maintains the contention in paragraph 27','It adds no new stressor or allegation','bears the onus of proof','maintains its dispute as to the authenticity','cease to be in issue','for each causal particular','within 14 days after that filing']: bold(E,q)
E.save()
L=Doc('2026-10_LETTER_to_Registry_FINAL.docx')
for q in ['298 of the 303 facts','29 of the 39 documents','the facts have since been largely settled by those admissions','the onus of proof is on the Appellant','adds no new stressor or allegation','No hearing date has been set','employment was a significant contributing factor','does not identify the management action relied upon','named no medical or expert witness and served no expert report','"the result of human error"','"appears to have been made in error"','not presently submitted for filing']: bold(L,q)
L.save()
N=Doc('2026-10_SECOND_AMENDED_9A_FINAL.docx')
for q in ['The Appellant accepts that he bears the onus of proof','critical function of the Switchboard to ensure effective clinical handover and patient safety','I am satisfied your employment was a significant contributing factor to the psychological injury','does not allege that access to the database was restored','That is approximately nine months','This new process is effective from today.','five days, eighteen hours and fourteen minutes after the first email','two hours after the conclusion of the office hours she had stated','five hours and eight minutes later','a break of seven hours','is only applied where staff initiated shift swaps have occurred','amounted to unreasonable management action','23 days later, with a refusal',"Cory's roster will not be considered, however Cory is not yet aware of this",'occurred after 30 June 2024','509 days after the shift was worked','the Appellant was informed, at any time before 1 May 2024, that it could be terminated by him','does not allege that Ms Taylor was the Switchboard Manager on 17 June 2020','does not identify, by particular, date, document or cross-reference, the management action relied upon']: bold(N,q)
# stressor table: tighter padding and line spacing, 8.5pt event rows, firmer borders
tbl=[t for t in re.findall(r'<w:tbl>.*?</w:tbl>',N.x,re.S) if 'The conditions in which' in t][0]; nt=tbl
nt=re.sub(r'<w:tblBorders>.*?</w:tblBorders>','<w:tblBorders><w:top w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/><w:left w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/><w:right w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/><w:insideH w:val="single" w:sz="2" w:space="0" w:color="BFBFBF"/><w:insideV w:val="single" w:sz="2" w:space="0" w:color="BFBFBF"/></w:tblBorders>',nt,flags=re.S)
nt=nt.replace('<w:top w:w="65" w:type="dxa"/>','<w:top w:w="20" w:type="dxa"/>').replace('<w:bottom w:w="65" w:type="dxa"/>','<w:bottom w:w="20" w:type="dxa"/>').replace('<w:left w:w="80" w:type="dxa"/>','<w:left w:w="60" w:type="dxa"/>').replace('<w:right w:w="80" w:type="dxa"/>','<w:right w:w="60" w:type="dxa"/>')
nt=nt.replace('<w:spacing w:after="40" w:before="40" w:line="252" w:lineRule="auto"/>','<w:spacing w:after="0" w:before="0" w:line="240" w:lineRule="auto"/>')
rows=re.findall(r'<w:tr[ >].*?</w:tr>',nt,re.S)
for r in rows:
    if re.search(r'<w:t[^>]*>\d\([a-z]\)</w:t>',r): nt=nt.replace(r,r.replace('<w:sz w:val="18"/>','<w:sz w:val="17"/>'),1)
N.x=N.x.replace(tbl,nt)
N.save(); print('ok')
# (second pass, run separately) intervals table: same padding and borders as the stressor table
