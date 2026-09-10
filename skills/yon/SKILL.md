---
name: yon
description: YON Digital Product System master skill. Use when designing, building, auditing, polishing, or verifying a website, landing page, SaaS, dashboard, or digital product. Apply YON's product-engineering loop, inspect the real project before changing it, discover and resolve reusable capabilities and patterns before implementation, execute approved product decisions in controlled slices, and verify the running result.
---

# YON — Master Skill

YON is a decision and execution system for AI-assisted product development. It is not a visual component library and not a prompt collection.

## Mission

Build products that are useful, understandable, efficient, resilient, accessible, and polished while avoiding unnecessary complexity.

## Operating loop

Always reason through:

`OBSERVE → UNDERSTAND → DETECT → PROPOSE → IMPLEMENT → RUN → INSPECT → CORRECT → VERIFY`

For broad products, the decision path is:

`BUSINESS DISCOVERY → PRODUCT MODEL → CAPABILITY DISCOVERY → RESOLUTION → BLUEPRINT → EXECUTION → VERIFICATION`

### OBSERVE

Inspect the repository, framework, routes, components, data flows, assets, dependencies, scripts, tests, and project instructions before changing anything.

### UNDERSTAND

Identify users, participants, roles, relationships, primary jobs, critical workflows, business constraints, success criteria, and existing behavior that must be preserved.

For broad products, first understand the **business operating model** when the request describes a real-world operation. Consult `discovery/BUSINESS-OPERATING-ARCHETYPES.md` through `yon-business-discovery` to identify reusable operating archetypes without turning the business category into a template. Then use the Universal Product Model to establish a lightweight conceptual vocabulary before capability resolution when materially useful. Consult `model/UNIVERSAL-PRODUCT-MODEL.md` and use `model/PRODUCT-MODEL-TEMPLATE.md` only when the model materially improves the work.

### DETECT

Look for:

- UX friction and unnecessary steps
- unclear hierarchy or navigation
- missing loading, empty, success, error, permission, and edge states
- responsive problems
- accessibility issues
- visual inconsistency
- performance risks
- repetitive operator work
- automation opportunities
- AI opportunities
- reusable capabilities and patterns
- meaningful participant relationships, resource lifecycles, temporal rules, and workflow boundaries

### PROPOSE

Prioritize by user impact, confidence, and effort. Do not change something merely because a framework, trend, or design pattern suggests it.

Before implementation, discover and resolve reusable knowledge:

1. Establish the business operating model when the request describes a business operation and archetypes can improve discovery. Use `yon-business-discovery`; do not infer requirements from the vertical label alone.
2. Establish the relevant product model when the product is broad enough; do not over-model.
3. Check `capabilities/INDEX.md` and `capabilities/CAPABILITY-MAP.md`.
4. For broad, unfamiliar, or ambiguous problems, use `yon-capability-discovery` to decompose the workflow and detect genuine gaps.
5. Use `yon-capability-resolver` to choose the smallest justified composition when reusable behaviors are involved.
6. Check `patterns/INDEX.md` for recurring UX/UI solutions.
7. Check `evidence/INDEX.md` when a decision depends on observations, experiments, runtime verification, regression results, or production outcomes.
8. For broad or workflow-heavy products, create or refine a Product Blueprint before implementation.
9. Classify candidates as `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING`, or `PRODUCT-SPECIFIC`.
10. Prefer proven knowledge; validate experimental knowledge before treating it as established.
11. If no reusable solution fits, record the gap instead of forcing a match.

### IMPLEMENT / EXECUTE

For an approved Blueprint, use `yon-execute` when controlled execution is useful. Convert decisions into the smallest dependency-aware work slices, implement observable value, run the real product, inspect it, correct failures, and verify each meaningful slice.

Do not treat a Blueprint as permission to invent missing product decisions. When execution reaches an unresolved critical decision, missing authorization/access, or unverifiable high-risk boundary, stop at that boundary and report it honestly.

### RUN / INSPECT / CORRECT / VERIFY

Run the actual product whenever the environment permits. Exercise affected flows, inspect browser behavior and console/runtime output, check responsive states, correct regressions, and verify the original user outcome.

Use `validation/INDEX.md` to choose the appropriate evidence gates. A check is `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE`; never treat `BLOCKED` as `PASS`.

Record meaningful findings as evidence when they can support a future reusable decision.

## Reuse engine

Before inventing a solution, check the YON capability and pattern libraries.

A capability is a reusable product behavior such as asset management, rental management, geolocation, expiration handling, notifications, roles, workflows, documents, payments, or audit history.

A pattern is a reusable solution to a recurring product/interface problem.

Evidence is the support layer for these reusable decisions. It distinguishes what was observed or verified from what is inferred. Evidence does not automatically make a solution universal or `PROVEN`.

The **Business Discovery** layer describes recurring ways businesses operate, such as service delivery, scheduling, rental, field operations, fulfillment, case management, membership, marketplace matching, approvals, or intake/assessment. These are discovery hypotheses that help YON ask better questions and find reusable capabilities. They are not vertical templates, automatic feature lists, schemas, or architectures.

The Universal Product Model is a conceptual layer after business understanding and before capability composition. It describes common primitives such as Party, Relationship, Role, Resource, Action, Event, State, Time/Temporal Rule, Workflow, Transaction, Communication, Document, and Permission/Boundary. It does not prescribe a schema, framework, architecture, or implementation.

When a validated project solution appears broadly reusable, use `/yon-extract` to create a deliberate, privacy-checked extraction candidate. Extraction is separate from publication or promotion.

Prefer `proven` solutions. Treat `experimental` solutions as candidates that require validation.

## Private-project boundary

YON may be used inside private projects. Never publish or transfer private source code, secrets, credentials, customer data, proprietary prompts, identifying business rules, or private architecture into the public YON repository.

If a private project contains a broadly reusable solution, extract only the generalized capability or pattern and only publish it deliberately.

## Project instructions

Project-local `CLAUDE.md` and repository instructions remain authoritative for project-specific constraints. Do not overwrite them with generic YON assumptions.

## High-risk changes

Treat authentication, authorization, billing, destructive operations, database migrations, security controls, external integrations, tenancy/isolation, and core business rules as high-risk. Understand existing behavior first and verify more strongly.

## Definition of done

Do not declare a task complete merely because code compiles. Confirm the affected user journey works in the running product and that important states, responsive behavior, accessibility, visual coherence, runtime errors, and relevant security boundaries have been considered.

## Supporting YON references

- Core rules: `YON.md`
- Business discovery: `discovery/BUSINESS-OPERATING-ARCHETYPES.md`
- Business discovery template: `discovery/BUSINESS-DISCOVERY-TEMPLATE.md`
- Business discovery skill: `skills/yon-business-discovery/SKILL.md`
- Universal Product Model: `model/UNIVERSAL-PRODUCT-MODEL.md`
- Product Model template: `model/PRODUCT-MODEL-TEMPLATE.md`
- Product model skill: `skills/yon-product-model/SKILL.md`
- Product Blueprint: `skills/yon-blueprint/SKILL.md`
- Execution Engine: `skills/yon-execute/SKILL.md`
- Product design: `skills/product-design/SKILL.md`
- UX: `skills/ux/SKILL.md`
- UI: `skills/ui/SKILL.md`
- SaaS: `skills/saas/SKILL.md`
- Onboarding: `skills/onboarding/SKILL.md`
- QA: `skills/qa/SKILL.md`
- Capability discovery: `skills/yon-capability-discovery/SKILL.md`
- Capability resolution: `skills/yon-capability-resolver/SKILL.md`
- Commands/workflows: `commands/`
- Reusable capabilities: `capabilities/INDEX.md`
- Reusable patterns: `patterns/INDEX.md`
- Evidence: `evidence/INDEX.md`
- Extraction: `skills/yon-extract/SKILL.md`
- Validation gates: `validation/INDEX.md`
