"""End-to-end pipeline runner: build_database -> validate -> build_html -> export_json."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from legal_system.build import build_database, validate, build_html, export_json  # noqa: E402


def main() -> int:
    print("\n========== 1) BUILD DATABASE ==========")
    rc = build_database.main()
    if rc:
        return rc
    print("\n========== 2) VALIDATE ==========")
    rc = validate.main()
    if rc:
        return rc
    print("\n========== 3) BUILD HTML SITE ==========")
    rc = build_html.main()
    if rc:
        return rc
    print("\n========== 4) EXPORT JSON ==========")
    rc = export_json.main()
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
