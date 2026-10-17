#!/usr/bin/env python3
"""Validate plugins/main/index.yml before it is committed, pushed or served.

Stash reads this file as its plugin source list. One unparseable line makes Stash
reject the whole list ("reading package list: yaml: line N: mapping values are not
allowed in this context"), so an invalid file must never reach main.

Usual trap: an unquoted description containing an ASCII colon + space, e.g.

    description: Things to know: here is why          # breaks
    description: "Things to know: here is why"        # fine

Usage:
    python3 scripts/validate_index.py [path/to/index.yml]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_TARGET = "plugins/main/index.yml"
REQUIRED = ("id", "name", "version", "date", "path", "sha256")
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def main(argv: list[str]) -> int:
    target = Path(argv[1] if len(argv) > 1 else DEFAULT_TARGET)
    try:
        import yaml
    except ImportError:
        return fail("PyYAML is not installed — run: python -m pip install pyyaml")
    try:
        raw = target.read_text(encoding="utf-8")
    except OSError as error:
        return fail(f"cannot read {target}: {error}")
    try:
        entries = yaml.safe_load(raw)
    except yaml.YAMLError as error:
        return fail(
            f"{target} is not valid YAML: {error}\n"
            '       a description with ": " inside must be quoted'
        )
    if not isinstance(entries, list) or not entries:
        return fail(f"{target} must be a non-empty list of plugin entries")

    seen: set[str] = set()
    for number, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            return fail(f"entry #{number} is not a mapping")
        missing = [key for key in REQUIRED if not entry.get(key)]
        if missing:
            return fail(f"entry #{number} ({entry.get('id', '?')}) is missing: {', '.join(missing)}")
        plugin_id = str(entry["id"])
        if plugin_id in seen:
            return fail(f"duplicate plugin id: {plugin_id}")
        seen.add(plugin_id)
        if not isinstance(entry.get("metadata"), dict):
            return fail(f"{plugin_id}: metadata block is missing")
        if not SHA256.match(str(entry["sha256"])):
            return fail(f"{plugin_id}: sha256 must be 64 lowercase hex characters")

    print(f"OK: {target} — {len(entries)} entries, YAML parses")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
