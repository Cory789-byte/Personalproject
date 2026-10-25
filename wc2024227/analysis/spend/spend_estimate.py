#!/usr/bin/env python3
"""WC/2024/227 - what the Regulator has plausibly spent on this matter, to 23 October 2026.

INTERNAL. An ESTIMATE, not a finding. No document ties any expenditure to this matter.

Method: every step the Regulator actually took (verified against the file; basis column) is given
a low / most-likely / high range of officer hours and counsel hours, priced at:
  - counsel: at or under the Queensland Government cap for junior counsel, $300 an hour and
    $3,000 a day, excluding GST (Department of Justice, "Whole-of-government policy for engaging
    barristers", page last updated 25 May 2026; fees above the cap need the Attorney-General's
    approval). Ms Willson is junior counsel.
  - officers: a fully loaded hourly cost for an AO6-AO7-level officer (salary, on-costs,
    supervision overhead), $90-$130 an hour. Judgement, anchored on the Award figures used in
    skill/references/LABOUR-LEDGER-what-the-matter-cost-them.md (AO6 $119.8k-$127.9k, 2025).
Where it is not known whether counsel did a piece of work, the item carries a probability.
Two shared multipliers move all hours together (how thorough the officer was; how much counsel
was used), so the interval is not falsely narrow.

Run: python3 spend_estimate.py   (pure Python, fixed seed, reproducible)
"""
import random, statistics

N = 100_000
SEED = 20261023
CAP_DAY = 3000

CATS = {
 "read":   "Reading what you filed and sent",
 "answer": "Answering your notices and document requests",
 "own":    "Their own pleadings, notices, disclosure, witnesses",
 "attend": "Attendances (mentions, the conference)",
 "offers": "Your settlement offers and WP letter",
 "admin":  "File handling and procedure",
 "review": "The 2024 review decision",
}

# (id, phase, category, when, step, officer hours (lo, mode, hi),
#  counsel hours (lo, mode, hi) or None, P(counsel did it), basis)
STEPS = [
 # ---- before the appeal (reported separately) -------------------------------------------
 ("R1", "0 Review", "review", "Sep-Oct 2024", "Review of WorkCover's decision; Review Decision 69983 (28 pp)",
  (20, 35, 60), None, 0, "RD 69983, 28 pp; Appellant's list item 6. No external legal help counted"),
 # ---- 2024-25: the appeal while you had lawyers -------------------------------------------
 ("A01", "1 Appeal 2024-25", "admin", "Nov-Dec 2024", "Appeal received out of time; consent to proceed; file allocated; opening letter; directions",
  (5, 8, 14), None, 0, "pairs P01, P02"),
 ("A02", "1 Appeal 2024-25", "read", "Jan-Feb 2025", "Your evidence read; a call; replies of 16 Jan and 11 Feb",
  (3, 6, 10), None, 0, "pairs P03, P04"),
 ("A03", "1 Appeal 2024-25", "admin", "Feb-Jun 2025", "30 Apr 2025 conference listed then vacated by consent; AFDO; liaison with Saines",
  (2, 4, 8), None, 0, "AFDO 3 Jun 2025"),
 ("A04", "1 Appeal 2024-25", "read", "Jun 2025", "Saines-drafted Form 9A read and analysed",
  (2, 4, 7), (0.5, 2, 4), 0.6, "pairs P05"),
 ("A05", "1 Appeal 2024-25", "own", "Jul 2025", "Three non-party disclosure notices drafted and served; records received and reviewed",
  (6, 10, 18), (0, 1, 3), 0.3, "documents/2025-07-04_NNPD_* (3 sealed notices)"),
 ("A06", "1 Appeal 2024-25", "own", "8-11 Jul 2025", "Witness conferencing x3 (Reese, Taylor, Christesen) and the disclosure from it",
  (6, 10, 16), (1, 3, 6), 0.3, "Appellant's list items 25-27"),
 ("A07", "1 Appeal 2024-25", "own", "Jul 2025", "Statement of Facts and Contentions (Form 9C, 6 pp) drafted and served",
  (4, 7, 12), (3, 6, 10), 0.6, "2025-07_Regulator_SOFC_Form9C_original.pdf, 6 pp"),
 ("A08", "1 Appeal 2024-25", "admin", "Jul-Aug 2025", "Extension correspondence; Saines withdraws; directions vacated",
  (1, 2, 4), None, 0, "pairs P06-P08"),
 # ---- Feb-Aug 2026: the contested phase ---------------------------------------------------
 ("B01", "2 Feb-Aug 2026", "read", "9-12 Feb 2026", "Urgent Form 4 and affidavit with 381 pp of exhibits read; counsel reads in",
  (6, 12, 20), (5, 9, 15), 0.95, "confirmed-record 9 Feb 2026; pairs P09"),
 ("B02", "2 Feb-Aug 2026", "admin", "12-13 Feb", "Carriage correspondence handled by an OIR manager",
  (2, 4, 8), None, 0, "pairs P11, P13 (existence only)"),
 ("B03", "2 Feb-Aug 2026", "answer", "11-18 Feb", "Response to notice to admit #1 (50 facts; 13 pp with email)",
  (5, 9, 15), (1, 3, 6), 0.6, "2026-02-18_Form24_Response..., 13 pp"),
 ("B04", "2 Feb-Aug 2026", "offers", "17-19 Feb", "Calderbank #1 considered and rejected next day",
  (1.5, 3, 5), (0.5, 1, 2), 0.5, "pairs P14"),
 ("B05", "2 Feb-Aug 2026", "admin", "17-18 Feb", "Mention moved 26 to 27 Feb at their request",
  (0.3, 0.5, 1), None, 0, "confirmed-record (17 Feb email)"),
 ("B06", "2 Feb-Aug 2026", "read", "25-27 Feb", "Supplementary Form 4 and affidavits (71 pp) read",
  (3, 5, 9), (2, 3, 6), 0.9, "documents/filings/2026-02-25..27, 71 pp"),
 ("B07", "2 Feb-Aug 2026", "attend", "27 Feb", "Mention: counsel appeared; officer instructing",
  (1.5, 2.5, 4), (4, 5.5, 7.5), 1.0, "confirmed-record (your recollection)"),
 ("B08", "2 Feb-Aug 2026", "attend", "13 Mar", "First s 552A conference: counsel appeared; preparation; report to the delegate",
  (4, 6, 9), (8, 11, 14), 1.0, "confirmed-record"),
 ("B09", "2 Feb-Aug 2026", "answer", "20 Mar", "Your withdrawals; their reply offering informal disclosure",
  (1, 2, 3), None, 0, "pairs P16"),
 ("B10", "2 Feb-Aug 2026", "attend", "7 Apr", "Telephone mention: counsel appeared; directions order",
  (1, 1.5, 2.5), (2, 3, 4.5), 1.0, "confirmed-record"),
 ("B11", "2 Feb-Aug 2026", "read", "8 Apr", "Amended 9A read and analysed",
  (3, 5, 8), (2, 4, 7), 0.9, "documents/filings/2026-04-08_Amended_Form9A"),
 ("B12", "2 Feb-Aug 2026", "read", "22 Apr", "Your Form 29 to MSH (served on them as affected party) read",
  (0.5, 1.5, 3), None, 0, "correspondence 2026-04-22"),
 ("B13", "2 Feb-Aug 2026", "own", "27 Apr", "Their own disclosure notice to Qld Health payroll; production reviewed",
  (3, 5, 8), None, 0, "documents/2026-04-27_NNPD_Regulator_to_QldHealth (6 pp)"),
 ("B14", "2 Feb-Aug 2026", "own", "13 May", "Amended Statement of Facts and Contentions (7 pp) drafted",
  (3, 6, 10), (6, 10, 16), 0.85, "WC.2024.227_Regulator_SOFC_13.05.2026.pdf, 7 pp"),
 ("B15", "2 Feb-Aug 2026", "attend", "22 May", "Mention (no counsel)",
  (1, 1.5, 2.5), None, 0, "confirmed-record"),
 ("B16", "2 Feb-Aug 2026", "read", "5 Jun", "MSH's objection (5 pp) read",
  (0.5, 1, 2), None, 0, "2026-06-05_MSH_Objection, 5 pp"),
 ("B17", "2 Feb-Aug 2026", "own", "11 Jun", "Supplementary disclosure assembled and served",
  (3, 6, 10), None, 0, "confirmed-record 11 Jun; disclosure PDF 10 pp"),
 ("B18", "2 Feb-Aug 2026", "read", "12-23 Jun", "Rule 64G application read (no written position taken)",
  (2, 3.5, 6), (0.5, 1.5, 3), 0.5, "pairs P20"),
 ("B19", "2 Feb-Aug 2026", "offers", "1-16 Jul", "Calderbank #2 considered; 3-page rejection",
  (2, 4, 7), (0.5, 1.5, 3), 0.6, "2026-07-16 rejection, 3 pp"),
 ("B20", "2 Feb-Aug 2026", "answer", "24 Jul-14 Aug", "Amended list of documents (52 items) and notice copies; holding reply",
  (5, 8, 13), None, 0, "working-notes 14 Aug; pairs P22"),
 ("B21", "2 Feb-Aug 2026", "offers", "31 Jul-14 Aug", "Without-prejudice letter considered; reply",
  (1, 2.5, 4), (0.3, 1, 2), 0.4, "pairs P23"),
 ("B22", "2 Feb-Aug 2026", "attend", "6-7 Aug", "Rule 64G mention: Matheson alone (about 65 min); preparation and report",
  (3, 4.5, 7), (0.3, 1, 2), 0.3, "7 Aug transcript: no counsel; runs to 64:34"),
 ("B23", "2 Feb-Aug 2026", "read", "10-22 Aug", "64G withdrawn; FDO(3); your 1(a) bundle, 13 stressor bundles, privilege schedule received",
  (2, 4, 8), None, 0, "pairs P24-P26; Appellant's list items 15-16"),
 # ---- late Aug to 23 Oct 2026: the admissions phase ---------------------------------------
 ("C01", "3 Aug-Oct 2026", "answer", "28 Aug-8 Sep", "Notice to admit #2: 303 facts with 133-pp annexure, and 39 documents, checked; 22 + 5 + 2 pp in reply",
  (20, 32, 55), (3, 6, 12), 0.75, "FORM24_SERVED 22 pp, ANNEXURE_A 133 pp, PART_B 7 pp; regulator-response-2026-09-08"),
 ("C02", "3 Aug-Oct 2026", "read", "28 Aug-7 Sep", "Witness question answered; your rule 49 email read",
  (0.5, 1, 2), None, 0, "pairs P28, P29"),
 ("C03", "3 Aug-Oct 2026", "answer", "9 Sep-12 Oct", "Disputed documents: 4 confirmed 24 Sep; 9 obtained from MSH and confirmed 12 Oct",
  (6, 10, 16), None, 0, "regulator-2026-09-24, regulator-2026-10-12"),
 ("C04", "3 Aug-Oct 2026", "own", "10-24 Sep", "Witness list and four outlines (Taylor, Reese, Wright, Earl; 5 pp)",
  (8, 13, 20), (1, 3, 6), 0.6, "regulator-2026-09-24: outlines 5 pp, list 2 pp"),
 ("C05", "3 Aug-Oct 2026", "read", "Sep", "Your three outlines and documents letter read",
  (1.5, 3, 5), (0.5, 1.5, 3), 0.5, "SEND_9SEP2026; pairs P30"),
 ("C06", "3 Aug-Oct 2026", "read", "1-12 Oct", "Direction 5 election and Second Amended 9A read; conference agreed",
  (3, 5, 8), (1, 2, 4), 0.7, "pairs P33"),
 ("C07", "3 Aug-Oct 2026", "answer", "7-16 Oct", "Rule 49: Tab 32A and 32B confirmed",
  (1, 2, 3), None, 0, "pairs P34"),
 ("C08", "3 Aug-Oct 2026", "read", "13-23 Oct", "Dwyer's instruction; counsel's dates; your 11-page letter read and acknowledged",
  (2.5, 4, 6), (0.3, 0.8, 1.5), 0.9, "pairs P35, P36; correspondence 22-23 Oct"),
]

# The least counsel could have done: read in, appear three times, settle the May pleading.
MIN_COUNSEL = {"B01", "B07", "B08", "B10", "B14"}

# Still to come (reported separately, not in "to date")
FORWARD = [
 ("F1", "by 30 Oct 2026", "Answers to your six questions", (5, 8, 14), (2, 4, 8), 0.85, 0),
 ("F2", "21 Jan 2027", "Second s 552A conference, counsel attending", (5, 8, 12), (8, 11, 14), 1.0, 0),
 ("F3", "2027, if it runs", "Two-day hearing: preparation, witnesses, submissions, two hearing days",
  (30, 50, 80), (25, 40, 60), 1.0, 2),   # last field: hearing days at a day fee
]

def pct(xs, q):
    xs = sorted(xs); return xs[min(len(xs) - 1, int(q * len(xs)))]

def run(n=N, pin=None, counsel=None):
    """pin: fix a driver, e.g. {"m_o": 0.6}. counsel: None (use P), "min" or "max"."""
    pin = pin or {}
    rnd = random.Random(SEED)
    T = lambda lo, mo, hi: rnd.triangular(lo, hi, mo)
    g = lambda k, lo, mo, hi: pin[k] if k in pin else T(lo, mo, hi)
    out = {k: [] for k in ("counsel", "officer", "disb", "appeal", "review", "total",
                           "c_hours", "o_hours", "F1", "F2", "F3")}
    by_phase, by_cat = {}, {}
    item_cost = {s[0]: 0.0 for s in STEPS}
    for _ in range(n):
        c_rate = g("c_rate", 240, 285, 300)   # capped at $300/h
        o_rate = g("o_rate", 90, 105, 130)
        m_o = g("m_o", 0.6, 1.0, 1.5)          # shared: how thorough the officer was
        m_c = g("m_c", 0.5, 1.0, 1.7)          # shared: how much counsel was used
        ovh = g("ovh", 0.08, 0.12, 0.18)       # supervision, delegate approvals, admin
        c = o = rev = ch = oh = 0.0
        ph, ct = {}, {}
        for sid, phase, cat, _w, _d, oh_r, ch_r, p, _b in STEPS:
            hrs_o = T(*oh_r) * m_o * (1 + ovh)
            cost_o = hrs_o * o_rate
            cost_c = hrs_c = 0.0
            if counsel == "min": p = 1.0 if sid in MIN_COUNSEL else 0.0
            elif counsel == "max": p = 1.0
            if ch_r and rnd.random() < p:
                hrs_c = T(*ch_r) * m_c
                cost_c = hrs_c * c_rate
            if phase.startswith("0"):
                rev += cost_o + cost_c
            else:
                o += cost_o; c += cost_c; oh += hrs_o; ch += hrs_c
                ph[phase] = ph.get(phase, 0) + cost_o + cost_c
                ct[cat] = ct.get(cat, 0) + cost_o + cost_c
            item_cost[sid] += (cost_o + cost_c) / n
        d = T(0, 300, 1000)                     # record production fees, copying, service
        out["counsel"].append(c); out["officer"].append(o); out["disb"].append(d)
        out["appeal"].append(c + o + d); out["review"].append(rev)
        out["total"].append(c + o + d + rev)
        out["c_hours"].append(ch); out["o_hours"].append(oh)
        for k, v in ph.items(): by_phase.setdefault(k, []).append(v)
        for k, v in ct.items(): by_cat.setdefault(k, []).append(v)
        for fid, _w, _d, oh_r, ch_r, p, days in FORWARD:
            f = T(*oh_r) * m_o * (1 + ovh) * o_rate
            if rnd.random() < p:
                f += T(*ch_r) * m_c * c_rate + days * T(2400, 2850, CAP_DAY)
            out[fid].append(f)
    return out, by_phase, by_cat, item_cost

def fmt(x): return f"${x:,.0f}"

# ---- The Appellant's side ------------------------------------------------------------------
# Paid to date (verified): Saines Legal trust statement, WC matter 252158, as at 28 Aug 2025
# (01-appeal repo, Exhibit H1): $2,029.40 + $3,445.40 + $435.60 + $1,119.00 + $2,704.60.
APPELLANT_PAID = 9734.00

# His own counsel at a hearing, if it runs. Day rate from Saines' 21 Jul 2025 email: barristers
# "$3,300.00 a day to $4,400.00 a day (including GST)", charged by half or full days.
def run_appellant(n=N):
    rnd = random.Random(SEED + 1)
    T = lambda lo, mo, hi: rnd.triangular(lo, hi, mo)
    direct, with_sol, days_l = [], [], []
    for _ in range(n):
        rate = T(3300, 3850, 4600)                 # incl GST; allows a 2026 rise
        u = rnd.random()
        hearing = 1 if u < 0.20 else (2 if u < 0.75 else 3)
        days = (T(1.0, 1.5, 2.5)                   # reading in, brief, chronology
                + T(0.25, 0.5, 0.75)               # conference(s) with you
                + T(0.25, 0.5, 1.0)                # your witnesses and the doctors
                + T(0.5, 0.75, 1.25)               # cross-examination of their four witnesses
                + hearing
                + (T(0.5, 1.0, 1.5) if rnd.random() < 0.7 else 0))   # written submissions
        c = days * rate
        # Instructing solicitor, if not a direct brief: Stone Group's schedule put briefing counsel
        # at $1,500-$4,000 ex GST; attendance at the hearing; liaison and witness logistics.
        s = T(1650, 2750, 4400) + hearing * T(1500, 2500, 3850) + T(1000, 2000, 4000)
        direct.append(c); with_sol.append(c + s); days_l.append(days)
    return direct, with_sol, days_l

# What a costs order would return if he won (UCPR sch 2 pt 2, column C, incl GST; current UCPR
# fetched 23 Oct 2026): WC Regulation 2025 s 191(2)(a), up to 1.5x under s 191(3).
SCALE_C = {"counsel_day1": 1845.00, "counsel_later_day": 1232.00, "counsel_conf_hour": 290.50,
           "counsel_advise_evidence": 303.40, "prep_with_conference": 1975.00 + 2098.00,
           "solicitor_with_counsel_day": 742.40}

def scale_c(hearing_days=2, conf_hours=3, solicitor=False):
    s = (SCALE_C["counsel_day1"] + (hearing_days - 1) * SCALE_C["counsel_later_day"]
         + conf_hours * SCALE_C["counsel_conf_hour"] + SCALE_C["counsel_advise_evidence"])
    if solicitor:
        s += SCALE_C["prep_with_conference"] + hearing_days * SCALE_C["solicitor_with_counsel_day"]
    return s

if __name__ == "__main__":
    out, by_phase, by_cat, item_cost = run()
    print(f"WC/2024/227 - Regulator spend estimate to 23 Oct 2026 ({N:,} draws, seed {SEED})\n")
    print(f"{'':34}{'P10':>10}{'median':>10}{'P90':>10}{'mean':>10}")
    for k, lab in [("counsel", "Counsel fees (ex GST)"), ("officer", "Officer time (loaded)"),
                   ("disb", "Disbursements"), ("appeal", "APPEAL TO DATE"),
                   ("review", "Review decision (2024)"), ("total", "APPEAL + REVIEW")]:
        xs = out[k]
        print(f"{lab:34}{fmt(pct(xs,.1)):>10}{fmt(pct(xs,.5)):>10}{fmt(pct(xs,.9)):>10}{fmt(statistics.fmean(xs)):>10}")
    print(f"\nHours (appeal): officer median {pct(out['o_hours'],.5):.0f} h "
          f"(P10 {pct(out['o_hours'],.1):.0f}, P90 {pct(out['o_hours'],.9):.0f}); "
          f"counsel median {pct(out['c_hours'],.5):.0f} h "
          f"(P10 {pct(out['c_hours'],.1):.0f}, P90 {pct(out['c_hours'],.9):.0f})")
    print("\nBy phase (median):")
    for k in sorted(by_phase):
        print(f"  {k:24}{fmt(pct(by_phase[k],.5)):>10}  (P10 {fmt(pct(by_phase[k],.1))}, P90 {fmt(pct(by_phase[k],.9))})")
    print("\nBy kind of work, appeal only (mean, and share of the appeal mean):")
    am = statistics.fmean(out["appeal"])
    for k, v in sorted(by_cat.items(), key=lambda kv: -statistics.fmean(kv[1])):
        mu = statistics.fmean(v)
        print(f"  {CATS[k]:52}{fmt(mu):>9}  {100*mu/am:4.0f}%")
    print("\nLargest steps (mean cost):")
    names = {s[0]: (s[3], s[4]) for s in STEPS}
    for sid, v in sorted(item_cost.items(), key=lambda kv: -kv[1])[:10]:
        print(f"  {sid:4} {fmt(v):>8}  {names[sid][0]:>14}  {names[sid][1][:78]}")
    print("\nWhat moves the appeal figure (median with one driver pinned at each end):")
    base = pct(out["appeal"], .5)
    for lab, lo, hi in [("Officer thoroughness (x0.6 / x1.5)", {"m_o": 0.6}, {"m_o": 1.5}),
                        ("Counsel use (x0.5 / x1.7)", {"m_c": 0.5}, {"m_c": 1.7}),
                        ("Officer rate ($90 / $130 an hour)", {"o_rate": 90}, {"o_rate": 130}),
                        ("Counsel rate ($240 / $300 an hour)", {"c_rate": 240}, {"c_rate": 300})]:
        a = pct(run(20_000, pin=lo)[0]["appeal"], .5); b = pct(run(20_000, pin=hi)[0]["appeal"], .5)
        print(f"  {lab:40}{fmt(a):>10} to {fmt(b):>9}  (swing {fmt(b-a)})")
    a = pct(run(20_000, counsel="min")[0]["appeal"], .5); b = pct(run(20_000, counsel="max")[0]["appeal"], .5)
    print(f"  {'Counsel on the minimum / on everything':40}{fmt(a):>10} to {fmt(b):>9}  (swing {fmt(b-a)})")
    print(f"  (base median {fmt(base)})")
    print("\nStill to come (not in the figures above):")
    for fid, w, d, *_ in FORWARD:
        xs = out[fid]
        print(f"  {fid} {w:16} {d[:60]:60} median {fmt(pct(xs,.5))} (P10 {fmt(pct(xs,.1))}, P90 {fmt(pct(xs,.9))})")

    print("\n=== The Appellant's side ===")
    print(f"Paid to Saines Legal for the appeal (verified): {fmt(APPELLANT_PAID)}")
    direct, with_sol, days_l = run_appellant()
    print(f"His counsel at a hearing (incl GST), counsel days median {pct(days_l,.5):.1f} "
          f"(P10 {pct(days_l,.1):.1f}, P90 {pct(days_l,.9):.1f}):")
    for lab, xs in [("Direct brief (no solicitor)", direct), ("With an instructing solicitor", with_sol)]:
        print(f"  {lab:32} median {fmt(pct(xs,.5))}  (P10 {fmt(pct(xs,.1))}, P90 {fmt(pct(xs,.9))})")
    print("Recoverable on a costs order if he wins (scale C; x1.5 is the s 191(3) maximum):")
    for hd in (1, 2, 3):
        a, b = scale_c(hd), scale_c(hd, solicitor=True)
        print(f"  {hd}-day hearing: direct {fmt(a)} (x1.5 {fmt(1.5*a)});  with solicitor {fmt(b)} (x1.5 {fmt(1.5*b)})")
    # Both sides, through a hearing (Regulator incl review + its forward costs; his paid + counsel)
    reg_thru = [t + f1 + f2 + f3 for t, f1, f2, f3 in zip(out["total"], out["F1"], out["F2"], out["F3"])]
    m = min(len(reg_thru), len(direct))
    both_d = [reg_thru[i] + APPELLANT_PAID + direct[i] for i in range(m)]
    both_s = [reg_thru[i] + APPELLANT_PAID + with_sol[i] for i in range(m)]
    print(f"Regulator through a hearing (incl review): median {fmt(pct(reg_thru,.5))} "
          f"(P10 {fmt(pct(reg_thru,.1))}, P90 {fmt(pct(reg_thru,.9))})")
    print(f"BOTH SIDES through a hearing, direct brief: median {fmt(pct(both_d,.5))} "
          f"(P10 {fmt(pct(both_d,.1))}, P90 {fmt(pct(both_d,.9))})")
    print(f"BOTH SIDES through a hearing, with solicitor: median {fmt(pct(both_s,.5))} "
          f"(P10 {fmt(pct(both_s,.1))}, P90 {fmt(pct(both_s,.9))})")
    print("Not modelled: the treating doctors' court-attendance fees (his witnesses; ask each doctor).")
