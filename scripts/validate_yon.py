#!/usr/bin/env python3
"""Structural integrity validator for the YON Digital Product System repository.

Portable: Python standard library only. Intended for local use and CI.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:
        fail(f"cannot read {path.relative_to(ROOT)}: {exc}")
        return ""


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    result: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    return result


def check_required_files() -> None:
    required = [
        ".claude-plugin/plugin.json",
        "YON.md",
        "README.md",
        "CONTRIBUTING.md",
        "INSTALL-CLAUDE-CODE.md",
        "skills/yon/SKILL.md",
        "capabilities/INDEX.md",
        "patterns/INDEX.md",
        "evidence/INDEX.md",
        "validation/INDEX.md",
    ]
    for rel in required:
        if not (ROOT / rel).is_file():
            fail(f"missing required file: {rel}")


def check_plugin() -> None:
    path = ROOT / ".claude-plugin/plugin.json"
    if not path.is_file():
        return
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in .claude-plugin/plugin.json: {exc}")
        return
    for key in ("name", "version"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            fail(f"plugin.json missing non-empty '{key}'")


def check_skills() -> None:
    skills_dir = ROOT / "skills"
    if not skills_dir.is_dir():
        fail("missing skills/ directory")
        return
    for directory in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        path = directory / "SKILL.md"
        if not path.is_file():
            fail(f"skill directory missing SKILL.md: {directory.relative_to(ROOT)}")
            continue
        meta = frontmatter(read_text(path))
        if not meta.get("name"):
            fail(f"skill missing frontmatter name: {path.relative_to(ROOT)}")
        elif meta["name"] != directory.name:
            fail(f"skill name mismatch: {path.relative_to(ROOT)} declares '{meta['name']}'")
        if not meta.get("description"):
            fail(f"skill missing frontmatter description: {path.relative_to(ROOT)}")


def check_commands() -> None:
    commands_dir = ROOT / "commands"
    if not commands_dir.is_dir():
        fail("missing commands/ directory")
        return
    for path in sorted(commands_dir.glob("*.md")):
        text = read_text(path)
        meta = frontmatter(text)
        if not meta.get("description"):
            fail(f"command missing frontmatter description: {path.relative_to(ROOT)}")
        # Any explicit `foo` skill reference must resolve.
        for name in re.findall(r"`([a-z0-9][a-z0-9-]*)` skill", text, re.I):
            if not (ROOT / "skills" / name / "SKILL.md").is_file():
                fail(f"command {path.relative_to(ROOT)} references missing skill: {name}")


def check_agents() -> None:
    agents_dir = ROOT / "agents"
    if not agents_dir.is_dir():
        return
    for path in sorted(agents_dir.glob("*.md")):
        if not frontmatter(read_text(path)).get("name"):
            fail(f"agent missing frontmatter name: {path.relative_to(ROOT)}")


def check_markdown_paths() -> None:
    """Validate repository-relative markdown path references of the form `path/file.md`."""
    pattern = re.compile(r"(?<![\w/.-])((?:skills|commands|agents|capabilities|patterns|evidence|validation|adapters|templates|scripts|\.github)/[A-Za-z0-9_.\-/]+\.md)(?![\w/.-])")
    skip = {"<path>/file.md", "path/to/file.md"}
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") and part not in {".github"} for part in path.relative_to(ROOT).parts):
            continue
        text = read_text(path)
        for ref in pattern.findall(text):
            if ref in skip or "<" in ref or "..." in ref:
                continue
            if not (ROOT / ref).is_file():
                fail(f"broken markdown path in {path.relative_to(ROOT)}: {ref}")


def check_indexes() -> None:
    index_specs = {
        "capabilities/INDEX.md": "capabilities",
        "patterns/INDEX.md": "patterns",
    }
    for index_rel, directory in index_specs.items():
        path = ROOT / index_rel
        if not path.is_file():
            continue
        text = read_text(path)
        # Catch explicit markdown links to local files in the same knowledge directory.
        for target in re.findall(r"\]\(([^)]+\.md)\)", text):
            target = target.split("#", 1)[0]
            if target.startswith("http"):
                continue
            candidate = (path.parent / target).resolve()
            if not candidate.is_file():
                fail(f"broken index link in {index_rel}: {target}")


def main() -> int:
    check_required_files()
    check_plugin()
    check_skills()
    check_commands()
    check_agents()
    check_markdown_paths()
    check_indexes()

    if ERRORS:
        print(f"YON validation FAILED: {len(ERRORS)} issue(s)")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    skill_count = len([p for p in (ROOT / "skills").iterdir() if p.is_dir()]) if (ROOT / "skills").is_dir() else 0
    command_count = len(list((ROOT / "commands").glob("*.md"))) if (ROOT / "commands").is_dir() else 0
    print(f"YON validation PASS — {skill_count} skills, {command_count} commands, repository structure coherent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
