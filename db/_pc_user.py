"""Helpers that lean on the user's Windows session instead of asking for creds.

Two things this module gives the loaders:

    pc_user()        -> the Windows username, for the ingested_by audit column.
    onedrive_root()  -> the path Windows already knows when OneDrive is signed
                        in. Falls back to ONEDRIVE_ROOT env var.

Both are pure stdlib so they also work fine on Linux/macOS for testing.
"""

from __future__ import annotations

import getpass
import os
from pathlib import Path


def pc_user() -> str:
    """Return the current OS username — Windows: %USERNAME%, *nix: $USER."""
    return (
        os.environ.get("USERNAME")           # Windows
        or os.environ.get("USER")            # *nix
        or getpass.getuser()                 # last resort
    )


def onedrive_root() -> Path | None:
    """Return the user's OneDrive sync root if Windows knows where it is.

    Windows sets %OneDrive% (and %OneDriveCommercial% / %OneDriveConsumer%)
    automatically once the user signs into OneDrive with their Microsoft
    account — no extra setup. Falls back to ONEDRIVE_ROOT for non-Windows
    or for users who want to override.
    """
    for var in ("ONEDRIVE_ROOT", "OneDriveCommercial", "OneDriveConsumer", "OneDrive"):
        value = os.environ.get(var)
        if value:
            p = Path(value)
            if p.is_dir():
                return p
    return None
