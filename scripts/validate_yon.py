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
        ".claude-plugin/plugin.json", "YON.md", "README.md", "CONTRIBUTING.md",
        "INSTALL-CLAUDE-CODE.md", "skills/yon/SKILL.md",
        "skills/yon-environment/SKILL.md", "skills/yon-tool-registry/SKILL.md",
        "skills/yon-orchestrate/SKILL.md", "skills/yon-agent-system/SKILL.md",
        "commands/yon-environment.md", "commands/yon-tool-registry.md",
        "commands/yon-orchestrate.md", "commands/yon-agent-system.md",
        "adapters/claude-code/CLAUDE.md", "capabilities/INDEX.md", "patterns/INDEX.md",
        "evidence/INDEX.md", "validation/INDEX.md", "environment/README.md",
        "environment/DETECTION-RULES.md", "environment/ENVIRONMENT-PROFILE-TEMPLATE.md",
        "environment/TOOL-REGISTRY-BRIDGE.md", "orchestration/README.md",
        "orchestration/TOOL-CAPABILITY-REGISTRY.md", "orchestration/TOOL-CAPABILITY-MATRIX.md",
        "orchestration/TOOL-ADAPTER-TEMPLATE.md", "scripts/detect_environment.py",
        "scripts/validate_yon.py", ".github/workflows/validate.yml",
        "model/BUSINESS-GRAPH.md", "model/UNIVERSAL-PRODUCT-MODEL.md",
        "events/README.md", "events/EVENT-CONTRACT-TEMPLATE.md",
        "agents/AGENT-AUTONOMY.md", "agents/AGENT-PROFILE-TEMPLATE.md",
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


def check_environment_contract() -> None:
    required_terms = {
        "environment/README.md": ("Environment Profile", "DOCUMENTED ≠ AVAILABLE", "UNAUTHORIZED", "Privacy"),
        "environment/DETECTION-RULES.md": ("Project detection", "Tool detection", "Authority detection", "Conflict resolution"),
        "environment/ENVIRONMENT-PROFILE-TEMPLATE.md": ("Stack signals", "Tool adapters", "Authority", "Blockers", "Privacy"),
        "environment/TOOL-REGISTRY-BRIDGE.md": ("ACTUAL", "CONFIGURED", "SIGNALLED", "UNKNOWN", "Drift", "Privacy"),
        "skills/yon-environment/SKILL.md": ("INSPECT", "SIGNAL", "PROBE SAFELY", "CLASSIFY", "PROFILE", "HANDOFF"),
        "skills/yon-tool-registry/SKILL.md": ("READ PROFILE", "RESOLVE STATUS", "CHECK AUTHORITY", "MATCH CAPABILITY", "UNKNOWN"),
        "commands/yon-environment.md": ("Environment Profile", "read-only", "BLOCKED"),
        "commands/yon-tool-registry.md": ("Environment Profile", "BLOCKED", "secrets"),
        "scripts/detect_environment.py": ("secret_values_read", "tool_states", "authorization"),
    }
    for rel, terms in required_terms.items():
        path = ROOT / rel
        if not path.is_file():
            continue
        text = read_text(path)
        for term in terms:
            if term not in text:
                fail(f"environment contract missing '{term}' in {rel}")


def check_orchestration_contract() -> None:
    required_terms = {
        "orchestration/README.md": ("SELECT TOOL", "AUTHORIZE", "OBSERVE", "BLOCKED", "Environment Profile"),
        "orchestration/TOOL-CAPABILITY-REGISTRY.md": ("DOCUMENTED ≠ AVAILABLE", "availability_status", "risk"),
        "orchestration/TOOL-CAPABILITY-MATRIX.md": ("Minimum evidence", "Fallback policy", "No-tool rule"),
        "orchestration/TOOL-ADAPTER-TEMPLATE.md": ("Inputs", "Outputs", "Risk", "Privacy"),
        "skills/yon-orchestrate/SKILL.md": ("DECIDE", "SELECT", "AUTHORIZE", "EXECUTE", "OBSERVE", "DECIDE NEXT", "yon-tool-registry"),
    }
    for rel, terms in required_terms.items():
        path = ROOT / rel
        if not path.is_file():
            continue
        text = read_text(path)
        for term in terms:
            if term not in text:
                fail(f"orchestration contract missing '{term}' in {rel}")


def check_graph_event_agent_contract() -> None:
    required_terms = {
        "model/BUSINESS-GRAPH.md": ("Business Graph", "Relationship types", "Provenance", "Temporal graph", "Implementation neutrality", "Privacy"),
        "events/README.md": ("Event Engine", "Commands versus events", "idempotent", "retry", "Privacy"),
        "events/EVENT-CONTRACT-TEMPLATE.md": ("Event identity", "Correlation ID", "Causation ID", "Idempotency identity", "Final result"),
        "agents/AGENT-AUTONOMY.md": ("Level 1", "Level 2", "Level 3", "Level 4", "MODEL CAPABILITY ≠ TOOL ACCESS", "Stop conditions", "Privacy"),
        "agents/AGENT-PROFILE-TEMPLATE.md": ("Autonomy", "Approval thresholds", "Stop conditions", "Verification"),
        "skills/yon-agent-system/SKILL.md": ("BUSINESS GRAPH", "EVENT ENGINE", "MODEL CAPABILITY ≠ TOOL ACCESS", "BLOCKED", "verification"),
        "commands/yon-agent-system.md": ("autonomy", "approval", "BLOCKED", "verification"),
        "capabilities/INDEX.md": ("Business Graph", "Event-driven Coordination", "Agentic Operations", "Graph, events, and agents"),
    }
    for rel, terms in required_terms.items():
        path = ROOT / rel
        if not path.is_file():
            continue
        text = read_text(path)
        for term in terms:
            if term not in text:
                fail(f"graph/event/agent contract missing '{term}' in {rel}")


def main() -> int:
    check_required_files()
    check_plugin()
    check_skills()
    check_knowledge_directories()
    check_environment_contract()
    check_orchestration_contract()
    check_graph_event_agent_contract()
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
