import re, sys, os
D=sys.argv[1]
def grab(fn, start, end=None):
    t=open(os.path.join(D,fn),encoding='utf-8',errors='ignore').read()
    i=t.find(start); assert i>=0, (fn,start)
    j=t.find(end,i) if end else len(t)
    return re.sub(r'\s+',' ',t[i:j if j>0 else len(t)])
texts={
 "Feb 11 urgent filing":   grab("p1_feb11_urgent.txt","1. Notification of Representation Change","Yours faithfully"),
 "Feb 17 Calderbank 1":    grab("p1_feb17_calderbank1.txt","Please find attached my Without Prejudice","Yours faithfully"),
 "Mar 20 update":          grab("p2_mar20_update.txt","I refer to the conference held","Yours faithfully"),
 "Jul 01 Calderbank 2":    grab("p3_jul01_calderbank2.txt","I refer to the above appeal","Yours faithfully"),
 "Jul 31 WP letter":       grab("p3_jul31_wp.txt","I write to inform the Respondent","Yours"),
 "Aug 28 notices email":   grab("p4_aug28_in_reply.txt","I refer to this appeal.","Yours sincerely"),
 "Sep 09 footing letter":  grab("p5_sep09_letter.txt","Thank you for the responses of 8 September","Yours faithfully"),
 "Oct 19 six matters":     grab("p6_oct19_letter_full.txt","The documents. With those confirmations","Yours sincerely"),
}
M={
 "intensity": r"\burgent(ly)?\b|\bimmediate(ly)?\b|\bSEAL\b|\bmust\b|\bdeemed\b|!",
 "accusation": r"unlawful|violat|breach|reprisal|hostil|deliberate|embarrass|denied me|misconduct|detriment",
 "rules cited": r"\b(Section|section|s|Rule|rule|r)\s?\d+[A-Z]?\b|Human Rights Act|Practice Direction",
 "anchors": r"\bfacts? \d+|\[¶|\bTabs? \d+|admitted|admission",
 "courtesy": r"\bplease\b|grateful|thank|\bcould\b|\bwould\b",
 "dated asks": r"\bby (4\.00 pm|4:00 pm|Friday|Monday|Tuesday|Wednesday|Thursday)\b|\bwithin \d+ days\b",
 "disclaims": r"does not contend|draws no characterisation|not relied (on|upon)|does not rely|would not require",
}
I_RX=r"\bI\b"; APP_RX=r"\bthe Appellant\b"
def ws(t): return re.findall(r"[A-Za-z][A-Za-z'’-]*",t)
hdr=f"{'text':24}{'words':>6}{'w/sent':>7}"+"".join(f"{k:>12}" for k in M)+f"{'I':>5}{'Appellant':>10}"
print(hdr)
for k,t in texts.items():
    w=ws(t); n=len(w); s=max(1,len(re.findall(r"[.?!](\s|$)",t)))
    row="".join(f"{100*len(re.findall(rx,t))/n:12.1f}" for rx in M.values())
    i_n=len(re.findall(I_RX,t)); a_n=len(re.findall(APP_RX,t))
    print(f"{k:24}{n:6}{n/s:7.1f}{row}{i_n:5}{a_n:10}")
print("\n(feature columns are counts per 100 words)")
for k in ["Feb 11 urgent filing","Oct 19 six matters"]:
    t=texts[k]
    for name in ["intensity","accusation","disclaims"]:
        hits=[m.group(0) for m in re.finditer(M[name],t)]
        print(f"  {k} / {name}: {hits[:12]}")
