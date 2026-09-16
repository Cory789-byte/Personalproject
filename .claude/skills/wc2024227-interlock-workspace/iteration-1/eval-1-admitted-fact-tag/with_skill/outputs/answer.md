# Is "Admitted Fact: Form 24, Para 37" right for the UMA finding?

**Short answer: No. It is wrong on every available reading — and it is the one proposition in the
whole Form 24 that the Regulator specifically refused to admit.**

---

## Files I actually opened

**Skill:**
- `.claude/skills/wc2024227-interlock/SKILL.md`
- `.claude/skills/wc2024227-interlock/references/interlock-index.md`
- `.claude/skills/wc2024227-interlock/references/source-integrity.md`

**Primary sources (read from the page, not from notes):**
- `wc2024227/documents/filings/2026-04-08_Amended_Form9A_SOFC_Appellant.pdf` — the pleading (5pp, text extract)
- `wc2024227/documents/2026-02-18_Form24_Response_and_email_communication.pdf` — **rendered** at
  `pdftoppm -r 150 -png`, all 13 pages; Notice at render pp. 1–6, Response at render pp. 7–10.
  (Per `source-integrity.md`, `pdftotext` silently drops every exhibit reference, date and quoted
  phrase in this document. I did not rely on the text layer for any part of this answer.)
- `wc2024227/documents/Review_Decision_69983_24.10.2024.pdf` — 28pp, incl. pp. 26–28 and the signature block
- `wc2024227/documents/WC.2024.227_Regulator_SOFC_13.05.2026.pdf` — ¶¶2–5, ¶¶22–25

**Downstream documents checked for propagation:**
- `wc2024227/lodgement/WC2024227_Form20_FINAL.pdf` and `.md` (affidavit ¶41)
- `wc2024227/lodgement/WC2024227_Form4_FINAL.pdf` and `.md` (Item 1 of the disclosure table)
- `wc2024227/lodgement/WC2024227_Form_4_Application_Rule_64G.pdf` and `.docx`
- `wc2024227/lodgement/PRE-LODGEMENT-CHECKLIST.md`
- `wc2024227/drafts/WC2024-227_Rule64G_FILING_v5R_FINAL.pdf`
- `wc2024227/drafts/WC2024227_Application_v5.3_signed_master.docx`

**Working records (used only to know where to look, never as authority):**
- `wc2024227/skill/references/FORM24-VERIFICATION-5AUG.md`
- `wc2024227/skill/references/confirmed-record.md` (targeted reads)
- `wc2024227/skill/references/FULL-PICTURE-READ-6AUG2026.md`
- `wc2024227/working-notes.md` (grep only, for the provenance of one quote)

---

## 1. What the pleading currently says

`2026-04-08_Amended_Form9A_SOFC_Appellant.pdf`, Part B, Stressor 3(d), p. 4:

> **(d) Admitted Unreasonableness:** The Regulator's own Independent Review Office (IRO) formally
> found that this 7-hour rest break constituted unreasonable management action **(Admitted Fact:
> Form 24, Para 37).**

And Contention 3, p. 5, rests on it:

> The Respondent's pleading that "all management action was reasonable" is in direct evidentiary
> contradiction with **its own IRO finding.**

---

## 2. What the Form 24 actually says

The Response numbering drifts from the Notice numbering after row 26. I verified the whole map from
the rendered pages rather than assuming it:

| Response row | answers Notice ¶ |
|---|---|
| 1–25 | 1–25 |
| **26** | **26–29** ← drift starts |
| 27–38 | 30–41 |
| **39** | **42–45** |
| 40–44 | 46–50 |

Three paragraphs matter here, and they are three different things.

### Notice ¶2 — this is your UMA fact

Render p. 1:

> **2.** In the Review Decision dated **24 October 2024** (**Exhibit B1**, p. 27), the Review Officer
> found that rostering the Appellant with a 7-hour break *"amounted to unreasonable management action"*.

**Response row 2** (render p. 7):

> With respect to paragraph 2, **does not admit** the fact contained therein because the appeal is a
> hearing de novo and **it is for the Commission to determine if this fact amounted to unreasonable
> management action.**

### Notice ¶37 — a completely different fact

Render p. 4:

> **37.** In the Review Decision (**Exhibit B1**, p. 16), the Regulator stated: *"I am satisfied your
> employment was a significant contributing factor to the psychological injury"*.

**Response row 34** (render p. 9) — note the row number, not 37:

> With respect to paragraph 37, **admits the contents of the Respondent's review unit decision** but
> says that this fact is **not relevant** because the appeal is a hearing de novo and it is for the
> Commission to determine. action

### Response row 37 — a third thing entirely

Render p. 9:

> With respect to **paragraph 40**, admits the facts contained therein.

Notice ¶40 is the 3 May 2024 email from Payroll Officer Elaine Grant to Ms Taylor. Nothing to do with
the Review Decision at all.

---

## 3. So the citation fails three ways

**Read as a Notice paragraph** (which is the convention the rest of your pleading uses — Stressor 2(b)
cites "Para 40" and "Para 41" for the payroll facts, which are Notice numbers): **Para 37 is the
"significant contributing factor" quote, not the UMA finding.** Wrong fact.

**Read as a Response row:** **row 37 admits the payroll email.** Wrong fact again, and further away.

**Either way, it is not an "Admitted Fact."** Row 34 admits *contents* — that the document says what
it says — with relevance expressly reserved. That is the Type B pattern, not an admission of truth.
And the UMA finding specifically, pleaded at Notice ¶2, is **expressly not admitted** at row 2.

> There is **no admission anywhere in the Form 24** that the 7-hour break amounted to unreasonable
> management action. The Regulator has reserved that question to the Commission twice over — at row 2,
> and again at row 16 ("the characterisation of any management action is a matter for determination by
> the Commission").

**The best argument the other way, and why it doesn't survive.** Row 34's words — "admits the contents
of the Respondent's review unit decision" — are unqualified as to *which* contents, and the decision
contains the UMA finding. You could argue that admits the whole document. But row 2 answers the UMA
finding specifically and refuses it. A pleading is read as a whole, and the specific answer governs the
general. Pushing row 34 to cover the UMA finding puts you in direct conflict with row 2, on a
*Briginshaw* record, in a document you filed by leave. **It is not safe to plead as an admitted fact.**

---

## 4. The good news: the finding is real, and you don't need an admission to prove it

The substance of what you pleaded is **true**. Review Decision 69983, p. 26:

> In considering the evidence, I find there was uncertainty between you and the employer regarding
> whether the 8-hour agreement continued to apply. However, it is not necessary for me to consider
> whether the employer's stance on its application was reasonable. The break between the shift on
> 17 March 2024 and 18 March 2024 equated to 7 hours. Even if you were allowed to leave early on
> 17 March 2024 as suggested by the employer, you left a maximum of 30 minutes early, which meant you
> still did not receive a minimum 8-hour break. **Based on this, I find the rostering of these two
> shifts amounted to unreasonable management action given that it was in direct contradiction to the
> award and the 8-hour agreement.**

And in the Conclusion, p. 27:

> **factor 4 amounted to unreasonable management action.**

**You do not need it admitted. You need it tendered.** It is the Respondent's own delegate's decision,
it is the decision under appeal, and it is Exhibit B1. Prove it by the document.

### Three corrections that come with it

**(a) There is no "Independent Review Office".** The decision is signed:

> Yours sincerely / **Victoria Squires** / **Senior Reviewing Officer** / **Review Unit** /
> Workers' Compensation Regulatory Services

The Respondent's own Form 24 calls it "the Respondent's review unit decision" (rows 34 and 44). The
Regulator's SOFC ¶3 says the WorkCover decision "was confirmed by **the respondent's review unit**".
Your own Notice ¶2 got it right — it says "the Review Officer".

**The correct name is the stronger fact.** "Independent Review Office" invites the answer *so what — an
independent body disagreed with us*. "The Respondent's own Review Unit" is an internal finding by the
very party now denying it. Calling it independent gives away the only thing that makes it bite.

**(b) The finding rests on 8 hours, not 10.** Squires expressly declined to decide whether the 8-hour
agreement applied, and found unreasonableness because **7 < 8 on anybody's case**. Your Stressor 3(b)
pleads the FRMS 10-hour mandate as the yardstick. The finding does not go that far, and Response row 4
denies Notice ¶4 precisely on the strength of the 17 June 2020 agreement — as does SOFC ¶22(e). Plead
the subtraction that nobody can answer, not the one that is in issue.

**(c) The finding did not survive at review — and you need to say why, before they do.** Same decision,
p. 27:

> I note that since two out of the three causative factors amounted to reasonable management action
> taken in a reasonable way, this means your psychological injury **mainly** arose out of such
> management action. Further, factor 4 was initially only substantiated to the extent of one incident
> and it was only the one incident which amounted to unreasonable management action. **Therefore, I
> find overall your psychological injury arose out of reasonable management action taken in a
> reasonable way and section 32(5) is consequently enlivened.**

Squires got there by expressly applying ***Delaney*** — global evaluation — two paragraphs earlier.

---

## 5. ⛔ The bigger problem sitting three paragraphs below the one you asked about

**Your Contention 2(a) pleads *Delaney* affirmatively, as your own case:**

> **(a) Global Evaluation (Delaney):** The clinical governance dereliction, WHS records destruction,
> 25-day AVAC delay, and PID retaliation form a **composite, hostile course of conduct.**

That is the exact reasoning pathway Squires used to swallow your only winning finding. *Delaney* is the
Respondent's authority. A composite course lets one unreasonable incident be diluted by two reasonable
ones — which is precisely what happened to you at p. 27. The structure you want is **one mechanism with
one proven instance** (*Mahaffey*), which your Contention 2(b) already pleads correctly. Contention 2(a)
actively undercuts 2(b).

**Two further live defects in the same pleading:**

- **Contention 2 opening:** *"The Respondent bears the onus under Prizeman v Q-Comp."* Wrong twice. The
  **appellant** bears the onus — the Regulator's own SOFC ¶5 says so ("the appellant bears the onus to
  prove that there was sustained an injury"), and so does the QIRC Workers' Compensation Appeal Guide
  v2.10 Part 7.3. *Prizeman* is about the **reality** of the employer's conduct versus the worker's
  perception of it — which is a point you want, but not on onus.
- **Stressor 3(b): the "2006 Ombudsman 'Neville Report'".** I searched the Review Decision (zero hits
  for "Neville" or "Ombudsman") and the whole repository. **The only occurrences of "Neville" anywhere
  are internal labels for this pleading itself** — "the Neville pleading", "the Neville governance
  anchor". Nothing supports the existence of a 2006 Ombudsman report of that name. On the current
  record this is the second "Independent Review Office". **Do not repeat it in anything filed until you
  hold the document.**

---

## 6. ⛔ The error has propagated into your lodgement bundle

This is the part that matters most given you said "before I file anything else."

| File | What it says | Status |
|---|---|---|
| `lodgement/WC2024227_Form20_FINAL.pdf` / `.md`, **affidavit ¶41** | *"The Respondent admits the contents of that Review Decision — **both findings** — reserving only its relevance on the hearing de novo **(Admitted Fact: Form 24, Para 37)**."* | ⛔ **Worst instance — this is sworn material.** It asserts on oath that the Regulator admits the UMA finding. Row 2 says it does not. |
| `lodgement/WC2024227_Form_4_Application_Rule_64G.pdf` / `.docx` | *"the Regulator's own **Independent Review Office** has found that the 7-hour rest break constituted unreasonable management action **(Form 24, ¶37)**"* | ⛔ Both errors in one sentence. |
| `lodgement/WC2024227_Form4_FINAL.pdf` / `.md`, Item 1 | *"Para 37 (the Regulator admits the contents of its own Reviewing Officer's decision — **both** the 'unreasonable management action' finding and that … employment was a significant contributing factor …)"* | ⚠ Softer wording, same defect: ¶37's contents-admission stretched to cover the UMA finding. |
| `drafts/WC2024227_Application_v5.3_signed_master.docx` | Same sentence as the Form 4 above | ⛔ |
| `drafts/WC2024-227_Rule64G_FILING_v5R_FINAL.pdf` | *"(Response ¶34, responding to Notice ¶37)"*, framed as *"persuasive material identifying the matters in issue"* | ✅ **Closest to correct** — right row map, right characterisation, does not call it an admission. Still attaches the UMA finding to ¶37 rather than ¶2. |

**Note this in particular.** `lodgement/PRE-LODGEMENT-CHECKLIST.md` already records the fix as done:

> **¶41 — settled.** … **NO "Admitted Fact" tag** (Form 24 Resp ¶2 "does not admit" the UMA point —
> only the decision's *contents* are admitted, at Para 37; we no longer rely on that tag).

**The fix was never applied.** `WC2024227_Form20_FINAL.md` line 100 and the FINAL PDF both still carry
`(Admitted Fact: Form 24, Para 37)`. The checklist and the document disagree, and the document is what
gets filed. **Check the file, not the checklist.**

---

## 7. Corrected drafting

**Stressor 3(d) — replace the whole paragraph:**

> **(d) The Regulator's own Review Unit has already found this unreasonable.** In Review Decision 69983
> dated 24 October 2024, Ms Victoria Squires, Senior Reviewing Officer of the Respondent's Review Unit,
> found that the rostering of the shifts of 17 and 18 March 2024 *"amounted to unreasonable management
> action given that it was in direct contradiction to the award and the 8-hour agreement"* (Exhibit B1,
> p. 26), and concluded that *"factor 4 amounted to unreasonable management action"* (Exhibit B1, p. 27).
> The Respondent admits the 7-hour break itself (Form 24, Notice ¶1, admitted at Response row 1) and
> admits the same shortfall in its Statement of Facts and Contentions at ¶22(a): *"the shift was
> separated by only a 7-hour break (rather than an 8-hour break)"*. **The Appellant does not contend
> that the Review Officer's finding binds the Commission on this de novo hearing.** He relies on it as
> the considered view of the Respondent's own delegate, reached on the employer's own material.

**Affidavit ¶41 — delete the tag and the "both findings" claim:**

> **41. The Reviewing Officer's findings.** In Review Decision 69983 dated 24 October 2024, the
> Respondent's own Senior Reviewing Officer found that rostering me with the 7-hour break "amounted to
> unreasonable management action", and was "satisfied [my] employment was a significant contributing
> factor to the psychological injury". ~~The Respondent admits the contents of that Review Decision —
> both findings — reserving only its relevance on the hearing de novo (Admitted Fact: Form 24, Para 37).~~

Say nothing about admission in the affidavit. An affidavit deposes to facts; the state of the pleadings
is a submission and belongs in the outline.

**Contention 3 — recast, because "evidentiary contradiction" overstates it:**

The Regulator is not being incoherent. Its position is that the appeal is de novo and the review
decision is therefore not relevant — an orthodox position, stated at Response rows 2, 34 and 44. The
usable point is narrower and survives contact:

> The Respondent's SOFC ¶21(g) asserts that Ms Taylor's actions "were not unreasonable management
> actions in the circumstances", and ¶11 denies "any managerial hostility or unreasonable management
> action". Its own Review Unit, on the employer's own material, found otherwise as to the shifts of
> 17–18 March 2024. That finding is not binding on this hearing, but it is evidence of what a
> decision-maker applying s 32(5)(a) to this employer's own rule concluded, and the Respondent has not
> disavowed it.

**Contention 2 — two deletions:**
- Strike *"The Respondent bears the onus under Prizeman v Q-Comp."* The appellant bears it.
- Strike Contention 2(a) (*Delaney* / composite course). It hands them the dilution argument that
  already cost you the review.

---

## 8. Full audit of every "Admitted Fact" tag in the Amended Form 9A

You said you wanted to be sure before filing anything else. Since the row map had to be built anyway,
here is every tag in the pleading, each checked against the rendered Notice paragraph **and** the
mapped Response row. Only three of fifteen are clean.

| Form 9A | Tag | Notice ¶ says | Response row | Verdict |
|---|---|---|---|---|
| ¶1.2 clean baseline | Para 34 | 16 Nov 2023 entry "No psychological illness such as depression/psychosis" | **row 31** — "admits the entry is **listed** in the record, but **does not admit the accuracy** of the entry" | ⛔ **Type B, not an admitted fact.** And row 32 **denies** ¶35, asserting anxiety/ADHD history **from 26 October 2022** "missing from Exhibit A5". Do not run the clean baseline as unanswered. |
| ¶1.3 MDD diagnosis | Para 38 | Krishnaiah diagnosed MDD 13 Feb 2025 | **row 35** — "admits that the report **does say** … but **does not admit the accuracy** of the report" | ⛔ Type B |
| ¶1.3 deterioration warning | Para 39 | premature exposure → "significant deterioration" | **row 36** — admits the report says it (quotes it in full), "**does not admit the accuracy**" | ⛔ Type B |
| ¶1.4 Hawes mechanism | Para 36 | WCC "dated 1 July 2024" — mechanism "ongoing breaking of workplace rules by bosses, victimizing him" | **row 33** — admits Hawes provided a certificate so stating "but **denies that as a fact**" and **denies the date**: the certificate is **signed 8 September 2024** | ⛔ Type B **and your own Notice has the date wrong** |
| S1(b) "I took it out last week" | Para 14 | ⛔ Notice ¶14 is a **different quote**: *"I did raise my voice and asked him to please stop talking over the top of me."* | row 14 admits ¶14 | ⛔ **Quote/tag mismatch.** "I took it out last week" appears **nowhere in the Notice** — the only hit in the whole repo is `working-notes.md`. The **removal** is Notice **¶6**, admitted at row 6 (removal only, **not** the handwriting). Cite ¶6 for removal, ¶14 for the raised voice, and drop the quote until you hold its source. |
| S1(c) grievance dismissed | Para 5 | Reese email 7 Aug 2023: "there was a rostering error that was accidentally made by Chloe with regards to night shifts" | row 5 admits | ⚠ **Tag over-reaches.** ¶5 admits an acknowledgment of a rostering error. It does not admit "dismissed the complaint the same day without formal investigation", or "endorsing the unsafe rostering practices". |
| S1(e) PID | Para 20 | ESU determined PID, 24 Dec 2024 | row 20 admits | ✅ **Correct** |
| S1(f) retraction | Para 21 | 15 May 2024 Reese retraction direction, 48 hrs after the PID | row 21 — "admits the facts … **but says there was no correlation between the two events**" | ⚠ Fact admitted, **causation expressly denied**. "Immediate Reprisal" is your characterisation, not an admitted one — and see the s 32(5)(b) warning below. |
| S1(g) delegate interest | Para 18 | notified intent **11 August 2023** | row 18 — admits a **text at 5.03pm** "just putting his hand up", "but says this was **not a formal notification**" | ⚠ Partial. **Also: your pleading says "In April 2023" — your own Notice says 11 August 2023.** And ¶19 ("exceeding 9 months") is **denied** at row 19 on three grounds, while the pleading claims **13 months**. |
| S1(g) QH-POL-248 | Para 17 | Policy requires a "positive, supportive role" | row 17 — "admits **the Policy says words to that effect**" | ⚠ Qualified |
| S2(b) payroll instruction | Para 40 | 3 May 2024 Grant email: *"submit an AVAC to correct these shifts"* | **row 37** admits | ✅ Correct as to the fact — ⚠ but **"IMMEDIATELY" is not in the admitted text.** Your pleading puts it in capitals and quotation marks. Quote ¶40's actual words. |
| S2(b) 25-day delay | Para 41 | AVAC not submitted until 28 May 2024, delay of 25 days | **row 38** — admits the 28 May submission, **adds** the 21 May "waiting payroll confirmation" email | ⚠ Substantially admitted; the arithmetic (3 May → 28 May = 25) holds, but they have pleaded an explanation. Drop the word "admitted" before "25-day delay". |
| S3(a) 7-hour break | Para 1 | rostered to finish 23:00, recommence 06:00 — a break of only 7 hours | row 1 admits | ✅ **Correct. This is the anchor.** Also admitted independently at SOFC ¶22(a). |
| S3(b) rest minimum | Para 3 | FRMS and Award require a minimum of 10 hours **"or 8 hours by written agreement"** | row 3 admits | ⚠ **Overstated.** Your pleading drops the qualifier and says the Award and FRMS "mandate a minimum 10-hour rest break". Row 4 **denies** ¶4 on the strength of the 17 June 2020 8-hour agreement; SOFC ¶22(e) repeats it; and your own affidavit ¶40 now concedes you signed it. Plead the admitted version: 10 hours, or 8 by written agreement — **and 7 is short of both.** |
| S3(d) UMA finding | Para 37 | — | — | ⛔ **The subject of this note. Wrong.** |
| Part 3(c) Form 29 | Para 25 | "did not serve a Form 29 … (breach of **Rule 64E**)" | row 25 — admits no Form 29 was served on him, "but says there was **no requirement to do so pursuant to section 64D**", and **denies** any breach of 64E | ⛔ **The fact is admitted; the breach is not, and it fails.** **r 64D(1)(a)** requires service on a person *"other than a party"* — you **are** a party and are carved out. There is no service breach to plead. Your pleading also cites **"Rule 64C"**, a third rule number. The remedy is **r 64E(2)** leave to object, on grounds (e) confidential nature and (f) effect on any person, plus s 580 and relevance/prejudice. |

**One further drafting risk across the pleading.** *Hostile*, *capricious*, *reprisal*, *punishment*,
*maliciously* — these appear throughout Stressor 1 and in Contention 2(a). Motive is not an element of
s 32(5)(a); *Prizeman* makes it the reality of the employer's conduct, not anyone's perception of it.
Worse, that vocabulary opens **s 32(5)(b)** — injuries connected to the worker's *expectation or
perception* of reasonable management action. The Regulator has not pleaded 32(5)(b). Every one of those
words offers it to them from your own side, and each characterisation of a person raises your own
*Briginshaw* bar. **State the dated sequence and let it do the work.**

---

## 9. What I would do before filing anything else

1. **Fix the affidavit before you swear it.** `WC2024227_Form20_FINAL.md` line 100 / FINAL PDF ¶41 —
   delete the "Admitted Fact: Form 24, Para 37" tag and the words "both findings". This is the one
   that is about to become sworn evidence.
2. **Fix `WC2024227_Form_4_Application_Rule_64G`** (`.pdf` and `.docx`) and
   `WC2024227_Application_v5.3_signed_master.docx` — remove "Independent Review Office", remove
   "(Form 24, ¶37)", and adopt the formulation already used correctly in
   `drafts/WC2024-227_Rule64G_FILING_v5R_FINAL.pdf`.
3. **Fix `WC2024227_Form4_FINAL` Item 1** — the anchor column should read *Notice ¶1 (7-hr break,
   admitted at Response row 1); Notice ¶8 (patient-safety function, admitted)*, and should cite the
   Review Decision as **Exhibit B1 pp. 26–27**, not as a Form 24 admission.
4. **Do not file a standalone correction to the Amended 9A.** It was filed by leave; a further amended
   SOFC needs fresh leave, and a leave application puts the whole pleading under the microscope —
   including the onus error, the *Delaney* contention, the r 64C limb and the Neville Report. If you
   go for leave, **fix Part B and Part C in the same document**, all of it at once.
5. **Otherwise correct it in the Outline of Submissions**, once, in a neutral sentence: *"The Appellant
   does not rely on any admission as to the characterisation of the 17–18 March 2024 rostering. He
   relies on Exhibit B1 at pp. 26–27."* Then stop. Do not draw attention to where the error came from.
6. **Verify the Neville Report or delete it.** Currently unsupported anywhere in the record.
7. **Locate the A/B/C/D/E/F/H/I exhibit bundle as served.** Every pinpoint above — including B1 pp. 26
   and 27 — depends on it, and the bundle is not in the repository under those labels.

**Bottom line.** You lose nothing real by fixing this. The 7-hour break is admitted at Notice ¶1, at
Response row 1, and again in the Regulator's own SOFC ¶22(a). The unreasonableness finding is in the
decision under appeal, in the Respondent's own delegate's words, and you can tender it. What you had
was a citation that claimed slightly more than the record gives — and claimed it in the one place the
Regulator had drawn a line. On a *Briginshaw* record, being caught overstating an admission costs more
than the admission was ever worth.
