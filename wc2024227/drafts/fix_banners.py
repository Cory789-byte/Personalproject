#!/usr/bin/env python3
"""Purge the stale 'double standard'/'obstruction' banners: white-out, restamp
neutral banner + footer, rasterize the affected pages. Applied to the doctor set
and to v2 copies of the two service bundles."""
import subprocess, os
import pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
W,H = A4
BAR=HexColor('#1b1b2f'); GREY=HexColor('#555555')

HOURS = dict(
  pages={27:'Hours sequence 1 of 4 · the appellant’s office-hours request · 15 May 2024, 1:15pm',
         28:'Hours sequence 2 of 4 · the retract email · 15 May 2024, 6:23pm (sent to the appellant only)',
         29:'Hours sequence 3 of 4 · the appellant’s reply · 15 May 2024, 7:09pm (attaching Ellen’s hours email)',
         30:'Hours sequence 4 of 4 · Ms Taylor · On call and Hours all-staff · 17 May 2024'},
  topclear=122, botclear=48, footer='Shepherd · WC/2024/227 · Stressor 1(a) · TAB 6', fy=34)
COVID = dict(
  pages={9:'COVID leave texts · Feb–Mar 2024 · p.1 of 3',
         10:'COVID leave texts · Feb–Mar 2024 · p.2 of 3',
         11:'COVID leave texts · Feb–Mar 2024 · p.3 of 3'},
  topclear=58, botclear=40, footer='Shepherd · WC/2024/227 · Stressor 1 · TAB 2', fy=28)

JOBS = [
 ('STRESSOR_1A_BUNDLE_DR_12AUG.pdf', 'STRESSOR_1A_BUNDLE_DR_12AUG.pdf', HOURS),
 ('STRESSOR_1_COURSE_BUNDLE_DR_12AUG.pdf', 'STRESSOR_1_COURSE_BUNDLE_DR_12AUG.pdf', COVID),
 ('STRESSOR_1A_PARTICULARS_BUNDLE_11AUG.pdf', 'STRESSOR_1A_PARTICULARS_BUNDLE_11AUG_v2.pdf', HOURS),
 ('STRESSOR_1_COURSE_BUNDLE_1b-1f_11AUG.pdf', 'STRESSOR_1_COURSE_BUNDLE_1b-1f_11AUG_v2.pdf', COVID),
]

for src_fn, out_fn, FIX in JOBS:
    tag = os.path.splitext(out_fn)[0][:20]
    # 1. overlay
    ov_fn=f'_ov_{tag}.pdf'
    c=canvas.Canvas(ov_fn,pagesize=A4)
    order=sorted(FIX['pages'])
    for p in order:
        label=FIX['pages'][p]
        c.setFillColor(white)
        c.rect(0,H-FIX['topclear'],W,FIX['topclear'],stroke=0,fill=1)
        c.rect(0,0,W,FIX['botclear'],stroke=0,fill=1)
        c.setFillColor(BAR); c.rect(0,H-30,W,30,stroke=0,fill=1)
        c.setFillColor(white); c.setFont('Helvetica-Bold',9.5)
        c.drawString(14,H-19,label)
        c.setFillColor(GREY); c.setFont('Helvetica',8)
        c.drawString(57,FIX['fy'],FIX['footer'])
        c.showPage()
    c.save()
    pdf=pikepdf.open(src_fn)
    ov=pikepdf.open(ov_fn)
    for i,p in enumerate(order):
        pdf.pages[p-1].add_overlay(ov.pages[i])
    tmp=f'_tmp_{tag}.pdf'
    pdf.save(tmp)
    # 2. rasterize affected pages
    repl_fn=f'_repl_{tag}.pdf'
    cc=canvas.Canvas(repl_fn,pagesize=A4)
    for p in order:
        subprocess.run(['pdftoppm','-r','150','-jpeg','-jpegopt','quality=85',
                        '-f',str(p),'-l',str(p),tmp,f'_rast_{tag}_{p}'],check=True)
        jpg=[f for f in os.listdir('.') if f.startswith(f'_rast_{tag}_{p}') and f.endswith('.jpg')][0]
        cc.drawImage(jpg,0,0,W,H)
        cc.showPage()
    cc.save()
    final=pikepdf.open(tmp)
    repl=pikepdf.open(repl_fn)
    for i,p in enumerate(order):
        final.pages[p-1]=repl.pages[i]
    # 3. metadata scrub (page replacement can drop it? re-assert)
    src_title=str(final.docinfo.get('/Title','WC/2024/227 bundle'))
    with final.open_metadata(set_pikepdf_as_editor=False) as meta:
        meta['dc:title']=src_title
        meta['dc:creator']=['Cory Lea Shepherd']
        meta['dc:description']='Shepherd v Workers’ Compensation Regulator · WC/2024/227'
    di=final.docinfo
    for k in list(di.keys()): del di[k]
    di['/Title']=src_title
    di['/Author']='Cory Lea Shepherd'; di['/Creator']='Cory Lea Shepherd'
    di['/Producer']='Cory Lea Shepherd'
    di['/Subject']='Shepherd v Workers’ Compensation Regulator · WC/2024/227'
    raw=f'_fixed_{tag}.pdf'
    final.save(raw)
    subprocess.run(['qpdf','--linearize',raw,out_fn],check=True)
    print('FIXED ->',out_fn)
