# Windows runbook — end-to-end

For processing a matter saved at `C:\Evidence\CO-25-2722\`.

## 1. Install tools (once)

Open **PowerShell as Administrator** and run:

```powershell
winget install --id=Gyan.FFmpeg -e
winget install --id=Python.Python.3.12 -e
winget install --id=UB-Mannheim.TesseractOCR -e
winget install --id=Git.Git -e
```

Close and reopen PowerShell so the new PATH picks up.

Verify installs:

```powershell
ffmpeg -version
ffprobe -version
python --version
tesseract --version
git --version
```

## 2. Clone the skill (once)

```powershell
cd C:\Evidence
git clone -b claude/build-evidence-processor-skill-Y1QgE https://github.com/cory789-byte/personalproject.git skill-repo
```

## 3. Install Python deps (once)

```powershell
cd C:\Evidence\skill-repo\skills\bwc-evidence-processor
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install pdfminer.six python-docx openpyxl pypdf striprtf pytesseract Pillow
```

(Leave the venv activated for the rest of the steps.)

## 4. Prepare matter folders (once per matter)

Already done for `CO-25-2722`. For a new matter:

```powershell
$m = "C:\Evidence\CO-25-2722"
mkdir $m\source, $m\output, $m\sworn, $m\config -ErrorAction SilentlyContinue
```

Unzip your disclosure into `C:\Evidence\CO-25-2722\source\`.

## 5. Create a matter config (once per matter)

Copy the template and edit the matter identifiers:

```powershell
Copy-Item keywords\matter_template.json C:\Evidence\CO-25-2722\config\matter_CO-25-2722.json
notepad C:\Evidence\CO-25-2722\config\matter_CO-25-2722.json
```

Fill in `matter_refs` with PID / CO / WC numbers and category phrases.

## 6. Run the batch

```powershell
python scripts\batch_process.py `
    --matter-root   C:\Evidence\CO-25-2722 `
    --matter-config C:\Evidence\CO-25-2722\config\matter_CO-25-2722.json `
    --model small.en `
    --device auto
```

Options:

- `--model` — `tiny.en`, `base.en`, `small.en`, `medium.en`, `large-v3`
- `--device cuda` — use GPU (needs NVIDIA CUDA; 10-20x faster)
- `--ocr` — OCR burnt-in timestamps on keyframes (needs tesseract)
- `--no-resume` — reprocess files already done
- `--docs-only` / `--videos-only` — process only one class

The batch:

1. Extracts text from every PDF / DOCX / XLSX / TXT into
   `output\documents\` and builds `sworn\corpus.txt`
2. Runs the full 11-stage pipeline on every MP4 / MOV / WAV / MP3
3. Uses the corpus as the contradictions source (so officer notes and
   statements are cross-referenced against what they actually said on BWC)
4. Writes `output\MATTER_INDEX.md` with severity-ranked highlights,
   aggregate counts, and links to per-exhibit master reports

## 6a. (Optional) Pull exhibits from OneDrive links

If the exhibits are OneDrive / 1drv.ms share links rather than files on disk,
download and process them in one command instead of steps 4-6:

```powershell
.\run_links.ps1 -MatterRoot C:\Evidence\CO-25-2722 `
    "https://1drv.ms/v/c/...." "https://1drv.ms/v/c/...."
```

Links must be shared as "Anyone with the link can view"; a sign-in-only link
reports 401/403, in which case download it manually into `source\` and use the
normal step 6. See `ONEDRIVE_LINKS.md` for detail.

## 7. Review

Start here:

```
C:\Evidence\CO-25-2722\output\MATTER_INDEX.md
```

Drill down into individual `*.master_report.md` files for per-exhibit
detail. Every CSV has a `human_verified` column — sign off each row in
Excel or a text editor before using any finding.

## 8. Re-running after new disclosure

Drop new files into `source\` and rerun the command in step 6. The batch
skips files already processed (by checking for the master report).

## Troubleshooting

- **"ffmpeg not found"**: reopen PowerShell after winget install, or
  manually add `C:\Program Files\ffmpeg\bin` to PATH.
- **Out of memory on large-v3**: drop to `medium.en` or `small.en`.
- **GPU not detected**: install NVIDIA CUDA 12 + cuDNN matching your card.
  Without GPU, stay on CPU — it just takes longer.
- **One file crashes the pipeline**: it shouldn't. The batch logs the error
  and continues. Check the processing log in `MATTER_INDEX.md`.
