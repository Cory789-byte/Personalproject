# Processing OneDrive / 1drv.ms exhibit links

The pipeline works on **local files**. This helper pulls exhibits that were
disclosed (or stored) as OneDrive share links into a matter's `source\` folder
so the full GPU pipeline can run on them.

## One command (Windows GPU box)

```powershell
cd C:\Evidence\skill-repo\skills\bwc-evidence-processor
.\run_links.ps1 -MatterRoot C:\Evidence\001_SIBLEY `
    "https://1drv.ms/v/c/...firstlink..." `
    "https://1drv.ms/v/c/...secondlink..."
```

What it does:

1. Activates the venv.
2. Downloads each link into `C:\Evidence\001_SIBLEY\source\`
   (already-downloaded files of the same name are skipped — safe to re-run).
3. Hands off to `run_all.ps1`: CUDA probe → picks `small.en`/`base.en` on the
   GPU (or CPU fallback) → `batch_process.py` (all 11 stages per file) →
   Google Drive sync of the reports.

Switches mirror `run_all.ps1`: `-NoGpu`, `-NoSync`, `-NoResume`,
`-DriveFolder <path>`, plus `-Overwrite` to force re-download.

## Download only (any platform)

```bash
python scripts/onedrive_fetch.py --dest /path/to/matter/source URL [URL ...]
```

Then run the normal batch (`batch_process.py` / `run_all.ps1`) over the matter.

## The sharing-permission requirement (important)

Only links shared as **"Anyone with the link can view"** can be downloaded
unattended. A link restricted to specific people or your sign-in returns
**401 / 403**, and there is no way to fetch it without that account's
credentials.

When that happens the tool prints exactly what to do. Pick one:

- **Re-share anonymously** — in OneDrive: *Share → Anyone with the link can
  view → Copy link*, then pass the **new** link and re-run; or
- **Download manually** — open the link in your browser, click **Download**,
  drop the file into `<MatterRoot>\source\`, then run `.\run_all.ps1
  -MatterRoot <MatterRoot>` directly (no link step needed).

Either way the rest of the pipeline is identical.

## Why not just download it for you from the cloud?

These links are personal-OneDrive shares tied to your Microsoft account. A
Claude Code **web/cloud session runs in an isolated container with no access to
your machine, your GPU, or your OneDrive sign-in**, so it cannot fetch a
sign-in-only link or drive your GPU. The download + GPU run must happen on the
box that holds the matter (e.g. "001 sibley"). This helper makes that a single
command there.
