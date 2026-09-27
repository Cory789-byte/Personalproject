"""Finalise WC/2024/227: Second Amended 9A (DOCX + PDF), Registry letter (DOCX + PDF), combined PDF.
Single font (Arial; Liberation Sans metrics in the PDF), single bold hierarchy.
Source: struct.json (paragraph structure of the v2 DOCX) + edits_9A.txt (plain-language edits).
"""
import json,re,sys,zipfile,os,html
from xml.sax.saxutils import escape
SP='/tmp/claude-0/-home-user/6625dff5-a18f-544c-a62c-8ea1e8b9d28c/scratchpad'
V2='2026-09-27_SECOND_AMENDED_9A_draft_v2.docx'
OUT_DOCX='2026-10_SECOND_AMENDED_9A_FINAL.docx'
OUT_PDF='2026-10_SECOND_AMENDED_9A_FINAL.pdf'
LET_PDF='2026-10_LETTER_to_Registry_FINAL.pdf'
LET_DOCX='2026-10_LETTER_to_Registry_FINAL.docx'
COMBINED='2026-10_FINAL_Letter_Schedule_and_Second_Amended_9A.pdf'

# ---------- 1. structure + edits ----------
S=json.load(open(SP+'/struct.json'))
blocks=[]
for o in S:
    runs=o['runs']; kind=o['kind']
    if any(r['br'] for r in runs):
        lines=[];cur=''
        for r in runs:
            if r['br']: lines.append(cur);cur=''
            cur+=r['t']
        lines.append(cur)
        lines=[l.strip() for l in lines if l.strip()]
        if len(lines)==1 and 'Appellant' in lines[0]:
            k=lines[0].index('Appellant'); lines=[lines[0][:k].strip(),lines[0][k:].strip()]
        blocks.append({'i':o['i'],'kind':'signature','label':'','body':'','lines':lines,'pb':False}); continue
    label=runs[0]['t'] if runs and runs[0]['b'] and kind in('body','callout') else ''
    body=o['text'][len(label):]
    if kind in('title','subtitle','part','section','stressor'): label=''; body=o['text']
    blocks.append({'i':o['i'],'kind':kind,'label':label.strip(),'body':body.strip(),'pb':'pageBreakBefore' in o['ppr']})

# parse edits
edits=[];cur=None
for line in open('edits_9A.txt',encoding='utf8').read().split('\n'):
    if line.startswith('@@ '):
        if cur: edits.append(cur)
        parts=[x.strip() for x in line[3:].split('|')]
        idx=parts[0]; ins=idx.endswith('+'); idx=int(idx.rstrip('+'))
        cur={'idx':idx,'insert':ins,'label':None if parts[1]=='-' else parts[1],'kind':parts[2] if len(parts)>2 else None,'body':[]}
    elif cur is not None: cur['body'].append(line)
if cur: edits.append(cur)
def tokens(s):
    return (sorted(re.findall(r'\d+(?:[:./]\d+)*',s)), sorted(re.findall(r'"([^"]+)"',s)), sorted(re.findall(r'\[¶[^\]]*\]',s)))
report=[]
by_i={b['i']:b for b in blocks}
inserts={}
for e in edits:
    body='\n'.join(e['body']).strip()
    if e['insert']:
        inserts.setdefault(e['idx'],[]).append({'i':None,'kind':e['kind'] or 'body','label':e['label'] or '','body':body,'pb':False}); continue
    b=by_i[e['idx']]
    old=(b['label']+' '+b['body']).strip()
    if e['kind']=='delete': b['kind']='delete'; continue
    if e['kind']=='table':
        b['kind']='table'; b['rows']=[[c.strip() for c in ln.split('|')] for ln in e['body'] if ln.strip()]; b['label']=''; b['body']=' '.join(' '.join(r) for r in b['rows']); continue
    if e['label'] is not None: b['label']=e['label']
    if body!='=': b['body']=body
    if e['kind']: b['kind']=e['kind']
    if b['kind'] in('title','subtitle','part','section','stressor'):
        if e['label'] is not None: b['body']=e['label']
        b['label']=''
    new=(b['label']+' '+b['body']).strip()
    tn,qn,cn=tokens(new); to,qo,co=tokens(old)
    if (tn,qn,cn)!=(to,qo,co):
        miss=[x for x in to if x not in tn]+[x for x in qo if x not in qn]+[x for x in co if x not in cn]
        add=[x for x in tn if x not in to]+[x for x in qn if x not in qo]+[x for x in cn if x not in co]
        report.append((e['idx'],miss,add))
final=[]
for b in blocks:
    if b['kind']=='delete': continue
    if b['kind']=='body' and b['body'].startswith('Dated:'): b['body']='Dated: ______________________ 2026'
    final.append(b)
    for ins in inserts.get(b['i'],[]): final.append(ins)
# whole-document check of fact citations
def cites(bs):
    s=' '.join((b['label']+' '+b['body']) for b in bs if b['kind']!='signature')
    return set(re.findall(r'¶¶? ?[\d, to]+',s))|set(re.findall(r'paragraphs? [\d, to]+',s))
old_text=open(SP+'/v2_final_before.txt',encoding='utf8').read()
old_c=set(re.findall(r'¶¶? ?[\d, to]+',old_text))|set(re.findall(r'paragraphs? [\d, to]+',old_text))
new_c=cites(final)
print('EDIT TOKEN DIFFERENCES (idx, missing, added):')
for r in report: print(' ',r)
print('citation strings lost:',sorted(old_c-new_c)); print('citation strings new:',sorted(new_c-old_c))
from collections import Counter
newtxt=' '.join((b['label']+' '+b['body']) for b in final if b['kind']!='signature')
lostnums=Counter(re.findall(r'\d+(?:[:./]\d+)*',old_text))-Counter(re.findall(r'\d+(?:[:./]\d+)*',newtxt))
print('numeric tokens with fewer occurrences than v2:',dict(lostnums))
banned=['reprisal','retaliat','suppress','fraud','conspir','hostile','punish','capricious','will give evidence','pending','$']
alltext=' '.join((b['label']+' '+b['body']) for b in final)
print('banned words present:',[w for w in banned if w.lower() in alltext.lower()])
json.dump(final,open(SP+'/final_blocks.json','w'),indent=0)

# ---------- 2. DOCX ----------
def E(s): return escape(s).replace('"','&quot;')
def run(t,b=False,i=False,sz=20):
    return f'<w:r><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>{"<w:b/>" if b else ""}{"<w:i/>" if i else ""}<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/></w:rPr><w:t xml:space="preserve">{E(t)}</w:t></w:r>'
def P(ppr,runs): return f'<w:p><w:pPr>{ppr}</w:pPr>{runs}</w:p>'
LINE='<w:spacing w:before="{b}" w:after="{a}" w:line="264" w:lineRule="auto"/>'
BOX='<w:pBdr><w:top w:val="single" w:sz="4" w:space="4" w:color="BFBFBF"/><w:left w:val="single" w:sz="4" w:space="4" w:color="BFBFBF"/><w:bottom w:val="single" w:sz="4" w:space="4" w:color="BFBFBF"/><w:right w:val="single" w:sz="4" w:space="4" w:color="BFBFBF"/></w:pBdr>'
def docx_par(b):
    k=b['kind']
    if k=='title': return P(LINE.format(b=0,a=80)+'<w:jc w:val="center"/>',run(b['body'],True,sz=28))
    if k=='subtitle': return P(LINE.format(b=0,a=200)+'<w:jc w:val="center"/>',run(b['body'],sz=18))
    if k=='part':
        pb='<w:pageBreakBefore/>' if b['pb'] else ''
        return P('<w:keepNext/>'+pb+'<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="808080"/></w:pBdr>'+LINE.format(b=240,a=100),run(b['body'],True,sz=24))
    if k=='stressor': return P('<w:keepNext/><w:shd w:val="clear" w:color="auto" w:fill="E9E9E9"/>'+LINE.format(b=200,a=100),run(b['body'],True,sz=22))
    if k=='section': return P('<w:keepNext/>'+LINE.format(b=180,a=80),run(b['body'],True,sz=22))
    if k=='callout':
        rr=(run(b['label']+' ',True) if b['label'] else '')+run(b['body'])
        return P(BOX+'<w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/>'+LINE.format(b=80,a=140),rr)
    if k=='particulars': return P(LINE.format(b=0,a=100)+'<w:ind w:left="284"/>',run(b['body'],i=True,sz=18))
    if k=='table':
        def tc(txt,bold=False,shade=None):
            sh=f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>' if shade else ''
            return f'<w:tc><w:tcPr>{sh}</w:tcPr><w:p><w:pPr><w:spacing w:after="0"/></w:pPr>{run(txt,bold,sz=17)}</w:p></w:tc>'
        rows=['<w:tr><w:trPr><w:tblHeader/></w:trPr>'+''.join(tc(c,True,'E9E9E9') for c in b['rows'][0])+'</w:tr>']
        for r in b['rows'][1:]: rows.append('<w:tr>'+''.join(tc(c) for c in r)+'</w:tr>')
        grid='<w:tblGrid>'+''.join(f'<w:gridCol w:w="{w}"/>' for w in (4700,1900,1700,1338))+'</w:tblGrid>'
        return '<w:tbl><w:tblPr><w:tblW w:w="9638" w:type="dxa"/><w:tblBorders><w:top w:val="single" w:sz="4"/><w:left w:val="single" w:sz="4"/><w:bottom w:val="single" w:sz="4"/><w:right w:val="single" w:sz="4"/><w:insideH w:val="single" w:sz="4"/><w:insideV w:val="single" w:sz="4"/></w:tblBorders></w:tblPr>'+grid+''.join(rows)+'</w:tbl><w:p><w:pPr><w:spacing w:after="60"/></w:pPr></w:p>'
    if k=='signature':
        rr=run(b['lines'][0],True)+'<w:r><w:br/></w:r>'+run(b['lines'][1])
        return P(LINE.format(b=120,a=80),rr)
    rr=(run(b['label']+' ',True) if b['label'] else '')+run(b['body'])
    return P(LINE.format(b=0,a=100),rr)
src=zipfile.ZipFile(V2)
docxml=src.read('word/document.xml').decode()
head=docxml[:docxml.index('<w:body>')+len('<w:body>')]
sect=re.search(r'<w:sectPr.*?</w:sectPr>',docxml,flags=re.S).group(0)
sect=re.sub(r'<w:pgMar[^>]*/>','<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="567" w:footer="567" w:gutter="0"/>',sect)
newxml=head+''.join(docx_par(b) for b in final)+sect+'</w:body></w:document>'
names=src.namelist(); order=['[Content_Types].xml','_rels/.rels']+sorted(n for n in names if n not in('[Content_Types].xml','_rels/.rels'))
with zipfile.ZipFile(OUT_DOCX,'w',zipfile.ZIP_DEFLATED) as z:
    for n in order:
        data=newxml.encode('utf8') if n=='word/document.xml' else src.read(n)
        if n=='word/header1.xml': data=data.replace(b'w:sz w:val="15"',b'w:sz w:val="16"')
        if n=='word/settings.xml' and b'<w:zoom ' in data and b'w:percent' not in data: data=data.replace(b'<w:zoom ',b'<w:zoom w:percent="100" ')
        z.writestr(n,data)
print('docx written',OUT_DOCX)

# ---------- 3. PDF (shared stylesheet) ----------
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
FD='/usr/share/fonts/truetype/liberation/'
pdfmetrics.registerFont(TTFont('Arial',FD+'LiberationSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold',FD+'LiberationSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Italic',FD+'LiberationSans-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Arial-BoldItalic',FD+'LiberationSans-BoldItalic.ttf'))
addMapping('Arial',0,0,'Arial');addMapping('Arial',1,0,'Arial-Bold');addMapping('Arial',0,1,'Arial-Italic');addMapping('Arial',1,1,'Arial-BoldItalic')
GREY=colors.HexColor('#808080')
ST={
 'title':ParagraphStyle('title',fontName='Arial-Bold',fontSize=14,leading=17,alignment=1,spaceAfter=4),
 'subtitle':ParagraphStyle('subtitle',fontName='Arial',fontSize=9,leading=11.5,alignment=1,spaceAfter=10),
 'part':ParagraphStyle('part',fontName='Arial-Bold',fontSize=12,leading=15,spaceBefore=12,spaceAfter=5,keepWithNext=1),
 'stressor':ParagraphStyle('stressor',fontName='Arial-Bold',fontSize=11,leading=14,spaceBefore=10,spaceAfter=5,backColor=colors.HexColor('#E9E9E9'),borderPadding=(3,3,3,3),keepWithNext=1),
 'section':ParagraphStyle('section',fontName='Arial-Bold',fontSize=11,leading=14,spaceBefore=9,spaceAfter=4,keepWithNext=1),
 'body':ParagraphStyle('body',fontName='Arial',fontSize=10,leading=13,spaceAfter=5),
 'callout':ParagraphStyle('callout',fontName='Arial',fontSize=10,leading=13,backColor=colors.HexColor('#F2F2F2'),borderColor=colors.HexColor('#BFBFBF'),borderWidth=0.5,borderPadding=(5,5,5,5),spaceBefore=6,spaceAfter=11,leftIndent=3,rightIndent=3),
 'particulars':ParagraphStyle('particulars',fontName='Arial-Italic',fontSize=9,leading=11.5,leftIndent=14,spaceAfter=5),
 'signature':ParagraphStyle('signature',fontName='Arial',fontSize=10,leading=13,spaceBefore=6),
}
esc=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
TC=ParagraphStyle('tc',fontName='Arial',fontSize=8.5,leading=10.5); TCB=ParagraphStyle('tcb',parent=TC,fontName='Arial-Bold')
def pdf_par(b):
    k=b['kind']
    if k=='table':
        data=[[Paragraph(esc(c),TCB) for c in b['rows'][0]]]+[[Paragraph(esc(c),TC) for c in r] for r in b['rows'][1:]]
        W=A4[0]-40*mm; tb=Table(data,colWidths=[W*0.49,W*0.20,W*0.17,W*0.14],repeatRows=1)
        tb.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E9E9E9')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
        return [tb,Spacer(1,6)]
    if k=='signature': return Paragraph('<b>'+esc(b['lines'][0])+'</b><br/>'+esc(b['lines'][1]),ST['signature'])
    if k=='part' and b['pb']: return [PageBreak(),Paragraph(esc(b['body']),ST['part'])]
    txt=('<b>'+esc(b['label'])+'</b> ' if b['label'] else '')+esc(b['body'])
    return Paragraph(txt,ST[k])
def deco_factory(headtext):
    def deco(c,d):
        c.saveState(); c.setFont('Arial',7.5); c.setFillColor(GREY)
        c.drawString(20*mm,A4[1]-11*mm,headtext); c.drawRightString(A4[0]-20*mm,9*mm,f"Page {d.page}")
        c.setStrokeColor(colors.HexColor('#BFBFBF')); c.setLineWidth(0.4); c.line(20*mm,A4[1]-12.5*mm,A4[0]-20*mm,A4[1]-12.5*mm)
        c.restoreState()
    return deco
story=[]
for b in final:
    x=pdf_par(b); story.extend(x if isinstance(x,list) else [x])
doc=SimpleDocTemplate(OUT_PDF,pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=20*mm,bottomMargin=18*mm,title='Second Amended Form 9A WC/2024/227',author='Cory Lea Shepherd')
d=deco_factory("WC/2024/227  |  Shepherd v Workers' Compensation Regulator  |  Second Amended Statement of Facts and Contentions (Form 9A)")
doc.build(story,onFirstPage=d,onLaterPages=d)
import fitz
n9a=fitz.open(OUT_PDF).page_count; print('9A pdf pages',n9a)

# ---------- 4. Letter (same stylesheet) ----------
import importlib,letter_content as L; importlib.reload(L)
note=L.SCHEDULE_NOTE.replace('{PAGES}',str(n9a))
LB=ParagraphStyle('lb',parent=ST['body'],fontSize=9,leading=11,spaceAfter=3)
LT=ParagraphStyle('lt',fontName='Arial-Bold',fontSize=11,leading=13.5,spaceAfter=3)
LS=ParagraphStyle('ls',fontName='Arial-Bold',fontSize=9,leading=11,spaceAfter=4)
cell=ParagraphStyle('c',fontName='Arial',fontSize=8,leading=9.8); cellb=ParagraphStyle('cb',parent=cell,fontName='Arial-Bold')
S=[Paragraph(esc(L.DATE),LB)]
for l in L.TO: S.append(Paragraph(esc(l),ParagraphStyle('to',parent=LB,spaceAfter=0)))
S+= [Spacer(1,2),Paragraph(esc(L.CC),LB),Spacer(1,1),Paragraph(esc(L.TITLE),LT),Paragraph(esc(L.SUBJECT),LS)]
for b,txt in L.BODY: S.append(Paragraph('<b>'+esc(b)+'</b> '+esc(txt),LB))
S.append(Paragraph(esc(L.CLOSE[0]),LB)); S.append(Spacer(1,6)); S.append(Paragraph('<b>'+esc(L.CLOSE[1])+'</b>',LB))
S.append(PageBreak()); S.append(Paragraph(esc(L.SCHEDULE_TITLE),LT))
data=[[Paragraph(esc(h),cellb) for h in L.SCHEDULE_COLS]]
for r in L.SCHEDULE_ROWS: data.append([Paragraph(esc(str(v)),cell) for v in r])
W=A4[0]-34*mm
tbl=Table(data,colWidths=[W*0.05,W*0.36,W*0.11,W*0.10,W*0.18,W*0.20],repeatRows=1)
ts=[('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E9E9E9')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]
for i,r in enumerate(L.SCHEDULE_ROWS,start=1):
    if r[4]==L.C: ts.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#F3F7F3')))
    elif r[3]==L.D: ts.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#FBF5EE')))
tbl.setStyle(TableStyle(ts)); S.append(tbl); S.append(Spacer(1,8)); S.append(Paragraph(esc(note),LB))
docL=SimpleDocTemplate(LET_PDF,pagesize=A4,leftMargin=17*mm,rightMargin=17*mm,topMargin=16*mm,bottomMargin=14*mm,title='Letter to the Industrial Registry WC/2024/227',author='Cory Lea Shepherd')
dl=deco_factory("WC/2024/227  |  Shepherd v Workers' Compensation Regulator  |  Letter to the Industrial Registry, with schedule of documents")
docL.build(S,onFirstPage=dl,onLaterPages=dl)
nl=fitz.open(LET_PDF).page_count; print('letter pdf pages',nl)

# letter DOCX
def lrun(t,b=False,sz=19): return run(t,b,sz=sz)
def lp(text,lead='',bold=False,after=80,keep=False):
    k='<w:keepNext/>' if keep else ''
    return P(k+LINE.format(b=0,a=after),(lrun(lead+' ',True) if lead else '')+lrun(text,bold))
body=[lp(L.DATE)]+[lp(l,after=0) for l in L.TO]+[lp(''),lp(L.CC),lp(L.TITLE,bold=True),lp(L.SUBJECT,bold=True,after=120)]
for b,t in L.BODY: body.append(lp(t,lead=b))
body.append(lp(L.CLOSE[0],after=200)); body.append(lp(L.CLOSE[1],bold=True))
body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>'); body.append(lp(L.SCHEDULE_TITLE,bold=True,after=120))
def tc(t,b=False,shade=None):
    sh=f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>' if shade else ''
    return f'<w:tc><w:tcPr>{sh}</w:tcPr><w:p><w:pPr><w:spacing w:after="0"/></w:pPr>{lrun(t,b,sz=16)}</w:p></w:tc>'
rows=['<w:tr><w:trPr><w:tblHeader/></w:trPr>'+''.join(tc(h,True,'E9E9E9') for h in L.SCHEDULE_COLS)+'</w:tr>']
for r in L.SCHEDULE_ROWS:
    shade='F3F7F3' if r[4]==L.C else ('FBF5EE' if r[3]==L.D else None)
    rows.append('<w:tr>'+''.join(tc(str(v),False,shade) for v in r)+'</w:tr>')
grid='<w:tblGrid>'+''.join(f'<w:gridCol w:w="{w}"/>' for w in (480,3450,1050,960,1730,1960))+'</w:tblGrid>'
body.append('<w:tbl><w:tblPr><w:tblW w:w="9630" w:type="dxa"/><w:tblBorders><w:top w:val="single" w:sz="4"/><w:left w:val="single" w:sz="4"/><w:bottom w:val="single" w:sz="4"/><w:right w:val="single" w:sz="4"/><w:insideH w:val="single" w:sz="4"/><w:insideV w:val="single" w:sz="4"/></w:tblBorders></w:tblPr>'+grid+''.join(rows)+'</w:tbl>')
body.append(lp('')); body.append(lp(note))
ldoc=f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>{''.join(body)}<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1000" w:right="1134" w:bottom="900" w:left="1134" w:header="567" w:footer="567" w:gutter="0"/></w:sectPr></w:body></w:document>'''
ct='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>'''
rels='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>'''
with zipfile.ZipFile(LET_DOCX,'w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml',ct); z.writestr('_rels/.rels',rels); z.writestr('word/document.xml',ldoc)
print('letter docx written')

# ---------- 5. combined ----------
c=fitz.open(); c.insert_pdf(fitz.open(LET_PDF)); c.insert_pdf(fitz.open(OUT_PDF))
c.set_metadata({'title':'WC/2024/227 Letter to the Industrial Registry, schedule of documents, and Second Amended Form 9A','author':'Cory Lea Shepherd'})
c.save(COMBINED); print('combined pages',c.page_count)
