---
name: yon-tool-registry
description: Resolve an evidence-backed project-local Tool Registry from the detected environment, distinguishing actual availability, authorization, degradation, absence, and unknown state before YON orchestrates real actions.
disable-model-invocation: true
---

# YON Tool Registry

Use this skill after environment detection and before substantial tool-mediated execution.

## Position

`PROJECT → ENVIRONMENT → PROFILE → TOOL REGISTRY → ORCHESTRATE → EXECUTE`

The registry is a decision aid, not a list of installed software. `DOCUMENTED ≠ AVAILABLE`.

## Resolution loop

`READ PROFILE → NORMALIZE SIGNALS → RESOLVE STATUS → CHECK AUTHORITY → MATCH CAPABILITY → EXPOSE EVIDENCE`

### 1. Read profile

Read the current Environment Profile and project-local instructions. If no profile exists, use `yon-environment` first.

### 2. Normalize signals

Collect only relevant signals: executable probes, connected adapters, package manifests, lockfiles, scripts, configuration, local instructions and previous verification evidence.

Never expose secret values.

### 3. Resolve status

Each concrete adapter receives one state:

`AVAILABLE | UNAVAILABLE | UNAUTHORIZED | DEGRADED | UNKNOWN`

Use precedence:

`ACTUAL > AUTHORIZED > CONFIGURED > SIGNALLED > ASSUMED`

Configuration can indicate that a tool is expected; it cannot by itself prove availability.

### 4. Check authority

Separate presence from permission. A tool can be installed but unauthorized for a repository, tenant, production environment, database, or destructive operation.

### 5. Match capability

Map concrete adapters to abstract classes from `orchestration/TOOL-CAPABILITY-REGISTRY.md`. Select the smallest adapter capable of producing the evidence required by the current plan slice.

### 6. Expose evidence

For every selected adapter record enough evidence to explain why it was chosen, its current status, risk, authority, side effects, and verification freshness.

## Mandatory rules

- Never infer availability from documentation alone.
- Never infer permission from authentication artifacts alone.
- Never print or persist secrets.
- Never select a high-risk adapter without current enough evidence and required authorization.
- Never hide contradictory signals; lower-precedence signals cannot erase stronger observations.
- If the required capability is `UNKNOWN`, perform the smallest safe probe or remain `BLOCKED`.
- If an equivalent lower-risk adapter produces sufficient evidence, prefer it.
- Refresh relevant state before production, migration, billing, auth/authz, destructive, security-sensitive, or critical external actions.

## Output

A resolved Tool Registry should answer:

1. What tools can YON actually use?
2. What can each tool do for this project?
3. What permission does each action require?
4. What evidence established availability?
5. What is the risk?
6. What side effects are possible?
7. What remains unknown or blocked?

The output must remain project-local unless generalized knowledge is deliberately extracted through YON's evidence process.