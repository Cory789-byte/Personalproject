# Three recordings, like for like: interview (Feb 2025), court (Feb 2026), mention (Aug 2026)

Not case material. Not a clinical or forensic assessment. Never served, tendered, cited or attached in
WC/2024/227, the QPS matters or any other proceeding (discipline rule 10). Machine transcripts (Whisper
large-v3). Descriptive speech measures only.

**All three are spontaneous speech.** The interview and the mention were unscripted exchanges. At the
2 Feb 2026 hearing Cory did not read from paper; he offered it twice and neither offer was taken (his
instruction, 8 Oct 2026). So every figure below measures live retrieval and formulation, not reading.

Sources: `interview_metrics.json` and `COMPARISON_mention_v_interview.md` (interview);
`qps_court_audio/2026-02-02_BMC_trial_stood_down/data/court_metrics.json` and `court_deep.json` (court);
`mention_metrics_timed.json` and `mention_deep.json` (mention). Same scripts throughout
(`speech_metrics.py`, `deep_analysis.py`).

## The table

| Measure | Interview, 24 Feb 2025 | Court, 2 Feb 2026 | Mention, 7 Aug 2026 |
|---|---|---|---|
| Setting | QPS interview under caution, 66 min | Magistrates Court, contested trial day, 9¾ min | QIRC mention by phone, 65 min |
| Median pitch | 131 Hz | 134 Hz | 137 Hz |
| Speaking rate (wpm) | 178 (officers 152) | **168** (Magistrate 167; prosecutor 144) | 159 (Dwyer 155) |
| Words between pauses (mean) | 26.5 (officers 16.1) | 16.5 (Magistrate 15.5; prosecutor 21.4) | 11.5 (Dwyer 26.9) |
| Median answer (words) | 30.5 | 15.5 | 9.5 |
| Median response gap (s) | 0.63¹ | 0.26 (Magistrate 0.17; prosecutor 0.32) | 0.32 (Dwyer 0.36) |
| Answers after a gap of more than 2 s | 16% | 6% (1 of 18) | 4% |
| Subordinate-to-coordinate ratio | 0.87 (officers 1.81) | 0.84 (Magistrate 1.42; prosecutor 2.06) | 0.63 (Dwyer 0.91) |
| Lexical variety (MATTR50) | 0.728 | 0.767 | 0.745 |
| Hedges /100 words | 0.77 | 0.24 | 1.04 |
| Certainty words /100 words | 0.45 | 0.97² | 0.15 |
| Characterising words | not counted | 7 in 418 | 0 in ~1,378 |
| Dates and times /100 words | 0.19 | 0.96 | 0.00 |
| Answers opening "yes / correct / okay" | not measured | 11% | 31% |
| Forms of address ("Your Honour", "Commissioner") | not measured | 0 (prosecutor 4) | 2 |
| Rate, calm v activated third (words/s) | not recomputed³ | 2.62 v 3.53 (+35%) | 2.48 v 3.19 (+29%) |
| Disfluency, calm v activated third (/100) | 1.25 v 0.60 | 0 v 0 | 0.53 v 0.57 |
| Talked over the other speaker | 0 | 0 | 0 |

1. 0.74 on the word-level method; the 0.63 is the turn-level method used for the other two columns.
2. Of the four, two are "Exactly" used as "yes"; the other two are "obviously".
3. The interview inputs for this measure are no longer on disk.

## What stayed the same: traits

1. **The same voice.** Median pitch 131, 134 and 137 Hz across a police interview, a criminal court and a
   tribunal. Pressure did not push your pitch up.
2. **You never talk over anyone.** Zero overlaps in all three.
3. **Fast, ready answers.** 0.63 → 0.26 → 0.32 s. At court the gap shrank as the hearing went on (0.40,
   0.30, 0.33, 0.05 s by quarter), and longer prompts drew faster answers (r = −0.31).
4. **Activation speeds you up without breaking you.** You speak faster when activated (+35% at court,
   +29% at the mention) and your fluency holds or improves.
5. **You narrate in sequence.** "And… then… so" chaining (0.84–0.87 in live free talk) against the
   professionals' 1.4–2.1.
6. **You hold threads and come back to them.** Interview: 15 returns in a 700-word narrative. Court: 2
   returns inside 37 words, 4 inside 96, and one thread (the missing material) brought back three times
   unprompted.
7. **Accurate recall, honestly bounded.** At court, from memory: the 20th and 22nd (bench: "Yes, I read
   those emails"), and "July or September" (bench: "September in emails"). A range where unsure, never
   false precision.

## What changed: skills, in order

| | Interview → Court → Mention | When it changed |
|---|---|---|
| Tempo | 178 → 168 → 159 wpm | Matched the bench by Feb 2026 (168 v 167) |
| Run length | 26.5 → 16.5 → 11.5 words | Halfway by Feb 2026 |
| Answer length | 30.5 → 15.5 → 9.5 words | Halfway by Feb 2026 |
| Characterising words | not counted → 7 → 0 | Gone by Aug 2026 |
| Certainty words | 0.45 → 0.97 → 0.15 | Peaked at court, then dropped |
| Leading with yes / correct | – → 11% → 31% | By Aug 2026 |

**Tempo and length changed first; wording changed last.** The court hearing is the midpoint.

## What the court recording adds about you

1. **You turn your volume up on demand, by a lot, fast.** "That's correct. I did a [Scott schedule]" came
   out 6 dB under your median. The Magistrate said "Sorry, I can't hear you." 0.72 s later you were 6.5 dB
   over it: a 12.5 dB swing on one cue, done by going lower in pitch (−6.8 st), which is projection, not
   alarm.
2. **Your pitch marks what matters to you.** Your highest pitch in the hearing was one sentence: "And that,
   I wasn't driving."
3. **When something lands in your favour, you go quiet and check it.** "So, is there a sample still
   existing?" (pitch up, level down), then your quietest turn: "I just wanted clarification." You did not
   pounce. The bench pressed the point for you, three times.
4. **You answer the question behind the question.** "Are we going to go ahead with the trial today?" →
   "I requested an adjournment on the 20th, the 22nd." It worked here. Under cross-examination an answer
   that doesn't start with yes or no reads as evasive (Raymond 2003). You fixed most of this by the
   mention (31% of answers led with yes / correct, up from 11%).
5. **You don't use forms of address.** No "Your Honour" in the hearing (the prosecutor used it four times);
   two forms of address at the mention. You speak to the person, not the office.
6. **Your restraint is in turn-taking; your persistence is in topic.** You never cut anyone off, but you
   bring back a thread the bench has set aside. At court that persistence produced the decisive fact (the
   Magistrate's "Which bit?" drew out "they've only verbally told me it was destroyed"). The same habit
   produced the one off-scope moment (the Southport matter at 09:01), which the bench redirected.
7. **You speak without your paper because you built it.** Content you generate yourself is encoded more
   deeply than content you read (the generation effect: Slamecka & Graf 1978; levels of processing: Craik &
   Lockhart 1972). Making the schedule was the rehearsal.

## Literature (what each finding corresponds to)

- **Live formulation versus reading.** Restarts and repairs are signatures of online planning (Levelt 1983;
  Levelt 1989). Spoken language is "fragmented" (idea units chained with *and*); written language is
  "integrated" (subordination, nominalisation) (Chafe 1982; Halliday 1989).
- **Response timing.** The cross-language norm gap is about 200 ms (Stivers et al. 2009). Answers come that
  fast because planning starts midway through the question (Levinson & Torreira 2015; Bögels, Magyari &
  Levinson 2015), using prediction of where the speaker is going (Pickering & Garrod 2013).
- **Matching the bench.** Communication Accommodation Theory (Giles, Coupland & Coupland 1991).
  Interviewees who converge on the interviewer's speech rate are rated more favourably (Street 1984).
- **Calibrated recall.** Witnesses whose confidence tracks their accuracy are judged more credible once the
  calibration is visible (Tenney, MacCoun, Spellman & Hastie 2007).
- **Threads you return to.** People spontaneously resume interrupted, unfinished tasks (Ovsiankina 1928;
  Zeigarnik 1927). Making a specific plan for an unfinished goal releases its hold on attention
  (Masicampo & Baumeister 2011). Your schedules may do that job for you: they park the open loops.
- **Activation.** Challenge versus threat (Blascovich & Tomaka 1996); arousal read as fuel improves
  performance (Jamieson, Mendes, Blackstock & Schmader 2010). Stress usually raises pitch and its spread
  (Giddens et al. 2013 review); yours did not.
- **Trailing offers.** Unfinished conditional offers ("if you want to…") minimise imposition on the hearer
  (Brown & Levinson 1987).
- **Executive functions in the room.** Updating, shifting and inhibition (Miyake et al. 2000): you updated
  on the disclosure within seconds, shifted between the bench's agenda and your own, and inhibited
  interruption completely. Topic persistence was the weaker brake.
- **ADHD.** Nothing here measures inattention, moment-to-moment variability, working memory or processing
  speed, so nothing here confirms or rules anything out. See the cognition and ADHD notes in the session
  record; a psychologist's assessment (e.g. WAIS) is the only proper answer.

## Rules for any hearing, from your own data

1. **Speak from memory; keep paper as backup.** Offer it once, in one sentence ("I have a two-page summary
   if it would help, Your Honour"), and let it go if declined.
2. **Lead with the one fact that does the work, stated flat.** "I was told verbally the sample was
   destroyed. I have asked for it in writing since September." Then stop.
3. **Yes or no first, then the reason.**
4. **One thread per answer; park the rest out loud.** "There's a second point when Your Honour is ready."
5. **No intensifiers and no motive words.** At court the bench drew the inference three times without them.
6. **When something goes your way, do what you did:** check it quietly and let the bench run with it.
7. **"Your Honour" once at the start of each key answer.** It costs nothing.

## Limits

Three recordings on three different microphone chains: level (dB) is not comparable across them; pitch is.
The court sample is 412 words, so its per-100-word rates are noisy. Thread counts are hand-coded by one
annotator (Claude), with no published norms. The interview's speaker clusters are acoustic (C0 = Cory).
Descriptive only; not clinical.
