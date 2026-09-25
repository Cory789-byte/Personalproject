# WC/2024/227 — ONBOARDING
> **This is the entry point. Written 12 September 2026. It supersedes the read-order in CLAUDE.md.**
> Everything below was verified from source in the session of 12 September 2026, or carries a
> pointer to where it was. Where something is unverified it says so.

---

## 1 · READ ORDER

| You have | Read |
|---|---|
| **5 minutes** | this file, §2 and §3 |
| **30 minutes** | + `CURRENT.md`, `skill/references/INDEX.md`, `index/EVENT_LEDGER_README.md` |
| **Before drafting anything** | + `CLAUDE.md` §"The discipline rules", `skill/references/RULES-admissions-documents-and-sequence.md` |
| **Before asserting any fact** | `index/EVENT_LEDGER.tsv` → the paragraph number → the source document. **Never from a note.** |

⛔ `working-notes.md` is 622KB of running log. It is history, not authority. Do not read it to
find the current position; read it only to find out *when* something happened in the work.

---

## 2 · THE LIVE POSITION — 12 September 2026

**The appeal.** Cory Lea Shepherd v Workers' Compensation Regulator. Appeal under **WCRA s 549**;
notice of appeal filed under **s 550(4)**; hearing **de novo** (Appeal Guide p 279 — *not* from any
section of the Act; s 561(3) is the appeal *from* the Commission to the Industrial Court).
Commissioner **Dwyer**. Psychological injury; the whole appeal is **s 32(5)(a)**.

**Where it stands.**

| Date | What |
|---|---|
| 28 Aug 2026 | Form 24 (303 facts) + Form 25 (39 documents) served |
| 8 Sep 2026 | Response: **298 admitted, 5 not admitted, 0 denied**; Form 25 — 25 authenticity admitted, 14 disputed |
| 9 Sep 2026 | Direction 2 material served: witness list, outlines, medical schedule M1–M9, the letter fixing the footing, the request for what was not admitted |
| 10 Sep 2026 | Matheson seeks extension to **25 Sep** on the production request only |
| **25 Sep 2026** | Matheson's extended date |
| ⭐ **30 Sep 2026, 4pm** | **Directions 3 and 4 — the Respondent's witness list and outlines.** Fixed by the Commissioner; she cannot move it |
| after that | **Direction 5: the Appellant must contact the Registry** to proceed to a second s 552A conference or to hearing, or the matter may be placed in abeyance and lapse under r 230 |

**No hearing date is listed.**

**The live document.** `drafts/out/FORM9A_SECOND_AMENDED_FOR_FILING.pdf` — Second Amended Form 9A,
14pp, metadata clean, **not yet served**. Internal annotated build at `drafts/INTERNAL/`.
⭐ **Recommendation on the record: serve it well before 30 September**, so the Respondent's witness
list and outlines are prepared against the amended case.

---

## 3 · CANONICAL SOURCE FOR EACH QUESTION

⭐ **The rule: one question, one canonical file. If two files disagree, the one named here wins.**

| Question | Canonical source |
|---|---|
| What was admitted, and at which paragraph | `documents/regulator-response-2026-09-08/SERVED_303_facts_and_verdicts.json` |
| What happened on a date, and is it admitted | `index/EVENT_LEDGER.tsv` |
| The served response and its qualifications | `documents/regulator-response-2026-09-08/` (originals) |
| How r 49 works; documents vs facts; the sequence | `skill/references/RULES-admissions-documents-and-sequence.md` |
| The response analysed against r 49 | `skill/references/FORM24-25-RESPONSE-against-the-rules.md` |
| Withdrawing an admission | `documents/authorities/Tuesley_v_WCR_2020_QIRC_027.pdf` + `skill/references/RULE-49-CASE-LAW-how-rare-this-is.md` |
| What the decision under appeal found | `documents/Review_Decision_69983_24.10.2024.pdf` — **read it, do not quote the notes** |
| The pleading as it stands | `drafts/form9a_content.py` + `drafts/build_form9a_secondamended_onus.py` |
| Instruments (EB11, Award, WCRA, IR Act, Rules) | `documents/instruments/ATT*.pdf` |
| Directions and deadlines | `documents/orders/` — ⛔ **no text layer, render with `pdftoppm -r 150 -png`** |
| Correspondence | `documents/correspondence-2026/`, `corpus/FULL_CORPUS.md` |
| Everything else | `skill/references/INDEX.md` (178 notes, grouped) |

---

## 4 · CORRECTIONS LEDGER

Everything here was believed and was wrong. **Each line is a mistake that cost time or would have
cost credit.** Read before repeating any of them.

| # | Was believed | Actually | Verified from |
|---|---|---|---|
| 1 | The appeal is under s 550(4) | Brought under **s 549**; s 550(4) is only the filing step. Every sealed order is headed s 549 | WCRA ss 549, 550; `documents/orders/2026-08-19_Further_Directions_Order_3_SEALED.pdf` |
| 2 | The de novo character comes from s 550 | **No provision says so.** It comes from the Appeal Guide and authority. s 561(3) is the appeal to the Industrial Court | WCRA s 561; Appeal Guide p 279 |
| 3 | The notice has 308 facts | **303.** `build_form24_second.py` is a working draft that moved on after service | the served response |
| 4 | The UCPR applies / the UCPR does not apply | **Both were wrong in turn.** The IR(T) Rules do not adopt it — but **WCRA s 553(1) applies UCPR ch 7 pt 2** (disclosure generally, incl. **r 215** originals for inspection, and interrogatories) **and ch 9 pt 4** (mediation, case appraisal). **r 189 (notice to admit) still does not apply** — it is in ch 6. r 49 IR(T) remains the admissions provision | WCRA s 553; IR(T) rr 70, 106, 111, 123ZB |
| 5 | r 49(3) is the risk to the 298 | r 49(3) reaches an admission **"taken to have been made under subrule (2)"** — a *deemed* one. These are **express**, served in 11 days. The rule does not on its face reach them | IR(T) r 49; the response |
| 6 | r 49 carries a costs sanction for refusing | ⛔ It does not. **UCPR r 189(4)** does; r 49 has no equivalent. Costs run through **WCRA s 558(3)** | both rules |
| 7 | The ESU referred the matter to HR in Dec 2024 | **Twice — 27 May 2024 and again 24 Dec 2024.** The May referral is in the decision under appeal at Factor 2 | Review Decision 69983 pp 12–13 |
| 8 | The complaint concerned the effect on clinical staff and call times | ⛔ **The form does not say that.** It is directed at the manager personally. Only "concerns raised within the department were not being addressed" and "decisions… that directly affect service delivery and patient outcomes" survive | `documents/2024-05-13_ESU_PID_Complaint_Form_E5_Att1.pdf` |
| 9 | The review officer answered the wrong EB11 clause | ⛔ **Cory cited cl 1.9 himself** (Posting of the Agreement) in his response of 9 Aug 2024. Do not run this as their error | Review Decision 69983 |
| 10 | Prizeman puts the onus on the Respondent | ⛔ Reverse. The **appellant** bears it; *Prizeman* is reality v perception. Expressly withdrawn in the new pleading | Appeal Guide 7.3 |
| 11 | Factor 2 was not substantiated | **Substantiated in part** — "to the extent that you lodged a complaint, and some action was taken." The Conclusion finds the injury arose out of factors **2, 3 and 4** | Review Decision 69983 |
| 12 | The employer "relied solely on information from you" and closed fairly | Lodged 13 May, **closed 27 May — 14 days**, 7 days after particulars were first sought | Review Decision 69983 |
| 13 | The Form 24 outline citations | Ranges were derived from an enumeration that counted headings as facts; all nine were wrong by ~4. **Never hand-count** | the served numbering |
| 14 | Form 24 (Feb 2026) response numbering is 1:1 | Drifts after ¶25. All "Form 24, Para N" cites are in **notice** numbering | `2026-02-18_Form24_Response...pdf` |
| 15 | There is "settlement" to be had | ⛔ **No commercial settlement is possible** (Guide 5.1). The outcomes are **concession**, discontinuance, or hearing. Concession follows a **conference**, on "new information … not yet considered" | Appeal Guide 5.1 |
| 16 | Counsel can simply be hired | **WCRA s 552B** — a lawyer may appear at a conference or hearing **only with** the other party's agreement or the appeal body's **leave** | WCRA s 552B |
| 17 | The Regulator holds the psychiatric file | Its amended List of Documents lists **only the report** (item 10) and the **GP** records (item 11) — no Mind & Memory file or correspondence. The 4 Jul 2025 notice was limited to "concerning work related issues" | LOD 14 Aug 2026; NNPD 4 Jul 2025 |
| 18 | Executing the attendance-notice threat is always good | It is the **worst** of three outcomes: he cannot lead or cross-examine his own witness, and pays her conduct money. The **threat** is valuable; **execution** is a fresh decision on 1 Oct | Guide 10.1; IR(T) r 62; s 531 |

**Corrections that were mine about people, not documents** — Dwyer knew what the application contained;
the disclosure answer of 18:03 was not mistaken; the 24 July request had *not* already been done in the
form the bench directed; speech rate is normal, the load is integration not parsing. ⛔ **The pattern:
every one was an inference about why someone did something.** See §7.

---

## 5 · STANDING DISCIPLINES (full text in `CLAUDE.md`)

1. ⛔ Never voiced in either track: the December 2024 respondent matter, that it was struck out, the
   service of a separation document.
2. ⛔ The word **"fraud"** never appears in the WC track. Nor "malicious", "corruption", "plot".
3. ⛔ Never "continuity of service preserved" — *"reinstated to my employment with an effective date of
   20 September 2024, the reinstatement taking effect despite any payroll documentation."*
4. ⛔ WCRA s 32(1) is **"a significant contributing factor"** — never "major".
5. ⛔ No erectile-dysfunction material in any document.
6. ⛔ Conspiracy, collusion and motive never reach paper. **State the chronology, never the motive.**
7. ⛔ Never open the s 32(5)(b) door — no *punishment, hostile, capricious, reprisal* from our side.
8. ⛔ PID/reprisal stays off the WC track. Content of the disclosure never set out.
9. ⛔ `documents/2025-hughes-history/AttA`–`AttD` (DFV material) **deliberately not opened.** Ask first.
10. Originals only, metadata scrubbed, served originals never rebuilt.
11. HopgoodGanim: **"Ask. Never allege."** Do not publish, post, forward or circulate.

---

## 6 · WHAT IS NOT BUILT — refreshed 13 Sep evening

**Built today, awaiting his decision:** the letter to Matheson (extension agreed; ¶6 foreshadow
behind a flag) · the one-page **element grid** for the conference · the **Second Amended Form 9A**
(⚠ **still a draft, not served**).

- ⛔ **An exhibit list** keyed to the 39 tabs + M1–M9, in tender order. ⭐ **Now with a statutory
  deadline: WCRA s 554** — every document to be adduced must be given to the other side **at least
  10 business days before the hearing**, or it cannot be relied on without leave.
- ⛔ **The Emergency Code Register** (¶¶ 228–231). Production first, admissions second (r 46(2)).
  **UCPR r 215** (via s 553) is available for originals of anything they have disclosed a copy of.
- ⛔ **Item 5 — Dr Krishnaiah's clinical records**, requested 5 Sep, not received. ⭐ Fold in the
  question of **what Mind and Memory produced to the Regulator** under the 4 Jul 2025 notice, and
  on what scope. One letter, two answers.
- ⛔ **The 24 December 2024 ESU letter** — OneDrive `E5 PID Outcome Letter`.
- ⛔ **The doctors' availability confirmed in writing**, and **conduct money** at expert rates
  budgeted (Guide 10.1; IR(T) r 62). Nothing in the repo evidences either.
- ⛔ **Readiness for a WCRA s 556 examination** — consent promptly; be heard on the **brief**
  (the admitted facts + Tabs M1–M4), specialty, costs, timing.
- ◻ Witness decision on Ms Jeffrey and Mr Parry — before 30 September if they are to be added.
- ◻ 46 pending `[¶ ___]` slots in the 9A; only ~8 genuinely unproved.

---

## 7 · HOW TO USE THE ASSISTANT ON THIS MATTER

**Reliable:** finding a regularity across documents; cross-document contradiction; arithmetic on
dates; what a rule or a deadline *constrains*; reading a form for its function.

**Unreliable:** why anyone did anything. Every correction in §4's second block is of that kind.

⭐ **The failure mode:** a fluent reconstruction feels identical to a recollection. The output reads
the same whether it rests on 303 admitted facts or on a guess.

⭐ **The rule:** trust it most when it points to a paragraph number; least when it explains someone's
reasoning. **And never let it re-derive a sequence by search — send it to `EVENT_LEDGER.tsv` first.**
Re-derivation is where corrections 7, 8 and 13 came from.
