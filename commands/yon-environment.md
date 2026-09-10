# /yon-environment

Create or refresh a YON Environment Profile for the current project.

## Process

1. Read `skills/yon-environment/SKILL.md`.
2. Read `environment/DETECTION-RULES.md` and `environment/ENVIRONMENT-PROFILE-TEMPLATE.md`.
3. Identify the project root and local instructions.
4. Inspect manifests, lockfiles, scripts, test/browser configuration and deployment signals.
5. Detect candidate tools from repository signals.
6. Safely verify actual executable/tool availability when required.
7. Separate availability from authorization.
8. Record evidence, confidence and blockers without exposing secrets.
9. Produce/update the environment profile.
10. Hand the profile to `yon-orchestrate` for tool selection.

## Rules

- Do not invent tools, frameworks, permissions or deployment state.
- `DOCUMENTED ≠ AVAILABLE`.
- Prefer read-only detection.
- Never print secret values.
- Do not install dependencies, deploy, migrate, delete or mutate production state as part of detection.
- If a critical condition remains unknown, use `NEEDS SAFE DETECTION` or `BLOCKED`, not `READY FOR ACTION`.
