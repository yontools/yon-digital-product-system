---
name: yon-execute
description: Execute an approved YON Product Blueprint through implementation, runtime inspection, correction, and proportional verification without turning YON into a rigid architecture generator.
disable-model-invocation: true
---

# YON Execution Engine

Turn an approved Product Blueprint into a controlled implementation cycle.

The Execution Engine is an **orchestration contract**, not an autonomous permission to change anything. It connects product decisions to real implementation and evidence.

## Position in YON

`UNDERSTAND → BUSINESS DISCOVERY → PRODUCT MODEL → DISCOVER → RESOLVE → BLUEPRINT → EXECUTE → VERIFY → EVIDENCE`

## Core loop

`PLAN → IMPLEMENT → RUN → INSPECT → CORRECT → VERIFY`

Repeat the smallest useful cycle until the affected outcome is verified or execution is honestly blocked.

## Execution contract

Before changing code:

1. Read the approved Blueprint and project-local instructions.
2. Confirm the primary outcome, critical workflow, affected scope, and success criteria.
3. Identify implementation dependencies and high-risk boundaries.
4. Convert Blueprint decisions into an ordered execution plan.
5. Define the evidence required to consider each meaningful step complete.

Do not invent missing product decisions during implementation. If a decision is required and not justified by the Blueprint or project-local authority, stop at the smallest boundary and record the unresolved question.

## Execution plan

Each work item should contain:

- objective;
- Blueprint traceability;
- affected scope;
- dependencies;
- risk level;
- expected behavior;
- verification evidence;
- completion state.

Prefer vertical slices that produce observable user value over large disconnected technical batches.

## Implementation rules

- Inspect the existing implementation before modifying it.
- Reuse existing components, patterns, capabilities, and architecture when they fit.
- Do not rewrite working behavior without a justified outcome.
- Do not add dependencies, abstractions, modules, or screens solely for completeness.
- Keep product-specific rules local unless the Blueprint explicitly resolves them as reusable.
- Preserve tenancy, authorization, data boundaries, and existing integrations.
- Treat authentication, authorization, billing, migrations, destructive actions, security controls, external integrations, and core business rules as high-risk.
- Never expose or copy secrets, credentials, customer data, proprietary prompts, or confidential implementation details into reusable YON knowledge.

## Run and inspect

After each meaningful slice, run the real product as early as practical.

Inspect proportionally:

- primary workflow;
- loading, empty, success, error, permission, and recovery states;
- browser/runtime behavior;
- console and network failures;
- responsive behavior;
- keyboard/focus/semantic behavior when relevant;
- visual hierarchy and interaction feedback;
- data integrity and authorization boundaries for high-risk flows.

Source code quality alone is not runtime verification.

## Correct

When inspection finds a failure:

1. Reproduce it.
2. Identify the smallest responsible boundary.
3. Correct the cause rather than masking the symptom.
4. Re-run the affected journey.
5. Check relevant regression risk.
6. Record meaningful evidence when the finding may improve YON.

Do not silently broaden scope while fixing unrelated issues.

## Verification gate

Use `validation/INDEX.md` and select gates proportional to the risk and affected journey.

A result must be one of:

- `PASS` — expected behavior demonstrated with sufficient evidence.
- `FAIL` — expected behavior not achieved.
- `BLOCKED` — verification cannot be completed because a required condition/access/dependency is unavailable.
- `NOT_APPLICABLE` — the gate genuinely does not apply.

`BLOCKED` is never `PASS`.

## Stop conditions

Execution should pause rather than guess when:

- the Blueprint contradicts project-local instructions;
- a critical product decision is unresolved;
- a high-risk change lacks sufficient authorization or evidence;
- required access or infrastructure is unavailable;
- continuing would expand scope materially beyond the approved outcome;
- verification cannot distinguish success from failure.

## Completion

Execution is complete only when:

1. the approved outcome is implemented within scope;
2. the critical affected journey works in the running product;
3. relevant states and recovery paths are handled;
4. proportional UX/UI/accessibility/runtime/security/regression checks are complete;
5. no unresolved high-risk failure is hidden;
6. evidence supports the final disposition;
7. meaningful reusable findings are available for deliberate extraction, without publishing private information.

If completion is blocked, report the exact boundary, missing condition, impact, and next action instead of declaring success.
