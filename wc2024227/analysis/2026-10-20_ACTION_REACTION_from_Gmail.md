# How the Regulator reacts to your steps and counters: the whole Gmail record, Nov 2024 to 20 Oct 2026

> Internal. Prediction only; never for correspondence or submissions.
>
> **Sources:**
> - four full readings of the 60 appeal threads in Gmail (about 123 distinct original emails, 26 Nov 2024 to
>   20 Oct 2026; 20 of them are employment-track emails embedded in one 2025 email, and are not used here);
> - the repo's as-sent and as-received copies for what the attachments say. **The Gmail connector lists
>   attachment names but cannot open them.** The copies used are in `documents/`,
>   `documents/regulator-response-2026-09-08/`, `documents/regulator-2026-09-24/`,
>   `documents/regulator-2026-10-12/`, `documents/correspondence-2026/` and `evidence-index/sources-text/`;
> - the dataset `analysis/action_reaction/pairs.py` (37 step-and-reaction pairs; output in
>   `pairs_output.txt`, table in `pairs.csv`).
>
> **Checked against the originals today:** the 11 Feb 2025 email (Gmail); the 17 Dec 2024 "not at all costs"
> statement (quoted verbatim in your 14 Jul 2025 email, exhibit to the 26 Feb 2026 affidavit, p 15); the
> 3 Aug and both 14 Aug 2026 emails; the 8 Sep 2026 cover letter; the 13 May 2026 pleading's decision sought.
>
> All times AEST. ⛔ The February 2026 complaint and conflict items are described by existence only. Medical
> material appears only as "medical documents". Employment-track material is not reproduced.

## Short answer

1. **They react to the type of step, not to you.** The pattern holds across 23 months:

   | Your step | Their reaction | Record |
   |---|---|---|
   | A settlement offer, or "please concede" | Refused. No counter-offer, no reasons beyond their pleading, no conferral | 4 of 4 |
   | Pressure: complaints, carriage, findings against their people | Ranks close: refused or ignored; Counsel brought in | 0 concessions from 5 |
   | A rule-based notice with a clock | Answered inside the time; the second one mostly admitted | 2 of 2 on time; 298 of 303 |
   | A request for documents | Always delivered, often slowly, with apologies | 3 of 3; median about 18 days |
   | A legal or merits question in correspondence | Never answered on the substance; deferred to Counsel or the conference | 0 of 7 answered; the 19 Oct set is now under a dated undertaking |
   | Dates, time, process, a Commission instruction | Fast and reciprocal | minutes to days |

2. **When you plead, they investigate before they argue.** After both of your pleadings (June 2025 and April
   2026), their first move was a notice to the employer's own payroll records. Then they pleaded, conceding the
   one point their own test disproved.
3. **The change is stark.**

   | Period | Your steps | Concessions or commitments | Refusals |
   |---|---|---|---|
   | Feb–Mar 2026 | 8 | 0 | 3 |
   | Aug–Oct 2026 | 14 | 7 | 0 |

4. **What changed was your step type, not their character.** Their officer has been courteous throughout: no
   characterisation of you in any 2026 email. They moved when you moved from pressure and offers to notices,
   documents and closed questions.
5. **What they have never done:**
   - argued with you in writing;
   - threatened costs in correspondence;
   - pushed for dismissal or lapse, even through five months of dormancy;
   - contested a fact they could check.

   **What they still hold:**
   - the costs claim in their 13 May pleading;
   - the "reasonable" contentions;
   - the right to object to relevance and admissibility at the hearing.
6. **The bottom line: they do not negotiate with you; they verify you.** Every concession has come through a
   channel that lets them say the record required it: rule 49, "upon further review of the appeal file", or
   "new information". They told you on 17 Dec 2024 that this is how they change position: "the Regulator does
   not defend review decisions at all costs and depending on what new information, if any, is obtained during
   the course of the appeals process, we may decide to concede an appeal."

## 1. How this was built

- **Every step you took in the appeal** was paired with the first reaction from the Regulator (or from OIR or the
  Commission where they answered instead). Each pair is coded by step type and reaction type, and timed.
- **Steps were coded by what they ask for**, not by tone: offer, pressure, rule-based notice, document request,
  legal question, process, narrowing, filing.
- **"No reply"** means nothing in the 60 threads answers it. It is then run through the silence filter: would an
  answer have been normal, cheap, and wanted by a party that was fighting? Silence imposed by role (an application
  is answered at the listing, not by email) is separated from silence by choice.
- **Limits** are in section 10.

## 2. The eight reaction rules, with the evidence

### Rule 1. Offers are refused. The speed shows who decided

| Your step | Their answer | Time taken |
|---|---|---|
| 6 Feb 2025, after a call: documents, and a request that "conceding on some points" be considered | 11 Feb 2025: "After considering all of the information, it is the position of the Regulator to continue to the defend the appeal"; only events "leading up to your attendance at your GP" are relevant; "Any events post that date cannot be considered causative of you sustaining your alleged injury"; "this appeal is only in relation to your workers' compensation application" | 4.7 days |
| 18 Feb 2026, Calderbank #1 (open 7 days) | 19 Feb: "The Respondent does not accept your offer, and we will be defending the appeal." | 23 hours |
| 1 Jul 2026, Calderbank #2 (open 21 days, with an invitation to confer) | 16 Jul: "The Respondent's position remains to defend the appeal as outlined in our Statement of Facts and Contentions. Should our position change at any point, we will advise you as soon as possible." | 15.2 days |
| 31 Jul 2026, without-prejudice "material development" letter | 14 Aug: "its position remains to defend… As mentioned previously, please note that should our position change at any point, we will advise you as soon as possible." | 14.1 days |

**Never once:** a counter-offer, a reason beyond "our Statement of Facts and Contentions", or acceptance of an
invitation to talk.

**What the timing tells you (inference):**
- The 23-hour no was reflexive: a standing "defend" instruction applied without a review.
- The 15-day no went up the chain: time to brief, consider and approve a text.
- The 14 Aug no reused the approved text ("As mentioned previously").

**The clause that matters** is the one added on 16 Jul: "Should our position change at any point, we will
advise you." It is the channel they have reserved for a change. A change, if it comes, will arrive as their own
advice after a review, not as an acceptance of your offer.

**The defend line has not appeared since 14 Aug.** It is absent from every communication since 8 Sep.

### Rule 2. Pressure closes ranks and never buys a concession

**February 2026, your steps:**
- urgent filings;
- a complaint to OIR about the conduct of the appeal, with a request for a different officer (quarantined:
  existence only);
- a notice to the Registrar of a conflict;
- a supplementary application seeking findings, referrals, strike-out and removal of the Regulator's
  representatives.

**Their reactions:**
- OIR kept the complaint separate from the appeal. Its appeals manager confirmed within a day that Matheson
  "shall continue to represent" the Regulator "unless and until" a conflict was "identified and established".
  On 23 Feb OIR reported no further action.
- Counsel was confirmed for every listing in the contested phase (27 Feb, 13 Mar, 7 Apr). The 26 Feb mention was
  moved because Counsel was in another hearing.
- The first notice to admit was answered with denials and reasons.
- Calderbank #1 was refused the next day.

**But the officer stayed courteous.** The morning after the urgent filing she waived hard-copy service "to save
any difficulty to you".

**Count:** five pressure steps; two refused, two ignored, one courtesy; no concessions.

### Rule 3. A rule-based notice with a clock is answered in time, and the answer tracks what can be checked

| Notice | Answer | What was admitted | What was denied |
|---|---|---|---|
| **#1**: 11 Feb 2026, 50 facts | 6.9 days, inside the time | The documented facts: the 7-hour break, the payroll instruction, the 25-day AVAC delay | Inferences. On fact 47 (that Taylor held the instruction from 3 May): "needed confirmation from payroll" |
| **#2**: 28 Aug 2026, 303 facts and 39 documents | 10.9 days, three days early | 298 of 303 facts; 25 of 39 documents | Nothing; five facts "not admitted" |

**The 8 Sep cover letter** came with notice #2. It sets out rule 49 in full and limits everything: "for the
proceeding only", existence and wording only, "a hearing de novo", relevance and admissibility reserved.

**The difference between the two:** the second notice asked only what the documents say. In February they
denied inferences. In August there were none to deny.

### Rule 4. Document requests are always met, slowly, with apologies; the Regulator now fetches from Metro South

| Your request | Their answer | Time taken |
|---|---|---|
| **24 Jul 2026:** list of documents and copies of their NNPDs | 3 Aug: holding reply, "I apologise for the delay". 14 Aug: delivered, "I sincerely apologise on the delay" | 20.6 days |
| **9 Sep 2026:** 14 disputed tabs | 10 Sep: extension asked. 24 Sep: four confirmed "upon further review of the appeal file", nine asked of MSH. 12 Oct: nine delivered, "The regulator confirms the veracity" | 14.9 days for four; 32.8 days for nine |
| **7 Oct 2026:** Tab 32A by 16 Oct | Confirmed on the date: both tabs, with the 8 Sep reservation | 9.3 days |

**The standing offer behind all of these** came on 20 Mar 2026: "you can email me a request for those documents
and I will disclose them to you without the need for a Notice to Produce."

**Count:** three requests, all delivered (the 9 Sep one in two parts), none refused.

### Rule 5. Legal and merits questions in correspondence are never answered on the substance

| When | Your question | What happened |
|---|---|---|
| 16 Jan 2025 | The review officer's finding on the union | The reply dealt with the list of documents; the question was not addressed |
| 14 Jul 2025 | Four questions, including whether "not at all costs" still held and whether the new payroll documents would be considered | No reply. The answer came by conduct: the 22 Jul 2025 defence sought dismissal and costs |
| 14 Aug 2026 | The Part 2 privilege schedule; the post-injury categories; the properties of Review Decision 69983 | No reply on any point (67 days at 20 Oct) |
| 7 Sep 2026 | Rule 49 says serve, not file | No reply; the point dropped (see rule 6) |
| 9 Sep 2026 | The five facts not admitted (fact 154, the Communication Book; facts 228–231, the Tab 31 register); whether they objected to delivery to the Registry | Never answered |
| 1 Oct 2026 | Whether they consent to leave | Not answered; routed to the conference (12 Oct) |

**Count:** seven sets of legal questions, counting the 19 Oct letter. Five were never answered, one was
deferred to the conference, and one is now under a dated undertaking.

**Where their merits positions actually appear:**
- in formal documents only: both pleadings, the notice responses, the 8 Sep letter;
- once in an email: 11 Feb 2025, the post-injury cut-off.

**The exception, as of 20 Oct:** "I will review your letter of 19 October 2026 and respond by Friday 30 October
2026 as requested." This is their first written commitment in 23 months to answer questions that touch the law:
s 32(1), ¶27 and leave.

### Rule 6. Challenge one of their procedural assertions with the rule's own words, and they drop it silently

- **7 Sep 2026.** Matheson wrote that the notices "should also be filed with the QIRC registry". Your 10:20
  reply set out rule 49's words (serve, not file) and asked what rule she relied on.
- **What followed:** no reply. The 8 Sep letter does not mention filing, and the point has never come back.

**The mirror image, 20 Mar 2026.** When the rules were on their side, she corrected you: a Form 29 goes to the
employer, not to the Regulator.

**So:** they correct you when a rule supports them, and go quiet when it does not.

### Rule 7. Dates, time and Commission instructions: fast and reciprocal

**They ask for time, and get it:**
- 14 Jul 2025: their defence;
- 17 Feb 2026: the mention moved for Counsel;
- 10 Sep 2026: to 25 Sep. You answered "no conditions attach".

**They give time:**
- 2 Dec 2024: consent to your out-of-time appeal proceeding (the Registry had said the Commission could not
  extend time itself);
- 20 Aug 2025: consent to your extension, 25 minutes after you asked;
- 12 Feb 2026: hard copies waived.

**They meet clocks early:**

| Clock | Met |
|---|---|
| Rule 49 response | 3 days early |
| Outlines | 6 days early |
| Counsel's dates after the 13 Oct instruction | 3 days before 22 Oct |

**Their fastest replies:** 21 minutes (witnesses), 25 minutes (consent, 2025), 54 minutes (Tab 32A).

### Rule 8. Your Registry filings get no reply unless they create an obligation; your pleadings trigger an investigation

**Pleading 1:**
1. 11 Jun 2025: your Form 9A (lawyer-drafted).
2. 4 Jul 2025: three non-party notices, to the two treating practices and to Queensland Health payroll. The
   payroll notice sought "Any amended Payslips… (including date of amendment…)" and the 2020 agreement.
3. 22 Jul 2025: a defence seeking dismissal and costs.

**Pleading 2:**
1. 8 Apr 2026: your Amended 9A.
2. 27 Apr: a notice to payroll for the leave form with "screenshot(s) of the request progression over time".
3. 13 May: the amended defence. It concedes ¶14(e), "a review indicates that in fact, the attachments were
   present", but pleads "human error", "reasonable in all respects", and still asks that you pay the costs of
   the hearing.

**Your Form 29 and rule 64G application against MSH:** no written position from the Regulator at all, and 67
words from Matheson at the 7 Aug mention.

**Your 10 Aug withdrawal:** no acknowledgement from anyone. From then on, though, the Regulator became your
channel to MSH (section 4, counter 6).

**Fencing.** When material crosses their time boundary (after the injury) or their forum boundary (the
employment matter), they fence it off. They did so in their 11 Feb 2025 email ("only… events leading up to
your attendance at your GP"; "Any other matters… will be dealt with separately"), in ¶25 of both defences,
and by silence on 14 Aug 2026.

## 3. Phase by phase: every step and its reaction

### Phase 0, Nov 2024 to Jan 2026: open door, then defence, then dormancy

| Date | Your step | Reaction | Time | Type |
|---|---|---|---|---|
| 26–27 Nov 2024 | Appeal filed out of time; the Registry asks the Regulator | "happy for the appeal to proceed" | 5.1 days | Concede |
| 27 Nov 2024 | Letter enclosing the appeal | Form letter: allocated to Matheson; costs reserved (Scale C) | about 7 days | Reserve |
| 17 Dec 2024 | (Their own step) | Matheson: de novo explained; "does not defend review decisions at all costs… may decide to concede"; list of documents served | — | Stated rule |
| 16 Jan 2025 | Evidence; the union-finding question | No list needed; question not addressed | 11 hours | Silence on substance |
| 6 Feb 2025 | Documents; "conceding on some points" | "continue to the defend"; post-injury cut-off; "alleged injury"; other matters separate | 4.7 days | Refuse and fence |
| 11 Jun 2025 | Form 9A (Saines) | Three non-party notices (4 Jul), disclosure and an extension request (14 Jul) | 23 days | Investigate |
| 14 Jul 2025 | Conditional consent; four questions | No reply; 22 Jul defence: dismissal and costs. Your lawyers ended the retainer the next day | — | Silence, then defend |
| 14 Aug 2025 | Urgent request for a stay | Matheson: "I didn't receive this email". The Commission vacated all directions "to give the Appellant a chance to reorganise" (22 Aug) | 7.8 days | Commission accommodates |
| 20 Aug 2025 | Extension request resent | Consented; more time offered. Her earlier email that day set out abeyance for 12 months and the rule 230 lapse | 25 minutes | Concede |
| Sep 2025 to Jan 2026 | Nothing in the record (whether the 30 Sep 2025 progress update went is not in Gmail or the repo) | They took no step: no lapse, no strike-out | — | Not attrition |

### Phase 1, Feb–Mar 2026: pressure

| Date | Your step | Reaction | Time | Type |
|---|---|---|---|---|
| 11 Feb | Urgent filing: Form 4 (exclusion, sealing, production), affidavit, 381 pp | Receipt; hard copies waived "to save any difficulty to you" | 18.7 hours | Accommodate |
| 11 Feb | Notice to admit #1 (50 facts) | Response filed 18 Feb: admissions plus denials with reasons | 6.9 days | Mixed |
| 12 Feb | Complaint to OIR and a request for a different officer ⛔ existence only | Separated from the appeal; carriage change refused (13 Feb); no further action (23 Feb) | 1–11 days | Refuse |
| 12 Feb | "Service & Carriage" to Matheson | No reply from her (Ethical Standards answered) | — | Silence (role) |
| 12 Feb | Conflict notice to the Registrar | OIR: Matheson "shall continue to represent" | 18.2 hours | Refuse |
| 18 Feb | Calderbank #1 | "does not accept… we will be defending the appeal" | 23 hours | Refuse |
| 25 Feb | Supplementary Form 4 (findings, referrals, strike-out, removal) | No written reply; Counsel at the 27 Feb mention and the 13 Mar conference | — | Silence (role) |
| 20 Mar | Withdraws those limbs; proposes a timetable and a notice to produce | Informal disclosure offered; Form 29 route corrected; withdrawals not mentioned | 3 hours | Accommodate |

### Phase 2, Apr–Jul 2026: pleading, the MSH fight, offers

| Date | Your step | Reaction | Time | Type |
|---|---|---|---|---|
| 7 Apr | Leave to amend sought at the mention | Granted the same day; nothing in the record shows opposition; 35 days to re-plead | same day | Not opposed |
| 8 Apr | Amended 9A | Own notice to payroll (27 Apr), then the 13 May defence: ¶14(e) conceded, "reasonable in all respects", costs | 19 days / 35 days | Investigate, concede one, defend |
| 22 Apr | Form 29 to MSH (Regulator served) | No written position | — | Silence (role) |
| 22 May | Mention | Matheson alone; no Counsel | — | Downshift |
| 11 Jun | (Their own step) | Disclosed employer correspondence of 15–16 May 2024 obtained through their notice and conferencing | — | Disclose |
| 12–23 Jun | Rule 64G application, refiled | No written position | — | Silence (role) |
| 1 Jul | Calderbank #2 | The formula, plus "Should our position change" | 15.2 days | Refuse |
| 24 Jul | List of documents and NNPD copies | Holding apology 3 Aug; delivered 14 Aug | 20.6 days | Comply, slowly |
| 31 Jul | WP "material development" letter | The formula, "As mentioned previously" | 14.1 days | Refuse |

### Phase 3, Aug–Oct 2026: admissions

| Date | Your step | Reaction | Time | Type |
|---|---|---|---|---|
| 7 Aug | Mention on the 64G | Matheson alone; 67 words; "No" to Dwyer's question whether he had placed a burden on her she would not accept | — | Neutral |
| 10 Aug | Withdraws the 64G; does not press the Form 29 | No acknowledgement; the Commission's FDO(3) is made "FURTHER TO" it | — | Silence (role) |
| 12 Aug | Stressor 1(a) bundle | No reply | — | Silence (role) |
| 14 Aug | Part 2; post-injury categories; Review Decision 69983's properties | No reply on any point | 67 days | Silence (see section 6) |
| 28 Aug | Notices #2: 303 facts, 39 documents | 7 Sep "reviewing"; 8 Sep: 298 admitted, 0 denied; 25 documents; reservation letter | 10.9 days | Concede and reserve |
| 28 Aug | Which witnesses? Offer to confer | "cannot confirm its witnesses at this stage"; 24 Sep: Taylor, Reese, Wright, Earl | 21 minutes / 27 days | Defer, then file |
| 7 Sep | Rule 49: serve, not file | No reply; point dropped | — | Drop |
| 9 Sep | Outlines, medical schedule, footing letter, tabs request | Extension; 4 confirmed, 9 to MSH; then 9 vouched (12 Oct); the five facts never answered; no expert by 30 Sep | 1 day / 15 days / 33 days | Concede documents; silent on facts |
| 10 Sep | Extension agreed "no conditions attach" | Outlines 24 Sep, six days early | — | Reciprocate |
| 1 Oct | Election; directions 2–7; leave; Second Amended 9A | Auto-reply; 7 Oct receipt; 12 Oct: conference agreed, items 2–7 "in lieu of ordered in directions"; leave not answered | 10.7 days | Concede the conference; defer the law |
| 7 Oct | Tab 32A by 16 Oct | Both tabs confirmed on the date, with the reservation | 9.3 days | Concede and reserve |
| 13 Oct | (Dwyer's instruction) | Counsel's dates on 19 Oct | 5.9 days | Comply early |
| 19 Oct | All three dates; six closed questions by 30 Oct | 20 Oct: joint dates to the Registry (letter not mentioned); "respond by Friday 30 October 2026 as requested" | 17.7 hours | Commit |

## 4. Your counters, one at a time: what each did to them

1. **The February 2026 pressure package hardened them for six months.**
   - Counsel at every listing, denials in the first notice response, a next-day no to the first offer.
   - Their officer's conduct was put in issue, and the institution answered by separating the complaint from
     the appeal.
   - On the appeal itself it bought nothing. Sealing was dealt with by Dwyer on 13 Mar.
2. **The 20 March withdrawal brought their most helpful reply on record.** Within three hours: informal
   disclosure on request. At the next listing (7 Apr), leave to amend went through with no opposition recorded.
3. **The Amended 9A was tested, not argued.**
   - They went to payroll, found the leave attachments had been there, and pleaded that concession (¶14(e)).
   - They then rebuilt the defence around "human error" and "reasonable in all respects".
   - A verifier concedes where its own test fails, and holds the rest.
4. **The Form 29 and 64G fight with MSH: the Regulator stayed out of it.** It was not their fight. But five days
   after your notice, they ran their own notice to payroll. On 11 Jun they disclosed employer correspondence
   they had obtained themselves.
5. **Calderbank #2 and the WP letter were refused by formula.** The only gain was the 16 Jul clause, "Should our
   position change at any point, we will advise you", which stated the channel for a future change.
6. **The 10 Aug withdrawal and the 28 Aug existence-only notices produced the largest single movement on the
   record.**
   - 298 of 303 facts admitted, none denied.
   - No defend line since.
   - The Regulator took over the role your 64G was meant to play: it asked MSH for nine documents (24 Sep) and
     vouched for them (12 Oct), then vouched for Tab 32 (16 Oct).
   - A three-way fight with an objecting employer became a two-party documentary record that the Regulator
     certifies.
7. **The 14 Aug questions on the review decision's properties met total silence.** Read it honestly:
   - on a de novo appeal the review's process is legally beside the point;
   - no institution discusses its decision-maker's process with an opponent in writing.

   This silence is mostly role-driven and signals nothing either way. Do not press it. It sits closest to
   discipline rule 1, and pressing it would hand them the kind of step that has always hardened them (rule 2).
8. **The 9 Sep package drew time, then documents.**
   - They asked for an extension, then dealt with 13 of the 14 tabs.
   - Their 24 Sep outlines came with no expert.
   - The five non-admitted facts were never answered. Four of them (228–231, the Tab 31 register) are now
     question 1 of your 19 Oct letter. The fifth (154) is the Communication Book.
9. **The 1 Oct election and corrected 9A got the conference, but the law was sent to Counsel.**
   - "In lieu of ordered in directions" means they want no orders.
   - Leave is the unanswered item; it now sits inside the 30 Oct undertaking.
10. **The 19 Oct letter brought a dated written commitment.** It is the first time in the record they have
    undertaken to answer law-touching questions by a date.

## 5. Speed: what they answer fast, slow, and never

| Step type | Answered | Typical time | Never answered |
|---|---|---|---|
| Process, dates, Commission instructions | Nearly all | 21 minutes to 6 days | 1 (a disclosure bundle needing no reply) |
| Pressure | Only by OIR, never on the merits | About a day | 2 |
| Rule-based notices | 2 of 2, in time | 7–11 days | 0 |
| Document requests | 3 of 3 (one in two parts) | Median about 18 days (9 to 33) | 0 |
| Offers | 4 of 4 refused | 4.7 days (2025); then 23 hours, 15 days and 14 days (2026) | 0 |
| Legal and merits questions | 0 of 7 on the substance | — | 5 silent, 1 deferred, 1 now undertaken |

**The pattern:** speed follows consequence, not difficulty.
- **Fastest:** what costs nothing ("cannot confirm" in 21 minutes) and what a clock or the Commission demands.
- **Slowest:** what needs someone senior: offers, and documents held by MSH.
- **Never:** whatever would commit them on the law in writing to you.

## 6. The silences, filtered

| Silence | Normal to answer? | Cheap? | Wanted by a fighting party? | Reading |
|---|---|---|---|---|
| 14 Jul 2025, four questions | Yes | Yes | No | **Choice.** Answered by conduct (the 22 Jul defence) |
| 12 Feb and 25 Feb 2026 applications | No (answered at the listing) | — | — | **Role** |
| Form 29 and 64G | No (your dispute with a non-party) | — | — | **Role** |
| 10 Aug withdrawal; 12 Aug bundle | No reply needed | — | — | **Role** |
| 14 Aug: Review Decision 69983's properties | No (irrelevant de novo; institutional) | No | No | **Role and caution.** Signals nothing |
| 14 Aug: Part 2 privilege ("or confirm nothing is withheld") | Yes | Yes, one line | Yes, if nothing is withheld | **Choice or oversight.** Ordinary if privileged material exists (Counsel's advice is privileged). Low weight |
| 7 Sep: filing basis | Yes | Yes, if a rule existed | Yes | **Choice.** No rule to cite, so the point was dropped |
| 9 Sep: five facts; objection to delivery | Yes | Moderately | Yes, if they had a reason | **Choice.** Explaining a non-admission invites argument |
| 1 Oct: consent to leave | Yes | No (a legal position) | — | **Choice, routed to Counsel.** Now inside 30 Oct |

**The silences that carry signal are the choices:** the filing basis (they had no rule), the five facts, and
leave. Each is a point where answering would have meant either conceding or arguing in writing. They did
neither, consistent with rule 5.

## 7. How their picture of you changed, in their own words

| When | Their words | What it shows |
|---|---|---|
| Dec 2024 | "the Regulator does not defend review decisions at all costs… we may decide to concede an appeal" | The stated decision rule: new information |
| Feb 2025 | "your alleged injury"; post-injury events "cannot be considered causative"; "only in relation to your workers' compensation application" | An appellant to be processed and fenced |
| Jul 2025 | A defence seeking dismissal and costs | Full defence on the 2025 pleading |
| Aug 2025 | "this may be difficult now that you are no longer represented"; abeyance; the lapse rule | A self-represented appellant offered a quiet exit, while still given time |
| Feb 2026 | "we will be defending the appeal"; Counsel at every listing | An adversarial litigant to be contained |
| Mar 2026 | "you can email me a request… I will disclose them to you" | A litigant to be helped on process |
| Jul–Aug 2026 | The formula; "As mentioned previously" | Held at arm's length on the merits |
| 8 Sep 2026 | "So that there is no misunderstanding as to the effect of the enclosed responses…" | A documentary opponent whose notice had to be contained |
| Oct 2026 | "Thank you for your assistance"; "Thankfully"; "the parties"; "as requested" | A counterparty in a joint process |

**About the 8 Sep letter.** It is the most carefully built document they have sent you:
- it sets out rule 49 in full;
- it limits each admission;
- it states the hearing is de novo;
- it reserves relevance and admissibility.

It is in a lawyer's register, and it is signed "Appeals Officer, Appeals Unit" where her emails say "Senior
Appeals Officer". That points to a settled template rather than her email voice; low weight. **The care is the
tell:** they recognised what the second notice had done and built a firewall around it.

**"Alleged" is gone.** It appears in her February 2025 email and in none of her 2026 emails.

## 8. MSH and the Commission, for contrast

**MSH:**
- an 18-minute internal redirect;
- an extension request eight days later, sent to the Regulator rather than the Registry;
- absent from the 22 May mention;
- its objection an hour before the deadline;
- silent after service of the 64G.

Since your 10 Aug withdrawal it has disappeared from the correspondence. Its documents now reach you through
the Regulator, vouched.

**The Commission (Dwyer):**
- **Your procedural requests have been granted, or more than granted:**
  - Aug 2025: all directions vacated "to give the Appellant a chance to reorganise";
  - 7 Apr 2026: leave the same day;
  - 19 Aug 2026: FDO(3) "further to the correspondence of the Appellant".
- **No contested ruling, ever.**
- **Neutral formulas throughout.**

## 9. What it predicts

1. **30 Oct.** By rule 5's history, expect:
   - the documentary items answered;
   - the legal items (s 32(1), leave, ¶27) answered at the level of "to be discussed at the conference", or a
     position that commits to little.

   The earlier table stands: shape A (documents answered, law deferred) about 45%.
   (`2026-10-20_EVERY_DATA_POINT_7-20OCT_Matheson_QIRC_and_the_19Oct_letter.md` §5B.)
2. **What would be new.** Any substantive legal position in writing would be the first in 23 months.
   - "Not opposed" on leave, or "not contested" on s 32(1), would be the strongest signal yet.
   - The defend formula returning would be the clearest bad one (about 15%).
3. **The channel for any concession** is their own advice ("should our position change… we will advise you"),
   framed as a review on new information (Dec 2024; Guide 5.1), after the conference. It will not come as an
   accepted offer. So do not send an offer now. Keep feeding the new-information channel: the 30 Oct answers,
   the one-page agenda, the doctors' availability.
4. **If they need time after leave,** expect them to ask for it. They took 35 days in April, and each pleading
   has been followed by a records check. There is little left to check: 38 of 39 documents are confirmed.
5. **What would harden them again** is anything from the pressure family: complaints, findings sought against
   their people, characterisations. The record says that costs months.

## 10. Limits

1. **The Gmail connector cannot open attachments.** Their contents come from the repo's copies:
   - the 8 Sep letter and responses;
   - the 24 Sep outlines;
   - the 12–16 Oct items;
   - the 13 May defence;
   - the Form 29 notices;
   - the 14 Aug emails.

   The first notice response (Feb 2026) has a broken text layer, so its content is from the verified extracts
   in `skill/references/FORM24-VERIFICATION-5AUG.md`.
2. **Some originals survive only as quoted text** (for example 7 Sep 09:43 and 7 Oct 08:20). Two dates differ
   between sources (FDO(3) 18 or 19 Aug; the Amended 9A "filed 7" or "8 April"). Neither changes a reading here.
3. **Whether a progress update was sent by 30 Sep 2025** is not in the record.
4. **Correlation, not proof.** The August admissions also reflect that the facts are documentary. The pattern
   (narrowing moves them, pressure hardens them) is consistent across 37 pairs, but the record cannot separate
   your step from everything else happening at the same time (Dwyer's 7 Aug remarks, their own verification).
5. **Coding is judgement.** Each pair and its code are in `pairs.py` so any one can be checked or re-coded.
6. **Quarantine held.** The February 2026 complaint and conflict items appear by existence only. The
   employment-track material in the 6 Feb 2025 email and Saines' advice are not reproduced.
