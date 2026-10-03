"""Fact sequences: every supporting fact, in order, for each 9A particular (Stressor 3 told completely)."""
import json, re
F = {x['n']: x['t'] for x in json.load(open('facts_served_303.json'))}
NA = {154, 228, 229, 230, 231}
def clean(t):
    t = re.sub(r'( (Not admitted|Admitted))+( |$)', ' ', t)
    t = re.sub(r' [A-S] (STRESSOR|THE |MATTERS|FACTS|PART).*$', '', t); t = re.sub(r' PART (ONE|TWO|THREE|FOUR|FIVE).*$', '', t)
    t = re.sub(r'\s*\(Annexure A, (Tabs? [^)]*)\)', r' [\1]', t)
    t = t.replace("The Respondent's amended statement of facts and contentions dated 13 May 2026, as presently constituted,", "The SOFC (13 May 2026)")
    t = t.replace("The Respondent's amended statement of facts and contentions dated 13 May 2026", "The SOFC (13 May 2026)")
    t = t.replace("The Respondent's amended List of Documents dated 14 August 2026", "The Respondent's LOD (14 Aug 2026)")
    return t.strip()
ANT = [  # replace orphaned antecedents with the full source name
 (r'^That role description', 'The role description (Tab 1)'),
 (r'^That decision', 'Review Decision 69983'),
 (r'^That amended statement of facts and contentions, as presently constituted,', 'The SOFC (13 May 2026)'),
 (r'^That amended statement of facts and contentions', 'The SOFC (13 May 2026)'),
 (r'^That history', 'The myHR leave history for 15480560'),
 (r'^That register', 'The 2024 Emergency Code Register'),
 (r'^That report', 'The myHR submissions report (MSH Item 11)'),
 (r'^That letter', "MSH's letter of 5 June 2026 (K-LM26/729)"),
 (r'^That Consultation Paper', 'The Consultation Paper'),
 (r'^That document', 'The Consultation outcome document'),
 (r'^That Instrument', 'The Instrument of Sub-Delegation'),
 (r'^In that response the Respondent', 'In its response of 18 February 2026 to the notice to admit, the Respondent'),
 (r'^In admitting that paragraph', 'In admitting paragraph 8 of that notice'),
 (r'^Beneath it in the same document is', 'The same document (Tab 1B) contains'),
 (r'^In that history', 'In the myHR leave history for 15480560,'),
]
OVR = {45: "Ms Stibbard's email of 18 July 2023", 50: "Ms Taylor's email of 15 April 2024", 31: "The Appellant's application of 31 August 2023",
       190: "Payroll's message of 3 May 2024", 188: "Payroll's message of 3 May 2024"}
def text(n, prev):
    t = clean(F[n])
    if prev != n - 1:
        if n in OVR:
            t = re.sub(r'^That (email|message|application)', OVR[n], t)
        for a, b in ANT:
            t = re.sub(a, b, t)
    return t
SEQ = {}
def S(key, title, groups): SEQ[key] = (title, groups)
S('1a', '1(a) Directives, the manager\'s hours, and misrouted calls', [
 ('The role and the admitted standard', [2, 6, 8, 9, 289]),
 ('18 July 2023: the database and the contact book', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 55]),
 ('23 August 2023: the manager\'s hours', [70, 71, 72, 73]),
 ('15 and 19 April 2024: directives', [49, 50, 51, 52, 53, 181, 273, 54]),
 ('2 to 9 May 2024: misrouted calls', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]),
 ('13 to 17 May 2024: on call, contact rules, the hours asked for and given', [111, 112, 162, 163, 164, 165, 166, 89, 90, 74, 75, 113, 81, 82, 83, 84, 88]),
 ('20 May 2024: the directory', [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]),
 ('18 June 2024: onset day', [85, 86, 87]),
 ('The employer\'s position and the record', [267, 272, 290, 291, 281, 282, 303]),
])
S('1b', '1(b) The Communication Book', [
 ('6 June 2023: the removal', [148, 149, 145, 146, 147, 143, 144, 288]),
 ('What the Respondent does not have or allege', [150, 151, 152, 153, 154]),
 ('18 July 2023: a second record removed', [45]),
 ('The standard', [289, 12]),
])
S('1c', '1(c) August 2023: concerns about rostering and fatigue', [
 ('The standard already in place (June 2020)', [239, 240]),
 ('7 to 9 August 2023: raised, acknowledged, redirected', [26, 27, 155, 156, 157, 158, 287, 28, 29]),
 ('29 August to 4 September 2023', [160, 161]),
 ('April to May 2024: the same issue again', [211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223]),
 ('Nothing assessed or changed before 30 June 2024', [264, 269, 270, 271, 272]),
])
S('1f', '1(f) The 15 May 2024 email and the request to retract', [
 ('23 August 2023: the manager raises her own hours', [71, 72, 73]),
 ('April to May 2024: contact her in office hours', [50, 162, 164]),
 ('15 May 2024', [74, 75, 76, 77, 78]),
 ('17 and 21 May 2024', [81, 82, 83, 84, 88, 79, 80]),
 ('What the Respondent does not allege', [300, 301, 302]),
])
S('1g', '1(g) Union representation (reserve)', [
 ('The facts', [31, 32, 293, 167, 168, 180, 181, 178, 179]),
])
S('2a', '2(a) Persistent payroll failures: (i) the four fortnights', [
 ('The contract', [37, 38]),
 ('April 2024: raised by me', [242, 246]),
 ('3 May 2024: Payroll identifies the errors', [182, 183, 184, 185, 186, 187, 188, 189, 296]),
 ('The record', [210, 255, 256]),
])
S('2a2', '2(a) Persistent payroll failures: (ii) the pandemic leave entitlement', [
 ('The entitlement and the authority', [127, 128]),
 ('20 February 2024', [136, 114, 115]),
 ('21 February 2024: first refusal', [116, 137, 138]),
 ('28 to 29 February 2024: second refusal, then approval', [117, 118, 139, 119, 120, 124]),
 ('1 March 2024: final approval', [121, 125, 140, 141, 122, 123, 126]),
 ('The Respondent\'s own account', [132, 133, 134, 135]),
 ('What the Respondent does not allege', [129, 130, 131, 142]),
])
S('2b', '2(b) The delay, and a correction I could not make myself', [
 ('April 2024: asked for a review', [242, 246]),
 ('3 May 2024: the direction to the manager', [183, 190, 296]),
 ('10 to 28 May 2024', [191, 192, 193, 194, 195, 298, 196, 197, 209, 297]),
 ('The myHR record', [198, 199, 200, 201, 202, 203, 204, 205, 206, 210]),
 ('The pandemic leave: the same dependence on the manager', [122, 123, 126]),
 ('The Respondent\'s position', [207, 208]),
])
S('3', 'STRESSOR 3: the whole story', [
 ('A. The role [3(b)]', [1, 2, 7, 8, 12, 13, 14, 15, 16]),
 ('B. The standard [3(b)]', [285, 257, 239, 240]),
 ('C. The 2020 agreement [3(c)]', [17, 23, 24, 25, 18, 19, 20, 21, 22]),
 ('D. August 2023: the earlier rostering error and "the required rest period" [3(b)]', [28, 156, 157, 287]),
 ('E. 17 to 18 March 2024: the break [3(a)]', [180, 284, 227, 258, 259, 251, 234]),
 ('F. The emergency load on the day [3(b)] (register entries NOT ADMITTED)', [268, 228, 229, 230]),
 ('G. 19 March 2024: sick leave [3(c)]', [235, 231, 188]),
 ('H. 8 April to 1 May 2024: the fatigue request, 23 days [3(c)]', [242, 243, 244, 245, 246, 247, 248, 249, 250]),
 ('I. 16 April to 20 May 2024: the continuing exposure', [211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223]),
 ('J. No fatigue system before 30 June 2024 [3(b)]', [263, 264, 265, 269, 270, 271]),
 ('K. The employer\'s response and the Review Decision, 6 September to 24 October 2024 [3(c), 3(d)]', [252, 253, 254, 260, 261, 262, 295]),
 ('L. HR, 7 July 2026: what the agreement covers [3(c)]', [224, 225]),
 ('M. The Respondent\'s positions', [226, 232, 286, 233, 236, 237, 238]),
 ('N. What the Respondent does not allege', [303, 300, 301, 302]),
])
out = []
for key, (title, groups) in SEQ.items():
    out.append(f"\n## {title}\n")
    for g, ns in groups:
        out.append(f"**{g}**\n")
        prev = None
        for n in ns:
            flag = ' **[NOT ADMITTED]**' if n in NA else ''
            out.append(f"- **{n}**{flag} {text(n, prev)}")
            prev = n
        out.append("")
open('_seq_body.md', 'w').write("\n".join(out))
# orphan check
for key, (title, groups) in SEQ.items():
    for g, ns in groups:
        prev = None
        for n in ns:
            t = text(n, prev)
            if re.match(r'^(That|Each of those|In that response|In admitting|Beneath it|In that history)', t) and prev != n - 1:
                print('ORPHAN', key, n, t[:90])
            prev = n
