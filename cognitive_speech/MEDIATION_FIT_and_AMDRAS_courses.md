# Mediation: course options, fit, and a skills test from the recordings (8 Oct 2026)

Personal / self-analysis only. Course details were retrieved from the web on 8 Oct 2026 and change often:
confirm dates and fees with the provider before enrolling.

## 1. NMAS has been replaced

The National Mediator Accreditation System (NMAS) was replaced by the **Australian Mediator and Dispute
Resolution Accreditation Standards (AMDRAS)** from 1 July 2025. The Mediator Standards Board became the AMDRAS
Board on 1 July 2024. A course advertised as "NMAS" today should be checked for AMDRAS alignment.

**What AMDRAS accreditation involves** (secondary sources; confirm against the current Standards at amdras.au):
- **Training:** at least 45 hours with a Recognised Training Provider.
- **Assessment:** a separate step, including a simulated mediation of about 2–2.5 hours with no coaching.
- **Accreditation:** through a Recognised Accreditation Provider (for example Resolution Institute, or QLS for
  lawyers).
- **Levels:** Accredited, Advanced, Leading.
- **Renewal, every two years:** practice hours (20 at the Accredited level), 25 hours of professional
  development, and professional indemnity cover or statutory immunity.

## 2. Courses

| Provider | What | Format | Cost (as listed) | Dates |
|---|---|---|---|---|
| **Queensland Dispute Resolution Branch (DJAG)**, Level 1 Certificate of Training | 46 hours: 5 days in person (Brisbane city) + 1 day online. The required first step. | Brisbane + online | $2,677; concession $1,971 (full-time students, pension card holders, Jack Cranstoun scholarship applicants) | 2026 runs (Aug, Sep) have passed. Watch the page and the Branch newsletter for 2027. |
| **DRB Level 2 Certificate of Assessment** | 3 days in person; enrol within 12 months of Level 1. Prepares for the AMDRAS assessment. | Brisbane | $1,532; concession $1,205 | Aug 2026 run was fully booked. Check for 2027. |
| **College of Law**, Nationally Accredited Mediator Training (+ separate assessment) | Training online; assessment includes a video role-play and a written component | Online | $2,990 (training) | Feb/Mar 2026 runs have passed. Check for new dates. |
| **Bond University** (postgraduate subjects LAWS77-801 Mediation and Dispute Resolution Practice; LAWS77-783 Mediation) | University subjects taught on the facilitative model | Gold Coast / online | University fees | A Sep 2026 mixed-mode run of 783 was listed. Ask Bond about AMDRAS alignment. |

**Recommended route:** DRB Level 1 + Level 2. It costs about $4,209 at full price, or about $3,176 at
concession rates. It is local, government-run and AMDRAS-aligned, and the same Branch runs the State's
community mediation service: a pool of about 120 casual mediators doing court-referred and community
mediations. That service is the obvious place to get practice hours once you are accredited. Appointment as
a centre mediator is a government appointment and may involve probity checks.

## 3. The skills test from the three recordings

**Caveat on the evidence.** In every recording you were the party, not the mediator. So some core mediator
skills (open questions, summarising the other side) were never called for, and are untested rather than
weak.

| Mediator skill | Evidence | Now |
|---|---|---|
| Listening without interrupting | 0 overlaps in all three recordings (2 h+) | **Strong** |
| Tolerating silence | Interview: after you finished and 5 s+ of silence followed, you left the next move to the officers 10 times out of 15 (corrected 8 Oct 2026) | **Good** |
| Calm presence | Same pitch in every room; pressure goes into speed, not pitch; least within-phrase pitch movement in every room | **Strong** |
| Matching the other person's pace | 168 v 167 wpm (court); 159 v 155 (mention) | **Strong** |
| Precision about what was said | "Correct/Exactly" ×10 when restated accurately; "Well" to correct a wrong premise (5 of 6) | **Strong** |
| Issue mapping | The 9A, the two-page table, the fork at court (paper, not audio) | **Strong** |
| Acknowledging the other side's aim | "I understand… what you think you are trying to achieve" (mention 07:09); "I understand where you're getting at… I think I can meet most of the way" (32:02) | **Good** |
| Showing you have heard (receipts) | 35 stand-alone "Okay / Yes / Correct" at the mention | **Good** |
| Separating position from interest | "It's not what's inside those complaints… it's that they happen to me" (mention 08:36) | **Good** |
| Neutral language | 7 loaded words at court → 0 at the mention | **Good, under discipline** |
| Summarising the other person's view | 0 at the mention; 1 at court ("I mean you're saying, so the law is…") | Untested |
| Open questions | 1 genuine question at court | Untested |
| Warmth in the voice | Narrow pitch range reads as composed, not warm | Needs deliberate work |
| Short written agreements | Your paper reads "heavy-going" | Needs work |
| Starting from neutral | "they", "targeted", "dishonesty" as a party | **Developing: the main work** |

**Tally:** 6 strong, 4 good, 2 untested, 3 to build.

## 3A. Listening: do you follow, or think on your own point? (`listening.py`, `listening_output.txt`)

Each content word in an answer is classed as taken from the question just asked (FOLLOW), carried from your
own last three turns but not in the question (OWN), or new. Following is compared with a shuffled baseline:
the same answer paired with a random other question.

| | Your answer words from the question | From your own earlier point | Answers reusing a word of the question |
|---|---|---|---|
| Mention: you answering Dwyer (53 answers) | **17%** (chance 4%: ×4.3) | **2%** | 51% |
| Mention: Dwyer answering you (88) | 7% (chance 1%) | 22% | 25% |
| Court: you answering the Magistrate (14) | 11% (chance 2%: ×4.4) | 12% | 14%* |
| Court: the Magistrate answering you (15) | 11% (chance 2%) | 5% | 27% |
| Interview (topic tags, `threads.py`) | Your topics carried from your own earlier talk: 71% (officers 72%) | | |

\*Many of her prompts had no content words ("Which bit?", "He just said there was").

**Who adopted whose words.** Lexical entrainment is the shared vocabulary speakers settle on (Brennan & Clark
1996).
- *Mention:* Dwyer adopted 15 of the 23 key terms you introduced (65%), including "filter", "correspondence",
  "constructive" and "access". You adopted 86 of his 430 (20%), including "directive", "unassessed",
  "document" and "union".
- *Court:* the Magistrate adopted your words "told" and "destroyed", which became the hinge of the hearing
  ("he was told… it was destroyed"; "told to the contrary"). The prosecutor took up "destroyed" too.

**Verdict.** You follow: you take up the question's words at about four times chance. You also keep your own
thread alive in parallel, and the room decides which wins:
- **Structured hearing (mention):** you follow. Only 2% of your answer words were your own carried-over point,
  against the Commissioner's 22%.
- **Your account (interview):** you lead, as the officers did.
- **A point close to you (court, the missing material):** your own thread runs alongside, at 12% against the
  Magistrate's 5%.

**Your particular way of following.** You follow the purpose of a question more than its wording.
- "Are we going ahead today?" → your adjournment history.
- "Is it in the form of an email?" → why you no longer had it.

That is listening for intent, which is a mediator's core skill. On closed questions, though, it reads as not
answering ("Yes or no?"). Mediators need both:
- **Looping:** reflect the person's own words back until they say "that's right" (Friedman & Himmelstein 2008).
- **Your advantage:** your exactness about when a restatement is accurate ("Correct" / "Exactly") is the
  standard a good loop has to meet.

## 3B. Against the population, and against other new mediators

**Against the general population (on the measures available):**
- **Stress does not reach your pitch.** In most people it rises (Giddens et al. 2013 review).
- **You do not take a wrong premise on board.** You corrected 5 of 6 with "Well…". Many people accept part
  of what a leading question assumes when questioned by someone in authority (Gudjonsson's suggestibility
  research).
- **You tolerate silence:** after you finished speaking and a silence of 5 s or more followed, you left the next move to the officers 10 times out of 15 (you carried on yourself 5); when they finished and a long silence followed, they carried on themselves 16 times out of 21. (Corrected 8 Oct 2026: the earlier "officers 26, you 10" counted officers resuming after their own pauses.)
- **You answer at conversational speed in formal rooms:** 0.26–0.32 s, against the officers' 1.22 s.
- **You hold and return to more threads** than reference speakers: 3.4 switches and 2.1 returns per 100
  words, against 1.6–2.0 and 0.4–1.0 in recorded conversations between strangers.
- **You change your style from feedback** within months (tempo, loaded words, yes-first).

**Against other new mediators.** Studies of successful mediators rank three things:
1. **Rapport:** empathy, honesty, trustworthiness.
2. **Process skills:** patience, persistence, listening.
3. **Substantive expertise.**

(Goldberg 2005; Goldberg & Shaw 2007.)
- **Your edge:** honesty and calibration; persistence; patience (no interruptions, comfort with silence);
  measured listening; expertise in health workplaces, rostering, industrial relations, workers' compensation
  and court process; and having been the less powerful party.
- **At the start you would be average or below on:** visible warmth (empathy put into words and voice), open
  questions and summaries (untested), short writing, and starting from neutral.

## 4. Fit

- **Strong fit:** workplace, industrial, administrative and community disputes, which are document-heavy and
  rights-adjacent. Your structure, precision and composure carry there.
- **Watch:** the facilitative model taught in most courses keeps the mediator out of the merits (Riskin's
  grid: facilitative v evaluative). Your natural style is evaluative and issue-focused. The training will
  ask you to hold back your strongest tool, structuring and testing facts, and to hand the problem back to
  the parties. That is exactly the habit you most need for any neutral role.
- **Not first:** family dispute resolution. It needs a separate accreditation (FDRP) and sits close to your
  own experience.
- **Where you work best overall:** neutral fact-finding (investigation, conciliation with a rights edge,
  tribunal work). Mediation is a strong fit and the best training ground for the neutral default those roles
  require.

## 5. How good

- **With AMDRAS training and about two years of supervised practice:** a strong mediator in structured
  disputes, in my judgement in the upper third of newly accredited mediators.
- **What sets the ceiling:** the untested skills (questions, summaries, warmth) and starting from neutral.
  Neutrality in mediation is performed in talk turn by turn, and it is trainable (Jacobs 2002).
- This is a judgement from the evidence above, not a measurement.
