#!/usr/bin/env python3
"""Parse the 2025-26 text-layer Switchboard rosters: extract every staff line, cell by cell."""
import subprocess, re, glob, os, datetime as dt
DIR='../documents/rosters/2025-26_published'
LEAVE={'A/L','S/L','LWOP','RDO','N/A','SICK','LSL','P/L','x','X'}
def parse(path):
    txt=subprocess.run(['pdftotext','-layout',path,'-'],capture_output=True,text=True).stdout
    lines=txt.split('\n')
    hdr=None
    for ln in lines:
        ds=list(re.finditer(r'\d\d-[A-Z][a-z]{2}-\d\d',ln))
        if len(ds)>=10: hdr=ds; break
    if not hdr: return None
    bounds=[]
    for i,m in enumerate(hdr):
        lo=m.start()-6 if i==0 else (hdr[i-1].end()+hdr[i].start())//2
        hi=(hdr[i].end()+hdr[i+1].start())//2 if i+1<len(hdr) else m.end()+9
        bounds.append((max(0,lo),hi))
    dates=[dt.datetime.strptime(m.group(),'%d-%b-%y').date() for m in hdr]
    staff=[]
    for ln in lines:
        m=re.match(r'\s*(\d{5,8})\s+([A-Z] - )?([A-Za-z][A-Za-z \'\-\.]+?)\s{2,}',ln)
        if not m: continue
        cells=[]
        for lo,hi in bounds:
            c=ln[lo:hi].strip() if lo<len(ln) else ''
            c=re.sub(r'\s+','',c)
            cells.append(c if c else '-')
        staff.append((m.group(1), m.group(3).strip(), cells))
    return dates, staff
if __name__=='__main__':
    for f in sorted(glob.glob(DIR+'/*.pdf')):
        r=parse(f)
        if not r: print(os.path.basename(f),'PARSE FAIL'); continue
        dates,staff=r
        sh=[s for s in staff if 'Shepherd' in s[1]]
        print(f"\n{os.path.basename(f)}  {dates[0]} to {dates[-1]}  ({len(staff)} staff rows)")
        if sh: print("   SHEPHERD:", ' | '.join(sh[0][2]))
        else:  print("   *** NO SHEPHERD LINE ***")
