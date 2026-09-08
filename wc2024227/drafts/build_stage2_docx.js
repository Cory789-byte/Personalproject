// Build the Stage 2 referral as a Word draft for review.
// - DRAFT watermark line + review header
// - The three fill-me brackets highlighted YELLOW so they cannot be missed
// - Metadata scrubbed (no author/company/lastModifiedBy; neutral timestamps handled post-zip)
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, BorderStyle,
} = require("docx");

const INK = "111111";
const MUTE = "555555";

const F = "Calibri";
const SZ = 21;          // 10.5pt body
const SZ_SMALL = 18;

function p(opts, runs) {
  return new Paragraph({ spacing: { after: 160, line: 276 }, ...opts, children: runs });
}
function r(text, extra) { return new TextRun({ font: F, size: SZ, color: INK, text, ...extra }); }
function bold(text, extra) { return r(text, { bold: true, ...extra }); }
function slot(text) { return new TextRun({ font: F, size: SZ, color: "7A5C00", highlight: "yellow", text }); }

const doc = new Document({
  creator: "", description: "", title: "Stage 2 referral - draft for review",
  lastModifiedBy: "",
  styles: { default: { document: { run: { font: F, size: SZ, color: INK } } } },
  sections: [{
    properties: {
      page: { margin: { top: 1080, bottom: 1080, left: 1240, right: 1240 } },
    },
    children: [
      p({ spacing: { after: 60 } }, [ bold("DRAFT FOR REVIEW — NOT SENT", { color: "B00000", size: SZ }) ]),
      p({ spacing: { after: 200 } }, [ new TextRun({ font: F, size: SZ_SMALL, color: MUTE,
        text: "Stage 2 referral · one section remains open, reserved for Together Queensland's input; all else is final. Send as soon as the union section resolves — the Stage 2 seven days run from the date of sending." }) ]),

      p({ spacing: { after: 40 } }, [ bold("To: "), r("LBH Human Resources — LBH_HR@health.qld.gov.au") ]),
      p({ spacing: { after: 40 } }, [ bold("Cc: "), r("Ms Chloe Taylor, Manager, Switchboard Services; LBH Injury Management; Mr Heath Moran and Ms Emily Petering, Together Queensland") ]),
      p({ spacing: { after: 200 } }, [ bold("Attachments: "), r("(1) Notice of dispute, 3 August 2026; (2) Ms Taylor's letter, 4 August 2026; (3) my response dated 4 August 2026 (provided 5 August 2026).") ]),

      p({ border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "999999" } }, spacing: { after: 200 } },
        [ bold("Subject: Referral to Stage 2 — clause 1.11.2(b) — attendance, roster, leave and pay from 26 June 2026", { size: SZ }) ]),

      p({}, [ r("Dear Human Resources team,") ]),

      p({}, [ r("I refer the dispute lodged on 3 August 2026 to Stage 2 under clause 1.11.2(b) of the Certified Agreement (No. 12) 2025 (EB12), and I ask that it be routed to the appropriate management representative, who under the clause shall arrange a conference of the parties. Given the matters set out in my letter to the Chief Executive of 3 August 2026, I ask that the representative be an officer independent of the matters in dispute.") ]),

      p({}, [ bold("1  Why the referral is made") ]),
      p({}, [ r("Stage 1 has concluded unresolved. The record is short:") ]),
      p({ indent: { left: 360, hanging: 360 } }, [ r("1.1\tThe dispute was acknowledged as validly lodged on 4 August 2026: “Your dispute has been lodged in accordance with clause 1.11.2(a).”") ]),
      p({ indent: { left: 360, hanging: 360 } }, [ r("1.2\tThe 24-hour discussion did not occur. The Health Service's letter of 4 August 2026 states: “the 24-hour timeframe specified in the clause will not be achieved.”") ]),
      p({ indent: { left: 360, hanging: 360 } }, [ r("1.3\tNo Stage 1 discussion has taken place at any point in the seven days, notwithstanding that my response offered availability on Wednesday 5 and Thursday 6 August, from 9:00am to 5:00pm, and other times including outside business hours.") ]),
      p({ indent: { left: 360, hanging: 360 } }, [
        r("1.4\tMy response set out, at its section 2, five facts and invited correction; none has been corrected. It asked, at its section 3, seven questions so that the correct arrangement could be applied, and asked that any answer sitting with a more senior decision-maker be escalated within Stage 1 so the seven days were not lost. None of the seven questions has been answered."),
      ]),
      p({ indent: { left: 360, hanging: 360 } }, [
        r("1.5\tThe letter of 4 August 2026 is the only communication received from the Health Service during the Stage 1 period. My response of 5 August 2026 has not been answered. The matters in dispute accordingly remain unresolved: the instrument under which I am held from work has not been identified (question 3.1), the status quo under clause 1.11.4 has not been restored, and the leave and pay position from 26 June 2026 remains as it was."),
      ]),
      p({ indent: { left: 360, hanging: 360 } }, [
        r("1.6\tMy response of 5 August 2026 stated that I did not consent to my recreation leave being applied to the period 20 July to 2 August 2026, and requested special leave on full pay under Directive 12/24 instead. That request has not been answered. Any leave applied is, per that response, recorded as applied at the Health Service's initiative, without my consent, without prejudice to the dispute, and subject to re-credit."),
      ]),
      p({}, [ r("My response foreshadowed this referral in terms: “If the dispute is unresolved by 10 August I will refer it to Stage 2 as the clause provides.” That date has passed, the dispute remains unresolved, and this is that referral.") ]),

      p({}, [ bold("2  What the conference needs to resolve") ]),
      p({ indent: { left: 360, hanging: 360 } }, [ r("2.1\tThe instrument question: what decision prevents my attendance since 26 June 2026, made by whom, on what date, under what power. Asked in the notice of 3 August (sections 2.1 and 4(b)–(c)), in my response (questions 3.1 to 3.3), and in earlier correspondence; unanswered.") ]),
      p({ indent: { left: 360, hanging: 360 } }, [ r("2.2\tPay and leave: wages for the period from 26 June 2026; re-credit of all leave debited; the coding of the absence (special leave on full pay under Directive 12/24 was requested on 5 August); the “income protection” characterisation applied from 13 July 2026, under which I receive neither wages nor benefit (my response, section 5); and cessation of further debits per clause 1.11.4 — the status quo before this dispute emerged was that I was rostered, working and paid.") ]),
      p({ indent: { left: 360, hanging: 360 } }, [ r("2.3\tReturn to work: the Employee Capabilities Checklist of 3 July 2026 certifies me fit for work with restrictions and records the pattern as a “continuation of existing arrangement”; my return to work proposal of 3 August 2026 stands; no Return to Work Plan exists.") ]),
      p({ indent: { left: 360, hanging: 360 } }, [
        r("2.4\tThe position communicated to my insurer: on 4 August 2026 my income protection insurer recorded, on information from the Health Service, that the Health Service is “currently unable to accommodate a graduated return to work”. I have not been given that position directly, by its maker, with reasons. My response, section 4, sets out what is asked; it remains open."),
      ]),
      p({ indent: { left: 360, hanging: 360 } }, [ r("2.5\tThe work health and safety matters: the feedback required by clause 7.1.11 on the matters I have raised, and the psychosocial risk assessment of the work area under clause 7.2, requested on 3 August 2026 and identified by the Health Service's own letter of 7 July 2026, which recorded that it did not then have sufficient information to assess psychosocial hazards affecting my return to work. No assessment has been undertaken.") ]),
      p({ indent: { left: 360, hanging: 360 } }, [ r("2.6\tAny remaining unanswered items of the Stage 1 notice of 3 August 2026 and my response dated 4 August 2026 (including the policies sought, the roster and payroll records, and the suspension or status question), to the extent not already covered by 2.1 to 2.5.") ]),
      p({}, [ r("For clarity, my separate request of 3 August 2026 under clause 10.3.2 is not part of this dispute and continues on its own timeframe.") ]),

      p({}, [ bold("3  Union representation") ]),
      p({}, [ slot("[Heath and Emily — this section is yours. If Together is able to represent me, or attend with me, at the Stage 2 conference, and to confirm my delegate status for the workplace, this is where it would sit, in your words. If that is not something Together can do before Monday, that is completely fine and no explanation is needed: I will simply remove this section, respect that position, and proceed with the referral on my own. It stands either way.]") ]),

      p({}, [ bold("4  Arrangements") ]),
      p({}, [ r("Clause 1.11.2(b) provides that the management representative shall arrange a conference of the parties, and that the process should not extend beyond seven days from this referral. I am available at any time, with my support person and union representative present. I ask that whoever attends for the Health Service have authority to resolve the matters at 2.1 to 2.6, and that the answers to the seven questions of my response be available at the conference. I will provide anything further required the same day it is requested.") ]),
      p({}, [ r("I remain ready, willing and able to work, and my object in this referral is unchanged: to return to work, paid, under the certified restrictions, with the matters above resolved in the ordinary way.") ]),

      p({ spacing: { before: 120, after: 40 } }, [ r("Yours sincerely,") ]),
      p({ spacing: { after: 0 } }, [ r("Cory Lea Shepherd") ]),
      p({ spacing: { after: 0 } }, [ new TextRun({ font: F, size: SZ_SMALL, color: MUTE, text: "AO3, Switchboard Services, Logan Hospital" }) ]),
      p({ spacing: { after: 0 } }, [ new TextRun({ font: F, size: SZ_SMALL, color: MUTE, text: "0417 400 227 · coryshepherd1@hotmail.com" }) ]),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync("/home/user/Personalproject/wc2024227/drafts/out/STAGE2_REFERRAL_DRAFT_FOR_REVIEW.docx", buf);
  console.log("written");
});
