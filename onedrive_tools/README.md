# onedrive_fetch — pull files from a personal OneDrive (hotmail/outlook)

`onedrive_fetch.py` reads/downloads files from a **personal Microsoft account**
OneDrive (e.g. `coryshepherd1@hotmail.com`) via Microsoft Graph, using MSAL
**device-code** sign-in — no client secret, nothing stored except a token cache.

> This is a *different* account from the work OneDrive
> (`coryshepherd@trustandcollectiveco`) that other tooling in this repo talks to.
> That work account does **not** contain the "Shepherd command hub" /
> "001 sibley howdens" / "criminal" folders, which is why this script targets the
> personal account instead.

## 1. Register a free Azure app (one-off, ~3 min)

You need an Application (client) ID. Microsoft Graph requires apps to identify
themselves even for personal accounts; the app itself is free.

1. Go to <https://entra.microsoft.com> → **App registrations** → **New registration**
   (you can sign in with the same hotmail account).
2. **Name**: `onedrive-fetch` (anything).
3. **Supported account types**: choose
   **"Personal Microsoft accounts only"** (or "…and personal Microsoft accounts").
4. **Redirect URI**: leave blank.
5. Register → copy the **Application (client) ID**.
6. **Authentication** → **Advanced settings** → set
   **"Allow public client flows"** = **Yes** → Save.
   (This enables the device-code flow.)
7. **API permissions** → **Add a permission** → **Microsoft Graph** →
   **Delegated** → add `Files.Read`, `Files.Read.All`, `User.Read`,
   `offline_access`. (No admin consent needed for a personal account.)

## 2. Install + configure

```bash
pip install -r onedrive_tools/requirements.txt
export ONEDRIVE_CLIENT_ID="<the Application (client) ID from step 1>"
```

## 3. Use it

```bash
# First call opens a device-code prompt: visit the URL, sign in as
# coryshepherd1@hotmail.com, then it caches the token.
python onedrive_tools/onedrive_fetch.py whoami

# Browse
python onedrive_tools/onedrive_fetch.py ls "/"
python onedrive_tools/onedrive_fetch.py ls "/Documents"
python onedrive_tools/onedrive_fetch.py tree "/Documents" --depth 3

# Find the case folders
python onedrive_tools/onedrive_fetch.py search "sibley"
python onedrive_tools/onedrive_fetch.py search "command hub"
python onedrive_tools/onedrive_fetch.py search "lease"

# Pull files down
python onedrive_tools/onedrive_fetch.py download "/Documents/Shepherd command hub/001 sibley howdens/criminal/somefile.docx" ./pulled/
python onedrive_tools/onedrive_fetch.py download-id 01ABC...XYZ ./pulled/
```

## Notes
- Scopes are **read-only** (`Files.Read*`). Change to `Files.ReadWrite` in the
  script's `SCOPES` if you later need to upload.
- Token cache lives at `~/.onedrive_token_cache.json` (chmod 600). Delete it to
  force a fresh sign-in or to switch accounts.
- To target **both** personal and work accounts, set
  `ONEDRIVE_AUTHORITY=https://login.microsoftonline.com/common`.
- Throttling (HTTP 429) is retried automatically with backoff.

## Why this isn't wired into the running agent session
The agent's connected OneDrive/SharePoint tools are bound to the work tenant.
Pulling the *personal* OneDrive needs its own delegated sign-in, which is exactly
what this script does. Run it locally where you can complete the device-code login;
once files are downloaded you can point the `bwc-evidence-processor` skill at them.
