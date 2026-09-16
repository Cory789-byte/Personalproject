# SEND CHECKLIST — the three-document package, 1 August 2026

⭐ **THREE SEPARATE EMAILS, THREE SUBJECT LINES.** Not one email with three attachments — receipt
of **each document** is what starts **its own clock**. Each document says on its face that it does
not answer the other two.

## Email 1 — response to the Request for Medical Information

| Item | File |
|---|---|
| Covering email | `RFMI_RESPONSE_EMAIL.txt` |
| Attachment | `drafts/out/RFMI_Response_and_Allocation_MSH-INJ-5795.pdf` (14pp, A4, scrubbed) |
| Not sent to MSH | `NOTE_FOR_DR_MA.txt` — Dr Ma only, with the RFMI documents |

**To:** lbh_InjuryManagement@health.qld.gov.au
**Cc:** LBH.HRTeam1@health.qld.gov.au
**Subject:** Response — Request for Medical Information, MSH-INJ-5795 [CLM-317073]

## ⭐ Email 2 — the clause 10.3 request (this is the one with the 21-day clock)

| Item | File |
|---|---|
| Attachment | `drafts/out/REQUEST_Change_in_the_way_I_work_cl10.3_MSH-INJ-5795.pdf` (3pp) |
| Source | `FWA_REQUEST_cl10.3.txt` |

**To:** lbh_InjuryManagement@health.qld.gov.au
**Cc:** LBH.HRTeam1@health.qld.gov.au; Scott Hughes; Chloe Taylor; Emily Petering; Heath Moran
**Subject:** Request under clause 10.3.2 — change in the way I work — C Shepherd, MSH-INJ-5795

> Dear Injury Management team,
>
> I attach a request under clause 10.3.2 of the certified agreement for a change in the way I
> work. I have made it as a separate document so that there is no question about what it is or
> when it was received.
>
> The request sets out the change I am asking for and my reasons for it, in the form clause 10.3.3
> requires. I have asked that the decision be made by an officer outside Corporate Services, for
> the reasons at part 4.
>
> I would much prefer this be resolved by discussion and I am available at any time.
>
> Kind regards,
> Cory Shepherd

⛔ **Do not mention the 21 days in the covering email.** It is in the document, at part 5, quoted
from the clause. Saying it twice makes it a demand instead of a citation.

## ⭐ Email 3 — the Stage 1 dispute notice

| Item | File |
|---|---|
| Attachment | `drafts/out/NOTICE_OF_DISPUTE_cl1.11_Stage1.pdf` (3pp) |
| Source | `DISPUTE_NOTICE_cl1.11_STAGE1.txt` |

**To:** chloe.taylor3@health.qld.gov.au *(immediate supervisor — cl 1.11.2(a) requires this)*
**Cc:** Scott Hughes; LBH.HRTeam1; lbh_InjuryManagement; Emily Petering; Heath Moran
**Subject:** Notice of dispute — clause 1.11 — attendance, roster, leave and pay from 26 June 2026

> Dear Chloe,
>
> I attach a notice of dispute under clause 1.11.2(a) of the certified agreement. It is addressed
> to you as my immediate supervisor because the clause requires that.
>
> I would prefer this resolved at Stage 1 and I am available to discuss it at any time, including
> today. I have asked that a support person and my union representative be present.
>
> I have raised at part 5 a question about who should conduct the Stage 1 discussion. I make no
> allegation against anyone and will attend whichever way the Health Service prefers.
>
> Kind regards,
> Cory Shepherd

⚠️ **It must go to Taylor** even though the conflict is raised. cl 1.11.2(a) requires the immediate
supervisor to be informed — if he skips her, MSH can say Stage 1 never started and Stages 2–4 never
opened. Part 5 of the notice handles the conflict in the same document. ⭐ **There is no answer to
part 5 that costs him anything:** nominate someone else and the conflict is conceded and managed;
insist on Taylor and the insistence is documented.

## Before you send — fields to fill

- [ ] ⚠️ **`[PHONE]`** in both new letters, and check the sign-off on the RFMI response. **`0417 400 227`
      appears nowhere in the record; `0422 438 627` is on file.** Confirm which is current — a wrong
      number on a document that asks them to call you before every shift is the worst possible place
      for it.
- [ ] **`[SEND DATE]`** in `FWA_REQUEST_cl10.3.txt` and `DISPUTE_NOTICE_cl1.11_STAGE1.txt`.
- [ ] **`[21DAYDATE]`** in `FWA_REQUEST_cl10.3.txt` part 5 — send date **+ 21 calendar days**.
      *(Send 1 Aug → **22 August 2026**.)*
- [ ] Re-run `python3 build_letters.py` after editing either letter.

### Diarise on sending
- **send + 1 day** — Stage 1 discussion due (cl 1.11.2(a), 24 hours)
- **send + 7** — Stage 1 ends
- **send + 14** — Stage 2 ends → Stage 3 EB12IG / Stage 4 QIRC
- ⭐ **send + 21** — cl 10.3.6 decision due. **Silence = deemed refusal, IR Act s 29.**

## Before you send — 3 more fields

- [ ] **PDF header, page 1 — "Response date:"** — insert the date you send.
- [ ] **PDF page 5, Part 6, first line — `[DATE]`** — the date of the earlier email in which you
      raised the delegation / conflict question. Use the actual date; "previously" invites them to
      say they don't recall it.
- [ ] ⭐ **Part 7.2 — `[21DAYDATE]`** — the send date **plus 21 calendar days**, being the day
      EB12 cl 10.3.6 requires MSH's written decision. *(Send 1 Aug → **22 August 2026**. Send
      2 Aug → 23 August 2026. Recompute if the send slips — a wrong date here is worse than none,
      and if you would rather not commit to one, delete the sentence containing it; the clause
      still runs.)*
      **Then diarise that date.** Under **IR Act s 29**, silence to that date is a **deemed
      refusal** — which is a decision, and which carries no stated grounds.

*(Edit `RFMI_ALLOCATION_AND_PROPOSAL.txt`, then re-run `python3 build_alloc_pdf.py` from the repo
root. Metadata is scrubbed automatically — verify with `pdfinfo` that Custom Metadata and Metadata
Stream both read "no".)*

## Optional cut

- [ ] **Part 5.1, the AD Act s 124 paragraph.** Now points at a single question. Keep it (it is the
      one provision placing an onus on MSH, and it is framed as a self-check, not a complaint), or
      cut it if you want the document to read as purely cooperative. It is self-contained — removing
      it changes nothing else.

## Before you send — 1 fact to confirm

- [ ] **Part 5.2** lists "a formal complaint in February 2026" among the concerns raised. Confirm
      that description matches the document. It is the only item in that list described rather than
      quoted from a source.

## Same day

- [ ] Forward the RFMI bundle **and** your response to **Emily Petering** (industrial officer) and
      **Heath Moran**. This is the most actionable document in the matter: a Director-signed request
      built on a false premise, an undisclosed conflict, a seven-day threat, and five weeks of unpaid
      exclusion.
- [ ] Give **Dr Ma** the `NOTE_FOR_DR_MA.txt` with the RFMI letters, so he has the context before he
      is asked anything.
- [ ] Save your sent item as PDF into `documents/`.

## Do not

- ❌ Do not sign the **option 2** authority (direct access to your practitioners).
- ❌ Do not add anything to the **24 October 2024** diagnosis date beyond what Part 3.2 says. The date
      is disclosed openly; the clinical context comes from the psychiatrist. Do not explain the
      sequence with the review decision — that belongs in the appeal file, not in HR correspondence.
- ❌ Do not use the word **"privileged"** about anything going to MSH. Report A is
      *medical-in-confidence*, not privileged. (Report B — the appeal report — is privileged.)
- ❌ Do not connect the **1 July** and **2 July** dates anywhere in correspondence.
- ❌ Do not raise the appeal, the PID, or reprisal in this correspondence.

## After you send

- [ ] Diarise **7 August 2026** — 64G mention before Dwyer. Ordinary procedural machinery; volunteer
      nothing about the employment dispute.
- [ ] Brief the psychiatrist for **Report A**: capacity, functional restrictions, adjustments. Full
      history and chronology — but **no opinion on cause or origin**, even in passing. If a question
      invites it, he should say it falls outside the scope of the report.
- [ ] Instruct the psychiatrist only after MSH confirms which questions it presses. Invoice direct to
      Harrison at lbh_InjuryManagement@health.qld.gov.au.
- [ ] Tell MSH the expected fee once known — a notification, not a request for approval.
- [ ] **Obtain the separate medical certificate** from Dr Ma covering the period from 3 July 2026.
      The checklist form requires one and it was not provided. MSH has never raised it in four
      weeks — if they ever do, their silence is your answer, so bank that rather than argue it now.

## Evidence to collect this week (appeal file, not MSH)

- [ ] Clinical note for **24 October 2024**, with the **consultation time**.
- [ ] The email delivering **Review Decision 69983**, with its **timestamp**.
- [ ] The **psychiatrist referral document** and its date.
- [ ] The **last shift actually worked** before 2 July 2026.
