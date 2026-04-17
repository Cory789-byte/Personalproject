"""Ensure external tools (ffmpeg, ffprobe, tesseract) are discoverable.

On Windows, `winget` installs tools but the user's shell may not have the
winget Links directory on PATH - this is particularly common in git-bash
and other non-PowerShell environments. This module augments os.environ
with a set of known install locations so shutil.which() can find them.

Call `ensure_tools_on_path()` at module import time in any script that
shells out to ffmpeg / ffprobe / tesseract.
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path


def _candidate_dirs() -> list[Path]:
    dirs: list[Path] = []
    if sys.platform == "win32":
        home = Path(os.environ.get("USERPROFILE") or os.path.expanduser("~"))
        program_files = Path(os.environ.get("ProgramFiles", r"C:\Program Files"))
        program_files_x86 = Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"))
        local_app = Path(os.environ.get("LOCALAPPDATA", home / "AppData/Local"))

        dirs += [
            local_app / "Microsoft" / "WinGet" / "Links",
            program_files / "ffmpeg" / "bin",
            program_files_x86 / "ffmpeg" / "bin",
            program_files / "Tesseract-OCR",
            program_files_x86 / "Tesseract-OCR",
        ]
        # All winget package install roots for ffmpeg
        winget_pkgs = local_app / "Microsoft" / "WinGet" / "Packages"
        if winget_pkgs.is_dir():
            for sub in winget_pkgs.glob("Gyan.FFmpeg*"):
                for bin_dir in sub.rglob("bin"):
                    dirs.append(bin_dir)
            for sub in winget_pkgs.glob("UB-Mannheim.TesseractOCR*"):
                dirs.append(sub)
    else:
        dirs += [
            Path("/usr/bin"),
            Path("/usr/local/bin"),
            Path("/opt/homebrew/bin"),
            Path("/snap/bin"),
        ]
    return [d for d in dirs if d.is_dir()]


def ensure_tools_on_path() -> None:
    sep = os.pathsep
    current = os.environ.get("PATH", "")
    existing = {p for p in current.split(sep) if p}
    added: list[str] = []
    for d in _candidate_dirs():
        s = str(d)
        if s not in existing:
            added.append(s)
            existing.add(s)
    if added:
        os.environ["PATH"] = current + (sep if current else "") + sep.join(added)


def locate(tool: str) -> str | None:
    """Return the absolute path of a tool, augmenting PATH first if needed."""
    found = shutil.which(tool)
    if found:
        return found
    ensure_tools_on_path()
    return shutil.which(tool)


ensure_tools_on_path()
