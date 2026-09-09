#!/usr/bin/env python3
"""WC/2024/227 — assemble CASE_FILE/, the navigable case file.

⛔ COPIES, NEVER MOVES. Every builder script, the full-text index and the manifest reference the
original paths under documents/, drafts/ and lodgement/. Moving anything breaks them silently.
CASE_FILE/ is a second, human-ordered view of the same material and is rebuilt from scratch on
every run.

Folders are ordered by direction of travel: issued by the Commission; sent to the Commission;
served on the Respondent; received from the Respondent; received from Metro South Health; evidence;
working papers; and material neither served nor filed.

⛔ Folder descriptions are DESCRIPTIVE ONLY. They say what a document is, who it is from and when.
They carry no assessment of the case, of any document's weight, or of any party's position.

Bulk collections — the rosters, the correspondence packs, the disclosure productions and the
medical records — ARE copied in, as sub-folders. Git stores identical content once regardless of
path, so the duplication costs working-tree disk and almost nothing in the repository.
Run:  python3 build_case_file.py
"""
import os, shutil, glob, sys

HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
ROOT = "CASE_FILE"
DRA, LOD = "drafts/out", "lodgement"
F9 = f"{DRA}/FINAL_9SEP2026"

# destination folder -> (blurb, [(source, optional new name)], [pointer lines])
TREE = {

"01_ORDERS_AND_DIRECTIONS": (
 "Orders and directions issued by the Commission in this proceeding.",
 [(f, None) for f in sorted(glob.glob("documents/orders/*"))], []),

"02_SUBMISSIONS_TO_QIRC/01_pleadings": (
 "The Appellant's statement of facts and contentions.",
 [("documents/filings/2026-04-08_Amended_Form9A_SOFC_Appellant.pdf", None)], []),

"02_SUBMISSIONS_TO_QIRC/02_applications_and_notices": (
 "Applications and notices filed in the Industrial Registry.",
 [("documents/filings/2026-02-27_Form4_Application_Disclosure_stamped.pdf", None),
  ("documents/filings/2026-02-25_Supplementary_Form4.pdf", None),
  ("documents/filings/2026-04-22_Form29_Notice_NonParty_Disclosure_sealed.pdf", None),
  ("documents/filings/2025-08_Form35_Withdrawal_of_Saines_Legal_Paul_Conrad.pdf", None),
  (f"{LOD}/WC2024227_Form_4_Application_Rule_64G.pdf", "2026-06-23_Form4_Application_Rule_64G.pdf"),
  (f"{LOD}/WC2024227_Draft_Order.pdf", "2026-06-23_Draft_Order_for_the_Form4.pdf"),
  (f"{LOD}/WC2024227_Form21_Certificates.pdf", "2026-06-23_Form21_Exhibit_Certificates.pdf")], []),

"02_SUBMISSIONS_TO_QIRC/03_affidavits": (
 "Affidavits filed in the Industrial Registry. The three February 2026 affidavits are scans "
 "without a text layer.",
 [("documents/filings/2026-02-27_Affidavit_for_Form4_Disclosure_stamped.pdf", None),
  ("documents/filings/2026-02-25_Supplementary_Affidavit_Form20.pdf", None),
  ("documents/filings/2026-02-26_Supplementary_Affidavit_stamped.pdf", None),
  (f"{LOD}/WC2024227_Form20_FINAL.pdf", "2026-06-23_Form20_Affidavit_of_Cory_Lea_Shepherd.pdf")], []),

"02_SUBMISSIONS_TO_QIRC/04_filed_9_September_2026": (
 "Filed in the Industrial Registry on 9 September 2026 under direction 1 of the Further Directions "
 "Order (3) dated 19 August 2026. Material served under direction 2 is at 03_SERVED_ON_THE_RESPONDENT.",
 [(f"{F9}/1_COMMISSION/Appellant_List_of_Witnesses_WC2024227.pdf", None),
  (f"{F9}/1_COMMISSION/Covering_Letter_to_Industrial_Registrar_WC2024227.pdf", None),
  (f"{F9}/3_EMAILS/Email_1_to_Industrial_Registry_cc_Regulator.txt", None)], []),

"02_SUBMISSIONS_TO_QIRC/05_to_be_filed": (
 "Prepared for filing. Not yet filed.",
 [("drafts/out/SEND_9SEP2026/HOLD_AFTER_11SEP_EMAIL_REGISTRY_FILE_FORM24_FORM25_WITH_RESPONSE.txt",
   "HOLD_file_Form24_Form25_and_responses_after_11SEP2026.txt")],
 ["To be filed after Friday 11 September 2026: the Form 24, the Form 25, Annexure A, the "
  "Respondent's responses of 8 September 2026 and its covering letter."]),

"03_SERVED_ON_THE_RESPONDENT/01_notices_to_admit_28AUG2026": (
 "Notices to admit facts and documents served on the Respondent on 28 August 2026 at 1:47 pm "
 "under rule 49(1).",
 [], ["The Form 24, Form 25 and Annexure A as served are held in `drafts/`. The Respondent's "
      "responses are at 04_FROM_THE_RESPONDENT."]),

"03_SERVED_ON_THE_RESPONDENT/02_direction_2_material_9SEP2026": (
 "Served on the Respondent on 9 September 2026 under direction 2 of the Further Directions Order "
 "(3) dated 19 August 2026. Not filed.",
 [(p, None) for p in sorted(glob.glob(f"{F9}/2_REGULATOR/*.pdf"))]
 + [(f"{F9}/3_EMAILS/Email_2_to_Regulator_directions_and_request.txt", None)], []),

"03_SERVED_ON_THE_RESPONDENT/03_earlier_service": (
 "Served on the Respondent before 9 September 2026.",
 [("documents/2026-08-11_Stressor1a_Particulars_Bundle_SERVED_on_Matheson.pdf", None),
  ("documents/2026-07-24_Cory_to_Matheson_disclosure_list_request.pdf", None),
  (f"{DRA}/LIST_OF_DOCUMENTS_WC2024227.pdf", "2026-08-05_Appellant_List_of_Documents_AS_SERVED.pdf"),
  (f"{DRA}/LIST_OF_DOCUMENTS_BY_SOFC_WC2024227.pdf",
   "2026-09-09_Appellant_List_of_Documents_BY_MATTER_IN_ISSUE_not_yet_served.pdf")], []),

"04_FROM_THE_RESPONDENT/01_response_to_the_notices_8SEP2026": (
 "The Respondent's responses to the notices to admit facts and documents, and its covering "
 "letter, served on 8 September 2026.",
 [(p, None) for p in sorted(glob.glob("documents/regulator-response-2026-09-08/*"))], []),

"04_FROM_THE_RESPONDENT/02_pleadings_and_lists": (
 "The Respondent's statements of facts and contentions and its lists of documents.",
 [("documents/WC.2024.227_Regulator_SOFC_13.05.2026.pdf", None),
  ("documents/2025-07_Regulator_SOFC_Form9C_original.pdf", None),
  ("documents/2025-07-22_Regulator_SOFC_served_via_Saines.pdf", None),
  ("documents/2026-08-14_Regulator_AMENDED_List_of_Documents_Form23.pdf", None),
  ("documents/2026-08-14_1028_Matheson_amended_LOD_and_NNPDs_covering_email.pdf", None)], []),

"04_FROM_THE_RESPONDENT/03_review_decision_and_notices": (
 "Review Decision 69983 and notices of non-party disclosure issued by the Respondent. The copy of "
 "the Review Decision held here is a later re-save; the original file is not in the repository.",
 [("documents/Review_Decision_69983_24.10.2024.pdf", None),
  ("documents/2025-07-04_NNPD_Regulator_to_MindAndMemory_SEALED.pdf", None),
  ("documents/2025-07-04_NNPD_Regulator_to_OurMedicalAshmore_SEALED.pdf", None),
  ("documents/2025-07-04_NNPD_Regulator_to_QldHealth_SEALED.pdf", None),
  ("documents/2026-04-27_NNPD_Regulator_to_QldHealth_COVIDleave_PRN15480560.pdf", None),
  ("documents/2026-07-16_Matheson_Calderbank2_rejection.pdf", None)],
 ["The Respondent's disclosure of July 2025 is at `documents/disclosure-2025-07/`."]),

"05_FROM_METRO_SOUTH/01_answer_to_the_commission": (
 "Metro South Hospital and Health Service's response to the notice of non-party disclosure, "
 "addressed to the Commission. Metro South Health is not a party to this proceeding.",
 [("documents/2026-06-05_MSH_Objection_KLM26-729_Cridland.pdf", None)],
 ["Documents produced by Metro South Health are at `documents/disclosure-2026-06_MSH_production/`."]),

"05_FROM_METRO_SOUTH/02_employment_correspondence": (
 "Correspondence with Metro South Hospital and Health Service concerning the Appellant's "
 "employment.",
 [("documents/2024-09-26_MSH_ShowCause_Abandonment_Coccetti_K-CF24-3196.pdf", None),
  ("documents/2024-10-09_MSH_Confirmation_Abandonment_Johns_K-CF24-3270.pdf", None),
  ("documents/2024-10-09_Cory_reply_DRAFT_to_abandonment_letter_Firoz_Johns.pdf", None),
  ("documents/2024-10-11_Cory_reply_to_abandonment_SENT.eml", None),
  ("documents/2026-07-07_MSH_HR_Forrest_ECC_further_information.pdf", None),
  ("documents/2024-11-14_MSH_Consultation_Paper_Proposed_Rosters_LH_Switchboard.pdf", None),
  ("documents/2024-12_MSH_Consultation_Outcome_Proposed_Rosters_LH_Switchboard.pdf", None)], []),

"06_EVIDENCE/01_the_role": (
 "Role description, Administration Officer (AO3), Switchboard Services, Logan Hospital.",
 [("documents/AO3_Switchboard_Role_Description_MSH.pdf", None)], []),

"06_EVIDENCE/02_rosters": (
 "Published Logan Hospital Switchboard Services rosters. Every roster is a scan without a text "
 "layer and must be rendered to be read.",
 [], ["91 files at `documents/rosters/` and `documents/rosters/2023-24_published/`, covering "
      "pay periods from 2023 to October 2024."]),

"06_EVIDENCE/03_payroll_and_leave": (
 "Payroll and leave records. No payslip for the 2024 calendar year is held.",
 [("documents/2026-09-04_Leave_Takings_Report_25MAR2019-04SEP2026_FULL.xlsx", None),
  ("documents/evidence/Shepherd_Payslips_FY2025-26_analysis.xlsx", None),
  ("documents/financial/Shepherd_2025_RTW_7_Fortnights_Days_QSuper.xlsx", None)], []),

"06_EVIDENCE/04_emergency_codes": (
 "Screen capture of the workbook \"2024 Emergency Code Register.xlsx\", March 2024 sheet. "
 "Annexure A Tab 31. The native workbook is held on Metro South Health's systems.",
 [("documents/2026-08-28_Emergency_Code_Register_MARCH2024_capture.pdf", None)], []),

"06_EVIDENCE/05_medical": (
 "The schedule of medical documents relied upon, served 9 September 2026.",
 [(f"{F9}/2_REGULATOR/Schedule_of_Medical_Documents_Relied_Upon_Tabs_M1_to_M9_WC2024227.pdf", None)],
 ["The underlying records are at `documents/medical/`. The redacted pages for Tab M1 are at "
  "`drafts/assets/redacted/` and are the only copy held."]),

"06_EVIDENCE/06_correspondence_packs": (
 "Correspondence packs, produced on 5 August 2026 as items 9 to 14 of the Appellant's list of "
 "documents.",
 [], ["`documents/correspondence-packs/`, `documents/correspondence/` and "
      "`documents/correspondence-2026/`. A consolidated text of the correspondence is at "
      "`corpus/FULL_CORPUS.md`."]),

"07_WORKING_PAPERS": (
 "Working papers. Not part of any filing or service.",
 [("skill/references/EVIDENCE-BY-LIMB-integrated.md", None),
  ("skill/references/THE-NON-ADMISSIONS-8SEP2026.md", None),
  ("skill/references/MENTION-STEP-BY-STEP-forensic.md", None),
  ("skill/references/RD69983-OBJECT-LEVEL-FORENSICS.md", None),
  ("working-notes.md", None), ("CURRENT.md", None), ("MASTER.md", None)], []),

"08_NOT_FOR_SERVICE": (
 "Material that is neither served nor filed.",
 [(f"{DRA}/REVIEW_BUNDLE_9SEP2026.pdf", None),
  (f"{DRA}/RD69983_FILE_METADATA_1PAGE.pdf", None),
  (f"{F9}/00_SEND_SHEET.md", "SEND_SHEET_9SEP2026.md")], []),
}


# destination folder  ->  [(source directory, subfolder name or None)]
# whole collections copied in. Git stores identical content once regardless of path, so the
# duplication costs disk in the working tree but almost nothing in the repository.
DIRS = {
 "03_SERVED_ON_THE_RESPONDENT/01_notices_to_admit_28AUG2026": [],
 "04_FROM_THE_RESPONDENT/03_review_decision_and_notices": [
     ("documents/disclosure-2025-07", "disclosure_July_2025")],
 "05_FROM_METRO_SOUTH/01_answer_to_the_commission": [
     ("documents/disclosure-2026-06_MSH_production", "production_June_2026")],
 "06_EVIDENCE/02_rosters": [
     ("documents/rosters", "rosters")],
 "06_EVIDENCE/03_payroll_and_leave": [
     ("documents/financial", "financial"), ("documents/evidence", "analyses")],
 "06_EVIDENCE/05_medical": [
     ("documents/medical", "records")],
 "06_EVIDENCE/06_correspondence_packs": [
     ("documents/correspondence-packs", "packs"),
     ("documents/correspondence", "correspondence_to_2025"),
     ("documents/correspondence-2026", "correspondence_2026")],
}


def main():
    if os.path.isdir(ROOT):
        shutil.rmtree(ROOT)
    placed = missing = 0
    lines = ["# WC/2024/227 — CASE FILE", "",
             "> Rebuilt by `python3 build_case_file.py`. **Copies, never moves** — the builders, the",
             "> full-text index and the manifest all reference the original paths, so nothing here is",
             "> authoritative for a script. Bulk collections are copied in as sub-folders; a folder that has",
             "> anything else behind it also carries a `POINTER.md`.", "",
             "> Folder descriptions are descriptive only: what a document is, who it is from, and",
             "> when. They carry no assessment of the case or of any document.", "",
             "| Folder | What is in it |", "|---|---|"]
    for dest, (blurb, files, pointers) in TREE.items():
        os.makedirs(os.path.join(ROOT, dest), exist_ok=True)
        got = []
        for src, name in files:
            if not os.path.exists(src):
                print(f"  ⛔ MISSING  {src}"); missing += 1; continue
            shutil.copy2(src, os.path.join(ROOT, dest, name or os.path.basename(src)))
            got.append(name or os.path.basename(src)); placed += 1
        for srcdir, sub in DIRS.get(dest, []):
            if not os.path.isdir(srcdir):
                print(f"  ⛔ MISSING DIR  {srcdir}"); missing += 1; continue
            tgt = os.path.join(ROOT, dest, sub or os.path.basename(srcdir))
            shutil.copytree(srcdir, tgt)
            n = sum(len(fs) for _, _, fs in os.walk(tgt))
            got.append(f"{sub or os.path.basename(srcdir)}/  ({n} files)"); placed += n
        with open(os.path.join(ROOT, dest, "README.md"), "w") as fh:
            fh.write(f"# {dest}\n\n{blurb}\n")
            if got:
                fh.write("\n## In this folder\n\n" + "".join(f"- `{g}`\n" for g in sorted(got)))
        if pointers:
            with open(os.path.join(ROOT, dest, "POINTER.md"), "w") as fh:
                fh.write(f"# Also held elsewhere — {dest}\n\n" + "".join(f"- {p}\n" for p in pointers))
        lines.append(f"| `{dest}` | {blurb.split('.')[0]}. {len(got)} file(s)"
                     f"{' + pointer' if pointers else ''} |")
    lines += ["", "## Orders, and submissions to the Commission", "",
              "- `01_ORDERS_AND_DIRECTIONS/` — orders and directions issued by the Commission.",
              "- `02_SUBMISSIONS_TO_QIRC/` — documents filed or sent to the Commission, in five",
              "  sub-folders: pleadings; applications and notices; affidavits; documents filed on",
              "  9 September 2026; and documents prepared for filing after 11 September 2026.", "",
              "Material served under direction 2 of the Further Directions Order (3) is served and",
              "not filed. It is at `03_SERVED_ON_THE_RESPONDENT/`."]
    open(os.path.join(ROOT, "00_INDEX.md"), "w").write("\n".join(lines) + "\n")
    print(f"\n{ROOT}: {placed} files placed, {len(TREE)} folders"
          + (f", ⛔ {missing} MISSING" if missing else ", nothing missing"))
    if missing:
        sys.exit("sources missing — fix the map before relying on the tree")


if __name__ == "__main__":
    main()
