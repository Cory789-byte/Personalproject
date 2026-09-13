# Mention of 7 August 2026 — tempo and response-latency metrics
> 13 September 2026. Computed from `documents/transcripts/MENTION_7AUG2026_segments.jsonl`
> (1,068 diarised segments merged into 205 speaker turns). ⚠ Diarisation is imperfect: some tails
> of Dwyer's questions are attributed to Mr Shepherd (e.g. 36:52, 37:17, 43:36, 59:53), so
> "finished his sentence" instances are NOT relied on. Latency figures on clean turns are robust.
> Purpose: witness preparation. Internal only.

| Measure | Dwyer IC | Mr Shepherd |
|---|---|---|
| words spoken | 8,343 | 1,333 |
| speaking time | ~53 min | ~8 min (14% of the hour) |
| speech rate | 2.61 w/s | 2.68 w/s |
| response latency to the other (median) | 0.36 s | **0.32 s** |
| response latency (mean) | 1.03 s | 0.65 s |
| answers > 2 s after the question | 9 of 100 | 4 of 98 |
| answers > 3 s | 6 | 2 (one is 16 s at 23:19 — Dwyer reading the handed-up pages, not Shepherd thinking) |

**Reading.** Same speech rate; he answered faster than the Commissioner answered him. The
Commissioner's longer pauses are judicial habit (think, then speak). Speed of processing was never
the problem in the room; **routing** was — answering the question behind the question (40:13), and
under-claiming documents held. Both are fixable and neither is a speed defect.

## The clean fast turns (gap from end of question to first word)
| Time | Gap | Question (tail) → answer |
|---|---|---|
| 08:36 | — | *"…whether that's relevant to your case"* → **"it didn't really matter what's inside those complaints. It's that they happened to me… I wouldn't even need to read them."** ⭐ the relevance point — see below |
| 21:29 | 0.00 s | *"…this is the other difficulty…"* → **"Could I give you a simplified…"** — 30 s after the volume complaint, hands up two pages |
| 22:52 | 0.10 s | *"This is the simple version, is it?"* → "Yes." |
| 32:02 | 0.00 s | the cost framing → **"I think I can understand where you're getting at, I think I can meet most of the way"** — adapts on the spot |
| 40:28 | 0.12 s | *"Yes or no?"* → "Yes." |
| 42:25 | 0.14 s | *"…the email from Ms Taylor that you're comparing to yours?"* → "Correct, yes." |
| 42:53 | ~2 s | "Yeah." → **"but you don't know… I don't know that… to a certainty."** ⭐ self-corrects his own answer within two seconds |
| 52:46 | 0.18 s | *"have you got access to the rosters?"* → **"I have all the evidence for that."** |
| 53:22 | 0.00 s | Dwyer's premise about pay disclosure → **"I think I actually said that I'm not asking disclosure about that anymore"** — corrects the bench's premise instantly, and correctly |

## The best pause of the day
**42:42 — 3.9 s** before *"I don't have knowledge of that."* He slowed down exactly when the honest
answer required it. **That is the model for the witness box: fast on facts he holds, slow on what he
does not know.**

## ⭐ The relevance point at 08:36, and what it became
Dwyer had just said that three boxes of doctors' complaints would still each have to pass
relevance. Shepherd's answer: the content of the complaints is not the stressor; **receiving them
is.** The documents matter as events that happened to him, not as statements to be read for their
truth. Dwyer's response was *"perhaps you can explain that to me a bit more clearly"* — and then
the AI question. **A month later that instinct became ¶2 of the footing letter of 9 September:**
*"Where the document is itself the step taken… the Appellant does not rely on those documents as
statements about some other event."* The distinction he reached for live is the architecture of the
case as now built.

## For the witness box
- Latency 0.3 s reads as certainty. On admitted facts that is right. On characterisation it is a
  risk: the fast "Yeah" at 42:53 needed the 2-second correction that followed.
- Borrow the Commissioner's habit: a one-second pause before every answer in cross costs nothing
  and reads as considered. It also stops the question-behind-the-question reflex.
- The two under-claims (Q10, Q32) were memory under no-notice, not speed. With the fact numbers in
  front of him the same questions get *"yes — fact 49, Tab 6."*

## Syntax, hedging and thread-holding — his 100 turns against the Commissioner's 102
> Same source. ⚠ 1,324 words of spontaneous speech, mostly answers to closed questions, through
> ASR. Enough for pattern, not for precision. Rates per 100 words.

| | Mr Shepherd | Dwyer IC |
|---|---|---|
| mean words per turn | 13.2 | 81.1 |
| mean / median sentence length | 8.1 / 6 | 15.9 / 10 |
| subordinators (because, if, which, when, whether…) | **1.7** | 1.8 |
| coordinators (and, but, or, so) | 5.9 | 5.3 |
| contrast markers (but, rather, not just, other than…) | **1.4** | 0.8 |
| hedges (I think, I guess, for me, kind of, probably…) | **1.7** | 0.4 |
| turns of 40+ words | 5 | 47 |
| abandoned sentence starts | 5 (13:28, 16:18, 17:45, 21:29, 27:28) | ~0 |

**Reading.** Subordination is the same as a trained lawyer's in the same room — spoken English is
paratactic for everyone. He holds several parts at once by **chaining** (and / but / then), not by
embedding. Contrast markers are nearly double the Commissioner's: he frames by distinction ("not
X, it's Y"). Hedging is four times the Commissioner's, and that is the one number that costs him.

### Where the thread-holding shows (his own words)
| Time | What he did | Threads live |
|---|---|---|
| 13:28 | access to the room → login data → "it all works as one system" → an attachment about an unanswered complaint → **"No, hang on a sec. Sorry."** | **4 — and it collapsed.** He noticed the collapse himself. The ceiling, visible |
| 23:40 | server-side filter → Outlook analogy → "effective immediately" as the filter → "I basically just want the count" | 3, resolved cleanly — an analogy built live for the listener's model, then scoped down |
| 24:59 / 25:55 | "A to E, which is number 10" | cross-referencing Form 29 item numbers to his own table on the fly |
| 27:06 | defines the Commissioner's word ("unassessed… wasn't even in the room… without any input of the staff") then **pre-empts the rebuttal**: "Like a manager? I mean, usually a manager would need input" | 2 — his point and the bench's objection, held together **before the bench made it** ("that's just management action" came after) |
| 29:17 | direct calls to this number → it is an emergency contact → doctors sent to the wrong side of the room → not to the cardiac arrest, not to respiratory distress → "we're now not even contacting them by their numbers" | a five-link causal chain in one breath, coordinated not embedded |
| 39:18 | "what stressed me out was what action was taken when HR received that complaint" | two embedded clauses, correct — the stressor is the *response* to the complaint, not the complaint |
| 46:44 | "it wasn't actively spread, it was actively avoided, but would be more likely" | re-pleads a word live, downward, honestly |
| 47:55 | "I'm asking for evidence or a sworn statement to say that… they didn't do anything with it" | the **absence** concept — disclosure of inaction — which became the does-not-allege / does-not-list negatives |
| 53:22 / 53:50 | "I actually said I'm not asking disclosure about that anymore" / "that's a different subject" | bookkeeping across twenty minutes: which threads are closed, which are separate |

### Verdict — above a regular lay person, in a specific way
- **Concept formation and bookkeeping: well above.** Four ideas produced live under no notice —
  the relevance point (08:36), the absence concept (47:55), the pre-empted management-action
  rebuttal (27:06), the stressor-is-the-response point (39:18) — each later became a structural
  part of the case. Most self-represented litigants do not produce one of those in an hour.
- **Sentence delivery: ordinary, and under load it breaks.** Five abandoned starts, all in turns
  carrying three or more threads. The concept arrives faster than the sentence that carries it.
  ⭐ That mismatch is exactly what the Commissioner heard: paper that was "heavy-going" (full
  syntax carrying the concepts) and speech that was "floundering" (the same concepts in fragments).
- **Hedging: the fixable cost.** "For me", "I guess", "I think" at four times the bench's rate. On
  facts he holds, a hedge reads as doubt. Keep hedges only for what he genuinely does not know
  (42:42 was the right use).

### For the box
**One thread per answer.** His best turns were single-thread and under ten words; his one collapse
was four threads. In cross he will never need more than one. In chief, the outline already breaks
the evidence into single topics — answer the topic, stop, wait for the next.
