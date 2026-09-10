# /yon-orchestrate

Use YON orchestration to choose and execute the smallest sufficient tool action for the current product task.

## Process

1. Read the relevant Blueprint and Execution Plan slice when present.
2. Inspect repository-local instructions and current state.
3. Define the smallest desired outcome.
4. Select the minimum tool class that can establish the needed evidence.
5. Classify risk and required authorization.
6. Execute only within approved scope.
7. Observe the real result.
8. Decide whether to correct, continue, verify, or block.
9. Record evidence and final disposition.

## Selection rules

Prefer:

- repository/filesystem for static understanding
- terminal/runtime for execution and builds
- browser/automation for real interactive behavior
- tests for repeatable acceptance evidence
- GitHub for repository collaboration and CI state
- deployment/infrastructure only when hosted state is actually relevant
- visual/media only when a meaningful visual outcome is required

Do not use a larger tool than necessary.

## Safety rules

- Inspect before mutate.
- Preserve existing behavior unless the approved outcome requires a change.
- Do not invent tool availability or results.
- HIGH-risk actions require explicit authorization and proportional verification.
- If a required tool, permission, input, or verification is unavailable, return `BLOCKED`.
- `BLOCKED` is never `PASS` or `VERIFIED`.
- Never expose secrets, private data, proprietary code, private prompts, or identifying business rules.

## Output

Return:

- objective
- selected tool and reason
- risk / authorization
- action performed
- observed result
- evidence
- next decision
- verification result
- blockers
- final disposition: `COMPLETED | BLOCKED`
