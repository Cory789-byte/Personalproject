# Brisbane Magistrates Court, 2 February 2026 — trial stood down (QPS prosecution)

> ⛔ **QPS track / personal file only.** Never voiced, cited or attached in WC/2024/227 or the
> employment track (discipline rule 10). ⚠ **MACHINE-GENERATED — UNVERIFIED.** Not a certified
> transcript; order one from the court before quoting anywhere. Proceedings connected with domestic and
> family violence matters can carry publication restrictions in Queensland: private analysis only.

| | |
|---|---|
| Source | `PRF0447826_20260202_MAG-DJAG_Brisbane-Magistra_SHEPHERDCORYLEAMR__AudioofProceeding_Standard_1.mp3` (audio of proceeding supplied by the court) |
| SHA-256 | `1a8c9bf6d72f691deb4a8ae10179eaa769e2dd9fa6b66c02cbbb75827feebcb4` |
| Duration | 586.0 s (9 min 46 s), MP3 128 kbps, 48 kHz stereo |
| Audio | **Not committed** (recording of a proceeding; same rule as the 7 Aug 2026 mention audio). Kept in the owner's storage |
| Transcript | faster-whisper **large-v3**, int8 CPU, beam 5, word timestamps + per-word probabilities, VAD (`data/whisper_large-v3_segments.jsonl`) |
| Speakers | ECAPA-TDNN (speechbrain spkrec-ecapa-voxceleb), mean-normalised; k = 2…6 tried; **k = 3 best** (silhouette 0.42; three k3 methods agree 94–97%) |
| Prosody | Praat via parselmouth, per segment and per corrected split: f0 median, intensity mean, robust f0 range (p5–p95, semitones), words/s |

**Speakers.** MAGISTRATE (f0 median 181 Hz) · PROSECUTOR, Mr D. A. Hodgetts, QPS (127 Hz) · SHEPHERD (134 Hz).
Identified on content (the prosecutor announces himself at 00:01; "Your Honour"; "my application").

**Markers** (same vocabulary as the mention transcript, always relative to *that speaker's own* recording medians):
`↑/↓ Nst` pitch ≥2 semitones from own median · `wide/flat` f0 range above own p75 / below own p25 ·
`fast/slow N w/s` above p75 / below p25 · `louder/quieter` above p75 / below p25 dB · `(N s pause)` silence ≥2 s ·
⚑ = the turn contains a word Whisper scored below 0.5.
Absolute dB is **not** comparable with the mention or the interview (different recording system; this file's
median level is ~54 dB against ~62–66 dB at the mention).

## Amendment log (speaker attribution)

ECAPA labels whole segments; 13 segments ran two speakers together and were split at word boundaries,
each side confirmed by its own pitch; six short or mislabelled segments were assigned. Every change:

- seg 0 words 0-1 -> MAGISTRATE (pitch 214 Hz; calls the prosecutor)
- seg 0 words 2-19 -> PROSECUTOR
- seg 6 words 0-4 -> MAGISTRATE (pitch 166 Hz)
- seg 6 words 5-8 -> SHEPHERD (repeats his answer)
- seg 8 words 0-8 -> SHEPHERD
- seg 8 words 9-11 -> MAGISTRATE (pitch 202 Hz; question)
- seg 9 words 0-4 -> MAGISTRATE (pitch 177 Hz)
- seg 9 words 5-10 -> SHEPHERD (answer)
- seg 20 -> PROSECUTOR (time of the email; pitch 126 Hz)
- seg 21 -> PROSECUTOR (time of the email (context))
- seg 27 words 0-0 -> MAGISTRATE (pitch 200 Hz)
- seg 27 words 1-15 -> SHEPHERD
- seg 49 -> MAGISTRATE (pitch 209 Hz)
- seg 50 -> SHEPHERD (ECAPA said Magistrate; pitch 129 Hz and content (answers 'Which bit?'))
- seg 53 words 0-2 -> MAGISTRATE (pitch 176 Hz; ends her sentence)
- seg 53 words 3-16 -> PROSECUTOR (pitch 130 Hz)
- seg 55 words 0-5 -> MAGISTRATE (pitch 195 Hz; interjection)
- seg 55 words 6-16 -> PROSECUTOR (pitch 124 Hz)
- seg 61 words 0-3 -> PROSECUTOR (pitch 126 Hz)
- seg 61 words 4-14 -> SHEPHERD (continues into 'medications in my list' (136 Hz); pitch here 128 Hz, ambiguous)
- seg 62 words 0-4 -> SHEPHERD (pitch 136 Hz)
- seg 62 words 5-13 -> MAGISTRATE (pitch 175 Hz)
- seg 89 words 0-4 -> MAGISTRATE (pitch 189 Hz; question)
- seg 89 words 5-14 -> PROSECUTOR (pitch 133 Hz; answer)
- seg 90 words 0-8 -> PROSECUTOR (pitch 119 Hz)
- seg 90 words 9-17 -> MAGISTRATE (pitch 212 Hz)
- seg 95 words 0-0 -> PROSECUTOR (end of 'outside')
- seg 95 words 1-3 -> MAGISTRATE (pitch 178 Hz)
- seg 97 words 0-5 -> MAGISTRATE (pitch 201 Hz)
- seg 97 words 6-6 -> SHEPHERD (pitch 152 Hz; 'Exactly.')
- seg 122 -> MAGISTRATE (too short to embed; pitch 183 Hz matches the Magistrate (flagged))
- seg 132 -> UNATTRIBUTED (too short to embed; pitch 105 Hz)

## Likely mishearings (shown inline in brackets)

"Scottsdale" → *Scott schedule?* · "VIX" → *Vicks* · "NATO complaint" → *NATA?* (the laboratory accreditation body) ·
"Prince Sergeant" → *? Sergeant* · "Mr Hodges" → *Mr Hodgetts* · "between a horse and a car" → *? horse and cart* ·
"with the women they can get a check" → *unclear* · "mr here" → *unclear*. None has been re-decoded; treat them as unresolved.

---

## Transcript

**00:00.02  MAGISTRATE**  `↑+2.8st slow 2.04w/s louder`  ·  1.0s  f0 214 Hz  56.1 dB
> Mr Hodgetts?

**00:01.06  PROSECUTOR**  `fast 3.72w/s louder`  ·  7.1s  f0 121 Hz  56.8 dB  ⚑low-confidence word
> Yes, if it pleases the court, Your Honour, Hodgetts, spelled H -O -D -G -E -T -T -S, initials D-A, prosecutor on behalf of Queensland Police.

**00:09.86  MAGISTRATE**  `slow 2.37w/s quieter`  ·  19.8s  f0 174 Hz  51.7 dB  ⚑low-confidence word
> Okay, so as far as there are two separate things that I can work out from this, there seems to be an issue, oops, there's the actual trial in relation to this charge and there's also your application for a permanent stay of proceedings, is that correct?

**00:29.99  SHEPHERD**  `wide slow 2.07w/s quieter`  ·  3.9s  f0 134 Hz  48.0 dB
> That's correct. I did a Scottsdale [Scott schedule?]

**00:33.86  MAGISTRATE**  ·  1.6s  f0 166 Hz  52.7 dB  ⚑low-confidence word
> Sorry, I can't hear you.

**00:36.14  SHEPHERD**  `↓-2.3st wide`  ·  8.5s  f0 117 Hz  53.8 dB  ⚑low-confidence word
> I did a Scottsdale [Scott schedule?] thing which lists all the issues with the charges. It's only two pages, it's a better summary.

**00:44.80  MAGISTRATE**  ·  2.1s  f0 187 Hz  54.3 dB
> Is it different from all this other stuff?

**00:47.02  SHEPHERD**  `wide`  ·  7.5s  f0 136 Hz  53.1 dB  ⚑low-confidence word
> It summarises everything in three pages. It's very small. but if you would like to

**00:54.48  MAGISTRATE**  `quieter`  ·  6.5s  f0 177 Hz  52.3 dB  ⚑low-confidence word
> If you have three pages of tiny print and it doesn't actually add anything new I'm not that interested. Have you had a look at it?

**01:01.66  PROSECUTOR**  `fast 3.75w/s`  ·  3.2s  f0 123 Hz  55.1 dB  ⚑low-confidence word
> Oh I haven't been I haven't had any material given to me

            *(2.4s pause)*

**01:07.30  PROSECUTOR**  `wide louder`  ·  4.0s  f0 131 Hz  58.4 dB
> Apologies Your Honour I haven't received I received an email at

            *(2.6s pause)*

**01:13.89  PROSECUTOR**  `slow 1.92w/s quieter`  ·  2.0s  f0 126 Hz  47.5 dB
> 11 20

            *(6.9s pause)*

**01:22.83  PROSECUTOR**  ·  6.3s  f0 120 Hz  54.9 dB  ⚑low-confidence word
> 11 25 and I haven't had enough time to go through all of it

**01:29.16  MAGISTRATE**  `↓-2.1st wide quieter`  ·  1.7s  f0 160 Hz  51.2 dB  ⚑low-confidence word
> I'm not surprised. Sorry,

            *(2.6s pause)*

**01:33.46  SHEPHERD**  ·  15.4s  f0 132 Hz  53.6 dB
> it's pretty much the same as my entire application, but I understood the Vicks, so there's no reason why there should be methamphetamine on my laboratory result, because Vicks Australian brand does not have anything to do with meth. Vicks in America does.

**01:49.98  MAGISTRATE**  `wide fast 4.52w/s`  ·  3.1s  f0 179 Hz  53.7 dB
> So that's not what's in your other material, so that was on the big...

**01:53.08  SHEPHERD**  `fast 3.71w/s`  ·  10.7s  f0 138 Hz  53.9 dB
> I was just updating that one factor. All the other factors are the same, except that I found out that that has... So there's no reason why I should have had a positive result unless that is not mine.

            *(3.9s pause)*

**02:07.69  MAGISTRATE**  `flat slow 1.3w/s quieter`  ·  9.2s  f0 191 Hz  47.4 dB
> Okay, so are we going to go ahead with the trial today?

**02:17.60  SHEPHERD**  `wide`  ·  3.4s  f0 135 Hz  54.7 dB
> I requested an adjournment on the 20th, the 22nd.

**02:20.98  MAGISTRATE**  `wide`  ·  1.2s  f0 175 Hz  54.7 dB
> Yes, I read those emails.

**02:22.58  SHEPHERD**  `slow 2.24w/s quieter`  ·  8.2s  f0 126 Hz  50.9 dB  ⚑low-confidence word
> But the prosecutor said no. I have requested a stay, so a stay or adjournment and a stay.

**02:30.74  MAGISTRATE**  `wide`  ·  8.1s  f0 173 Hz  52.8 dB  ⚑low-confidence word
> But your basic argument for the stay is in relation to the US VIX [Vicks] as opposed to the Australian VIX [Vicks], isn't it?

**02:39.82  SHEPHERD**  `fast 3.45w/s louder`  ·  12.3s  f0 144 Hz  55.8 dB
> Yeah, obviously. And that, I wasn't driving. The other, the sergeant, his statement's not even there. He's the only one that drove my car, and his statement's not even in there. His body-worn camera's not in there.

**02:52.40  MAGISTRATE**  `wide slow 2.64w/s quieter`  ·  19.7s  f0 170 Hz  52.4 dB  ⚑low-confidence word
> They're things to bring up on the trial rather than the stay proceedings. Well, I don't know. My initial feeling is the fact that your grounds for stay, I think, is the fact that it's in relation to the destruction of a sample of the consumption or whatever they were consumed of.

**03:12.12  SHEPHERD**  ·  6.9s  f0 129 Hz  53.2 dB  ⚑low-confidence word
> Well, that and the prosecutors are not giving over material. I've been asking it since last year, July or September.

**03:19.30  MAGISTRATE**  `↑+2.5st fast 4.35w/s`  ·  0.5s  f0 209 Hz  53.6 dB
> Which bit?

**03:20.06  SHEPHERD**  `wide`  ·  29.9s  f0 136 Hz  54.7 dB  ⚑low-confidence word
> The statement of the Prince Sergeant [?… Sergeant]. Well obviously they haven't, they've only verbally told me it was destroyed, so they've only verbally, this man told me verbally it was destroyed, however I've requested that material again and again and again, so for me it's an abuse, I mean you're saying, so the law is that you will present, if I ask for the saliva to test you'll be able to do it, I'll be able to see, that restricted me and I've asked for it and asked for it and they just ignore me.

**03:49.96  MAGISTRATE**  `slow 1.01w/s quieter`  ·  17.8s  f0 167 Hz  47.9 dB  ⚑low-confidence word
> yeah so basically so you've only just had the verbal confirmation that sample correct the sample was destroyed

**04:07.72  PROSECUTOR**  `quieter`  ·  13.1s  f0 123 Hz  53.5 dB  ⚑low-confidence word
> so maybe mr here [?…] i can probably assist in in this and noting that all of this will be addressed in the trial there hasn't been any destruction of any sample

**04:20.81  MAGISTRATE**  `wide`  ·  1.8s  f0 195 Hz  53.4 dB
> why was he told there was

**04:22.65  PROSECUTOR**  `slow 2.07w/s`  ·  42.0s  f0 124 Hz  54.6 dB  ⚑low-confidence word
> i can't speak on behalf of and i don't have any evidence or information to suggest otherwise. The roadside random drug test, which is the lollipop, that in of itself, when it gets used for the testing, once it's finalised and the witness from Queensland Health that I intend on calling will be able to speak to that the secondary test which is done the saliva analysis test which is done at the police station after roadside that hasn't been destroyed there's still that sample still exists

**05:04.63  SHEPHERD**  `slow 2.06w/s quieter`  ·  7.8s  f0 131 Hz  52.1 dB  ⚑low-confidence word
> that's why we want to figure out because I have four medications in my list vitamins

**05:12.40  MAGISTRATE**  `louder`  ·  11.8s  f0 191 Hz  56.2 dB  ⚑low-confidence word
> which this is why we're not going into the nitty-gritty here because we're just working out what we're doing today what What I'm interested... So, did you know there was still a sample still existing?

**05:24.60  SHEPHERD**  `↑+2.9st flat quieter`  ·  2.6s  f0 158 Hz  52.3 dB
> So, is there a sample still existing?

**05:27.52  MAGISTRATE**  `↑+3.4st flat fast 5.81w/s`  ·  0.9s  f0 220 Hz  54.1 dB
> He just said there was.

**05:29.06  SHEPHERD**  `flat quieter`  ·  1.4s  f0 122 Hz  48.3 dB
> I just wanted clarification.

**05:31.30  PROSECUTOR**  ·  28.8s  f0 123 Hz  56.5 dB  ⚑low-confidence word
> As I've just disclosed to the court, the sample still exists. The prosecution witness will attest to that. In any case, I think what... And this will be for the court to decide. I think it may be a case between a horse and a car [?horse and cart] in that the... and this will be made apparent with my evidence, the defendant was offered, on a number of occasions, his statutory right to take a secondary sample.

**06:01.00  MAGISTRATE**  `slow 2.35w/s`  ·  13.9s  f0 176 Hz  53.0 dB  ⚑low-confidence word
> In his material, he says basically that he just said whatever the... The body-worn camera footage reveals that he didn't refuse in the sense that he... I can't remember the word.

**06:15.10  SHEPHERD**  `fast 9.8w/s louder`  ·  1.0s  f0 140 Hz  57.6 dB  ⚑low-confidence word
> I've got it here for you if you want to...

**06:16.12  MAGISTRATE**  `wide louder`  ·  5.0s  f0 186 Hz  56.5 dB  ⚑low-confidence word
> Basically that he's happy to take, you know, it'll all come out when the analysis...

**06:22.21  PROSECUTOR**  ·  31.1s  f0 124 Hz  55.1 dB  ⚑low-confidence word
> Yes, Your Honour, I've reviewed that correspondence from the defendant. I've also reviewed the body-worn camera footage on a number of occasions. And it will be my position that that, which will be for the court to decide that. The information the defendant has raised in his written correspondence to prosecution execution is not prima facie what happens in the body-worn camera. It will be for the court to decide. I've got it here if you'd like to hear it. If we go ahead with the trial

**06:53.29  MAGISTRATE**  `slow 2.39w/s louder`  ·  9.6s  f0 181 Hz  55.9 dB  ⚑low-confidence word
> yes it will be relevant but at this stage it's what we do today. Is it possible to get that remaining sample retested?

**07:03.25  PROSECUTOR**  `quieter`  ·  7.2s  f0 125 Hz  50.9 dB
> I can't speak to that Your Honour. It's not something that I'm able to inform the court. It's not.

**07:10.68  MAGISTRATE**  ·  23.7s  f0 182 Hz  54.6 dB  ⚑low-confidence word
> Well he was told there was no viable sample. There was no sample left and the only sample that even though there was enough quantity of material was all consumed in the testing and it was destroyed. And one of his issues is the possible, you know, meant to keep it for six months and stuff. But how does he go about getting, if there is another sample, how does he get that tested?

**07:35.00  PROSECUTOR**  `wide`  ·  5.6s  f0 132 Hz  56.5 dB
> If you could indulge me, I can ask the lab technician who's sitting outside. side.

**07:42.47  MAGISTRATE**  ·  4.4s  f0 196 Hz  53.5 dB
> Yeah, I think that's relevant. Is that what you want to do, is get that tested?

**07:47.03  SHEPHERD**  `louder`  ·  4.6s  f0 137 Hz  55.8 dB
> Exactly. And I also got a NATO [NATA?] complaint that I did send off.

**07:51.83  MAGISTRATE**  `fast 5.56w/s`  ·  1.6s  f0 168 Hz  54.5 dB
> I don't know what a NATO [NATA?] complaint is.

**07:53.47  SHEPHERD**  `slow 2.01w/s`  ·  7.5s  f0 131 Hz  53.5 dB
> It's who oversees the forensic analysis about the destruction. They also have to provide a...

**08:00.93  MAGISTRATE**  ·  5.9s  f0 180 Hz  54.0 dB
> I know there's lots of issues in relation to the storage and all that, but if you could find out, Mr Hodges [Mr Hodgetts].

**08:07.13  PROSECUTOR**  ·  29.9s  f0 137 Hz  56.5 dB  ⚑low-confidence word
> I can do that. I guess the primary issue that we face here, and we'll come out if we go to trial is, prosecution's evidence indicates, it's my position, prosecution evidence indicates that the defendant was provided with the opportunity to take a B sample. He has not taken police up on that offer and now months down the track when we're two and a half hours past nine o'clock on the day of the trial.

**08:37.12  MAGISTRATE**  `↑+2.7st wide`  ·  2.7s  f0 212 Hz  55.8 dB  ⚑low-confidence word
> And he was first raised this back in September in emails.

**08:40.03  PROSECUTOR**  `wide louder`  ·  15.4s  f0 134 Hz  56.9 dB  ⚑low-confidence word
> The position that prosecution holds is that the defendant had the opportunity, he was given his statutory right on the evening or the early hours of the morning of the test and chose not to take up that option.

**08:55.69  MAGISTRATE**  `quieter`  ·  1.1s  f0 190 Hz  52.2 dB
> Which is contested.

**08:57.40  PROSECUTOR**  `wide`  ·  4.2s  f0 119 Hz  56.4 dB
> Which is contested and it would be for the court to determine.

**09:01.58  SHEPHERD**  `wide louder`  ·  10.2s  f0 135 Hz  55.2 dB  ⚑low-confidence word
> I raise a concern. I believe this is about them stealing my dog in a court across on Southport that's been going on for about a year and a half.

**09:12.04  MAGISTRATE**  `wide louder`  ·  3.6s  f0 176 Hz  56.9 dB
> These are the complaints to police you said that was part of the profiling.

**09:15.72  SHEPHERD**  `louder`  ·  5.4s  f0 145 Hz  55.3 dB
> Exactly. So they've targeted me and now they can't even give me my evidence.

**09:23.00  MAGISTRATE**  ·  21.6s  f0 182 Hz  54.2 dB  ⚑low-confidence word
> I'm going to stand it down while Mr Hodgetts finds out whether you can get with the women they can get a check [?… can get a check] process or whatever. That's right. This existed. So we didn't know until just this minute that there was a viable material when he's been told to the contrary, there's none. So that's what it's about. So we'll stand down while you find that out. How long do you think? Five, ten minutes?

**09:44.84  PROSECUTOR**  `↓-2.2st flat fast 6.45w/s`  ·  0.6s  f0 112 Hz  56.6 dB
> Ten minutes, thank you.

**09:45.46  UNATTRIBUTED**  ·  0.2s  f0 105 Hz  55.2 dB
> Okay.
