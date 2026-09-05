from build_ce_letter_pdf import build, rule, TITLE, SUBT, BLK, HEAD, BODY, SMALL
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import Paragraph as P, Spacer

SRC = PS('sr', fontName='Helvetica-Bold', fontSize=9.2, leading=12, spaceBefore=7, spaceAfter=2)
QUO = PS('qu', fontName='Helvetica-Oblique', fontSize=9.2, leading=12.4, leftIndent=8*mm,
         rightIndent=3*mm, spaceAfter=3)
NOTE= PS('nt', fontName='Helvetica', fontSize=9.0, leading=12, leftIndent=8*mm, spaceAfter=3)

def foot(c, d):
    c.saveState(); c.setFont('Helvetica',7.6); c.setFillColor(colors.HexColor('#777777'))
    c.setStrokeColor(colors.HexColor('#cccccc')); c.setLineWidth(0.4)
    c.line(25*mm, 15*mm, 185*mm, 15*mm)
    c.drawString(25*mm, 11*mm, 'Cory Lea Shepherd · MSH-INJ-5795 · Schedule of provisions relied on')
    c.drawRightString(185*mm, 11*mm, 'Page %d' % c.getPageNumber())
    c.restoreState()

f=[P('Schedule of the provisions relied on', TITLE),
   P('Enclosure 4 to my letter of 5 September 2026', SUBT),
   P('Cory Lea Shepherd', BLK),
   P('Employee number 388372 &#183; Employee reference MSH-INJ-5795', BLK),
   P('Date:&#160;&#160;5 September 2026', BLK),
   Spacer(1,7), rule(), Spacer(1,6),
   P('Quotations are exact, and clause numbers are given so that each may be checked. The '
     'instruments themselves are not enclosed, as the Health Service holds them.', BODY)]

DATA=[('A. SPECIAL LEAVE ON FULL PAY',[
 ('Certified Agreement (No. 12) 2025, cl 9.12.1',
  '&#8220;The parties agree the Minister for Employment and Industrial Relations Directive 12/24: '
  'Special Leave applies to all employees covered by this Agreement.&#8221;',None),
 ('Directive 12/24 &#8212; Special Leave, cl 6.1',
  '&#8220;A chief executive may approve paid leave for employees for any purpose, with duration '
  'appropriate to the purpose of the leave.&#8221;',None),
 ('Directive 12/24, cl 6.1(a)',
  '&#8220;Leave approved under clause 6.1 must not exceed more than five (5) working days per year '
  'per reason unless the chief executive considers that circumstances warrant the granting of '
  'additional paid leave. Any additional leave must be reasonable and proportionate to the '
  'circumstances.&#8221;',None),
 ('Directive 12/24, cl 6.5',
  '&#8220;In determining an application for leave under clause 6.1 or clause 6.2, a chief executive '
  'must consider: (a) the reason the leave is requested; (b) the duration of the requested leave; '
  '(c) if applicable, for fixed term temporary employees, the duration of the person&#8217;s '
  'employment (including end date); (d) the impact on the employee if the requested leave is not '
  'approved.&#8221;',None)]),
('B. LONG SERVICE LEAVE &#8212; ACCESS AFTER SEVEN YEARS',[
 ('Hospital and Health Service General Employees (Queensland Health) Award &#8211; State 2015, cl 22(c)',
  '&#8220;Employees who have completed 7 years&#8217; continuous service are entitled to take long '
  'service leave on full pay or half pay.&#8221;',None),
 ('Directive 10/24 &#8212; Long Service Leave (current from 30 September 2024, superseding 11/18), cl 8.1',
  '&#8220;Subject to clause 7.1, employees are entitled to take pro rata long service leave after '
  '7 years continuous service.&#8221;',None),
 ('HR Policy C38 &#8212; Long Service Leave (QH-POL-163), &#167;1',
  '&#8220;Queensland Health employees may apply for pro rata long service leave on full pay, or '
  'half pay, after completing seven years continuous service&#8230;&#8221;',None),
 ('Certified Agreement (No. 12) 2025, cl 9.10.1',
  '&#8220;Long service leave entitlements and conditions are outlined in HR Policy C38 Long Service '
  'Leave.&#8221;',None)]),
('C. THE OBLIGATION TO ANSWER AN APPLICATION',[
 ('Directive 10/24, cl 7.4',
  '&#8220;The employer must respond to a request to take long service leave in a timely manner '
  'indicating whether the leave applied for has been approved or not.&#8221;',None),
 ('HR Policy C38, Attachment One',
  '&#8220;Granting of long service leave, including on a half pay basis, is subject to '
  'organisational convenience however requests for leave are not to be unreasonably '
  'refused.&#8221;<br/>&#8220;The employee is to be given timely advice as to whether or not leave '
  'is approved.&#8221;',None),
 ('HR Policy C38, &#167;2',
  '&#8220;For leave on full pay - the minimum leave taken at any one time is one day, or one '
  'rostered shift.&#8221;',None)]),
('D. COMMENCEMENT DATE',[
 ('Deed of Settlement executed 21 February 2025, recital B',
  '&#8220;The Employment commenced on 25 March 2019.&#8221;',
  'Seven years of continuous service accordingly fell due on 25 March 2026.')])]

for h,items in DATA:
    f.append(P(h, HEAD))
    for s,q,n in items:
        f.append(P(s,SRC)); f.append(P(q,QUO))
        if n: f.append(P(n,NOTE))

print('schedule pages:', build(f,'out/SCHEDULE_OF_PROVISIONS_5SEP2026.pdf', foot))
