import zipfile,re,html,os
esc=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
TRX=r'(<w:t(?: [^>]*)?>)([^<]*)(</w:t>)'
class Doc:
    def __init__(s,F):
        s.F=F; z=zipfile.ZipFile(F); s.items=[(i,z.read(i.filename)) for i in z.infolist()]; z.close()
        s.x=dict((i.filename,d) for i,d in s.items)['word/document.xml'].decode()
    def paras(s): return re.findall(r'<w:p[ >].*?</w:p>',s.x,re.S)
    def rep(s,old,new,n=1):
        ps=[p for p in s.paras() if old in html.unescape(''.join(m[1] for m in re.findall(TRX,p)))]
        tot=sum(html.unescape(''.join(m[1] for m in re.findall(TRX,p))).count(old) for p in ps)
        assert tot==n,(old[:70],tot)
        for p in ps:
            np_=p
            while True:
                ms=list(re.finditer(TRX,np_)); texts=[html.unescape(m.group(2)) for m in ms]
                full=''.join(texts); i=full.find(old)
                if i<0: break
                # map offsets
                pos=0; si=ei=None
                for k,t in enumerate(texts):
                    if si is None and i<pos+len(t)+ (1 if False else 0) and i>=pos: si=k; soff=i-pos
                    if ei is None and i+len(old)<=pos+len(t) and i+len(old)>pos: ei=k; eoff=i+len(old)-pos
                    pos+=len(t)
                if ei is None: ei=si; eoff=soff+len(old)
                newtexts=list(texts)
                if si==ei: newtexts[si]=texts[si][:soff]+new+texts[si][eoff:]
                else:
                    newtexts[si]=texts[si][:soff]+new
                    for k in range(si+1,ei): newtexts[k]=''
                    newtexts[ei]=texts[ei][eoff:]
                out=[];last=0
                for k,m in enumerate(ms):
                    out.append(np_[last:m.start()])
                    out.append('<w:t xml:space="preserve">'+esc(newtexts[k])+'</w:t>' if newtexts[k]!=texts[k] else m.group(0))
                    last=m.end()
                out.append(np_[last:]); np_=''.join(out)
            assert s.x.count(p)==1; s.x=s.x.replace(p,np_)
    def save(s):
        out=s.F+'.tmp'
        with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as w:
            for i,d in s.items: w.writestr(i, s.x.encode() if i.filename=='word/document.xml' else d)
        os.replace(out,s.F)
