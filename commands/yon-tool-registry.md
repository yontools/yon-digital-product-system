# /yon-tool-registry

Resolve the current project-local Tool Registry from the Environment Profile before substantial tool-mediated execution.

## Process

1. Read `skills/yon-tool-registry/SKILL.md`.
2. Read the current Environment Profile and project-local instructions.
3. If the profile is missing or stale, run the smallest safe environment detection required.
4. Normalize tool signals and resolve concrete adapter states.
5. Distinguish availability from authorization.
6. Map concrete adapters to abstract capability classes.
7. Record evidence, confidence, risk, side effects and freshness.
8. Mark unresolved capabilities `UNKNOWN`, `UNAVAILABLE`, `UNAUTHORIZED`, or `DEGRADED`; do not promote them to available by assumption.
9. Return the registry for `yon-orchestrate`.

## Output

Produce a concise project-local registry containing:

- environment identity
- detected stack/runtime
- concrete adapters
- abstract capability class
- status
- confidence
- authority/scope
- read/write capability
- default risk
- evidence
- verification freshness
- side effects
- blockers

Never include secrets or secret values.