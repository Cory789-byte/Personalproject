import zipfile,re,os
F='2026-10_LETTER_to_Registry_FINAL.docx'
z=zipfile.ZipFile(F); items=[(i,z.read(i.filename)) for i in z.infolist()]; z.close()
x=dict((i.filename,d) for i,d in items)['word/document.xml'].decode()
def txt(p): return ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p))
ps=re.findall(r'<w:p[ >].*?</w:p>',x,re.S)
def one(start): m=[p for p in ps if txt(p).startswith(start)]; assert len(m)==1; return m[0]
def sub(o,n):
    global x; assert x.count(o)==1,o[:80]; x=x.replace(o,n)
for s in ['The Appellant asks that this letter and its enclosure','This letter accompanies the Appellant']:
    p=one(s); sub(p,p.replace('<w:pPr><w:spacing','<w:pPr><w:keepNext/><w:spacing',1))
p=one('Schedule, Part 1:'); sub(p,p.replace('<w:pPr><w:keepNext/>','<w:pPr><w:keepNext/><w:pageBreakBefore/>',1))
out=F+'.tmp'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as w:
    for i,d in items: w.writestr(i, x.encode() if i.filename=='word/document.xml' else d)
os.replace(out,F); print('ok')
