# Rule 13(1) Industrial Relations (Tribunals) Rules 2011: Times New Roman, 11 point, fully justified,
# 2 cm margins, consecutive page numbers, no embellishment. Plus italics for case names and Act titles.
import zipfile,re,html,os
esc=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
ITAL=["Prizeman v Q-COMP","Delaney v Q-COMP","Workers' Compensation Regulator v Langerak","Carr v Workers' Compensation Regulator",
      "Simon Blackwood (Workers' Compensation Regulator) v Mahaffey","Workers' Compensation and Rehabilitation Act 2003",
      "Workers' Compensation and Rehabilitation Regulation 2025","Industrial Relations Act 2016","Uniform Civil Procedure Rules 1999",
      "Uniform Civil Procedure (Fees) Regulation 2019","de novo"]
ITAL+= [p.replace("'","’") for p in ITAL if "'" in p]
FOOTER=('<?xml version=\'1.0\' encoding=\'UTF-8\' standalone=\'yes\'?><w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
 '<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:t xml:space="preserve">Page </w:t></w:r>'
 '<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>'
 '<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
 '<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r>'
 '<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:t>1</w:t></w:r>'
 '<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>')
PPR_AFTER_JC=('<w:textDirection','<w:textAlignment','<w:textboxTightWrap','<w:outlineLvl','<w:divId','<w:cnfStyle','<w:rPr','<w:sectPr','<w:pPrChange')
def add_jc(p):
    if '<w:jc ' in p.split('</w:pPr>')[0] if '<w:pPr>' in p else False: return p
    if '<w:pPr>' not in p and '<w:pPr ' not in p:
        return re.sub(r'^(<w:p(?: [^>]*)?>)',r'\1<w:pPr><w:jc w:val="both"/></w:pPr>',p,count=1)
    m=re.search(r'<w:pPr>(.*?)</w:pPr>',p,re.S); inner=m.group(1)
    pos=len(inner)
    for t in PPR_AFTER_JC:
        i=inner.find(t)
        if i!=-1: pos=min(pos,i)
    new=inner[:pos]+'<w:jc w:val="both"/>'+inner[pos:]
    return p[:m.start(1)]+new+p[m.end(1):]
def italicise(x):
    n=0
    def fix_run(r):
        nonlocal n
        m=re.match(r'<w:r>(<w:rPr>.*?</w:rPr>)?<w:t[^>]*>([^<]*)</w:t></w:r>$',r,re.S)
        if not m: return r
        rpr,t=m.group(1) or '<w:rPr></w:rPr>',html.unescape(m.group(2))
        hits=[(t.find(q),q) for q in ITAL if q in t]
        if not hits or '<w:i/>' in rpr: return r
        # all occurrences, non-overlapping, earliest first
        spans=[]
        for q in ITAL:
            for mm in re.finditer(re.escape(q),t): spans.append((mm.start(),mm.end()))
        spans.sort(); keep=[]
        for s in spans:
            if not keep or s[0]>=keep[-1][1]: keep.append(s)
        irpr=rpr.replace('</w:rPr>','<w:i/></w:rPr>') if '<w:b' not in rpr else re.sub(r'(<w:b(?: w:val="0")?/>)',r'\1<w:i/>',rpr,count=1)
        out=''; pos=0
        for a,b in keep:
            if a>pos: out+='<w:r>'+rpr+'<w:t xml:space="preserve">'+esc(t[pos:a])+'</w:t></w:r>'
            out+='<w:r>'+irpr+'<w:t xml:space="preserve">'+esc(t[a:b])+'</w:t></w:r>'; pos=b; n+=1
        if pos<len(t): out+='<w:r>'+rpr+'<w:t xml:space="preserve">'+esc(t[pos:])+'</w:t></w:r>'
        return out.replace('<w:rPr></w:rPr>','')
    x=re.sub(r'<w:r>(?:(?!</w:r>).)*?</w:r>',lambda m:fix_run(m.group(0)),x,flags=re.S)
    return x,n
def fonts_sizes(x):
    x=re.sub(r'w:(ascii|hAnsi|cs|eastAsia)="Arial"',r'w:\1="Times New Roman"',x)
    x=re.sub(r'<w:sz w:val="\d+"/>','<w:sz w:val="22"/>',x); x=re.sub(r'<w:szCs w:val="\d+"/>','<w:szCs w:val="22"/>',x)
    return x
def convert(F,add_footer):
    z=zipfile.ZipFile(F); items=[(i,z.read(i.filename)) for i in z.infolist()]; z.close()
    D={i.filename:d for i,d in items}
    x=D['word/document.xml'].decode()
    x=fonts_sizes(x)
    # justify every paragraph that has no alignment set (centred title lines keep their centring)
    x=re.sub(r'<w:p(?: [^>]*)?>.*?</w:p>',lambda m:add_jc(m.group(0)),x,flags=re.S)
    # no shading (rule 13(1)(j))
    x=re.sub(r'<w:shd [^>]*w:fill="(?!auto|FFFFFF)[0-9A-Fa-f]{6}"[^>]*/>','',x)
    # margins at least 2 cm (1134 twips) on each side
    def mar(m):
        s=m.group(0)
        for k in ['top','right','bottom','left']:
            s=re.sub(r'w:%s="(\d+)"'%k,lambda mm:'w:%s="%d"'%(k,max(int(mm.group(1)),1134)),s)
        return s
    x=re.sub(r'<w:pgMar [^>]*/>',mar,x)
    x,ni=italicise(x)
    if add_footer:
        rels=D['word/_rels/document.xml.rels'].decode()
        rels=rels.replace('</Relationships>','<Relationship Id="rIdFtrPg" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/></Relationships>')
        D['word/_rels/document.xml.rels']=rels.encode()
        ct=D['[Content_Types].xml'].decode().replace('</Types>','<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>')
        D['[Content_Types].xml']=ct.encode()
        x=re.sub(r'<w:sectPr>','<w:sectPr><w:footerReference w:type="default" r:id="rIdFtrPg"/>',x,count=1)
        D['word/footer1.xml']=FOOTER.encode()
    D['word/document.xml']=x.encode()
    for k in list(D):
        if re.match(r'word/(header|footer)\d+\.xml$',k) and not (add_footer and k=='word/footer1.xml'):
            h=fonts_sizes(D[k].decode()); D[k]=h.encode()
        if k in ('word/styles.xml','word/stylesWithEffects.xml'):
            s=D[k].decode(); s=re.sub(r'w:(ascii|hAnsi|cs|eastAsia)="Arial"',r'w:\1="Times New Roman"',s)
            s=re.sub(r'<w:sz w:val="\d+"/>','<w:sz w:val="22"/>',s); s=re.sub(r'<w:szCs w:val="\d+"/>','<w:szCs w:val="22"/>',s); D[k]=s.encode()
    names=[i.filename for i,_ in items]
    with zipfile.ZipFile(F+'.tmp','w',zipfile.ZIP_DEFLATED) as w:
        for i,_ in items: w.writestr(i,D[i.filename])
        for k in D:
            if k not in names: w.writestr(k,D[k])
    os.replace(F+'.tmp',F); print(F[8:20],'italicised',ni)
convert('2026-10_REQUEST_election_and_directions_FINAL.docx',True)
convert('2026-10_LETTER_to_Registry_FINAL.docx',True)
convert('2026-10_SECOND_AMENDED_9A_FINAL.docx',False)
