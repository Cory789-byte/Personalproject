"""Assemble the ready-to-send set for Mind and Memory Service, 5 September 2026.
Every PDF that leaves here is metadata-clean. The as-served original of the Notice is
preserved untouched at documents/2025-07-04_NNPD_Regulator_to_MindAndMemory_SEALED.pdf
and at drafts/out/pack_v2/06_ATTACHMENT_6_...pdf — only the outgoing copy is scrubbed.
"""
import os, shutil, hashlib, pikepdf

SEND='out/SEND_5SEP2026'
os.makedirs(SEND, exist_ok=True)

def scrub(src, dst):
    pdf=pikepdf.open(src)
    before=len(pdf.pages)
    with pdf.open_metadata() as md:
        for x in list(md): del md[x]
    for x in list(pdf.docinfo.keys()): del pdf.docinfo[x]
    for x in ('/Metadata','/PieceInfo','/Lang'):
        if x in pdf.Root: del pdf.Root[x]
    if '/Names' in pdf.Root and '/EmbeddedFiles' in pdf.Root['/Names']:
        del pdf.Root['/Names']['/EmbeddedFiles']
    for pg in pdf.pages:
        for x in ('/Metadata','/PieceInfo'):
            if x in pg.obj: del pg.obj[x]
    pdf.save(dst, fix_metadata_version=False)
    after=len(pikepdf.open(dst).pages)
    assert before==after, f'{src}: page count changed {before}->{after}'
    return after

FILES=[('out/SHEPHERD_01_Notice_of_Non-Party_Disclosure_sealed_4Jul2025.pdf',
        '01_Notice_of_Non-Party_Disclosure_sealed_4Jul2025.pdf'),
       ('out/SHEPHERD_02_Finding_aid_and_enclosures_5Sep2026.pdf',
        '02_Finding_aid_and_enclosures_5Sep2026.pdf'),
       ('out/SHEPHERD_03_Chronology_5Sep2026.pdf',
        '03_Chronology_5Sep2026.pdf')]

print(f'{"file":52s} {"pp":>4s} {"MB":>6s}  metadata')
for src,name in FILES:
    dst=os.path.join(SEND,name)
    n=scrub(src,dst)
    d=pikepdf.open(dst)
    clean=(not dict(d.docinfo)
           and '/Metadata' not in d.Root and '/PieceInfo' not in d.Root
           and not any('/Metadata' in p.obj or '/PieceInfo' in p.obj for p in d.pages))
    with d.open_metadata() as m: xmp=len(list(m))
    assert clean and xmp==0, f'{name}: metadata survived'
    print(f'{name:52s} {n:4d} {os.path.getsize(dst)/1048576:6.2f}  CLEAN')

# paste-ready body: everything from the salutation on. The header block is routing, not message.
raw=open('EMAIL_2_5SEP_Practice_scope_and_timing.txt').read()
i=raw.index('Dear Mind and Memory Service')
body=raw[i:]
open(os.path.join(SEND,'EMAIL_BODY_paste_into_Outlook.txt'),'w').write(body)

hdr=raw[:i]
subject=[l for l in hdr.splitlines() if l.startswith('SUBJECT:')][0][len('SUBJECT:'):].strip()
to=[l for l in hdr.splitlines() if l.startswith('TO:')][0][len('TO:'):].strip()
sheet=f"""SEND SHEET — Mind and Memory Service — 5 September 2026

FROM      coryshepherd1@hotmail.com   (NOT the .onmicrosoft.com account)
TO        {to}
SUBJECT   {subject}

BODY      EMAIL_BODY_paste_into_Outlook.txt — paste whole, it begins at "Dear Mind and
          Memory Service". Send as HTML if the arrows in the Reading line look wrong.

ATTACH    all three, in this order:
""" + ''.join(f"          {n}\n" for _,n in FILES) + f"""
TOTAL     {sum(os.path.getsize(os.path.join(SEND,n)) for _,n in FILES)/1048576:.2f} MB.
          Under Outlook's 20 MB limit. If a practice gateway bounces it at 10 MB, send
          attachment 02 in a second email — 01 and 03 are the ones needed for a fast answer.

CHECK     the report is due 4:00 pm Wednesday 9 September 2026.
"""
open(os.path.join(SEND,'SEND_SHEET.txt'),'w').write(sheet)

print('\nbody chars:',len(body),'| files in',SEND+':')
for f in sorted(os.listdir(SEND)): print('   ',f)
