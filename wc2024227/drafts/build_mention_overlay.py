#!/usr/bin/env python3
"""WC/2024/227 - THE MENTION OVERLAY.

What was said at the mention of 7 August 2026, and what the Respondent admitted on
8 September 2026 in answer to the notice to admit facts served 28 August 2026.

Facts are the 303 paragraphs of the notice to admit facts served 28 August 2026 as the
Respondent answered them on 8 September 2026, read from
documents/regulator-response-2026-09-08/SERVED_303_facts_and_verdicts.json via served_facts.py.
Not from build_form24_second.py, which is a working draft and has moved on from what was served.

INTERNAL. The mention transcript is a working transcript produced from the approved audio.
It is NOT a certified transcript and the speaker labels are inferred (90% on hand-checked
anchors). Order the certified transcript before any passage is quoted externally.
"""
import io, re, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, KeepTogether

# ---------- facts, verbatim, with the served numbering ----------
from served_facts import FACT, NOT_ADMITTED, TOTAL   # the 303 facts as served and answered
assert TOTAL == 303

BLUE  = colors.HexColor('#123f8c')
GREY  = colors.HexColor('#6b6b6b')
RED   = colors.HexColor('#8a2b2b')

H1   = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13, leading=15.5, spaceAfter=2)
H2   = ParagraphStyle('H2', fontName='Helvetica', fontSize=8.4, leading=10.5,
                      textColor=GREY, spaceAfter=5)
KEY  = ParagraphStyle('KEY', fontName='Helvetica', fontSize=7.7, leading=9.6, spaceAfter=2)
SEC  = ParagraphStyle('SEC', fontName='Helvetica-Bold', fontSize=9.2, leading=11.5,
                      spaceBefore=7, spaceAfter=2.5, textColor=colors.HexColor('#1a1a1a'))
SAID = ParagraphStyle('SAID', fontName='Helvetica', fontSize=8.3, leading=10.4,
                      leftIndent=4*mm, spaceAfter=1.5)
ADM  = ParagraphStyle('ADM', fontName='Helvetica', fontSize=8.0, leading=9.9,
                      leftIndent=4*mm, textColor=BLUE, spaceAfter=1.2)
STAT = ParagraphStyle('STAT', fontName='Helvetica-Oblique', fontSize=7.8, leading=9.6,
                      leftIndent=4*mm, textColor=RED, spaceAfter=4)
def P(t, s): return Paragraph(t, s)

def facts(ns):
    out = []
    for n in ns:
        mark = ' <b>[NOT ADMITTED]</b>' if n in NOT_ADMITTED else ''
        out.append(P(f"<b>[{n}]</b> {FACT[n]}{mark}", ADM))
    return out

# ---------- the overlay ----------
# (heading, [ (speaker, spoken text) ... ], [fact numbers], status line)
E = [
("1. &nbsp;15:57 &ndash; the stressor read from the pleading, and the first question",
 [("DWYER IC", "So your evidence is she had an erratic presence. What do you mean by that, "
   "Mr Shepherd? Well, this, and you explain what that is. &hellip; imposed unassessed unilateral "
   "directives. How did she impose unassessed unilateral directives?"),
  ("MR SHEPHERD", "So, for instance, without consulting any of the staff members?")],
 [39, 40, 44, 45, 49, 51, 53, 54, 273],
 "The two directives are now documents, admitted word for word, and the absence of any "
 "consultation document is admitted from the Respondent's own list. MADE OUT."),

("2. &nbsp;16:11 &ndash; are they in writing",
 [("DWYER IC", "Well, first of all, first of all, was this done by&hellip; How did she do it? By "
   "email? Are these things in writing?")],
 [40, 50, 51, 52, 53],
 "Yes, and the wording is admitted. MADE OUT."),

("3. &nbsp;16:37 &ndash; a question of particulars",
 [("DWYER IC", "Um, so you say, and perhaps it's a question of particulars, you say, um, imposed, "
   "unassessed unilateral directives. Do you mean by that, and tell me if I've got this wrong, that "
   "she sent emails in the form of a directive to staff?"),
  ("MR SHEPHERD", "Correct.")],
 [281, 282],
 "The pleading answer of 13 May 2026 was that there were no particulars to respond to. The "
 "particulars were served on 11 August 2026 and admitted on 8 September. That answer is spent. "
 "MADE OUT."),

("4. &nbsp;17:38 &ndash; whether the disclosure holds them",
 [("DWYER IC", "Okay. Does that include email communications from Ms Chloe Taylor to staff?"),
  ("MS MATHESON", "Yes, Commissioner. We've disclosed all we have currently."),
  ("DWYER IC", "Okay. Have you examined those documents that have been disclosed to you, "
   "Mr Shepherd, to see whether or not it contains examples of these unassessed unilateral "
   "directives?"),
  ("MR SHEPHERD", "They do not. They're more just isolated towards me."),
  ("DWYER IC", "You say there's nothing like that in what's been disclosed to you from the "
   "regulator?"),
  ("MR SHEPHERD", "Not that I can recall, no.")],
 [277, 278, 279],
 "⛔ The answer given on 7 August 2026 cannot be measured against the amended List of "
 "Documents, which is dated 14 August 2026 – one week after the mention. The list "
 "identifying the three emails at items 25, 26 and 27 did not then exist, and the Regulator "
 "had undertaken on 3 August to provide its updated list and the non-party copies \"as soon "
 "as possible this week\" - it arrived on 14 August 2026. What the admissions establish is that the documents were in the "
 "Respondent's hands, the Appellant having sent them to WorkCover on 29 and 30 August 2024. "
 "MADE OUT – and the delivery dates are the answer if the exchange is ever put."),

("5. &nbsp;18:31 &ndash; the starting point",
 [("DWYER IC", "You see, making an order for a third party to disclose documents is a step sort of "
   "beyond what normally happens in disclosure. &hellip; The starting point is to ask the regulator "
   "to produce those documents. Have you done that?"),
  ("MR SHEPHERD", "I have asked the regulator to produce what they have."),
  ("DWYER IC", "Have you asked them to produce the unassessed unilateral directives?"),
  ("MR SHEPHERD", "Not those specific things, no.")],
 [],
 "⭐ A written request was already outstanding, though not the narrower one directed. The "
 "Appellant had asked the Regulator for an up-to-date list of documents and for the non-party "
 "notices with the documents produced under each on "
 "24 July 2026 - fourteen days before the mention. On 3 August the Regulator apologised for the "
 "delay and undertook to provide them \"as soon as possible this week\"; they arrived on "
 "14 August 2026, seven days after the mention. The narrower step the bench directed - asking "
 "for the directives by description - had NOT been taken. But a written request was overdue on "
 "the day, and that was not said on the record. "
 "The later request of 9 September 2026 asks for the remaining documents by item; the reply of "
 "10 September seeks until 25 September."),

("6. &nbsp;19:51 &ndash; how the stressor is proved",
 [("DWYER IC", "the way in which you prove this, if you were going to prove this, is you would give "
   "evidence about the erratic movements of Chloe Taylor and then you would produce documentary "
   "evidence of the unassessed unilateral directives as you describe them. &hellip; and that's the "
   "starting point.")],
 [55, 70, 72, 82, 83, 86, 87],
 "Both halves are now documentary. The directives are admitted; and the presence he said would "
 "be oral evidence is in the manager's own emails, which state that her hours “can vary”, "
 "that she would not be in until around 11 am, and, on 18 June 2024, “I am sorry I haven't "
 "been there for you all over the past week”. MADE OUT, and stronger than the route he set."),

("7. &nbsp;26:56 &ndash; what does unassessed mean",
 [("DWYER IC", "She's your manager, right? &hellip; So she's going to send you directions "
   "unilaterally. Anyway, you can be directed as an employee to do certain things, right? What do "
   "you mean by unassessed?"),
  ("MR SHEPHERD", "Unassessed would be that she wasn't even in the room or she doesn't even enter "
   "the room to see what's going on and makes a decision without any input of the staff."),
  ("DWYER IC", "Like a manager. Managers make decisions without consulting staff all the time. "
   "It's totally legitimate.")],
 [267, 266, 263, 264, 265, 272, 269, 271],
 "This is the exchange the admissions change. The proposition is about the act of deciding. What "
 "is admitted is the absence of any assessment step at all: complaints are “managed solely "
 "via email or verbally with the complainant”, there were “no 'consequential' changes to "
 "operating procedures”, the fatigue records “do not exist”, and assessment began "
 "only after 30 June 2024. On the employer's own description there was nothing to assess with. "
 "MADE OUT, on a different footing from the one put to him."),

("8. &nbsp;27:28 and 29:17 &ndash; patient safety, raised twice",
 [("MR SHEPHERD", "But I think when it's in a patient safety environment that they —"),
  ("DWYER IC", "If you think it's in a patient safety environment you can raise that. Anyway, "
   "let's not get into the case."),
  ("MR SHEPHERD", "[at 29:17] so for me it was direct calls to this number but this number is an "
   "emergency contact and then those doctors, the ones that get called for an emergency, they're "
   "sent to the wrong side of the room, they're not sent to someone having a cardiac arrest, "
   "they're not sent to someone in respiratory distress"),
  ("&mdash;", "[5.7 second silence &ndash; the only long pause on the tape that reading a handed-up "
   "document does not explain]"),
  ("DWYER IC", "It's going to move on for a moment, okay? Because after my speech about efficiency "
   "of conduct of proceedings, I'm concerned at the direction this is going in, Mr Shepherd.")],
 [56, 57, 58, 59, 60, 61, 68, 69, 89, 91],
 "Put twice, taken up neither time. It is now documentary and admitted: nine occasions of calls "
 "reaching the wrong team reported by a clinician, one of them the MET call team ringing to ask "
 "where the MET call was; the occasions fell while the 15 April arrangement was in force; and the "
 "Respondent does not allege anything was sent to the Switchboard about them for six days. "
 "MADE OUT on documents, not on assertion."),

("9. &nbsp;28:04 &ndash; characterisation, and the test he set",
 [("DWYER IC", "the argument might be about whether or not they're correctly categorised by you as "
   "unassessed directives made without consultation, you've placed subjectively a characterisation "
   "on these emails which may be contradicted, but the existence of the emails may not be in "
   "dispute as far as I can tell. &hellip; And if you give evidence that you were sent unassessed "
   "directives by Ms Taylor, as you call them, and the regulator doesn't contradict it, doesn't "
   "cross-examine you, doesn't produce documents for you to comment on and that sort of thing, "
   "well, you know, that's a problem for them, not for you.")],
 [],
 "He was right about the characterisation, and it should go. On 8 September the Respondent "
 "admitted 298 of the 303 facts, not admitted five (154 and 228 to 231), denied none, and gave no "
 "reasons. The test he set is met on his own terms."),

("10. &nbsp;34:43 &ndash; the communication book",
 [("DWYER IC", "Unilateral destruction of work health and safety records. &hellip; You're not "
   "going to need documents for that, are you? &hellip; Did she physically tear the page out of a "
   "book? &hellip; So maybe the book. So we can see the torn out page. But she might admit she tore "
   "it out, in which case we probably don't need the book.")],
 [143, 146, 147, 149, 150, 151, 152, 154, 288],
 "She has admitted it, in the pleading and again on 8 September. The page cannot be produced: the "
 "Respondent does not allege it has been located or that any copy exists, and the book is not on "
 "its list. Fact 154 was not admitted, and is not pressed. MADE OUT as to the removal; the manner "
 "of the exchange remains oral evidence, as he said."),

("11. &nbsp;36:15 &ndash; the fatigue complaint in writing",
 [("DWYER IC", "Refusal to investigate work health and safety fatigue complaints. Did you make a "
   "health and safety fatigue complaint in writing?"),
  ("MR SHEPHERD", "Yes, I made many."),
  ("DWYER IC", "So you'll have a copy, or there should be a copy of an email to that effect?")],
 [242, 243, 244, 246, 263, 264, 265, 269, 270, 271],
 "The request, the escalation to Human Resources, the twenty-three day silence and the refusal are "
 "all admitted from the Respondent's own review decision, and the employer has stated in writing "
 "that the assessment records do not exist. MADE OUT, and the absence is admitted rather than "
 "asserted."),

("12. &nbsp;40:13 &ndash; the email he did not have",
 [("DWYER IC", "Ms Rees has given you a direction to retract a routine workplace email. How did she "
   "give you that direction? Is it in the form of an email?"),
  ("MR SHEPHERD", "Yes."),
  ("DWYER IC", "Have you got that email?"),
  ("MR SHEPHERD", "No, I do not."),
  ("DWYER IC", "Ms Matheson, have you got that email?")],
 [74, 75, 76, 77, 78, 79, 80],
 "The whole exchange is now admitted word for word, both sides of it, including the reply of "
 "21 May asking which changes and directives he was concerned about. MADE OUT."),

("13. &nbsp;41:55 &ndash; the comparator",
 [("DWYER IC", "Your case then tilts into a comparison. You say that a highly comparable email sent "
   "by Ms Taylor attracted no such discipline. Well, firstly, do you have a copy of the email from "
   "Ms Taylor that you're comparing to yours?"),
  ("MR SHEPHERD", "Correct, yes.")],
 [71, 72, 81, 82, 84, 113],
 "Both emails are admitted. The comparison itself is argument, not fact, and is best left to be "
 "drawn from the two documents rather than pleaded."),

("14. &nbsp;62:30 &ndash; what he said to go away and do",
 [("DWYER IC", "Look closely at what you've got from the regulator in terms of disclosure to this "
   "point, and if you feel like there's still something that you can say for certainty exists "
   "&hellip; If you're going to talk about those things that we talked about before, which was the "
   "unassessed directives or whatever, you might be on to something there. They might have an "
   "obligation to provide those. &hellip; it seems to me that those are going to be more about the "
   "character of those emails as opposed to whether they were actually sent or not &hellip; that "
   "particular point is the one area I think in all of what we've been through that there might be "
   "something to look at.")],
 [],
 "The existence half is closed by the admissions. The character half is where the appeal now "
 "sits, and the answer to it is not a better adjective: it is the admitted absence at item 7 "
 "above. That is the work the Second Amended Form 9A has to do."),
]

# ---------- the authenticity point ----------
TAIL_HEAD = "What the Respondent did not admit, and the pattern in it"
TAIL = [
 "Five facts of 303 were not admitted: 154 (that the Communication Book is not on the amended List "
 "of Documents) and 228 to 231 (the entries in the 2024 Emergency Code Register for 17, 18 and "
 "19 March 2024). Nothing was denied and no reasons were given.",
 "Separately, on the Form 25, the authenticity of fourteen documents was disputed, among them "
 "Tab 6, Ms Taylor's email of 15 April 2024 as forwarded by the Appellant to WorkCover; Tab 31, "
 "the screen capture of the 2024 Emergency Code Register; Tab 1, the role description; Tab 20, "
 "Metro South Health's letter of 5 June 2026 to Commissioner Dwyer; and Tabs 22 and 23, the "
 "Consultation Paper and outcome.",
 "The pattern is one line. Where the source is a document from the Respondent's own disclosure, "
 "the fact is admitted. Where the source is a document the Appellant captured or forwarded "
 "himself, the fact or the authenticity is not. The five not-admitted facts and most of the "
 "fourteen disputed tabs fall on that side of the line.",
 "That does not unsettle what is made out. The wording of Ms Taylor's email of 15 April 2024 is "
 "admitted at facts 49 to 53 whatever happens to Tab 6, and the contents of the letter of "
 "5 June 2026 are admitted at facts 263 to 268 whatever happens to Tab 20. An admission of fact "
 "under rule 49 binds for this proceeding independently of the authenticity of the page it came "
 "from. What the line does show is where the remaining work is: the register behind facts 228 to "
 "231, and nothing else.",
]

s = [P("THE MENTION OVERLAY &ndash; WHAT WAS SAID, AND WHAT WAS ADMITTED", H1),
     P("WC/2024/227 &ndash; Cory Lea Shepherd v Workers' Compensation Regulator. "
       "Mention before Dwyer IC, 7 August 2026. Admissions of 8 September 2026.", H2),
     P("<b>Black</b> is what was said at the mention. "
       "<font color='#123f8c'><b>Blue</b> is the text of a fact admitted by the Respondent on "
       "8 September 2026 in answer to the notice to admit facts served 28 August 2026, word for "
       "word, with its number on that notice in brackets. Admissions are for this proceeding only, "
       "under rule 49 of the Industrial Relations (Tribunals) Rules 2011.</font> "
       "<font color='#8a2b2b'><b>Red is navigation only. It is not evidence and it is not for "
       "service.</b></font>", KEY),
     P("⛔ <b>INTERNAL.</b> The spoken text is taken from a working transcript produced from "
       "the approved audio of the proceeding. It is <b>not a certified transcript</b>; the speaker "
       "labels are inferred and were measured at 90% against hand-checked anchors. Order the "
       "certified transcript before any passage is quoted externally. Nothing in this document is "
       "a criticism of the Commission; it is a record of what was asked and what now answers it.",
       KEY),
     Spacer(1, 2*mm)]

for head, spoken, fs, status in E:
    blk = [P(head, SEC)]
    for who, txt in spoken:
        blk.append(P(f"<b>{who}:</b> &nbsp;{txt}", SAID))
    if fs:
        blk.append(P("<b>Admitted 8 September 2026:</b>", ADM))
        blk.extend(facts(fs))
    blk.append(P(status, STAT))
    s.append(KeepTogether(blk) if len(blk) < 9 else blk[0])
    if len(blk) >= 9:
        s.extend(blk[1:])

s.append(P(TAIL_HEAD, SEC))
for t in TAIL:
    s.append(P(t, SAID))

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                      topMargin=12*mm, bottomMargin=12*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[
    Frame(15*mm, 11*mm, A4[0]-30*mm, A4[1]-23*mm, leftPadding=0, rightPadding=0,
          topPadding=0, bottomPadding=0)])])
doc.build(s); buf.seek(0)
pdf = pikepdf.open(buf)
n = len(pdf.pages)
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
with pdf.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del pdf.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(pdf.docinfo.keys()): del pdf.docinfo[k]
out = "INTERNAL/2026-09-12_MENTION_OVERLAY_what_was_said_and_what_was_admitted.pdf"
pdf.save(out, linearize=True)
print(f"built {out} - {len(E)} exchanges, {n} page(s)")
