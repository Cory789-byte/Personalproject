# GPU + CPU parallel processing

## Check whether CUDA is usable

```powershell
cd C:\Evidence\skill-repo\skills\bwc-evidence-processor
.\.venv\Scripts\Activate.ps1
python scripts\cuda_probe.py
```

The probe checks: NVIDIA driver, ctranslate2 CUDA support, `faster-whisper`
loading a model on CUDA, and VRAM headroom. It either prints `VERDICT: GPU
path is usable` or tells you the specific install step needed.

## If the probe fails

Most common fix on Windows:

```powershell
pip install nvidia-cublas-cu12 nvidia-cudnn-cu9
```

`cuDNN 9` matches the CUDA 12 cuBLAS wheel above. If pip cannot satisfy both,
install the NVIDIA CUDA Toolkit 12.x from the NVIDIA site and cuDNN 9 matching
that toolkit. Then re-run the probe.

If you have very old drivers (pre 2023), update them first:
<https://www.nvidia.com/drivers>

## Quadro P400 (2 GB VRAM) notes

- 2 GB is tight. Use `--model small.en` or smaller.
- Only **one** GPU worker can fit at once (`--gpu-workers 1`).
- `medium.en` (~1.5 GB) might fit with int8 but leaves almost no headroom.
- If you see `CUDA out of memory`, drop to `--model base.en` or back off to CPU.

## Running the full 18 GB matter at close to real-time

Once the probe passes, the batch supports mixed GPU + CPU workers:

```powershell
python scripts\batch_process.py `
    --matter-root C:\Evidence\CO-25-2722 `
    --videos-only `
    --model small.en `
    --gpu-workers 1 `
    --cpu-workers 2
```

What this does:

1. Sorts videos **largest first**, so the big BWC interviews go to the GPU
   where the speedup is largest.
2. Maintains a queue of worker slots — 1 CUDA + 2 CPU (tune cpu-workers to
   your core count; 2 is usually optimal, 3-4 on 12+ core CPUs).
3. Each file runs through all 11 stages independently.
4. Falls back gracefully: if GPU OOMs on a file, that run errors out and
   continues; re-running resumes on the failed ones only.
5. Refreshes `MATTER_INDEX.md` and `CASE_THEORY.md` at the end.

## Tuning

- More CPU workers is not always better. Whisper already uses multi-threading
  internally. On a 4-core CPU, `--cpu-workers 1` is often fastest; on 8+ core
  CPU, `--cpu-workers 2` is the sweet spot; on 12+ core CPU, try 3.
- If CPU starves the GPU worker (the GPU finishes first and waits), lower
  cpu-workers.
- Watch Task Manager: GPU util should sit 60-95% while transcribing; CPU util
  per worker should be 60-90%.

## Without GPU

```powershell
python scripts\batch_process.py --matter-root C:\Evidence\CO-25-2722 --videos-only --model small.en --cpu-workers 2
```

On 18 GB this runs ~4-6 hours on a modern CPU. With GPU + CPU the same set
drops to ~1.5-2.5 hours.

## How to interrupt and resume

Ctrl-C in the PowerShell window aborts the batch. Run the same command again
and it resumes — any video with a `*.master_report.md` is skipped.
