# WC/2024/227 — MENTION OF 7 AUGUST 2026 — DIARISED TRANSCRIPT WITH PROSODY

**Source.** `PRF0466309_20260807_QIRCOIR_Brisbane` — audio of proceeding, 64 kbps MP3,
3,875.9 s (64 min 36 s). The recording **begins mid-sentence**, already inside the Commissioner's
opening remarks; the appearance announcements are not on the tape.

**Method.** Decoded to 16 kHz mono; high-pass 70 Hz, low-pass 7.6 kHz, 1-second-window AGC, soft
limiter, normalised to −3 dBFS. Transcribed with **Whisper large-v3** (CTranslate2 int8, beam 5,
temperature fallback, word-level timestamps, Silero VAD, domain-primed initial prompt), split at
silence into four chunks decoded in parallel. **1,068 segments; mean segment log-probability
−0.180; zero segments below the −0.6 low-confidence threshold.**

Diarisation: Resemblyzer GE2E embeddings over 1.5 s windows at 0.75 s hop **computed on the
un-normalised audio** (the AGC erases the 12 dB mic-distance difference between the bench and the
bar table, which is the strongest speaker cue in the room), reduced by PCA to 32 dimensions and
combined with segment level, spectral centroid and spectral tilt. Because both principal speakers
are men sharing a median F0 of 136 Hz on one distant microphone, acoustics alone could not separate
them; the assignment is therefore **inferential**, decided by Viterbi over three evidence streams:

1. **Acoustic** — distance to speaker centroids seeded from utterances only one person could have
   made ("the appellant" read from the pleading; "my manager", "my colleagues", "I was rostered").
2. **Lexical** — ~60 weighted patterns. Reading the pleading aloud, naming the parties, judicial
   first person and second-person reference to "your case" mark the bench; first-person reference to
   his own employment, bare answers and "Commissioner" mark the Appellant.
3. **Adjacency** — a question invites the other voice (switch penalty x0.15 after "?"); certain
   openings prove the *previous* segment was the other speaker ("Hand it up" answers an offer;
   a bare "Yes" answers a question). Long silence makes switching cheap.

**Validated against 30 hand-checked anchor turns cross-referenced with the independent small.en
transcript: 27/30 correct (90%).**

Prosody: Praat (via parselmouth) F0 and intensity per segment.

⚠ **RELIABILITY.** The transcription is high-confidence (mean log-probability −0.180, nothing below
−0.59). **The speaker labels are inferred, not certified — measured at 90% on hand-checked anchors.**
Long turns and question-answer exchanges are reliable. The residual errors are concentrated in
one- and two-word interjections and in overlapping speech. ⛔ **Order the certified transcript
before any passage is quoted externally.**

## ⛔ SPEAKER CORRECTIONS APPLIED — 12 SEPTEMBER 2026
The Viterbi assignment below is **inferential** and its known failure mode is a short acknowledgement
inside a long run: the diariser gives the backchannel to whoever holds the floor. Eleven segments were
re-examined; **ten are corrected**, one is confirmed as originally labelled. Corrections are listed here
rather than rewritten into the body so that the original machine output remains auditable.

| Seg | Time | Labelled | **Corrected to** | Basis | Confidence |
|---|---|---|---|---|---|
| **437** | 30:13 | DWYER IC | **MR SHEPHERD** | *"Yeah, I actually understand what you're getting at."* Spliced into the middle of one Dwyer sentence that runs 432→436→438→439 (*"…at the other end of the table. … If we can't get to that,"*). **Confirmed first-hand by the Appellant, who was present.** | **Certain** |
| 440 | 30:19 | DWYER IC | **MR SHEPHERD** | *"Yeah."* Bare backchannel inside the same 471-word run | High |
| 620 | 40:28 | DWYER IC | **MR SHEPHERD** | *"Yes."* answers *"Is it in the form of an email? Yes or no?"* — the bench does not ask and answer, then ask again | High |
| 673 | 42:59 | DWYER IC | **MR SHEPHERD** | *"Yeah."* interrupts Dwyer's own sentence (*"…put to Ms. Taylor … and you don't need any other documents"*) | High |
| 792 | 49:53 | DWYER IC | **MR SHEPHERD** | *"Yeah."* answers *"So they didn't have coverage of that workplace?"* | High |
| 623 | 40:30 | MR SHEPHERD | **DWYER IC** | *"All right."* acknowledges the Appellant's *"No, I do not."* immediately before the bench turns to Ms Matheson | High |
| 1008 | 61:37 | MR SHEPHERD | **MS MATHESON** | *"No."* answers *"Have I misrepresented your role in the matter or placed a burden on you that you're not prepared to accept?"* — a question addressed to Ms Matheson | High |
| 1009 | 61:38 | MR SHEPHERD | **DWYER IC** | *"All right."* immediately precedes *"And Ms. Rutland, any?"* | High |
| 627 | 40:36 | MR SHEPHERD | **MS MATHESON** | *"I do believe we have those"* — answers *"Ms. Matheson, have you got that email?"*; seg 626 is already hers | High |
| 628 | 40:41 | MR SHEPHERD | **MS MATHESON** | *"and I do believe we've disclosed them."* — **"we've disclosed them" is the Regulator's voice** | High |
| 231–232 | 17:45 | SHEPHERD / DWYER | **one speaker, probably MS MATHESON** | *"There has been some emails to involve the quality of the staff, but I have to probably / consider that."* is **a single clause split across two labels** and cannot be two people. It answers a question put to Ms Matheson | ⚠ Uncertain |
| 908 | 55:53 | DWYER IC | **no change** | *"Okay."* is the bench's own marker between pleaded items he is reading aloud — the same *"Okay. All right."* pattern he uses throughout | Confirmed |

**Effect on the share table below:** Ms Matheson spoke at least **six** times, not three; the Appellant's
count rises by four short turns and falls by four; the Commissioner's share is overstated by roughly
30 words. The 86% / 14% split is not materially altered.

⚠ **The substantive analysis is unaffected**: no conflict was found between content markers and speaker
labels on any long turn (0 of 1,068 segments). Every correction is in a turn of ten words or fewer, except
627–628.

## SPEAKING SHARE
| Speaker | Segments | Talk time | Share |
|---|---|---|---|
| Commissioner Dwyer | 846 | 2,949 s (49m 09s) | **86.2%** |
| Mr Shepherd | 219 | 466 s (7m 46s) | **13.6%** |
| Ms Matheson | 3 | 7 s | 0.2% |
| Ms Ruttan | 0 | 0 s | 0.0% |

**Turn changes: 202.**

## PROSODIC MARKERS
Markers are **relative to each speaker's own baseline**, not to each other.
`↑/↓ Nst` pitch shift in semitones · `wide`/`flat` F0 range · `fast`/`slow` speech rate ·
`louder`/`quieter` intensity · *(N.Ns pause)* silence before the turn.

---

**00:00.00  DWYER IC**  
Not just for your interests, but for the efficient administration of justice, which is an overriding consideration that I've got my eye on.
And so what I mean by that is that I will endeavour to progress matters as quickly and efficiently as they possibly can be progressed
in a way that does not compromise or prejudice people's rights
in respect of their case.  `flat`
And to that end, oftentimes that involves me
directing certain things to happen  `wide`
or declining to allow certain things to happen.
And in particular, there is from time to time
a tendency to proliferate interlocutory disputes, which delay and complicate the overall resolution  `slow 0.8w/s`
of a matter. Disclosure disputes can oftentimes be exactly that. They can be an unnecessary
and unnecessary distraction that impacts the efficiency
of the conduct of proceedings.

            *(3.1s pause)*
Without specifically being critical of the matters
that you are pursuing, in broad terms,
there are a number of aspects to the application
that you brought that I think are potentially going
to impact on the efficiency of the conduct of your proceedings.
And so one of the things I hope to achieve in our discussions today, in our discussion  `wide`
about the matter today, is a different approach that will leave you satisfied that you are
not in any way at all compromised in the conduct of your proceedings and that this matter can  `flat`
get to hearing, which I would assume is your objective and you would like to be at a hearing
and you would like to have the question of whether you have sustained a workplace injury  `flat`
resolved sooner rather than later and I want that for you too and I want that
for all the parties and I want that for the people of Queensland who are
resourcing these proceedings. I just want to take it back to first principles okay  `wide quieter`
so that we know where we're at. I'm going to park the non-party disclosure  `wide quieter`
application for the moment. I'm going to take you back to your statement of facts
and contentions. In fact, I'll take you back one step further than that. In general terms,  `quieter`
as an appellant in proceedings of this type, you have the onus of proving that you have
sustained an injury within the meaning of section 32 of the workers' compensation legislation.  `flat`
legislation. Personal injury arising out of or in the course of your employment where
your employment is a significant contributing factor, not excluded by the provisions of
Section 32.5, reasonable management action taken in a reasonable way.  `↓-2.1st flat`
You have placed before the Commission a statement, an amended statement of facts in contentions  `wide`
and the amended statement of facts and contentions is the framework of your case.
It's a hearing de novo, as you know.  `flat fast 5.0w/s`
It's the framework of your case and it tells the commission
and it tells the respondent why you say you meet the requirements
in respect of Section 32 and not excluded by Section 32.5.
And in particular, you identify what are the stressors that you say are causative of your injury.
As in most of these cases, the presence or existence of an injury for the purposes of a medical diagnosis is usually not so much in dispute.
dispute. So the real crux of your case is going to be to show that if you have a diagnosis
of a psychiatric condition as you do in this particular case, how certain events or things
that took place in your workplace caused that, were significant contributors to the cause
cause of that condition. Now, in your case, you have identified multiple stressors. You  `wide slow 1.1w/s`
have broken them down into categories of one, two, three, three different categories and
you have broken them down into subcategories under each one of those categories. It's going  `wide`
going to take us a little bit of time this morning, but I'm hoping that this time in  `fast 5.1w/s`
me stepping you through these things will put in perspective what types of things will  `wide`
be relevant to you, are likely to be relevant to you, in proving your case. And in explaining
that to you, explaining also what types of things are not relevant to the proving of
of your case. And I fully appreciate as a person who's not represented, you may have
some difficulty differentiating between relevant and irrelevant. And in fact, it's not at all
uncommon to find an unrepresented person with an intense focus on proving certain things
that are ultimately, from an objective legal perspective, utterly irrelevant. And it has  `wide quieter`
been my experience throughout my career that sometimes people in that situation are very
very unwillingly disavowed of that view. But that's what I'm going to attempt to do this  `flat`
morning in terms of stepping through your case and your pleaded stressors and giving  `quieter`
you examples of how those stressors, how you would address the evidentiary burden in relation
to those stressors and how, for example, that has
nothing to do with a number of the documents that you are seeking
from the health service. Okay, so that's just to set the  `quieter`
scene in terms of where we're going. Do you have any questions or difficulties understanding all of that  `flat`
at the moment? No, I mean, you're  `quieter`
telling me, so I'm not experienced in it, but I just did what I understood.  `flat quieter`
That's okay. I want to stress, I'm not  `↑+4.1st`
I'm not being critical of you, Mr Shepherd, but I also need to be very firm in terms of
explaining these things to you so that I impress upon you the concern I have with respect to  `flat`
how this impacts the efficient conduct of the proceedings.  `flat`

**07:09.36  MR SHEPHERD**  `wide`  
I understand, I think I understand, what you think you are trying to achieve and I'm not

**07:17.78  DWYER IC**  `↑+2.1st`  
saying you are entirely wrong and the thing with disclosure is that if
someone's willing to give you some documents you've asked for and they  `wide`

**07:25.32  MR SHEPHERD**  
don't have any problem with it that's fine I don't have a problem with that

**07:29.24  DWYER IC**  
they can give you whatever they want back in the day it was a fairly standard
tactic in more commercial types of litigation rather than resist disclosure
to send 78 boxes of disclosure to somebody and bury them in paperwork
work. So if the health service wants to give you  `wide`
a truckload of documents for you to sift through, you won't ever get into hearing
until 2028 by the time you've worked through all of that.
And then you've got to run the gauntlet of whether or not those documents
are accepted by the commission into evidence because of their  `flat`
relevance. So it's one thing to get the documents, it's another thing to get the documents into
evidence. So that's the challenges you face in respect of a document
document heavy case is that even if some third party is compelled to or voluntarily provides
you with three boxes of documents that go to how many complaints were made by doctors  `flat`
as to whether the calls were sent to the right person or whatever, all of that, then it still
becomes a question of whether or not that's relevant to your case in respect of the matters
that you've pleaded as stressors.  `flat`

**08:36.40  MR SHEPHERD**  `flat`  
Well, for me, it wasn't so much.
I didn't really matter what's inside those complaints.  `flat`
it's that they happen to me, if that makes sense.  `flat`
So that was my point.  `↓-2.0st flat fast 4.9w/s`
But I wouldn't even need to read them.  `flat`
Okay.  `flat`

**08:50.02  DWYER IC**  
Well, perhaps you can explain that to me a bit more clearly
because I must confess,

            *(2.8s pause)*
having read the material that you've filed,  `wide`
it's pretty heavy-going stuff.  `wide`
Is it AI-assisted, can I ask?  `↑+4.1st`
Because it feels like it.

**09:06.78  MR SHEPHERD**  `flat`  
Just to the end.
I do it all myself.  `flat fast 5.4w/s`
well  `quieter`

**09:11.52  DWYER IC**  `wide`  
it feels very AI
assisted, now
that allegation is thrown around a lot these  `flat`

**09:18.16  MR SHEPHERD**  `flat`  
days
and

**09:22.08  DWYER IC**  `flat`  
often times correctly
I don't purport to be an expert in what's
AI or what's not AI  `flat`
but when I read stuff and I start
to see terms and language and  `flat`
complexities of language  `flat`
that go above and beyond what  `flat`
you'd anticipate from a human being  `flat`
even a very intelligent human being
I immediately get suspicious about it
and AI is
look, everyone's got a view about it
you can do what you like
but I don't respond very well to it  `wide`
my brain doesn't respond very well to it  `flat`
because I can't understand half of what I'm reading  `flat fast 5.1w/s`
it is genuinely incomprehensible  `slow 1.0w/s`
in some cases
and it's not that a sentence doesn't necessarily make sense
it just doesn't necessarily make sense in the context of what we're doing here and it's
not the most efficient way to communicate your point. The old system of keep it short
and sweet, keep it simple. If you want to persuade a court of something, a simple message
is always the best. People make the mistake. I've got to have a big case because then it
looks more important. You don't have to.  `quieter`

**10:32.36  MR SHEPHERD**  
I mean for me it happened over a whole year
so it's not just one shift  `flat`

**10:39.24  DWYER IC**  
let me step you through your stressors
so I'm looking at your statement of facts and contentions  `wide quieter`
now this is the document  `↑+3.1st`
that ultimately in an argument like this around disclosure
this is the document that will inform
and determine really what's relevant  `slow 1.3w/s`
and I'm inclined to take a broad approach
in terms of things of relevance.
You know, if something might ultimately be relevant
in a peripheral way, OK,  `slow 1.2w/s quieter`
well, I won't have an issue with that necessarily.
What I'm going to do is, as I said,  `↑+2.3st fast 5.8w/s`
I'm going to step you through these stressors  `fast 5.3w/s`
and I'm going to hypothetically lay out for you
to the extent that I can to demonstrate to you,  `wide`
OK, well, this is what you are claiming.  `fast 5.2w/s`
claiming, how would you go about proving this? And that then hopefully will give you a clearer
idea of what is necessary, what's relevant, what kind of documents might be relevant.
Okay, I'll just get it underway because otherwise we'll be talking till this afternoon.
So I'm looking at, under the heading, the causative stressors. And I'm looking at category
Category stressor one, a hostile course of management conduct, reprisal and suppression of rights.
Number one, dereliction of, sorry, I should just say, anybody got any objections to me going through this process?
It's going to take a little while, but hopefully it'll save us some time and effort down the track.

            *(4.5s pause)*
Dereliction of clinical governance.  `↑+2.4st louder`
Throughout 2023 and 2024, the appellant's line manager, Ms Chloe Taylor, maintained an erratic physical presence and imposed unassessed unilateral directives, either extra-administrative checks paging, without consultation.
These arbitrary directives bottlenecked emergency workflows and directly caused verifiable delays to the communication of urgent pathology results to clinical staff.  `wide`
The appellant's responsible attempts to mitigate these clinical risks triggered the manager's subsequent hostility.  `wide`
Okay, I'll break it down.  `quieter`
Ms Chloe Taylor maintained an erratic physical presence
how do you propose to prove that  `wide`
other than your own testimony
you'll get in that witness box
and you'll say Chloe Taylor had an erratic presence
what do you mean by that
she was sometimes there, sometimes not there  `flat`

**13:28.66  MR SHEPHERD**  
correct and that's what I guess
access to the room
I don't even need to look at them  `flat fast 4.8w/s`
But access to the hospital itself would tend to prove, or log in to the computer, if she's there or not.
That's what I was tending to prove for that.  `flat`
But it's not, for me it all works together as one big system.
So yeah, the data of her coming in and going, and then the data of her logging into the computer as such,
would show that, you know, people would...
I think I attached one attachment  `flat`
and it showed that she didn't reply to a complaint about...
No, hang on a sec.  `↑+3.1st fast 5.4w/s louder`
Sorry.  `flat`

**14:13.96  DWYER IC**  `↑+3.7st slow 1.3w/s quieter`  
So her erratic physical presence
is something that you can give testimony about.
And I don't want you to do that now,  `flat fast 5.8w/s`
which is what you're launching into.  `flat`
But so one way you'll prove that
is that I worked there between 2023 and 2024.
in my observation, Chloe Taylor had an erratic presence.
What do you mean by that, Mr Sheppard?
Well, she was there some days, she was there not some days.  `wide`
She showed up in the morning and left in the afternoon.  `flat fast 5.8w/s`
She was there in the afternoon but not in the morning.  `fast 5.8w/s`
Is that what you mean by erratic presence?  `wide`

**14:48.62  MR SHEPHERD**  `wide`  
Exactly.

**14:49.42  DWYER IC**  `↑+2.9st`  
Okay, so you can give that evidence.
And it's for the regulator to contradict that.
If that's your evidence and you put it here
in your statement of facts and contentions.  `flat`
And no doubt, at some point,
I'm not sure whether we've got to the exchange of outlines of evidence,
but that's your evidence.
She had an erratic presence.  `flat`
That was based on your observation.  `flat fast 4.8w/s`
That's your evidence.  `flat`
If the regulator wants to dispute that, they can dispute it.  `wide`
No doubt they may have Ms Taylor on their witness list or not.

            *(2.2s pause)*
It's often thrown out there as an appellant
that you have the onus of proving your case, and that's true, but the regulator does have
to contradict things that you say. It's not the same thing as an onus, but if you say
something and it's not contradicted, then the likelihood is it's not guaranteed, but  `wide quieter`
there's a likelihood that it'll be accepted. So your evidence is she had an erratic presence.
What do you mean by that, Mr. Sheppard? Well, this, and you explain what that is.  `wide`

            *(3.3s pause)*
imposed unassessed unilateral directives.  `flat`
How did she impose unassessed unilateral directives?

**16:06.92  MR SHEPHERD**  `wide`  
So, for instance, without consulting any of the staff members?

**16:11.06  DWYER IC**  `↑+2.1st`  
Well, first of all, first of all, was this done by...
How did she do it? By email? Are these things in writing?

**16:18.90  MR SHEPHERD**  
Yeah, so that was what I was requesting, email.
But I said that...  `flat`

**16:23.08  DWYER IC**  
But don't you request that from...
Couldn't you request that from the regulator?

            *(2.9s pause)*

**16:29.72  MR SHEPHERD**  `flat`  
I guess I did request, but I didn't
be specific about that.

            *(2.4s pause)*

**16:37.02  DWYER IC**  
Um, so you say, and perhaps it's a question of particulars, you say, um, imposed, unassessed unilateral directives. Do you mean by that, and tell me if I've got this wrong, that she sent emails in the form of a directive to staff?

**16:55.94  MR SHEPHERD**  `flat quieter`  
Correct.

**16:56.22  DWYER IC**  `slow 1.0w/s quieter`  
Okay. So, in light of that pleading, wouldn't you be at liberty to ask the regulator to
produce those documents?  `flat`
I've just asked MSH. I thought that's who holds the documents.  `quieter`
Yes. Well, Ms Matheson, has disclosure in respect of documents taken place over the course of the matter so far?  `wide`

**17:35.36  MS MATHESON**  `wide`  
Yes, Commissioner. We've disclosed all we have currently.

**17:38.96  DWYER IC**  
Okay. Does that include email communications from Ms Chloe Taylor to staff?

**17:45.20  MR SHEPHERD**  `↑+3.3st quieter`  
There has been some emails to involve the quality of the staff, but I have to probably
consider that.  `flat quieter`

**17:53.42  DWYER IC**  `flat`  
Okay. Have you examined those documents that have been disclosed to you, Mr Shepherd, to
see whether or not it contains examples of these unassessed unilateral directives?

**18:03.48  MR SHEPHERD**  `flat`  
They do not. They're more just isolated towards me.

            *(2.0s pause)*

**18:09.88  DWYER IC**  
So do you say that in the disclosure that has occurred so far
there have been nothing that represents an example
of what you call an unassessed unilateral directive from Chloe Taylor?  `flat`
You say there's nothing like that in what's been disclosed to you from the regulator?  `↓-2.2st flat`

**18:29.00  MR SHEPHERD**  `flat`  
Not that I can recall, no.
Okay.  `quieter`

**18:31.60  DWYER IC**  `quieter`  
Okay. You see, making an order for a third party to disclose documents is a step sort
of beyond what normally happens in disclosure. It's quite an imposition because the health
service is not a party to these proceedings. They're not party to this. They're not involved
in these proceedings apart from the consequences of the application you file today. The starting
point is to ask the regulator to produce those documents. Have you done that?  `quieter`
I have asked the regulator to produce what they have.  `quieter`
Have you asked them to produce the unassessed unilateral directives?
Not those specific things, no.  `flat`
Okay. Well that would be a starting point. That's assuming that, because the regulator  `wide quieter`
whilst not representing the health service
will have access to the health service.
That necessarily will need to call potentially people  `wide`
who work for the health service as witnesses in the case, potentially.
Maybe not, but maybe.  `quieter`

            *(2.3s pause)*
In any event, the starting point for documents that you say exist  `wide`
that haven't been produced is the regulator.
You haven't specifically asked them for that.  `flat`

**19:45.62  MR SHEPHERD**  `flat`  
No, it was my understanding that I asked the person
and that control of the documents.  `flat`
Okay.  `↓-2.4st flat`

**19:51.22  DWYER IC**  
And perhaps I'm getting into stuff
you haven't even complained about.
But the point is, Mr. Sheppard,  `wide`
is that just looking at number...  `wide`
Stressor 1A,  `wide`
the way in which you prove this,  `↑+3.2st`
if you were going to prove this,  `flat fast 5.7w/s`
is you would give evidence  `flat`
about the erratic movements of Chloe Taylor
and then you would produce documentary evidence
of the unassessed unilateral directives
as you describe them.  `wide`

            *(4.0s pause)*
and that's the starting point.  `↑+2.7st flat quieter`
So, Chloe Taylor's here erratically  `↑+2.1st`
and she gives us these unassessed directives.
OK, so you give evidence that she's there erratically
and you produce the documents that are examples.  `wide`
How do you get those?  `flat fast 5.0w/s`
Well, the first thing you do is you see what the regulator's disclosed
and then if they haven't disclosed it, you write to them and say,  `wide fast 5.8w/s`
see, here I refer to unassessed unilateral directives.
I can recall on about July 2023 a directive to the effect of this.
That document should be in your possession or control
and I want you to make inquiries and produce it to me.
And if they don't, well, then you go to your non-party disclosure.
I'm not sure that these documents form part of your non-party disclosure
from recollection.  `wide`
It's a pretty wide net you're casting,
but I'm not sure you've actually asked for emails from Chloe Taylor  `wide`
tailor to the staff in respective directives.  `wide`

            *(8.4s pause)*
Where do I find that in your application?
And this is the other difficulty in respect of the...  `wide fast 5.1w/s louder`

**21:29.20  MR SHEPHERD**  `flat`  
Could I give you a simplified...
I gave it a mistake.  `flat fast 4.8w/s`
But it's just a...
It's really, really simple.

**21:34.88  DWYER IC**  `↑+3.4st`  
It should have been simple the first time.
Because when it's not simple, I'll tell you right now,  `↑+2.4st`
and I don't mind saying this,  `wide`
when I'm overloaded with page after page after page after page  `wide`
of what looks like AI generated material
I switch off
I'm a human being too Mr Shepherd
and my brain doesn't process it  `↑+2.5st wide`
and so what happens amongst all of that
is I miss the point
that's how I fall into error  `↑+3.2st flat louder`
if you give me way too much  `↑+3.8st`
if you talk at me for two hours  `↑+4.2st wide`
about something you can tell me in two minutes  `flat fast 5.0w/s`
I'm going to miss the point  `wide quieter`
Like any other human being.

**22:11.82  MR SHEPHERD**  `↑+4.1st fast 4.9w/s`  
Can I give you these two pieces of paper?

**22:13.82  DWYER IC**  `wide fast 5.9w/s`  
Hand it up, please.

            *(10.4s pause)*
What am I looking at?  `↑+3.0st fast 5.0w/s`
You've seen this, I take it, Ms Matheson?  `flat`

**22:29.58  MS MATHESON**  `↓-2.0st`  
Only just now.

**22:31.40  MR SHEPHERD**  `↑+2.4st wide`  
I haven't got a copy, but I can share.

**22:34.70  DWYER IC**  `fast 6.4w/s`  
If you don't mind, I'm just going to look at it and see where it takes us.
If I think you need to be across it, I'll let you know.  `fast 5.0w/s`
What am I looking at, Mr Sheppard?  `wide`

**22:42.12  MR SHEPHERD**  `flat`  
The 20 questions of my request of disclosure.
So the 20...  `wide`

**22:50.64  DWYER IC**  `fast 5.7w/s louder`  
This is the simple version, is it?

**22:51.96  MR SHEPHERD**  
Yes.

**22:53.46  DWYER IC**  
Where's the bit about Chloe Taylor's unassessed unilateral directives?
So just say email directives, basically.  `flat`
Where's that?  `flat quieter`

            *(16.0s pause)*

**23:19.06  MR SHEPHERD**  `flat`  
Manager, email, filters, that's what it would be, it would be under there.

**23:23.98  DWYER IC**  `wide`  
Which heading, which page, what number?

**23:26.28  MR SHEPHERD**  
10.

**23:27.98  DWYER IC**  
Item 10?

**23:29.16  MR SHEPHERD**  `↓-3.0st wide quieter`  
10.

**23:30.16  DWYER IC**  `flat`  
Manager, email, filters, A to E.

**23:33.48  MR SHEPHERD**  `flat`  
The filters would be directives.

**23:37.28  DWYER IC**  `↑+3.6st`  
What does filters mean?

**23:40.12  MR SHEPHERD**  
When you go into, let's say, e-health, for instance,
or let's say Outlook,  `flat`
and you put a word in Outlook  `flat`
and it filters all the words.
So my filters were effective immediately.
So that would be a filter.
So they get all these emails and say effective immediately.
Absolutely. Does that make sense? So that's the directives. And I basically just want  `wide`
the count. I don't even, for me, it doesn't matter.

**24:12.02  DWYER IC**  `↑+2.9st`  
Can I just, I don't mean to, I'm not picking on you, Mr. Sheppardson. I just want you
to, sorry, Mr. Sheppard. Let's just look at line 10, okay? So under the heading, disposition  `wide`
of items in brackets, single table. Okay? Doesn't make any sense to me. Disposition  `quieter`
of items, as in this is what you want me to do with the items contained in your non-party
disclosure, and then we go to line 10, status, press. What does press mean?

**24:43.10  MR SHEPHERD**  `flat`  
I would say...

**24:44.60  DWYER IC**  `↑+2.2st fast 6.1w/s louder`  
Press this, or what do I do?

**24:46.18  MR SHEPHERD**  
To either swear it or produce it.

**24:50.06  DWYER IC**  `wide`  
So you press, so you're still pressing for disclosure of manager email filters A-E.

**24:59.12  MR SHEPHERD**  
A. Yeah, A to A, which is on form 29.

            *(25.6s pause)*

**25:27.40  DWYER IC**  `flat quieter`  
This is the Form 29 file
on the 22nd of April, 2025, 26, yeah.  `wide`

            *(16.8s pause)*
A, C, E, what's that a reference to?  `flat quieter`

            *(2.0s pause)*

**25:55.04  MR SHEPHERD**  `flat`  
A, B, C, D, E, which is number 10.

            *(15.8s pause)*

**26:13.98  DWYER IC**  `↑+2.7st`  
manager email filters

            *(2.9s pause)*
I still don't understand what filters  `quieter`
means, is this filtered by  `wide`
language, is that what you're saying?  `flat fast 4.8w/s`

**26:23.84  MR SHEPHERD**  
yeah, so effective
immediately or for this
now or anything like that  `wide`

**26:29.48  DWYER IC**  `wide fast 5.4w/s louder`  
A through to E.

**26:30.40  MR SHEPHERD**  
Yeah.
Okay.  `flat`

            *(3.4s pause)*

**26:34.76  DWYER IC**  `wide quieter`  
You see, in a hearing, if you forget all these, right,
forget all these documents that you want to produce
to prove that she sent you these emails.  `flat`
So first of all, let me just come back to your statement of stressors, right?

**26:52.54  MR SHEPHERD**  
Unassessed unilateral directives.
Okay.

**26:54.90  DWYER IC**  
She's your manager, right?

**26:56.34  MR SHEPHERD**  `flat quieter`  
Yep.

**26:56.86  DWYER IC**  `wide`  
So she's going to send you directions.
unilaterally. Anyway, you can be directed as an employee
to do certain things, right? What do you mean by unassessed?

**27:06.64  MR SHEPHERD**  
What does unassessed mean? Unassessed would be that she wasn't even in the room or she doesn't even enter
the room to see what's going on and makes a decision  `flat`
without any input of the staff. Like a manager?  `flat`
I mean, usually a manager would need input.  `flat`

**27:22.96  DWYER IC**  
Like a manager. Managers make decisions without consulting staff
up all the time. It's totally legitimate.  `flat`

**27:28.90  MR SHEPHERD**  `flat fast 4.7w/s`  
But I think when it's in a
patient safety environment that they  `flat`

**27:32.64  DWYER IC**  
If you think it's in a patient safety environment
you can raise that.  `wide`
Anyway, let's not get into the case.  `↑+3.0st`
So let's just pretend none of this exists  `↑+3.1st`
and you're here in the witness box and you've  `flat`
got this stressor.  `flat`

**27:44.52  MR SHEPHERD**  `↑+4.1st`  
She's erratic physical
presence and  `slow 0.9w/s`
imposes unassessed unilateral
directives.  `↓-2.1st flat`

**27:52.44  DWYER IC**  `wide`  
You can give that evidence. You can say
and she gave us these directives. All
all the time, never asked us anything, she just kept sending these emails through saying  `↑+3.6st`

**27:59.66  MR SHEPHERD**  `↑+2.7st`  
effective immediately we're going to do this, effective immediately we're going to do that.

**28:04.00  DWYER IC**  
You can say that. Now, I don't know necessarily whether
I haven't checked the regulator's statement of facts and contentions in any great detail.  `flat`
They may wish to contradict that. They may not want to contradict that.
They might say the manager sent emails
giving directions to staff. Here's an example of one.
and the argument might not be about whether you received emails from Ms Taylor
the argument might be about whether or not they're correctly categorised by you  `wide`
as unassessed directives made without consultation  `flat`
you've placed subjectively a characterisation on these emails  `↑+2.4st`
which may be contradicted  `quieter`
but the existence of the emails may not be in dispute as far as I can tell
So you don't need the emails to prove that the emails are unassessed directives, necessarily.
And if you give evidence that you were sent unassessed directives by Ms Taylor, as you  `↑+2.1st`
call them, and the regulator doesn't contradict it, doesn't cross-examine you, doesn't produce  `quieter`
documents for you to comment on and that sort of thing, well, you know, that's a problem
for them, not for you.

**29:17.88  MR SHEPHERD**  `flat`  
so for me it was
direct calls to this number  `↑+3.0st`
but this number is an emergency
contact and then those doctors
the ones that get called for an emergency  `flat`
they're sent to the wrong side of the room
they're not sent to someone having a cardiac arrest
they're not sent to someone in respiratory
distress  `flat`
we're now not even contacting them by their numbers

            *(5.7s pause)*

**29:45.62  DWYER IC**  
It's going to move on for a moment, okay? Because after my speech about efficiency of
conduct of proceedings, I'm concerned at the direction this is going in, Mr Shepherd.  `flat`
And ultimately what I'm proposing is if we can't work this out today, if you can't get  `↑+3.2st`
yourself to a point where you're satisfied with the approach, a different approach or
or a more practical approach,  `flat`
or a more cohesive and cooperative approach  `↑+2.3st`
with the parties that are sitting at the other end of the table.  `flat fast 5.8w/s`
Yeah, I actually understand what you're getting at.  `wide`
If we can't get to that,  `↑+5.9st fast 6.4w/s louder`
I'm going to schedule this disclosure dispute for a hearing.

**30:19.46  MR SHEPHERD**  
Yeah.

**30:20.06  DWYER IC**  
And the health service is going to need to call evidence
to talk to their objections,  `wide`
and the regulator may or may not have anything to say,
but in the meantime, the party should work very hard  `↑+2.4st`
at formulating a bundle of documents that might satisfy you.
I don't know to what extent that's happened so far.
I see a very comprehensive objection,  `wide louder`
but what the responsibility of the parties is
when you have a disclosure dispute like this  `wide`
is to get working on whether they can resolve it
without my intervention.  `flat`
That's what the parties need to be doing as well.  `fast 5.0w/s`
I don't know whether that's happened or not  `flat`
or whether it's just a, this is what I want,  `wide`
no, you can't have it.  `flat fast 5.8w/s`
If that's where we're at, well, you've got a bit of work  `fast 6.3w/s`
to do down there at the bar table.  `↓-2.3st flat fast 6.0w/s`
But if we can't reach some understanding today  `wide`
day where you can be disavowed of the need to extract thousands of documents from the health
service then we're going to need to have a hearing and i need to decide whether you're entitled to do  `flat fast 5.5w/s`
that or whether it's unreasonable for you for you to require the health service or ask the health  `flat`
service to do that i can't do that in a mention this morning and i can't do that based on on the
papers i'm going to need to hear evidence about what's involved and that's going to have cost
consequences as well because i'd imagine the health service will probably want to engage  `flat`
aged ground law and they'll bring their lawyers along and I'll allow that because this is  `wide`
a complicated matter potentially if you want it to be and then there'll be cost consequences.
That's a hearing that's probably going to go longer than a day because there's a lot
of items in your list and lots of sub-items in your list, you know, A to E and 10 alone.
So, yeah, this is going to be a big sideshow, probably bigger than the hearing at the end  `↑+2.1st`
of the day and if you want it, you can have it.  `wide`

**32:02.78  MR SHEPHERD**  `↑+2.5st`  
I think I can
understand where you're getting at  `flat`
I think I can meet
most of the way, I understand how  `flat`

**32:10.84  DWYER IC**  
Have you had
discussions with the  `wide`
regulator about what they can
and can't facilitate in respect of
disclosure for documents that you say  `flat`
they could have or should  `quieter`
have, have you had  `quieter`

**32:24.58  MR SHEPHERD**  
constructive discussions with
them? We have not  `wide fast 5.6w/s`
not like a constructive discussion

            *(3.5s pause)*
I haven't been specific because I thought I had to go to MSH for, so.  `flat`

            *(2.4s pause)*

**32:43.46  DWYER IC**  
I don't know whether it's a generational thing, but back in my day we used to pick up the phone and we would talk to people and we'd say, hey, and just because you're an opponent to somebody in litigation doesn't mean you can't have a constructive civil conversation with them, right? Even if you're self-represented.
it. And it could be that all of this could be sorted out in a couple of constructive  `quieter`
phone calls. But before I release you to do that, I just want to bring you back to the  `quieter`
statement of stressors, right? I see that you've attempted to identify relevance in  `wide`
in terms of your response to the objection in relation to it,  `quieter`
and your application as well.  `flat`

            *(4.0s pause)*
But it's not at all unheard of.  `wide quieter`
In fact, it's more common than not  `flat`
that appellants will give evidence in these proceedings  `flat`
without relying heavily on documentary case,
not suggesting that you should or shouldn't.  `wide`
But if you were, as an appellant,  `wide slow 1.3w/s quieter`
to get in the witness box and say Miss Chloe Taylor had an erratic  `wide`
presence and she kept sending us these emails
and where are the emails Mr Sheppard? Well I asked the regulator
I said there will be examples and they haven't been provided
and then if I was presiding on the matter I'd say Miss Matheson have you got any emails  `wide`
of that type and they'll say we asked but none were provided to us  `wide`
and then I've got to decide whether or not I accept your evidence or not
but they don't contradict it, but more often than not, if you alleged that there were
emails that were causative of your stress, I would have
thought the regulator would be all over that and they'd say, right, well let's have a look at them, what do you mean by  `fast 5.8w/s`
that? And then they'd get examples of them and they would find their way into evidence.

**34:38.54  MR SHEPHERD**  `wide`  
Anyway.

            *(4.1s pause)*

**34:43.08  DWYER IC**  
Unilateral destruction of work health and safety
records. On the 6th of June, the appellant recorded a critical operation
and instruction in the communication book regarding the necessity of updating medical  `flat`
on-call contact numbers. Ms Taylor unilaterally removed and destroyed this entry. When questioned,
Ms Taylor subjected the appellant to a hostile and verbally aggressive reprimand. You're
not going to need documents for that, are you? That's just going to be, you're going  `wide fast 5.4w/s`
to make that assertion in your evidence and I would have thought the regulator will call
Ms Taylor to give her side of the story and you'll get to cross-examine Ms Taylor.
So you don't need any documents for that, do you?

**35:21.08  MR SHEPHERD**  `flat`  
Well, they've got documents for it, so...

**35:23.76  DWYER IC**  `louder`  
Okay, so have they disclosed those to you?

**35:26.56  MR SHEPHERD**  `flat`  
Yes.
She took them out.  `flat`
What have they disclosed to you?  `flat fast 5.0w/s`
I guess a dispute about the event, but it was taken out. That's it.

**35:37.98  DWYER IC**  `flat`  
So she's agreed it was taken out?

**35:40.40  MR SHEPHERD**  `flat`  
Yes. I mean, it wasn't ever said to me. It was said to...

**35:44.20  DWYER IC**  `flat`  
Okay.

**35:44.88  MR SHEPHERD**  `↓-2.9st`  
Yeah, so...

**35:45.72  DWYER IC**  
In any event, it sounds like there's going to be
a dispute around the characterisation of that event.
Did she unilaterally destroy work health and safety records  `flat`
in a way that was perhaps inappropriate in your view?

**36:02.34  MR SHEPHERD**  `louder`  
Or not?

**36:03.12  DWYER IC**  `wide`  
And she'll give evidence about that.
There's no documents required for that, is there?  `wide`
Did she physically tear the page out of a book?
Yes, she tore it.  `↓-2.2st wide quieter`
So maybe the book.  `flat fast 5.0w/s`
book. So we can see the torn out page. But she might admit she tore it out, in which  `quieter`
case we probably don't need the book. But anyway, that's the matter. It's not a particularly  `wide`
document heavy point, that one. Refusal to investigate work health and safety fatigue
complaints. Did you make a health and safety fatigue complaint in writing?

            *(2.0s pause)*
Yes, I made many. Okay. So you'll have a copy, or there should
should be a copy of an email to that effect?  `fast 6.4w/s louder`

**36:42.26  MR SHEPHERD**  `flat`  
Some of those emails,
but my health service email was restricted.  `flat`

**36:46.62  DWYER IC**  
Okay, but you've identified
that on the 7th of August, 2023,  `flat`
you submitted a formal grievance.
That's in the form of an email.  `fast 6.5w/s`

**36:52.92  MR SHEPHERD**  
Yep.
Do you still have a copy of that?  `fast 6.2w/s`
I have a copy of that.  `fast 8.3w/s`
So that's in your documentary case.  `flat`

**36:57.44  DWYER IC**  `flat`  
You've got that document.
And Ms. Taylor's conduct specifically raised  `flat`
is blah, blah, blah, and you said,  `flat fast 5.9w/s`
said, Miss Tammy Rees dismissed the complaint the same day without formal investigation
and directed the appellant to continue reporting directly to Miss Taylor. Did Miss Tammy Rees

**37:16.98  MR SHEPHERD**  
do that in an email or a letter? I wrote that to an email and that was our email correspondence
back of course. Yes, I got that. And you've got that? Yeah. Done. You've got your documents  `wide`
for that stressor.  `flat`

**37:29.56  DWYER IC**  `wide`  
Disparate treatment and statutory leave obstruction, COVID.
Between 20 February and 1 March 2024,
Ms Taylor forced the actively ill appellant  `wide`
to self-administer COVID-19 special pandemic leave
via MyHR,  `flat slow 0.8w/s`
a facilitation she routinely exercised
directly for other staff.  `flat`
The system server logs timestamp
the appellant's successful upload at exactly 11.41am on
20 February 2024. So you've been very specific about that. Despite the
subjective system log, Ms Taylor capriciously declined the application
twice, advancing factually erroneous claims contradicted by
objective server logs. So in essence
you were ill and you were seeking to take leave  `wide`
in relation to COVID and you say that  `wide`
Ms. Taylor capriciously declined your application  `flat`
twice. Did she decline it via email?  `wide`

**38:31.96  MR SHEPHERD**  `flat`  
Well, she actually declined it on the phone and then declined it
on the MyHR twice. Okay.

**38:38.90  DWYER IC**  
But that's all, I have all that. You've got all that? Okay, tick.
Public interest disclosure on the 13th of May 2024
lodged a corrupt conduct complaint regarding clinical risks.
It's Ethical Standards Unit formally determined
this constituted a public interest disclosure.  `flat`
Got all the documents for that?  `flat`

            *(2.2s pause)*
No, that's reform 29.
So presumably you lodged a corrupt conduct complaint.  `wide`
You'll have a copy of that because it's your document.  `flat`

**39:08.54  MR SHEPHERD**  
Yeah.

**39:09.18  DWYER IC**  `flat`  
And the Ethical Standards Unit formally determined
it constituted a public interest disclosure.  `flat`
You got a letter back confirming that.
So there you go.  `flat quieter`

**39:18.08  MR SHEPHERD**  
The point was that what, stress me out,
was what action was taken when HR received that complaint.  `flat`

**39:26.38  DWYER IC**  
Okay, so that's your next item.
That's F.  `wide`
So in relation to stressor E,
you've included the fact that you lodged a corrupt conduct complaint
and it was determined that it constituted a PID.
So you've got your documents in relation to that.
The next one is the immediate reprisal.  `wide`
Within 48 hours of the PID being lodged,
Ms Rees directed the appellant to retract a routine workplace email.  `flat`
A highly comparable email sent by Ms Taylor attracted no such discipline.
So presumably within, so sometime around the 15th of May 2024,  `wide`
Ms Rees has given you a direction to retract a routine workplace email.  `flat`
How did she give you that direction?  `flat`
Is it in the form of an email?  `fast 6.3w/s`

**40:13.04  MR SHEPHERD**  
She said that I have no longer got those.
Is it in the form of an email?  `flat fast 6.6w/s louder`

**40:18.44  DWYER IC**  `flat`  
Yes, but I've no longer got those.
But you've got, sorry?  `flat fast 4.9w/s`
I was restricted in my...  `flat`
First of all, answer my question first.  `↑+3.3st`
Is it in the form of an email?  `fast 6.3w/s`
Yes or no?  `flat quieter`

**40:28.28  MR SHEPHERD**  
Yes.

**40:28.64  DWYER IC**  `flat`  
Have you got that email?

**40:29.94  MR SHEPHERD**  `flat fast 6.9w/s`  
No, I do not.
All right.  `flat fast 6.2w/s`

**40:31.54  DWYER IC**  `wide`  
Ms. Matheson, have you got that email?
You don't know?  `flat quieter`

**40:36.74  MS MATHESON**  `↑+2.4st wide`  
The request for conducting an email,

**40:40.42  MR SHEPHERD**  `↑+3.2st flat quieter`  
I do believe we have those,
and I do believe we've disclosed them.  `flat quieter`

**40:45.04  DWYER IC**  
So it'll be an email from Ms Rees to Mr Sheppard
on or about 15 May 2024,  `flat`
the effect of which is purported to be a direction  `flat quieter`
to retract an email that he has sent.  `flat`

**41:01.20  MR SHEPHERD**  `↑+4.1st wide`  
I do believe that I have received those, Commissioner,
and disclosed them.  `quieter`
I would have to triple check to be...  `↑+2.9st quieter`

**41:07.98  DWYER IC**  `↑+3.1st`  
That's okay. That's all right.

**41:10.38  MR SHEPHERD**  `flat`  
Sorry, there's more emails which I don't

**41:14.42  DWYER IC**  
there's a conversation. I'll come back to that in a moment
we'll come back to the more emails in a moment. So the stressor  `wide`
you're relying on there, and I understand the case you're making  `wide`
so you put in a PID and then within 48 hours Ms Rees says to you  `wide`
retract an email you've sent. And so  `wide`
you've got the email from Ms Rees telling you to retract an email

**41:37.54  MR SHEPHERD**  `↑+6.7st`  
Correct.

**41:38.74  DWYER IC**  `flat`  
And you've, have you got the email that she asked you to retract?

**41:43.64  MR SHEPHERD**  
Yes, I got those two.

**41:45.98  DWYER IC**  
Okay, you've got that. And you, so you've got in essence the documents that support that allegation.

**41:53.82  MR SHEPHERD**  `quieter`  
Yep.

**41:55.02  DWYER IC**  
You've got your PID on the 13th of May. You've got on the 15th of May an email from Ms Rees saying retract this email that you sent.
and you've got a copy of the email that she was referring to.  `flat`

            *(2.4s pause)*
Your case then tilts into a comparison.  `wide`
You say that a highly comparable email sent by Ms Taylor  `wide`
attracted no such discipline.  `flat`
Well, firstly, do you have a copy of the email from Ms Taylor
that you're comparing to yours?

**42:25.34  MR SHEPHERD**  `flat`  
Correct, yes.

**42:25.90  DWYER IC**  `fast 5.4w/s louder`  
You do? All right.
And where does your knowledge come from
that you rely on to say  `flat`
Ms. Taylor wasn't subject to the same direction or discipline?

            *(3.9s pause)*

**42:42.42  MR SHEPHERD**  `flat`  
I don't have knowledge of that,
but it seemed pretty...  `flat`
I understood it.  `flat`
Okay.  `flat`

**42:47.96  DWYER IC**  
So your evidence is going to be
that Ms. Taylor sent the same sort of email
and nothing happened to her.  `flat fast 4.9w/s`

**42:53.60  MR SHEPHERD**  `↓-5.3st quieter`  
Yeah.
Okay, but you don't know...  `↑+2.4st wide`
I don't know that.  `fast 5.6w/s`
...to a certainty.  `↑+2.4st wide`

**42:57.44  DWYER IC**  `fast 5.1w/s`  
And that's a question you can put to Ms. Taylor.

**42:59.54  MR SHEPHERD**  `↓-10.7st quieter`  
Yeah.

**42:59.90  DWYER IC**  `flat`  
and you don't need any other documents for that.
So there you go.  `flat fast 6.9w/s`
You've got the documents that you need for those stressors.
G, suppression of industrial representation  `wide`
during roster disputes.  `flat`
In April 2023, the appellant formally expressed interest  `wide`
in assuming the role of union delegate.
In direct contravention of union encouragement,

            *(2.1s pause)*
the employer actively suppressed this appointment for 13 months.  `wide`
months. Okay, so in April 2023, you formally expressed interest in assuming the role of  `quieter`

**43:36.16  MR SHEPHERD**  `wide`  
union delegate, in an email I presume? Yeah, even in when I went for, when I went
from point A to full time as well, so even in an application.  `flat fast 4.8w/s`

**43:45.82  DWYER IC**  
Okay. And so there might be some oral testimony that goes with this, but there's presumably,
when you say formally expressed interest, I presume that's a reference to something in
writing? Yep, there's a few things. And you've got that? Yep. Okay.
So then you contend that the employer actively suppressed your appointment
as a union rep for 13 months. Crucially  `wide`
this deliberate administrative inaction left the department operating without
local delegate representation precisely during a period when the  `flat`
appellant was actively attempting to dispute unsafe time rostering  `flat`
etc. etc. So how do you say that
that they actively suppressed your appointment for 13 months?  `flat`
Like, what did they do?  `fast 5.0w/s`

**44:27.90  MR SHEPHERD**  `flat`  
Because the union said that they've emailed my manager.

**44:31.60  DWYER IC**  
So the union said that they have emailed your manager?

**44:34.92  MR SHEPHERD**  `fast 4.7w/s`  
I got that in writing, yes.
OK, you've got that letter?  `wide`
Yep.  `↑+2.4st flat quieter`

**44:38.38  DWYER IC**  `flat`  
And so it says something to the effect of,
we've been emailing your manager,  `flat louder`
but we haven't heard back from them,
or they're not cooperating, or whatever.  `flat`
Yeah, just that we've followed up with the health service,
or we've followed up with the manager,  `flat fast 5.2w/s`
and, yeah, it was just ongoing.  `flat quieter`
Can I just, as an aside, make the observation here  `wide`
that I've had a lot of experience with unions over my career
and if they had a person who they were putting forward
as their workplace delegate  `flat`
and they weren't getting cooperation from management  `flat`
about the installation of that person as the workplace,
in a formal sense,  `flat`
they wouldn't sit on it for 13 months.
Are you saying that they did?  `flat fast 6.2w/s`

**45:21.08  MR SHEPHERD**  `flat`  
Yeah, so I joined a second union.

**45:23.66  DWYER IC**  `flat`  
So you joined another union?

**45:25.16  MR SHEPHERD**  
Exactly.
Okay.  `↑+3.7st flat`

**45:26.48  DWYER IC**  `↑+3.4st wide slow 1.3w/s quieter`  
So, well, it just seems unusual to me, Mr. Shepard,
and I'm not going to get into the facts now  `fast 6.2w/s`
because I'm not hearing the matter,  `flat fast 5.7w/s`
but your evidence about the employer inactivity  `slow 1.1w/s`
or the employer, you say,
actively suppressed this appointment.
appointment. So deliberately, consciously interfered with your taking office as their  `wide`
workplace delegate. Is that what you're saying?  `flat`
We didn't have one.  `fast 5.9w/s`
No, no, no, no. It's a simple question. Your case, as you said here, is the employer actively  `↑+3.0st`
suppressed the appointment for 13 months. So actively means they deliberately. Am I  `wide`
right about that or have I read that wrong?  `fast 5.1w/s louder`

**46:10.84  MR SHEPHERD**  
I don't know if I can prove it as much.

**46:13.64  DWYER IC**  `quieter`  
Okay. Well, that answers the question.
So your case, but it doesn't mean you can't make the case.  `↑+4.5st`
I'm not saying to you you can't run the case,  `wide fast 6.2w/s`
but I'm focusing here on what you can prove and can't prove,
but more particularly, if you have to prove  `wide quieter`
or you think you can prove something,  `wide fast 6.7w/s`
whether there's a document that supports it.  `flat`
So you don't have any documents, or sorry,  `↑+3.4st`
the employer, to your knowledge,  `wide`
doesn't have any documents that demonstrate  `flat`
that they actively suppress the appointment.  `flat`
moment, it's more so the correspondence you got from the union.  `flat`

**46:44.90  MR SHEPHERD**  `↑+2.8st`  
The correspondence I also got from the manager, but it wasn't actively spread, it was actively
avoided, but would be more likely.  `flat`

**46:52.06  DWYER IC**  
Okay, but in any event, your characterisation of the conduct of the employer in relation
to this stressor is based on the fact that you put your hand up formally to be the union
union delegate, and 13 months went by, and you were not formally installed as the union
delegate in any formal way?  `wide`

**47:15.68  MR SHEPHERD**  `flat`  
Well, it was just time and time again, so it wasn't just 30 months, it was documented
time and time again, I was attempted.  `flat`
Okay.  `flat`

**47:22.84  DWYER IC**  
So have you got your correspondence between you and the union?

**47:26.80  MR SHEPHERD**  `flat`  
Yes, I got both, my manager and my union, but yeah.

**47:30.48  DWYER IC**  
So you got all the correspondence that demonstrates that it was 13 months?
you've got all of that? I just haven't got what the manager did with that
correspondence if that makes sense. Do you know
that they did anything with it? Well I think they didn't do anything with it
Do you know they did anything with it? Well I didn't
What are you asking for if that's the case? Do you think there is some

**47:55.66  MR SHEPHERD**  
I'm asking for evidence or a sworn statement to
say that I guess they didn't do anything with it  `flat`

**48:02.56  DWYER IC**  
So your case is going to be, based on the documents that I understand you've got now, is that you formally put your hand up to be the union delegate and that via communications from one of two unions in a 13-month period following that, there was no steps taken or recognition of your office being assumed as a union delegate in that 13-month period.
period and you're informed that management had some role in that through correspondence
from your union.  `flat`

**48:36.74  MR SHEPHERD**  
Correct.
Okay.  `↑+2.2st flat`

**48:37.76  DWYER IC**  `↑+2.1st fast 6.2w/s louder`  
And you can put all that in evidence.

            *(2.7s pause)*
When I say that, I'm not making a ruling on that now for the purposes of the final hearing,
so there may be some objection to correspondence from a union that's not supported by a testimony  `flat`
from the author of the correspondence, but if it's a letter to you, you can say, I've

**48:57.04  MR SHEPHERD**  `wide`  
I got this letter from the union, and the letter says the management is blocking me.

**49:03.58  DWYER IC**  `flat`  
You know, management's not being very helpful.
But as I said, I come back to my aside.  `wide fast 5.6w/s`
It's unusual, in my experience, that a union wouldn't have, you know, gone to town on that.  `wide`
Well, they just said that we emailed the health service.  `flat`

**49:19.58  MR SHEPHERD**  `flat`  
Yeah, they didn't really do much.
But that's why I ended up joining a second unit, a union at the time,  `flat`
because there was a lot of inconsistency there.

**49:29.32  DWYER IC**  `flat fast 5.0w/s`  
And how did the second union go
with having you put in as the union delegate?  `flat`

**49:33.46  MR SHEPHERD**  `flat`  
Well, second union, they basically...
I can't remember the...

**49:40.20  DWYER IC**  `↑+3.3st flat fast 6.8w/s louder`  
Yes or no?
Mr Sheppard, did they support your appointment  `↑+4.2st louder`
as the union delegate representing their union?  `flat`

**49:46.14  MR SHEPHERD**  `flat`  
They did not cover the administration.

**49:50.06  DWYER IC**  
So they didn't have coverage of that workplace?

**49:53.18  MR SHEPHERD**  
Yeah.

**49:53.36  DWYER IC**  
So you couldn't be a representative of that union in that workplace?
Okay. All right.  `wide quieter`
Okay, so I don't know that there's a lot of documents  `↑+2.4st quieter`
beyond what you've already got that support that contention.  `flat`
And remember that disclosure's not like an exercise of phishing.
You can't go sort of delving around at large in the inboxes and so forth.
You make the assertion here.  `wide`
Once you've made the assertion,
the regulator's got to respond to it.  `wide`
They've got to address it.
They'll address it in cross-examination.
They may produce documents that they seek to rely on to contradict it.
They've got to disclose those documents to you.
So you've got the documents that support that contention,
or that stressor, it would read to me.  `wide`

            *(2.2s pause)*
We go to stressor two,  `↑+2.8st`
systematic failure to discharge remuneration obligations
between February and April 2024.
The employer systematically failed to pay the appellant
whose correct statutory entitlement  `flat`
is resulting in a documented 42% pay disparity.  `flat`

            *(2.2s pause)*
Can I just say as an aside,  `↑+2.2st quieter`
has that been the subject of an unpaid wages claim  `flat`
or has your pay disparity been rectified?

**51:09.18  MR SHEPHERD**  `flat`  
I have not raised that.

**51:11.72  DWYER IC**  
So you haven't raised a 42% pay disparity?
I haven't raised it with the QARC or anything.
42% pay disparity  `↑+4.6st flat`
meaning what? You paid 42% under  `flat`
what you should be paying? Is that what you're saying?  `fast 6.0w/s`

**51:24.60  MR SHEPHERD**  
That's what me and my colleagues over a six week

**51:26.94  DWYER IC**  `wide`  
period. Over a six week period
you and your colleagues were underpaid  `flat`
in the amount of 42%  `flat`
of what they should have been paid  `flat fast 5.6w/s`

**51:35.28  MR SHEPHERD**  
So I guess over
public holidays and things  `↑+5.2st flat louder`
my manager decided to roster me
on different specific days  `flat`
and it ends up being  `wide`
42% difference  `flat`
In what?
Between me and my colleague.

**51:50.00  DWYER IC**  `louder`  
Between you and a colleague or your colleagues generally?

**51:52.84  MR SHEPHERD**  `flat`  
My colleagues generally because I would be rostered off.

**51:55.06  DWYER IC**  
Okay, so somewhere in the rostering system you didn't get public holidays
and therefore you didn't get the loading for public holidays.
Is that what you're saying?  `flat fast 6.4w/s`

**52:04.86  MR SHEPHERD**  
It was a consistent theme, yes.

**52:07.00  DWYER IC**  `quieter`  
Okay, all right.
And you'd prove that presumably through a sample of rosters
between February and April 2024, wouldn't you?  `flat`
or the rosters. So you're saying this stress
all particularly relies on evidence around what the rostering was  `flat`
in respect of public holidays between February and April 2024.
So those public holidays would be Good Friday,  `flat`
Easter Sunday, Easter Monday and  `wide`
Anzac Day. So four public holidays.
So  `flat quieter`

            *(2.3s pause)*
So have you got access to the rosters for that period?  `flat`

**52:46.46  MR SHEPHERD**  `fast 5.5w/s`  
I have all the evidence for that.

**52:47.86  DWYER IC**  `wide quieter`  
Got all those? Awesome.
So your theory is going to be look at the rostering in relation to me,
look at the rostering in relation to other staff members
in that three-month period.

**53:00.52  MR SHEPHERD**  `↓-6.8st flat quieter`  
Yes.
Okay.  `flat`

**53:02.86  DWYER IC**  `flat louder`  
Is there any other document that you say you know exists
which tends to support that you were deliberately  `flat`
rostered in a way that avoided you being put on public  `flat`
holidays? There's probably a few  `wide slow 1.2w/s quieter`
things yes. Well probably or is because disclosure is about what you know  `wide`

**53:22.68  MR SHEPHERD**  
I think I actually said that
I'm not asking disclosure about that anymore

**53:30.64  DWYER IC**  
Okay, alright, fine, that's okay. We probably should have led with that
I'll leave it up to you to tell me.  `flat fast 5.5w/s`
If we get into anything that you think we don't need to get into,  `fast 5.6w/s`
you tell me and it'll save us some time, all right?  `flat fast 6.3w/s`
Don't worry about interrupting me on that score, OK?

            *(2.5s pause)*
Unreasonable delay on the 3rd of May.  `↑+2.5st louder`
Are we still dealing with this one?  `wide fast 6.4w/s`

**53:49.98  MR SHEPHERD**  
So that's a different subject.

**53:51.96  DWYER IC**  `flat`  
Queensland Health Payroll explicitly identified the errors
and directed Ms Taylor to process corrections immediately.
What errors are you talking about there?
Failed to action the urgent directive until the 28th of May.  `flat`
So I recall that we don't need to go over that too because I've recalled that.  `flat`
That's all I need to know.  `flat fast 7.5w/s`
If you think we don't need to go over it, we can skip over.  `fast 6.5w/s louder`
Stressor 3, we're getting there.  `↑+2.8st`
Admitted breaches of statutory fatigue management.
Mathematical reality of the work health and safety breach.
On the 17th and 18th of March 2024,
the employer rostered the appellant to work consecutive shifts
separated by a mere seven-hour break.

            *(2.1s pause)*
factoring in the appellant's established commute
the appellant was subjected to 16 hours of wakefulness work  `flat`
and 4 hours of high risk commuting  `flat`
leaving approximately 4 hours of actual sleep  `flat`
so this is going to need  `wide`

**54:47.86  MR SHEPHERD**  
roster for the relevant period
I have everything for this
I have everything for this  `wide`

**54:54.76  DWYER IC**  
so we don't need to go into this one?
No. Okay. Flagrant bypass of the Neville safety mandate despite prior warnings. Are we going
into that? We don't need to go into that. Okay. Awesome. Unjustified administrative
detriment. When the appellant predictably required recovery time, is that all part of
the same thing? It's all part of the same thing, yes. You've got all the documents for  `fast 5.4w/s`
that? Yes. Admitted unreasonableness, the regulator's own independent review office,  `flat`
office, IRO. Got all that? Okay. And then the last one, which isn't necessarily identified  `wide`
as a stressor, but I'll go to it anyway. 12th and 16th of July, 24, while incapacitated
by a certified psychological leave, the employer scheduled meetings regarding his complaint.
On 8 October, the employer terminated the appellant under abandonment provisions despite
despite holding continuous medical certificates,
the appellant was subsequently reinstated.  `wide`
Okay.
During proceedings,
the respondent unilaterally obtained the appellant.
So this is after you sustained your injury?  `louder`

**55:59.66  MR SHEPHERD**  `flat quieter`  
Yeah.
Okay.  `flat`
All right.  `wide quieter`

            *(2.6s pause)*
Are there any documents in relation to any of that that you think...  `flat`
No, I have all of that.  `flat fast 9.7w/s`
Okay.  `flat`
All right.  `flat`

            *(3.1s pause)*
Has our discussion  `↑+3.1st wide`

            *(3.7s pause)*

**56:17.34  DWYER IC**  `flat quieter`  
focused your understanding of what your case is
to the extent of what documents might or might not be necessary?  `flat`

**56:26.18  MR SHEPHERD**  `wide`  
I think I can get it easier in a path
that I could probably really scope a lot of that.  `flat`
Yeah.  `↑+2.6st wide quieter`

**56:34.32  DWYER IC**  `↑+4.2st`  
I think it's important.
I understand you're acting for yourself, Mr Sheppard, I do,
and I understand that you're, you know,
and in no way at all being critical in this respect,  `flat fast 5.3w/s`
you're floundering around a bit, you know,
because you're not sure what you need to do  `wide fast 5.6w/s`
and what you don't need to do.  `↓-2.1st fast 6.9w/s`
And oftentimes people do make what I think is the mistake  `flat`
of, you know, overcooking it.  `flat`
Your case, you've got to keep coming back to those stressors,
but also what you can and can't prove.  `wide`

            *(3.0s pause)*
Ultimately, there's parts of this
that are going to need documents,  `flat fast 6.5w/s`
but it sounds like not the sort of volume of documents
you're talking about.  `flat`
You, I think, have as a broader grievance
a view that, you know, systemically,  `wide slow 0.8w/s quieter`
the place in which you worked had a number of failings
and problems related to aid manager
and non-compliance with proper protocol,
procedure, legislation, et cetera.

            *(2.0s pause)*
I may just be speculating about that  `wide`
but I get the sense that you've got that broader grievance
and it's important to  `quieter`
and you may be right about all of that  `fast 5.2w/s louder`
you don't have to go too far  `wide`
in any public sector or any organisation really
I shouldn't beat up the public sector  `flat`
but in any organisation to find  `wide`
failures to comply with legislation
failures to comply with protocol
failures to comply with policy  `flat`
it happens every single day in every single workplace  `wide`
place. It's a question of whether or not there's anything material that arises from any of
that and people do it all the time and it's only a problem if somebody gets sacked or
somebody gets killed or somebody, you know what I mean? And it's only then when these
things get a light shone on them and they become relevant. So understand, I think, that
you have, looking at your material, you have that broader grievance. But you need to understand
for the efficient conduct of this appeal
that it's about those matters that you've identified  `wide`
as being causative of your medical condition.  `flat`
And it's not about you proving that this was a terrible place,
a toxic place,  `flat`
that there's multiple examples of ways they didn't comply with this
or didn't do that or should have done that.  `flat fast 5.4w/s`
It's not a broad-brush criticism
of what you regard as the systemic failings of the organisation.  `flat`
organisation, your case must focus on the stressors that you've identified and to the
extent that you need documents to support those, from what I can see from them it's  `quieter`
a much shorter list. What I would rather do than subject everybody to a full blown hearing  `wide`
hearing about your Form 29, and I'm not closed to that idea if you really wish to press it,
I'm not closed to that at all, but I would, I think you will find Ms Matheson is sufficiently  `wide`
objective and cooperative to have a constructive discussion with the regulator. They have responsibilities  `wide`
as a model litigant, okay, so they can't hide stuff from you, they can't be sneaky or tricky
hearing like that, they will operate in the way that I've always experienced them operating

**59:53.24  MR SHEPHERD**  `flat`  
both as a commissioner and as a practitioner, appearing against them on many occasions as

**59:58.40  DWYER IC**  
professionals. And if there's a document that you can properly identify as being something
that they can readily access through their liaison with the health service, then they
should be able to provide it to you. But it'll be subject to constructive discussions about  `wide`
about, well, what is it? How do we identify it? How's it relevant? Those sorts of things.
And if there is a document in those discussions that Ms Matheson says, well, yeah, we know
it exists, but we don't think it's relevant, you can come back to me. And looking at a
single document, I can tell you very quickly whether it should be disclosed or shouldn't
be disclosed. There's also a case of being able to identify it, okay? But your case shouldn't  `wide`
be about, I'm loathe to say you can't and can do things, but to assist you, you need
to focus on the stressors that you rely on to support the contention that you've sustained
an injury within the meaning of the act. You don't need to prove it was an overall toxic  `flat`
place to work and Miss Taylor or whatever her name is, your supervisor was a terrible  `flat`
manager, et cetera. You don't need to prove all of that. You need to prove the matters  `flat`
that you've identified in the stressors  `flat`
as being causative of your injury.
And as I said, that's a much shorter scope  `flat`
in terms of documents.  `↓-2.3st flat`
Fewer documents means simpler case,  `↑+3.2st`
means easier for someone like me to understand it
and not get it wrong.  `flat fast 6.6w/s`

**61:23.96  MR SHEPHERD**  `quieter`  
Okay?

**61:26.10  DWYER IC**  `↑+2.1st`  
So this is what I'm...
I should just, before I move on,  `fast 5.0w/s`
anything arising out of all of that, Ms Matheson?
Have I misrepresented your role in the matter
or placed a burden on you
that you're not prepared to accept?  `flat fast 5.1w/s`

**61:37.14  MR SHEPHERD**  `flat`  
No.
All right.  `↓-11.3st`

**61:39.12  DWYER IC**  `wide`  
And Ms. Rutland, any?
Okay, all right.  `↑+2.6st wide quieter`
So what I want to do is this,  `↑+3.3st`
and I'm open to the parties telling me otherwise,  `flat fast 5.2w/s`
but this is what I want to do.  `fast 8.3w/s`
I'd like to park the Form 29 for a little bit longer
and hopefully with some meaningful discussions,  `wide`
having taken on board what we've talked about this morning,
Mr. Shepard, you can formulate a view
about whether there are any...  `flat`
Look at what you've got.  `fast 6.0w/s`
Look closely at what you've got from the regulator
later in terms of disclosure to this point, and
if you feel like there's still something that you can say for  `wide`
certainty exists, so look, I remember that Ms Taylor sent
us emails routinely during this  `slow 1.3w/s`
period. If you're going to talk about those things that we talked about
before, which was the unassessed directives or whatever, you might be on to
something there. They might have an obligation to provide those.  `flat`
they're likely to come out one way or the other  `↑+2.8st louder`
either they give them to you and you have them
or you contend they were sent and they produced them  `wide`
during the course of the proceedings  `flat`
it seems to me that those are going to be more about the character of those emails
as opposed to whether they were actually sent or not  `flat`
so the fact that you make the assertion that you were sent these emails
needs to be addressed by the regulator
and to that end they're likely going to produce them
if they haven't disclosed them already
then that probably that's probably something you need to look at that that  `wide`
particular point is the one one area I think in all of what we've been through  `flat`
that there might be something to look at but over the course of the next few  `quieter`
weeks if you want to have a think about the question of disclosure and attempt  `flat`
to have some constructive polite and professional discussions with Mathis
with Miss Matheson I'm sure you will be able to achieve that and it may be that
you managed to whittle this list right down to next to nothing if not nothing  `flat fast 4.9w/s`
thing. And then you can get on with the important business of getting this thing to a hearing.
Okay? Yep.  `↑+3.8st quieter`
Sound like a plan? Sounds good. Alright. Any objections  `↑+2.9st quieter`
to this just being stood down for about four weeks and  `wide`
pending a hearing back from Mr Sheppard about whether he wishes to press
any part of it? No, thank you, Commissioner. Ms Rutten, is that  `quieter`
alright with you? Yes, Your Honour, that's fine, thank you. Alright. And you're okay?  `quieter`
OK, so I'll stand it down for four weeks,
give you a chance to take on board what I've talked about
and recalibrate your thoughts,  `wide`
and then if you still wish to press any aspect of it,
we'll get down to the serious business  `flat`
of dealing with your specific application, OK?  `flat`
But I'm hopeful that if you take on board what I've said today
and you have some discussions with Ms Matheson,
you may find your way through this in a much simpler way.  `wide`
OK? All right.  `wide quieter`

**64:28.94  MR SHEPHERD**  
All right.

**64:29.68  DWYER IC**  `flat`  
Nothing further?
Nothing further?  `quieter`

**64:33.38  MR SHEPHERD**  `↓-5.8st fast 5.0w/s`  
All right.

**64:33.80  DWYER IC**  `flat`  
Thanks, Paddy.