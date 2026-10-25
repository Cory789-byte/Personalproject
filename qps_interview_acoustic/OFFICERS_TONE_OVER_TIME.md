# How the officers' tone changed across the interview (24 Feb 2025)

> ⛔ QPS track / personal file only (discipline rule 10). Machine measurements, unverified. This file is
> tone (loudness, pitch, pace, timing), not content. Content is coded turn by turn in
> `OFFICER_QUESTION_CODING.md`; the transcript stays outside the repo. Script: `officer_tone.py`; output:
> `officer_tone_output.txt`. Levels are relative to each speaker's own median.

**Who is who.** Cluster C1 is both officers. A two-component pitch model separates them reasonably well
(BIC 1087 v 1201; separation 2.38 SD):
- a **lower voice** (about 97 Hz), 83% of officer speech
- a **higher voice** (about 125 Hz)

The higher voice's share rose from about 5–8% of officer speech in the first 30 minutes to about 25% in the
last 30.

## The time course

| Window | Phase (by shape) | Officers: share of talk | Officers: level | Officers: pitch movement | Officers: gap after you | You: level | You: median turn |
|---|---|---|---|---|---|---|---|
| 0–8 min | Set-up, caution | **76%** | **+2.2 dB** | 4.45 st | **2.42 s** | −3.4 dB | 1.4 s |
| 8–20 | Your account | 24% | +0.7 | 4.06 | 1.64 | −0.5 | 9.3 s |
| 20–30 | Questioning | 32% | −0.1 | **3.65** (flattest) | 1.35 | −1.1 | 8.3 s |
| 30–40 | Most active exchange | 42% | +0.9 | 3.98 | **0.65** | +1.1 | **17.3 s** |
| 40–50 | | 37% | **−1.0** | 3.87 | 1.00 | **+2.0** | 4.6 s |
| 50–61 | Closing stretch | 35% | **−1.0** | **4.66** | 0.76 | +0.5 | 8.7 s |

## What changed

1. **They got quieter, both of them.**
   - The lower voice fell 0.78 dB per 10 minutes (r = −0.51); the higher voice fell 0.69 (r = −0.32).
   - That is about 4.5 dB over the hour. Your level held, rising 0.16 dB per 10 min (not significant).
   - Because both voices fell, this is not just a change in which officer was talking.
2. **Their pitch did not change.** Within each officer it was flat (+0.01 and −0.07 semitones per 10
   minutes). The small overall rise comes from the higher-voiced officer talking more later. No sign of
   rising agitation.
3. **They answered faster.** Their gap after you finished fell from 2.4 s in the set-up to 0.65–1.0 s from
   30 minutes on.
4. **Their pitch movement was U-shaped.** It was most varied at the start (procedure) and in the closing
   stretch, and flattest in the middle (20–30 min).
5. **You and they moved in opposite directions.** From 40 minutes, you were 2 dB above your own average and
   they were 1 dB below theirs. Your own pitch movement fell (4.12 → 3.49): you got steadier as they got
   quieter.

## What the literature says

- **Loudness is the voice cue of dominance.** In studies of interpersonal influence, loudness and its
  variation predicted perceived dominance more than pitch did (Tusing & Dillard 2000).
  - Low, loud voices signal assertion (Ohala 1984).
  - The officers' falling level with unchanged pitch, against your steady and then rising level, means
    vocal assertion shifted across the hour: they began as the louder party relative to their baseline and
    ended below it.
- **The turn-taking shape has phases.** Set-up and caution (they talk most, slowly, with long silences); your
  account (you talk three times as much); questioning (their share and speed rise); a closing stretch. That
  says when each side talked. It says nothing about what was said.
- **Faster follow-ups.** Their gap after you finished shortened from 2.4 s to under a second. With accusatory
  content (see the correction below), that reads as pressing, not as listening.

**Correction (8 Oct 2026).** The first version of this file, and a chat answer, said the officers' tone showed
"no accusatory escalation" and that their faster responses meant they were following you. Tone and content
are separate channels, and these measures see only tone. On Cory's account, every statement the officers made
was accusatory. The literature locates an accusatory interview in its content, not its volume:
- **Accusatory methods are defined by what is asked.** Presumption of guilt, confrontation, rejecting
  denials, and "minimisation" are all accusatory. Minimisation means offering sympathy or face-saving
  explanations, and it is delivered in a calm, even sympathetic voice (Kassin & Gudjonsson 2004; Kassin &
  McNall 1991; Meissner et al. 2014).
- **Interrogation training teaches a calm, confident, non-hostile demeanour while asserting guilt**
  (Inbau, Reid, Buckley & Jayne).
- **Interviewers who presume guilt ask guilt-presumptive questions and apply more pressure,** and observers
  then judge even innocent suspects as more defensive (Kassin, Goldstein & Savitsky 2003; Hill, Memon &
  McGeorge 2008).
- **What the two channels together show:** accusatory content delivered at a steady and then falling volume,
  with faster follow-ups. That is sustained, controlled pressure, not de-escalation.
- **Your side across the same hour:** your level held and then rose, and your voice got steadier (pitch
  movement 4.12 → 3.49). You did not escalate under sustained accusation.
- **What proves "every statement was accusatory":** the transcript. Each officer utterance can be coded:
  - open, closed or leading
  - guilt-presumptive or neutral
  - confrontation, minimisation or information-gathering

  The counts can then be set against the tone, minute by minute.

  **Done (8 Oct 2026), in `OFFICER_QUESTION_CODING.md`.** 53% of substantive officer turns were
  accusatory: 32% in minutes 6–30, then 69% in minutes 30–60. The most accusatory windows were also the
  fastest.
- **Over a long session, falling vocal effort is also the classic sign of fatigue.** It is the explanation
  to rule out before reading attitude into it.

## Cory's account of the content, and what it means (8 Oct 2026)

**Cory's account:** the officers sped up to press and accuse; they never listened to what he said; guilt was
presumed throughout; they did not follow a PEACE model.

**What PEACE requires.** Its founding principles (England and Wales, 1992) are:
- the aim is accurate and reliable information, not a confession;
- the interviewer keeps an open mind;
- the account is tested against the evidence, fairly.

Persistence alone is not the breach. A closed mind is. An interview that presumes guilt and does not take up
the interviewee's account is the opposite of the model, whatever its phases look like.

**The literature on the pattern Cory describes:**
- **Guilt presumption changes the interviewer.** Interviewers who expect guilt ask guilt-presumptive
  questions, use more pressure, and read the answers as confirming guilt (Kassin, Goldstein & Savitsky 2003;
  Hill, Memon & McGeorge 2008).
- **Investigator bias drives pressure tactics** (Narchet, Meissner & Russano 2011).
- **Tunnel vision:** once a suspect is settled on, information pointing elsewhere is discounted or not
  pursued (Findley & Scott 2006; Rassin, Eerland & Kuijpers 2010).

**The one documented instance on file.** Cory offered police every message on a USB. It was refused (QPS
track notes, `legal_system/`). Declining evidence the interviewee volunteers is not information-gathering.

**What would prove "never listening".** Speed alone cannot show it. A fast response can be a prepared next
accusation, or it can be a fast, attentive reply; Cory's own fast answers were the latter. The test is
uptake: whether each next question used what Cory had just said. Measured at the mention, the Commissioner
took up Cory's terms. For the interview it needs the transcript, plus a code for each officer utterance:
- guilt-presumptive or neutral;
- open, closed or leading;
- whether it followed up Cory's account, or ignored it and repeated the allegation.

**Result (`OFFICER_QUESTION_CODING.md`):**
- 30% of officer turns explored his point, 23% used his words to contest him, and 47% did not engage it.
- None of the 10 evidence offers he made was taken up when he made it.
- They heard him: word uptake was 4.8 times chance. What they followed up was selective.

## Limits
- **Body-worn camera:** the camera was on one officer, so posture or distance changes could lower both
  officers' recorded level. It cannot explain your level rising on the same microphone.
- **Officer separation:** the two officers are separated by pitch only (no separate microphones).
- **Content:** coded separately in `OFFICER_QUESTION_CODING.md`. The transcript stays outside the repo, and
  transcript and audio align to about ±2 s.
