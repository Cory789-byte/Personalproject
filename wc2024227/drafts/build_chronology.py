# Standalone one-page chronology (attachment 3). No links — it travels on its own.
import io, pikepdf, chronology
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate

buf=io.BytesIO()
SimpleDocTemplate(buf,pagesize=A4,leftMargin=17*mm,rightMargin=17*mm,topMargin=11*mm,
                  bottomMargin=10*mm,title='',author='').build(chronology.flowables())
buf.seek(0)
d=pikepdf.open(buf)
out=pikepdf.new(); out.pages.extend(d.pages)
with out.open_metadata() as md:
    for x in list(md): del md[x]
for x in list(out.docinfo.keys()): del out.docinfo[x]
for x in ('/Metadata','/PieceInfo','/Lang'):
    if x in out.Root: del out.Root[x]
for pg in out.pages:
    for x in ('/Metadata','/PieceInfo'):
        if x in pg.obj: del pg.obj[x]
out.save('out/SHEPHERD_03_Chronology_4Sep2026.pdf',fix_metadata_version=False)
print('standalone chronology pages:',len(out.pages))
