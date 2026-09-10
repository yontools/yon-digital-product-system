# YON Execution Plan

Create an implementation-ready execution plan from an approved Product Blueprint.

## Use

Invoke when a Blueprint exists and the next step is controlled implementation.

## Process

1. Read the Blueprint and project-local instructions.
2. Inspect the current repository and relevant existing implementation.
3. Confirm the approved outcome, critical workflows, scope, constraints, and decisions.
4. Decompose into the smallest useful vertical slices.
5. Trace every slice to an outcome/workflow/Blueprint decision.
6. Order by dependencies, value, risk, early verification, and reuse.
7. Define observable acceptance criteria for every slice.
8. Define proportional validation checkpoints and regression surfaces.
9. Mark high-risk work explicitly.
10. Record deferred work, product-specific behavior, assumptions, blockers, and unresolved decisions.
11. Produce the execution handoff using `execution/EXECUTION-PLAN-TEMPLATE.md`.

## Rules

- Do not invent product decisions inside implementation tasks.
- Do not convert every capability or Blueprint item into a separate task when composition makes a smaller slice possible.
- Prefer vertical slices over technical-layer task dumps.
- Existing working behavior is preserved unless the Blueprint authorizes a change.
- BLOCKED is not VERIFIED.
- High-risk work requires stronger evidence before completion.
- Never put private source code, secrets, customer data, proprietary prompts, confidential architecture, or identifying business rules into reusable YON knowledge.

## Output

Return:

- execution plan identity;
- Blueprint source;
- outcome and scope;
- ordered slices and dependencies;
- acceptance criteria;
- verification checkpoints;
- risk matrix;
- deferred scope;
- blockers/unresolved decisions;
- execution handoff state.
