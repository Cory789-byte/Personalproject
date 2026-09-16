# COGNITIVE SCRATCHPAD — C. SHEPHERD

**Accumulated from a single working session, 16 September 2026.**

> **Status and scope.** This is self-analysis. It is **not case material**, not evidence,
> not a filing, and not a clinical or forensic psychological assessment. It must never be
> served, tendered, cited, or attached to anything in WC/2024/227, the QPS matters, QHRC
> EDR19098, or any other proceeding.
>
> It also **crosses both tracks** (the QIRC appeal and the QPS/DV matter), which the matter
> discipline rules forbid on case paper. That is permissible here only because this document
> is about the person, not about either matter. Keep it out of both.
>
> Every measurement below is tied to a named timestamp in a named transcript. Where a claim
> rests on recollection rather than record, it is marked.

---

## 1. Sources

| Source | Status |
|---|---|
| QIRC mention, WC/2024/227, 7 Aug 2026, diarised with prosody | Whisper large-v3, 1,068 segments, mean segment log-prob −0.180. **Speaker labels inferred, 90% on hand-checked anchors.** Long turns reliable; short interjections are the weak point. Recording begins mid-sentence. |
| BICKERY body-worn stitched interview, 24 Feb 2025 | Rebuilt from SPK.clean diarisation. Supersedes the GPU stitched version. Spoken clock says 5:48am start; the computed AEST column says 17:48 and the file itself flags it for confirmation against the burnt-in clock. |
| `GPU_VALIDATION_BICKERY_interview.transcript.json` | Superseded by the above. Not read. |
| Repos: `Personalproject`, `mail-tools`, `01-appeal`, `wc-extractor` | Read. Neither transcript is stored in any of them. |
| 13 March 2026 conference before Dwyer | **Unrecorded. Recollection only.** Conferences are private and not transcribed. |

---

## 2. Measured — free narrative (QPS interview, 07:05 to 11:31)

Prompted at 06:46. Began at 07:05. **Nineteen seconds of composition before speaking.**

| Measure | Value |
|---|---|
| Segments | **61** |
| Speech time | ~242 s (266 s window) |
| Mean segment | **4.0 s** |
| Words | ~700 |
| Rate | 155 to 175 wpm |
| Threads opened | ~20 |
| New thread every | ~14 s |
| Segments per thread | ~3.1 |
| Navigation markers | 2 |
| Structural pauses | 0 |
| Interruptions survived | 1, at 07:51; resumed on thread at 08:01 |

**Topology:** paratactic. Connectives are *and, so, but, I mean*. Subordination present but shallow,
mostly one level (*because, if, even though*). Deepest construction observed is two levels.

**Ring closure:** opens on authority to be there, closes on whether theft was legally possible.

**Content:** lawful authority by lease; rent and utilities paid; prior verification with the RTA and
building management; Form 13 requires both signatures; no intent regarding the dog; independent
witness with footage; his own call to police; duress on signing; the 1 December incident.
Cross-checked against `source_documents/CHARGES_SUMMARY.md`, these are substantially the facts
that defeat the elements.

**Response latency:**
- 8 s of silence after he stopped.
- 11:39, a meta-sentence: "I'll start off with sort of a few things that I want to cover."
- 11:47, first question, on one thread of twenty: "How long have you had the dog for?"
- **Real uptake ~12 hours** — Davies recites the same facts back at the mother's house that evening.
- **Disposal ~28 hours** — Magistrate Brunello strikes out the order the next morning.

---

## 3. Measured — Dwyer's opening (00:00 to 07:09)

| Measure | Value |
|---|---|
| Speech time | ≥429 s (starts mid-sentence, so a floor) |
| Segments | ~123 at pipeline rate (846 segs / 2,949 s = 3.49 s); 67 as rendered |
| Mean segment | **3.5 s** |
| Words | ~820 |
| Rate | ~115 wpm |
| Rate range | **0.8 to 5.1 w/s** |
| Threads | ~17 |
| New thread every | ~25 s |
| Segments per thread | ~7 |
| Navigation markers | ~20, **1 per 3.4 segments** |
| Structural pauses | 1 (3.1 s), immediately before pivoting to the application |
| Threads parked and reopened | 1 (the Form 29, parked at ~05:00, reopened at 61:53 using the same word) |

**Topology:** hypotactic, 2 to 3 levels. Narrates his own stack aloud: *what I mean by that, to that
end, first principles, I'm going to park, one step further, that's just to set the scene.*

**Rate discipline is inverted relative to Shepherd.** Slow markers (0.8, 1.1 w/s) land on the thesis
and the pivot. Fast markers (5.0, 5.1) land on throat-clearing.

**Shepherd's response:** immediate inline answer to the comprehension check, then 8.4 s at 07:09
before being cut off. Compressed all ~17 threads into one clause: *"I understand, I think I
understand, what you think you are trying to achieve."* Confirmed real by the following 44 minutes
of correct item tracking.

---

## 4. Measured — Shepherd in the mention

| Measure | Value |
|---|---|
| Segments | 219 |
| Speech time | 466 s |
| Share of floor | **13.6%** (Dwyer 86.2%) |
| Turn changes | 202 |
| Mean segment | **2.1 s** |
| Longest runs | 45 s (13:28), 32 s (23:40), 28 s (29:17) |
| Rate on anchor facts | 8.3 and 9.7 w/s |
| Slow markers | 1 in the entire hearing (0.9 w/s) |

**The headline number.** One free narrative to two police officers (274 s window) is **59% as long
as everything he said across the entire 64-minute mention**.

**Segment length by condition:** free 4.0 s · Dwyer 3.5 s · interrupted 2.1 s.
**When he has the floor his segments are longer than the Commissioner's.**

---

## 5. The four comparators he runs natively

Present across both transcripts and all four repos.

1. **Symmetry.** What was done to me against a like person in like circumstances. *"I get decisions
   too." "One person can't make a decision."* In the appeal: Reese's business hours, Taylor's
   comparable email, the pay disparity. This is the native structure of a disparate-treatment claim.
2. **Rule against conduct.** Behaviour checked against a written instrument. Lease, RTA, Form 13,
   Award, QH-POL-248, fatigue policy, EB11. Never "was it fair" — always "what does it say and did
   they follow it."
3. **Stated against done.** Hunts the gap between a party's words and acts. Found the health
   service's own self-contradiction between Item 3(c) and Item 5 unaided.
4. **Process against outcome.** Treats procedural failure as a wrong in itself. PID determined then
   unactioned; grievance dismissed same-day without investigation.

**The missing fifth.** Materiality. He detects the breach accurately and weights it at full value
regardless of legal consequence. Dwyer's entire opening was about this: non-compliance *"happens
every single day in every single workplace... it's only a problem if somebody gets sacked or
somebody gets killed."* He can run the filter deliberately on paper — `wc2024227/FULL-PICTURE.md`
ranks stressors and names the soft spot — but not live, at speed, before material leaves him.
**That filter is most of what legal training installs.**

---

## 6. Cognitive framing (frameworks, not findings)

- **Suggestibility split.** Low yield and low shift under conditions that predict maximum
  suggestibility (custody, ~3 h sleep, caution, no lawyer), combined with high evidential updating
  five months later in a neutral room. These normally correlate. Split in opposite directions is
  uncommon.
- **Why it is not just intelligence.** Stanovich's finding that myside bias is largely independent
  of cognitive ability means conceding against interest is a **separable disposition**, not a proxy
  for brightness. It is why it stands out on its own.
- **Breadth.** Consistent with reduced latent inhibition. Genuinely double-edged in the literature.
- **Executive pattern.** Strong long-range retrieval, weak online monitoring and global
  self-monitoring under load. ADHD is pleaded by the Regulator at SOFC ¶8; lisdexamfetamine appears
  on the 3 July 2026 capability checklist.
- **Retention.** The 12-hour verbatim recall by a hostile listener is largely a *format* effect —
  concrete, first-person, causally chained, sensory. What is his is producing that format natively
  at 5:48am in custody with no preparation.
- **Nothing here is measured.** The Mind & Memory cognitive assessment booked 5 June 2026 has **no
  result anywhere in the repos**. That report is where the real answer lives.

---

## 7. What leaked under interruption

Four narrative fragments got out in the mention before being stopped. All four come from the same
thread family: clinical governance, directives, patient safety, misrouted emergency calls. Stressor 1(a).

| Time | Content | How it ended |
|---|---|---|
| 13:28 | access and login data, ~45 s | *"I don't want you to do that now."* |
| 23:40 | the filters explanation, ~32 s, uninterrupted | moved to line 10 |
| 27:28 | *"when it's in a patient safety environment"* | **"you can raise that"** |
| 29:17 | misrouted numbers, cardiac arrest, respiratory distress, ~28 s | 5.7 s silence, then *"I'm concerned at the direction this is going in"* |

**Every interruption was a deferral, not a rejection.** Squeeze him in any direction and what
surfaces is patient care. Same in the police interview at 29:17. Same in the March conference when
asked about returning to nursing.

**The thing that never landed.** At 08:36 and again at 23:40 he said he wanted **the count, not the
documents**. *"I wouldn't even need to read them." "I basically just want the count."* For a
course-of-conduct case the number is the fact in issue and the content is not, and a count answers
the expense objection before it is made. Dwyer spent the morning believing he wanted boxes of paper.
The narrowest, most defensible version of the disclosure request was on tape from minute eight.

---

## 8. The case as actually pleaded

- **Three stressors**, subcategorised. Not fourteen. Fourteen is the count of particulars Dwyer walked.
- **One unreasonable stressor suffices** — *Hochen*, adopted in *Mahaffey* [2016] ICQ 10. Not
  arithmetical, not cured by outnumbering (*Adams*).
- **The strongest is already admitted and already found unreasonable** — the seven-hour break,
  17–18 March 2024, Form 24 Response ¶1, plus the Review Officer's finding.
- **What Dwyer actually did** was a possession audit, item by item, running the r 64B(2) test: can
  this be proved another reasonably simple and inexpensive way. Answers logged as *"tick," "done,"
  "you've got the documents you need for those stressors," "awesome."* Not a merits assessment. He
  said so: *"I'm not going to get into the facts now because I'm not hearing the matter."*
- **Residual gap identified:** the directive emails. *"You might be on to something there."*
- **Outcome:** four-week stand-down, no ruling, no costs, no sideshow hearing.

---

## 9. The 13 March 2026 conference — recollection only, not on record

Two options offered in sequence: **law first, nursing second** — the harder and less obvious one
first, the fallback only after the first was declined. His answer to law was *"I don't know about
that."* His answer to nursing was about how staff treat each other and how they treat patients.

His mother attended. Ten minutes late. Spoke perhaps twice, five words, and used them to ask that
his medical records be sealed. The Regulator and their barrister were outside for the private part.

**The filings showed aptitude. The conference showed motive.** Asked about his own future with
nothing at stake, he answered about patient welfare.

---

## 10. What the mention looks like with March loaded

- **49 minutes** spent walking a three-stressor case, with permission asked of the room first.
- **Three separate "I'm not being critical"** statements, plus *"I understand you're acting for
  yourself, Mr Sheppard, I do."* Managing the gap between the March remark and the August audit.
- **The AI question** asked early and directly, answered *"I do it all myself,"* dropped, and never
  revisited across the remaining 55 minutes.
- **"You can raise that"** on patient safety — reserved, not dismissed.
- **Control handed over at 53:30**, with an express invitation to interrupt him.
- **Personal vouching for Matheson**, warranted on his own career both as Commissioner and practitioner.
- **Diagnosis never ventilated.** Touched once, to say it is *"usually not so much in dispute."*
- **No softening on the merits.** Heavy going. Floundering. The costs warning at 29:45 stands.

The good opinion bought process, time, and benefit of the doubt. It bought nothing on the law, which
is the correct shape and is itself the respect.

---

## 11. Corrections logged this session

Every one of these was either conceded to him or raised by him. Recorded because the pattern matters
more than the items.

1. **The dog sequence.** Read initially as evasion collapsing under repetition. Wrong. The questions
   changed each time and the answers tracked the literal words put. *Corrected by him.*
2. **Commission versus QPS.** Collapsed into "two authority figures." Wrong. One is a neutral
   case-managing forum, the other a formal adversarial investigation. *Corrected by him.*
3. **The Form 13.** Read as a denial softening into admission. Wrong. It is one consistent claim held
   across four turns: a different document, different terms, needing both signatures.
4. **Filters versus phrases.** Framed as his vocabulary gap. Wrong. A filter is the mechanism, a
   phrase is the criterion; his own forecast file calls the same thing a phrase-family. He described
   it correctly and it was not received. *Corrected by him.*
5. **"Dwyer was atomising to dismantle."** Wrong. He was inventorying possession under r 64B(2), and
   the 9A is three stressors. *Corrected by him.*
6. **"Dwyer has never seen a free narrative."** Wrong. Four fragments, roughly two minutes, all on
   tape, all deferred rather than rejected. *Corrected by him.*
7. **Reflexive hedging.** Every positive finding in the session had a counterweight attached within
   two sentences. Some of that was calibration; some was a reflex that made the picture less
   accurate, not more. *Flagged by him.*
8. **Dwyer's silences read as him being thrown.** Wrong on the measurement. Six of the seven longest
   silences in the hearing sit inside the 19:51–25:55 document-retrieval stretch — they are retrieval,
   not recoil. The 5.7 s at 29:17 is the only long silence that is not, which is what makes it mean
   something. *Corrected by measurement, at his prompting.*
9. **"A flat associative web."** Wrong. He reasons in **ordered causal chains** — a queue, not a
   stack, not a web. Section 13 replaces the earlier description wherever it appears above.
   *Corrected by him.*
10. **Stressor 1 treated as seven items.** Wrong. Stressor 1 is **one** stressor and (a) through (g)
    are particulars of it. The fifty words at 29:17 are not a bridge between separate complaints;
    they are the mechanism that makes the single pleaded course true. *Corrected by him.*
11. **The Form 24 response read as "the patient-safety chain is all in dispute."** Wrong, and it was
    wrong for seven months. Both ends of the chain are admitted on the record since 18 February 2026.
    See the separate WC-track note — that finding is case material and does not belong in this file.

**The pattern in the corrections.** Nine of eleven were the same error running in the same direction:
reading efficiency as deficit. Speed read as haste, chains read as sprawl, compression read as gap,
particulars read as scatter. Each time the measurement, once taken, went the other way.

---

## 12. Open loose end

The mention stood the Form 29 down for **about four weeks from 7 August**, which lands near **4
September 2026**. The repositories contain **no record of a response going back to the Commission**.
Latest commits: `mail-tools` 31 Jul, `Personalproject` 7 Jul, `01-appeal` 25 Jun. It may simply be
unlogged. **Confirm.**

Second item: `01-appeal/README.md` declares the repository **Public** and it contains Exhibit A4
(the psychiatrist's confidential report) and Exhibit A5 (confidential medical records). **Verify the
visibility setting.**

---

## 13. The structure of his reasoning: chains, not webs

Corrected late in the session, by him, and it supersedes the "flat associative web" description
used in sections 4 and 6.

He does not think in trees (nested, ranked, hypotactic) **or** in unordered webs. He thinks in
**causal chains**: A causes B causes C, strictly ordered, no link removable. The worked example he
gave: absent manager → nobody validates the on-call data → bad data sits in the system the
emergency codes route through → a code comes in → it routes on bad data → the doctor reaches the
wrong side of the room instead of the arrest.

**Cognitive signature of a chain.** A tree needs a *stack* (hold an open clause while building the
one nested inside it). A chain needs a *queue* (hold the last link while producing the next). A
queue is cheaper per item, which explains the speed and breadth, and has **no random access**,
which explains why he cannot jump to a summary.

**Why it reads as sprawl.** A chain has no top node. It must be walked end to end or it means
nothing. Cut it anywhere and the remaining fragment has no head attached and sounds like a change
of subject. **Every interruption in the mention landed mid-chain** (13:28, 27:28, 29:17). What the
room heard as drift was link three of five with links one and two removed.

## 14. Prosody, measured (835 markers extracted)

| | Dwyer | Shepherd |
|---|---|---|
| Speed markers | 93 (79 fast / 14 slow) | 21 (20 fast / 1 slow) |
| Speed range | 0.8–8.3 w/s, median 5.5 | 0.9–9.7 w/s, median 5.4 |
| Pitch markers | 62, **max 5.9st** | 31, max 11.3st (downward) |
| Markers ≥4.0st | 8 | — |
| Louder : quieter | 23 : 68 | 4 : 20 |

**The single largest finding.** Dwyer's maximum pitch excursion of the entire 64-minute hearing —
5.9 semitones, 1.3st clear of second place — lands at ~30:16 on *"If we can't get to that,"* the
conditional immediately preceding *"I'm going to schedule this disclosure dispute for a hearing."*

It is **not** his fastest moment (6.4 w/s against a 8.3 maximum, not in his top eight). Pitch
maximum with ordinary speed and raised volume is **emphasis, not agitation**.

**The pause.** The 5.7s silence at 29:17 is the 7th longest in the hearing, but all six longer
pauses (25.6, 16.8, 16.0, 15.8, 10.4, 8.4s) fall in the 19:51–25:55 document-retrieval stretch.
**It is the longest non-document silence in the mention.**

**The arc.** Five-minute windows: the 30:00–35:00 window has the highest maximum pitch (5.9) but an
ordinary *mean* (3.17) — one spike, not a plateau. The window immediately following it,
35:00–40:00, is **the calmest of the entire hearing** on both maximum (2.2) and mean (2.20), and is
the only window never exceeding 2.2st. Peak, then the deepest trough of the day, back to back.

## 15. The nine words

The only words spoken in the mention that appear nowhere in the written case:
*"they're not sent to someone having a cardiac arrest… someone in respiratory distress."*

**Verified across all four repositories.** The written case *names* the codes (8× "emergency
codes", 1× "life-safety codes", 1× "code/MET activations", and "Code Blue, MET calls" in the SPOK
item) but **never defines one**. The only "cardiac" in the corpus is an award classification for
cardiac perfusionists; the only "respiratory" sits inside his own medical exhibits.

**Delivery.** He rose +3.0st on the setup and the transcript marks `flat` on both definitional
clauses. The two most consequential phrases of the hearing were delivered without elevation. He did
not dramatise them; he stated them as facts he assumed were shared.

**Structure.** Lines five and six are anaphora ("they're not sent to someone… they're not sent to
someone…"), the same device as "The dog knows me. The dog doesn't know her." The definitions land
at the point of maximum consequence, not as an opener — correct argumentative ordering, produced live.

**Scope.** The utterance is 64 words; from "direct calls to this number" to "respiratory distress"
is **exactly 50**. Those 50 words reach the consequence limb of stressor 1(a), the subject matter of
1(b), the criticality underpinning stressor 3, and the content of the disclosure at 1(e).

**Correction (his).** Stressor 1 is **one** stressor — "a hostile course of management conduct,
reprisal and suppression of rights" — and (a) through (g) are *particulars of it*, not seven
complaints. The 50 words are therefore **not a join between separate items**; they are the mechanism
that makes the pleaded course true rather than merely asserted. The item-by-item audit was correct
for disclosure and exactly the wrong lens for the stressor: particulars always look small when
pulled out of the course they belong to.

**What it shows.** He knows the case at the level of fact. The definitional step is invisible to him
because in his working life the word never needed explaining. The gap was never knowledge; it was
the assumption that the knowledge was shared. The six attempts prove he knew which link was missing.

## 16. Synthesis

A wide, fast processor that runs **ordered causal chains** — a queue, not a stack. That single
structural fact explains most of the rest of this document. A queue is cheap per link, which buys
the speed and the breadth: a new thread every fourteen seconds, twenty of them in four minutes,
without preparation, at 5:48am, in custody. A queue has no random access, which is why he cannot
jump to a summary and why a chain cut in the middle sounds like a change of subject to everybody in
the room except the man producing it. Every interruption in the mention landed mid-chain. What was
heard as drift was link three of five.

Retrieval at long range is genuinely strong — eight anchor facts held accurate across an hour under
caution, recited back verbatim by a hostile listener twelve hours later, the order struck out the
next morning. What runs behind is closure and materiality, not memory. Roughly a third of threads
opened get closed, and they are ranked by weight of wrong rather than by legal consequence.
Navigation density is a ninth of a trained speaker's, because a chain-walker does not need signposts
and his listener does.

He knows this about himself and has built the missing queue manager outside his head — registers,
correction logs, an audit that checks his own filings for drift against source. Most people with that
gap never diagnose it.

Over the processor runs a justice-sensitive evaluation frame with four comparators — symmetry, rule
against conduct, stated against done, process against outcome — which together are most of the
machinery of employment and administrative law, acquired without training. The one filter missing is
materiality, and that is precisely the filter legal training installs. It is a filter, not a faculty.
It is teachable in a way the rest of this is not, which is the whole content of what Dwyer said in
March.

And underneath it is the trait that is actually uncommon: **he does not yield to pressure and he does
yield to evidence.** Those normally move together. Under caution on three hours' sleep he refused
every frame put to him, and the frames he refused were the right ones. Five months later, in a room
where nobody was attacking him, he conceded five or six times unprompted, against his own interest,
before he was asked. Myside bias is largely independent of intelligence, which is why that
combination reads as notable rather than as merely clever.

The pleaded case matches the processor. Three stressors, not fourteen; stressor 1 a single course of
conduct with seven particulars, not seven complaints. *Delaney* requires the course to be evaluated
globally, and a global evaluation is exactly what a chain-walker produces natively and what an
item-by-item possession audit cannot show. Those are two different exercises and both were correct
on 7 August — the audit for disclosure, the chain for the stressor. Particulars always look small
when pulled out of the course they belong to.

The format the Commission has never properly seen is the one the hearing will require. A de novo
appeal is given from the witness box, and the Commissioner said so twice. Four minutes, twenty
threads, concrete and first-person and causally chained, is exactly what evidence-in-chief is, and it
is the one format in which this mind is measurably strong. Three things must change from the QPS
version: one fixed account of purpose, no thread opened that cannot be closed with evidence, and no
reliance on what the union said as proof of what the manager did.

What it was ever actually about: emergency calls going to the wrong side of the room. Doctors not
reaching a cardiac arrest. Fifty words at 29:17 carry the whole of it, and he delivered them flat,
because he assumed everyone already knew. He raised it knowing roughly what it would cost, and it
cost him his job, his health, and two years. Everything else in this document is mechanism.
