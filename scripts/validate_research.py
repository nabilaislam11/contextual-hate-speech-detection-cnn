#!/usr/bin/env python3
"""Verify research documents and local Markdown links."""
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
paper = ROOT / "research" / "Final Paper.pdf"
if not paper.is_file() or paper.stat().st_size == 0:
    errors.append("Expected research paper is missing or empty")

link_pattern = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
for document in [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]:
    for raw in link_pattern.findall(document.read_text(encoding="utf-8")):
        link = raw.split(' "', 1)[0].strip().strip("<>")
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (document.parent / unquote(url.path)).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"Outside repository: {document.relative_to(ROOT)} -> {link}")
            continue
        if not target.exists():
            errors.append(f"Broken local link: {document.relative_to(ROOT)} -> {link}")

if errors:
    raise SystemExit("\n".join(errors))
print("Research PDF and local Markdown links verified.")
