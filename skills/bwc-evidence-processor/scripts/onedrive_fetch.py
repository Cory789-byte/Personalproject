"""Download OneDrive / 1drv.ms share links to a local directory.

Used to pull BWC exhibits that were disclosed as OneDrive share links straight
into a matter's ``source/`` folder so the rest of the pipeline (which only
takes local paths) can process them.

How it works
------------
Microsoft exposes an anonymous "shares" API for consumer OneDrive links that
are shared as *"Anyone with the link can view"*::

    GET https://api.onedrive.com/v1.0/shares/u!<base64url(shareUrl)>/root/content

The share URL is base64url-encoded, ``=`` padding stripped, and prefixed with
``u!``. ``/root`` returns metadata (filename, size); ``/root/content`` 302s to
the actual byte stream with a ``Content-Disposition`` filename.

Limitations (important)
-----------------------
This only works for links shared anonymously. A link restricted to specific
people / sign-in returns 401/403 and CANNOT be fetched without that account's
credentials. In that case this raises :class:`PrivateShareError` with a clear
instruction: either change the link to "Anyone with the link can view" and
re-run, or download the file manually into ``<matter>/source/``.

stdlib-only on purpose so it runs in the bare venv with no extra installs.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

SHARE_API = "https://api.onedrive.com/v1.0/shares/{token}"
_UA = "Mozilla/5.0 (bwc-evidence-processor onedrive_fetch)"
_CHUNK = 1 << 20  # 1 MiB
_ONEDRIVE_HOST_RE = re.compile(
    r"https?://(?:[\w-]+\.)?(?:1drv\.ms|onedrive\.live\.com|"
    r"[\w-]+\.sharepoint\.com|photos\.onedrive\.com)/",
    re.IGNORECASE,
)


class OneDriveFetchError(RuntimeError):
    """Base class for fetch failures."""


class PrivateShareError(OneDriveFetchError):
    """The share is not anonymously accessible (needs sign-in)."""


def is_onedrive_url(value: str) -> bool:
    """True if ``value`` looks like a OneDrive / 1drv.ms / SharePoint share link."""
    return bool(_ONEDRIVE_HOST_RE.match(value.strip()))


def share_token(url: str) -> str:
    """Encode a share URL into the ``u!`` token the shares API expects."""
    b64 = base64.urlsafe_b64encode(url.strip().encode("utf-8")).decode("ascii")
    return "u!" + b64.rstrip("=")


def _open(url: str, timeout: float):
    req = urllib.request.Request(url, headers={"User-Agent": _UA, "Accept": "*/*"})
    return urllib.request.urlopen(req, timeout=timeout)


def _filename_from_disposition(disp: str | None) -> str | None:
    if not disp:
        return None
    # RFC 5987 filename*=UTF-8''... first, then plain filename="..."
    m = re.search(r"filename\*=(?:UTF-8'')?([^;]+)", disp, re.IGNORECASE)
    if m:
        return urllib.request.unquote(m.group(1).strip().strip('"'))
    m = re.search(r'filename="?([^";]+)"?', disp, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None


def _safe_name(name: str) -> str:
    name = name.strip().replace("\\", "_").replace("/", "_")
    name = re.sub(r'[<>:"|?*\x00-\x1f]', "_", name)
    return name or "onedrive_download"


def probe_metadata(url: str, timeout: float = 30.0) -> dict:
    """Return the share item's metadata (``name``, ``size`` ...).

    Raises :class:`PrivateShareError` on 401/403, :class:`OneDriveFetchError`
    on other HTTP errors.
    """
    meta_url = SHARE_API.format(token=share_token(url)) + "/root"
    try:
        with _open(meta_url, timeout) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            raise PrivateShareError(_private_msg(url)) from e
        raise OneDriveFetchError(
            f"OneDrive metadata request failed ({e.code} {e.reason}) for {url}"
        ) from e


def _private_msg(url: str) -> str:
    return (
        "This OneDrive share is not anonymously accessible (got 401/403):\n"
        f"  {url}\n"
        "Fix one of these, then re-run:\n"
        "  1. In OneDrive, set the link to 'Anyone with the link can view',\n"
        "     copy the NEW link, and pass that instead; OR\n"
        "  2. Open the link in your browser, click Download, and drop the file\n"
        "     directly into  <matter>\\source\\  then run run_all.ps1."
    )


def fetch(url: str, dest_dir: str | Path, *, timeout: float = 120.0,
          overwrite: bool = False) -> Path:
    """Download a OneDrive share ``url`` into ``dest_dir``; return the file path.

    Skips the download if a same-named file already exists (unless
    ``overwrite``). Raises :class:`PrivateShareError` for sign-in-only links.
    """
    if not is_onedrive_url(url):
        raise OneDriveFetchError(f"Not a OneDrive / 1drv.ms share link: {url}")

    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Resolve a filename up front (cheap metadata call) so resume works.
    name: str | None = None
    try:
        name = _safe_name(probe_metadata(url, timeout=min(timeout, 30.0)).get("name") or "")
    except PrivateShareError:
        raise
    except OneDriveFetchError:
        name = None  # fall back to Content-Disposition below

    if name:
        final = dest_dir / name
        if final.exists() and not overwrite:
            print(f"  already present, skipping: {final.name}")
            return final

    content_url = SHARE_API.format(token=share_token(url)) + "/root/content"
    try:
        resp = _open(content_url, timeout)
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            raise PrivateShareError(_private_msg(url)) from e
        raise OneDriveFetchError(
            f"OneDrive content request failed ({e.code} {e.reason}) for {url}"
        ) from e

    with resp:
        ctype = (resp.headers.get("Content-Type") or "").lower()
        disp_name = _filename_from_disposition(resp.headers.get("Content-Disposition"))
        if disp_name:
            name = _safe_name(disp_name)
        if not name:
            name = _safe_name(Path(resp.geturl().split("?", 1)[0]).name) or "onedrive_download"
        final = dest_dir / name

        # An HTML response means we hit a sign-in / error page, not the file.
        if "text/html" in ctype:
            raise PrivateShareError(_private_msg(url))

        if final.exists() and not overwrite:
            print(f"  already present, skipping: {final.name}")
            return final

        tmp = final.with_suffix(final.suffix + ".part")
        total = resp.headers.get("Content-Length")
        total_i = int(total) if total and total.isdigit() else 0
        written = 0
        with tmp.open("wb") as fh:
            while True:
                chunk = resp.read(_CHUNK)
                if not chunk:
                    break
                fh.write(chunk)
                written += len(chunk)
                if total_i:
                    pct = written * 100 // total_i
                    print(f"\r  downloading {name}: {pct:3d}% "
                          f"({written >> 20} / {total_i >> 20} MiB)", end="", flush=True)
        if total_i:
            print()

    if written == 0:
        tmp.unlink(missing_ok=True)
        raise OneDriveFetchError(f"Downloaded 0 bytes from {url}")
    tmp.replace(final)
    print(f"  saved: {final}  ({written >> 20} MiB)")
    return final


def fetch_many(urls: list[str], dest_dir: str | Path, *, timeout: float = 120.0,
               overwrite: bool = False) -> tuple[list[Path], list[tuple[str, str]]]:
    """Fetch each URL; return (downloaded_paths, [(url, error_message), ...])."""
    ok: list[Path] = []
    failed: list[tuple[str, str]] = []
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] {url}")
        try:
            ok.append(fetch(url, dest_dir, timeout=timeout, overwrite=overwrite))
        except OneDriveFetchError as e:
            print(f"  FAILED: {e}", file=sys.stderr)
            failed.append((url, str(e)))
    return ok, failed


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Download OneDrive / 1drv.ms share links into a folder "
                    "(anonymously-shared links only).")
    ap.add_argument("urls", nargs="+", help="OneDrive / 1drv.ms share link(s)")
    ap.add_argument("--dest", required=True, help="Destination directory")
    ap.add_argument("--timeout", type=float, default=120.0)
    ap.add_argument("--overwrite", action="store_true",
                    help="Re-download even if a same-named file exists")
    args = ap.parse_args()

    ok, failed = fetch_many(args.urls, args.dest,
                            timeout=args.timeout, overwrite=args.overwrite)
    print(f"\n== Downloaded {len(ok)} file(s) to {args.dest}")
    if failed:
        print(f"== {len(failed)} link(s) could not be fetched:", file=sys.stderr)
        for url, _ in failed:
            print(f"   - {url}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
