# Auto-pilot: probe GPU, pick best settings, run the batch, sync to Google Drive.
#
# Usage from PowerShell (at your PC, or via RDP from a phone):
#
#     cd C:\Evidence\skill-repo\skills\bwc-evidence-processor
#     .\run_all.ps1
#
# Optional switches:
#     .\run_all.ps1 -MatterRoot C:\Evidence\CO-25-2722
#     .\run_all.ps1 -NoGpu          # force CPU only
#     .\run_all.ps1 -DriveFolder "C:\Users\User\My Drive\SHEPHERD_v_QPS_MASTER_CASE_FILE"
#     .\run_all.ps1 -NoSync         # skip Google Drive copy
#
# The script picks small.en on GPU if VRAM >= 800 MiB, base.en on GPU if
# 400 - 800 MiB, or falls back to CPU-only with 4 workers otherwise.
# It runs the batch, then syncs every report + CSV to your Drive folder
# in a timestamped subdirectory.

param(
    [string]$MatterRoot = "C:\Evidence\CO-25-2722",
    [string]$DriveFolder = "C:\Users\User\My Drive\SHEPHERD_v_QPS_MASTER_CASE_FILE",
    [switch]$NoGpu = $false,
    [switch]$NoSync = $false,
    [switch]$Screenshots = $true,
    [switch]$NoResume = $false
)

$ErrorActionPreference = "Continue"
$SkillRoot = Split-Path -Parent $PSCommandPath

Write-Host ""
Write-Host "===== BWC Evidence Processor - Auto Pilot =====" -ForegroundColor Cyan
Write-Host "Matter: $MatterRoot"
Write-Host "Skill:  $SkillRoot"
Write-Host ""

# -- Activate venv --
$Activate = Join-Path $SkillRoot ".venv\Scripts\Activate.ps1"
if (-not (Test-Path $Activate)) {
    Write-Error "venv not found at $Activate - run pip install first"
    exit 1
}
& $Activate

# -- Pull latest skill code --
Write-Host "--- git pull ---" -ForegroundColor Yellow
Push-Location $SkillRoot
git pull 2>&1 | Out-Host
Pop-Location

# -- Decide GPU / CPU settings --
$GpuWorkers = 0
$CpuWorkers = 2
$Model = "small.en"

if (-not $NoGpu) {
    Write-Host "--- CUDA probe ---" -ForegroundColor Yellow
    $ProbeOutput = python "$SkillRoot\scripts\cuda_probe.py" 2>&1 | Out-String
    Write-Host $ProbeOutput

    $Usable = $ProbeOutput -match "VERDICT: GPU path is usable"
    $FreeMatch = [regex]::Match($ProbeOutput, "free\s+(\d+)\s+MiB")
    $FreeVram = if ($FreeMatch.Success) { [int]$FreeMatch.Groups[1].Value } else { 0 }

    if ($Usable -and $FreeVram -ge 800) {
        Write-Host "Decision: GPU usable with $FreeVram MiB free - small.en on GPU + 2 CPU workers" -ForegroundColor Green
        $GpuWorkers = 1
        $CpuWorkers = 2
        $Model = "small.en"
    } elseif ($Usable -and $FreeVram -ge 400) {
        Write-Host "Decision: tight VRAM ($FreeVram MiB) - base.en on GPU + 2 CPU workers" -ForegroundColor Yellow
        $GpuWorkers = 1
        $CpuWorkers = 2
        $Model = "base.en"
    } else {
        Write-Host "Decision: GPU not usable or VRAM too low - CPU only with 4 workers" -ForegroundColor Yellow
        $GpuWorkers = 0
        $CpuWorkers = 4
        $Model = "small.en"
    }
} else {
    Write-Host "Decision: -NoGpu set - CPU only with 4 workers" -ForegroundColor Yellow
    $CpuWorkers = 4
}

# -- Kick off the batch --
Write-Host ""
Write-Host "--- batch_process ---" -ForegroundColor Yellow
Write-Host "Model=$Model  GPU=$GpuWorkers  CPU=$CpuWorkers  Screenshots=$Screenshots"
Write-Host ""

$BatchArgs = @(
    "$SkillRoot\scripts\batch_process.py",
    "--matter-root", $MatterRoot,
    "--videos-only",
    "--model", $Model,
    "--gpu-workers", $GpuWorkers.ToString(),
    "--cpu-workers", $CpuWorkers.ToString()
)
if ($Screenshots) { $BatchArgs += "--screenshots" }
if ($NoResume)    { $BatchArgs += "--no-resume" }

$Start = Get-Date
python @BatchArgs
$Elapsed = (Get-Date) - $Start
Write-Host ""
Write-Host "Batch finished in $($Elapsed.ToString('hh\:mm\:ss'))" -ForegroundColor Green

# -- Mobile summary --
Write-Host "--- mobile summary ---" -ForegroundColor Yellow
python "$SkillRoot\scripts\mobile_summary.py" --matter-root $MatterRoot

# -- Sync to Google Drive --
if (-not $NoSync -and (Test-Path $DriveFolder)) {
    $TS = Get-Date -Format "yyyy-MM-dd_HHmm"
    $Dest = Join-Path $DriveFolder ("bwc_analysis_$TS")
    Write-Host ""
    Write-Host "--- Sync to Google Drive: $Dest ---" -ForegroundColor Yellow
    $Output = Join-Path $MatterRoot "output"
    robocopy $Output $Dest /E /R:2 /W:2 /XF *.wav *.tmp 2>&1 | Out-Host

    # Also overwrite a "latest" copy at the top of the Drive folder
    $Latest = Join-Path $DriveFolder "bwc_analysis_latest"
    robocopy $Output $Latest /E /R:2 /W:2 /XF *.wav *.tmp /MIR 2>&1 | Out-Host
    Write-Host "Drive copy complete. Open Google Drive app on your phone to view." -ForegroundColor Green
} elseif (-not $NoSync) {
    Write-Warning "Drive folder not found: $DriveFolder"
    Write-Warning "Pass -DriveFolder or install Google Drive for desktop."
}

Write-Host ""
Write-Host "===== DONE =====" -ForegroundColor Cyan
Write-Host "On your phone, open Google Drive and look for:"
Write-Host "  <your Drive>/bwc_analysis_latest/MOBILE_SUMMARY.md"
Write-Host "  <your Drive>/bwc_analysis_latest/CASE_THEORY.md"
Write-Host "  <your Drive>/bwc_analysis_latest/TRIANGULATION.md"
Write-Host "  <your Drive>/bwc_analysis_latest/TAMPERING_TALLY.md"
Write-Host ""
