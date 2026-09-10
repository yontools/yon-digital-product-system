---
name: yon-orchestrate
description: Select and coordinate the smallest sufficient development, runtime, browser, test, GitHub, deployment, or media tool for a YON action, with explicit authorization, observation, risk, evidence, and blocking rules.
disable-model-invocation: true
---

# YON Orchestration

Use this skill when YON needs to move from a product decision or execution-plan slice to a real tool action.

## Position

`BLUEPRINT → EXECUTION PLAN → ORCHESTRATE → EXECUTE → OBSERVE → DECIDE NEXT → VERIFY`

Orchestration is a control layer, not an architecture generator and not permission to expand scope.

## Operating loop

`DECIDE → SELECT → AUTHORIZE → EXECUTE → OBSERVE → DECIDE NEXT`

### 1. DECIDE

State the smallest outcome the action must produce. Tie it to the approved Blueprint, workflow, or Execution Plan slice when one exists.

### 2. SELECT

Choose the smallest available tool class that can produce sufficient evidence:

| Need | Preferred class |
|---|---|
| understand files/code/config | repository/filesystem |
| run scripts/build/server | terminal/runtime |
| inspect actual UI journey | browser/automation |
| prove behavior automatically | tests |
| inspect or update repository collaboration state | GitHub |
| deploy or inspect hosted infrastructure | deployment/infrastructure |
| create meaningful visual/media assets | visual/media |

Do not use a larger or riskier tool merely because it is available.

### 3. AUTHORIZE

Classify the action:

- `LOW`: read-only inspection, local tests, non-destructive browser QA.
- `MEDIUM`: edits, dependency installation, generated assets, commits, reversible repository changes.
- `HIGH`: production deployment, database migrations, billing, authentication/authorization, destructive operations, security-sensitive changes, critical external integrations, or core business rules.

For HIGH actions, require explicit authorization and proportional verification. If authorization or verification is missing, stop as `BLOCKED`.

### 4. EXECUTE

Use the minimum input and minimum scope required. Respect repository-local instructions and project boundaries. Never fabricate tool availability, command output, screenshots, test results, deployments, or successful changes.

### 5. OBSERVE

After every meaningful mutation, inspect its real result. Observation may include:

- command output
- changed files/diff
- running application
- browser state
- test result
- CI result
- deployment status
- integration response

Convert observations into evidence before deciding the next action.

### 6. DECIDE NEXT

Continue only when the observed result justifies another action. If a failure can be corrected safely, return to `EXECUTE`. If a critical condition is missing, enter `BLOCKED`.

## State machine

`PLANNED → AUTHORIZED → EXECUTING → OBSERVING → DECIDING → COMPLETED`

Blocked transitions:

`PLANNED / AUTHORIZED / EXECUTING / OBSERVING → BLOCKED`

`BLOCKED` is never `PASS`, `VERIFIED`, or completion.

## Tool boundaries

### Repository / filesystem

Inspect before editing. Preserve unrelated behavior. Keep changes small and traceable.

### Terminal / runtime

Prefer existing project scripts. Do not install dependencies or execute destructive commands without a reason and appropriate permission.

### Browser / automation

Use for behavior that cannot be established statically: critical journeys, responsive behavior, interactive states, accessibility observations, and visual/runtime regressions. Prefer a real running product over assumptions from source code.

### Tests

Use the strongest existing test that directly proves the acceptance criterion. A passing unrelated test does not prove a product outcome.

### GitHub

Use only the connected/authenticated repository context. Read before write. Commits, branches, PRs, issues, labels and CI operations must stay within authorized project scope.

### Deployment / infrastructure

Treat hosted changes as HIGH unless the environment explicitly establishes a lower-risk read-only operation. Never invent credentials, project IDs, environments, URLs, or deployment state.

### Visual / media

Generate or edit assets only when they solve a real product/communication need. Avoid generic decorative assets that add complexity without user value.

## Failure rules

- Tool unavailable → `BLOCKED`.
- Permission unavailable → `BLOCKED`.
- Required input unknown → inspect first; if still unknown and critical → `BLOCKED`.
- Verification unavailable for a HIGH-risk action → `BLOCKED`.
- Tool output contradicts the plan → stop and re-evaluate; do not force completion.
- A build passing does not prove runtime/product success.
- A screenshot looking correct does not prove data integrity or authorization.

## Privacy

Never move private project material into public YON knowledge. Do not expose secrets, credentials, customer data, proprietary code, private prompts, private architecture, or identifying business rules. Keep tenant boundaries explicit.

## Handoff

For substantial work, record the action using `orchestration/TOOL-CONTRACT-TEMPLATE.md` or an equivalent project-local record. Evidence should be sufficient for another agent or human to understand what was executed and why the next action is justified.
