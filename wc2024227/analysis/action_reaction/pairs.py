# Every Appellant step in the appeal paired with the Regulator's (or OIR's / the Commission's) reaction.
# Source: four Gmail readings of 60 appeal threads (20 Oct 2026), plus the repo's as-sent copies for
# attachment contents. Times AEST. A date-only time is written 12:00 and flagged approx.
# Step types:  OFFER (settlement or "please concede")   PRESS (complaint, carriage, findings, widening)
#              NOTICE (rule-based notice with a clock)   DOCREQ (request for documents)
#              LAWQ (question that commits them on law or merits)   PROC (time, dates, process)
#              NARROW (withdrawal or narrowing)          FILE (Appellant filing with the Registry)
# Reaction types: CONCEDE  REFUSE  DEFER  RESERVE  SILENCE  ACCOMMODATE  INVESTIGATE  COMMIT  COMPLY
import csv, datetime as dt, statistics as st, collections, sys

P = [
# id, phase, step time, step, step type, reactor, reaction time ('' = none), reaction, reaction type, approx
("P01","0 2024-25","2024-11-27 12:20","Appeal filed out of time; Registry refers the time question to the Regulator","FILE","Regulator","2024-12-02 14:52","Consents: 'happy for the appeal to proceed'","CONCEDE",""),
("P02","0 2024-25","2024-11-27 12:00","Appellant's letter enclosing the notice of appeal","PROC","Regulator","2024-12-04 11:58","Form letter: allocated to Matheson; costs reserved (Scale C)","RESERVE","approx"),
("P03","0 2024-25","2025-01-16 00:03","Evidence sent; question on the review officer's union finding","LAWQ","Regulator","2025-01-16 11:05","No list needed (accommodation); union question not addressed","SILENCE",""),
("P04","0 2024-25","2025-02-06 18:04","Documents after a call; asks that conceding some points be considered","OFFER","Regulator","2025-02-11 11:40","'continue to defend'; post-injury events 'cannot be considered causative'; 'alleged injury'","REFUSE",""),
("P05","0 2024-25","2025-06-11 14:37","Lawyer-drafted Form 9A filed (Saines)","FILE","Regulator","2025-07-04 12:00","Three NNPDs: two treating practices and Qld Health payroll (forensic tests of the employer's paper)","INVESTIGATE","approx"),
("P06","0 2024-25","2025-07-14 22:07","Conditional consent to their extension; four questions incl. whether 'not at all costs' still holds","LAWQ","Regulator","","No reply; answered by conduct: 22 Jul 2025 defence seeking dismissal and costs","SILENCE",""),
("P07","0 2024-25","2025-08-14 15:39","Urgent request for a two-week stay (lawyers gone)","PROC","Commission","2025-08-22 11:00","Commission vacates all directions 'to give the Appellant a chance to reorganise' (Matheson: email not received)","ACCOMMODATE",""),
("P08","0 2024-25","2025-08-20 12:11","Resends the extension request","PROC","Regulator","2025-08-20 12:36","Consents to the extension; offers more time","CONCEDE",""),
("P09","1 Feb-Mar 2026","2026-02-11 15:01","URGENT filing: Form 4 (exclusion, sealing, production), affidavit, 381 pp bundle","PRESS","Regulator","2026-02-12 09:42","Acknowledges; waives hard-copy service 'to save any difficulty to you'","ACCOMMODATE",""),
("P10","1 Feb-Mar 2026","2026-02-11 15:01","Notice to admit #1 (50 facts), deemed-admission warning","NOTICE","Regulator","2026-02-18 13:18","Response filed in time: admissions plus denials with reasons (2020 agreement asserted)","RESERVE",""),
("P11","1 Feb-Mar 2026","2026-02-12 07:30","Complaint to OIR about the conduct of the appeal; asks for a different officer [quarantined]","PRESS","OIR","2026-02-13 11:03","Carriage change refused 'unless and until' a conflict is 'identified and established'; 23 Feb: no further action","REFUSE",""),
("P12","1 Feb-Mar 2026","2026-02-12 13:12","'Service & Carriage' to Matheson: asks her to suspend action on the file","PRESS","Regulator","","No reply from Matheson (Ethical Standards replied instead)","SILENCE",""),
("P13","1 Feb-Mar 2026","2026-02-12 16:49","Notice to the Registrar of a conflict affecting the Regulator's representative","PRESS","OIR","2026-02-13 11:03","Manager: Matheson 'shall continue to represent' the Regulator","REFUSE",""),
("P14","1 Feb-Mar 2026","2026-02-18 09:43","Calderbank #1 (open 7 days)","OFFER","Regulator","2026-02-19 08:39","'does not accept your offer, and we will be defending the appeal'","REFUSE",""),
("P15","1 Feb-Mar 2026","2026-02-25 13:23","Supplementary Form 4: findings, referrals, strike-out, removal of representatives","PRESS","Regulator","","No written reply; Counsel appears at the 27 Feb mention and the 13 Mar conference","SILENCE",""),
("P16","1 Feb-Mar 2026","2026-03-20 14:14","Post-conference update: withdraws the findings/referral/strike-out/removal limbs; proposes a timetable and a notice to produce","NARROW","Regulator","2026-03-20 17:11","Offers informal disclosure on request, no notice needed; corrects the Form 29 route; silent on the withdrawals","ACCOMMODATE",""),
("P17","2 Apr-Jul 2026","2026-04-08 15:59","Amended Form 9A filed","FILE","Regulator","2026-04-27 12:00","Own NNPD to Qld Health payroll: the leave form and 'screenshot(s) of the request progression over time'","INVESTIGATE","approx"),
("P18","2 Apr-Jul 2026","2026-04-08 15:59","Amended Form 9A filed","FILE","Regulator","2026-05-13 15:56","Amended defence: ¶14(e) 'in fact, the attachments were present'; 'human error'; 'reasonable in all respects'; costs still sought","RESERVE",""),
("P19","2 Apr-Jul 2026","2026-04-22 17:00","Form 29 to MSH served (Regulator served as Affected Party 1)","FILE","Regulator","","No written position on the Form 29 or the later 64G; 67 words at the 7 Aug mention","SILENCE","approx"),
("P20","2 Apr-Jul 2026","2026-06-12 18:10","Rule 64G application (rejected for format, refiled 23 Jun)","FILE","Regulator","","No written position","SILENCE",""),
("P21","2 Apr-Jul 2026","2026-07-01 12:16","Calderbank #2 (open 21 days), with an invitation to confer","OFFER","Regulator","2026-07-16 15:54","'position remains to defend… Should our position change at any point, we will advise you'; no counter, no conferral","REFUSE",""),
("P22","2 Apr-Jul 2026","2026-07-24 19:08","Request for an up-to-date list of documents and copies of their NNPDs","DOCREQ","Regulator","2026-08-14 10:28","Holding reply 3 Aug with apology; delivered 14 Aug, 'sincerely apologise'","COMPLY",""),
("P23","2 Apr-Jul 2026","2026-07-31 10:47","WP 'material development' letter inviting reconsideration","OFFER","Regulator","2026-08-14 13:29","'position remains to defend… As mentioned previously…'","REFUSE",""),
("P24","3 Aug-Oct 2026","2026-08-10 14:00","Withdraws the 64G application and does not press the Form 29","NARROW","Regulator","","No acknowledgement from anyone; Commission's FDO(3) of 19 Aug is made 'FURTHER TO' it","SILENCE",""),
("P25","3 Aug-Oct 2026","2026-08-12 07:26","Stressor 1(a) bundle (30 pp) under the duty of disclosure","PROC","Regulator","","No reply","SILENCE",""),
("P26","3 Aug-Oct 2026","2026-08-14 13:40","Part 2 privilege schedule; post-injury categories; questions on Review Decision 69983's properties; preservation","LAWQ","Regulator","","No reply on any point (67 days at 20 Oct)","SILENCE",""),
("P27","3 Aug-Oct 2026","2026-08-28 13:47","Notice to admit #2 (303 facts) and Form 25 (39 documents)","NOTICE","Regulator","2026-09-08 11:22","298 of 303 admitted, 0 denied; 25 of 39 documents; reservation letter (existence only, de novo, relevance reserved)","CONCEDE",""),
("P28","3 Aug-Oct 2026","2026-08-28 13:47","Asks whether Taylor, Reese or Stibbard will be called; offers to confer","PROC","Regulator","2026-08-28 14:08","'cannot confirm its witnesses at this stage'; conferral not taken up","DEFER",""),
("P29","3 Aug-Oct 2026","2026-09-07 10:20","Challenges their 'should also be filed' point with rule 49's words","LAWQ","Regulator","","No reply; the point is never raised again","SILENCE",""),
("P30","3 Aug-Oct 2026","2026-09-09 12:36","Letter: 14 disputed tabs, produce or confirm (reply by 18 Sep)","DOCREQ","Regulator","2026-09-24 09:51","4 documents confirmed 'upon further review of the appeal file', 9 sought from MSH","CONCEDE",""),
("P30b","3 Aug-Oct 2026","2026-09-09 12:36","Same letters: the five facts not admitted (154, 228-231); any objection to delivery to the Registry (by 11 Sep)","LAWQ","Regulator","","Never answered; 228-231 return as question 1 of the 19 Oct letter","SILENCE",""),
("P31","3 Aug-Oct 2026","2026-09-09 12:36","Same letter: the nine documents to be sought from MSH","DOCREQ","Regulator","2026-10-12 08:30","Nine MSH documents delivered: 'The regulator confirms the veracity'","CONCEDE",""),
("P32","3 Aug-Oct 2026","2026-09-10 19:12","Agrees their extension 'no conditions attach'; notes their 30 Sep date","PROC","Regulator","2026-09-24 11:55","Witness list and outlines served six days early (no expert)","COMPLY",""),
("P33","3 Aug-Oct 2026","2026-10-01 16:45","Direction 5 election; directions 2-7; leave for the Second Amended 9A; asks whether they consent","LAWQ","Regulator","2026-10-12 09:21","Conference agreed; items 2-7 'in lieu of ordered in directions'; Counsel 'not contactable until 22 October'; consent to leave not answered","DEFER",""),
("P34","3 Aug-Oct 2026","2026-10-07 08:20","Rule 49 admission of Tab 32A requested by 16 Oct","DOCREQ","Regulator","2026-10-16 15:57","Confirmed on the date (32A and 32B) with the 8 Sep reservation","CONCEDE",""),
("P35","3 Aug-Oct 2026","2026-10-13 12:26","[Commission] Instruction to obtain Counsel's availability as soon as possible after 22 Oct","PROC","Regulator","2026-10-19 10:52","Counsel's three dates, three days before 22 Oct","COMPLY",""),
("P36","3 Aug-Oct 2026","2026-10-19 16:04","All three dates; 11-page letter with six closed questions by 30 Oct","LAWQ","Regulator","2026-10-20 09:48","'I will review your letter… and respond by Friday 30 October 2026 as requested'","COMMIT",""),
]

def t(s): return dt.datetime.strptime(s, "%Y-%m-%d %H:%M")
rows = []
for p in P:
    lat = (t(p[6]) - t(p[2])).total_seconds()/3600 if p[6] else None
    rows.append(dict(id=p[0], phase=p[1], step_time=p[2], step=p[3], step_type=p[4], reactor=p[5],
                     reaction_time=p[6], reaction=p[7], reaction_type=p[8], approx=p[9],
                     latency_hours=None if lat is None else round(lat, 1)))
out = sys.argv[1] if len(sys.argv) > 1 else "pairs.csv"
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

def fmt(h):
    if h is None: return "none"
    return f"{h:.1f} h" if h < 48 else f"{h/24:.1f} d"

print(f"{len(rows)} pairs\n")
print("REACTION TYPE BY STEP TYPE")
by = collections.defaultdict(collections.Counter)
for r in rows: by[r["step_type"]][r["reaction_type"]] += 1
for k in ["OFFER","PRESS","NOTICE","DOCREQ","LAWQ","PROC","NARROW","FILE"]:
    print(f"  {k:7s} n={sum(by[k].values()):2d}  " + ", ".join(f"{a} {b}" for a, b in by[k].most_common()))
print("\nLATENCY OF ANSWERED STEPS (median, range), by step type")
for k in ["OFFER","PRESS","NOTICE","DOCREQ","LAWQ","PROC","NARROW","FILE"]:
    L = [r["latency_hours"] for r in rows if r["step_type"] == k and r["latency_hours"] is not None and not r["approx"]]
    n0 = sum(1 for r in rows if r["step_type"] == k and r["latency_hours"] is None)
    if L: print(f"  {k:7s} answered {len(L)} (exact times)  median {fmt(st.median(L))}  range {fmt(min(L))} to {fmt(max(L))}  unanswered {n0}")
    else: print(f"  {k:7s} answered 0 (exact times)  unanswered {n0}")
print("\nSETTLEMENT LATENCY SERIES")
for r in rows:
    if r["step_type"] == "OFFER": print(f"  {r['step_time'][:10]}  {fmt(r['latency_hours']):>8s}  {r['reaction'][:70]}")
print("\nSILENCES (no reply at all)")
for r in rows:
    if r["reaction_type"] == "SILENCE" and not r["reaction_time"]: print(f"  {r['id']} {r['step_time'][:10]} [{r['step_type']}] {r['step'][:80]}")
print("\nBY PHASE: share of steps that drew a concession or commitment")
ph = collections.defaultdict(list)
for r in rows: ph[r["phase"]].append(r["reaction_type"])
for k in sorted(ph):
    v = ph[k]; c = sum(x in ("CONCEDE","COMMIT","COMPLY") for x in v); s = sum(x == "SILENCE" for x in v); rf = sum(x == "REFUSE" for x in v)
    print(f"  {k:16s} steps {len(v):2d}  concede/comply/commit {c:2d}  refuse {rf:2d}  silence {s:2d}")
