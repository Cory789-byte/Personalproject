#!/usr/bin/env python3
"""WC/2024/227 - MAY 2024, DAY BY DAY. Internal working chronology: what I was rostered, whether I
attended, and what was happening. Roster and leave from the employer's own records; events from the
notice to admit facts served 28 August 2026. Not for filing or service. Metadata stripped."""
import io, pikepdf, sys, datetime as dt, collections, openpyxl
sys.path.insert(0,'.'); from roster_data import R, cells
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Table, TableStyle, Spacer
PS=landscape(A4); W=PS[0]-24*mm
HD=ParagraphStyle('HD',fontName='Helvetica-Bold',fontSize=8.4,leading=10.5,textColor=colors.HexColor('#333333'))
T=ParagraphStyle('T',fontName='Helvetica-Bold',fontSize=13,leading=16,spaceAfter=2)
SUB=ParagraphStyle('S',fontName='Helvetica-Oblique',fontSize=8,leading=10.5,textColor=colors.HexColor('#555555'),spaceAfter=7)
H1=ParagraphStyle('H1',fontName='Helvetica-Bold',fontSize=11,leading=14,spaceBefore=7,spaceAfter=4)
B=ParagraphStyle('B',fontName='Helvetica',fontSize=8.9,leading=11.4,spaceAfter=4)
C=ParagraphStyle('C',parent=B,fontSize=7.5,leading=9.3,spaceAfter=0)
CB=ParagraphStyle('CB',parent=C,fontName='Helvetica-Bold')
def P(t,s=B): return Paragraph(t,s)
def c(t,bold=False): return Paragraph(t,CB if bold else C)

EV={
 dt.date(2024,5,1):["<b>1:18 pm</b> &ndash; I email Ms Reese citing the Operations Manual fatigue toolkit: \"This section includes a toolkit required by management to manage fatigue\" and \"I forwarded the toolkit to Chloe last week for review and action but have yet to receive feedback\". <i>[Notice &para;&para;214&ndash;215]</i>",
                    "Ms Taylor refuses fatigue leave for 18 March 2024, 23 days after the request of 8 April, \"due to the existing 8-hour agreement signed by you on 17 June 2020\". <i>[Review Decision, Notice &para;&para;250&ndash;253]</i>"],
 dt.date(2024,5,3):["<b>3:06 pm</b> &ndash; Vivian Kwok, MASPER Registrar, emails Ms Taylor listing five occasions on 2 and 3 May where calls reached the wrong team, including the MET call team ringing because \"switchboard could not tell them where VHUB was\". <i>[&para;&para;56&ndash;58]</i>",
                    "Ms Elaine Grant of Payroll emails Ms Taylor, copying me, identifying incorrect payments across four fortnights: \"Please submit an AVAC to correct these shifts for each fortnight\". <i>[&para;&para;183&ndash;190]</i>"],
 dt.date(2024,5,8):["<b>9:08 am</b> &ndash; Ms Reese replies that she is \"following up with regards to these with HR for further advice\". <i>[&para;217]</i>",
                    "<b>5:28 pm</b> &ndash; Vivian Kwok emails again, four further occasions on 5, 7 and 8 May, twice \"incorrectly put through to MASPER\". Nine occasions in all. <i>[&para;&para;59&ndash;61]</i>"],
 dt.date(2024,5,9):["<b>9:20 am</b> &ndash; Ms Taylor's first response, five days and eighteen hours after the first report, asking Dr Wong to confirm her business hours because they are \"not provided on the rosters\", and noting her phone is \"currently switched off\". <i>[&para;&para;63&ndash;65]</i>",
                    "<b>10:15 am</b> &ndash; Ms Taylor tells Logan Switch there have been \"many ongoing issues raised by the MASPER and the medical department about calls being transferred to the wrong medical teams\". <i>[&para;&para;66&ndash;67]</i>"],
 dt.date(2024,5,10):["<b>2:08 pm</b> &ndash; Ms Reese emails Mr Mackenzie Pritchard of HR: I have \"concerns over how his manager is rostering... and how it is impacting on staff fatigue\"; on the Roster Risk Assessment Matrix \"at best there would be a rating of 11 which is moderate\"; and \"I acknowledge there has been a few rostering errors made by Chloe with regards to Cory's line in past rosters\". <i>[&para;&para;219&ndash;221]</i>",
                     "<b>2:21 pm</b> &ndash; I email Payroll and Ms Grant. <i>[&para;191]</i>"],
 dt.date(2024,5,13):["<b>8:21 am</b> &ndash; Payroll to me: \"I cannot see that any of the issues below have been corrected. Please speak to your Line Manager to have them corrected with an AVAC submitted through My HR.\" <i>[&para;&para;192&ndash;193]</i>",
                     "I make the complaint later determined by the Ethical Standards Unit to be a public interest disclosure. <i>(content not set out)</i>",
                     "<b>4:29 pm</b> &ndash; Ms Stibbard circulates the on-call roster: she is on call 13&ndash;19 May, Ms Taylor 20&ndash;26 May; \"During business hours you are to still contact Chloe.\" <i>[&para;&para;111&ndash;112]</i>"],
 dt.date(2024,5,14):["<b>12:08 pm</b> &ndash; Ms Taylor emails me, copying Ms Reese, subject \"Sick leave 14.05.24\": \"in business hours you are to follow the correct process and speak to me directly if its regarding emergent leave, you can contact me either through switch or my office/mobile.\" <i>[&para;&para;163&ndash;164]</i>"],
 dt.date(2024,5,15):["<b>11:47 am</b> &ndash; Ms Sue Marriott, Integrated Respiratory Service, emails Logan Switch, High importance: \"Could you please amend your number registry/directory to show #8768 belongs to the Integrated Respiratory Service... We are not Respiratory Medical OPD and we do not have any doctors working out of this area.\" <i>[&para;89]</i>",
                     "<b>1:15 pm</b> &ndash; I email Ms Taylor and Logan Switch, copying the Switchboard staff, Ms Reese and LBH_HR: \"could you please share your office hours so the entire department can be aware of your regular schedule? There has been some noted inconsistency in your arrival and departure times\", and asking that directives be made \"in consultation with the team\". <i>[&para;&para;74&ndash;75]</i>",
                     "<b>6:23 pm</b> &ndash; Ms Reese replies, High importance, that the email \"did not demonstrate our iCARE2 value of Respect and did not comply with our Code of conduct\", and asks me to retract it. <i>[&para;&para;76&ndash;77]</i>",
                     "<b>7:09 pm</b> &ndash; I reply: \"Requesting clarity on business hours is a reasonable question, especially when no one in the department can provide a definitive answer in response to directives to contact Chloe during office hours.\" <i>[&para;78]</i>"],
 dt.date(2024,5,16):["General practice, Dr William Zhao: \"renew referral to psychiatrist\"; letter written to Dr Arash Amini. <i>[General-practice records]</i>"],
 dt.date(2024,5,17):["<b>9:30 am</b> &ndash; Ms Taylor emails the whole department, subject \"Switchboard Manager - On call and Hours.\": \"My office hours can vary due to having to take my girls to school in the morning... Otherwise my hours are from 06:30-14:30\", and undertakes to \"advise of any change to my office hours for the week\". Two days after I was asked to retract the email asking for exactly that. <i>[&para;&para;81&ndash;84]</i>"],
 dt.date(2024,5,20):["<b>11:03 am</b> &ndash; Ms Marriott emails again, High importance, on the fifth calendar day after her first: \"we continue to get calls put through to us for Respiratory Medical Outpatients... we can not help patients or other clinical staff with OPD issues.\" <i>[&para;&para;91&ndash;92]</i>",
                     "<b>2:05 pm</b> &ndash; I reply, High importance, five minutes after my shift ends: switchboard staff \"may not be aware of the clinics due to modifications to the Document: Outpatients Department - Clinic contact Details. on the 22nd of February 2024. I recommend a modification and review of the document.\" <i>[&para;&para;96&ndash;98]</i>",
                     "<b>4:07 pm</b> &ndash; Ms Reese emails LBH_HR attaching the Queensland Health Fatigue Risk Management Systems Implementation Guideline. <i>[&para;222]</i>",
                     "<b>4:30 pm</b> &ndash; Ms Taylor replies to me, two hours after her own stated hours ended: \"this task was being actioned. I had discussed with Richard this morning about the update of outpatients respiratory/medical\", adding that the updated procedures could go \"out to the team for consultation before implementing\". <i>[&para;&para;99&ndash;101]</i>"],
 dt.date(2024,5,21):["<b>12:33 pm</b> &ndash; Ms Taylor emails me: \"I am still I am waiting payroll confirmation about a few of these payroll issues and as soon as I do get that confirmation, I will submit an AVAC for next pay run.\" <i>[&para;&para;194&ndash;195]</i>",
                     "<b>2:53 pm</b> &ndash; Ms Reese: \"With regards to your concerns about having more clarity as to what are Chole's business hours I will follow up on the issues raised\", and asks \"was there one or more particular changes and/or directives where you had concerns about consultation and communication?\" <i>[&para;&para;79&ndash;80]</i>"],
 dt.date(2024,5,28):["<b>8:36 am</b> &ndash; Ms Taylor asks me to sign a \"Validation of claims older than 3 months\" so she can \"escalate for delegate approval\". <i>[&para;&para;196&ndash;197]</i>",
                     "The AVAC Payroll asked for on 3 May is submitted, process 16450619, effective 30 March 2024, status \"Part Completed\". 25 days after the instruction. <i>[&para;&para;203&ndash;204]</i>"],
}
L={}
for st,(lab,line,unc) in R.items(): L.update(cells(st,line))
wb=openpyxl.load_workbook('../documents/2026-09-04_Leave_Takings_Report_25MAR2019-04SEP2026_FULL.xlsx',read_only=True,data_only=True)
lv=collections.defaultdict(list)
for ws in wb.worksheets:
    for r in ws.iter_rows(values_only=True):
        if r and len(r)>8 and r[1]=='00388372' and r[6]:
            rng=str(r[6]).split(' - ')
            d0=dt.datetime.strptime(rng[0].strip(),'%d/%m/%Y').date()
            d1=dt.datetime.strptime(rng[-1].strip(),'%d/%m/%Y').date()
            for k in range((d1-d0).days+1): lv[d0+dt.timedelta(k)].append((str(r[4]),float(r[7] or 0)))

s=[P("QUEENSLAND INDUSTRIAL RELATIONS COMMISSION",HD),
   P("Matter No. WC/2024/227 | Cory Lea Shepherd (Appellant) v Workers' Compensation Regulator (Respondent)",HD),
   P("MAY 2024, DAY BY DAY",T),
   P("What I was rostered, whether I attended, and what was happening. Roster from the published Switchboard roster for "
     "13 to 26 May 2024 and the fortnight before it; attendance from the Payroll leave takings report of 4 September 2026; "
     "events from the notice to admit facts served on the Respondent on 28 August 2026, with paragraph numbers. Prepared "
     "6 September 2026. INTERNAL working chronology, not for filing or service.",SUB)]
rows=[[Paragraph(x,CB) for x in ["Date","Rostered","Attended","What happened"]]]
for k in range((dt.date(2024,5,31)-dt.date(2024,5,1)).days+1):
    d=dt.date(2024,5,1)+dt.timedelta(k)
    cell=L.get(d,'&mdash;')
    lvs=lv.get(d,[])
    if cell in ('-','&mdash;'): ros='not rostered'
    elif cell=='x': ros='marked off'
    elif cell=='RDO': ros='RDO'
    else: ros=cell
    if lvs:
        att='<b>ABSENT</b><br/>'+'<br/>'.join(f"{t} {h:.1f}h" for t,h in lvs)
    elif cell in ('-','x','RDO','&mdash;'): att='&mdash;'
    else: att='<b>worked</b>'
    ev=EV.get(d)
    body='<br/><br/>'.join(ev) if ev else '&mdash;'
    rows.append([c(f"<b>{d.strftime('%a %d %b')}</b>"),c(ros),c(att),c(body)])
t=Table(rows,colWidths=[20*mm,24*mm,40*mm,W-84*mm],repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.35,colors.HexColor('#999999')),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#EEEEEE')),
 ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
 ('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
s.append(t)
s.append(P("What the month shows",H1))
for t_ in [
 "<b>I raised fatigue on 1 May and was refused the same day.</b> The toolkit had gone to Ms Taylor the week before and had "
 "not been answered. The Respondent does not allege she ever reviewed it.",
 "<b>Between 2 and 8 May the Switchboard misdirected nine clinical calls</b>, reported by the MASPER Registrar in two emails. "
 "The manager's first response came on 9 May, five days and eighteen hours after the first report, and it was to ask a doctor "
 "for her own business hours because they were \"not provided on the rosters\", and to note that the doctor's phone was "
 "switched off. The information the operators did not have, the manager did not have either.",
 "<b>On 10 May the Director wrote to Human Resources</b> recording my fatigue concerns, a roster risk rating of 11, and \"a "
 "few rostering errors made by Chloe with regards to Cory's line in past rosters\". That is the employer, internally, on the "
 "same point I had raised on 1 May.",
 "<b>I was absent on 13, 14 and 15 May</b>, two days sick and one on recreation leave. The public interest disclosure was made "
 "on 13 May. On 14 May, while I was on sick leave, I was told the correct process for notifying leave. On 15 May, while on "
 "recreation leave, I asked for the manager's office hours and was asked that evening to retract it.",
 "<b>Ms Marriott's first respiratory email arrived at 11:47 am on 15 May</b>, two hours before mine and on the same day. The "
 "directory was still wrong five days later.",
 "<b>On 16 May, the day after being asked to retract, I saw my general practitioner and the psychiatric referral was renewed.</b>",
 "<b>On 17 May Ms Taylor told the whole department her office hours.</b> Two days after I had been asked to withdraw the email "
 "asking for them. I had complied.",
 "<b>I returned to work on 18 May and worked six consecutive shifts</b>: three earlies, then three nights, 18 to 23 May.",
 "<b>The respiratory failure was answered on my return.</b> Ms Marriott wrote again at 11:03 am on 20 May, on the fifth "
 "calendar day, saying \"we can not help patients or other clinical staff\". I replied at 2:05 pm, five minutes after my "
 "06:00&ndash;14:00 shift ended. Ms Taylor replied at 4:30 pm, two hours after the office hours she had stated three days "
 "earlier, to say the task \"was being actioned\". The Respondent's amended List of Documents lists no document created that "
 "day recording that discussion, and none recording any communication to Ms Marriott.",
 "<b>The pay was still not corrected.</b> Payroll instructed on 3 May; told me on 13 May that nothing had been corrected and "
 "to speak to my line manager; on 21 May my manager was still \"waiting payroll confirmation\"; on 28 May I was asked to sign "
 "a validation of claims older than three months, and the AVAC went in that day, 25 days after the instruction, and is the "
 "only one in the period recorded as \"Part Completed\".",
 "<b>And then I lost the rest of the month.</b> Carer's leave charged to my recreation leave on 27, 28 and 29 May, and sick "
 "leave charged to recreation leave on 31 May. Of the ten shifts I was rostered from 27 May, I attended two.",
]: s.append(P(t_))
buf=io.BytesIO(); doc=BaseDocTemplate(buf,pagesize=PS,leftMargin=12*mm,rightMargin=12*mm,topMargin=11*mm,bottomMargin=13*mm)
def footer(cv,d):
    cv.saveState(); cv.setFont('Helvetica',7); cv.setFillColor(colors.HexColor('#666666'))
    cv.drawString(12*mm,7*mm,"WC/2024/227 - May 2024 day by day - INTERNAL, NOT FOR SERVICE")
    cv.drawRightString(PS[0]-12*mm,7*mm,f"Page {d.page}"); cv.restoreState()
doc.addPageTemplates([PageTemplate(id='n',frames=[Frame(12*mm,13*mm,PS[0]-24*mm,PS[1]-24*mm,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=footer)])
doc.build(s); buf.seek(0); pdf=pikepdf.open(buf)
try: del pdf.Root.Metadata
except (AttributeError,KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out="out/MAY2024_DAY_BY_DAY_INTERNAL.pdf"; pdf.save(out,linearize=True); print("built",out,len(pdf.pages),"pages")
