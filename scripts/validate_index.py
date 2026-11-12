#!/usr/bin/env python3
"""Validate plugins/main/index.yml before it is committed, pushed or served.

Stash reads this file as its plugin source list. One unparseable line makes Stash
reject the whole list ("reading package list: yaml: line N: mapping values are not
allowed in this context"), so an invalid file must never reach main.

Usual trap: an unquoted description containing an ASCII colon + space, e.g.

    description: Things to know: here is why          # breaks
    description: "Things to know: here is why"        # fine

Also cross-checks README.md, because three sections there are maintained by hand
(the workflow only rewrites the version column): every plugin in index.yml must
appear in the 包含的插件 table, in 前置依赖, and its release repo must appear in
相关仓库. Without this, a newly added plugin silently stays unfindable in the docs.

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


def section(text: str, heading: str) -> str:
    """Return the body of a `## heading` block, or "" when absent."""
    if heading not in text:
        return ""
    return text.split(heading, 1)[1].split("\n## ", 1)[0]


def readme_drift(entries: list[dict], readme: str) -> list[str]:
    """List plugins that index.yml has but a hand-maintained README section lacks."""
    problems: list[str] = []

    table = []
    for line in section(readme, "## 包含的插件").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.split("|")]
        if len(cells) > 2 and cells[1] and not re.fullmatch(r":?-+:?", cells[1]):
            table.append(cells[1])

    deps = [re.split(r"[（(]", m.group(1))[0].strip()
            for m in re.finditer(r"^-\s+(.+?)\s*$", section(readme, "## 前置依赖"), re.M)]

    repos = set(re.findall(r"github\.com/[^/\s]+/([A-Za-z0-9_.-]+)", section(readme, "## 相关仓库")))

    for entry in entries:
        name = str(entry["name"])
        if name not in table:
            problems.append(f"{name}: missing from the 包含的插件 table")
        if name not in deps:
            problems.append(
                f"{name}: missing from 前置依赖 — list it under 纯 UI 插件 (no Python) "
                f"or Python 插件 (with requirements)"
            )
        repo = re.match(r"https://github\.com/[^/]+/([^/]+)/releases/", str(entry["path"]))
        if repo and repo.group(1) not in repos:
            problems.append(f"{name}: release repo {repo.group(1)} is missing from 相关仓库")
    return problems


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

    readme = target.resolve().parents[2] / "README.md"
    if readme.exists():
        drift = readme_drift(entries, readme.read_text(encoding="utf-8"))
        if drift:
            return fail(
                "README.md is out of sync with index.yml:\n       "
                + "\n       ".join(drift)
            )

    print(f"OK: {target} — {len(entries)} entries, YAML parses, README in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
