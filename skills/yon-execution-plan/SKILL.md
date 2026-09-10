---
name: yon-execution-plan
description: Turn an approved YON Product Blueprint into a dependency-aware, evidence-driven execution plan with vertical slices, checkpoints, acceptance criteria, and explicit blockers.
disable-model-invocation: true
---

# YON Execution Plan Engine

Turn an approved Product Blueprint into a **controlled execution plan** that can be handed to an implementation agent without silently inventing product decisions.

## Position in YON

`BLUEPRINT → EXECUTION PLAN → EXECUTE → VERIFY → EVIDENCE`

The Execution Plan is not architecture, a task dump, or permission to expand scope. It is the operational bridge between product decisions and implementation.

## Planning sequence

`READ → DECOMPOSE → TRACE → ORDER → SLICE → GATE → HANDOFF`

### 1. Read

Read the approved Blueprint, project-local instructions, repository state, existing implementation, relevant tests, and constraints.

If the Blueprint is missing a critical product decision, do not guess. Mark the plan `BLOCKED` at the smallest affected boundary.

### 2. Decompose

Break the approved outcome into the smallest coherent **vertical slices** that produce observable value. A slice may cross UI, application logic, data, integration, and tests when that is necessary to deliver the behavior.

Avoid decomposing solely by technical layer when that prevents early verification.

### 3. Trace

Every meaningful work item should trace to:

`OUTCOME → WORKFLOW → BLUEPRINT DECISION → WORK ITEM → ACCEPTANCE EVIDENCE`

If a work item has no justified trace, remove it or mark it explicitly as product-specific follow-up rather than smuggling it into scope.

### 4. Order

Order work by:

1. blocking dependencies;
2. primary user value;
3. high-risk boundaries;
4. ability to verify early;
5. reuse opportunities;
6. secondary enhancements.

Do not order by file count, folder structure, or arbitrary module sequence.

### 5. Slice

Each slice must define:

- objective;
- user-visible behavior;
- Blueprint traceability;
- prerequisites/dependencies;
- affected areas;
- implementation notes only where justified;
- acceptance criteria;
- verification gates;
- regression surface;
- risk;
- completion state.

### 6. Gate

Define a checkpoint after each meaningful slice. A checkpoint asks whether the expected behavior is actually demonstrated, not merely whether code exists.

Use proportional gates from `validation/INDEX.md`.

### 7. Handoff

Produce a plan that an execution agent can follow sequentially while preserving scope, decisions, boundaries, and stop conditions.

## Work item states

`PLANNED → READY → IN_PROGRESS → VERIFYING → VERIFIED`

If execution cannot continue:

`READY / IN_PROGRESS / VERIFYING → BLOCKED`

A blocked item must record:

- exact missing condition;
- affected outcome/workflow;
- impact;
- required decision/access/dependency;
- next action.

`BLOCKED` is never equivalent to `VERIFIED`.

## Acceptance criteria

Acceptance criteria must describe observable behavior. Prefer:

`Given → When → Then`

or a concise observable outcome.

Bad:

- "Create the orders component."

Good:

- "Given a valid customer and order items, when the operator confirms the order, then the order is persisted with the expected state and the operator can see the resulting status without refreshing."

For UI work, include important states where relevant: loading, empty, success, error, permission, responsive, keyboard/focus, and recovery.

## Risk model

Use `LOW`, `MEDIUM`, or `HIGH`.

`HIGH` includes authentication, authorization, billing, migrations, destructive actions, security controls, external integrations, tenancy/isolation, and core business rules.

High-risk items require explicit verification evidence before being marked `VERIFIED`.

## Scope control

Every plan must distinguish:

- `IN_SCOPE` — required for the approved outcome;
- `DEFERRED` — useful but intentionally postponed;
- `PRODUCT_SPECIFIC` — local behavior that must not be generalized;
- `BLOCKED` — cannot proceed without a missing condition.

Do not turn visible opportunities into scope automatically.

## Execution checkpoints

A checkpoint should answer:

1. Did the intended behavior work in the running product?
2. Did critical states behave correctly?
3. Did the change preserve relevant existing behavior?
4. Did runtime/network/console behavior remain healthy?
5. Did applicable accessibility/responsive/security checks pass?
6. Is there evidence sufficient to continue?

If the answer is no, route back to `CORRECT` rather than continuing blindly.

## Output

Use `execution/EXECUTION-PLAN-TEMPLATE.md` and return:

- plan identity and source Blueprint;
- target outcome;
- scope and explicit exclusions;
- dependency graph/order;
- vertical slices;
- acceptance criteria;
- verification checkpoints;
- risk matrix;
- blockers and unresolved decisions;
- final handoff state.

## Completion

An Execution Plan is ready when every in-scope slice has a justified Blueprint trace, clear dependencies, observable acceptance criteria, proportional verification gates, risk classification, scope boundary, and a defined next action. No critical decision is hidden inside an implementation task.
