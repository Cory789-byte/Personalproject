# Move the "In summary." paragraph from after the list of stressors to directly after Part A (page 1). No text change.
import zipfile,re,html,os
F='2026-10_SECOND_AMENDED_9A_FINAL.docx'
z=zipfile.ZipFile(F); items=[(i,z.read(i.filename)) for i in z.infolist()]; z.close()
x=dict((i.filename,d) for i,d in items)['word/document.xml'].decode()
T=lambda p:html.unescape(''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p)))
ps=re.findall(r'<w:p[ >].*?</w:p>',x,re.S)
summ=[p for p in ps if T(p).startswith('In summary.')]; assert len(summ)==1; summ=summ[0]
parta=[p for p in ps if T(p).startswith('Appellant: Cory Lea Shepherd.')]; assert len(parta)==1; parta=parta[0]
assert x.count(summ)==1 and x.count(parta)==1
x=x.replace(summ,'',1); x=x.replace(parta,parta+summ,1)
with zipfile.ZipFile(F+'.tmp','w',zipfile.ZIP_DEFLATED) as w:
    for it,d in items: w.writestr(it, x.encode() if it.filename=='word/document.xml' else d)
os.replace(F+'.tmp',F); print('moved')
