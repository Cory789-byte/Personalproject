"""Smoke tests for _path_helper (no external tools required)."""

from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from _path_helper import ensure_tools_on_path, locate  # noqa: E402


class PathHelperTests(unittest.TestCase):
    def test_ensure_tools_on_path_idempotent(self):
        before = os.environ.get("PATH", "")
        ensure_tools_on_path()
        after = os.environ.get("PATH", "")
        # Should not duplicate entries
        parts = after.split(os.pathsep)
        self.assertEqual(len(parts), len(set(parts)))
        # Must not shrink the path
        self.assertGreaterEqual(len(after), len(before))

    def test_locate_returns_none_for_garbage(self):
        self.assertIsNone(locate("definitely-not-a-real-binary-xyz123"))


if __name__ == "__main__":
    unittest.main()
