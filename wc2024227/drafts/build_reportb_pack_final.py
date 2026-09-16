#!/usr/bin/env python3
"""Report B doctor's pack v3 — full spec build.
Reorders body pages, regenerates cover+question pages with computed pins and live
links, rebuilds full bookmark tree (date-author grammar), adds return-links,
fixes hours banners, stamps new E-codes, scrubs metadata."""
import json, subprocess, re
import pikepdf
from pikepdf import Name, Dictionary, Array
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white

SRC = 'REPORT_B_LEAN_DOCTOR_PACK.pdf'
OUT = 'REPORT_B_DOCTOR_PACK_FINAL_11AUG.pdf'
W, H = A4  # 595.27 x 841.89

# ---------------- 1. BODY ORDER (source pages, 1-based) ----------------
def rng(a, b): return list(range(a, b + 1))
BODY = []
def block(key, pages, title):
    start = len(BODY)
    BODY.extend(pages)
    BLOCKS[key] = {'start': start, 'n': len(pages), 'title': title}
BLOCKS = {}
# B — Form 24
block('E05',  [13],        '13 Feb 2026 · Form 24 · KEY ADMISSIONS schedule')
block('F24N', rng(14, 19), 'Form 24 · original notice to admit facts (as filed)')
block('F24R', rng(20, 25), '18 Feb 2026 · Regulator · Form 24 response (admit / not-admit map)')
# C — 9A
block('E04MAP', [26],      'Amended Form 9A · stressor map (3 fatigue · 1 course · 2 pay)')
block('E04',  rng(27, 31), '8 Apr 2026 · Amended Form 9A · full pleaded course (5 pp)')
# D — spine
block('E01',  rng(34, 37), 'Letter of instruction · Report B (questions 6.1–6.11)')
block('E02',  [38],        'Chronology · one page · sourced dates')
block('E03',  rng(39, 40), 'Fatigue raised · contemporaneous dates from/to')
block('E06',  rng(41, 55), 'Form 20 affidavit · assumed-facts spine (role + stressors)')
# E — fatigue proof
block('E07',  rng(56, 57), '17-18 Mar 2024 · roster · the 7-hour break pairing')
block('E38',  [159],       '10 May 2024 · Reese/Taylor · FRMS risk matrix rating 11 + rostering errors + 20 May chase')
block('E08',  rng(58, 59), '19 Mar 2024 · Att 6 · fatigue leave / pairing / 8-hour agreement emails')
block('E09',  rng(60, 64), '5 Jun 2026 · Chief Executive · objection K-LM26/729 (no Switchboard FRMS assessment in period)')
block('E10',  rng(65, 67), 'QH-GDL-401-3.3 · FRMS guideline (extract)')
block('E30',  rng(108, 111), '2023-24 · Shepherd · rostering concerns chain (break / leave / travel)')
block('E31',  rng(112, 113), 'Shepherd · rostering FRMS communication not following EB11')
block('E32',  [114],       'Reese · developing rosters / does not know FRMS in place')
block('E33',  [115],       '20 Apr 2023 · Reese · rostering change email')
block('R1MAY', rng(126, 129), '26 Apr - 8 May 2024 · Roster Concerns · the 1 May request and refusal')
# R — rosters
block('RDRAFT', rng(132, 138), 'Draft rotational rosters · 6 sheets (Shepherd proposal)')
block('RPP',   rng(139, 143), 'Mar-Apr 2024 · management pay-period rosters')
block('RATT4', rng(144, 145), 'Mar 2024 · Att 4 face roster · pairing period')
block('RPHOT', rng(146, 154), 'Phone photographs · rosters and pay sheets')
# F — baseline + medical
block('E19', [87],         '31 Aug 2023 · Shepherd · CS-3 application 0.8 to full-time')
block('E39', [160],        '27 Sep 2023 · Taylor · Permanent Full-Time APPROVED (from 16 Oct 2023)')
block('E21', rng(93, 95),  'Ashmore GP records · 2022 pages · 16 Nov 2023 baseline · 1 Jul 2024 note')
block('E22', [96],         '1 Jul 2024 · Dr Hawes · first Work Capacity Certificate')
block('E40', [161],        'to 8 Sep 2024 · Dr Hawes · continuing Work Capacity Certificate')
block('E23', rng(97, 100), '13 Feb 2025 · Dr Krishnaiah · prior report to QSuper (Ings, Claims Manager)')
block('E24', [101],        '3 Jul 2026 · Employee Capabilities Checklist (fit with restrictions)')
block('E25', rng(102, 103), '2 Jul 2026 · MSH email · "unable to facilitate" context')
block('E26', [104],        '2026 · Mind and Memory clinic correspondence')
# G — governance / May / hours
block('E11', rng(68, 71),  '9-15 May 2024 · CS-1 · MASPER call-handling course')
block('E12', rng(72, 74),  'Jun 2023 · communication book / page-removal strand')
block('BK23', [130],       '6 Jun 2023 · communication book page')
block('BK24', [131],       '21 May 2024 · communication book page')
block('E13', rng(75, 77),  'Feb-Mar 2024 · COVID leave texts')
block('E14', rng(78, 80),  '24 Dec 2024 · PID outcome letter · 24-ESU-1130')
block('E15', [81],         '13 May 2024 · ESU complaint face')
block('E16', rng(82, 84),  '15-16 May 2024 · CS-4 complaint / HR disclosure')
block('E17', rng(85, 86),  '15-17 May 2024 · office-hours email and retract strand')
block('E27', [105],        '18 Jul 2023 · Ellen · database access removal email')
block('E35', [123],        'Ellen · Switchboard after-hours on-call manager email')
block('E36', [124],        'Taylor · after-hours on-call self-delegation email')
block('E37', [125],        '17 May 2024 · Taylor · on-call and hours all-staff email')
block('HRS', rng(155, 158), 'Hours requests and responses · sequence of four')
# H — pay + leave
block('E20', rng(88, 92),  '3-28 May 2024 · payroll AVAC / underpayment correspondence')
block('E28', rng(106, 107), '21 May 2024 · Taylor · "still waiting payroll" / AVAC next run')
block('E34', rng(116, 122), 'Qld Health payroll disclosure package (NNPD originals)')
block('E41', [162],        '19 Mar 2024 · Item 15 · QH Leave Takings Report (system record)')
block('E42', [163],        'Feb-May 2024 · Item 11 · myHR leave submissions (system record)')
# I — review decision
block('E43', rng(166, 174), '24 Oct 2024 · Review Decision 69983 (sources completeness · de novo)')

N_FRONT = 12  # cover + 11 question pages
def fp(key):  # final 1-based page of a block start
    return N_FRONT + BLOCKS[key]['start'] + 1

# list-line titles (short form for question pages)
LT = {
 'E00': 'E00 Fatigue + pairing matrix', 'E01': 'E01 Letter of instruction (Q6.1-6.11)',
 'E02': 'E02 Chronology one-page', 'E03': 'E03 Fatigue raised · dates from/to',
 'E04': 'E04 Amended Form 9A · full pleaded course', 'E05': 'E05 Form 24 key admissions',
 'E06': 'E06 Form 20 · assumed-facts spine', 'E07': 'E07 March 2024 roster · 17-18 Mar pairing',
 'E08': 'E08 Att 6 · fatigue leave / 8-hour agreement emails',
 'E09': 'E09 CE letter K-LM26/729 · FRMS gap', 'E10': 'E10 FRMS guideline extract',
 'E11': 'E11 CS-1 MASPER · 9-15 May 2024', 'E14': 'E14 PID outcome · 24-ESU-1130',
 'E17': 'E17 Office-hours / retract strand · 15-17 May 2024',
 'E19': 'E19 CS-3 application 31 Aug 2023', 'E21': 'E21 Ashmore GP pages · baseline',
 'E22': 'E22 Hawes WCC · 1 Jul 2024', 'E23': 'E23 Prior report · Dr Krishnaiah · 13 Feb 2025',
 'E24': 'E24 ECC · 3 Jul 2026', 'E25': 'E25 Email 2 Jul 2026', 'E26': 'E26 Clinic correspondence',
 'E27': 'E27 Database access removal · 18 Jul 2023',
 'E30': 'E30 Rostering concerns chain (break / leave / travel)',
 'E32': 'E32 Reese · rosters without FRMS awareness',
 'E38': 'E38 Employer FRMS rating of 11 · 10 May 2024',
 'E39': 'E39 Full-time APPROVED · 27 Sep 2023 (from 16 Oct 2023)',
 'E40': 'E40 Hawes WCC continuing · to 8 Sep 2024',
 'E41': 'E41 Item 15 · leave takings 19 Mar 2024 (system)',
 'E42': 'E42 Item 11 · myHR leave submissions (system)',
 'E43': 'E43 Review Decision 69983 (included last, completeness)',
}
QDEF = [
 ('Q6.1', ['E02','E19','E39','E21','E23','E22','E05']),
 ('Q6.2', ['E23','E21','E19','E02']),
 ('Q6.3', ['E19','E39','E21','E23','E05','E02','E06']),
 ('Q6.4', ['E01','E43']),
 ('Q6.5', ['E04','E05','E07','E06','E09','E30','E02']),
 ('Q6.6', ['E38','E03','E08','E41','E42','E17','E22','E02']),
 ('Q6.7', ['E23','E02','E01']),
 ('Q6.8', ['E23','E21','E01']),
 ('Q6.9', ['E38','E06','E05','E09','E11','E27','E32','E02']),
 ('Q6.10', ['E24','E25','E23','E01']),
 ('Q6.11', ['E23','E40','E24','E25','E26','E02']),
]
QT = json.load(open('qtexts.json'))
_q65k = [k for k in QT if k.startswith('Q6.5')][0]
QT[_q65k] = QT[_q65k].replace('union suppression', 'union-communication strand')
TITLES = {k.split(' ')[0]: k for k in QT}
TITLES['Q6.8'] = 'Q6.8 Premorbid personality'
QT[TITLES['Q6.8']] = ('From your own current assessment: do any premorbid personality '
 'features bear on diagnosis and/or causation (Q6.5)? Please address from your own '
 'current assessment.')
# Q6.11 retitle per v2 bookmark
TITLES['Q6.11'] = 'Q6.11 Change in capacity since the 13 February 2025 assessment'
QT[TITLES['Q6.11']] = QT.pop('Q6.11 Change in capacity over time')

# ---------------- 2. FRONT MATTER ----------------
LINKS = []   # (front_page_idx0, rect, target_key)
def wrap(c, text, x, y, wmax, size, leading, font='Helvetica'):
    c.setFont(font, size)
    words = text.split()
    line = ''
    while words:
        t = (line + ' ' + words[0]).strip()
        if c.stringWidth(t, font, size) <= wmax:
            line = t; words.pop(0)
        else:
            c.drawString(x, y, line); y -= leading; line = words.pop(0)
    if line: c.drawString(x, y, line); y -= leading
    return y

c = canvas.Canvas('front.pdf', pagesize=A4)
INK = HexColor('#1a1a1a'); BLUE = HexColor('#1552a0'); GREY = HexColor('#555555')
# --- cover (front page 0) ---
c.setFillColor(INK)
c.setFont('Helvetica-Bold', 15); c.drawString(57, H-70, 'WC/2024/227')
c.setFont('Helvetica-Bold', 13)
c.drawString(57, H-92, 'Report B — Questions, pleadings and source documents')
c.setFont('Helvetica', 10.5); c.setFillColor(GREY)
c.drawString(57, H-108, 'Dr Krishnaiah · Cory Shepherd · Confidential')
c.setFillColor(INK); y = H-140
y = wrap(c, 'Navigate by the bookmarks panel — every document has its own dated '
          'bookmark. Page references appear on each question page. Blue lines are links.',
          57, y, 480, 10, 13); y -= 8
c.setFont('Helvetica-Bold', 10.5); c.drawString(57, y, 'READ IN THIS ORDER:'); y -= 16
ORDER = [
 ('1.  Questions for the doctor (Q6.1–6.11, per the letter of instruction)', 'QSTART'),
 ('2.  Form 24 key admissions · original notice · Respondent’s response', 'E05'),
 ('3.  Form 9A stressor map, then the full Form 9A', 'E04MAP'),
 ('4.  Spine: letter of instruction · chronology · Form 20', 'E01'),
 ('5.  Fatigue documents, incl. the employer’s 10 May 2024 risk-matrix email', 'E07'),
 ('6.  Rosters (proposals · pay-period rosters · photographs)', 'RDRAFT'),
 ('7.  Baseline and medical, incl. the full-time approval and both certificates', 'E19'),
 ('8.  Governance, May 2024, and the hours sequence', 'E11'),
 ('9.  Pay and leave records (correspondence and system records)', 'E20'),
 ('10. Review Decision 69983 (included last, for completeness of sources)', 'E43'),
]
c.setFillColor(BLUE)
for txt, key in ORDER:
    c.setFont('Helvetica', 10.5); c.drawString(66, y, txt)
    LINKS.append((0, (60, y-3, 545, y+11), key)); y -= 16
c.setFillColor(INK); y -= 10
c.setFont('Helvetica-Bold', 10.5); c.drawString(57, y, 'DATES AS THE DOCUMENTS SHOW THEM:'); y -= 15
y = wrap(c, 'Full-time applied for 31 Aug 2023 · approved 27 Sep 2023 · commenced '
          '16 Oct 2023 · GP entry 16 Nov 2023 recording no psychological illness · '
          'attendance difficulty from 13–15 May 2024 (recorded in the Respondent’s '
          'pleading) · last day worked ~3 Jun 2024 · pleaded onset 18 Jun 2024 · first '
          'certificate and claim 1 Jul 2024.', 57, y, 480, 10, 13.5); y -= 14
c.setFont('Helvetica-Bold', 10.5); c.drawString(57, y, 'YOUR OPINION IS YOURS ALONE.'); y -= 15
y = wrap(c, 'The questions are those in the letter of instruction. Clinical conclusions, '
          'diagnosis, causation and capacity are matters for your independent judgment; '
          'legal questions (including the reasonableness of management action) are not '
          'asked of you.', 57, y, 480, 10, 13.5)
c.setFont('Helvetica', 8); c.setFillColor(GREY)
c.drawString(57, 40, 'Private · confidential · Shepherd WC/2024/227')
c.showPage()
# --- question pages (front pages 1..11) ---
for qi, (qk, elist) in enumerate(QDEF):
    title = TITLES[qk]; body = QT[title]
    c.setFillColor(INK); c.setFont('Helvetica-Bold', 12.5)
    y = wrap(c, title, 57, H-70, 480, 12.5, 16, 'Helvetica-Bold'); y -= 10
    c.setFont('Helvetica-Oblique', 10); c.setFillColor(GREY)
    c.drawString(57, y, 'Please address with clinical reasons:'); y -= 16
    c.setFillColor(INK)
    y = wrap(c, body, 57, y, 480, 10.5, 14.5); y -= 14
    c.setFont('Helvetica-Bold', 10); c.drawString(57, y, 'Supporting documents (blue lines are links):'); y -= 15
    for ek in elist:
        if qk == 'Q6.4' and ek == 'E43':
            c.setFillColor(INK); c.setFont('Helvetica', 9.5)
            y = wrap(c, 'Note: the Review Decision 69983 (E43, final section) is included, '
                      'last, so your sources list may record that it was reviewed.', 57, y, 470, 9.5, 12.5)
            LINKS.append((1+qi, (57, y-2, 540, y+26), 'E43')); y -= 6
            continue
        c.setFillColor(BLUE); c.setFont('Helvetica', 10)
        line = f'·  {LT[ek]}  —  p.{fp(ek)}'
        c.drawString(63, y, line)
        LINKS.append((1+qi, (57, y-3, 545, y+11), ek)); y -= 14.5
    c.setFillColor(GREY); c.setFont('Helvetica', 8)
    c.drawString(57, 40, f'Shepherd · WC/2024/227 · {title.split(" ")[0]}')
    c.showPage()
c.save()

# ---------------- 3. STAMPS ----------------
def make_stamp(fn, draw):
    cc = canvas.Canvas(fn, pagesize=A4); draw(cc); cc.save()
def pill(cc, x0, x1, label):
    cc.setFillColor(HexColor('#222222'))
    cc.roundRect(x0, 824, x1-x0, 15, 4, stroke=0, fill=1)
    cc.setFillColor(white); cc.setFont('Helvetica-Bold', 8)
    cc.drawCentredString((x0+x1)/2, 828.5, label)
make_stamp('st_ret.pdf', lambda cc: pill(cc, 498, 585, '◂ Questions'))
for code in ['E38','E39','E40','E41','E42','E43']:
    make_stamp(f'st_{code}.pdf', lambda cc, cd=code: pill(cc, 452, 492, cd))
# hours banner fix: white-out the old inner title line and reprint
import xml.etree.ElementTree as ET
def hours_fix(src_page_num, n, who):
    xml = subprocess.run(['pdftotext','-bbox','-f',str(src_page_num),'-l',str(src_page_num),SRC,'-'],
                         capture_output=True, text=True).stdout
    ys = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>', xml):
        if m.group(5) in ('double','standard'):
            ys.append((float(m.group(2)), float(m.group(4))))
    if not ys: return None
    ymin = min(a for a,b in ys); ymax = max(b for a,b in ys)
    # bbox origin is top-left; convert
    ry0 = H - ymax - 2; ry1 = H - ymin + 2
    fn = f'st_hrs{n}.pdf'
    def draw(cc):
        cc.setFillColor(white); cc.rect(30, ry0, 535, ry1-ry0, stroke=0, fill=1)
        cc.setFillColor(INK); cc.setFont('Helvetica-Bold', 10)
        cc.drawString(36, ry0 + 3, f'Hours requests and responses · {n} of 4 · {who}')
    make_stamp(fn, draw)
    return fn

def map26_fix():
    ry0 = H - 308.863 - 2; ry1 = H - 300.538 + 2
    def draw(cc):
        cc.setFillColor(white); cc.rect(26, ry0, 545, ry1-ry0, stroke=0, fill=1)
        cc.setFillColor(INK); cc.setFont('Helvetica', 8.3)
        cc.drawString(28, ry0 + 3.2, "\u00b7 Hours sequence: managers' all-staff hours emails; his hours request; the retract sent to him only.")
    make_stamp('st_map26.pdf', draw)
map26_fix()
HFIX = {155: hours_fix(155,1,'Ellen · all-department'),
        156: hours_fix(156,2,'Taylor · all-department'),
        157: hours_fix(157,3,'Shepherd · office-hours request'),
        158: hours_fix(158,4,'Reese · retract (to Shepherd only)')}


def banner_fix(src_page, keys, label, fn):
    xml = subprocess.run(['pdftotext','-bbox','-f',str(src_page),'-l',str(src_page),SRC,'-'],
                         capture_output=True, text=True).stdout
    words=[(float(m.group(1)),float(m.group(2)),float(m.group(3)),float(m.group(4)),m.group(5))
           for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]+)</word>', xml)]
    bands = sorted({round(w[1]) for w in words if any(k in w[4].lower() for k in keys)})
    if not bands: return None
    def draw(cc):
        for by in bands:
            line=[w for w in words if abs(w[1]-by)<2]
            y0=min(w[1] for w in line); y1=max(w[3] for w in line)
            ry0=H-y1-2; rh=y1-y0+4
            dark = y1 < 25
            cc.setFillColor(HexColor('#1b1b2f') if dark else white)
            cc.rect(0 if dark else 24, ry0, W if dark else 548, rh, stroke=0, fill=1)
            cc.setFillColor(white if dark else HexColor('#1a1a1a'))
            cc.setFont('Helvetica-Bold' if dark else 'Helvetica', min(9, rh-2))
            cc.drawString(10 if dark else 28, ry0+2.5, label)
    make_stamp(fn, draw); return fn
BFIX = {}
for sp in (75,76,77):
    BFIX[sp] = banner_fix(sp, ['obstruction'], 'COVID leave texts · Feb-Mar 2024', f'st_b{sp}.pdf')
BFIX[130] = banner_fix(130, ['pattern'], 'Communication book · 6 Jun 2023', 'st_b130.pdf')
BFIX[131] = banner_fix(131, ['pattern'], 'Communication book · 21 May 2024', 'st_b131.pdf')
# footer cover for hours pages
def _foot(cc):
    cc.setFillColor(white); cc.rect(20, 18, 555, 50, stroke=0, fill=1)
    cc.setFillColor(HexColor('#555555')); cc.setFont('Helvetica', 7)
    cc.drawString(30, 30, 'Shepherd · WC/2024/227 · confidential')
make_stamp('st_foot.pdf', _foot)

# ---------------- 4. ASSEMBLE ----------------
src = pikepdf.open(SRC)
front = pikepdf.open('front.pdf')
pdf = pikepdf.new()
for p in front.pages: pdf.pages.append(p)
for sp in BODY: pdf.pages.append(src.pages[sp-1])
assert len(pdf.pages) == N_FRONT + len(BODY)

# overlays
ret = pikepdf.open('st_ret.pdf')
for i in range(N_FRONT, len(pdf.pages)):
    pdf.pages[i].add_overlay(ret.pages[0])
for code in ['E38','E39','E40','E41','E42']:
    st = pikepdf.open(f'st_{code}.pdf')
    pdf.pages[fp(code)-1].add_overlay(st.pages[0])
stE43 = pikepdf.open('st_E43.pdf')
for k in range(BLOCKS['E43']['n']):
    pdf.pages[fp('E43')-1+k].add_overlay(stE43.pages[0])
st26 = pikepdf.open('st_map26.pdf')
pdf.pages[fp('E04MAP')-1].add_overlay(st26.pages[0])

srcpage_to_block = {}
for k,b in BLOCKS.items():
    pass
def final_of_source(sp):
    for k,b in BLOCKS.items():
        pgs = None
    return None
# apply banner fixes: map source page -> final page via BODY list
for sp, fn in BFIX.items():
    if fn:
        idx = BODY.index(sp)
        st = pikepdf.open(fn)
        pdf.pages[N_FRONT + idx].add_overlay(st.pages[0])
stf = pikepdf.open('st_foot.pdf')
for k in range(4):
    pdf.pages[fp('HRS')-1+k].add_overlay(stf.pages[0])
for j,(spg) in enumerate(rng(155,158)):
    if HFIX[spg]:
        st = pikepdf.open(HFIX[spg])
        pdf.pages[fp('HRS')-1+j].add_overlay(st.pages[0])

# links
def add_link(page, rect, target_page):
    annot = Dictionary(Type=Name.Annot, Subtype=Name.Link,
        Rect=Array([rect[0], rect[1], rect[2], rect[3]]),
        Border=Array([0,0,0]),
        A=Dictionary(S=Name.GoTo, D=Array([target_page.obj, Name.Fit])))
    if '/Annots' not in page: page.Annots = pdf.make_indirect(Array())
    page.Annots.append(pdf.make_indirect(annot))
for fpg, rect, key in LINKS:
    tgt = pdf.pages[1] if key == 'QSTART' else pdf.pages[fp(key)-1]
    add_link(pdf.pages[fpg], rect, tgt)
q1 = pdf.pages[1]
for i in range(N_FRONT, len(pdf.pages)):
    add_link(pdf.pages[i], (498, 822, 585, 841), q1)

# ---------------- 5. BOOKMARKS ----------------
from pikepdf import OutlineItem
def oi(title, key=None, page=None):
    pg = pdf.pages[(fp(key)-1) if key else page]
    return OutlineItem(title, destination=Array([pg.obj, Name.Fit]))
with pdf.open_outline() as ol:
    r = ol.root
    r.append(oi('Cover — reading order (links live)', page=0))
    a = oi('A. Questions for the doctor (Q6.1–6.11)', page=1)
    for i,(qk,_) in enumerate(QDEF):
        a.children.append(oi(TITLES[qk], page=1+i))
    r.append(a)
    def section(title, first_key, items):
        s = oi(title, key=first_key)
        for k in items: s.children.append(oi(BLOCKS[k]['title'], key=k))
        r.append(s)
    section('B. Form 24 admissions', 'E05', ['E05','F24N','F24R'])
    section('C. Amended Form 9A — pleaded course', 'E04MAP', ['E04MAP','E04'])
    section('D. Spine — instruction · chronology · Form 20', 'E01', ['E01','E02','E03','E06'])
    section('E. Fatigue and rostering proof', 'E07',
            ['E07','E38','E08','E09','E10','E30','E31','E32','E33','R1MAY'])
    section('F. Rosters', 'RDRAFT', ['RDRAFT','RPP','RATT4','RPHOT'])
    section('G. Baseline trajectory and medical', 'E19',
            ['E19','E39','E21','E22','E40','E23','E24','E25','E26'])
    section('H. Governance · May 2024 · hours', 'E11',
            ['E11','E12','BK23','BK24','E13','E14','E15','E16','E17','E27','E35','E36','E37','HRS'])
    section('I. Pay and leave records', 'E20', ['E20','E28','E34','E41','E42'])
    section('J. Review Decision 69983 — sources completeness (last)', 'E43', ['E43'])
    jl = oi('K. Jump list (alphabetical)', key='E05')
    for k in sorted([k for k in BLOCKS if k not in ('F24N','F24R')],
                    key=lambda k: BLOCKS[k]['title'].lower()):
        jl.children.append(oi(BLOCKS[k]['title'], key=k))
    r.append(jl)

# ---------------- 6. METADATA + SAVE ----------------
with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
    meta['dc:title'] = 'Report B — Questions, pleadings and source documents — WC/2024/227'
    meta['dc:creator'] = ['Cory Shepherd']
di = pdf.docinfo
for k in list(di.keys()): del di[k]
di['/Title'] = 'Report B — Questions, pleadings and source documents — WC/2024/227'
di['/Author'] = 'Cory Shepherd'
di['/Creator'] = 'Cory Shepherd'; di['/Producer'] = 'Cory Shepherd'

pdf.save('_v3_raw.pdf')
# rasterize authored label pages so no stale text layer survives
import os
RAST = [fp('E04MAP')] + [fp('HRS')+k for k in range(4)] + [N_FRONT + BODY.index(sp) + 1 for sp in BFIX if BFIX[sp]]
for pn in RAST:
    subprocess.run(['pdftoppm','-r','150','-jpeg','-jpegopt','quality=88','-f',str(pn),'-l',str(pn),'_v3_raw.pdf','rast_%d'%pn], check=True)
rpdf = pikepdf.open('_v3_raw.pdf')
from reportlab.pdfgen import canvas as rcanvas
for pn in RAST:
    img = [f for f in os.listdir('.') if f.startswith('rast_%d'%pn) and f.endswith('.jpg')][0]
    cc = rcanvas.Canvas('imgpg_%d.pdf'%pn, pagesize=A4)
    cc.drawImage(img, 0, 0, W, H); cc.save()
    ip = pikepdf.open('imgpg_%d.pdf'%pn)
    # replace page content but keep annotations (links)
    old = rpdf.pages[pn-1]
    annots = old.get('/Annots')
    rpdf.pages[pn-1] = ip.pages[0]
    if annots is not None: rpdf.pages[pn-1].Annots = annots
rpdf.save('_v3_rast.pdf')
subprocess.run(['qpdf','--linearize','--compress-streams=y','--object-streams=generate',
                '_v3_rast.pdf', OUT], check=True)

print('BUILT', OUT, len(pdf.pages), 'pages')
print('E38 at p', fp('E38'), '| E39 at p', fp('E39'), '| E43 at p', fp('E43'))
