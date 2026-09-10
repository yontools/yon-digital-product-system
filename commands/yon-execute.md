# YON Execute

Execute an approved Product Blueprint through controlled implementation, runtime inspection, correction, and verification.

## Run

1. Read the approved Blueprint and project-local instructions.
2. Confirm the primary outcome, critical workflow, affected scope, success criteria, and constraints.
3. Identify dependencies and high-risk boundaries.
4. Convert the Blueprint into the smallest dependency-aware execution plan.
5. Implement in vertical slices that produce observable value.
6. Run the real product after each meaningful slice.
7. Inspect runtime, UX/UI, responsive/accessibility behavior, and relevant data/security boundaries.
8. Correct failures at the smallest responsible boundary.
9. Re-run the affected journey and relevant regression checks.
10. Apply proportional validation gates and record evidence.
11. Stop and report when a required product decision, authorization, access, or verification condition is genuinely missing.

## Execution states

Use these states for meaningful work items:

`PLANNED → IN_PROGRESS → INSPECTING → CORRECTING → VERIFIED`

If execution cannot proceed:

`IN_PROGRESS → BLOCKED`

A blocked item must state the missing condition and next action. It must not be represented as verified.

## Rules

- The Blueprint is the product decision contract; do not silently invent product behavior.
- Project-local instructions remain authoritative.
- Inspect existing code before changing it.
- Prefer reuse over unnecessary rewrites or abstractions.
- Do not broaden scope merely because a nearby improvement is visible.
- Treat auth, authorization, billing, migrations, destructive operations, security, integrations, tenancy/isolation, and core business rules as high-risk.
- Never put private source code, secrets, customer data, proprietary prompts, confidential architecture, or identifying business rules into public YON knowledge.

## Verification

Use `validation/INDEX.md` and record:

- gate;
- expected evidence;
- observed evidence;
- result;
- severity/risk;
- follow-up when needed.

Results are `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE`. `BLOCKED` is never `PASS`.

## Output

Return an execution report containing:

- Blueprint used;
- completed work items;
- current execution state;
- files/areas changed;
- runtime inspection performed;
- verification evidence and results;
- regressions or remaining risks;
- blocked decisions/conditions;
- evidence candidates for deliberate YON extraction.

Do not publish reusable knowledge automatically.
