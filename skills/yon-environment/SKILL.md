---
name: yon-environment
description: Detect and profile the real project environment, stack, tool availability, and authority before YON selects or executes development actions. Never expose secrets or infer availability from documentation alone.
disable-model-invocation: true
---

# YON Environment

Use this skill when YON enters an unfamiliar project, when tool availability is unknown, or when orchestration needs a refreshed environment profile.

## Position

`PROJECT → ENVIRONMENT DETECTION → PROFILE → TOOL REGISTRY → ORCHESTRATE`

## Operating loop

`INSPECT → SIGNAL → PROBE SAFELY → CLASSIFY → PROFILE → HANDOFF`

### 1. INSPECT

Identify the project root, repository, local instructions, manifests, lockfiles, scripts, test configuration and deployment signals.

### 2. SIGNAL

Infer candidate runtimes, frameworks, package managers, test/browser systems, databases and deployment providers only from observable project signals.

A signal is not proof of availability.

### 3. PROBE SAFELY

When needed, perform the smallest non-destructive check for actual tool availability. Prefer executable lookup or read-only status checks. Do not install, deploy, migrate or mutate state just to prove a tool exists.

### 4. CLASSIFY

Use tool states:

`UNKNOWN | SIGNALLED | AVAILABLE | UNAVAILABLE | UNAUTHORIZED | DEGRADED`

Use confidence:

`HIGH | MEDIUM | LOW`

Actual availability outranks repository signals. Authorization is always a separate property.

### 5. PROFILE

Create or refresh an environment profile using `environment/ENVIRONMENT-PROFILE-TEMPLATE.md`. Record evidence and blockers, not secrets.

The profile must distinguish:

- what the project appears to use
- what is actually executable/available
- what is authorized
- what remains unknown
- what can be verified

### 6. HANDOFF

Pass the profile to `yon-orchestrate`. If a required tool is unknown, orchestration may request one safe detection action. If a critical permission or verification condition remains missing, mark the intended action `BLOCKED`.

## Privacy

Never print or store secret values, tokens, cookies, credentials, customer data, private code, private architecture, or proprietary business rules. Environment detection must be safe to run against private projects.

## Completion

Environment detection is complete when YON can answer:

1. Where am I working?
2. What stack signals exist?
3. Which tools are actually available?
4. Which are only signalled?
5. What authority exists for the intended action?
6. What evidence supports those conclusions?
7. What is the smallest safe next action?
