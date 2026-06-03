#!/usr/bin/env python3
"""
Fetch files from a *personal* Microsoft OneDrive (e.g. coryshepherd1@hotmail.com)
via the Microsoft Graph API, using MSAL device-code auth (no client secret needed).

Personal Microsoft accounts (outlook.com / hotmail.com / live.com) authenticate
against the "consumers" authority. This script is built for that case.

Setup (one-off):
  1. Create a free Azure app registration — see README.md in this folder.
  2. Put its Application (client) ID in env var ONEDRIVE_CLIENT_ID
     (or pass --client-id).
  3. pip install -r requirements.txt

Usage:
  python onedrive_fetch.py whoami
  python onedrive_fetch.py ls "/"                 # list a folder by path
  python onedrive_fetch.py ls "/Documents/Shepherd command hub"
  python onedrive_fetch.py tree "/Documents" --depth 3
  python onedrive_fetch.py search "lease"          # full-text/name search
  python onedrive_fetch.py download "/Documents/foo.docx" ./out/
  python onedrive_fetch.py download-id <itemId> ./out/

The first command opens a device-code prompt: go to the URL it prints, sign in as
coryshepherd1@hotmail.com, and the token is cached to ~/.onedrive_token_cache.json
so later runs are non-interactive until it expires.
"""
from __future__ import annotations

import argparse
import os
import sys
import json
import time
from pathlib import Path
from urllib.parse import quote

try:
    import msal
    import requests
except ImportError:
    sys.exit("Missing deps. Run:  pip install -r onedrive_tools/requirements.txt")

GRAPH = "https://graph.microsoft.com/v1.0"
# "consumers" = personal MS accounts only. Use "common" if you also need work accounts.
AUTHORITY = os.environ.get(
    "ONEDRIVE_AUTHORITY", "https://login.microsoftonline.com/consumers"
)
# Delegated, least-privilege scopes. offline_access/openid/profile are added by MSAL.
SCOPES = ["Files.Read", "Files.Read.All", "User.Read"]
CACHE_PATH = Path(os.environ.get(
    "ONEDRIVE_TOKEN_CACHE", str(Path.home() / ".onedrive_token_cache.json")
))


# --------------------------------------------------------------------------- auth
def _load_cache() -> "msal.SerializableTokenCache":
    cache = msal.SerializableTokenCache()
    if CACHE_PATH.exists():
        cache.deserialize(CACHE_PATH.read_text())
    return cache


def _save_cache(cache: "msal.SerializableTokenCache") -> None:
    if cache.has_state_changed:
        CACHE_PATH.write_text(cache.serialize())
        try:
            os.chmod(CACHE_PATH, 0o600)
        except OSError:
            pass


def get_token(client_id: str) -> str:
    cache = _load_cache()
    app = msal.PublicClientApplication(
        client_id, authority=AUTHORITY, token_cache=cache
    )
    result = None
    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
    if not result:
        flow = app.initiate_device_flow(scopes=SCOPES)
        if "user_code" not in flow:
            raise RuntimeError(f"Failed to start device flow: {json.dumps(flow)}")
        print("\n" + flow["message"] + "\n", file=sys.stderr)
        result = app.acquire_token_by_device_flow(flow)  # blocks until you sign in
    _save_cache(cache)
    if "access_token" not in result:
        raise RuntimeError(
            f"Auth failed: {result.get('error')}: {result.get('error_description')}"
        )
    return result["access_token"]


# -------------------------------------------------------------------------- graph
class Graph:
    def __init__(self, token: str):
        self.s = requests.Session()
        self.s.headers["Authorization"] = f"Bearer {token}"

    def get(self, url: str, **kw) -> requests.Response:
        if url.startswith("/"):
            url = GRAPH + url
        for attempt in range(5):
            r = self.s.get(url, **kw)
            if r.status_code == 429:  # throttled
                wait = int(r.headers.get("Retry-After", 2 ** attempt))
                time.sleep(wait)
                continue
            r.raise_for_status()
            return r
        r.raise_for_status()
        return r

    def paged(self, url: str):
        """Yield items across @odata.nextLink pages."""
        while url:
            data = self.get(url).json()
            for item in data.get("value", []):
                yield item
            url = data.get("@odata.nextLink")


def _path_url(path: str, suffix: str = "") -> str:
    """Build a Graph drive-item URL addressed by path."""
    path = path.strip()
    if path in ("", "/"):
        return f"/me/drive/root{(':/' + suffix) if suffix else ''}" if suffix \
            else "/me/drive/root"
    p = quote(path.strip("/"))
    base = f"/me/drive/root:/{p}"
    return f"{base}:{suffix}" if suffix else base


def _fmt(item: dict) -> str:
    kind = "DIR " if "folder" in item else "FILE"
    size = item.get("size", 0)
    return f"{kind} {size:>12,}  {item.get('name','')}  [{item.get('id','')}]"


# ------------------------------------------------------------------------ actions
def cmd_whoami(g: Graph, _):
    me = g.get("/me").json()
    drive = g.get("/me/drive").json()
    print(f"User : {me.get('displayName')} <{me.get('userPrincipalName', me.get('mail'))}>")
    q = drive.get("quota", {})
    print(f"Drive: {drive.get('id')}  type={drive.get('driveType')}")
    print(f"Quota: used {q.get('used',0):,} / {q.get('total',0):,} bytes")


def cmd_ls(g: Graph, a):
    url = _path_url(a.path, "/children")
    for item in g.paged(url):
        print(_fmt(item))


def cmd_tree(g: Graph, a):
    def walk(path: str, depth: int):
        for item in g.paged(_path_url(path, "/children")):
            indent = "  " * (a.depth - depth)
            print(f"{indent}{_fmt(item)}")
            if "folder" in item and depth > 1:
                walk(path.rstrip("/") + "/" + item["name"], depth - 1)
    walk(a.path, a.depth)


def cmd_search(g: Graph, a):
    url = f"/me/drive/root/search(q='{quote(a.query)}')"
    n = 0
    for item in g.paged(url):
        par = item.get("parentReference", {}).get("path", "")
        print(f"{_fmt(item)}  @ {par}")
        n += 1
    print(f"\n{n} result(s).", file=sys.stderr)


def _download(g: Graph, item_url: str, outdir: Path):
    meta = g.get(item_url).json()
    name = meta.get("name", meta.get("id"))
    outdir.mkdir(parents=True, exist_ok=True)
    dest = outdir / name
    with g.get(item_url + "/content", stream=True) as r:
        with open(dest, "wb") as fh:
            for chunk in r.iter_content(chunk_size=1 << 20):
                fh.write(chunk)
    print(f"Saved {dest}  ({dest.stat().st_size:,} bytes)")


def cmd_download(g: Graph, a):
    _download(g, _path_url(a.path), Path(a.outdir))


def cmd_download_id(g: Graph, a):
    _download(g, f"/me/drive/items/{a.item_id}", Path(a.outdir))


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--client-id", default=os.environ.get("ONEDRIVE_CLIENT_ID", ""),
                    help="Azure app (client) ID; or set ONEDRIVE_CLIENT_ID")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("whoami").set_defaults(func=cmd_whoami)

    p = sub.add_parser("ls"); p.add_argument("path", nargs="?", default="/")
    p.set_defaults(func=cmd_ls)

    p = sub.add_parser("tree"); p.add_argument("path", nargs="?", default="/")
    p.add_argument("--depth", type=int, default=2); p.set_defaults(func=cmd_tree)

    p = sub.add_parser("search"); p.add_argument("query")
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("download"); p.add_argument("path")
    p.add_argument("outdir", nargs="?", default="."); p.set_defaults(func=cmd_download)

    p = sub.add_parser("download-id"); p.add_argument("item_id")
    p.add_argument("outdir", nargs="?", default="."); p.set_defaults(func=cmd_download_id)

    a = ap.parse_args()
    if not a.client_id:
        sys.exit("No client id. Register an Azure app (see README.md) and set "
                 "ONEDRIVE_CLIENT_ID or pass --client-id.")
    g = Graph(get_token(a.client_id))
    a.func(g, a)


if __name__ == "__main__":
    main()
