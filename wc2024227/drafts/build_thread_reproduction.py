import re, io, glob, os, datetime as dt
from dateutil import parser as dp
S='/tmp/claude-0/-home-user-Personalproject/a3f5ec62-69fa-5452-a28c-d1c8e460180e/scratchpad/thread'
SOURCES=[  # order irrelevant; dedupe + sort handles it
 '2026-07-03_1518_Cory_to_Taylor_ECC_LeaveType_reply','2026-07_Cory_to_InjuryMgmt_ECC_further_information_FULL_THREAD_12pp',
 '2026-07-15_Harrison_reply_pay_refused_discretion','2026-07-28_1739_Cory_to_HR_incorrect_application_EB12_Award_policies',
 '2026-07-29_1610_MSH_reply_to_28July_letter','2026-07-30_1125_Cory_reply_to_MSH_29July','2026-07-30_1433_MSH_holding_reply_delegate_approval',
 '2026-08-05_0730_SENT_Stage1_reply_cover_email','2026-08-13_1548_Harrison_reply_consent_and_EAF',
 '2026-08-13_1642_Roberts_FollowUpOnEnquiries_RECALLED','2026-08-18_1047_Roberts_FollowUpOnEnquiries_RESENT_personal_email',
 '2026-08-18_to_28_Roberts_FollowUpOnEnquiries_FULL_THREAD','2026-08-25_1508_Roberts_Teams_invite',
 '2026-08-31_FULL_THREAD_v2_Taylor_LSL_AVAC_incl_1606_correction']
HDR=re.compile(r'^\s*From:\s*(.*)$')
FIELD=re.compile(r'^\s*(To|Cc|Sent|Subject):\s*(.*)$')
BOILER=[r'This email originated from outside Queensland Health', r'DO NOT click on any links', r'you recognise the sender', r'^\s*safe\.\s*$',
        r'Get Outlook for Android', r'acknowledges the Traditional Custodians', r'Elders past and present', r'recognises and pays respect',
        r'Jaggera, Ugarapul', r'past, present and emerging', r'^\s*\*{10,}\s*$']
DISCLAIM_START=re.compile(r'^\s*Disclaimer: This email and any attachments',re.I)
DISCLAIM_END=re.compile(r'appropriate use of its\s*$|computer network\.\s*$')
SOLV_START=re.compile(r'Please be advised that we are currently'); SOLV_END=re.compile(r'via the above contact details')

def parse_sent(s):
    s=s.strip(); s=re.sub(r'\s+at\s+',' ',s); s=re.sub(r'^\w+,?\s+','',s)   # drop weekday
    try: d=dp.parse(s, default=dt.datetime(2026,1,1))
    except Exception: return None
    if d.year!=2026: d=d.replace(year=2026)
    return d

def clean(lines):
    out=[]; skip=False
    for ln in lines:
        if skip:
            if DISCLAIM_END.search(ln) or SOLV_END.search(ln): skip=False
            continue
        if DISCLAIM_START.search(ln) or SOLV_START.search(ln): skip=True; continue
        if any(re.search(p,ln) for p in BOILER): continue
        out.append(ln.rstrip())
    # collapse >2 blank lines
    res=[]; blank=0
    for ln in out:
        if ln.strip()=='' :
            blank+=1
            if blank>1: continue
        else: blank=0
        res.append(ln)
    while res and res[0].strip()=='': res.pop(0)
    while res and res[-1].strip()=='': res.pop()
    return res

msgs=[]
for src in SOURCES:
    L=open(f'{S}/{src}.txt',encoding='utf-8',errors='replace').read().splitlines()
    # find header starts: a From: line with a Sent: within the next 8 lines
    starts=[i for i,ln in enumerate(L) if HDR.match(ln) and any(FIELD.match(L[j]) and FIELD.match(L[j]).group(1)=='Sent' for j in range(i+1,min(i+9,len(L))))]
    for k,i in enumerate(starts):
        end=starts[k+1] if k+1<len(starts) else len(L)
        blk=L[i:end]
        frm=HDR.match(blk[0]).group(1).strip(); j=1; fields={}
        # header lines: continuation lines (emails) allowed until Sent/Subject seen and a blank line
        while j<len(blk) and j<14:
            m=FIELD.match(blk[j])
            if m: fields[m.group(1)]=m.group(2).strip(); j+=1; continue
            if blk[j].strip()=='' and 'Sent' in fields: j+=1; break
            if 'Sent' not in fields and '@' in blk[j] and 'From' not in fields:  # email continuation under From
                fields['From']=blk[j].strip(); j+=1; continue
            if blk[j].strip()=='' : j+=1; continue
            # continuation of To/Cc line (mobile export wraps) — only before Sent
            if 'Sent' not in fields: j+=1; continue
            break
        sent=parse_sent(fields.get('Sent',''))
        if not sent: continue
        body=clean(blk[j:])
        who=re.sub(r'<.*?>','',frm).strip()
        if 'LBH Injury Management' in who: who='LBH Injury Management (Michelle Harrison)' if any('Michelle Harrison' in b for b in body) else 'LBH Injury Management'
        msgs.append(dict(src=src,when=sent,frm=who,to=fields.get('To',''),cc=fields.get('Cc',''),subj=fields.get('Subject',''),body=body,top=(k==0)))

# dedupe: same sender-surname + within 3 minutes
def key(m): return (re.sub(r'\W','',m['frm'].split('(')[0].lower())[:12], m['when'])
uniq=[]
for m in sorted(msgs,key=lambda m:(m['when'],-len(m['body']))):
    dup=None
    for u in uniq:
        if key(u)[0]==key(m)[0] and abs((u['when']-m['when']).total_seconds())<=180: dup=u; break
    if dup:
        if len(m['body'])>len(dup['body']) or (m['top'] and not dup['top'] and len(m['body'])>=len(dup['body'])*0.9):
            for f in ('body','src','top'): dup[f]=m[f]
            for f in ('to','cc','subj'):
                if not dup[f] and m[f]: dup[f]=m[f]
        continue
    uniq.append(m)
uniq.sort(key=lambda m:m['when'])
# the 22 July payroll enquiry — a portal item, not an email; insert as its own entry
pe=open(f'{S}/2026-07-22_Payroll_Enquiry_4438861_PendingInvestigation.txt',encoding='utf-8',errors='replace').read().splitlines()
uniq.append(dict(src='2026-07-22_Payroll_Enquiry_4438861_PendingInvestigation',when=dt.datetime(2026,7,22,12,0),frm='Cory Shepherd (payroll enquiry portal)',to='Queensland Health Payroll',cc='',subj='Payroll Enquiry 4438861 — status "Pending Investigation"',body=clean(pe),top=True))
uniq.sort(key=lambda m:m['when'])
for n,m in enumerate(uniq,1):
    print(f"{n:2d}. {m['when']:%a %d %b %Y %H:%M}  {m['frm'][:34]:34s} -> {m['to'][:28]:28s} | {m['subj'][:40]:40s} | {len(m['body'])} lines | {m['src'][:28]}")
import pickle; pickle.dump(uniq,open(f'{S}/messages.pkl','wb'))
