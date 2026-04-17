"""Diagnose whether faster-whisper can actually use CUDA on this system.

Prints a clear verdict + remediation hints. Exits 0 if CUDA works, 1 if not.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import traceback
from pathlib import Path


def _line(s: str) -> None:
    print(s, flush=True)


def probe() -> int:
    _line("== CUDA / faster-whisper probe ==")

    # 1. NVIDIA driver via nvidia-smi
    smi = shutil.which("nvidia-smi")
    if not smi:
        _line("FAIL: nvidia-smi not found on PATH - no NVIDIA driver visible.")
        _line("      Install the latest NVIDIA driver from nvidia.com/drivers")
        return 1
    try:
        out = subprocess.run([smi], capture_output=True, text=True, timeout=10)
        _line("nvidia-smi detected. First lines:")
        for line in out.stdout.splitlines()[:12]:
            _line(f"  {line}")
    except Exception as e:
        _line(f"FAIL: nvidia-smi errored: {e}")
        return 1

    # 2. ctranslate2 CUDA support
    try:
        import ctranslate2  # type: ignore
    except Exception as e:
        _line(f"FAIL: cannot import ctranslate2: {e}")
        _line("      Run: pip install -r requirements.txt")
        return 1

    supported = []
    try:
        supported = ctranslate2.get_supported_compute_types("cuda")
    except Exception as e:
        _line(f"FAIL: ctranslate2.get_supported_compute_types('cuda') raised: {e}")
        _line("      Install cuBLAS / cuDNN DLLs via: "
              "`pip install nvidia-cublas-cu12 nvidia-cudnn-cu9`")
        _line("      Or install the NVIDIA CUDA Toolkit 12.x + cuDNN 9 manually.")
        return 1

    _line(f"ctranslate2 CUDA compute types supported: {supported}")
    if not supported:
        _line("FAIL: ctranslate2 built without CUDA.")
        return 1

    # 3. Try loading a tiny Whisper model on CUDA
    try:
        from faster_whisper import WhisperModel  # type: ignore
    except Exception as e:
        _line(f"FAIL: cannot import faster_whisper: {e}")
        return 1

    _line("Attempting to load faster-whisper tiny.en on CUDA...")
    try:
        model = WhisperModel("tiny.en", device="cuda", compute_type="int8")
        del model
        _line("PASS: tiny.en loaded on CUDA successfully.")
    except Exception:
        _line("FAIL: WhisperModel('tiny.en', device='cuda') raised:")
        traceback.print_exc()
        _line("")
        _line("Common fixes:")
        _line("  1. pip install nvidia-cublas-cu12 nvidia-cudnn-cu9")
        _line("  2. Update NVIDIA driver to the latest")
        _line("  3. Install CUDA Toolkit 12.x and cuDNN 9 if pip packages fail")
        return 1

    # 4. Estimate VRAM headroom for small.en
    try:
        smi_out = subprocess.run(
            [smi, "--query-gpu=memory.total,memory.free,name",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=10
        )
        for row in smi_out.stdout.strip().splitlines():
            total_mb, free_mb, name = [x.strip() for x in row.split(",", 2)]
            _line(f"GPU: {name}  total {total_mb} MiB, free {free_mb} MiB")
            free = int(free_mb)
            if free < 800:
                _line("  WARN: < 800 MiB free. small.en may not fit; try tiny.en/base.en.")
            elif free < 1500:
                _line("  OK for small.en (int8). Leave no parallel GPU workers - "
                      "this card only fits one Whisper instance.")
            else:
                _line("  Plenty of room for small.en. medium.en may fit at int8.")
    except Exception:
        pass

    _line("")
    _line("VERDICT: GPU path is usable. Recommended batch args:")
    _line("  --device cuda --gpu-workers 1 --cpu-workers 1 --model small.en")
    return 0


if __name__ == "__main__":
    raise SystemExit(probe())
