# One-shot: download OneDrive / 1drv.ms exhibit links into a matter, then run
# the full GPU pipeline (probe -> batch -> Google Drive sync) via run_all.ps1.
#
# Usage from PowerShell on your GPU box (e.g. "001 sibley"):
#
#     cd C:\Evidence\skill-repo\skills\bwc-evidence-processor
#     .\run_links.ps1 -MatterRoot C:\Evidence\001_SIBLEY `
#         "https://1drv.ms/v/c/...." "https://1drv.ms/v/c/...."
#
# Or with named links and CPU-only:
#
#     .\run_links.ps1 -MatterRoot C:\Evidence\001_SIBLEY -NoGpu `
#         -Links @("https://1drv.ms/v/c/....","https://1drv.ms/v/c/....")
#
# Notes:
#   * Links must be shared as "Anyone with the link can view". A sign-in-only
#     link will report 401/403 - in that case open it in your browser, click
#     Download, drop the file into <MatterRoot>\source\, and run .\run_all.ps1.
#   * Already-downloaded files (same name) are skipped, so re-running is safe.

param(
    [Parameter(Mandatory = $true)]
    [string]$MatterRoot,

    # Links can be passed either via -Links @(...) or as trailing positional args.
    [string[]]$Links = @(),

    [string]$DriveFolder = "C:\Users\User\My Drive\SHEPHERD_v_QPS_MASTER_CASE_FILE",
    [switch]$NoGpu = $false,
    [switch]$NoSync = $false,
    [switch]$NoResume = $false,
    [switch]$Overwrite = $false,

    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$RemainingLinks = @()
)

$ErrorActionPreference = "Continue"
$SkillRoot = Split-Path -Parent $PSCommandPath

$AllLinks = @()
$AllLinks += $Links
$AllLinks += $RemainingLinks
$AllLinks = $AllLinks | Where-Object { $_ -and $_.Trim() -ne "" }

Write-Host ""
Write-Host "===== BWC Evidence Processor - Links Runner =====" -ForegroundColor Cyan
Write-Host "Matter: $MatterRoot"
Write-Host "Links : $($AllLinks.Count)"
Write-Host ""

if ($AllLinks.Count -eq 0) {
    Write-Error "No links supplied. Pass -Links @('https://1drv.ms/...') or as trailing arguments."
    exit 1
}

# -- Activate venv --
$Activate = Join-Path $SkillRoot ".venv\Scripts\Activate.ps1"
if (-not (Test-Path $Activate)) {
    Write-Error "venv not found at $Activate - run pip install first (see WINDOWS_RUNBOOK.md)."
    exit 1
}
& $Activate

# -- Ensure matter source folder exists --
$Source = Join-Path $MatterRoot "source"
New-Item -ItemType Directory -Force -Path $Source | Out-Null

# -- Download the links into <matter>\source\ --
Write-Host "--- Downloading OneDrive links into $Source ---" -ForegroundColor Yellow
$FetchArgs = @("$SkillRoot\scripts\onedrive_fetch.py", "--dest", $Source)
if ($Overwrite) { $FetchArgs += "--overwrite" }
$FetchArgs += $AllLinks
python @FetchArgs
$FetchExit = $LASTEXITCODE

if ($FetchExit -ne 0) {
    Write-Warning "One or more links could not be downloaded (see messages above)."
    $existing = Get-ChildItem -Path $Source -File -ErrorAction SilentlyContinue
    if (-not $existing) {
        Write-Error "Nothing in $Source to process. Aborting."
        exit 1
    }
    Write-Host "Continuing with the files already in $Source ..." -ForegroundColor Yellow
}

# -- Hand off to the GPU auto-pilot (probe -> batch -> Drive sync) --
Write-Host ""
Write-Host "--- Handing off to run_all.ps1 (GPU pipeline) ---" -ForegroundColor Yellow
$RunAllArgs = @{
    MatterRoot  = $MatterRoot
    DriveFolder = $DriveFolder
}
if ($NoGpu)    { $RunAllArgs["NoGpu"]    = $true }
if ($NoSync)   { $RunAllArgs["NoSync"]   = $true }
if ($NoResume) { $RunAllArgs["NoResume"] = $true }

& (Join-Path $SkillRoot "run_all.ps1") @RunAllArgs
