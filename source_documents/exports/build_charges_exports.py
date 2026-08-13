"""Generate HTML / PDF / PPTX for the current charge position.

Voice: first person, as I would put it myself. Covers the prosecution's
response of August 2026 — Charge 2 discontinued, Charges 1 and 3
continuing — and my answer to each reason they gave.
"""
from __future__ import annotations

import html
from dataclasses import dataclass, field
from pathlib import Path

OUT = Path(__file__).resolve().parent

TITLE = "Where my charges stand"
SUBTITLE = "Charge 2 discontinued. Charges 1 and 3 continuing. My answer to each reason they gave."
AUTHOR = "Cory Lea Shepherd"
MATTER = "CO-25-2722 — Southport Magistrates Court — 13 August 2026"


@dataclass
class Section:
    heading: str
    paragraphs: list[str] = field(default_factory=list)
    bullets: list[str] = field(default_factory=list)
    quote: str | None = None


@dataclass
class Exhibit:
    number: str
    name: str
    what_it_is: str
    what_it_shows: list[str]
    quote: str | None = None


OPENING = Section(
    "Where things stand today",
    paragraphs=[
        "I was charged with three things. The prosecution has now answered my "
        "submissions on all three.",
        "Charge 2 — unlawful stalking, intimidation, harassment or abuse — has "
        "been accepted and is being discontinued. That charge was on me for "
        "about eighteen months.",
        "Charge 1 — entering premises and committing an indictable offence — "
        "and Charge 3 — contravening a domestic violence order — are "
        "continuing. They gave three reasons for Charge 1. They gave no "
        "reasons at all for Charge 3.",
        "What follows is my answer to each of those reasons, and what I say "
        "the police did that they had no power to do.",
    ],
)


BODY = [
    Section(
        "Charge 2 is gone, and it should never have been there",
        paragraphs=[
            "The stalking charge is being discontinued. I want to be clear "
            "about what that means, because it is not a small thing.",
            "On 24 February 2025 — the second day — Constable Davies described "
            "that same charge on his own body-worn camera, standing in my "
            "mother's house. He said it was a blanket charge, and that the "
            "substance of it was emails I had sent to Alexia and to her family.",
            "So the officer who charged me knew on day two what that charge "
            "actually was. It stayed on me for eighteen months anyway. Now the "
            "prosecution has accepted it cannot stand.",
            "The whole 'stalking' idea came from Laura Phillips emailing police "
            "to say we were stalking her. I had never met her before that "
            "night. I said so to the first officer who spoke to me: 'we've "
            "never even seen her in her life.'",
        ],
        quote=(
            "it's a blanket charge i believe it's stalk harass intimidate that "
            "they all fall under the one umbrella right and so the harassment "
            "side of that are some emails that he sent to alexia but also her "
            "family"
        ),
    ),
    Section(
        "What Charge 1 actually requires them to prove",
        paragraphs=[
            "Charge 1 is section 421(2) — entering premises AND committing an "
            "indictable offence inside them. It has two parts. They have to "
            "prove both.",
            "They have not said in their letter what the second part is. It can "
            "only be stealing the dog, because their third reason is that the "
            "dog belonged to Alexia. There is no separate stealing charge on "
            "the indictment. Stealing is being run inside Charge 1.",
            "Charge 3 cannot be about me entering, because the order had no "
            "condition keeping me away from the unit. The only conditions were "
            "be of good behaviour and do not commit domestic violence. So "
            "Charge 3 must also be about the dog.",
            "That means both charges that are left come down to the same "
            "question: was taking Romeo a criminal act. Everything now sits on "
            "that one point.",
        ],
    ),
    Section(
        "The version of the charge they picked tells you something",
        paragraphs=[
            "Section 421 has two limbs. The first is entering with the "
            "intention of committing an offence. The second is entering and "
            "then committing one — no intention needed at the door.",
            "They charged the second limb. They did not charge the first, and "
            "they did not charge burglary.",
            "That is because their own investigating officer said on his own "
            "camera that I did not go there intending to take the dog. They "
            "have built the charge around what their officer already admitted.",
        ],
        quote=(
            "but he's collected the dog which doesn't sound like he had the "
            "intent of taking the dog but he's taken it anyway"
        ),
    ),
    Section(
        "Their first reason — the Form 13",
        paragraphs=[
            "They say the leasing manager has given a statement that I sent a "
            "Form 13 notice of intent to leave, that it was accepted, and that "
            "I was removed.",
            "The same leasing manager told the police the exact opposite, on "
            "their own cameras, on the night.",
            "He told Constable Davies the lease-off was not accepted, because "
            "Alexia could not hold the apartment with only her name on it.",
            "He told Constable Easthope that he was not aware of me signing "
            "any notice of intent to leave, that both of us would have to sign "
            "it, and that the process had not even started.",
            "He told Constable Easthope that we were both allowed to be there, "
            "and that it was the third party — Laura Phillips — whose position "
            "was the questionable one.",
            "And at 1:54 in the morning, in the middle of the lockout, he "
            "telephoned Constables Bickery and Harmer and told them straight "
            "out that a Form 13 does not terminate the lease.",
            "So there are now two completely different accounts from the same "
            "witness. The one they are relying on came later. The one on the "
            "police cameras was on the night, and he swore the same thing in "
            "his statutory declaration.",
        ],
        quote=(
            "Both parties must sign that form, Corey and Alexia. And then "
            "there's another form to fill out for the bond… No, it hasn't even "
            "started and we're not aware of it."
        ),
    ),
    Section(
        "The new lease — this is my strongest point",
        paragraphs=[
            "Alexia herself put material before the court showing that a new "
            "lease started months later.",
            "You do not need a new lease if the old one had already ended. If "
            "my tenancy had genuinely finished in December or February, and she "
            "had simply carried on living there, there would be nothing to "
            "replace. A brand new agreement starting months afterwards means "
            "the old agreement — the one with my name on it — was still the "
            "live one until it was replaced.",
            "It also matches what the leasing manager told the police that "
            "night. He said she could not have the apartment with her name "
            "only on it. That is exactly why a new lease had to be made later.",
            "This is not my word against anybody's. It is a dated document that "
            "she filed in court herself.",
        ],
    ),
    Section(
        "The bond was never dealt with",
        paragraphs=[
            "Alexia told me that a Form 20 is the only thing that actually ends "
            "a lease. That form was only ever sent and accepted by her. I never "
            "signed it.",
            "The leasing manager said the same thing to Constable Easthope on "
            "camera. After saying both of us would have to sign the notice, he "
            "said there was another form to fill out for the bond — and that "
            "none of it had started.",
            "I told the police the same thing myself within hours of being "
            "arrested: my bond is still there, everything is still there, my "
            "name is still on the lease.",
            "The bond is not held by the agent and it is not held by either of "
            "us. It is held by the Residential Tenancies Authority. Their "
            "record will show who the contributors were, whether that was ever "
            "changed, whether it was ever refunded and to whom, and whether a "
            "new bond was lodged for a new tenancy and when.",
            "That record does not care who is asking. It either backs what I "
            "have said or it does not, and I have been saying the same thing "
            "since the night it happened.",
        ],
    ),
    Section(
        "Their second reason — that I checked and was told I was not on the lease",
        paragraphs=[
            "They say that before any of this I clarified whether I was on the "
            "lease, that I was not, and that there was therefore clearly no "
            "mistake of fact.",
            "I did check. I took a whole week to check. I confirmed it with the "
            "Residential Tenancies Authority, I printed out the documents, and "
            "I confirmed it with building management, because my bond was still "
            "there and my name was still on the lease. I said all of that to "
            "the first officer who spoke to me, on his camera, within hours.",
            "Whatever answer anyone says I was given, a man who spends a week "
            "checking with the tenancy authority and the building manager "
            "before he goes anywhere is not a man being reckless. Checking is "
            "the opposite of not caring.",
            "And Constable Davies said on his own camera that I had been "
            "informed I could go to that unit, that my name was still on the "
            "lease, and that I had been tricked.",
        ],
        quote=(
            "he was told he was informed that he could go to that unit his "
            "name's still on the lease… so that's really tricked him"
        ),
    ),
    Section(
        "Their third reason — that the dog belonged to her",
        paragraphs=[
            "I bought Romeo. My mother and I drove from the Gold Coast to "
            "Sydney on 25 October 2024 and picked him up from the breeder "
            "ourselves. I have the receipt.",
            "I registered him in my own name in Queensland with the Gold Coast "
            "City Council. That registration is older than the New South Wales "
            "transfer they are relying on.",
            "The New South Wales Pet Registry wrote to me themselves on 15 May "
            "2025 and said that once the animal moved interstate they have no "
            "authority over him.",
            "But the more important point is that ownership is not actually the "
            "test. For a stealing allegation, what matters is whether I acted "
            "in the honest belief that I had a right to. It does not matter "
            "whether I turn out to be right. It matters whether I honestly "
            "believed it.",
            "I said 'it's my dog' at the time. I said it three times in a row "
            "at the seizure a month later, with the receipt and the "
            "registration in the car with me. I have said the same thing to "
            "every officer who has asked me since.",
            "And Alexia's own messages say: I won't restrict you from the "
            "animals. All in your name now. He's always happy to see you. You "
            "can trust me too.",
            "Laura Phillips even told the police that I had said I had a text "
            "from Alexia giving me permission to walk him.",
        ],
    ),
    Section(
        "The state I was in when I signed things",
        paragraphs=[
            "I was diagnosed with major depressive disorder. That is in my "
            "medical records, along with PTSD and anxiety, and I was on "
            "prescribed medication for it.",
            "Alexia knew that. She had been my partner for five years, and she "
            "told the police about my diagnosis herself.",
            "The dog transfer she relies on was signed on 17 December 2024 — "
            "weeks after she left with her friends and took him, while I was "
            "diagnosed, medicated, and trying to hold the relationship "
            "together. The Form 13 came out of the same period.",
            "And then the protection notice itself says that I have a mental "
            "illness, that I do not take my medication, and that this makes me "
            "act crazy and fly into rages. I was taking my medication. I was "
            "working and studying. The building manager described me as "
            "consistently helpful and devoted.",
            "So the same condition was used to get the signatures out of me, "
            "and then used to tell the police I was dangerous. That is one "
            "pattern, not three coincidences.",
        ],
    ),
    Section(
        "Charge 3 — the order had no condition I could have breached",
        paragraphs=[
            "The order had two conditions. Be of good behaviour towards the "
            "aggrieved. Do not commit domestic violence against the aggrieved. "
            "That is all it said.",
            "There was no no-contact condition. There was no order excluding me "
            "from the unit. There was no ouster.",
            "Alexia's own sworn statement repeats those same two conditions and "
            "nothing else.",
            "Constable Easthope said on his own camera at the scene that she "
            "had told me the wrong conditions, because technically I was "
            "allowed to be there.",
            "And she was in Perth. Three and a half thousand kilometres away, "
            "on a plane. She never made a report to Western Australian police "
            "at any point, in the state where she actually was. Four days "
            "earlier she had put it in writing that this was a legal civil case "
            "that I needed a lawyer for.",
        ],
        quote=(
            "she's told him the wrong conditions because technically he's "
            "allowed to be here"
        ),
    ),
    Section(
        "What the police did that they had no power to do",
        paragraphs=[
            "They seized Romeo and gave him to Alexia before there was any "
            "court order. They admitted that in court in August 2025. There is "
            "no power to do that.",
            "It matters even more now. Whose dog Romeo is has become the whole "
            "case. He is the central exhibit in a live criminal proceeding, and "
            "the police handed him to the complainant. Nobody can now scan a "
            "microchip, or check an independent vet record, or trace where he "
            "went. They are asserting a fact about the dog that their own "
            "conduct made impossible to test.",
            "They took my phone and did not put it on the property receipt. "
            "Receipt 137237 lists one dog and nothing else. I told them on tape "
            "there was a message on that phone from Alexia saying I could walk "
            "him. The officer said they would not delete it and that they "
            "wanted to see what was on the phone. Fourteen months later it has "
            "never been examined and that message has never been produced.",
            "Constable Davies told the property manager to reinstate the fobs "
            "immediately because I was not the leaseholder, told him I would "
            "not be going back for the foreseeable future, and told him his "
            "conduct had obstructed police. The property manager corrected him "
            "on the lease on the same recording.",
            "Constable Bickery was handed a printed folder of my evidence at "
            "the scene by Tom Balsey — the lease, the emails, Alexia's messages "
            "inviting me to stay two to three weeks. He did not log it. He left "
            "it in the apartment with Laura Phillips.",
            "And they used domestic violence emergency powers when the person "
            "they were protecting was on a plane on the other side of the "
            "country, and had told them in writing four days before that this "
            "was a civil matter.",
            "Before I was even charged, an officer said on the recording in the "
            "van that they were going to put me on bail conditions not to go "
            "back there. The exclusion was the plan. The charge was how they "
            "got there.",
        ],
        quote=(
            "regardless of what paperwork he has, we've got to seize the dog "
            "and then he's got to go through the courts to get the dog back"
        ),
    ),
]


EXHIBITS = [
    Exhibit(
        "A",
        "The new lease filed by Alexia",
        "The tenancy agreement she put before the court, showing a commencement date months after February 2025.",
        [
            "A new lease is only necessary if the old one was still running.",
            "It matches what the leasing manager told police — that she could "
            "not hold the apartment with her name only on it.",
            "It is dated, documentary, and she filed it herself.",
        ],
    ),
    Exhibit(
        "B",
        "The RTA bond record",
        "The bond history for Unit 104, held by the Residential Tenancies Authority.",
        [
            "Who the bond contributors were, and when it was lodged.",
            "Whether any change of contributors was ever processed.",
            "Whether it was ever refunded, when, and to whom.",
            "Whether a new bond was lodged for a new tenancy, and on what date.",
            "Independent of both of us and of the agent.",
        ],
    ),
    Exhibit(
        "C",
        "The leasing manager on the police body-worn cameras",
        "Denis Constable speaking to Constable Davies and to Constable Easthope on the night of 23–24 February 2025.",
        [
            "To Davies: the lease-off was not accepted, because she could not "
            "have the apartment with her name only on it.",
            "To Easthope: he was not aware of me signing a notice of intent to "
            "leave; both parties would have to sign; there was another form "
            "needed for the bond; none of it had started.",
            "To Easthope: we were both allowed to be there — the third party "
            "was the questionable one.",
            "At 1:54 a.m., by telephone to Bickery and Harmer: a Form 13 does "
            "not terminate the lease.",
        ],
        quote="Form 13 does NOT terminate the lease.",
    ),
    Exhibit(
        "D",
        "The leasing manager's later statement",
        "The statement the prosecution is now relying on. Not yet disclosed to me.",
        [
            "It says the Form 13 was accepted and that I was removed.",
            "That is the opposite of what the same man told two police officers "
            "on camera on the night.",
            "The inconsistency needs to go on the record.",
        ],
    ),
    Exhibit(
        "E",
        "Constable Easthope's arrival briefing — 2:00 a.m.",
        "The first thing recorded when police arrived, before any decision was made.",
        [
            "'he's got the key and he's got a lease… it's his lease, his "
            "bottom and it's his key, so he's entering the property to get "
            "stuff out.'",
            "Later on the same recording: 'so technically you can be here', "
            "'she's told him the wrong conditions', 'we don't know who owns "
            "the place'.",
            "Laura Phillips on the same recording: 'I don't have any forms "
            "that show that I'm on the lease here.'",
        ],
        quote="he's got the key and he's got a lease... it's his lease, his bottom and it's his key",
    ),
    Exhibit(
        "F",
        "Constable Davies at my mother's house — 24 February 2025",
        "The recording that was left out of the original brief of evidence. Marked 'Not contained with original FBOE — Not relevant to offence'.",
        [
            "'we have to defer to the judgment of our other police… and we "
            "don't reinvestigate that… That's not how it works.'",
            "'alexia was 2 000 kilometres away… because he was told that he "
            "could enter that place. His name's still in the lease. His "
            "belongings are still there.'",
            "'doesn't sound like he had the intent of taking the dog.'",
            "'the harassment side of that are some emails that he sent to "
            "alexia but also her family.'",
            "'that's really tricked him because she said… two to three weeks "
            "can cory come and stay here.'",
            "The keys taken off me were 'a master key for that Scion unit… it "
            "gets into everywhere in that building.'",
            "All of it said the night before the Magistrate struck the order "
            "out.",
        ],
    ),
    Exhibit(
        "G",
        "Romeo's purchase and Queensland registration",
        "How I came to have him, and in whose name he was registered.",
        [
            "Bought from a Sydney breeder on 25 October 2024. My mother and I "
            "drove down and collected him ourselves.",
            "Registered in my name with the Gold Coast City Council — before "
            "the 17 December 2024 New South Wales transfer.",
            "WhatsApp, 25 October 2024, 6:34 a.m.: 'I got Romeo babe'.",
            "NSW Pet Registry, 15 May 2025: 'As you have moved the pet "
            "interstate NSW doesn't have any authority on the pet now'.",
        ],
    ),
    Exhibit(
        "H",
        "Alexia's own messages about the animals",
        "What she put in writing to me.",
        [
            "'I won't restrict you from the animals'",
            "'All in your name now'",
            "'He's always happy to see you'",
            "'You can trust me too'",
            "'I will never give away my animals'",
        ],
    ),
    Exhibit(
        "I",
        "My medical records",
        "The diagnoses and prescriptions on foot at the time the documents were signed.",
        [
            "Major depressive disorder, PTSD, anxiety.",
            "Prescribed Lisdexamfetamine, Fluoxetine and Quetiapine.",
            "The protection notice says I do not take my medication and that "
            "this makes me act crazy. I was taking it.",
        ],
    ),
    Exhibit(
        "J",
        "Field Property Receipt 137237",
        "What the police wrote down that they took from me.",
        [
            "It lists '1 x dog'. That is the whole list.",
            "It does not list my phone. They took my phone.",
            "It does not list the folder of evidence Tom Balsey handed to "
            "Constable Bickery at the scene.",
        ],
    ),
    Exhibit(
        "K",
        "Senior Constable Yaun's email — 21 August 2025",
        "From the officer who issued the original notice.",
        [
            "'My original application for a DVO was struck out of Court "
            "several months ago upon my submission of no evidence from the "
            "aggrieved.'",
            "'I believe another application may have been made by another "
            "officer from Southport who incorrectly used my original Police "
            "occurrence.'",
            "'I have had no further involvement in your matters.'",
        ],
        quote=(
            "struck out of Court several months ago upon my submission of no "
            "evidence from the aggrieved"
        ),
    ),
]


ASKS = Section(
    "What I want done now",
    paragraphs=[
        "Get the new lease Alexia filed, and the date it starts. That date "
        "answers their first reason on its own.",
        "Get the full bond history from the Residential Tenancies Authority — "
        "contributors, any change, any refund, and whether a new bond was "
        "lodged and when.",
        "Get the leasing manager's statement that they are relying on, with "
        "the date it was taken and who took it, and put it alongside what he "
        "told the two officers on camera and what he swore in his statutory "
        "declaration.",
        "Make them say, in writing, what the indictable offence inside Charge "
        "1 is meant to be.",
        "Make them identify which order Charge 3 is brought on, produce a "
        "certified copy with its conditions, and produce the service record — "
        "and answer Senior Constable Yaun's email.",
        "Put honest claim of right on notice, with the breeder receipt, the "
        "Gold Coast Council registration, Alexia's own messages, and the NSW "
        "Pet Registry's letter.",
        "Produce the body-worn camera serials X60508355, X60507687 and "
        "X60500949, agreed for release through the external review and never "
        "handed over, and Constable Davies's five-page statement listed in "
        "the index as 'to be provided'.",
        "Examine my phone or give it back, and produce the message from "
        "Alexia saying I could walk the dog.",
        "Formal notice about the dog being given away before any court order, "
        "and the fact that nobody can now test the very thing they are "
        "asserting against me.",
        "Review my bail conditions now that Charge 2 has gone.",
    ],
)


# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------

CSS = """
:root { color-scheme: light; }
body {
  font-family: Georgia, "Times New Roman", serif;
  max-width: 820px; margin: 40px auto; padding: 0 24px 64px;
  color: #1a1a1a; line-height: 1.55; background: #fafafa;
}
h1 { font-size: 2em; margin-bottom: 0.2em; }
.subtitle { color: #555; font-style: italic; font-size: 1.05em; margin-top: 0; }
.meta { color: #555; font-size: 0.95em; margin: 0.5em 0 2.5em; }
h2 { border-bottom: 2px solid #1a1a1a; padding-bottom: 6px; margin-top: 2.2em; }
h3 { margin-top: 1.8em; color: #222; }
ul { padding-left: 1.3em; }
li { margin: 0.35em 0; }
blockquote {
  border-left: 4px solid #555; margin: 1em 0; padding: 0.4em 1em;
  background: #f0f0f0; font-style: italic; color: #222;
}
.exhibit {
  border: 1px solid #bbb; border-radius: 6px; padding: 14px 22px;
  margin: 1.6em 0; background: #fff; page-break-inside: avoid;
}
.exhibit-number {
  display: inline-block; background: #1a1a1a; color: #fff; padding: 2px 10px;
  border-radius: 3px; font-size: 0.85em; font-weight: bold;
  letter-spacing: 0.04em; margin-right: 0.5em;
}
.exhibit-name { font-weight: bold; font-size: 1.1em; }
.exhibit-what { color: #444; font-style: italic; margin: 0.6em 0; }
table { border-collapse: collapse; width: 100%; margin: 1.2em 0; }
th, td { border: 1px solid #bbb; padding: 8px 10px; text-align: left; font-size: 0.95em; }
th { background: #ececec; }
@media print {
  body { background: #fff; max-width: 100%; margin: 0; padding: 1.4cm; }
  h2 { page-break-after: avoid; }
  .exhibit { page-break-inside: avoid; }
}
"""

CHARGE_TABLE = [
    ("1", "Entering premises and committing an indictable offence — s 421(2)", "Continuing"),
    ("2", "Unlawful stalking, intimidation, harassment or abuse — s 359E(1)", "Discontinued"),
    ("3", "Contravention of a domestic violence order — s 177(2)(b)", "Continuing"),
]


def _p(items: list[str]) -> str:
    return "\n".join(f"<p>{html.escape(x)}</p>" for x in items)


def _ul(items: list[str]) -> str:
    if not items:
        return ""
    return "<ul>\n" + "\n".join(f"  <li>{html.escape(i)}</li>" for i in items) + "\n</ul>"


def build_html() -> str:
    out = ["<!DOCTYPE html>", "<html lang='en'><head><meta charset='utf-8'>",
           f"<title>{html.escape(TITLE)}</title>", f"<style>{CSS}</style></head><body>"]
    out.append(f"<h1>{html.escape(TITLE)}</h1>")
    out.append(f"<p class='subtitle'>{html.escape(SUBTITLE)}</p>")
    out.append(f"<p class='meta'>{html.escape(AUTHOR)} &middot; {html.escape(MATTER)}</p>")

    out.append(f"<h2>{html.escape(OPENING.heading)}</h2>")
    out.append(_p(OPENING.paragraphs))
    out.append("<table><tr><th>Charge</th><th>What it is</th><th>Where it stands</th></tr>")
    for num, desc, status in CHARGE_TABLE:
        out.append(f"<tr><td>{num}</td><td>{html.escape(desc)}</td><td>{status}</td></tr>")
    out.append("</table>")

    for sec in BODY:
        out.append(f"<h2>{html.escape(sec.heading)}</h2>")
        out.append(_p(sec.paragraphs))
        if sec.bullets:
            out.append(_ul(sec.bullets))
        if sec.quote:
            out.append(f"<blockquote>{html.escape(sec.quote)}</blockquote>")

    out.append("<h2>The documents behind it</h2>")
    for ex in EXHIBITS:
        out.append("<div class='exhibit'>")
        out.append(f"<div><span class='exhibit-number'>{html.escape(ex.number)}</span>"
                   f"<span class='exhibit-name'>{html.escape(ex.name)}</span></div>")
        out.append(f"<p class='exhibit-what'>{html.escape(ex.what_it_is)}</p>")
        out.append(_ul(ex.what_it_shows))
        if ex.quote:
            out.append(f"<blockquote>{html.escape(ex.quote)}</blockquote>")
        out.append("</div>")

    out.append(f"<h2>{html.escape(ASKS.heading)}</h2>")
    out.append(_ul(ASKS.paragraphs))
    out.append("</body></html>")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# PDF
# ---------------------------------------------------------------------------

def build_pdf(path: Path) -> None:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.lib.colors import HexColor
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, KeepTogether, Table, TableStyle,
        ListFlowable, ListItem,
    )

    styles = getSampleStyleSheet()
    body = ParagraphStyle("body", parent=styles["BodyText"], fontName="Times-Roman",
                          fontSize=11, leading=15, spaceBefore=4, spaceAfter=8)
    title_s = ParagraphStyle("title", parent=styles["Title"], fontName="Times-Bold",
                             fontSize=22, leading=26)
    subtitle_s = ParagraphStyle("subtitle", parent=styles["BodyText"], fontName="Times-Italic",
                                fontSize=12, leading=15, spaceAfter=4, textColor=HexColor("#555"))
    meta_s = ParagraphStyle("meta", parent=styles["BodyText"], fontName="Times-Roman",
                            fontSize=10, textColor=HexColor("#555"), spaceAfter=18)
    h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontName="Times-Bold",
                        fontSize=15, leading=20, spaceBefore=18, spaceAfter=8)
    quote_s = ParagraphStyle("quote", parent=body, fontName="Times-Italic", leftIndent=18,
                             rightIndent=12, textColor=HexColor("#222"), spaceBefore=4, spaceAfter=6)
    ex_name_s = ParagraphStyle("ex_name", parent=styles["Heading3"], fontName="Times-Bold",
                               fontSize=12, leading=15, spaceBefore=2, spaceAfter=2)
    ex_what_s = ParagraphStyle("ex_what", parent=body, fontName="Times-Italic", fontSize=10.5,
                               leading=13, spaceBefore=0, spaceAfter=6, textColor=HexColor("#444"))

    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=2.2 * cm, rightMargin=2.2 * cm,
                            topMargin=2 * cm, bottomMargin=2 * cm, title=TITLE, author=AUTHOR)
    story = []

    def para(text, style=body):
        story.append(Paragraph(text, style))

    def bullets(items):
        if not items:
            return
        story.append(ListFlowable([ListItem(Paragraph(i, body), leftIndent=14) for i in items],
                                  bulletType="bullet", start="•", leftIndent=14,
                                  spaceBefore=2, spaceAfter=6))

    para(TITLE, title_s)
    para(SUBTITLE, subtitle_s)
    para(f"{AUTHOR} &nbsp;&middot;&nbsp; {MATTER}", meta_s)

    para(OPENING.heading, h2)
    for p in OPENING.paragraphs:
        para(p)

    tbl_data = [["Charge", "What it is", "Where it stands"]]
    for num, desc, status in CHARGE_TABLE:
        tbl_data.append([num, Paragraph(desc, body), status])
    tbl = Table(tbl_data, colWidths=[1.6 * cm, 10.6 * cm, 4.2 * cm])
    tbl.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, HexColor("#999")),
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#ececec")),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("FONTNAME", (0, 1), (0, -1), "Times-Roman"),
        ("FONTNAME", (2, 1), (2, -1), "Times-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 10))

    for sec in BODY:
        para(sec.heading, h2)
        for p in sec.paragraphs:
            para(p)
        bullets(sec.bullets)
        if sec.quote:
            para(f"&ldquo;{sec.quote}&rdquo;", quote_s)

    para("The documents behind it", h2)
    for ex in EXHIBITS:
        block = [Paragraph(f"<b>{ex.number}</b> &nbsp; {ex.name}", ex_name_s),
                 Paragraph(ex.what_it_is, ex_what_s)]
        if ex.what_it_shows:
            block.append(ListFlowable([ListItem(Paragraph(s, body), leftIndent=14)
                                       for s in ex.what_it_shows],
                                      bulletType="bullet", start="•", leftIndent=14,
                                      spaceBefore=2, spaceAfter=4))
        if ex.quote:
            block.append(Paragraph(f"&ldquo;{ex.quote}&rdquo;", quote_s))
        wrapped = Table([[block]], colWidths=[doc.width], style=TableStyle([
            ("BOX", (0, 0), (-1, -1), 0.4, HexColor("#999")),
            ("LEFTPADDING", (0, 0), (-1, -1), 10),
            ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        story.append(KeepTogether(wrapped))
        story.append(Spacer(1, 8))

    para(ASKS.heading, h2)
    bullets(ASKS.paragraphs)

    doc.build(story)


# ---------------------------------------------------------------------------
# PPTX
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
    ACCENT = RGBColor(0x33, 0x33, 0x33)

    def add_text(slide, left, top, width, height, text, *, size=18, bold=False,
                 color=DARK, italic=False, align=PP_ALIGN.LEFT):
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = align
        r = p.add_run()
        r.text = text
        r.font.name = "Calibri"
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
        return tb

    def add_bullets(slide, left, top, width, height, items, *, size=15, color=DARK):
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = True
        for i, item in enumerate(items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            r = p.add_run()
            r.text = "•  " + item
            r.font.name = "Calibri"
            r.font.size = Pt(size)
            r.font.color.rgb = color
            p.space_after = Pt(6)
        return tb

    def divider(label):
        s = prs.slides.add_slide(blank)
        add_text(s, Inches(0.6), Inches(3.0), Inches(12), Inches(1.2), label, size=38, bold=True)

    def content(heading, paragraphs=None, bullets=None, quote=None):
        s = prs.slides.add_slide(blank)
        add_text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(1.0), heading, size=25, bold=True)
        y = Inches(1.55)
        for p in (paragraphs or []):
            add_text(s, Inches(0.6), y, Inches(12), Inches(1.2), p, size=15)
            lines = max(1, len(p) // 92 + 1)
            y += Inches(0.30 * lines + 0.10)
        if bullets:
            add_bullets(s, Inches(0.6), y, Inches(12), Inches(4.5), bullets)
        if quote:
            qb = s.shapes.add_textbox(Inches(0.6), Inches(6.1), Inches(12), Inches(1.1))
            tf = qb.text_frame
            tf.word_wrap = True
            r = tf.paragraphs[0].add_run()
            r.text = "“" + quote + "”"
            r.font.italic = True
            r.font.size = Pt(14)
            r.font.color.rgb = ACCENT
        return s

    # Title
    s = prs.slides.add_slide(blank)
    add_text(s, Inches(0.6), Inches(2.3), Inches(12), Inches(1.4), TITLE, size=46, bold=True)
    add_text(s, Inches(0.6), Inches(3.8), Inches(12), Inches(1.0), SUBTITLE, size=20,
             italic=True, color=MID)
    add_text(s, Inches(0.6), Inches(5.5), Inches(12), Inches(0.5), AUTHOR, size=18, color=MID)
    add_text(s, Inches(0.6), Inches(6.0), Inches(12), Inches(0.5), MATTER, size=14, color=MID)

    # Charge table slide
    s = prs.slides.add_slide(blank)
    add_text(s, Inches(0.6), Inches(0.4), Inches(12), Inches(0.9),
             "The three charges, and where each one stands", size=25, bold=True)
    rows = len(CHARGE_TABLE) + 1
    tbl = s.shapes.add_table(rows, 3, Inches(0.6), Inches(1.7), Inches(12), Inches(3.0)).table
    tbl.columns[0].width = Inches(1.4)
    tbl.columns[1].width = Inches(8.2)
    tbl.columns[2].width = Inches(2.4)
    for j, head in enumerate(("Charge", "What it is", "Where it stands")):
        c = tbl.cell(0, j)
        c.text = head
        c.text_frame.paragraphs[0].runs[0].font.size = Pt(14)
        c.text_frame.paragraphs[0].runs[0].font.bold = True
    for i, (num, desc, status) in enumerate(CHARGE_TABLE, start=1):
        for j, val in enumerate((num, desc, status)):
            c = tbl.cell(i, j)
            c.text = val
            run = c.text_frame.paragraphs[0].runs[0]
            run.font.size = Pt(13)
            if j == 2:
                run.font.bold = True

    divider("My answer to each reason they gave")
    for sec in BODY:
        paras = sec.paragraphs
        chunks = [paras[i:i + 3] for i in range(0, len(paras), 3)] or [[]]
        for idx, chunk in enumerate(chunks):
            heading = sec.heading if idx == 0 else sec.heading + " (continued)"
            content(heading, paragraphs=chunk,
                    quote=sec.quote if idx == len(chunks) - 1 else None)

    divider("The documents behind it")
    for ex in EXHIBITS:
        s = prs.slides.add_slide(blank)
        badge = s.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(0.9), Inches(0.6))
        r = badge.text_frame.paragraphs[0].add_run()
        r.text = ex.number
        r.font.size = Pt(16)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xff, 0xff, 0xff)
        badge.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        badge.fill.solid()
        badge.fill.fore_color.rgb = DARK
        badge.line.fill.background()
        add_text(s, Inches(1.7), Inches(0.4), Inches(11), Inches(0.8), ex.name, size=22, bold=True)
        add_text(s, Inches(0.6), Inches(1.2), Inches(12), Inches(0.7), ex.what_it_is,
                 size=14, italic=True, color=MID)
        add_bullets(s, Inches(0.6), Inches(2.0), Inches(12), Inches(4.2), ex.what_it_shows, size=14)
        if ex.quote:
            qb = s.shapes.add_textbox(Inches(0.6), Inches(6.3), Inches(12), Inches(1.0))
            qb.text_frame.word_wrap = True
            r = qb.text_frame.paragraphs[0].add_run()
            r.text = "“" + ex.quote + "”"
            r.font.italic = True
            r.font.size = Pt(14)
            r.font.color.rgb = ACCENT

    divider(ASKS.heading)
    half = (len(ASKS.paragraphs) + 1) // 2
    content(ASKS.heading, bullets=ASKS.paragraphs[:half])
    content(ASKS.heading + " (continued)", bullets=ASKS.paragraphs[half:])

    prs.save(str(path))


def main() -> None:
    stem = "Shepherd_Charges_Position_2026-08-13"
    html_path = OUT / f"{stem}.html"
    pdf_path = OUT / f"{stem}.pdf"
    pptx_path = OUT / f"{stem}.pptx"

    html_path.write_text(build_html(), encoding="utf-8")
    build_pdf(pdf_path)
    build_pptx(pptx_path)

    for p in (html_path, pdf_path, pptx_path):
        print(f"  wrote {p.name}  ({p.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
