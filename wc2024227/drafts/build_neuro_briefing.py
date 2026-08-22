#!/usr/bin/env python3
"""WC/2024/227 - neuro-architectural stress briefing, 22 August 2026.

⛔ NOT A CLINICAL OR EXPERT DOCUMENT. NOT FOR DISCLOSURE, SERVICE OR FILING.

This is a plain-language science-literacy briefing, written for Cory's own
understanding and to help frame questions for Dr Krishnaiah. It sets out
established stress-neuroscience literature (allostatic load; McEwen's model
of stress-induced neural remodeling) and maps it, as HYPOTHESIS ONLY, against
the occupational demand profile already described in the WHS material.

It contains NO finding about Cory's actual brain. No imaging or biomarker
data exists for him. Every neuroscience claim here is drawn from the general
literature on chronic occupational stress, not from any examination of him.
The diagnosis and the causal opinion remain Dr Krishnaiah's alone, per the
existing rule in skill/references/medical-causation-framework.md.
"""
import io, pikepdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Table, TableStyle, Spacer, PageBreak)

OUT = "out/NEURO_STRESS_BRIEFING_22Aug2026.pdf"
PW, PH = A4

H1  = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=14, leading=17, spaceAfter=3)
H2  = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=11, leading=14,
                     spaceBefore=10, spaceAfter=4, textColor=colors.HexColor('#1a1a1a'))
H3  = ParagraphStyle('H3', fontName='Helvetica-Bold', fontSize=9.6, leading=12.5,
                     spaceBefore=6, spaceAfter=2)
SUB = ParagraphStyle('SUB', fontName='Helvetica', fontSize=9, leading=12.5,
                     textColor=colors.HexColor('#555555'), spaceAfter=4)
B   = ParagraphStyle('B', fontName='Helvetica', fontSize=9.3, leading=13.2, spaceAfter=5)
C   = ParagraphStyle('C', fontName='Helvetica', fontSize=8.4, leading=11.2)
CH  = ParagraphStyle('CH', parent=C, fontName='Helvetica-Bold')
WARNBOX = ParagraphStyle('WARNBOX', fontName='Helvetica-Bold', fontSize=9.2, leading=13,
                         textColor=colors.HexColor('#7a1414'))
def P(t, s=B): return Paragraph(t, s)

def warning_block(title, body):
    rows = [[P(f"&#9888; {title}", WARNBOX)], [P(body, ParagraphStyle('wb', parent=B, fontSize=8.6))]]
    t = Table(rows, colWidths=[164*mm])
    t.setStyle(TableStyle([
        ('BOX',(0,0),(-1,-1),0.8,colors.HexColor('#a33')),
        ('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#fbeaea')),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
    ]))
    return t

story = []

# ---------------------------------------------------------------- cover / boundary
story.append(P("Neuro-architectural stress briefing", H1))
story.append(P("A science-literacy document on chronic occupational stress, mapped against the "
              "demand profile of a hospital switchboard role &middot; prepared 22 August 2026", SUB))
story.append(Spacer(1, 3*mm))
story.append(warning_block(
    "What this document is, and is not",
    "This is <b>not a clinical assessment, not an expert report, and not evidence of anything that "
    "occurred inside Cory Shepherd's brain.</b> No neuroimaging, no cortisol assay, no biomarker of "
    "any kind has been obtained. Every neuroscience proposition below is drawn from the published "
    "literature on chronic occupational stress in general populations. It is written for Cory's own "
    "understanding and to help frame questions for his treating psychiatrist, Dr Krishnaiah, in the "
    "same channel already used for workplace-conditions material handed to him for job-demands "
    "context. <b>It must not be disclosed, served, filed, or put to the Commission or the Regulator "
    "in any form, and no diagnostic or causal conclusion may be drawn from it.</b> The diagnosis and "
    "the causal opinion in this matter are Dr Krishnaiah's independent clinical judgment alone."))
story.append(Spacer(1, 4*mm))
story.append(P("Why it exists", H2))
story.append(P("The WHS cognitive-load analysis already prepared for this matter describes the "
              "<i>occupational</i> side of the picture well: a queue that rarely empties, frequent "
              "task-switching, emergency-code interruptions, and insufficient recovery between "
              "demands. This briefing adds the other half - what the general science says happens to "
              "a brain subjected to that kind of chronic demand pattern, over months rather than a "
              "single shift - so that the mechanism connecting workplace conditions to a "
              "psychological injury is something Cory can discuss intelligibly with his psychiatrist, "
              "rather than something asserted without foundation.", B))

# ---------------------------------------------------------------- 1. allostatic load
story.append(P("1. Allostatic load - the basic model", H2))
story.append(P("<b>Allostasis</b> is the process by which the body maintains stability by actively "
              "adjusting internal systems - cortisol, blood pressure, immune signalling, autonomic "
              "tone - in response to demand. <b>Allostatic load</b> is the cumulative wear that "
              "results when those adjustments are triggered repeatedly, or the system fails to switch "
              "off between demands (McEwen &amp; Stellar, 1993; McEwen, 1998).", B))
story.append(P("McEwen describes four conditions that generate allostatic load. The occupational "
              "profile in the WHS analysis maps onto at least three of them as a matter of general "
              "principle - this is a structural observation about the type of work, not a finding "
              "about Cory specifically:", B))
rows = [[P("McEwen's condition", CH), P("General description", CH), P("How the switchboard demand profile maps, as hypothesis", CH)]]
rows.append([P("Repeated hits", C), P("The same stressor recurs often, without habituation", C),
             P("A queue that rarely reaches zero, over an entire shift, repeated across a working week", C)])
rows.append([P("Failure to habituate", C), P("The stress response should quiet with repetition of a predictable stressor but does not", C),
             P("Emergency-code activation is high-consequence by design and is not the kind of stimulus the stress system habituates to", C)])
rows.append([P("Failure to shut off", C), P("The response continues after the demand has passed", C),
             P("Interruption research describes a 'resumption lag' - unfinished task states persist in working memory after the interrupting demand ends", C)])
t = Table(rows, colWidths=[30*mm, 62*mm, 78*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
story.append(t)
story.append(Spacer(1,2*mm))
story.append(P("The fourth condition - inadequate response, where a system under-reacts and other "
              "systems compensate - is not addressed here, as it requires physiological data this "
              "briefing does not have and should not speculate about.", C))

# ---------------------------------------------------------------- 2. McEwen's neural remodeling
story.append(P("2. McEwen's model of stress-induced neural remodeling", H2))
story.append(P("A separate and more specific body of work, associated particularly with Bruce "
              "McEwen and colleagues, describes structural changes observed in animal models (and, "
              "with more variability, in human neuroimaging studies) after sustained stress exposure. "
              "Three regions recur in this literature:", B))

story.append(P("Medial prefrontal cortex (mPFC)", H3))
story.append(P("The mPFC supports executive function: planning, working-memory manipulation, "
              "cognitive flexibility, and top-down regulation of the amygdala's threat response. "
              "Chronic stress models show <b>dendritic debranching</b> in this region - a reduction "
              "in the complexity of dendritic branching on pyramidal neurons - associated in animal "
              "studies with reduced capacity for cognitive flexibility and for regulating emotional "
              "reactivity (Radley et al., 2004; Liston et al., 2006; Arnsten, 2009). Functionally, "
              "this is the region whose sustained engagement is demanded by the task-switching, "
              "working-memory holding, and inhibition-of-distraction load described in the WHS "
              "cognitive-load analysis.", B))

story.append(P("Amygdala", H3))
story.append(P("The amygdala drives rapid threat detection and the emotional salience of a "
              "stimulus. Where the mPFC shows debranching under chronic stress, the amygdala in the "
              "same animal models shows the opposite pattern - <b>dendritic hypertrophy</b> (increased "
              "branching) in the basolateral nucleus, associated with heightened and more persistent "
              "reactivity to subsequent stressors (Vyas et al., 2002; Roozendaal, McEwen &amp; "
              "Chattarji, 2009). The functional pairing matters: as the region that inhibits an "
              "overreaction becomes less complex, the region that generates the reaction becomes more "
              "reactive.", B))

story.append(P("Hippocampus", H3))
story.append(P("The hippocampus supports contextual memory and exerts negative feedback on the "
              "hypothalamic-pituitary-adrenal (HPA) axis - it is part of what tells the stress "
              "response to switch off. Sustained glucocorticoid exposure is associated in the "
              "literature with dendritic atrophy in the CA3 region and, in some human cohort studies "
              "of chronic stress and PTSD, reduced hippocampal volume (Sapolsky, 1996; McEwen, 2000; "
              "Bremner, 1999). Reduced hippocampal regulation is one proposed mechanism by which a "
              "stress response, once triggered, becomes harder to switch off - consistent with the "
              "'failure to shut off' allostatic-load condition described above.", B))

story.append(warning_block(
    "The limits of this literature, stated plainly",
    "These findings come overwhelmingly from animal models (typically rodent) and from human cohort "
    "studies using group-level neuroimaging, not from any assessment of a specific individual's "
    "brain. They describe a plausible, well-replicated general mechanism connecting sustained "
    "occupational stress to changes in cognitive and emotional regulation. <b>They do not establish, "
    "and this document does not assert, that any such change occurred in Cory Shepherd.</b> Whether "
    "his diagnosed condition involves these mechanisms is a question for his treating psychiatrist, "
    "informed by his clinical presentation - not something this briefing can determine."))

story.append(PageBreak())

# ---------------------------------------------------------------- 3. vulnerability matrix
story.append(P("3. Vulnerability matrix - mapping occupational demand to the stress-response literature", H2))
story.append(P("This matrix places the demand elements already identified in the WHS cognitive-load "
              "analysis alongside the general mechanism from the literature that a treating clinician "
              "might consider relevant. <b>It is a discussion tool, not a set of findings.</b> Every "
              "row states a general proposition from the literature next to an occupational feature; "
              "neither column says anything about Cory's actual physiology.", B))
rows = [[P("Occupational demand feature\n(from the WHS analysis)", CH), P("General allostatic-load concept", CH),
         P("Region implicated in the general literature", CH)]]
VM = [
 ("Queue rarely reaches zero; little interval for attention to reset",
  "Repeated hits without recovery interval; failure to habituate", "mPFC (sustained executive load)"),
 ("Frequent task-switching between call, directory, paging/code system, and unfinished prior tasks",
  "Working-memory occupation by unfinished task states ('resumption lag')", "mPFC (working-memory / cognitive flexibility)"),
 ("Emergency-code activation: high urgency, high accuracy demand, concurrent with queued calls",
  "Acute, high-salience threat-type stimulus, repeated over a working week", "Amygdala (threat salience and reactivity)"),
 ("Exposure to caller distress, complaint, blame or hostility",
  "Chronic exposure to socially/emotionally threatening stimuli", "Amygdala; mPFC-amygdala regulatory coupling"),
 ("Insufficient recovery between shifts; night or rotating work; on-call ambiguity",
  "Failure of the stress response to switch off between demand periods", "Hippocampus (HPA-axis negative feedback)"),
 ("Sustained period of the above across months, not a single shift",
  "Cumulative allostatic load rather than a single acute stressor", "All three regions, cumulatively, per the literature"),
]
for a, b, c in VM:
    rows.append([P(a, C), P(b, C), P(c, C)])
t = Table(rows, colWidths=[62*mm, 58*mm, 50*mm], repeatRows=1)
t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#999999')),
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dddddd')),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4),
    ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
story.append(t)
story.append(Spacer(1,2*mm))
story.append(P("The final row is the one worth raising directly with Dr Krishnaiah: the WHS material "
              "describes a demand pattern sustained over roughly a year (the pleaded period in the "
              "Amended Statement of Facts and Contentions runs from mid-2023), not an isolated bad "
              "shift. The allostatic-load literature is specifically about cumulative exposure over "
              "that kind of timeframe, which is the reason it may be a useful frame for him to "
              "consider rather than a reason to draw any conclusion from it here.", B))

# ---------------------------------------------------------------- 4. recovery protocol
story.append(P("4. General recovery considerations - not a treatment plan", H2))
story.append(warning_block(
    "Not medical advice",
    "This section restates general, widely published findings about what supports recovery from "
    "chronic stress exposure. It is not a treatment plan, is not tailored to Cory's diagnosis or "
    "presentation, and must not substitute for anything Dr Krishnaiah or his GP actually prescribes "
    "or recommends. Anything in this section should be raised with them, not acted on independently "
    "where it might conflict with clinical advice already given."))
GEN = [
 ("Restoring HPA-axis regulation",
  "The literature on hippocampal-mediated feedback suggests that regularising sleep-wake timing, "
  "reducing unpredictable demand, and consistent daily structure support the systems that switch a "
  "stress response off. This is consistent with why removal from the triggering environment - as has "
  "occurred here since June 2024 - is itself considered by the literature to be part of recovery, "
  "not merely an accommodation."),
 ("Working-memory and executive recovery",
  "mPFC-dependent function is described in the literature as recovering, at least partially, once "
  "chronic demand is removed (Liston et al., 2009, found partial reversal of stress-induced "
  "dendritic changes after a recovery period in animal models). This is consistent with cognitive "
  "symptoms - difficulty concentrating, word-finding, decision fatigue - being expected to improve "
  "gradually with sustained removal from the stressor, rather than resolving immediately."),
 ("Amygdala reactivity",
  "Reduction in generalised threat-reactivity is described in the literature as the slower-recovering "
  "domain, and as the one most responsive to structured therapeutic intervention (rather than simple "
  "removal of the stressor) - relevant to why psychiatric or psychological treatment, not time alone, "
  "is usually the indicated pathway for this component."),
 ("Structure and reintegration",
  "The literature on return-to-work after stress-related psychological injury generally treats "
  "graduated, structured re-engagement - rather than either full removal or full resumption - as "
  "the pathway associated with the best functional outcome, which is a matter for Dr Krishnaiah's "
  "own assessment of timing and capacity."),
]
for title, body in GEN:
    story.append(P(title, H3))
    story.append(P(body, B))

story.append(P("Questions this raises for the appointment on 27 August 2026", H2))
story.append(P("Framed as questions for Dr Krishnaiah to consider, not propositions for him to "
              "adopt:", B))
QS = [
 "Does the sustained, cumulative nature of the workplace demand (as opposed to a single incident) "
 "fit the clinical picture he has observed - in particular, whether the presentation looks more like "
 "response to a discrete event or to prolonged cumulative load?",
 "Do the cognitive symptoms reported (concentration, word-finding, decision fatigue) fit a pattern "
 "consistent with prefrontal-mediated executive difficulty, and does that inform his view on "
 "functional capacity and timing of return to work?",
 "Does the general framework of cumulative allostatic load - as opposed to a single-stressor model - "
 "assist him in articulating causation and mechanism in his report, to the extent he considers it "
 "clinically appropriate to do so?",
]
for q in QS:
    story.append(P(f"&bull; {q}", B))

story.append(Spacer(1,4*mm))
story.append(P("Sources referred to", H2))
story.append(P("McEwen, B.S. &amp; Stellar, E. (1993). Stress and the individual: mechanisms leading "
              "to disease. <i>Archives of Internal Medicine</i>, 153(18), 2093-2101.<br/>"
              "McEwen, B.S. (1998). Protective and damaging effects of stress mediators. "
              "<i>New England Journal of Medicine</i>, 338(3), 171-179.<br/>"
              "McEwen, B.S. (2000). Effects of adverse experiences for brain structure and function. "
              "<i>Biological Psychiatry</i>, 48(8), 721-731.<br/>"
              "Radley, J.J. et al. (2004). Chronic behavioral stress induces apical dendritic "
              "reorganization in pyramidal neurons of the medial prefrontal cortex. <i>Neuroscience</i>, "
              "125(1), 1-6.<br/>"
              "Liston, C. et al. (2006). Stress-induced alterations in prefrontal cortical dendritic "
              "morphology predict selective impairments in perceptual attentional set-shifting. "
              "<i>Journal of Neuroscience</i>, 26(30), 7870-7874.<br/>"
              "Liston, C. et al. (2009). Circadian glucocorticoid oscillations promote learning-"
              "dependent synapse formation and maintenance. <i>Nature Neuroscience</i>, 12(3), 297-299 "
              "(recovery/reversal findings).<br/>"
              "Vyas, A. et al. (2002). Chronic stress induces contrasting patterns of dendritic "
              "remodeling in hippocampal and amygdaloid neurons. <i>Journal of Neuroscience</i>, "
              "22(15), 6810-6818.<br/>"
              "Roozendaal, B., McEwen, B.S. &amp; Chattarji, S. (2009). Stress, memory and the "
              "amygdala. <i>Nature Reviews Neuroscience</i>, 10(6), 423-433.<br/>"
              "Sapolsky, R.M. (1996). Stress, glucocorticoids, and damage to the nervous system: the "
              "current state of confusion. <i>Stress</i>, 1(1), 1-19.<br/>"
              "Bremner, J.D. (1999). Does stress damage the brain? <i>Biological Psychiatry</i>, "
              "45(7), 797-805.<br/>"
              "Arnsten, A.F.T. (2009). Stress signalling pathways that impair prefrontal cortex "
              "structure and function. <i>Nature Reviews Neuroscience</i>, 10(6), 410-422.", C))
story.append(Spacer(1,2*mm))
story.append(P("These are landmark and widely cited papers in the stress-neuroscience literature, "
              "reproduced here from general knowledge of the field. They have not been independently "
              "re-verified against original text for this briefing and should be checked before any "
              "citation is relied upon for a purpose beyond framing a conversation.", C))

def foot(cv, doc):
    cv.setFont('Helvetica', 7); cv.setFillColor(colors.HexColor('#777777'))
    cv.drawString(16*mm, 10*mm, "Neuro-stress briefing - science literacy only - NOT for disclosure or filing")
    cv.drawRightString(PW-16*mm, 10*mm, f"Page {doc.page}")

buf = io.BytesIO()
doc = BaseDocTemplate(buf, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
                      topMargin=15*mm, bottomMargin=16*mm)
doc.addPageTemplates([PageTemplate(id='n', frames=[Frame(16*mm, 16*mm, PW-32*mm, PH-31*mm)],
                                   onPage=foot)])
doc.build(story)
buf.seek(0)
p = pikepdf.open(buf)
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
with p.open_metadata(set_pikepdf_as_editor=False) as m: m.clear()
try: del p.Root.Metadata
except (AttributeError, KeyError): pass
for k in list(p.docinfo.keys()): del p.docinfo[k]
p.save(OUT, linearize=True)
print(f"built {OUT} pages: {len(p.pages)}")
