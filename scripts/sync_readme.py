#!/usr/bin/env python3
"""Sync plugin versions from plugins/main/index.yml into README.md's plugin table.

Pure-stdlib (no PyYAML dependency). Triggered by the GitHub Action
`.github/workflows/sync-readme.yml` whenever `plugins/main/index.yml` changes:
parses each plugin's `name`/`version`, then rewrites the version column of the
"## 包含的插件" table rows whose plugin name matches. No-op when versions
already match (idempotent). Only the version cell is touched; other columns and
the rest of the file are left as-is.
"""
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "plugins" / "main" / "index.yml"
README = ROOT / "README.md"
TABLE_HEADING = "## 包含的插件"


def parse_index(text):
    """Extract {name: version} from index.yml without requiring PyYAML.

    Each top-level entry starts with `- id: ...` at column 0; its `name:`
    and `version:` fields are indented by two spaces.
    """
    versions = {}
    current_name = None
    for line in text.splitlines():
        if re.match(r"^-\s+id:\s*\S+", line):
            current_name = None  # new entry
            continue
        m = re.match(r"^\s+name:\s*(.+?)\s*$", line)
        if m:
            current_name = m.group(1).strip()
            continue
        m = re.match(r"^\s+version:\s*([0-9][0-9A-Za-z._-]*)", line)
        if m and current_name:
            versions[current_name] = m.group(1)
    return versions


def sync_readme(text, versions):
    """Rewrite the version column of matching rows in the plugin table."""
    lines = text.splitlines()
    out = []
    in_table = False
    changed = False
    for line in lines:
        if line.startswith("## "):
            in_table = (line.strip() == TABLE_HEADING)
        elif in_table and line.startswith("|"):
            cells = line.split("|")
            # Skip the header (| 插件 | 版本 | ...) and the separator (|---|...)
            if len(cells) >= 3 and not re.match(r"^\s*:?-+\s*$", cells[1]) \
               and not re.match(r"^\s*:?-+\s*$", cells[2]):
                name = cells[1].strip()
                if name in versions:
                    old_cell = cells[2]
                    old_version = old_cell.strip()
                    new_version = versions[name]
                    if old_version != new_version:
                        leading = old_cell[:len(old_cell) - len(old_cell.lstrip())]
                        trailing = old_cell[len(old_cell.rstrip()):]
                        cells[2] = "{}{}{}".format(leading, new_version, trailing)
                        line = "|".join(cells)
                        changed = True
        out.append(line)
    newline = "\r\n" if "\r\n" in text else "\n"
    result = newline.join(out)
    if text.endswith("\n"):
        result += newline
    return result, changed


def main():
    index_text = io.open(str(INDEX), encoding="utf-8").read()
    versions = parse_index(index_text)
    if not versions:
        print("ERROR: no plugin versions parsed from index.yml", file=sys.stderr)
        sys.exit(1)
    readme_text = io.open(str(README), encoding="utf-8").read()
    new_text, changed = sync_readme(readme_text, versions)
    if changed:
        with io.open(str(README), "w", encoding="utf-8", newline="") as f:
            f.write(new_text)
        print("README.md updated: {}".format(
            ", ".join("{}={}".format(k, v) for k, v in sorted(versions.items()))))
    else:
        print("README.md already up to date")


if __name__ == "__main__":
    main()
