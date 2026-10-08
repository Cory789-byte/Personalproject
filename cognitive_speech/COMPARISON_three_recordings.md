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
| Median answer (words) | 30.5 | 15.5 | 9 |
| Median response gap (s) | 0.63¹ | 0.26 (Magistrate 0.17; prosecutor 0.32) | 0.32 (Dwyer 0.36) |
| Answers after a gap of more than 2 s | 16% | 6% (1 of 18) | 4% |
| Subordinate-to-coordinate ratio | 0.87 (officers 1.81) | 0.84 (Magistrate 1.42; prosecutor 2.06) | 0.63 (Dwyer 0.91) |
| Lexical variety (MATTR50) | 0.728 | 0.767 | 0.745 |
| Hedges /100 words | 0.77 | 0.24 | 1.04 |
| Certainty words /100 words | 0.45 | 0.97² | 0.15 |
| Characterising words | not counted | 7 in 418 | 0 in ~1,378 |
| Dates and times /100 words | 0.19 | 0.96 | 0.00 |
| Answers opening "yes / correct / okay" | not measured | 11% | 32% |
| Forms of address ("Your Honour", "Commissioner") | not measured | 0 (prosecutor 4) | 2 |
| Rate, calm v activated third (words/s) | not recomputed³ | 2.62 v 3.53 (+35%) | 2.48 v 3.19 (+29%) |
| Disfluency, calm v activated third (/100) | 1.25 v 0.60 | 0 v 0 | 0.53 v 0.87⁴ |
| Talked over the other speaker | 0 | 0 | 0 |

1. 0.74 on the word-level method; the 0.63 is the turn-level method used for the other two columns.
2. Of the four, two are "Exactly" used as "yes"; the other two are "obviously".
3. The interview inputs for this measure are no longer on disk.
4. All of the mention's rise is one segment (30:12.98, yours), counted because it contains "actually", which
   the measure treats as a repair word.

## What stayed the same: traits

1. **The same voice.** Median pitch 131, 134 and 137 Hz across a police interview, a criminal court and a
   tribunal. Pressure did not push your pitch up.
2. **You never talk over anyone.** Zero overlaps in all three.
3. **Fast, ready answers.** 0.63 → 0.26 → 0.32 s. At court the gap shrank as the hearing went on (0.40,
   0.30, 0.33, 0.05 s by quarter), and longer prompts drew faster answers (r = −0.31).
4. **Activation speeds you up without breaking you.** You speak faster when activated (+35% at court,
   +29% at the mention) and your fluency holds or improves in the interview and in court. At the mention the
   measure rises only on one segment, counted for the word "actually".
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
| Answer length | 30.5 → 15.5 → 9 words | Halfway by Feb 2026 |
| Characterising words | not counted → 7 → 0 | Gone by Aug 2026 |
| Certainty words | 0.45 → 0.97 → 0.15 | Peaked at court, then dropped |
| Leading with yes / correct | – → 11% → 32% | By Aug 2026 |

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
   mention (32% of answers led with yes / correct, up from 11%).
5. **You don't use forms of address.** No "Your Honour" in the hearing (the prosecutor used it four times);
   two forms of address at the mention. You speak to the person, not the office.
6. **Your restraint is in turn-taking; your persistence is in topic.** You never cut anyone off, but you
   bring back a thread the bench has set aside. At court that persistence produced the decisive fact (the
   Magistrate's "Which bit?" drew out "they've only verbally told me it was destroyed"). The same habit
   produced the one off-scope moment (the Southport matter at 09:01), which the bench redirected.
7. **You speak without your paper because you built it.** Content you generate yourself is encoded more
   deeply than content you read (the generation effect: Slamecka & Graf 1978; levels of processing: Craik &
   Lockhart 1972). Making the schedule was the rehearsal.

## Why the voice is steady (measured 8 Oct 2026; `steady_voice.py`, output in `steady_voice_output.txt`)

| | Interview | Court | Mention |
|---|---|---|---|
| Pitch–loudness link (r), you v them | 0.28 v 0.45 (officers) | **0.15** v 0.52 (Magistrate), 0.57 (prosecutor) | 0.15 v 0.03 (Dwyer) |
| Pitch rise in your loudest fifth of speech | +1.7 st v +3.9 | **+0.3 st** v +1.1, +1.1 | +0.9 st v +0.4 |
| Pitch movement inside a phrase (SD) | 3.80 st v 4.02 | **2.90 st** v 3.90, 4.18 | 2.28 st v 2.83 |

Court, turns of similar length (2–12 s): your pitch range was 7.2 st (median turn 7.5 s) against the
Magistrate's 13.1 st (5.4 s) and the prosecutor's 15.2 st (4.9 s). Your turns were longer and still
narrower, so it is not a length effect. Questions asked: you 1, the Magistrate 13, the prosecutor 0.

**Four reasons, all measured.**
1. **You emphasise with loudness, not pitch.** When the Magistrate and the prosecutor got louder their pitch
   went up with it; yours barely moved. Dwyer is the only speaker in any of the recordings built the same way.
2. **You hold a level inside each sentence.** Your within-phrase pitch movement is the lowest in the room in
   all three recordings, and it has fallen every time: 3.80 → 2.90 → 2.28 st (three
   different microphones, so the trend is indicative; the comparison inside each room is the solid one). You set a level for a sentence
   and move it only for the ones that matter (the denial "And that, I wasn't driving" was set +3.0 st up).
3. **You were stating, not asking or advocating.** Questions and persuasion carry the most pitch movement.
   The prosecutor asked nothing, but his pitch rose with every push (r = 0.57).
4. **Activation does not reach your pitch.** Median 134 Hz at court, inside your 131–137 Hz across all three
   rooms. In most people stress raises it.

**What it is not.** Not reading (the restarts in §5 of the court analysis prove the speech was live). Not
the flatness of fatigue or low mood, which comes with slow speech, long pauses and a quiet voice: you were at
168 wpm, answered in 0.26 s, and swung 12.5 dB on one cue.

The interview figures are the weakest: "officers" is both officers merged, and the body-worn camera was
farther from them.

## Formulation patterns (`formulation.py`, output in `formulation_output.txt`)

| Per 100 words | Court: you | Magistrate | Prosecutor | Mention: you | Dwyer |
|---|---|---|---|---|---|
| Contrast and exception (but, except, unless, only, without…) | **2.43** | 1.26 | 0.00 | **1.50** | 0.86 |
| Reasons (because, reason, why, therefore, since) | **1.94** | 0.54 | 0.00 | 0.38 | 0.28 |
| Negation (same lexicon as `speech_metrics.py`) | **2.67** | 2.33 | 1.57 | **3.13** | 1.94 |
| they / them / their | **1.94** | 0.54 | 0.00 | **1.80** | 1.17 |
| I / me / my | **8.50** | 2.51 | 4.91 | **8.33** | 2.62 |
| Turns that open with "I" | 5 of 18 | 2 of 27 | 3 of 15 | 17 of 104 | 4 of 152 |

Interview, same negation lexicon: you 2.60, officers 1.91. You use the most negation in the room in all three.

1. **Your first word is a verdict on the question.**
   - When the bench restates you accurately, you open with "Correct" or "Exactly": 10 times across the two
     hearings (e.g. "she sent emails in the form of a directive to staff?" → "Correct.").
   - When its premise is wrong, you open with "Well" and correct it, 5 of your 6 "Well" openers. At court
     (03:12): "Well, that and the prosecutors are not giving over material." At the mention, three examples:
     - 35:21: "you don't need any documents for that, do you?" → "Well, they've got documents for it."
     - 38:31: "Did she decline it via email?" → "Well, she actually declined it on the phone and then declined
       it on the MyHR twice."
     - 47:15: "13 months went by…" → "Well, it was just time and time again…"
   - "Well" marks an answer that resists the question's terms (Heritage 2015).
2. **You give reasons and draw lines.** Close to twice the bench's rate of contrast and exception words, and at court
   nearly four times the Magistrate's rate of causal words. The prosecutor used neither: he stated positions
   ("it's my position", "for the court to decide").
3. **You reason by elimination.** "There's no reason why I should have had a positive result unless that is
   not mine." The structure is: no X, unless Y.
4. **You speak in absences.** "Not even there", "wasn't driving", "no reason". Listeners take longer to
   process negatives than positives (Clark & Chase 1972).
5. **Your institutions are "they".** "They've only verbally told me", "they just ignore me", "they can't
   even give me my evidence". The professionals name roles ("the defendant", "the prosecution witness").
6. **You start from yourself.** "I" is your most common first word. Dwyer opens with "So", "Okay", "And".
7. **You make frequency audible.** "Again and again and again", "asked for it and asked for it", "time and
   time again" (twice).
8. **You check you've been understood.** "If that makes sense" (08:36) and "Does that make sense?" (23:40)
   at the mention.
9. **You offer two pages, in both hearings.**
   - At the mention you offered them 0.48 s after Dwyer said "if you talk at me for two hours about something
     you can tell me in two minutes, I'm going to miss the point". He answered "Hand it up, please" 0.16 s
     later.
   - At court you offered them before the bench had asked for anything, and they repeated what she already
     had. They were declined.
   - In your two hearings, paper was taken when it answered the bench's problem and declined when it repeated
     what the bench already had.

The mention "questions asked" figure in `formulation_output.txt` is not used: several segments merge the
Commissioner's question with your answer.

## Loudness (measured 8 Oct 2026; `loudness.py`, output in `loudness_output.txt`)

All levels are measured against your own median in each recording. Absolute dB cannot be compared
across the three microphone chains, or between speakers on different microphones.

| | Interview (66 min) | Court (9¾ min) | Mention (65 min) |
|---|---|---|---|
| Drift across the recording | +0.16 dB per 10 min (officers −0.65; they fell 3.7 dB from the first quarter to the last) | +1.4 (the whole room rose: Magistrate +2.5, prosecutor +1.9) | +0.3 (Dwyer +0.2) |
| End of turn against start | −0.2 dB (officers −1.1) | −1.2 dB; 4 of 16 turns ended more than 3 dB down (Magistrate −0.9; prosecutor −2.6) | −1.1 dB (Dwyer +0.5) |
| Louder goes with faster (r) | not measurable | +0.39 | +0.30 |

1. **You don't fade.** Over an hour you hold your level. The officers faded.
2. **Your volume is a confidence meter.** You are quietest when conceding, unsure or retreating.
   - *Court:*
     - the opening, "That's correct. I did a [Scott schedule]" (−6.0 dB; the bench could not hear it)
     - "I just wanted clarification." (−5.7)
     - "But the prosecutor said no. I have requested a stay, so a stay or adjournment and a stay." (−3.2)
   - *Mention:*
     - "I guess I did request, but I didn't be specific about that." (−5.8 to −8.4)
     - "I can't remember the…" (−5.5)
     - "I haven't been specific because I thought I had to go to MSH" (−3.8)

   Confident answers are louder and faster (Kimble & Seidel 1991), and listeners hear the drop.
3. **At court your volume went to the wrong places.**
   - *Loudest:* the paper offer (+3.6), "Yeah, obviously…" (+2.7), the NATA complaint (+2.1), "targeted"
     (+1.3) and Southport (+1.2).
   - *Quieter:* your request for a stay was at −3.2. The facts that won ("not giving over material";
     "only verbally told me it was destroyed") were at −0.8 and +0.4.
   - *During the disclosure:* in the third quarter the bench and the prosecutor got louder and you dropped
     1.7 dB. You listened and checked, which was right.
4. **At the mention you were loud where it counted:** the emergency calls ("they're not sent to someone
   having a cardiac arrest", +4.6 dB at your normal pitch). It came at the end of a long answer and the
   Commissioner moved on.
5. **You disagree softly.** Answers that open with "Well" (correcting the premise) start 2.3 dB under your
   median. That is disagreement softened, not raised (Pomerantz 1984).
6. **Your loud is also your fast.** "I've got it here for you if you want to…" was +3.6 dB at 9.8 words a
   second.

Not used: your loud-segment share at the mention, because several segments labelled as you carry the
Commissioner's louder voice where a question and answer were merged. The six lines re-attributed to
Ms Matheson are excluded throughout.

## How you come across

- **Sincere.** You answer in about a quarter of a second, and fast answers are judged more sincere than slow
  ones (Ziano & Wang 2021).
- **Calm, controlled and serious, not theatrical.** Listeners hear liveliness and charisma in pitch movement
  (Rosenberg & Hirschberg 2009; Niebuhr et al. 2016). You have little, so you read as composed. Some will
  read it as intense rather than warm.
- **Firm, not agitated, when you push.** You push with volume at a steady or lower pitch. Low pitch signals
  size and assertion; high pitch signals smallness, deference or uncertainty (Ohala 1984).
- **Cooperative.** You match the bench's tempo, never talk over anyone, and check quietly when something
  lands. Interviewees who converge are rated more favourably (Street 1984).
- **Personal and owning.** You say "I" about three times as often as the bench. That is the language of
  someone answering for himself.
- **Precise.** "Correct" and "Exactly" tell the bench you are checking its paraphrase.
- **Two registers, two risks.** Court 2026 was certain and aggrieved ("obviously", "they", "targeted"). The
  mention was careful and slightly tentative ("I think", "if that makes sense"). Witnesses who speak plainly,
  without hedges or intensifiers, are rated more credible and competent (Erickson, Lind, Johnson & O'Barr
  1978; O'Barr 1982). Your best register is neither: plain facts.
- **In person versus on paper.** On paper both benches found you heavy: "pretty heavy-going stuff";
  "three pages of tiny print". In the room both engaged with you directly.

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

1. **Speak from memory; keep paper as backup.** Offer it only when it answers a question the bench has just
   asked or a problem it has just named (the mention: taken; the court: declined). One sentence ("I have a
   two-page summary if it would help, Your Honour"); let it go if declined.
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
