# YON Execution

This directory contains the operational planning layer between Product Blueprint and implementation.

## Flow

`BLUEPRINT → EXECUTION PLAN → EXECUTE → VERIFY → EVIDENCE`

The Execution Plan converts approved product decisions into dependency-aware vertical slices, observable acceptance criteria, verification checkpoints, risk boundaries, and explicit blockers.

## Principles

- Plan from user outcomes and workflows, not technical file lists.
- Keep every meaningful slice traceable to an approved Blueprint decision.
- Prefer vertical slices that can be run and verified early.
- Treat high-risk boundaries explicitly.
- Do not hide unresolved product decisions inside implementation tasks.
- `BLOCKED` is never `VERIFIED`.
- Deferred work is not silently included in scope.

## Contents

- `EXECUTION-PLAN-TEMPLATE.md` — reusable plan structure.
- `skills/yon-execution-plan/SKILL.md` — planning rules.
- `commands/yon-execution-plan.md` — manual command.
