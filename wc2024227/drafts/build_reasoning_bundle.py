import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate, Paragraph as P, Spacer, Table, TableStyle, PageBreak

PK='out/pack_v2/'
DOCS=[('LOI','Letter of instruction, 17 August 2026',PK+'00_LETTER_OF_INSTRUCTION.pdf'),
 ('SCH','Schedule of assumed facts',PK+'00b_SCHEDULE_OF_ASSUMED_FACTS.pdf'),
 ('A1','Attachment 1 — Regulator’s response to the notice to admit facts, 18 February 2026',PK+'01_ATTACHMENT_1_Regulator_Response_18Feb2026.pdf'),
 ('A2','Attachment 2 — Letter of Ms N Cridland, Chief Executive, 5 June 2026',PK+'02_ATTACHMENT_2_MSH_Chief_Executive_letter_5Jun2026.pdf'),
 ('A3','Attachment 3 — Role description, Administration Officer, Switchboard Services (AO3)',PK+'03_ATTACHMENT_3_AO3_Switchboard_Role_Description.pdf'),
 ('A4a','Attachment 4a — General-practice records, Our Medical Ashmore',PK+'04a_ATTACHMENT_4_GP_records_Our_Medical_Ashmore.pdf'),
 ('A4b','Attachment 4b — Medical certificate, Dr Hawes, 8 September 2024',PK+'04b_ATTACHMENT_4_Hawes_Work_Capacity_Certificate_signed_8Sep2024.pdf'),
 ('A4c','Attachment 4c — Employee Capability Checklist, 3 July 2026',PK+'04c_ATTACHMENT_4_Employee_Capability_Checklist_3Jul2026.pdf'),
 ('A5','Attachment 5 — Approved changes to working hours, 2026',PK+'05_ATTACHMENT_5_Movement_Forms_2026.pdf'),
 ('A7','Attachment 7 — Request for medical information, 31 July 2026 (capacity questions — deferred)',PK+'07_ATTACHMENT_7_Request_for_Medical_Information_31Jul2026.pdf')]
srcs=[(k,lab,pikepdf.open(p)) for k,lab,p in DOCS]
counts=[len(d.pages) for _,_,d in srcs]
KEYS=[k for k,_,_ in DOCS]

H1=PS('h1',fontName='Helvetica-Bold',fontSize=11.5,leading=14,spaceAfter=2)
H2=PS('h2',fontName='Helvetica-Bold',fontSize=8.8,leading=11,spaceBefore=7,spaceAfter=2)
SM=PS('sm',fontName='Helvetica',fontSize=7.1,leading=8.7)
SMB=PS('smb',fontName='Helvetica-Bold',fontSize=7.1,leading=8.7)
TINY=PS('t',fontName='Helvetica',fontSize=6.8,leading=8.4)
BLUE='#0645AD'
order=[]   # order of link targets as they appear
def L(key,txt):
    order.append(key); return f'<a href="#{key}" color="{BLUE}">{txt}</a>'
def tbl(rows,w):
    t=Table(rows,colWidths=w,repeatRows=1)
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#aaaaaa')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#ececec')),
      ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),2.5),('RIGHTPADDING',(0,0),(-1,-1),2.5),
      ('TOPPADDING',(0,0),(-1,-1),1.6),('BOTTOMPADDING',(0,0),(-1,-1),1.6)])); return t

def content(start):
    order.clear()
    pos={}; pg=start
    for k,n in zip(KEYS,counts): pos[k]=pg; pg+=n
    def J(k,label=None): return L(k,(label or f'p. {pos[k]}'))
    s=[P('WHERE THE MATERIAL SITS AGAINST THE THREE MATTERS IN ISSUE',H1),
       P('Cory Shepherd · WC/2024/227 · 4 September 2026. The three matters are those written on the Notice of Non-Party Disclosure requested by the Workers’ Compensation Regulator and sealed 4 July 2025, which is attached to my email separately. Every document referred to below is in this file, complete and unaltered. <b>The page references are clickable</b>, and the bookmarks panel lists each document.',TINY),
       Spacer(1,3),
       P('This page is a finding aid only. It makes no submission about what any item shows, and nothing in it is intended to bear on your opinion. It contains nothing that was not provided with my letter of 17 August 2026, other than the page references.',TINY),
       Spacer(1,3),
       P('<b>PLEASE NOTE — WHAT IS <u>NOT</u> ASKED.</b> The letter of instruction of 17 August 2026 (in this file at '+J('LOI')+') asks a longer set of questions. Only the five questions in my email of 4 September 2026 are asked now. In particular, <b>questions 3.4 to 3.8 of that letter — capacity, restrictions and adjustments — are NOT asked for this purpose and should be set aside.</b> They are the employer\'s questions, they are not urgent, and they can be dealt with separately.',TINY),
       Spacer(1,4),
       P('MATTER 1 — DID MR SHEPHERD SUSTAIN A PERSONAL INJURY?',H2)]
    r=[[P('<b>Material</b>',SMB),P('<b>Where</b>',SMB)]]
    for a,b in [
     ('Your own clinical file for me, from 24 October 2024','held by the practice'),
     ('Your report of 13 February 2025','held by the practice'),
     ('General-practice records, Our Medical Ashmore — including the entries of 26.10.2022 ("ADHD", "Anxiety", in the Past Medical History list of the referral of 16.05.2024); 16.11.2023 (Dr Nanayakkara); 16.05.2024 (renewal of psychiatric referral); 28.06.2024 (Dr Slawinski); 01.07.2024 (Dr Hawes)','Attachment 4a, '+J('A4a')+' · schedule E, '+J('SCH')),
     ('Workers’ compensation medical certificate of Dr Hawes, signed 8 September 2024','Attachment 4b, '+J('A4b')),
     ('Employee Capability Checklist, 3 July 2026','Attachment 4c, '+J('A4c')),
     ('The Regulator accepts that your report of 13 February 2025 states Major Depressive Disorder — as what the report says; its accuracy is not accepted','schedule A item 38, '+J('SCH')),
     ('The Regulator does not accept the accuracy of the entry of 16 November 2023, and asserts a past medical history of anxiety and ADHD from 26 October 2022','schedule B items 34, 35, '+J('SCH'))]:
        r.append([P(a,SM),P(b,SM)])
    s.append(tbl(r,[118*mm,52*mm]))
    s.append(P('MATTER 2 — DID THE INJURY ARISE OUT OF, OR IN THE COURSE OF, THE EMPLOYMENT?',H2))
    r=[[P('<b>Material</b>',SMB),P('<b>Where</b>',SMB)]]
    for a,b in [
     ('The requirements of the position as the employer describes them — continuous shift work over the full 24-hour period, 7 days a week; the Emergency Response process "strictly adhering to protocols and timeframes"; "maintain call queues to minimum at all times"; multitasking under "high volume call traffic"; judgement "in situations where precedence have not been set and procedures not defined"; "limited supervision"','Attachment 3, '+J('A3')),
     ('Accepted: on 17–18 March 2024 rostered to finish at 23:00 and commence at 06:00 — a break of 7 hours','schedule A item 1, '+J('SCH')),
     ('Accepted: the fatigue policy and the Award require a minimum of 10 hours, or 8 hours by written agreement','schedule A item 3'),
     ('The Regulator’s document of 13 May 2026: "only a 7-hour break (rather than an 8-hour break) … a result of human error and not intentional or repeated"; leave taken 19 March 2024, paid','schedule A2 22(a), 22(c)'),
     ('Recorded by the Chief Executive: the requested fatigue risk management training records and register entries do not exist, such training applying only to health practitioners and clinical assistants; fatigue risk management assessment at that Switchboard was implemented only after 30 June 2024','Attachment 2, '+J('A2')),
     ('Recorded by the Chief Executive: a spreadsheet of recorded MET calls is available for 17–18 March 2024; employee complaints about operational errors are "managed solely via email or verbally with the complainant"','schedule C items 1–2, 3(a)'),
     ('Accepted: Ms Reese, 7 August 2023 — "a rostering error that was accidentally made by Chloe with regards to night shifts"','schedule A item 5'),
     ('Accepted: maintaining accurate contact details for medical staff is "a critical function of the Switchboard to ensure effective clinical handover and patient safety"','schedule A item 8'),
     ('The Regulator’s document of 13 May 2026 on the leave of 20–27 February 2024: "a review indicates that in fact, the attachments were present"; "a matter of human error"','schedule A2 14(e), 14(f)'),
     ('Accepted: payroll instruction to correct the shifts issued 3 May 2024; "I am waiting payroll confirmation" 21 May 2024; correction submitted 28 May 2024','schedule A items 40, 46, 41'),
     ('Changes to working hours approved during 2026 by Mr Hughes as delegate — 27 February, 17 April, 9 June','Attachment 5, '+J('A5')),
     ('The three stressors identified in the Employee Capability Checklist of 3 July 2026 — complaint handling; being held accountable and blamed for the failures of others; unpredictable rostering','Attachment 4c, '+J('A4c'))]:
        r.append([P(a,SM),P(b,SM)])
    s.append(tbl(r,[118*mm,52*mm]))
    s.append(P('MATTER 3 — WAS THE EMPLOYMENT A SIGNIFICANT CONTRIBUTING FACTOR TO THE INJURY?',H2))
    r=[[P('<b>Material</b>',SMB),P('<b>Where</b>',SMB)]]
    for a,b in [
     ('All of the material listed above','Matters 1 and 2'),
     ('Your report of 13 February 2025 referred to multiple life stressors including relationship breakdown, job loss and bereavement','held by the practice'),
     ('Your clinical relationship with me began on 24 October 2024, and my partner attended that consultation with me. Each of those matters arose while I was under your care and is recorded in your own file','held by the practice'),
     ('The sequence, from sources other than my account: onset pleaded at or about 18 June 2024 · application for compensation lodged 1 July 2024 · rejected 13 September 2024 · correspondence as to abandonment 8 October 2024 · review decision 24 October 2024 · your report 13 February 2025 · reinstatement effective 20 September 2024, agreement executed 21 February 2025 · Employee Capability Checklist 3 July 2026','schedules A, B, C · '+J('SCH','schedule')),
     ('My letter of instruction of 17 August 2026, and the five questions in my email of 4 September 2026','Letter, '+J('LOI'))]:
        r.append([P(a,SM),P(b,SM)])
    s.append(tbl(r,[118*mm,52*mm]))
    s.append(Spacer(1,3))
    s.append(P('Cory Shepherd · 0417 400 227 · coryshepherd1@hotmail.com',TINY))
    return s

def render(start):
    body=content(start)
    seq=list(order)                      # link order as emitted
    uniq=[]
    for k in seq:
        if k not in uniq: uniq.append(k)
    flow=list(body)
    for _ in uniq: flow.append(PageBreak()); flow.append(Spacer(1,1))
    state={'n':0}
    def later(c,d):
        i=state['n']
        if i < len(uniq): c.bookmarkPage(uniq[i])
        state['n']+=1
    buf=io.BytesIO()
    doc=SimpleDocTemplate(buf,pagesize=A4,leftMargin=17*mm,rightMargin=17*mm,topMargin=13*mm,bottomMargin=12*mm,title='',author='')
    doc.build(flow,onLaterPages=later)
    buf.seek(0); return pikepdf.open(buf), seq, uniq

# two passes so the printed page numbers are right (locator is 1 page)
loc,seq,uniq=render(2)
front_pages=1
loc,seq,uniq=render(front_pages+1)
print('locator content page count (expect 1 + %d dummies):'%len(uniq), len(loc.pages))

out=pikepdf.new()
out.pages.append(loc.pages[0])
starts={}
for (k,lab,d),n in zip(srcs,counts):
    starts[k]=len(out.pages); out.pages.extend(d.pages)

annots=out.pages[0].get('/Annots')
print('link annotations on page 1:',len(annots) if annots else 0,'| link targets in order:',len(seq))
assert annots is not None and len(annots)==len(seq), 'annotation/target count mismatch'
for ann,key in zip(annots,seq):
    ann['/Dest']=pikepdf.Array([out.pages[starts[key]].obj, pikepdf.Name('/XYZ'), 0, 842, 0])
    ann['/Border']=pikepdf.Array([0,0,0])

with out.open_outline() as ol:
    ol.root.append(pikepdf.OutlineItem('Where the material sits — the three matters', 0))
    for k,lab,_ in srcs: ol.root.append(pikepdf.OutlineItem(lab, starts[k]))
with out.open_metadata() as md:
    for x in list(md): del md[x]
for x in list(out.docinfo.keys()): del out.docinfo[x]
R=out.Root
for x in ('/Metadata','/PieceInfo','/Lang'):
    if x in R: del R[x]
R['/PageMode']=pikepdf.Name('/UseOutlines')
for pg in out.pages:
    for x in ('/Metadata','/PieceInfo'):
        if x in pg.obj: del pg.obj[x]
out.save('out/02_Finding_aid_and_enclosures_4Sep2026.pdf',fix_metadata_version=False)
print('TOTAL',len(out.pages),'pages')
for k in KEYS: print(f'   {k:4s} → p.{starts[k]+1}')
