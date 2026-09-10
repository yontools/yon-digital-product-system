# YON Environment → Tool Registry Bridge

The Environment Profile is the evidence-backed input used to build a project-local Tool Registry.

It does not install, authenticate, or enable tools. It translates observations about the environment into explicit adapter states that `yon-orchestrate` can consume.

## Flow

`PROJECT → ENVIRONMENT DETECTION → PROFILE → TOOL REGISTRY → ORCHESTRATION`

## Resolution precedence

Use evidence in this order:

1. **ACTUAL** — a real tool probe or connected adapter confirms availability.
2. **AUTHORIZED** — the environment confirms the tool can be used for the required project scope.
3. **CONFIGURED** — project configuration or local instructions explicitly identify the tool.
4. **SIGNALLED** — manifests, lockfiles, scripts or config files indicate that the tool may exist.
5. **ASSUMED** — generic knowledge only. Never promote this to available.

A lower-precedence signal must never overwrite a stronger contradictory observation.

## Adapter states

Every concrete adapter should resolve to exactly one current state:

- `AVAILABLE` — executable/connected and authorized for the intended scope.
- `UNAVAILABLE` — evidence shows it cannot be used.
- `UNAUTHORIZED` — it may exist, but required permission/authentication is missing.
- `DEGRADED` — available but unable to provide the required evidence reliably.
- `UNKNOWN` — insufficient evidence.

`SIGNALLED` is an evidence level, not an availability state.

## Registry entry

A resolved entry should contain:

```yaml
id: terminal.local
class: TERMINAL
purpose: run project scripts
status: AVAILABLE
confidence: HIGH
authority: local-project
read_or_write: WRITE
risk_default: MEDIUM
requires_authorization: true
signals:
  - package-script:build
verification:
  method: command-probe
  result: confirmed
side_effects:
  - may start processes
rollback_or_stop: terminate process and preserve working tree
last_verified: <timestamp>
```

Do not store credentials, tokens, cookie values, private keys, or secret environment values in a registry.

## Confidence

- `HIGH` — direct observation or trusted connected adapter.
- `MEDIUM` — multiple consistent configuration signals.
- `LOW` — single weak signal or inferred presence.

Confidence does not override availability. A high-confidence `UNKNOWN` is still `UNKNOWN` until the capability is actually established.

## Capability matching

The registry maps concrete adapters to abstract orchestration classes:

| Project need | Abstract class | Registry question |
|---|---|---|
| inspect/edit files | REPOSITORY | Can YON safely read/write the project root? |
| run/build/test | TERMINAL | Can YON execute the required command? |
| interactive QA | BROWSER | Is a browser runner available and authorized? |
| repeatable checks | TEST | Which test command actually proves the criterion? |
| repository collaboration | GITHUB | Is the repository connected and writable? |
| hosted state | DEPLOYMENT | Is the provider connected and what scope is authorized? |
| database operations | DATABASE | Is a database adapter available and what risk applies? |
| visual generation/inspection | VISUAL | Is an appropriate visual capability available? |
| video/media | MEDIA | Is an appropriate media capability available? |

## Unknown-tool protocol

If orchestration needs a capability whose state is `UNKNOWN`:

1. identify the smallest safe probe;
2. execute it only if allowed by the current risk and authorization;
3. record the observation;
4. update the registry state;
5. retry selection only if the new evidence justifies it.

If the probe itself is unavailable, do not pretend the adapter exists. Use an equivalent safe path or mark the action `BLOCKED`.

## Drift

Environment profiles are snapshots. A tool can become unavailable after detection, permissions can change, or the project can change stack.

Before a high-risk or externally mutating action, refresh the relevant adapter state instead of trusting an old profile.

## Privacy

The registry is project-local operational metadata. Never copy private project paths, customer information, secrets, credentials, proprietary architecture or identifying business rules into the public YON knowledge base.