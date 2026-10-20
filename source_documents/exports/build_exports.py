"""Generate first-person HTML / PDF / PPTX exports of the conciliation brief.

Voice: as if I (Cory Lea Shepherd) am the one submitting and showing the
exhibits. No "analysis", "rebuttal", "the Complainant" framing — just
direct first-person.
"""
from __future__ import annotations

import html
import os
import textwrap
from dataclasses import dataclass, field
from pathlib import Path

OUT = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# CONTENT — first-person voice
# ---------------------------------------------------------------------------

TITLE = "What happened to me, and what the evidence shows"
SUBTITLE = "My submission and exhibits for the Conciliation on 14 May 2026"
AUTHOR = "Cory Lea Shepherd"
MATTER = "EDR19098 / CRM:0270704 — Queensland Human Rights Commission"


@dataclass
class Section:
    heading: str
    paragraphs: list[str] = field(default_factory=list)
    bullets: list[str] = field(default_factory=list)


@dataclass
class Exhibit:
    number: str
    name: str
    what_it_is: str
    what_it_shows: list[str]
    quote: str | None = None


OPENING = Section(
    "Who I am, and what I am asking the Commission to do",
    paragraphs=[
        "My name is Cory Lea Shepherd. I am 34 years old. I was the named lessee at "
        "Unit 104, 158 Scarborough Street, Southport from 10 April 2023 to 10 April "
        "2025. I am the person Queensland Police removed from that apartment on the "
        "night of 23–24 February 2025, while my then-partner was on a holiday in "
        "Perth and the property manager had four days earlier sent the police, in "
        "writing, a Form 9 Entry Notice that I could come and collect my things.",
        "I am asking the Commission to find that Queensland Police acted "
        "incompatibly with my human rights, that they failed to give proper "
        "consideration to my rights when they made the decisions that night and "
        "in the weeks and months that followed, and that the pattern of conduct "
        "against me — and against my mother, my sister, and my sister's baby — "
        "was retaliation for protected complaints I had been making since "
        "December 2023.",
        "Everything I say here is anchored to an exhibit. I am not asking the "
        "Commission to take my word for any of it. I am asking the Commission to "
        "look at what the officers themselves recorded, what the property "
        "manager told them at the time, what my then-partner herself wrote at "
        "the time, and what the Magistrate did the very next morning.",
    ],
)


WHAT_HAPPENED = [
    Section(
        "December 2023 — where this began",
        paragraphs=[
            "In December 2023, I lodged a Service Delivery Complaint about an "
            "officer at Southport Police Station. Case ID 8933558. The OIC of that "
            "station, Senior Sergeant Luke J. Tulacz, reviewed his own station's "
            "conduct and emailed me on 11 December 2023 that he considered the "
            "actions of the officer 'lawful and justified' and the matter "
            "'finalised'.",
            "I replied on 5 January 2024: 'I was unaware that the police officer I "
            "was complaining about was able to take his own complaint.'",
            "Later, I attended Southport Police Station at my mother's request to "
            "make a complaint about the welfare of my younger sister Isabella, who "
            "was 15 at the time. An officer yelled at me at the counter. I asked "
            "for the body-worn camera footage. I was refused. The same OIC "
            "reviewed it internally. There was no action.",
            "Everything that follows in my submission needs to be read in the "
            "knowledge that I had already, more than once, made formal complaints "
            "about this particular police station.",
        ],
    ),
    Section(
        "October to December 2024 — Romeo, the cats, the first false report",
        paragraphs=[
            "On 25 October 2024 my mother and I drove from the Gold Coast to "
            "Sydney to pick up a Pomeranian puppy I had bought from a breeder. I "
            "named him Romeo. I registered him with the Gold Coast City Council. "
            "The receipt and the registration are in my exhibits.",
            "By November 2024 there were seven animals at the unit — Romeo and six "
            "cats. The lease only permitted two. I had been the one looking after "
            "them. I suggested some of the cats should go to a shelter. That is "
            "the conversation that started the falling-out.",
            "On 1 December 2024 at around midnight my then-partner Alexia Negro "
            "left the unit with five of her friends and took Romeo with her. "
            "Within hours Robina Police issued a Police Protection Notice — "
            "QP0899 — on the application of Senior Constable Ryan Yaun and the "
            "authority of Acting Sergeant Bradley Harris. The QPRIME occurrence "
            "is QP2402065947.",
            "The only conditions on that Notice were that I be of good behaviour "
            "towards Alexia and not commit domestic violence against her. There "
            "was no no-contact condition. There was no order excluding me from "
            "the unit. There was no ouster.",
            "On 17 December 2024 I was pressured into signing a transfer of "
            "Romeo's registration to Alexia on the NSW Pet Registry. I have my "
            "Gold Coast registration. I have the breeder receipt. I have the "
            "messages where she promised me she would never restrict me from the "
            "animals.",
        ],
    ),
    Section(
        "17 to 22 February 2025 — Alexia goes to Perth, the property manager backs me",
        paragraphs=[
            "On 15 February 2025 Alexia's friend Laura Phillips moved into our "
            "unit to house-sit. I had never met her in my life. On 17 February "
            "Alexia and her mother flew to Perth on holiday.",
            "On 19 February 2025 at 4:36 in the morning the property manager, "
            "Denis Constable, sent Alexia an email telling her that I would be "
            "coming to the unit the following day at 9 a.m. to pick up my "
            "belongings. That is a Form 9 Entry Notice. The property manager "
            "issued it.",
            "At 7:26 a.m. Alexia replied from Perth telling Mr Constable I was "
            "'intimidating the person looking after my animals' and that the "
            "matter was 'contested property... will need a lawyer or police to "
            "get it'.",
            "At 9:29 a.m. she classified it again in writing: 'a legal civil "
            "case that he is required to obtain a lawyer for and dispute me for "
            "these items'.",
            "On 22 February 2025 the leasing manager confirmed that the tenancy "
            "had not been terminated and that the lease was valid until 10 April "
            "2025. I had served Alexia with end-of-civil-partnership documents "
            "the same day. I was trying to formally separate.",
        ],
    ),
    Section(
        "23 February 2025, 7:51 p.m. — what I actually did",
        paragraphs=[
            "At 7:51 p.m. on 23 February 2025 I called Police Link on 131444. The "
            "call lasted 36 minutes. I have the iPhone call log.",
            "While I was on that call I entered Unit 104 with my key. I had my "
            "friend Tom Balsey with me. He was filming because I was worried "
            "about being set up. The property manager had told me four days "
            "before I could come and collect my things.",
            "Romeo was inside the unit. He came to me. I did not go in to take "
            "the dog. The dog came to me.",
            "At 7:51 p.m. Laura Phillips sent Alexia a text. Alexia's own sworn "
            "statement records that text word-for-word. The text says: 'Cory's "
            "here, he opened the door, he came in and took Romeo (the dog).' "
            "She used the word 'opened'. Not 'burst'. Not 'broke'.",
            "I loaded a van with my belongings and left. Tom drove with me to his "
            "house. The Southport Police Station is 500 metres away from my "
            "apartment. The police did not arrive at the unit for about six hours.",
        ],
    ),
    Section(
        "24 February 2025, the early hours — what the officers themselves said",
        paragraphs=[
            "At 1:35 a.m. Constable Bickery attended me at my mother's house and "
            "recorded that Alexia was 'in Perth and currently on a flight'. Tom "
            "Balsey was there and confirmed it. Constable Easthope said it again "
            "on body-worn camera: 'she's on the plane'.",
            "At 1:50 a.m. police forced the door of Unit 104 to retrieve Laura "
            "Phillips. The barricade she had built from a bookshelf and a dog "
            "leash gave way. The door was broken by the police, not by me.",
            "At 1:54 a.m. the property manager, Denis Constable, telephoned "
            "Constables Bickery and Harmer during the lockout. He told them in "
            "express terms: 'Form 13 does NOT terminate the lease.' They were "
            "warned, in real time, that what they were doing was unlawful.",
            "At 2:00 a.m. Constable Easthope's arrival briefing was captured on "
            "his own body-worn camera. He said, in his own words: 'he's got the "
            "key and he's got a lease… it's his lease, his bottom and it's his "
            "key, so he's entering the property to get stuff out.'",
            "At 3:26 a.m. the police asked the same property manager to "
            "re-activate my fob — because I had been the one who had asked him "
            "to deactivate Alexia's fob during her absence. They were asking the "
            "building manager to undo a security decision that I had made as the "
            "lessee.",
            "They arrested me anyway. They took my phone. They did not put my "
            "phone on the Field Property Receipt 137237 — that receipt lists "
            "'1 x dog' and that is all.",
            "Tom Balsey, my friend, gave the arresting officer Constable Bickery "
            "a printed packet of email threads — the lease, my communications "
            "with Alexia, the messages where she told me I could come and stay "
            "'two to three weeks', the terms of the Notice. Constable Bickery "
            "did not log that packet. He left it inside the apartment with "
            "Laura Phillips. He left my exculpatory evidence with the woman "
            "whose evidence was being used against me.",
        ],
    ),
    Section(
        "24 February 2025, evening — at my mother's house, the night before the strike-out",
        paragraphs=[
            "On the evening of 24 February 2025, Constables Davies and Bickery "
            "came to my mother's house. Constable Davies's body-worn camera was "
            "running. That recording was withheld from the original Filed Brief "
            "of Evidence. The filename itself records the exclusion: 'Not "
            "contained with original FBOE — Not relevant to offence.' I only "
            "received it through an RTI release.",
            "On that recording, in the presence of Constable Bickery, who said "
            "nothing to correct him, Constable Davies said the following on his "
            "own camera:",
            "He said, at 12 minutes 57 seconds: 'And we have to defer to the "
            "judgment of our other police that have made that call that Alexia "
            "was in need of protection. And we don't reinvestigate that and we "
            "don't say, oh, no, we've spoken to his mum and his family and we "
            "don't think that's the case. That's not how it works.'",
            "He said, at 31 minutes 44 seconds: 'alexia was 2 000 kilometres "
            "away that's right that's why he went there when she was away "
            "because he was told that he could enter that place. His name's "
            "still in the lease. His belongings are still there.'",
            "He said, at 7 minutes 52 seconds: 'he was informed that he could "
            "go to that unit his name's still on the lease and alexia… she "
            "said two to three weeks can cory come and stay here two to three "
            "weeks.'",
            "He said, at 23 minutes 55 seconds: 'doesn't sound like he had the "
            "intent of taking the dog'.",
            "He said, at 27 minutes 16 seconds, about the stalking charge: "
            "'the harassment side of that are some emails that he sent to "
            "alexia but also her family.'",
            "My mother told Constable Davies on the same recording that Alexia "
            "had been to prison in America for domestic violence. Constable "
            "Davies said: 'I've been told about that yeah.'",
            "My mother also told him that on 1 December 2024 one of Alexia's "
            "friends had said to her: 'I'll try and get cory charged about the "
            "animals.'",
            "The next morning the Magistrate struck out the Notice.",
        ],
    ),
    Section(
        "25 February 2025 — the foundation collapses",
        paragraphs=[
            "On 25 February 2025 Magistrate Brunello formally withdrew and "
            "struck out the application. Form 44 Notice of Discontinuance.",
            "Six months later, on 21 August 2025 at 7:20 p.m., the officer who "
            "issued the original Notice — Senior Constable Yaun himself — "
            "emailed me. He wrote in his own words: 'My original application "
            "for a DVO was struck out of Court several months ago upon my "
            "submission of no evidence from the aggrieved. I believe another "
            "application may have been made by another officer from Southport "
            "who incorrectly used my original Police occurrence. I have had no "
            "further involvement in your matters.'",
            "Two admissions in one email from the man who issued the original "
            "Notice. There was no evidence. And Southport reused his case "
            "number to keep going.",
            "On the same 25 February, Alexia attended Southport Police Station "
            "for the first time to give a formal sworn statement. That was two "
            "days after they had locked me out. The decision to lock me out and "
            "arrest me was made on phone calls from Perth before any sworn "
            "statement existed.",
        ],
    ),
    Section(
        "22 March 2025 — Romeo taken from me at the petrol station",
        paragraphs=[
            "Four weeks later I was sitting in my car in a Supercheap car park. "
            "An officer told me on his own body-worn camera: 'We were just "
            "patrolling and I saw the car, saw you sitting in it.'",
            "By the time the seizure was complete I had asked, more than once, "
            "to call my solicitor. I was not given the chance.",
            "On the recording I told the officer Alexia had been in Perth at "
            "the time of the alleged breach. I told him the Notice had been "
            "struck out. I had the breeder receipt and the Gold Coast Council "
            "registration in the car.",
            "The officer's reply, in his own words: 'regardless of what "
            "paperwork he has, we've got to seize the dog and then he's got to "
            "go through the courts to get the dog back.'",
            "Constable Contacos: 'I've got pictures of it, alright?' That was "
            "the basis of identifying Romeo as the allegedly stolen dog. "
            "Photographs given to him by Alexia. Not a microchip, not a vet "
            "record, not my registration.",
            "In court in August 2025 the police admitted, for the first time, "
            "that they had already given Romeo to Alexia before any court "
            "order. The Magistrate dismissed the application I had filed and "
            "refused to award costs to the police.",
        ],
    ),
    Section(
        "May 2025 — eleven days after I filed an RTI",
        paragraphs=[
            "On 13 May 2025 I lodged a Right to Information application through "
            "Smart Service Queensland.",
            "Eleven days later, on 24 May 2025 at 3:39 a.m., I was stopped at "
            "a petrol station — I was walking to my car, not driving in motion "
            "— and an oral fluid specimen was taken from me. Specimen 22403-"
            "30264.",
            "The same eleven-day interval shows up in a second place. The "
            "forensic laboratory escalated my specimen to Priority 1 eleven "
            "days after the same RTI lodgement.",
            "Between collection at 3:39 a.m. on 24 May and receipt at the lab "
            "at 8:18 a.m. on 26 May there is a 52.6-hour gap with no "
            "temperature logs.",
            "The lab has since given three different stories about what "
            "happened to the specimen — 'destroyed or consumed', 'consumed', "
            "and 'stored but not viable'. Destruction during ongoing "
            "proceedings is against the statute and against the property "
            "receipt mandate.",
            "I was on prescribed Lisdexamfetamine (Vyvanse), Fluoxetine and "
            "Quetiapine at the time. I told the officer at the time. Without "
            "the laboratory's confirmatory data — ion ratios, retention times "
            "— nobody can say whether the result was the metabolites of my "
            "prescribed medicine or something else.",
        ],
    ),
    Section(
        "Throughout 2025 to 2026 — what happened to my family",
        paragraphs=[
            "After the arrest, a Queensland Police member changed my recorded "
            "residential address in QPRIME from Unit 104, 158 Scarborough "
            "Street, Southport to 207W 1 Marina Drive, Benowa. That is my "
            "mother's address. Nobody asked me. Nobody verified it. There was "
            "no evidence I lived there. I documented the change in writing in "
            "my RTI application of 18 May 2025.",
            "On the basis of that wrong record, police visited my mother's "
            "address at night. Letters were sent to that address claiming I "
            "lived there. A neighbour lodged an overcrowding complaint. My "
            "mother, my sister, and my sister's baby were evicted.",
            "I had to change my phone number because of ongoing enforcement "
            "contact.",
            "I have been homeless during parts of this. I told Constable Joe "
            "Butler so on his body-worn camera on 22 March 2025. I told him on "
            "the same recording that I had already lodged a harassment "
            "complaint against Southport police. He did not dispute it.",
        ],
    ),
]


THE_EXHIBITS = [
    Exhibit(
        "1",
        "The Police Protection Notice itself — QP0899",
        "The Notice issued on 1 December 2024 by Robina Police.",
        [
            "The conditions box reads: 'must be of good behaviour towards the "
            "aggrieved and must not commit domestic violence against the "
            "aggrieved.' That is all.",
            "There is no no-contact condition.",
            "There is no order excluding me from the unit.",
            "There is no ouster.",
            "Alexia's own sworn statement of 25 February 2025 at paragraph 3 "
            "recites the same two conditions. The aggrieved herself confirms "
            "the Notice contained nothing more than these.",
        ],
    ),
    Exhibit(
        "2",
        "Senior Constable Yaun's email of 21 August 2025",
        "An email I received from the very officer who issued the Notice.",
        [
            "He told me, in writing: 'My original application for a DVO was "
            "struck out of Court several months ago upon my submission of no "
            "evidence from the aggrieved.'",
            "He told me, in the same email: 'I believe another application may "
            "have been made by another officer from Southport who incorrectly "
            "used my original Police occurrence.'",
            "He told me: 'I have had no further involvement in your matters.'",
        ],
        quote=(
            "My original application for a DVO was struck out of Court several "
            "months ago upon my submission of no evidence from the aggrieved."
        ),
    ),
    Exhibit(
        "3",
        "The Form 9 Entry Notice email — 19 February 2025, 4:36 a.m.",
        "An email from the property manager Denis Constable to Alexia.",
        [
            "It reads: 'Hi Alexia. Cory wishes to pick up his possessions "
            "tomorrow at 9am please.'",
            "It is dated four days before the police say I entered without "
            "authority.",
            "It is the lessor's agent giving me permission, in writing, to "
            "enter for property recovery.",
        ],
        quote="Hi Alexia. Cory wishes to pick up his possessions tomorrow at 9am please.",
    ),
    Exhibit(
        "4",
        "Alexia's own emails of 19 February 2025",
        "Two emails Alexia sent from Perth, four days before the police say I breached.",
        [
            "At 7:26 a.m. she wrote: 'I'm not home... while I am on holiday.'",
            "At 9:29 a.m. she wrote: 'a legal civil case that he is required "
            "to obtain a lawyer for and dispute me for these items.'",
            "She herself, in writing, four days before the alleged breach, "
            "called this a civil case.",
        ],
        quote=(
            "a legal civil case that he is required to obtain a lawyer for and "
            "dispute me for these items"
        ),
    ),
    Exhibit(
        "5",
        "My iPhone Police Link call log — 7:51 p.m., 23 February 2025",
        "The call I made to Police Link before I entered the apartment.",
        [
            "Call started at 19:51 on 23 February 2025.",
            "Duration: 36 minutes.",
            "Phillips's text to Alexia, on Alexia's own statement at paragraph "
            "27, is at 7:51 p.m. — the same time the call started.",
            "I was on the phone with the police while I was in my own "
            "apartment.",
        ],
    ),
    Exhibit(
        "6",
        "Constable Easthope's body-worn camera — Initial Response",
        "The arrival briefing and the lockout in real time.",
        [
            "At 02:00 he said: 'going to enter the property he's got the key "
            "and he's got a lease… it's his lease, his bottom and it's his "
            "key, so he's entering the property to get stuff out.'",
            "At 14:25 he said to me: 'so technically you can be here.'",
            "At 17:14 he said: 'she's told him the wrong conditions because "
            "technically he's allowed to be here.'",
            "At 18:18 he said: 'is on the way back right now she's on the "
            "plane.'",
            "At 21:55 he asked Laura Phillips: 'do you have any forms that "
            "show you're on the lease here?' Her answer at 21:57: 'I don't "
            "have any forms that show that I'm on the lease here.'",
            "At 22:20 he said: 'we don't know who owns the place.'",
            "This is the officer of the call recording all of this on his own "
            "camera, before they locked me out.",
        ],
        quote=(
            "he's got the key and he's got a lease... it's his lease, his "
            "bottom and it's his key"
        ),
    ),
    Exhibit(
        "7",
        "The property manager telephones the police at 1:54 a.m.",
        "Denis Constable's contemporaneous telephone warning to Bickery and Harmer during the lockout.",
        [
            "He told them in express words: 'Form 13 does NOT terminate the "
            "lease.'",
            "He told them this during the lockout itself. They were on express "
            "notice that the action they were taking was unlawful.",
            "His sworn statutory declaration (AFF11) records the same warning "
            "in his own words.",
            "On Constable Easthope's body-worn camera, the property manager "
            "told the police: 'they're both allowed to be there, but the third "
            "party' is the questionable one. The 'third party' is Laura "
            "Phillips.",
        ],
        quote="Form 13 does NOT terminate the lease.",
    ),
    Exhibit(
        "8",
        "Constable Davies's body-worn camera at my mother's house",
        "The recording that was withheld from the original Filed Brief of Evidence. Filename: 'Not contained with original FBOE — Not relevant to offence.'",
        [
            "At 12:57: 'And we have to defer to the judgment of our other "
            "police that have made that call that Alexia was in need of "
            "protection. And we don't reinvestigate that.'",
            "At 31:44: 'alexia was 2 000 kilometres away… because he was "
            "told that he could enter that place. His name's still in the "
            "lease. His belongings are still there.'",
            "At 7:52: he confirms he had seen Alexia's messages inviting me to "
            "stay 'two to three weeks'.",
            "At 23:55: 'doesn't sound like he had the intent of taking the "
            "dog'.",
            "At 27:16: he confirms the 'stalking' framing is in fact emails "
            "to Alexia and her family.",
            "At 31:13: he confirms he had already been told about Alexia's "
            "US criminal history.",
            "At 2:43: he confirms the keys taken off me were 'a master key for "
            "that Scion unit… it gets into everywhere in that building.'",
            "Constable Bickery was present. He did not correct any of it.",
            "All of this was said the night before the Magistrate struck out "
            "the Notice.",
        ],
        quote=(
            "we have to defer to the judgment of our other police... we don't "
            "reinvestigate that... That's not how it works"
        ),
    ),
    Exhibit(
        "9",
        "Constable Harmer's body-worn camera at the unit on the night of arrest",
        "My first words to police when they finally arrived.",
        [
            "At 02:39, about Laura Phillips: 'Last time I saw her was the 1st "
            "of December, she broke into this apartment, so… I do not know "
            "her. I'm not sure though. Don't even know her name.'",
            "At 02:55: 'I live here with my ex, but I went down to her funeral "
            "and I said she could stay here 2-3 weeks.'",
            "At 03:57: 'So I took a week to confirm that my name was on the "
            "lease, had to confirm it with the RTA, printed out the documents, "
            "had to confirm it with the management, because my bond's still "
            "there.'",
            "At 04:37: I told the officer the Notice came from a household "
            "argument about there being too many cats for the lease limit.",
            "At 06:03: I told the officer the Notice required Alexia to leave, "
            "not me.",
            "At 07:39: 'And this girl told me, she emailed something and "
            "we're stalking her and we've never even seen her in her life.'",
        ],
    ),
    Exhibit(
        "10",
        "Laura Phillips's own bedroom video — 191 seconds",
        "Her own self-filmed recording on her own phone.",
        [
            "At 00:21 she says the police told her to hide in the bedroom — "
            "she was on the phone with them throughout.",
            "At 00:30 my voice on the recording: 'you're getting filmed so "
            "every false accusation will be shown'.",
            "At 00:39 my voice: 'you're trying to occupy my home'.",
            "At 01:30 she says 'I think he's in your room now'. I was not in "
            "the room. I was in the kitchen, then leaving. Her own paragraph "
            "10 of her statement places me in the kitchen, not the bedroom.",
            "At 01:33 she demands her key back — she has no lease and no key "
            "of her own.",
            "At 01:45 she says, in her own words: 'you are safe to leave.'",
            "At 02:00 she says, in her own words: 'he broke the thing off the "
            "wall that I put to stop him from opening the door' — she is "
            "admitting she built the barricade, and that the damage was to "
            "her own barricade as I was leaving.",
            "At 02:24 she says, in her own words: 'Are we fucking scared?'",
            "Throughout the video she argues with me, films me, demands her "
            "key back, calls me names, and invokes legal authority. None of "
            "that is what someone in genuine, imminent fear does.",
        ],
        quote=(
            "you are safe to leave ... Are we fucking scared? ... he broke the "
            "thing off the wall that I put to stop him from opening the door"
        ),
    ),
    Exhibit(
        "11",
        "Tom Balsey's affidavit — AFF12",
        "My friend's sworn statement. He drove with me to the unit that night and was filming.",
        [
            "He records that the police were 500 metres away and did not come "
            "for six hours.",
            "He records that on 1 December 2024 Alexia 'returned around "
            "midnight with five friends' and 'reportedly took the couple's / "
            "Cory's dog'.",
            "He records his long-standing observation of the relationship and "
            "of Alexia's dependency on me.",
            "He confirms I drove to his house with a van of my belongings — "
            "this was a property-recovery trip, not a dog-theft trip.",
        ],
    ),
    Exhibit(
        "12",
        "Denis Constable's statutory declaration — AFF11",
        "The property manager's sworn statement.",
        [
            "At paragraphs 7 to 9 he confirms the joint tenancy commenced on "
            "10 April 2023.",
            "At paragraph 29 he records his telephone call to Constables "
            "Bickery and Harmer at 1:54 a.m. on 24 February 2025: 'Form 13 "
            "does NOT terminate the lease.'",
            "He records the police asking him to reactivate my fob — at the "
            "same time they were arresting me.",
            "He records that across years he found me 'consistently helpful "
            "and devoted'.",
        ],
    ),
    Exhibit(
        "13",
        "The Field Property Receipt 137237",
        "What the police listed they took from me on the night of arrest.",
        [
            "The receipt lists: '1 x dog'. That is all.",
            "It does not list my iPhone. They took my iPhone.",
            "It does not list the printed packet of evidence Tom Balsey gave "
            "Constable Bickery at the scene. They left that packet at the unit "
            "with Laura Phillips.",
        ],
    ),
    Exhibit(
        "14",
        "The withheld body-worn camera serials",
        "Three serial numbers that the OIC External Review 318762 agreed should be released to me, and which have not been produced.",
        [
            "X60508355 — Constable Bickery's own body-worn camera, identified in "
            "his sworn statement at paragraph 3.",
            "X60507687 — Constable Easthope's own body-worn camera, identified "
            "in his sworn statement at paragraph 5.",
            "X60500949 — third serial agreed for release.",
            "Two of these are the arresting officers' own cameras, covering "
            "the operative event.",
        ],
    ),
    Exhibit(
        "15",
        "The Constable Shepherd anomaly in Constable Harmer's sworn statement",
        "An error in the prosecution brief that names me as one of the officers who arrested me.",
        [
            "Constable Harmer's sworn statement of facts reads: 'Constable "
            "SHEPHERD and Constable BICKERY placed Cory under arrest.'",
            "The named arresting officer is me, the person being arrested.",
            "Either the statement was generated from a template and copied "
            "without verification, or the name was inserted incorrectly. "
            "Either way, the document is signed under oath.",
        ],
    ),
    Exhibit(
        "16",
        "My medical and prescription records",
        "Documents that show the medications I was on at the relevant time.",
        [
            "Lisdexamfetamine (Vyvanse), Fluoxetine, and Quetiapine — all "
            "prescribed.",
            "Diagnoses of PTSD, MDD and anxiety on the record.",
            "I told the officer about my medications and the Vicks inhaler at "
            "the time the oral fluid specimen was taken.",
        ],
    ),
    Exhibit(
        "17",
        "My 1 March 2026 statutory complaint to Forensic Science Queensland",
        "Filed in respect of specimen 22403-30264.",
        [
            "A 52.6-hour gap between collection at 3:39 a.m. on 24 May 2025 "
            "and receipt at the lab at 8:18 a.m. on 26 May 2025.",
            "No temperature logs for that period.",
            "Three contradictory statements about disposition of the specimen.",
            "ISO/IEC 17025:2017 Clauses 7.4, 7.5, 7.8, 8.4 are engaged. "
            "Section 80AA TORUM is engaged.",
        ],
    ),
    Exhibit(
        "18",
        "RTI/54169 and OIC External Review 318762",
        "My Right to Information application and the resulting external review.",
        [
            "RTI lodged 13 May 2025 via Smart Service Queensland.",
            "On 18 May 2025 I wrote, in my own words: 'A QPS member has "
            "changed my residential address... from 104 158 Scarborough street "
            "Southport to 207W 1 Marina Drive Benowa without any verification, "
            "request, or evidence.'",
            "Eleven days after the RTI: the petrol-station stop.",
            "Eleven days after the RTI: the laboratory escalation of the "
            "specimen to Priority 1.",
            "The External Review agreed three body-worn camera serials for "
            "release. They have not been produced.",
        ],
    ),
    Exhibit(
        "19",
        "My contemporaneous emails to Senior Constable Yaun",
        "What I wrote to the issuing officer on 21 August 2025 at 7:08 p.m.",
        [
            "'Alexia's statements were false; she was not in refuge for four "
            "days. During that time, she was at home, and I was providing her "
            "dinner and transportation.'",
            "Yaun replied at 7:20 p.m. with the strike-out admission "
            "(Exhibit 2).",
        ],
    ),
    Exhibit(
        "20",
        "The Miami-Dade public criminal record",
        "Alexia's documented prior matter in the United States.",
        [
            "Court Case M18017586 / State Case 132018MM0175860001XX.",
            "Arrest 21 June 2018, Miami Beach Police Department.",
            "Charge: BATTERY MISDEMEANOR.",
            "Intake Unit: MISD DOMESTIC VIOLENCE.",
            "Pretrial conditional Stay Away Order against Piergiorgio Gerace.",
            "Disposition NOLLE PROS.",
            "Constable Davies confirmed on his body-worn camera at my mother's "
            "house: 'I've been told about that yeah.'",
        ],
    ),
    Exhibit(
        "21",
        "Constable Joe Butler's body-worn camera — 22 March 2025",
        "What I told a different unit's officer four weeks after the lockout.",
        [
            "I told him I had no home.",
            "I told him I had already lodged a harassment complaint against "
            "Southport police.",
            "I told him the Notice had said Alexia was supposed to leave, not "
            "me, and here I was homeless.",
            "He did not dispute any of it.",
        ],
    ),
]


WHAT_I_ASK = Section(
    "What I am asking the Commission to do",
    paragraphs=[
        "I am asking the Commission to record findings that on 23–24 February "
        "2025, and in the conduct that has continued since, Queensland Police "
        "acted incompatibly with my human rights and failed to give proper "
        "consideration to my rights when they made the decisions that affected "
        "me.",
        "I am asking for the body-worn camera serials X60508355, X60507687, "
        "and X60500949 to be produced, and for Constable Davies's 5-page "
        "statement, which the Index says was 'to be provided', to be produced.",
        "I am asking for my iPhone, seized on 24 February 2025 and never "
        "forensically examined, to be returned to me with a documented chain "
        "of custody.",
        "I am asking for an acknowledgement that the QPRIME residential-address "
        "change to my mother's address, made without verification, was wrong, "
        "and that the consequences for my mother, my sister and my sister's "
        "baby were caused by it.",
        "I am asking for the matter to be referred for systemic remedies — "
        "training and policy on the 'we don't reinvestigate' admission "
        "captured on Constable Davies's body-worn camera — so that the same "
        "operational policy cannot produce the same outcome for someone else.",
        "I am asking for compensation that reflects the direct loss, the "
        "consequential loss, the loss to my family, and the twelve months of "
        "court attendances that followed a Notice the Magistrate struck out on "
        "no evidence the morning after my arrest.",
    ],
)


# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------

CSS = """
:root { color-scheme: light; }
body {
  font-family: Georgia, "Times New Roman", serif;
  max-width: 820px;
  margin: 40px auto;
  padding: 0 24px 64px;
  color: #1a1a1a;
  line-height: 1.55;
  background: #fafafa;
}
h1, h2, h3 { font-family: Georgia, serif; }
h1 { font-size: 2em; margin-bottom: 0.2em; }
.subtitle { color: #555; font-style: italic; font-size: 1.05em; margin-top: 0; }
.meta { color: #555; font-size: 0.95em; margin: 0.5em 0 2.5em; }
h2 { border-bottom: 2px solid #1a1a1a; padding-bottom: 6px; margin-top: 2.2em; }
h3 { margin-top: 1.8em; color: #222; }
ul { padding-left: 1.3em; }
li { margin: 0.35em 0; }
blockquote {
  border-left: 4px solid #555;
  margin: 1em 0;
  padding: 0.4em 1em;
  background: #f0f0f0;
  font-style: italic;
  color: #222;
}
.exhibit {
  border: 1px solid #bbb;
  border-radius: 6px;
  padding: 14px 22px;
  margin: 1.6em 0;
  background: #fff;
  page-break-inside: avoid;
}
.exhibit-number {
  display: inline-block;
  background: #1a1a1a;
  color: #fff;
  padding: 2px 10px;
  border-radius: 3px;
  font-size: 0.85em;
  font-weight: bold;
  letter-spacing: 0.04em;
  margin-right: 0.5em;
}
.exhibit-name { font-weight: bold; font-size: 1.1em; }
.exhibit-what { color: #444; font-style: italic; margin: 0.6em 0; }
hr { border: none; border-top: 1px solid #ccc; margin: 2.4em 0; }
@media print {
  body { background: #fff; max-width: 100%; margin: 0; padding: 1.4cm; }
  h2 { page-break-after: avoid; }
  .exhibit { page-break-inside: avoid; }
}
"""


def html_paragraphs(paragraphs: list[str]) -> str:
    return "\n".join(f"<p>{html.escape(p)}</p>" for p in paragraphs)


def html_bullets(bullets: list[str]) -> str:
    if not bullets:
        return ""
    return "<ul>\n" + "\n".join(f"  <li>{html.escape(b)}</li>" for b in bullets) + "\n</ul>"


def build_html() -> str:
    parts: list[str] = []
    parts.append("<!DOCTYPE html>")
    parts.append("<html lang='en'><head><meta charset='utf-8'>")
    parts.append(f"<title>{html.escape(TITLE)}</title>")
    parts.append(f"<style>{CSS}</style></head><body>")
    parts.append(f"<h1>{html.escape(TITLE)}</h1>")
    parts.append(f"<p class='subtitle'>{html.escape(SUBTITLE)}</p>")
    parts.append(f"<p class='meta'>{html.escape(AUTHOR)} &middot; {html.escape(MATTER)}</p>")

    parts.append(f"<h2>{html.escape(OPENING.heading)}</h2>")
    parts.append(html_paragraphs(OPENING.paragraphs))

    parts.append("<h2>What happened</h2>")
    for sec in WHAT_HAPPENED:
        parts.append(f"<h3>{html.escape(sec.heading)}</h3>")
        parts.append(html_paragraphs(sec.paragraphs))
        if sec.bullets:
            parts.append(html_bullets(sec.bullets))

    parts.append("<h2>The exhibits</h2>")
    for ex in THE_EXHIBITS:
        parts.append("<div class='exhibit'>")
        parts.append(
            f"<div><span class='exhibit-number'>Exhibit {html.escape(ex.number)}</span>"
            f"<span class='exhibit-name'>{html.escape(ex.name)}</span></div>"
        )
        parts.append(f"<p class='exhibit-what'>{html.escape(ex.what_it_is)}</p>")
        parts.append(html_bullets(ex.what_it_shows))
        if ex.quote:
            parts.append(f"<blockquote>{html.escape(ex.quote)}</blockquote>")
        parts.append("</div>")

    parts.append(f"<h2>{html.escape(WHAT_I_ASK.heading)}</h2>")
    parts.append(html_paragraphs(WHAT_I_ASK.paragraphs))

    parts.append("</body></html>")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# PDF (reportlab)
# ---------------------------------------------------------------------------

def build_pdf(path: Path) -> None:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.lib.enums import TA_LEFT
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, Table, TableStyle,
        ListFlowable, ListItem,
    )
    from reportlab.lib.colors import HexColor, black

    styles = getSampleStyleSheet()
    body = ParagraphStyle(
        "body",
        parent=styles["BodyText"],
        fontName="Times-Roman",
        fontSize=11,
        leading=15,
        spaceBefore=4,
        spaceAfter=8,
        alignment=TA_LEFT,
    )
    title_s = ParagraphStyle(
        "title", parent=styles["Title"], fontName="Times-Bold", fontSize=22, leading=26,
    )
    subtitle_s = ParagraphStyle(
        "subtitle", parent=styles["BodyText"], fontName="Times-Italic", fontSize=12,
        leading=15, spaceAfter=4, textColor=HexColor("#555"),
    )
    meta_s = ParagraphStyle(
        "meta", parent=styles["BodyText"], fontName="Times-Roman", fontSize=10,
        textColor=HexColor("#555"), spaceAfter=18,
    )
    h2 = ParagraphStyle(
        "h2", parent=styles["Heading2"], fontName="Times-Bold", fontSize=15, leading=20,
        spaceBefore=18, spaceAfter=8,
    )
    h3 = ParagraphStyle(
        "h3", parent=styles["Heading3"], fontName="Times-Bold", fontSize=12.5, leading=16,
        spaceBefore=12, spaceAfter=4,
    )
    quote_s = ParagraphStyle(
        "quote", parent=body, fontName="Times-Italic", leftIndent=18, rightIndent=12,
        textColor=HexColor("#222"), spaceBefore=4, spaceAfter=6,
    )
    exhibit_name_s = ParagraphStyle(
        "ex_name", parent=styles["Heading3"], fontName="Times-Bold", fontSize=12,
        leading=15, spaceBefore=2, spaceAfter=2,
    )
    exhibit_what_s = ParagraphStyle(
        "ex_what", parent=body, fontName="Times-Italic", fontSize=10.5, leading=13,
        spaceBefore=0, spaceAfter=6, textColor=HexColor("#444"),
    )

    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=2.2 * cm,
        rightMargin=2.2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title=TITLE,
        author=AUTHOR,
    )
    story = []

    def para(text: str, style=body):
        story.append(Paragraph(text.replace("\n", "<br/>"), style))

    def bullets(items: list[str]):
        if not items:
            return
        flowables = [ListItem(Paragraph(i, body), leftIndent=14) for i in items]
        story.append(
            ListFlowable(flowables, bulletType="bullet", start="•", leftIndent=14, spaceBefore=2, spaceAfter=6)
        )

    para(TITLE, title_s)
    para(SUBTITLE, subtitle_s)
    para(f"{AUTHOR} &nbsp;&middot;&nbsp; {MATTER}", meta_s)

    para(OPENING.heading, h2)
    for p in OPENING.paragraphs:
        para(p)

    para("What happened", h2)
    for sec in WHAT_HAPPENED:
        para(sec.heading, h3)
        for p in sec.paragraphs:
            para(p)
        if sec.bullets:
            bullets(sec.bullets)

    para("The exhibits", h2)
    for ex in THE_EXHIBITS:
        block = []
        block.append(Paragraph(f"<b>Exhibit {ex.number}</b> &nbsp; {ex.name}", exhibit_name_s))
        block.append(Paragraph(ex.what_it_is, exhibit_what_s))
        sub_bullets = [ListItem(Paragraph(s, body), leftIndent=14) for s in ex.what_it_shows]
        if sub_bullets:
            block.append(
                ListFlowable(sub_bullets, bulletType="bullet", start="•", leftIndent=14, spaceBefore=2, spaceAfter=4)
            )
        if ex.quote:
            block.append(Paragraph(f"&ldquo;{ex.quote}&rdquo;", quote_s))
        # Wrap in a single-cell table for the bordered look
        wrapped = Table(
            [[block]],
            colWidths=[doc.width],
            style=TableStyle([
                ("BOX", (0, 0), (-1, -1), 0.4, HexColor("#999")),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("BACKGROUND", (0, 0), (-1, -1), HexColor("#ffffff")),
            ]),
        )
        story.append(KeepTogether(wrapped))
        story.append(Spacer(1, 8))

    para(WHAT_I_ASK.heading, h2)
    for p in WHAT_I_ASK.paragraphs:
        para(p)

    doc.build(story)


# ---------------------------------------------------------------------------
# PowerPoint (python-pptx)
# ---------------------------------------------------------------------------

def build_pptx(path: Path) -> None:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank = prs.slide_layouts[6]

    DARK = RGBColor(0x1a, 0x1a, 0x1a)
    MID = RGBColor(0x55, 0x55, 0x55)
    LIGHT = RGBColor(0xee, 0xee, 0xee)
    ACCENT = RGBColor(0x33, 0x33, 0x33)

    def add_text(slide, left, top, width, height, text, *, size=18, bold=False,
                 color=DARK, italic=False, align=PP_ALIGN.LEFT):
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = True
        # First paragraph
        para = tf.paragraphs[0]
        para.alignment = align
        run = para.add_run()
        run.text = text
        run.font.name = "Calibri"
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = color
        return tb

    def add_bullets(slide, left, top, width, height, items, *, size=16, color=DARK):
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = True
        for i, item in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = PP_ALIGN.LEFT
            p.level = 0
            run = p.add_run()
            run.text = "•  " + item
            run.font.name = "Calibri"
            run.font.size = Pt(size)
            run.font.color.rgb = color
            p.space_after = Pt(6)
        return tb

    def title_slide():
        slide = prs.slides.add_slide(blank)
        add_text(slide, Inches(0.6), Inches(2.2), Inches(12), Inches(1.4),
                 TITLE, size=44, bold=True)
        add_text(slide, Inches(0.6), Inches(3.7), Inches(12), Inches(0.8),
                 SUBTITLE, size=22, italic=True, color=MID)
        add_text(slide, Inches(0.6), Inches(5.4), Inches(12), Inches(0.5),
                 AUTHOR, size=18, color=MID)
        add_text(slide, Inches(0.6), Inches(5.95), Inches(12), Inches(0.5),
                 MATTER, size=14, color=MID)

    def section_divider(label):
        slide = prs.slides.add_slide(blank)
        add_text(slide, Inches(0.6), Inches(3), Inches(12), Inches(1.2),
                 label, size=40, bold=True)

    def content_slide(heading, paragraphs=None, bullets=None, quote=None,
                      mini_heading=None):
        slide = prs.slides.add_slide(blank)
        add_text(slide, Inches(0.6), Inches(0.4), Inches(12), Inches(0.9),
                 heading, size=26, bold=True)
        y = Inches(1.5)
        if mini_heading:
            add_text(slide, Inches(0.6), y, Inches(12), Inches(0.5),
                     mini_heading, size=16, italic=True, color=MID)
            y += Inches(0.55)
        if paragraphs:
            for p in paragraphs:
                tb = add_text(slide, Inches(0.6), y, Inches(12), Inches(1.2),
                              p, size=15)
                # rough height advance based on text length
                lines = max(1, len(p) // 90 + p.count("\n") + 1)
                y += Inches(0.32 * lines + 0.1)
        if bullets:
            tb = add_bullets(slide, Inches(0.6), y, Inches(12), Inches(5),
                             bullets, size=15)
            y += Inches(0.4 * len(bullets))
        if quote:
            qb = slide.shapes.add_textbox(Inches(0.6), Inches(6.0), Inches(12), Inches(1.2))
            tf = qb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT
            run = p.add_run()
            run.text = "“" + quote + "”"
            run.font.italic = True
            run.font.size = Pt(15)
            run.font.color.rgb = ACCENT

    def exhibit_slide(ex: Exhibit):
        slide = prs.slides.add_slide(blank)
        # number badge
        badge = slide.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(2.2), Inches(0.6))
        tf = badge.text_frame
        tf.word_wrap = False
        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = f"EXHIBIT {ex.number}"
        run.font.name = "Calibri"
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0xff, 0xff, 0xff)
        # Add a coloured fill to the badge
        badge.fill.solid()
        badge.fill.fore_color.rgb = DARK
        badge.line.fill.background()
        # name
        add_text(slide, Inches(2.95), Inches(0.4), Inches(10), Inches(0.7),
                 ex.name, size=22, bold=True)
        # what it is
        add_text(slide, Inches(0.6), Inches(1.2), Inches(12), Inches(0.7),
                 ex.what_it_is, size=15, italic=True, color=MID)
        # bullets
        add_bullets(slide, Inches(0.6), Inches(1.95), Inches(12), Inches(5),
                    ex.what_it_shows, size=14)
        # quote
        if ex.quote:
            qb = slide.shapes.add_textbox(Inches(0.6), Inches(6.3), Inches(12), Inches(1.0))
            tf = qb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            run = p.add_run()
            run.text = "“" + ex.quote + "”"
            run.font.italic = True
            run.font.size = Pt(15)
            run.font.color.rgb = ACCENT

    # ----- build -----
    title_slide()

    # Opening
    section_divider("Who I am, and what I am asking for")
    content_slide(OPENING.heading, paragraphs=OPENING.paragraphs)

    # What happened
    section_divider("What happened")
    for sec in WHAT_HAPPENED:
        # If the section has too many paragraphs for one slide, split
        paras = sec.paragraphs[:]
        chunk_size = 3
        chunks = [paras[i:i + chunk_size] for i in range(0, len(paras), chunk_size)]
        for idx, chunk in enumerate(chunks):
            heading = sec.heading if idx == 0 else sec.heading + " (continued)"
            content_slide(heading, paragraphs=chunk)

    # Exhibits
    section_divider("The exhibits")
    for ex in THE_EXHIBITS:
        exhibit_slide(ex)

    # What I am asking
    section_divider("What I am asking the Commission to do")
    content_slide(WHAT_I_ASK.heading, paragraphs=WHAT_I_ASK.paragraphs[:3])
    content_slide(WHAT_I_ASK.heading + " (continued)", paragraphs=WHAT_I_ASK.paragraphs[3:])

    prs.save(str(path))


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> None:
    html_path = OUT / "Shepherd_Conciliation_2026-05-14.html"
    pdf_path = OUT / "Shepherd_Conciliation_2026-05-14.pdf"
    pptx_path = OUT / "Shepherd_Conciliation_2026-05-14.pptx"

    html_path.write_text(build_html(), encoding="utf-8")
    build_pdf(pdf_path)
    build_pptx(pptx_path)

    for p in (html_path, pdf_path, pptx_path):
        print(f"  wrote {p}  ({p.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
