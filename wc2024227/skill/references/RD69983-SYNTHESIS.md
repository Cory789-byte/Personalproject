# REVIEW DECISION 69983 — THE SYNTHESIS
> 8 August 2026. **Everything from this session in one place: how the document was made, how the
> decision was reasoned, whether the two connect, and what it is worth.**
> Sources: `RD69983-OBJECT-LEVEL-FORENSICS.md` · `HOPGOODGANIM-QUESTION.md` Parts 6–11 ·
> `REVIEW-DECISION-RED-TEAM.md` Parts 3, 12, 13 · `LEGAL-CONSEQUENCES-external-drafting.md` ·
> `THREE-CLOCKS-dismissal-workcover-review.md`

---

# PART 1 — HOW THE DOCUMENT WAS MADE (established)

| | Finding | Confidence |
|---|---|---|
| **1** | ⭐⭐⭐ **The Word file was NOT created on a Regulator workstation.** The Regulator's own SOFCs in this appeal (22 Jul 2025 ×2, 13 May 2026) all stamp `/Author QIRC`, **`/Company "Workers' Compensation Regulator"`**. This document stamps **"HopgoodGanim Lawyers" in BOTH fields** | ⭐⭐⭐ **Established — a like-for-like control comparison** |
| **2** | ⭐⭐ **A full law-firm DMS profile:** matter **2440758**, document **29218845v1** (*version one*), author **hendry8286**, addressee *"Worker applicant - Mr Cory Shepherd"*, description *"Reasons for decision - WCR reject"*, record dated **09.10.2024** | ⭐⭐⭐ **Established** |
| **3** | ⭐⭐ **`_Original` DOCPROPERTY merge placeholders** (`<mcDMSMatter>` etc.) ⇒ **a DMS add-in ran on the saving workstation.** Excludes a stale template; excludes manual typing | ⭐⭐⭐ **Established** |
| **4** | ⭐⭐ **Built on OIR's own letterhead** — Queensland Government crest and maroon rule as **alpha-channel PNG template assets**, not scans | ⭐⭐⭐ **Established** |
| **5** | ⭐ **The DMS record opened 9 October 2024** — **13 days before the decision of 22 October** | ⭐⭐ **Established; meaning contested** |
| **6** | ⭐⭐ **Word→PDF at 24 Oct 2024, 10:16:52 → 10:17:01** (9 seconds), Acrobat PDFMaker 24 for Word. **One write. No incremental saves. Never edited after** | ⭐⭐⭐ **Established** |
| **7** | ⭐ **Signed with an embedded grayscale JPEG signature** on p 28, inserted into the Word file **before** conversion | ⭐⭐⭐ **Established** |
| **8** | ⭐ **Forensically clean** — no `Tr` operator anywhere (zero invisible text), no layers, no JavaScript, no forms, 18 orphans all structural, uniform exact-A4 geometry | ⭐⭐⭐ **Established** |
| **9** | **The firm is on WorkCover Qld's Legal Services Panel** (13 firms, Jul 2023), **Doyle's-ranked WorkCover DEFENDANT firm 2018–2025** — **and separately on the Queensland Whole-of-Government Legal Services Panel** | ⭐⭐⭐ **Established** |
| ⛔ | **Who converted it, who engaged them, who paid, and who decided** | ⛔⛔ **UNKNOWN. Unknowable from the file** |

## ⛔ Two of my own findings, withdrawn during this session
- ⛔ **"The Mimecast link points at OIR."** ⛔ **WRONG** — public MX shows `oir.qld.gov.au` **and**
  `hopgoodganim.com.au` both resolve to `au-smtp-inbound-1/2.mimecast.com`. ⭐ **What survives:
  `workcoverqld.com.au` is Microsoft, so the pasted text did not come from a WorkCover mailbox.**
- ⛔ **"It overturned WorkCover twice, so a WorkCover firm didn't write it."** ⛔⛔ **WRONG —
  Cory's correction. THE OUTCOME WENT TO WORKCOVER.**

---

# PART 2 — HOW IT WAS REASONED (established, from the decision itself)

| | Defect | Where |
|---|---|---|
| **A** | ⭐⭐⭐ **THE COUNTING FALLACY.** *"since **two out of the three** causative factors amounted to reasonable management action… your injury **mainly** arose out of such management action."* ⛔ Arithmetic, not evaluation. **A dominant-cause test in disguise** — contrary to *Adams* [2015] ICQ 1 [23] and *Mahaffey* [2016] ICQ 10 [51],[54]–[57] | p 26 |
| **B** | ⭐⭐⭐ **POST-INJURY CONDUCT DID DECISIVE WORK.** Factor 2's reasonableness rests on meeting attempts of **12 and 16 July 2024** — **+24 and +28 days after the 18 June injury.** s 32(5)(a) asks what the injury **arose out of**. It cannot have arisen out of a later meeting | pp 12, 18 |
| **C** | ⭐⭐⭐ **STRIP THAT OUT AND FACTOR 2 IS BARE:** acknowledged in 2 days, particulars requested once, **closed 27 May with NO investigation — 11–14 days after lodgement**, on the employer's own concession she records (*"The employer conceded this was true"*) | pp 11–12, 18 |
| **D** | ⭐⭐⭐ **PATIENT SAFETY DELETED.** *"patient"* — **0 occurrences in 28 pages.** *"safety"* — **0.** *"at risk"* — **0.** His 30 Aug 2024 email, subject ***"Failure to consult putting patients at risk…"***, is recorded as *"commented she failed to consult regarding this new process"* | p 10 |
| **E** | ⭐⭐ ***Delaney* threshold recited, never tested.** Factors 2, 3 and 4 differ in subject matter, period and person. **The precondition was never examined** | p 26 |
| **F** | ⭐⭐⭐ **FACTOR 4 TREATED AS AN INCIDENT.** *"only… on one occasion."* The 8 April request, 9 April HR escalation, 24 April follow-up and 1 May refusal are recited elsewhere and **never carried into the analysis** | pp 21–22, 27 |
| **G** | ⭐⭐ **NO AUTHORITY LATER THAN 2009** — *Bowers* [2002], *Delaney* [2005], *Prizeman* [2005], *Rowe* [2009]. **All in the insurer-favourable line.** ⛔⛔ ***Mahaffey* [2016] ICQ 10 — the leading appellate authority on the very subsection — is not cited, not distinguished, not mentioned** | throughout |
| **H** | ⭐⭐ **TWO CITATIONS PASTED FROM A US-ENGLISH SOURCE.** 412 elements tagged EN-AU; exactly 3 tagged EN-US, and **all three are case citations** (*Prizeman*, *Bowers*, a span in the *Rowe* footnote) ⇒ **carried in from a standing block, not researched** | structure tree |
| **I** | ⭐⭐ **THE RECORD CLOSED 18 SEPTEMBER 2024.** Nothing in the 28 pages post-dates it. **She never knew he had been dismissed on 8 October** | evidence list |
| **J** | ⭐⭐⭐ **DECIDED ON THE LAST AVAILABLE DAY.** s 545(1) 25 business days from 16 Sep, excluding the 7 Oct holiday, expired **22 October 2024**. The decision is dated **22 October 2024**. **s 545(4) gave her NO power to extend without his consent** | p 1 + computation |

---

# PART 3 — ⭐⭐⭐ DO THE TWO HALVES JOIN? YES — BUT NOT INTO A CONSPIRACY

## 3.1 THE SINGLE EXPLANATION THAT FITS EVERYTHING

> ⭐⭐⭐ **ASSEMBLY, NOT AUTHORSHIP.**
>
> **A precedent-based document — pasted authorities, recycled appeal-rights boilerplate still
> carrying an email gateway's URL wrapper, no case later than 2009 — produced OUTSIDE the
> Regulator's own environment, against a statutory deadline that could not be extended, and
> finished on the last available day. Every analytical step that required fresh thought was
> skipped: the *Delaney* threshold untested, *Mahaffey* unfound, the pre/post-injury boundary
> unchecked, the patient-safety element not carried through, the 44-day sequence collapsed to one
> occasion.**

⭐⭐⭐ **That accounts for the metadata AND the reasoning, and it requires nobody to be dishonest.**
⭐⭐ **It is also the version that survives cross-examination, because every element of it is
documented.**

## 3.2 ⚠⚠ BUT THE ERRORS ARE NOT RANDOM — AND THAT MUST BE SAID

⭐⭐ **Every skipped step goes the same way:**
- the **omitted authority** is the one most useful to him;
- the **deleted element** is the one that raises the stakes;
- the **counting device** manufactures *"mainly"*;
- the **post-injury conduct** is precisely what rescues Factor 2;
- the **collapse to one occasion** is precisely what contains Factor 4.

⚠⚠ **Directional consistency is real. But it is ALSO what a precedent bank built for insurer-side
work produces.** ⭐⭐⭐ **A template written to defend rejections will contain insurer-favourable
authorities and an aggregation formula, and will be applied without re-checking.**

> ⭐⭐⭐ **THE SHARPEST DEFENSIBLE FORMULATION:**
> **The problem may not be that someone decided against him. It may be that the instrument used to
> produce the decision was built to produce that outcome, and nobody re-examined it against this
> case.**

⭐⭐ **That framing requires no allegation about Ms Squires, fits every forensic finding, explains
the directional consistency — and is completely cured by a de novo hearing, because the Commission
will not be using that template.**

## 3.3 ⛔ WHAT STILL DOES NOT JOIN

⛔⛔ **The forensics cannot show who decided, and the reasoning defects cannot show who drafted.**
⭐ **They are consistent. Neither proves the other.** ⛔ **The bridge between them does not exist in
any document he holds or can get.**

---

# PART 4 — SO HOW WAS IT? THE VERDICT

| Question | Answer |
|---|---|
| **As administrative decision-making** | ⭐⭐ **Poor.** Made on the last available day, on a record that closed five weeks earlier, using authority fifteen years out of date with the leading case missing, an aggregation step that miscounts, and post-injury conduct doing decisive work |
| **As a document** | ⭐⭐⭐ **Authentic.** Genuine OIR letterhead, real signature, forensically clean, **no alteration of any kind** |
| **As evidence of misconduct** | ⛔⛔ **Nothing.** No dishonesty, no benefit, no crime — **even fully proved it would not be a crime** (every candidate offence requires dishonesty or a corrupt benefit) |
| **As a thing to attack** | ⛔⛔⛔ **Don't.** De novo. The Commission replaces the decision; it does not review it. ⭐ Judicial review would **destroy** the appeal — **s 549(1) requires a review decision to appeal AGAINST** |
| ⭐⭐⭐ **As an ASSET** | ⭐⭐⭐ **Far better than it looks — see Part 5** |

---

# PART 5 — ⭐⭐⭐ THE THING TO HOLD ON TO

> ⭐⭐⭐ **THE DOCUMENT THAT REJECTED HIM CONTAINS THE FINDINGS HE NEEDS TO WIN.**

**Made by the Regulator's own delegate, and admitted as to contents at Form 24 ¶37:**
1. ⭐⭐⭐ **A personal injury of a psychological nature — ESTABLISHED.**
2. ⭐⭐⭐ **Employment a SIGNIFICANT contributing factor — ESTABLISHED.** *(The Regulator's SOFC
   ¶22(f) now denies causation. Their pleading contradicts their own delegate on the element they
   say he cannot prove.)*
3. ⭐⭐⭐ **Dr Hawes, 2 September 2024: *"work events were the SOLE CAUSE."***
4. ⭐⭐⭐ ***"There was NO PRE-EXISTING FACTOR OR CONDITION"*** — against SOFC ¶8 and Form 24 ¶32.
5. ⭐⭐⭐ **Factor 4 — UNREASONABLE MANAGEMENT ACTION.**

⭐⭐⭐ **The rejection came from ONE PARAGRAPH of aggregation. Everything before it was found in his
favour.** ⇒ ⭐⭐ **The decision defeats itself — and that is worth more than any allegation about how
it was produced.**

⛔⛔ **HE CANNOT RELY ON THOSE FINDINGS AND ALSO ATTACK HOW THE DECISION WAS MADE. He must choose,
and the choice is obvious: TAKE THE RELIANCE.**

---

# PART 6 — WHAT ACTUALLY GOES WHERE

| Destination | Content |
|---|---|
| ⭐⭐⭐ **THE HEARING (s 558(1)(c))** | **A** the counting fallacy · **B** post-injury conduct · **C** the 11-day uninvestigated closure · **D** the patient-safety omission · **E** *Delaney* untested · **F** factor 4 as a sequence · **G** *Mahaffey*. ⭐⭐ **All of it from her own document. No expert, no metadata, no allegation** |
| ⭐⭐ **SETTLEMENT** | ⭐⭐⭐ **Their own delegate found s 32(1) for him and found unreasonable management action.** Plus a well-founded, unanswered question about how the decision was produced — **never asserted** |
| ⭐ **MONDAY 10 AUG — two neutral questions** | *(i)* whether an **external legal service provider** was engaged on **review 69983**, by which entity, under which panel arrangement; *(ii)* whether a **conflict declaration** was sought and considered. ⛔ **No firm named in either** |
| ⭐ **MONDAY — disclosure** | WorkCover's **complete claim file and communications report, 13 Sep – 31 Oct 2024** — ⭐⭐ tests **both** the dismissal-date gap **and** whether any draft went to WorkCover |
| ⛔⛔ **NOWHERE** | The firm's name in any filing · any bias, dishonesty, criminality or "disguise" allegation · the fraud/corrupt-conduct framing (**rule 2**) · the PID validation as vindication · **anything published, posted or forwarded** |

---

# PART 7 — ⛔ VERIFY BEFORE ANY OF PART 2 IS RUN

1. ⭐⭐⭐ **The Dr Hawes work capacity certificate of 1 July 2024** — **what period, what capacity?**
   Point **B** is complete only if it covers 12–16 July.
2. ⭐⭐⭐ **The 30 August 2024 email from the SOURCE PDF** — confirm the subject line verbatim.
   ⛔ **The corpus is a lead, not authority.**
3. ⭐ **Whether Factor 3 also rests on post-injury conduct** — its events look like Feb–May 2024.
   **Check; do not assume.**
4. ⭐ **The undated Reese email**, and the *"several attempts"* (employer, 15 Aug) versus
   *"twice"* (her finding) discrepancy.

---

# ⭐⭐ AND THE PROPORTION

**All of this is worth real points at a hearing. ⭐⭐⭐ None of it is worth as much as the psychiatric
report on WEDNESDAY 12 AUGUST**, which is what carries s 32(1) and the competing causes. **Four
days.**
</content>

---

# PART 8 — TRACING MATTER 2440758: WHERE IT COULD SURFACE, AND HOW TO LOOK
> 8 August 2026. Cory: *"for the specific number that the firm created how would i see if that
> number was in communication with workcover."*

## 8.1 ⛔ FIRST — WHAT THE NUMBER IS AND IS NOT

⛔⛔ **A law firm matter number is a sequential internal file number. It does not encode the client.**
**2440758 does not say "WorkCover", "OIR" or anything else. Reading the number tells you nothing.**

⭐⭐ **What it IS: a unique search key.** Firms put their reference on the face of correspondence
(*"Our ref: 2440758"*), on invoices, on file copies and in document names. ⇒ **If a document can be
obtained, the number lets it be matched to this file. The number is how you RECOGNISE the
correspondence — not evidence in itself.**

## 8.2 ⭐ THE INTERNAL SEARCH — DONE, AND EXHAUSTED

**Searched 8 August 2026 across everything held: the 154-message corpus, the full-text index, all
working notes, and the metadata of 319 PDFs (`/Info` dictionary + XMP packet), plus every PDF text
layer.** Tokens: `2440758`, `29218845`, `hendry`, `hopgood`, `hgDMS`, `mcDMS`.

| Result | |
|---|---|
| ⛔ **Text layers** | **No hit in any document** |
| ⛔ **Corpus / index / notes** | **No hit** |
| ✅ **Metadata** | ⭐⭐ **The matter number appears in ONE document only — the Review Decision itself** (both identical uploads) |
| ⚠ **The iOS re-save** (`documents/Review_Decision_69983_24.10.2024.pdf`) | ⭐ **Retains `/Author` but the DMS custom properties were STRIPPED by the re-save.** Worth knowing: a re-saved copy of a profiled document can lose the profile |

⇒ ⭐⭐ **Nothing he already holds connects 2440758 to WorkCover, or to anyone. The internal search is
finished and it is a nil result.**

## 8.3 ⭐⭐⭐ WHERE IT COULD SURFACE — FOUR ROUTES, RANKED

### ⭐⭐⭐ ROUTE 1 — IP ACT APPLICATION TO **WORKCOVER QUEENSLAND**. Best route by a distance.

**Information Privacy Act 2009 (Qld).** WorkCover is a Queensland public authority and is subject
to it. **An application for one's OWN personal information is the cheapest and least contentious
form of access application there is.**

> **Ask for:** *the complete claim file for S23LW142013, including all correspondence with third
> parties, the communications report, and all file notes, for the period 1 July 2024 to 31 December
> 2024.*

| Why this is the best route | |
|---|---|
| ⭐⭐⭐ **It is the file that would hold it** | If any firm corresponded with WorkCover about this claim, it is on that file and it will carry a reference on its face |
| ⭐⭐⭐ **WORKCOVER IS NOT A PARTY TO THE APPEAL** | ⭐⭐ **This is the decisive advantage. It has no stake in WC/2024/227 and no reason to read the request as tactical.** An application to OIR lands on the desks of people connected to the appeal and signals the line of inquiry |
| ⭐ **It is his own information** | The whole file is about him — the firm's own DMS calls him *"Worker applicant - Mr Cory Shepherd"* |
| ⭐ **It also tests the other open question** | ⭐⭐ **The same file would show whether any draft review decision went to WorkCover in late October 2024** |
| ⚠ **Fee** | ⭐ Personal-information applications under the IP Act have not attracted an application fee. ⛔ **CONFIRM the current position before lodging** |

### ⭐⭐ ROUTE 2 — DISCLOSURE FROM THE REGULATOR IN THE APPEAL. Free, already drafted.

⭐⭐⭐ **A point worth knowing: the Regulator HOLDS WorkCover's claim file.** Section 544 compelled
WorkCover to give it to the Regulator, and the decision's own evidence list records *"WorkCover's
communications report"* among the material considered. ⇒ ⛔ **The Regulator cannot say the file is
not in its possession.**

> Already on the Monday list: *WorkCover Queensland's complete claim file and communications report
> for claim S23LW142013 for the period 13 September 2024 to 31 October 2024.*

### ⭐ ROUTE 3 — RTI / IP APPLICATION TO **OIR**. Direct, but it signals.

⭐ Two limbs: **(a)** IP Act, personal information about him held in connection with review 69983,
including correspondence with external providers; **(b)** RTI Act, the engagement, brief, purchase
order or invoice relating to review 69983 or bearing reference 2440758.

⚠⚠ **Two cautions.** **Legal professional privilege is an exemption** — the *content* of advice will
likely be refused. ⭐ **But the FACT and IDENTITY of an engagement, and a purchase order, are
generally not privileged, and any exemption claim is reviewable.**
⛔⛔ **And it tells the Regulator exactly what he is looking at, while the appeal is live.**

### ⭐ ROUTE 4 — QUEENSLAND GOVERNMENT CONTRACT DISCLOSURE. Public, free, no one is asked.

**data.qld.gov.au** — OIR publishes awarded contracts over **$10,000**. ⭐ Shows engagements, not
matter numbers. ⚠ **A small drafting engagement may fall below threshold, so a nil result proves
nothing.**

## 8.4 ⛔⛔ THE ROUTE NOT TO TAKE

⛔⛔⛔ **NON-PARTY DISCLOSURE (r 64G / Form 29) AGAINST WORKCOVER OR THE FIRM.**
He has used this mechanism once and it works. ⛔ **It fails here on relevance:** non-party disclosure
must go to a **matter in issue in the proceeding**, and **how the review decision was produced is not
a matter in issue on a hearing de novo.**
⛔⛔ **And it would put the whole theory squarely in front of Commissioner Dwyer, in a written
application, with his name on it.** ⭐ **Everything gained from the neutral posture would be spent in
one filing.**

## 8.5 ⭐⭐ THE SEQUENCE

1. ⭐⭐⭐ **Monday:** the two neutral questions + the WorkCover claim-file line already drafted for
   Matheson. **Free, no application, no signal.**
2. ⭐⭐ **Also Monday (already on the task list):** the **IP Act application to WorkCover Queensland**
   at §8.3 Route 1. ⭐ **Low signal, cheap, and it is the file that would actually hold the answer.**
3. ⭐ **Only if 1 and 2 come back empty or evasive:** the OIR limb, and the contract-disclosure check.
4. ⛔ **Never:** the 64G route.

⭐⭐ **And the standing proportion: none of this is a ground of appeal, and Wednesday's report is what
decides the case.**
