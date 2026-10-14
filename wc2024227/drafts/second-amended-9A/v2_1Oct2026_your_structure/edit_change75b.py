# Second pass: table cells left-aligned; letter Part 1 column widths; 9A running header on one line.
import zipfile,re,os
def rewrite(F,fn):
    z=zipfile.ZipFile(F); items=[(i,z.read(i.filename)) for i in z.infolist()]; z.close()
    D={i.filename:d for i,d in items}; fn(D)
    with zipfile.ZipFile(F+'.tmp','w',zipfile.ZIP_DEFLATED) as w:
        for i,_ in items: w.writestr(i,D[i.filename])
    os.replace(F+'.tmp',F)
def tables_left(x):
    return re.sub(r'<w:tbl>.*?</w:tbl>',lambda m:m.group(0).replace('<w:jc w:val="both"/>','<w:jc w:val="left"/>'),x,flags=re.S)
def doc(D,extra=None):
    x=tables_left(D['word/document.xml'].decode())
    if extra: x=extra(x)
    D['word/document.xml']=x.encode()
def letter_cols(x):
    t=[t for t in re.findall(r'<w:tbl>.*?</w:tbl>',x,re.S) if 'Position now' in t][0]
    g=re.search(r'<w:tblGrid>.*?</w:tblGrid>',t,re.S).group(0)
    ng='<w:tblGrid>'+''.join('<w:gridCol w:w="%d"/>'%w for w in [620,3000,1450,1150,1560,1850])+'</w:tblGrid>'
    return x.replace(t,t.replace(g,ng))
rewrite('2026-10_REQUEST_election_and_directions_FINAL.docx',lambda D:doc(D))
rewrite('2026-10_LETTER_to_Registry_FINAL.docx',lambda D:doc(D,letter_cols))
def ninea(D):
    doc(D)
    h=D['word/header1.xml'].decode()
    old=re.findall(r'<w:t[^>]*>([^<]*)</w:t>',h); assert len(old)==1,old
    D['word/header1.xml']=h.replace(old[0],"WC/2024/227  |  Shepherd v Workers' Compensation Regulator").encode()
rewrite('2026-10_SECOND_AMENDED_9A_FINAL.docx',ninea)
print('ok')
