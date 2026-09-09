#!/usr/bin/env python3
"""WC/2024/227 — assemble the complete 9 September 2026 set, in one pass, from one source.

Runs every builder in dependency order, then writes BOTH delivery folders from the same
build so they can never drift apart:

  out/FINAL_9SEP2026/1_COMMISSION   filed in the Industrial Registry (direction 1)
  out/FINAL_9SEP2026/2_REGULATOR    served on the Respondent (directions 1 and 2)
  out/FINAL_9SEP2026/3_EMAILS       the emails, as text to paste
  out/SEND_9SEP2026                 the same PDFs under numbered names, for sending order

Every PDF is verified after assembly: no document information dictionary, no XMP packet,
no page-level metadata, no annotations, no embedded files. The build FAILS if any survives,
or if either outline runs past one A4 page (direction 2), or if a source file is missing.
"""
import os, shutil, subprocess, sys
import pikepdf

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

BUILDERS = [
    "build_outlines.py",                          # direction 2 — three lay outlines
    "build_medical_schedule.py",                  # direction 2 — the schedule (page 1 of the bundle)
    "build_medical_bundle.py",                    # direction 2 — schedule + Tabs M1-M9
    "build_direction_pack.py",                    # direction 1 — witness list + Registry letter
    "build_letter_regulator_8sep_response.py",    # reply to the Regulator's letter of 8 Sep
    "build_letter_regulator_further_request.py",  # request: the documents not admitted
]

# source in out/  ->  (commission name or None, regulator name or None, numbered send name)
MAP = [
    ("out/WITNESS_LIST_SERVE_9SEP2026.pdf",
     "Appellant_List_of_Witnesses_WC2024227.pdf",
     "Appellant_List_of_Witnesses_WC2024227.pdf",
     "01_WITNESS_LIST.pdf"),
    ("out/COVERING_LETTER_REGISTRY_9SEP2026.pdf",
     "Covering_Letter_to_Industrial_Registrar_WC2024227.pdf",
     "Covering_Letter_to_Industrial_Registrar_WC2024227.pdf",
     "02_COVERING_LETTER_REGISTRY.pdf"),
    ("out/LETTER_TO_REGULATOR_re_8SEP_letter_9SEP2026.pdf",
     None,
     "Letter_to_Regulator_re_letter_of_8_September_2026_WC2024227.pdf",
     "02A_LETTER_TO_MATHESON_re_8SEP_letter.pdf"),
    ("out/LETTER_TO_REGULATOR_request_documents_not_admitted_9SEP2026.pdf",
     None,
     "Request_to_Regulator_documents_not_admitted_WC2024227.pdf",
     "02B_REQUEST_documents_not_admitted.pdf"),
    ("out/OUTLINE_00_SHEPHERD.pdf",
     None,
     "Outline_of_Evidence_Cory_Lea_Shepherd_WC2024227.pdf",
     "03_OUTLINE_SHEPHERD.pdf"),
    ("out/OUTLINE_02_HARRISONJONES.pdf",
     None,
     "Outline_of_Evidence_Cory_Harrison-Jones_WC2024227.pdf",
     "04_OUTLINE_HARRISON-JONES.pdf"),
    ("out/OUTLINE_03_CONAGHAN.pdf",
     None,
     "Outline_of_Evidence_Patricia_Conaghan_WC2024227.pdf",
     "05_OUTLINE_CONAGHAN.pdf"),
    ("out/SCHEDULE_OF_MEDICAL_DOCUMENTS_RELIED_UPON.pdf",
     None,
     "Schedule_of_Medical_Documents_Relied_Upon_WC2024227.pdf",
     "07_MEDICAL_SCHEDULE.pdf"),
    ("out/MEDICAL_DOCUMENTS_TABS_M1_to_M9.pdf",
     None,
     "Medical_Documents_Relied_Upon_Tabs_M1_to_M9_WC2024227.pdf",
     "08_MEDICAL_DOCUMENTS_TABS_M1_to_M9.pdf"),
]

ONE_PAGE_ONLY = {   # direction 2: one A4 page per witness
    "out/OUTLINE_00_SHEPHERD.pdf",
    "out/OUTLINE_02_HARRISONJONES.pdf",
    "out/OUTLINE_03_CONAGHAN.pdf",
}

FINAL = "out/FINAL_9SEP2026"
SEND = "out/SEND_9SEP2026"
# a second copy of the PDFs has historically lived here; it is rewritten every build so that no
# superseded version of a served document can survive in it
SEND_MIRROR = "out/SEND_9SEP2026/TO_MATHESON_9SEP2026"
COMM, REG, MAIL = f"{FINAL}/1_COMMISSION", f"{FINAL}/2_REGULATOR", f"{FINAL}/3_EMAILS"


def run_builders():
    for b in BUILDERS:
        print(f"\n--- {b}")
        r = subprocess.run([sys.executable, b], capture_output=True, text=True)
        sys.stdout.write(r.stdout)
        if r.returncode != 0:
            sys.stderr.write(r.stderr)
            raise SystemExit(f"\nBUILD FAILED: {b}")


def verify(path):
    """Return (pages, problems[]). A clean file has no metadata of any kind."""
    problems = []
    pdf = pikepdf.open(path)
    if dict(pdf.docinfo):
        problems.append(f"document info: {list(dict(pdf.docinfo))}")
    if "/Metadata" in pdf.Root:
        problems.append("XMP packet on the catalogue")
    for k in ("/PieceInfo", "/Names", "/AcroForm", "/OpenAction", "/AA", "/StructTreeRoot"):
        if k in pdf.Root:
            if k == "/Names" and "/EmbeddedFiles" not in pdf.Root["/Names"]:
                continue
            problems.append(f"catalogue key {k}")
    for i, pg in enumerate(pdf.pages, 1):
        for k in ("/Metadata", "/PieceInfo", "/Annots", "/AA"):
            if k in pg.obj:
                problems.append(f"page {i} key {k}")
    try:
        with pdf.open_metadata(set_pikepdf_as_editor=False) as m:
            if len(list(m)):
                problems.append("XMP fields present")
    except Exception:
        pass
    return len(pdf.pages), problems


def main():
    run_builders()

    for d in (COMM, REG, MAIL, SEND, SEND_MIRROR):
        os.makedirs(d, exist_ok=True)

    print("\n--- assembling and verifying\n")
    print(f"{'file':58s} {'pp':>4s} {'MB':>6s}  status")
    failures = []
    for src, comm, reg, send in MAP:
        if not os.path.exists(src):
            failures.append(f"{src}: MISSING after build")
            continue
        n, problems = verify(src)
        if src in ONE_PAGE_ONLY and n != 1:
            problems.append(f"{n} pages — direction 2 allows one A4 page per witness")
        if problems:
            failures.append(f"{src}: " + "; ".join(problems))
        for folder, name in ((COMM, comm), (REG, reg), (SEND, send), (SEND_MIRROR, send)):
            if name:
                shutil.copy2(src, os.path.join(folder, name))
        mb = os.path.getsize(src) / 1048576
        print(f"{os.path.basename(src):58s} {n:4d} {mb:6.2f}  " + ("CLEAN" if not problems else "PROBLEM"))

    # The emails live ONLY in FINAL/3_EMAILS. They are not mirrored into the numbered folder:
    # their ATTACH blocks name the FINAL filenames, and a second copy under different names is
    # how the wrong version gets sent. SEND_9SEP2026 holds the PDFs and the held drafts only.
    for required in ("Email_1_to_Industrial_Registry_cc_Regulator.txt",
                     "Email_2_to_Regulator_direction_2_material.txt",
                     "Email_3_to_Regulator_request_documents_not_admitted.txt",
                     "Email_4_to_Dr_Krishnaiah_records_still_needed.txt"):
        if not os.path.exists(os.path.join(MAIL, required)):
            failures.append(f"{required}: MISSING from 3_EMAILS")

    if failures:
        print("\n".join("  ⛔ " + f for f in failures))
        raise SystemExit("\nASSEMBLY FAILED — nothing above should be served until these are fixed.")

    print(f"\nAll files clean. Serve from {FINAL}. {SEND} carries the same PDFs under numbered names.")


if __name__ == "__main__":
    main()
