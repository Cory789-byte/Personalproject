"""Per-document defence analysis using the Claude API.

Reads documents from a Drive ingest manifest (from `gdrive_ingest.py`) or a
directory of extracted `.doc.json` records (from `extract_documents.py`),
sends each through Claude Opus 4.7 with the QLD defence framework as a
cached system prompt, and writes one `<drive_id>.analysis.json` per file.

Key engineering choices:

- Prompt caching on the framework (~5K tokens) + a short always-present
  preamble. With 200+ documents, cache reads pay for themselves after the
  second call. The framework is the stable prefix; per-doc content comes
  after the `cache_control` breakpoint.
- Opus 4.7 + adaptive thinking + effort=high — the defence brief is the
  whole point; the skill docs say don't downgrade for cost.
- Structured output via `output_config.format` with a strict JSON schema.
- Images (BWC frames, photos, screenshots) are sent as vision content so
  Claude can see them directly; PDFs/DOCX/XLSX rely on pre-extracted text.
- Typed exceptions, retries, per-file error isolation — one bad document
  doesn't poison the run.
- Every output carries the MACHINE-GENERATED - UNVERIFIED header.

Run:
    export ANTHROPIC_API_KEY=sk-ant-...
    python scripts/defence_analysis.py \
        --manifest C:/Evidence/CO-25-2722/documents/incoming/manifest.json \
        --output   C:/Evidence/CO-25-2722/output/defence_analysis \
        --framework prompts/qld_defence_framework.md
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

HEADER = "MACHINE-GENERATED - UNVERIFIED"

MODEL = "claude-opus-4-7"
MAX_TOKENS = 16000
MAX_BYTES_INLINE_TEXT = 180_000
MAX_IMAGE_BYTES = 4_500_000
IMAGE_MIME = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
TEXTUAL_EXTS = {".pdf", ".docx", ".xlsx", ".xls", ".txt", ".rtf", ".md", ".csv", ".json", ".html", ".htm"}

ANALYSIS_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "classification": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "document_type": {"type": "string"},
                "authored_by": {"type": "string"},
                "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
            },
            "required": ["document_type", "authored_by", "confidence"],
        },
        "key_facts": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "date": {"type": "string"},
                    "fact": {"type": "string"},
                    "citation": {"type": "string"},
                    "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                },
                "required": ["fact", "citation", "confidence"],
            },
        },
        "elements_undermined": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "charge": {"type": "string"},
                    "element": {"type": "string"},
                    "how": {"type": "string"},
                    "citation": {"type": "string"},
                    "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                },
                "required": ["charge", "element", "how", "citation", "confidence"],
            },
        },
        "procedural_issues": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "rule": {"type": "string"},
                    "breach": {"type": "string"},
                    "citation": {"type": "string"},
                    "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                },
                "required": ["rule", "breach", "citation", "confidence"],
            },
        },
        "credit_points": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "witness": {"type": "string"},
                    "point": {"type": "string"},
                    "citation": {"type": "string"},
                    "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                },
                "required": ["witness", "point", "citation", "confidence"],
            },
        },
        "asymmetric_themes": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "theme": {
                        "type": "string",
                        "enum": [
                            "activation",
                            "power_use",
                            "charging",
                            "witness",
                            "recording",
                        ],
                    },
                    "support": {"type": "string"},
                    "counterfactual": {"type": "string"},
                    "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                },
                "required": ["theme", "support", "counterfactual", "confidence"],
            },
        },
        "priority": {"type": "string", "enum": ["H", "M", "L"]},
        "notes": {"type": "string"},
    },
    "required": [
        "classification",
        "key_facts",
        "elements_undermined",
        "procedural_issues",
        "credit_points",
        "asymmetric_themes",
        "priority",
        "notes",
    ],
}


@dataclass
class DocInput:
    record_id: str
    name: str
    kind: str
    local_path: Path
    drive_path: str


def _load_client():
    try:
        import anthropic  # type: ignore
    except ImportError as e:
        print(
            "Missing anthropic SDK. Install with:\n    pip install anthropic",
            file=sys.stderr,
        )
        raise SystemExit(1) from e
    return anthropic.Anthropic()


def _load_framework(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _iter_manifest(manifest_path: Path) -> list[DocInput]:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    out: list[DocInput] = []
    for f in data.get("files", []):
        local = Path(f["local_path"])
        if not local.exists():
            continue
        ext = local.suffix.lower()
        out.append(
            DocInput(
                record_id=f["drive_id"],
                name=f["name"],
                kind=ext.lstrip("."),
                local_path=local,
                drive_path=f.get("drive_path", f["name"]),
            )
        )
    return out


def _iter_doc_json_dir(dir_path: Path) -> list[DocInput]:
    out: list[DocInput] = []
    for p in sorted(dir_path.glob("*.doc.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        local = Path(data["path"])
        out.append(
            DocInput(
                record_id=data["sha256"][:16] or data["stem"],
                name=local.name,
                kind=data.get("kind", local.suffix.lstrip(".")),
                local_path=local,
                drive_path=local.name,
            )
        )
    return out


def _extract_text(doc: DocInput) -> tuple[str, list[str]]:
    """Return (text, warnings). Uses the existing extract_documents helpers."""
    warnings: list[str] = []
    ext = doc.local_path.suffix.lower()
    if ext not in TEXTUAL_EXTS:
        return "", warnings

    sibling_json = doc.local_path.with_suffix(doc.local_path.suffix + ".doc.json")
    if not sibling_json.exists():
        sibling_json = doc.local_path.parent / f"{doc.local_path.stem}.doc.json"
    if sibling_json.exists():
        try:
            rec = json.loads(sibling_json.read_text(encoding="utf-8"))
            return rec.get("text", "") or "", rec.get("warnings", []) or []
        except Exception as e:
            warnings.append(f"sibling doc.json unreadable: {e}")

    try:
        import extract_documents as ed
        rec = ed.extract_one(doc.local_path)
        return rec.text, list(rec.warnings)
    except Exception as e:
        warnings.append(f"inline extraction failed: {e}")
        return "", warnings


def _build_user_content(doc: DocInput) -> tuple[list[dict[str, Any]], list[str]]:
    """Build the user message content blocks for one document.

    For images → vision block + text header.
    For textual docs → extracted text + metadata header.
    For oversize text → truncated with a warning flag (so counsel knows).
    """
    warnings: list[str] = []
    ext = doc.local_path.suffix.lower()
    header = (
        f"DOCUMENT METADATA\n"
        f"  record_id: {doc.record_id}\n"
        f"  name: {doc.name}\n"
        f"  drive_path: {doc.drive_path}\n"
        f"  kind: {doc.kind}\n"
        f"Analyse this document under the framework. Return strict JSON only."
    )

    if ext in IMAGE_MIME:
        try:
            data = doc.local_path.read_bytes()
            if len(data) > MAX_IMAGE_BYTES:
                warnings.append(
                    f"image exceeds {MAX_IMAGE_BYTES} bytes; sending anyway — consider downsampling"
                )
            mime = mimetypes.guess_type(str(doc.local_path))[0] or "image/jpeg"
            b64 = base64.standard_b64encode(data).decode("ascii")
            return (
                [
                    {"type": "text", "text": header},
                    {
                        "type": "image",
                        "source": {"type": "base64", "media_type": mime, "data": b64},
                    },
                ],
                warnings,
            )
        except Exception as e:
            warnings.append(f"image read failed: {e}")
            return [{"type": "text", "text": header + f"\n\n[IMAGE UNREADABLE: {e}]"}], warnings

    text, extract_warns = _extract_text(doc)
    warnings.extend(extract_warns)
    if not text.strip():
        return (
            [
                {
                    "type": "text",
                    "text": header + "\n\n[DOCUMENT PRODUCED NO EXTRACTABLE TEXT]",
                }
            ],
            warnings,
        )
    if len(text) > MAX_BYTES_INLINE_TEXT:
        warnings.append(
            f"text truncated from {len(text)} to {MAX_BYTES_INLINE_TEXT} chars"
        )
        text = text[:MAX_BYTES_INLINE_TEXT] + "\n\n[... TRUNCATED ...]"

    return [{"type": "text", "text": f"{header}\n\n---\n\n{text}"}], warnings


def analyse_one(
    client,
    doc: DocInput,
    framework: str,
) -> dict[str, Any]:
    import anthropic  # type: ignore

    content, warnings = _build_user_content(doc)

    system = [
        {
            "type": "text",
            "text": framework,
            "cache_control": {"type": "ephemeral"},
        }
    ]

    last_err: Exception | None = None
    for attempt in range(3):
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                thinking={"type": "adaptive"},
                output_config={
                    "effort": "high",
                    "format": {
                        "type": "json_schema",
                        "schema": ANALYSIS_SCHEMA,
                    },
                },
                system=system,
                messages=[{"role": "user", "content": content}],
            )
            break
        except anthropic.RateLimitError as e:
            last_err = e
            delay = min(2 ** attempt * 5, 60)
            print(f"    rate-limited, sleeping {delay}s", file=sys.stderr)
            time.sleep(delay)
        except anthropic.APIStatusError as e:
            last_err = e
            if e.status_code and e.status_code >= 500:
                time.sleep(2 ** attempt)
                continue
            raise
    else:
        raise RuntimeError(f"API failed after retries: {last_err}")

    text_block = next((b for b in response.content if b.type == "text"), None)
    parsed: dict[str, Any] = {}
    parse_error: str | None = None
    if text_block:
        try:
            parsed = json.loads(text_block.text)
        except json.JSONDecodeError as e:
            parse_error = f"model output not valid JSON: {e}"
            parsed = {"raw": text_block.text}

    usage = response.usage
    return {
        "header": HEADER,
        "record_id": doc.record_id,
        "name": doc.name,
        "drive_path": doc.drive_path,
        "local_path": str(doc.local_path),
        "model": MODEL,
        "stop_reason": response.stop_reason,
        "usage": {
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "cache_creation_input_tokens": getattr(usage, "cache_creation_input_tokens", 0),
            "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", 0),
        },
        "warnings": warnings,
        "parse_error": parse_error,
        "analysis": parsed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run Claude Opus 4.7 defence analysis over an ingested corpus."
    )
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--manifest", help="Path to manifest.json from gdrive_ingest.py")
    src.add_argument(
        "--doc-json-dir",
        help="Directory of *.doc.json files from extract_documents.py",
    )
    parser.add_argument("--output", required=True, help="Output directory for per-doc analyses")
    parser.add_argument(
        "--framework",
        required=True,
        help="Path to prompts/qld_defence_framework.md",
    )
    parser.add_argument(
        "--limit", type=int, default=0, help="Stop after N documents (0 = no limit)"
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip documents whose <record_id>.analysis.json already exists",
    )
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("ANTHROPIC_API_KEY is not set.")

    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    framework = _load_framework(Path(args.framework))
    docs = (
        _iter_manifest(Path(args.manifest))
        if args.manifest
        else _iter_doc_json_dir(Path(args.doc_json_dir))
    )
    print(f"{len(docs)} documents to analyse")

    client = _load_client()

    done = 0
    cache_reads = 0
    errors = 0
    for doc in docs:
        out_path = output_dir / f"{doc.record_id}.analysis.json"
        if args.resume and out_path.exists():
            continue
        print(f"[{done + 1}/{len(docs)}] {doc.drive_path}")
        try:
            result = analyse_one(client, doc, framework)
            out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
            cache_reads += result["usage"]["cache_read_input_tokens"]
        except Exception as e:
            errors += 1
            print(f"    ERROR: {e}", file=sys.stderr)
            err_path = output_dir / f"{doc.record_id}.error.json"
            err_path.write_text(
                json.dumps({"header": HEADER, "record_id": doc.record_id, "error": str(e)}, indent=2),
                encoding="utf-8",
            )
        done += 1
        if args.limit and done >= args.limit:
            break

    print(
        f"\n{done} analysed, {errors} errors. Cache-read tokens: {cache_reads:,} "
        f"(higher = better; confirms framework prompt is being cached)."
    )


if __name__ == "__main__":
    main()
