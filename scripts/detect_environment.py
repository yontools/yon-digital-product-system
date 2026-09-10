#!/usr/bin/env python3
"""Portable, read-only YON environment detector.

Reports observable project/tool signals without printing secret values.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path.cwd().resolve()


def exists(name: str) -> bool:
    return (ROOT / name).exists()


def command_available(name: str) -> bool:
    return shutil.which(name) is not None


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def git_root() -> str | None:
    if not command_available("git"):
        return None
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except Exception:
        return None
    value = result.stdout.strip()
    return value or None


def main() -> int:
    package = read_json(ROOT / "package.json") if exists("package.json") else {}
    scripts = package.get("scripts", {}) if isinstance(package.get("scripts", {}), dict) else {}
    deps = {}
    for key in ("dependencies", "devDependencies", "peerDependencies"):
        value = package.get(key, {})
        if isinstance(value, dict):
            deps.update(value)

    markers = {
        "node": command_available("node"),
        "npm": command_available("npm"),
        "pnpm": command_available("pnpm"),
        "yarn": command_available("yarn"),
        "bun": command_available("bun"),
        "python": command_available("python") or command_available("python3"),
        "git": command_available("git"),
        "vercel": command_available("vercel"),
        "supabase": command_available("supabase"),
    }

    local_instruction_files = [
        name for name in (
            "CLAUDE.md", "AGENTS.md", "CONTRIBUTING.md", "README.md"
        ) if exists(name)
    ]

    lockfiles = [
        name for name in (
            "package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lock", "bun.lockb",
            "poetry.lock", "uv.lock", "Pipfile.lock"
        ) if exists(name)
    ]

    framework_signals = []
    known_dependencies = (
        "next", "react", "vue", "nuxt", "svelte", "sveltekit", "astro",
        "vite", "angular", "@angular/core", "remix", "express", "fastify",
        "tailwindcss", "playwright", "@playwright/test", "vitest", "jest",
        "cypress", "supabase", "@supabase/supabase-js"
    )
    for name in known_dependencies:
        if name in deps:
            framework_signals.append(name)

    tool_states = {}
    for tool, available in markers.items():
        tool_states[tool] = {
            "availability": "AVAILABLE" if available else "UNAVAILABLE",
            "evidence": "executable lookup in PATH",
        }

    result = {
        "profile_state": "DETECTED",
        "project": {
            "root": str(ROOT),
            "git_root": git_root(),
            "git_repository_signal": exists(".git"),
        },
        "instructions": local_instruction_files,
        "stack": {
            "package_manifest": "package.json" if exists("package.json") else None,
            "lockfiles": lockfiles,
            "framework_and_library_signals": framework_signals,
            "scripts": sorted(scripts),
        },
        "tools": tool_states,
        "authorization": {
            "repository_write": "UNKNOWN",
            "deployment": "UNKNOWN",
            "database_mutation": "UNKNOWN",
            "high_risk_actions": "UNKNOWN",
            "note": "Tool availability does not imply authorization.",
        },
        "privacy": {
            "secret_values_read": False,
            "environment_values_printed": False,
        },
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
