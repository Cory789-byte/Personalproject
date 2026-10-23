# Forensic features of every Regulator-authored text held verbatim, Dec 2024 to 20 Oct 2026.
# Bodies only (salutations, signatures, disclaimers and quoted text removed). Salutations are coded by hand
# below from the originals. Sources: analysis/stylometry/matheson_style.py (B01-B22, S1, T1-T4, L1) plus the
# originals read from Gmail on 21 Oct 2026 (E-*). B23/B24 (openings only) are replaced by the full texts.
import re, collections

src = open(__file__.replace('forensic/regulator_forensic.py', 'stylometry/matheson_style.py')).read()
s = src.index('T = {'); e = src.index('\n}\n', s) + 3
ns = {}; exec(src[s:e], ns); T = {k: v for k, v in ns['T'].items() if not k.startswith(('B23', 'B24'))}

E = {
"E 2024-12-02 Registry (Appeals Support)": "The Respondent has considered the request to extend time. The Respondent has accepted extension and is happy for the appeal to proceed. The Respondent will wait for the directions to be issued.",
"E 2024-12-04 Cory (Appeals Support form letter)": "On behalf of the Workers' Compensation Regulator I acknowledge your letter dated 27 November 2024 enclosing a copy of the notice of appeal that was filed in the Queensland Industrial Relations Commission on 26 November 2024. The appeal has been allocated to an Appeals Officer. The Appeals Officer will contact you in the near future to discuss the matter. If you have any additional information to support your case, please provide it to us as early as possible. Please note that it is the Workers' Compensation Regulatory Services' preference to receive all correspondence electronically. I would like to bring to your attention that if the Workers' Compensation Regulator is successful in this appeal, it reserves the right to seek an order from the Commission for Cory Lea Shepherd to pay their costs in accordance with Schedule 2, Part 2, Scale C of the Uniform Civil Procedure Rules 1999 as directed by s.132 of the Workers' Compensation and Rehabilitation Regulation 2014.",
"E 2024-12-17 Cory": "I am emailing in relation to the above matter before the Queensland Industrial Relations Commission (QIRC). As mentioned in the below email sent 4 December 2024, I am the Appeals Officer with carriage of this appeal on behalf of the Workers' Compensation Regulator (the Respondent). Workers' Compensation appeals are conducted on a de novo basis, which results in an in-person hearing before a Commissioner in a courtroom setting of the QIRC. At the hearing, both parties present evidence through witness testimony and the tendering of documents. The Commissioner then makes a fresh decision regarding your claim for workers' compensation under section 32 of the Act without direct regard to the decisions made by WorkCover Queensland or the Regulator's Review Unit. Please be aware that the Regulator's role in the appeals process is to defend the decision made by the Review Unit - however the Regulator does not defend review decisions at all costs and depending on what new information, if any, is obtained during the course of the appeals process, we may decide to concede an appeal. Before an appeal goes to hearing, there are a number of steps which both yourself and the Regulator are required to complete as outlined in the initial Directions Order of the QIRC (attached). The first of these is for us both to provide one another with a list of all of the relevant documents that we currently have in our possession or control by 4:00pm on 15 January 2025 (points 1 & 2). As per the directions order, please also see (attached) the Regulator's list of documents. If you require any copies of the documents that are listed, please let me know by reply email and I will forward copies to you. If you have any questions in relation to any of this information, please feel free to contact me on the below details.",
"E 2025-01-16 Cory": "Thank you for your below email and the disclosed documents. Could I please confirm if you had a list of documents that are in your possession or under your control as listed in the QIRC directions order dated 3 December 2024? For your reference I have again attached our list of documents of what we currently have. If you require any documents from our list, please let me know and I will be happy to send you a copy. These lists enable the parties to confirm that we have the same information going forward in the appeal. If you have nothing new to list aside from the witness statements you mentioned, you do not need to create a list. Throughout the appeal process, as you get new evidence you can simply disclose it to me via email. I will do the same if the Regulator comes into possession of new evidence through the process. Once we have exchanged documents and confirmed we both have the same information, we will have completed the directions order with the final step (5) is for you to contact the QIRC when you are ready for the matter to proceed to a s552A conference. If you have any questions in relation to the above, please do not hesitate to contact me.",
"E 2025-02-11 Cory": "My apologies I missed your call yesterday afternoon. I have reviewed all of the documentation on your file, from both the WorkCover and Review unit processes, as well as the additional documentation you have sent me directly. After considering all of the information, it is the position of the Regulator to continue to the defend the appeal before the Queensland Industrial Relations Commission (QIRC). Please note that the only events relevant to be considered at appeal are those events leading up to your attendance at your GP when you were first assessed for the alleged injury. Any events post that date cannot be considered causative of you sustaining your alleged injury. Now that we have completed the directions order from the QIRC and as per order 5 of the directions order you are to contact the QIRC in order for the appeal to be set down for a s552A conference. At the conference, a member of the QIRC will speak with the parties and outline the next steps of the appeal process in detail and be available to answer any questions about the process that you may have. I also want to be clear, that this appeal is only in relation to your workers' compensation application. Any other matters that you have in the QIRC cannot be dealt with through this appeal process and will be dealt with separately at the QIRC. If you have any further questions, please do not hesitate to contact me.",
"E 2025-08-20a Cory": "We have been informed by Saines Legal that you are no longer being represented by them in relation to this appeal matter. I note from the attached QIRC Amended Further Directions Order (2), dated 16 July 2025, that you were to file and serve upon the registry and the Regulator a list of witnesses you will be calling to give evidence in this matter by 4pm on 13 August 2025. I understand this may be difficult now that you are no longer represented and wished to confirm that you can request an extension of time if needed. Simply email me the request and once I confirm the Regulator's consent, you then email the QIRC registry with your request. Alternatively, if you wish to continue in this appeal however need additional time and not sure how long you need, you can request the QIRC to place your matter in abeyance (on hold) and it can sit there for 12 months to await you to be ready to progress the matter again. Once it is in abeyance please note: The appellant is responsible for the matter proceeding and if no action is taken by you to progress the matter within 12 months of the last action, the matter will lapse pursuant to rule 230 of the Industrial Relations (Tribunals) Rules 2011. I hope this is of assistance, if you have any questions in relation to the above please do not hesitate to contact me.",
"E 2025-08-20b Cory": "Apologies, but I didn't receive this email of 14 August 2025 for some reason. I can confirm my email address is correct so unsure what has happened. As the Respondent, I am happy to consent to the two week extension that you have requested to 28 August 2025. If you were to forward this email with my consent to the QIRC registry, requesting the extension be granted, the QIRC should then provide us with a new directions order with new dates. should you require more time, please do not hesitate to contact me.",
"E 2026-08-28 Cory": "Thank you for your email and update in relation to a forthcoming expert report. The Regulator cannot confirm its witnesses at this stage. The parties should call witnesses who they consider will provide evidence in support of their case. In response to your concerns in relation to the Regulator's list, the parties can amend their list of witnesses with leave of the Commission, should changes become necessary.",
"E 2026-09-07 Cory": "The Regulator is currently reviewing this email and the forms 24 and 25 and I have just noticed that this email was only sent to myself and wanted to confirm for your information that these forms should also be filed with the QIRC registry if not already done so. The Regulator understands it is needing to response within14 days, meaning COB Friday 11 September 2026.",
}
ALL = {**T, **E}
def date(k): return re.search(r'(20\d\d-\d\d-\d\d)', k).group(1)
def period(d):
    return ("1 Dec24-Aug25" if d < "2026-01-01" else "2 Feb-Mar26" if d < "2026-04-01" else
            "3 Apr-Aug26" if d < "2026-09-01" else "4 Sep-Oct26")

# Salutations, coded from the originals (letters and Registry emails excluded)
SAL = {"2024-12-17": "Dear Mr Shepherd", "2025-01-16": "Hello Cory", "2025-02-11": "Good morning Cory",
       "2025-08-20a": "Dear Mr Shepherd", "2025-08-20b": "Hi Cory", "2026-02-12": "Dear Mr Shepherd",
       "2026-02-18": "Dear Mr Shepherd", "2026-03-20": "Good afternoon Mr Shepherd", "2026-06-11": "Dear Mr Shepherd", "2026-07-16": "Dear Mr Shepherd",
       "2026-08-03": "Dear Mr Shepherd", "2026-08-14": "Dear Mr Shepherd (x2)", "2026-08-28": "Dear Mr Shepherd",
       "2026-09-07": "Dear Mr Shepherd", "2026-09-08": "Dear Mr Shepherd", "2026-09-24": "Dear Mr Shepherd",
       "2026-10-07": "Dear Mr Shepherd", "2026-10-12": "Dear Mr Shepherd", "2026-10-16": "Dear Mr Shepherd",
       "2026-10-19": "Dear Mr Shepherd", "2026-10-20": "Dear Mr Shepherd"}

F = collections.OrderedDict([
 ("undated promise", r"as soon as possible|in the near future|in due course"),
 ("dated promise",   r"\bthis week\b|respond by (Monday|Tuesday|Wednesday|Thursday|Friday)"),
 ("not-yet marker",  r"at this stage|in the first instance|if needed|should changes become necessary"),
 ("apology",         r"\bapologi[sz]e|\bapologies\b|\bsorry\b"),
 ("noting",          r"\bnote(s|d)?\b|\bnoting\b"),
 ("thanks",          r"\bthank(s| you)\b|\bthankfully\b|\bappreciate"),
 ("I/me",            r"\bI\b|\bme\b|\bmyself\b"),
 ("we/our/us",       r"\bwe\b|\bour\b|\bus\b"),
 ("the Regulator",   r"\bthe [Rr]egulator\b"),
 ("the Respondent",  r"\bthe [Rr]espondent\b|\bAs the Respondent\b"),
 ("the parties",     r"\bparties\b"),
 ("defend/refuse",   r"\bdefend|does not accept|remains to"),
 ("concede/consent", r"veracity|\bconsent\b|\bagrees?\b|able to confirm|happy to consent|happy for the appeal"),
 ("costs",           r"\bcosts\b"),
 ("alleged",         r"\balleged\b"),
])
rows = []
for k in sorted(ALL, key=date):
    t = ALL[k]; c = {f: len(re.findall(p, t, 0 if f == 'I/me' else re.I)) for f, p in F.items()}
    rows.append((date(k), k, len(t.split()), c))

print(f"{len(rows)} Regulator-authored texts held verbatim (bodies)\n")
print("PER PERIOD TOTALS (per 1,000 words in brackets)")
agg = collections.defaultdict(lambda: collections.Counter()); W = collections.Counter(); N = collections.Counter()
for d, k, w, c in rows:
    p = period(d); W[p] += w; N[p] += 1; agg[p].update(c)
hdr = "feature".ljust(18) + "".join(p.rjust(18) for p in sorted(W))
print(hdr); print("texts / words".ljust(18) + "".join(f"{N[p]} / {W[p]}".rjust(18) for p in sorted(W)))
for f in F:
    print(f.ljust(18) + "".join(f"{agg[p][f]} ({1000*agg[p][f]/W[p]:.1f})".rjust(18) for p in sorted(W)))
print("\nEVERY UNDATED PROMISE, APOLOGY, NOT-YET MARKER AND DATED PROMISE, IN ORDER")
for d, k, w, c in rows:
    t = ALL[k]
    for f in ("dated promise", "undated promise", "not-yet marker", "apology"):
        for m in re.finditer(F[f], t, re.I):
            a = max(0, m.start() - 70); print(f"  {d} {k.split(' ', 1)[0]:5s} [{f}] ...{t[a:m.end()+40].strip()}...")
print("\nSALUTATIONS (hand-coded from the originals)")
for d, v in SAL.items(): print(f"  {d}  {v}")
