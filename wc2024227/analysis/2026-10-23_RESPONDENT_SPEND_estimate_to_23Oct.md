# What has the Regulator spent on WC/2024/227? (23 Oct 2026)

> Internal. **An estimate, not a finding.** No document ties any expenditure to this matter.
> ⛔ Never put to the Regulator, the Registry or Dwyer (see the end of this file).
>
> **Read from source today:**
> - Department of Justice, *Whole-of-government policy for engaging barristers* (web page, last updated 25 May
>   2026): departments may pay junior counsel up to **$300 an hour and $3,000 a day**, and senior counsel up to
>   $500 an hour and $5,000 a day, **excluding GST**. Fees above the cap need the Attorney-General's approval.
> - Every step priced below, against its source (the basis column in `analysis/spend/spend_estimate.py`):
>   the pleadings and responses (page counts by `pdfinfo`), the notices, the 7 Aug transcript, the
>   action-reaction dataset, and `confirmed-record.md`.
>
> **Model:** `analysis/spend/spend_estimate.py` → `analysis/spend/spend_output.txt` (100,000 draws, fixed seed).

## Short answer

| | Most likely | Likely range (P10–P90) |
|---|---|---|
| **The appeal, to 23 Oct 2026** | **about $50,000** | $40,000 – $61,000 |
| Counsel's fees (ex GST) | about $19,000 (about 70 hours) | $13,000 – $27,000 |
| Officers' time (loaded cost) | about $30,000 (about 275 hours) | $22,000 – $38,000 |
| Disbursements (record fees, copying) | under $1,000 | |
| The 2024 review decision (RD 69983) | about $5,000 | $3,000 – $7,000 |
| **Appeal plus review** | **about $55,000** | **$44,000 – $67,000** |

**Not counted:**
- Metro South's own costs: its lawyer's objection and 7 Aug attendance, staff time on the documents, and the
  witnesses' time;
- the Commission's time;
- WorkCover's claim handling;
- GST, which government recovers.

## What the money went on (appeal only)

| Kind of work | Mean | Share |
|---|---|---|
| Reading what you filed and sent (381 pp of exhibits, the Form 4s, the 9As, the 64G, the bundles, letters) | $13,900 | 28% |
| Their own pleadings, disclosure notices, disclosure, witness outlines | $12,500 | 25% |
| Answering your notices to admit and document requests | $10,800 | 21% |
| **Attendances:** 27 Feb, 13 Mar and 7 Apr (counsel); 22 May and 7 Aug (Matheson alone) | $8,100 | 16% |
| File handling and procedure | $2,700 | 5% |
| Your two Calderbanks and the WP letter | $1,900 | 4% |

**By phase (median):**
- Nov 2024 to Aug 2025 (your lawyers' era): about $8,900;
- Feb to Aug 2026 (the contested phase): about $27,900;
- late Aug to 23 Oct 2026 (the admissions phase): about $12,500.

**The biggest single steps (mean):**
1. **Checking your 303-fact notice and 39 documents (28 Aug to 8 Sep): about $6,000.** It bought 298 admissions,
   the most productive money spent in the matter, for both sides.
2. The 2024 review decision: about $4,800.
3. Reading the February filing with 381 pages of exhibits, and counsel reading in: about $4,300.
4. The 13 Mar conference: about $4,000.
5. The 13 May amended defence: about $3,400.

## What moves the number

| Driver | Appeal figure, low end to high end |
|---|---|
| How thorough the officer was (hours ×0.6 to ×1.5) | $37,000 to $64,000 |
| How much counsel was used (×0.5 to ×1.7) | $39,000 to $62,000 |
| Counsel only on the minimum (read in, three appearances, the May defence) vs on everything | $42,000 to $56,000 |
| Officer's loaded rate ($90 to $130 an hour) | $45,000 to $56,000 |
| Counsel's rate ($240 to $300 an hour) | $48,000 to $52,000 |

**The cap makes counsel's rate the least important unknown.** The real unknowns are hours: Matheson's, and how much
work went to counsel beyond the appearances.

**A cross-check.** About 70 counsel hours at the cap is about $20,000. That is the size of a typical single
barrister engagement in OIR's Oct–Dec 2024 contract disclosure ($10,100 to $20,000; contracts under $10,000 are
not published).

## Still to come (not in the figures above)

| Step | Median | Range |
|---|---|---|
| Their answers to your six questions (due 30 Oct) | about $2,300 | $1,200 – $3,200 |
| The second conference (21 Jan 2027), counsel attending | about $4,200 | $3,200 – $5,500 |
| **A two-day hearing, if it runs** | **about $24,000** | $19,000 – $30,000 |

**If it runs to a hearing, the total comes to about $85,000.**

## Plus your own lawyers (added 23 Oct, on "plus my counsel")

**Verified, not estimated.** Source: Saines Legal's trust statement for WC matter 252158, as at 28 Aug 2025
(`01-appeal` repo, `WC_2024 227_Exhibit_H1_ Legal cost Trust Statement.pdf`), and Saines' emails of 25 Jun to
12 Aug 2025.

| | Amount |
|---|---|
| **Saines Legal, the appeal (Apr to Aug 2025), total paid** | **$9,734.00** (GST inclusive) |
| Funded by: $2,029.40 left in trust from the reinstatement matter (journalled 3 Apr 2025) | |
| Funded by: your deposit of 22 May 2025 | $5,000.00 |
| Funded by: your payment of 4–6 Aug 2025 (balance of invoice 4240) | $2,704.60 |

- **What that bought:**
  - the 12 May 2025 advice;
  - the Form 9A (filed 11 Jun 2025);
  - correspondence with the Regulator;
  - the timetable steps.
- **No barrister was briefed for you in the appeal.**
  - On 21 Jul 2025 Saines asked for a $3,300 deposit to brief one, quoting $3,300–$4,400 a day including GST.
  - The retainer ended on 23 Jul 2025.
  - The trust account was cleared on 12 Aug 2025.
- **Stone Group Lawyers (Nov 2024 to Jan 2025):**
  - Its costs agreement (the file mislabelled `2024-11-26_Saines_Cost_Agreement.pdf`) covered the reinstatement
    application and the appeal.
  - No Stone Group invoice or payment is on file.
  - The appeal was filed in your own name, and the Regulator dealt with you directly until about April 2025. Its
    work looks to have been on the reinstatement matter, which is a separate track and not counted here.

**Combined spend on the appeal so far:**

| | Most likely | Likely range |
|---|---|---|
| The Regulator (appeal, plus the 2024 review) | about $55,000 | $44,000 – $67,000 |
| Your lawyers (verified) | $9,734 | |
| **Total** | **about $64,000** | **$54,000 – $76,000** |

**If you brief a barrister yourself for a two-day hearing,** allow roughly $13,000–$26,000. That is two hearing
days plus two to four days of preparation, at the $3,300–$4,400 a day Saines quoted in 2025. A solicitor to
instruct them would cost more.

## How this compares with the earlier estimates, and what was wrong with them

| Earlier figure | Problem | Corrected |
|---|---|---|
| `drafts/out/RESPONDENT_SPEND_ESTIMATE.pdf` (23 Aug): $50,000–$122,000, mid **$86,000** | Priced steps as lump sums with no government cap. Assumed counsel was briefed for the 64G mention, but the 7 Aug transcript shows Matheson alone. Its "Stephen Gray, PDF author" row rests on metadata (never cite) | The same steps to 23 Aug come to about **$37,000** on capped rates. A superseded banner has been added |
| `skill/references/LABOUR-LEDGER…` (4 Aug): Willson 95 h at **$450 an hour** = $42,750 | **$450 is 50% above the cap** for junior counsel | At most $300 an hour. This model gives about 70 counsel hours to 23 Oct. Correction noted in the ledger |

## What it means, and what it doesn't

1. **Money is a small lever on them.**
   - Their spend so far is sunk.
   - The decision ahead is about the next $6,500 (the answers and the conference), or about $30,000 with a hearing.
   - For an agency that briefs more than a dozen barristers a quarter, that is routine.
   - They don't pay your compensation (WorkCover does), so conceding costs them almost nothing in cash.
   - The hearing cost is avoidable spend that a delegate has to justify. It pushes slightly toward resolving, but
     precedent and getting the decision right weigh more.
2. **Never put the figure to them.**
   - It is an estimate that their actual records could correct, to your embarrassment.
   - It reads as pressure, not merit.
   - The model-litigant line about keeping costs to a minimum is about their conduct. It is not a weapon here.
3. **This is what it has cost them. It is not what you could be ordered to pay.** That is a separate question,
   not assessed here.
4. **If you ever want the real number,** a Right to Information application after the appeal ends would get the
   counsel invoices or totals. Not now: mid-appeal it would look adversarial.

## Method and assumptions

**Steps.** 40 steps, each sourced: 39 in the appeal, plus the 2024 review. Each carries a low, most-likely and high number of officer hours, and of
counsel hours where counsel may have been involved.

**Counsel.**
- Rate: $240 to $300 an hour, most likely $285, excluding GST. The cap applies to departments, and OIR sits
  inside one.
- Known appearances (27 Feb, 13 Mar, 7 Apr) are certain.
- Other work carries a probability: 0.3 to 0.95 by item. For example, the 13 May defence is 0.85 and the July
  2025 conferences 0.3.
- A hearing day is priced at a day fee of $2,400 to $3,000.

**Officers.**
- $90 to $130 an hour, most likely $105, fully loaded.
- Anchor: AO6 $119.8k–$127.9k (2025 Award figures used in the 4 Aug ledger), divided by 1,720 hours, times 1.35
  on-costs, plus overheads.
- A further 8–18% is added for supervision, delegate approvals and administration.

**Correlation.** Two shared multipliers move all hours together: officer ×0.6 to ×1.5, counsel ×0.5 to ×1.7. This
keeps the range honest; independent items would average out and look falsely precise.

**Not modelled:**
- any internal OIR legal advice;
- transcripts;
- any external help on the 2024 review (none can be tied: `drafts/out/CONTRACT_DISCLOSURE_FINDING_23Aug2026.pdf`).
