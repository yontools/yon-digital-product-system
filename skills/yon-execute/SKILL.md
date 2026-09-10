---
name: yon-execute
description: Execute an approved YON Product Blueprint through an evidence-driven execution plan, implementation, runtime inspection, correction, and proportional verification without turning YON into a rigid architecture generator.
disable-model-invocation: true
---

# YON Execution Engine

Turn an approved Product Blueprint into controlled implementation through a dependency-aware Execution Plan.

The Execution Engine is an **orchestration contract**, not an autonomous permission to change anything. It connects product decisions to executable work, runtime evidence, correction, and verification.

## Position in YON

`UNDERSTAND → BUSINESS DISCOVERY → PRODUCT MODEL → DISCOVER → RESOLVE → BLUEPRINT → EXECUTION PLAN → EXECUTE → VERIFY → EVIDENCE`

## Core loop

`PLAN → IMPLEMENT → RUN → INSPECT → CORRECT → VERIFY`

The plan is the operational handoff. Use `yon-execution-plan` and `execution/EXECUTION-PLAN-TEMPLATE.md` before substantial implementation when a Blueprint contains multiple meaningful work items.

## Execution contract

Before changing code:

1. Read the approved Blueprint and project-local instructions.
2. Confirm the primary outcome, critical workflow, affected scope, success criteria, and constraints.
3. Identify dependencies and high-risk boundaries.
4. Create or read the dependency-aware Execution Plan.
5. Confirm each work item has Blueprint traceability, observable acceptance criteria, risk, dependencies, and verification evidence.
6. Execute the smallest ready vertical slice.

Do not invent missing product decisions during implementation. If a decision is required and not justified by the Blueprint or project-local authority, stop at the smallest boundary and record the unresolved question.

## Execution states

Plan states:

`PLANNED → READY → IN_PROGRESS → VERIFYING → VERIFIED`

Execution states:

`PLANNED → IN_PROGRESS → INSPECTING → CORRECTING → VERIFIED`

If execution cannot proceed:

`IN_PROGRESS / VERIFYING → BLOCKED`

A blocked item must state the missing condition and next action. It must not be represented as verified.

## Implementation rules

- Inspect the existing implementation before modifying it.
- Reuse existing components, patterns, capabilities, and architecture when they fit.
- Do not rewrite working behavior without a justified outcome.
- Do not add dependencies, abstractions, modules, or screens solely for completeness.
- Keep product-specific rules local unless the Blueprint explicitly resolves them as reusable.
- Preserve tenancy, authorization, data boundaries, and existing integrations.
- Treat authentication, authorization, billing, migrations, destructive actions, security controls, external integrations, tenancy/isolation, and core business rules as high-risk.
- Never expose or copy secrets, credentials, customer data, proprietary prompts, or confidential implementation details into reusable YON knowledge.

## Vertical-slice execution

Prefer work that can be demonstrated end-to-end. A slice may cross UI, application logic, data, integration, and tests when required to deliver the approved behavior.

After each meaningful slice:

1. Run the real product.
2. Exercise its acceptance criteria.
3. Inspect runtime behavior and critical states.
4. Correct failures at the smallest responsible boundary.
5. Re-run the affected journey and relevant regression checks.
6. Record evidence.

Do not wait until the end to discover that an early assumption was wrong.

## Run and inspect

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
- a required plan dependency is unresolved;
- a high-risk change lacks sufficient authorization or evidence;
- required access or infrastructure is unavailable;
- continuing would expand scope materially beyond the approved outcome;
- verification cannot distinguish success from failure.

## Completion

Execution is complete only when:

1. the approved outcome is implemented within scope;
2. all required in-scope plan slices are verified or an explicit final blocker is reported;
3. the critical affected journey works in the running product;
4. relevant states and recovery paths are handled;
5. proportional UX/UI/accessibility/runtime/security/regression checks are complete;
6. no unresolved high-risk failure is hidden;
7. evidence supports the final disposition;
8. meaningful reusable findings are available for deliberate extraction, without publishing private information.

If completion is blocked, report the exact boundary, missing condition, impact, and next action instead of declaring success.
