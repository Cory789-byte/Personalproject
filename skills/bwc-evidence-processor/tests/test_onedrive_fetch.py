"""Tests for onedrive_fetch (no network: urlopen is mocked)."""

from __future__ import annotations

import base64
import io
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import onedrive_fetch as odf  # noqa: E402


class _FakeResp(io.BytesIO):
    """Minimal stand-in for an http.client.HTTPResponse."""

    def __init__(self, data: bytes, headers: dict, url: str = "https://x/file"):
        super().__init__(data)
        self.headers = headers
        self._url = url

    def geturl(self) -> str:
        return self._url

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()
        return False


class TokenTests(unittest.TestCase):
    def test_share_token_format(self):
        url = "https://1drv.ms/v/c/abc/IQfoo"
        tok = odf.share_token(url)
        self.assertTrue(tok.startswith("u!"))
        self.assertNotIn("=", tok)  # padding stripped
        # Round-trips back to the original URL.
        decoded = base64.urlsafe_b64decode(tok[2:] + "===").decode()
        self.assertEqual(decoded, url)

    def test_is_onedrive_url(self):
        self.assertTrue(odf.is_onedrive_url("https://1drv.ms/v/c/abc/IQfoo"))
        self.assertTrue(odf.is_onedrive_url("https://onedrive.live.com/download?cid=1"))
        self.assertTrue(odf.is_onedrive_url("https://contoso.sharepoint.com/x"))
        self.assertFalse(odf.is_onedrive_url("https://example.com/video.mp4"))
        self.assertFalse(odf.is_onedrive_url("/local/path.mp4"))

    def test_filename_from_disposition(self):
        f = odf._filename_from_disposition
        self.assertEqual(f('attachment; filename="bwc 01.mp4"'), "bwc 01.mp4")
        self.assertEqual(f("attachment; filename*=UTF-8''bwc%2001.mp4"), "bwc 01.mp4")
        self.assertIsNone(f(None))

    def test_safe_name_strips_separators(self):
        self.assertEqual(odf._safe_name("a/b\\c.mp4"), "a_b_c.mp4")
        self.assertTrue(odf._safe_name("") == "onedrive_download")


class FetchTests(unittest.TestCase):
    def test_private_share_raises(self):
        err = urllib.error.HTTPError("u", 403, "Forbidden", {}, None)
        with mock.patch.object(odf.urllib.request, "urlopen", side_effect=err):
            with self.assertRaises(odf.PrivateShareError):
                odf.fetch("https://1drv.ms/v/c/abc/IQfoo", "/tmp/nope_dir_x")

    def test_rejects_non_onedrive_url(self):
        with self.assertRaises(odf.OneDriveFetchError):
            odf.fetch("https://example.com/x.mp4", "/tmp/nope_dir_x")

    def test_successful_download(self):
        body = b"\x00\x01video-bytes\x02\x03" * 10

        def fake_urlopen(req, timeout=0):
            url = req.full_url
            if url.endswith("/root"):
                meta = b'{"name": "interview 01.mp4", "size": 180}'
                return _FakeResp(meta, {"Content-Type": "application/json"})
            return _FakeResp(
                body,
                {"Content-Type": "video/mp4",
                 "Content-Length": str(len(body)),
                 "Content-Disposition": 'attachment; filename="interview 01.mp4"'},
            )

        with mock.patch.object(odf.urllib.request, "urlopen", side_effect=fake_urlopen):
            import tempfile
            with tempfile.TemporaryDirectory() as d:
                out = odf.fetch("https://1drv.ms/v/c/abc/IQfoo", d)
                self.assertEqual(out.name, "interview 01.mp4")
                self.assertEqual(out.read_bytes(), body)
                # No leftover .part file.
                self.assertFalse(out.with_suffix(out.suffix + ".part").exists())

    def test_html_response_treated_as_private(self):
        def fake_urlopen(req, timeout=0):
            if req.full_url.endswith("/root"):
                raise urllib.error.HTTPError("u", 404, "NF", {}, None)
            return _FakeResp(b"<html>sign in</html>",
                             {"Content-Type": "text/html; charset=utf-8"})

        with mock.patch.object(odf.urllib.request, "urlopen", side_effect=fake_urlopen):
            import tempfile
            with tempfile.TemporaryDirectory() as d:
                with self.assertRaises(odf.PrivateShareError):
                    odf.fetch("https://1drv.ms/v/c/abc/IQfoo", d)

    def test_fetch_many_collects_failures(self):
        def fake_urlopen(req, timeout=0):
            raise urllib.error.HTTPError("u", 403, "Forbidden", {}, None)

        with mock.patch.object(odf.urllib.request, "urlopen", side_effect=fake_urlopen):
            ok, failed = odf.fetch_many(
                ["https://1drv.ms/v/c/abc/IQa", "https://1drv.ms/v/c/abc/IQb"], "/tmp/x")
            self.assertEqual(ok, [])
            self.assertEqual(len(failed), 2)


if __name__ == "__main__":
    unittest.main()
