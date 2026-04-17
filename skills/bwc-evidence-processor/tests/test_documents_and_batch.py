"""Tests for document extraction and batch classification."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from extract_documents import (  # noqa: E402
    append_to_corpus,
    extract_one,
    process_directory,
    save_record,
)
from batch_process import classify, walk  # noqa: E402


class DocumentTests(unittest.TestCase):
    def test_txt_extraction(self):
        with TemporaryDirectory() as tmp:
            src = Path(tmp) / "statement.txt"
            src.write_text("I was at the park at 9pm.\nI did not have a weapon.")
            rec = extract_one(src)
            self.assertEqual(rec.kind, "txt")
            self.assertIn("weapon", rec.text)
            self.assertEqual(len(rec.sha256), 64)

    def test_save_record_and_corpus(self):
        with TemporaryDirectory() as tmp:
            src = Path(tmp) / "s.txt"
            src.write_text("sworn text")
            rec = extract_one(src)
            out = save_record(rec, Path(tmp) / "out")
            corpus = Path(tmp) / "corpus.txt"
            append_to_corpus(rec, corpus)
            payload = json.loads(out.read_text())
            self.assertEqual(payload["header"], "MACHINE-GENERATED - UNVERIFIED")
            self.assertIn("sworn text", corpus.read_text())

    def test_unsupported_extension_skipped_cleanly(self):
        with TemporaryDirectory() as tmp:
            src = Path(tmp) / "thing.xyz"
            src.write_text("x")
            rec = extract_one(src)
            self.assertTrue(any("unsupported" in w for w in rec.warnings))

    def test_process_directory_picks_supported(self):
        with TemporaryDirectory() as tmp:
            src = Path(tmp) / "src"
            src.mkdir()
            (src / "a.txt").write_text("alpha")
            (src / "b.md").write_text("# beta")
            (src / "c.bin").write_bytes(b"\x00\x01")
            sub = src / "sub"
            sub.mkdir()
            (sub / "d.txt").write_text("delta")

            out = Path(tmp) / "out"
            corpus = Path(tmp) / "corpus.txt"
            records = process_directory(src, out, corpus)
            self.assertEqual(len(records), 3)
            self.assertIn("alpha", corpus.read_text())
            self.assertIn("delta", corpus.read_text())


class BatchTests(unittest.TestCase):
    def test_classify(self):
        self.assertEqual(classify(Path("x.mp4")), "video")
        self.assertEqual(classify(Path("x.MP4")), "video")
        self.assertEqual(classify(Path("x.wav")), "audio")
        self.assertEqual(classify(Path("x.pdf")), "document")
        self.assertEqual(classify(Path("x.bin")), "other")

    def test_walk_buckets(self):
        with TemporaryDirectory() as tmp:
            src = Path(tmp)
            (src / "a.mp4").write_bytes(b"0")
            (src / "b.pdf").write_bytes(b"0")
            (src / "c.txt").write_text("t")
            sub = src / "sub"
            sub.mkdir()
            (sub / "d.wav").write_bytes(b"0")
            buckets = walk(src)
            self.assertEqual(len(buckets["video"]), 1)
            self.assertEqual(len(buckets["audio"]), 1)
            self.assertEqual(len(buckets["document"]), 2)


if __name__ == "__main__":
    unittest.main()
