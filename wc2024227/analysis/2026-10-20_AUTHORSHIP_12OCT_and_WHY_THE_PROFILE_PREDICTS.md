# Was the 12 Oct Registry email Matheson's? And why a data profile of the Regulator predicts (20 Oct 2026)

> Internal. Prediction only; never cited, never put to anyone. Metadata is read only.
> - **Script and output:** `analysis/stylometry/matheson_style.py`, `matheson_style_output.txt`.
> - **Timing data:** `documents/timeline/CHRONOLOGY_email_metadata_15Oct2026_AS_RECEIVED.md` on branch
>   `claude/workcover-matter-repo-krg8qg`.

## Verdict

- **She sent it, and the frame is hers.** That covers the opener, the closer and the slips.
- **The two sentences that carry the strategy are not in her voice.** They put items 2–7 to the conference
  "in lieu of ordered in directions, in the first instance", and they offer the "undertaking". None of their
  key phrases appears in any of her 24 other emails, before or since.
- **The text was pasted in.**
- **Most likely:** someone with legal-drafting habits (Counsel or a senior officer) settled the position, and
  she put it into an email.
- **Confidence:** moderately strong on "not her words". Who wrote them cannot be told from the text.

## The baseline

Her own emails, July 2025 to 12 Oct 2026:
- 17 full bodies, plus the openings of 7 more (24 in all);
- 4 emails since (16, 19, 20 and 20 Oct);
- control: the 8 Sep cover letter (Word author "Peter").

Lists, signatures and quoted text were removed.

## The tells

1. **Legal idiom she never uses.** Each of these is in 0 of her 24 emails, and in none of the four since:
   - "in lieu of";
   - "in the first instance";
   - "undertaking";
   - "in receipt of";
   - "better placed";
   - "believes";
   - "jointly";
   - "not contactable".

   They occur once in her whole record, in this email.
2. **The foreign part is the strategy.** Share of each sentence's word triples found in her other emails:

   | Sentence | Share |
   |---|---|
   | Opener ("I refer to the above matter and…") | 40% |
   | Agrees to the conference | 20% |
   | Points 2–7, "better placed… in lieu of ordered in directions, in the first instance" | **0%** |
   | Counsel "not contactable" | 4% |
   | The "undertaking" request | 11% |
   | Closer ("…consideration of this request") | 29% |

3. **Her fingerprints are on the frame.**
   - These phrases all occur in her earlier emails to the Registry: "I refer to the above matter" (3/24),
     "set down" (3/24), "respectfully requests" (1/24), "consideration of this request" (2/24).
   - Her kind of slip appears too. "The correspondent of the Appellant" (for correspondence) and "Commissions"
     (no apostrophe) sit with her earlier slips:
     - "note it contents" (19 Feb);
     - "apologise on the delay" and "NNPD's" (14 Aug);
     - "documents which authenticity was disputed", "logan hospital", "Movements forms" and "Email from
       yourself to Cory Shepherd" (24 Sep);
     - "lay witness" for four (24 Sep).
4. **A dropped word.** "In lieu of ordered in directions" is missing "being", the kind of break left when
   shorthand is turned into a sentence by someone else (inference).
5. **Pasted, not typed.**
   - New emails she writes to the Registry took 77–549 s from creation to sending: 17 Feb 549, 18 Feb 220,
     24 Feb 228, 13 May 122, 20 May 77, 6 Aug 101.
   - This one took **10 s**.
   - **Calibration:** her 24 Sep email to Cory was also pasted (20 s) and its wording is entirely hers. Pasting
     alone means prepared in advance, probably for approval. It does not mean another author.
   - Both pasted emails carried decisions. Routine emails are typed live.
6. **A new function for her.** Every other email she has sent to the Registry is logistics: attendance,
   rescheduling, filing. This is the only one that argues a procedural position to the Commission.

**Contrast.** The 19 Oct email also has new sentences, but its new phrasing is everyday: "Could you please
confirm", "in the hopes that", "while she finishes the last days of her leave". What marks this one is not
new phrasing but new *legal* phrasing.

### The later emails, by the same test

| Email | Reading |
|---|---|
| 16 Oct | Hers. Its reservation paragraph is the 8 Sep letter's wording, re-used |
| 19 and 20 Oct | Hers, with no legal idiom |
| Control: the 8 Sep letter | Mean sentence length 37 words, against her 14–26. Word-pair overlap with her emails 10%, against her own range of 30–93% |

### Earlier tells withdrawn after testing against the baseline

- "respectfully requests" is hers (17 Feb).
- "set down" is hers (24 Feb, 10 Mar, 31 Mar).
- "Pasted" does not by itself mean another author (24 Sep).

## Why a data profile predicts

1. **Routines repeat.** The same officer, templates, approval chain and rules recur, so behaviour has base
   rates.
2. **Incentives are fixed.** Dates that carry a consequence (deemed admission, Commission directions) are
   met. Others drift. The model-litigant duty, costs and avoiding a published loss produce the same choices
   each time.
3. **Change is visible only against a baseline.** Her voice, her timing and the defend sentence are the
   normal. A departure is then a signal: a new hand in an email, a sentence that stops appearing, a reply in
   17 h 40 min instead of 10–21 days.
4. **The channels are independent:**
   - timing;
   - wording;
   - recipients;
   - order;
   - metadata;
   - selection.

   Agreement between them raises confidence. Disagreement means look harder.

### Track record (examples, verified in the ledgers)

**Hits:**
- the r 49 response 3 days early (8 Sep);
- directions 3–4 met 6 days early (24 Sep);
- the defend sentence named as "the single most reliable tell" (13 Sep), and absent since 8 Sep;
- no denials, and the mechanical disputes dropped;
- Tab 32 on the day;
- joint dates to the Registry a day early (E40.1);
- the acknowledgement (E40.3);
- no substantive approach before 22 Oct (E38.2);
- nothing hardened before 22 Oct;
- the 16 Oct test.

**Misses:**
- "the 25th will be used in full" (they answered on the 24th);
- "the 25th letter will be in the legal register" (it was operational);
- "expect a s 556 application" (none);
- any contact before 22 Oct priced at about 20% (it came);
- "contact in the week of 26 Oct" (19 Oct);
- "conference mid–late November" (2–6 Nov offered).

**The misses lean one way.** The profile expected more delay and more legal machinery than the Regulator has
used. It was built mainly on July–August behaviour:
- apologies;
- 10–21-day replies;
- "this week" that slipped 11 days.

Since the admissions, latency has fallen to 6 days and then 17 h 40 min. The profile predicts well within a
phase and lags at a change of phase. The lag is itself the signal of the change: faster, with less fight
machinery.

### Limits

- About 25 emails from one officer, so the style analysis is indicative only.
- **It predicts behaviour, not private decisions.** The merits decision sits with Counsel and a delegate who
  are never seen. The profile is strong on how and when, and weaker on what.
- **Every tell must be tested against the baseline first.** Three were withdrawn today on that test.

## For 30 Oct

**On profile:**
- the reply arrives on or just before the day;
- it is a decision email, prepared in advance;
- her frame carries legal wording that is not hers.

**How to read the legal wording:**
- "review its position", "consent orders" or "without admission" means Counsel's hand, with the decision
  showing.
- "as outlined in our Statement of Facts and Contentions" means the fight is back.
