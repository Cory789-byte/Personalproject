"""Smoke test for the case theory synthesizer."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from case_theory import render  # noqa: E402


COMPLIANCE_CSV = """# MACHINE-GENERATED - UNVERIFIED
row,category,severity,start,end,timestamp_hms,utterance,detail,human_verified
1,missing_caution,high,0,30,00:00:00.000,,No caution detected.,
2,possible_inducement,critical,45,50,00:00:45.000,"If you tell me it'll be easier","Inducement risk.",
"""


class CaseTheoryTests(unittest.TestCase):
    def test_render_produces_markdown(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source").mkdir()
            (root / "output").mkdir()
            (root / "output" / "ex1.compliance.csv").write_text(
                COMPLIANCE_CSV, encoding="utf-8"
            )
            dest = render(root)
            text = dest.read_text(encoding="utf-8")
            self.assertIn("MACHINE-GENERATED", text)
            self.assertIn("Critical: 1", text)
            self.assertIn("High: 1", text)
            self.assertIn("possible_inducement", text)
            self.assertIn("missing_caution", text)
            # Cross-ex suggestion present
            self.assertIn("cross-examination", text.lower())


if __name__ == "__main__":
    unittest.main()
