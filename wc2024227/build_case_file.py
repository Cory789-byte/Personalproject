#!/usr/bin/env python3
"""WC/2024/227 — assemble CASE_FILE/, the navigable case file.

⛔ COPIES, NEVER MOVES. Every builder script, the full-text index and the manifest reference the
original paths under documents/, drafts/ and lodgement/. Moving anything breaks them silently.
CASE_FILE/ is a second, human-ordered view of the same material and is rebuilt from scratch on
every run.

The spine is the direction of travel:
    01  what the Commission ISSUED            (orders and directions)
    02  what was SENT TO the Commission       (submissions, applications, filings)
    03  what was SERVED ON the Respondent
    04  what came FROM the Respondent
    05  what came FROM Metro South Health
    06  the evidence, by the limb it goes to
    07  working analysis  — internal
    08  not for service   — internal

Bulk collections (91 rosters, the correspondence packs, the disclosure productions, medical) are
NOT copied. Each folder that has such a collection behind it carries a POINTER.md naming the
directory to open. Run:  python3 build_case_file.py
"""
import os, shutil, glob, sys

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
ROOT = "CASE_FILE"
DRA, LOD = "drafts/out", "lodgement"
F9 = f"{DRA}/FINAL_9SEP2026"

# destination folder -> (blurb, [(source, optional new name)], [pointer lines])
TREE = {

"01_ORDERS_AND_DIRECTIONS": (
 "Issued BY the Commission. The Further Directions Order (3) of 19 August 2026 is the live one: "
 "directions 1 and 2 fell due 4.00 pm 9 September 2026; directions 3 and 4 fall due 4.00 pm "
 "30 September 2026.",
 [(f, None) for f in sorted(glob.glob("documents/orders/*"))], []),

"02_SUBMISSIONS_TO_QIRC/01_pleadings": (
 "The Appellant's case as pleaded.",
 [("documents/filings/2026-04-08_Amended_Form9A_SOFC_Appellant.pdf", None)], []),

"02_SUBMISSIONS_TO_QIRC/02_applications_and_notices": (
 "Applications and notices filed in the Registry.",
 [("documents/filings/2026-02-27_Form4_Application_Disclosure_stamped.pdf", None),
  ("documents/filings/2026-02-25_Supplementary_Form4.pdf", None),
  ("documents/filings/2026-04-22_Form29_Notice_NonParty_Disclosure_sealed.pdf", None),
  ("documents/filings/2025-08_Form35_Withdrawal_of_Saines_Legal_Paul_Conrad.pdf", None),
  (f"{LOD}/WC2024227_Form_4_Application_Rule_64G.pdf", "2026-06-23_Form4_Application_Rule_64G.pdf"),
  (f"{LOD}/WC2024227_Draft_Order.pdf", "2026-06-23_Draft_Order_for_the_Form4.pdf"),
  (f"{LOD}/WC2024227_Form21_Certificates.pdf", "2026-06-23_Form21_Exhibit_Certificates.pdf")], []),

"02_SUBMISSIONS_TO_QIRC/03_affidavits": (
 "⛔ The three February 2026 affidavits have NO TEXT LAYER. Render them; do not grep them.",
 [("documents/filings/2026-02-27_Affidavit_for_Form4_Disclosure_stamped.pdf", None),
  ("documents/filings/2026-02-25_Supplementary_Affidavit_Form20.pdf", None),
  ("documents/filings/2026-02-26_Supplementary_Affidavit_stamped.pdf", None),
  (f"{LOD}/WC2024227_Form20_FINAL.pdf", "2026-06-23_Form20_Affidavit_of_Cory_Lea_Shepherd.pdf")], []),

"02_SUBMISSIONS_TO_QIRC/04_filed_9_September_2026": (
 "Direction 1 of the Further Directions Order (3). ⭐ The only documents FILED on 9 September 2026 "
 "— direction 2 material is served and NOT filed.",
 [(f"{F9}/1_COMMISSION/Appellant_List_of_Witnesses_WC2024227.pdf", None),
  (f"{F9}/1_COMMISSION/Covering_Letter_to_Industrial_Registrar_WC2024227.pdf", None),
  (f"{F9}/3_EMAILS/Email_1_to_Industrial_Registry_cc_Regulator.txt", None)], []),

"02_SUBMISSIONS_TO_QIRC/05_to_be_filed": (
 "Held, not yet filed.",
 [("drafts/out/SEND_9SEP2026/HOLD_AFTER_11SEP_EMAIL_REGISTRY_FILE_FORM24_FORM25_WITH_RESPONSE.txt",
   "HOLD_file_Form24_Form25_and_responses_after_11SEP2026.txt")],
 ["The Form 24, Form 25, Annexure A, the Respondent's responses of 8 September 2026 and its "
  "covering letter are to be filed together AFTER Friday 11 September 2026."]),

"03_SERVED_ON_THE_RESPONDENT/01_notices_to_admit_28AUG2026": (
 "Served 28 August 2026 at 1:47 pm under rule 49(1).",
 [], ["The Form 24, Form 25 and Annexure A as served are held with the build that produced them "
      "in `drafts/`. The Respondent's responses are at 04_FROM_THE_RESPONDENT."]),

"03_SERVED_ON_THE_RESPONDENT/02_direction_2_material_9SEP2026": (
 "⛔ SERVED, NOT FILED. Direction 2 of the Further Directions Order (3).",
 [(p, None) for p in sorted(glob.glob(f"{F9}/2_REGULATOR/*.pdf"))]
 + [(f"{F9}/3_EMAILS/Email_2_to_Regulator_directions_and_request.txt", None)], []),

"03_SERVED_ON_THE_RESPONDENT/03_earlier_service": (
 "Served before 9 September 2026.",
 [("documents/2026-08-11_Stressor1a_Particulars_Bundle_SERVED_on_Matheson.pdf", None),
  ("documents/2026-07-24_Cory_to_Matheson_disclosure_list_request.pdf", None),
  (f"{DRA}/LIST_OF_DOCUMENTS_WC2024227.pdf", "2026-08-05_Appellant_List_of_Documents_AS_SERVED.pdf"),
  (f"{DRA}/LIST_OF_DOCUMENTS_BY_SOFC_WC2024227.pdf",
   "2026-09-09_Appellant_List_of_Documents_BY_MATTER_IN_ISSUE_not_yet_served.pdf")], []),

"04_FROM_THE_RESPONDENT/01_response_to_the_notices_8SEP2026": (
 "⭐ 298 of 303 facts admitted; 14 of 39 tabs disputed as to authenticity. See "
 "07_WORKING_ANALYSIS for what that response is and is not.",
 [(p, None) for p in sorted(glob.glob("documents/regulator-response-2026-09-08/*"))], []),

"04_FROM_THE_RESPONDENT/02_pleadings_and_lists": (
 "The Respondent's own case and disclosure.",
 [("documents/WC.2024.227_Regulator_SOFC_13.05.2026.pdf", None),
  ("documents/2025-07_Regulator_SOFC_Form9C_original.pdf", None),
  ("documents/2025-07-22_Regulator_SOFC_served_via_Saines.pdf", None),
  ("documents/2026-08-14_Regulator_AMENDED_List_of_Documents_Form23.pdf", None),
  ("documents/2026-08-14_1028_Matheson_amended_LOD_and_NNPDs_covering_email.pdf", None)], []),

"04_FROM_THE_RESPONDENT/03_review_decision_and_notices": (
 "⚠ The Review Decision copy here is a later re-save. The clean original "
 "(f59eb0c1…, sha256 d0b2a514…) is NOT in the repository — re-obtain it before any forensic use.",
 [("documents/Review_Decision_69983_24.10.2024.pdf", None),
  ("documents/2025-07-04_NNPD_Regulator_to_MindAndMemory_SEALED.pdf", None),
  ("documents/2025-07-04_NNPD_Regulator_to_OurMedicalAshmore_SEALED.pdf", None),
  ("documents/2025-07-04_NNPD_Regulator_to_QldHealth_SEALED.pdf", None),
  ("documents/2026-04-27_NNPD_Regulator_to_QldHealth_COVIDleave_PRN15480560.pdf", None),
  ("documents/2026-07-16_Matheson_Calderbank2_rejection.pdf", None)],
 ["The Respondent's July 2025 disclosure is at `documents/disclosure-2025-07/`."]),

"05_FROM_METRO_SOUTH/01_answer_to_the_commission": (
 "Metro South is a non-party. Its letter of 5 June 2026 is Annexure A Tab 20 and is already before "
 "the Commission; its authenticity was not admitted on 8 September 2026.",
 [("documents/2026-06-05_MSH_Objection_KLM26-729_Cridland.pdf", None)],
 ["What Metro South actually produced is at `documents/disclosure-2026-06_MSH_production/`."]),

"05_FROM_METRO_SOUTH/02_employment_correspondence": (
 "The employment track. ⛔ Sequenced behind the appeal; keep its arguments out of appeal filings.",
 [("documents/2024-09-26_MSH_ShowCause_Abandonment_Coccetti_K-CF24-3196.pdf", None),
  ("documents/2024-10-09_MSH_Confirmation_Abandonment_Johns_K-CF24-3270.pdf", None),
  ("documents/2024-10-09_Cory_reply_DRAFT_to_abandonment_letter_Firoz_Johns.pdf", None),
  ("documents/2024-10-11_Cory_reply_to_abandonment_SENT.eml", None),
  ("documents/2026-07-07_MSH_HR_Forrest_ECC_further_information.pdf", None),
  ("documents/2024-11-14_MSH_Consultation_Paper_Proposed_Rosters_LH_Switchboard.pdf", None),
  ("documents/2024-12_MSH_Consultation_Outcome_Proposed_Rosters_LH_Switchboard.pdf", None)], []),

"06_EVIDENCE/01_the_role": (
 "Stressor 1(a) and SOFC ¶1.1. Contents admitted at facts 1–13.",
 [("documents/AO3_Switchboard_Role_Description_MSH.pdf", None)], []),

"06_EVIDENCE/02_rosters": (
 "⭐ Unbroken coverage PP17 (22 Jan 2024) → PP27 (23 Jun 2024). ⛔ EVERY ROSTER IS A SCAN WITH NO "
 "TEXT LAYER — grep cannot see them. Render with pypdfium2 and read the page.",
 [], ["91 files at `documents/rosters/` and `documents/rosters/2023-24_published/`.",
      "⭐ `2024-03-18_to_03-31_PP21_v1.0_NO_SHEPHERD_LINE.pdf` — the fortnight beginning the day "
      "after the 7-hour break carries no line for the Appellant. No v2.0 is held."]),

"06_EVIDENCE/03_payroll_and_leave": (
 "Stressor 2. ⭐ Facts 182–210 are all admitted and prove the limb by subtraction — see "
 "07_WORKING_ANALYSIS/EVIDENCE-BY-LIMB-integrated.md §2. ⛔ No 2024 payslip is held.",
 [("documents/2026-09-04_Leave_Takings_Report_25MAR2019-04SEP2026_FULL.xlsx", None),
  ("documents/evidence/Shepherd_Payslips_FY2025-26_analysis.xlsx", None),
  ("documents/financial/Shepherd_2025_RTW_7_Fortnights_Days_QSuper.xlsx", None)], []),

"06_EVIDENCE/04_emergency_codes": (
 "⛔ Stressor 3 and the ONLY contested document in the case. Annexure A Tab 31; facts 228–231 not "
 "admitted; authenticity not admitted. The native workbook is on Metro South's systems.",
 [("documents/2026-08-28_Emergency_Code_Register_MARCH2024_capture.pdf", None)], []),

"06_EVIDENCE/05_medical": (
 "Contention 1, s 32(1). Served 9 September 2026 behind the schedule of medical documents.",
 [(f"{F9}/2_REGULATOR/Schedule_of_Medical_Documents_Relied_Upon_Tabs_M1_to_M9_WC2024227.pdf", None)],
 ["The underlying records are at `documents/medical/`. ⛔ Redacted pages for Tab M1 are held at "
  "`drafts/assets/redacted/` and are the only copy — losing them rebuilds the bundle UNREDACTED."]),

"06_EVIDENCE/06_correspondence_packs": (
 "Produced in full on 5 August 2026 as List items 9 to 14.",
 [], ["`documents/correspondence-packs/`, `documents/correspondence/`, "
      "`documents/correspondence-2026/`, and the whole record in one searchable file at "
      "`corpus/FULL_CORPUS.md` (154 messages, 2020–2026). ⛔ Never quote into a filing from the "
      "corpus — only from the source PDF."]),

"07_WORKING_ANALYSIS": (
 "⛔ INTERNAL. None of this is phrased for service.",
 [("skill/references/EVIDENCE-BY-LIMB-integrated.md", None),
  ("skill/references/THE-NON-ADMISSIONS-8SEP2026.md", None),
  ("skill/references/MENTION-STEP-BY-STEP-forensic.md", None),
  ("skill/references/RD69983-OBJECT-LEVEL-FORENSICS.md", None),
  ("working-notes.md", None), ("CURRENT.md", None), ("MASTER.md", None)], []),

"08_NOT_FOR_SERVICE": (
 "⛔ Neither served nor filed, and not to be.",
 [(f"{DRA}/REVIEW_BUNDLE_9SEP2026.pdf", None),
  (f"{DRA}/RD69983_FILE_METADATA_1PAGE.pdf", None),
  (f"{F9}/00_SEND_SHEET.md", "SEND_SHEET_9SEP2026.md")], []),
}


def main():
    if os.path.isdir(ROOT):
        shutil.rmtree(ROOT)
    placed = missing = 0
    lines = ["# WC/2024/227 — CASE FILE", "",
             "> Rebuilt by `python3 build_case_file.py`. **Copies, never moves** — the builders, the",
             "> full-text index and the manifest all reference the original paths, so nothing here is",
             "> authoritative for a script. Bulk collections are not copied; each folder that has one",
             "> behind it carries a `POINTER.md`.", "",
             "| Folder | What is in it |", "|---|---|"]
    for dest, (blurb, files, pointers) in TREE.items():
        os.makedirs(os.path.join(ROOT, dest), exist_ok=True)
        got = []
        for src, name in files:
            if not os.path.exists(src):
                print(f"  ⛔ MISSING  {src}"); missing += 1; continue
            shutil.copy2(src, os.path.join(ROOT, dest, name or os.path.basename(src)))
            got.append(name or os.path.basename(src)); placed += 1
        with open(os.path.join(ROOT, dest, "README.md"), "w") as fh:
            fh.write(f"# {dest}\n\n{blurb}\n")
            if got:
                fh.write("\n## In this folder\n\n" + "".join(f"- `{g}`\n" for g in sorted(got)))
        if pointers:
            with open(os.path.join(ROOT, dest, "POINTER.md"), "w") as fh:
                fh.write(f"# Held elsewhere — {dest}\n\n" + "".join(f"- {p}\n" for p in pointers))
        lines.append(f"| `{dest}` | {blurb.split('.')[0]}. {len(got)} file(s)"
                     f"{' + pointer' if pointers else ''} |")
    lines += ["", "## The two folders asked for", "",
              "- **`01_ORDERS_AND_DIRECTIONS/`** — everything the Commission has issued.",
              "- **`02_SUBMISSIONS_TO_QIRC/`** — everything filed or sent to the Commission, in five",
              "  sub-folders: pleadings, applications and notices, affidavits, what was filed on",
              "  9 September 2026, and what is held to be filed after 11 September 2026.", "",
              "⛔ Direction 2 material is **served and not filed**. It is at",
              "`03_SERVED_ON_THE_RESPONDENT/`, never at `02_SUBMISSIONS_TO_QIRC/`."]
    open(os.path.join(ROOT, "00_INDEX.md"), "w").write("\n".join(lines) + "\n")
    print(f"\n{ROOT}: {placed} files placed, {len(TREE)} folders"
          + (f", ⛔ {missing} MISSING" if missing else ", nothing missing"))
    if missing:
        sys.exit("sources missing — fix the map before relying on the tree")


if __name__ == "__main__":
    main()
