#!/usr/bin/env python3
"""Reliable, dependency-free structural validator for the YON repository."""
from __future__ import annotations

import json
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
        if ":" in line:
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
        "scripts/validate_yon.py",
        ".github/workflows/validate.yml",
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
        if meta.get("name") != directory.name:
            fail(f"skill name mismatch: {path.relative_to(ROOT)} declares '{meta.get('name', '')}'")
        if not meta.get("description"):
            fail(f"skill missing description: {path.relative_to(ROOT)}")


def check_knowledge_directories() -> None:
    for directory in ("capabilities", "patterns", "evidence", "validation"):
        path = ROOT / directory
        if not path.is_dir():
            fail(f"missing knowledge directory: {directory}/")
        elif not (path / "README.md").is_file() and directory != "validation":
            fail(f"missing knowledge README: {directory}/README.md")


def main() -> int:
    check_required_files()
    check_plugin()
    check_skills()
    check_knowledge_directories()

    if ERRORS:
        print(f"YON validation FAILED: {len(ERRORS)} issue(s)")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    skills = [p for p in (ROOT / "skills").iterdir() if p.is_dir()]
    commands = list((ROOT / "commands").glob("*.md")) if (ROOT / "commands").is_dir() else []
    print(f"YON validation PASS — {len(skills)} skills, {len(commands)} commands, core structure coherent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
