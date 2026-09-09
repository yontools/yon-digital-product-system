---
name: yon
description: YON Digital Product System master skill. Use when designing, building, auditing, polishing, or verifying a website, landing page, SaaS, dashboard, or digital product. Apply YON's product-engineering loop, inspect the real project before changing it, resolve reusable capabilities and patterns before implementation, and verify the running result.
---

# YON — Master Skill

YON is a decision system for AI-assisted product development. It is not a visual component library and not a prompt collection.

## Mission

Build products that are useful, understandable, efficient, resilient, accessible, and polished while avoiding unnecessary complexity.

## Operating loop

Always reason through:

`OBSERVE → UNDERSTAND → DETECT → PROPOSE → IMPLEMENT → RUN → INSPECT → CORRECT → VERIFY`

### OBSERVE

Inspect the repository, framework, routes, components, data flows, assets, dependencies, scripts, tests, and project instructions before changing anything.

### UNDERSTAND

Identify users, roles, primary jobs, critical workflows, business constraints, success criteria, and existing behavior that must be preserved.

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

### PROPOSE

Prioritize by user impact, confidence, and effort. Do not change something merely because a framework, trend, or design pattern suggests it.

Before implementation, resolve reusable knowledge:

1. Check `capabilities/INDEX.md` and `capabilities/CAPABILITY-MAP.md`.
2. Use the capability resolver when the product need spans multiple reusable behaviors.
3. Check `patterns/INDEX.md` for recurring UX/UI solutions.
4. Check `evidence/INDEX.md` when a decision depends on observations, experiments, runtime verification, regression results, or production outcomes.
5. Classify candidates as `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING`, or `PRODUCT-SPECIFIC`.
6. Prefer proven knowledge; validate experimental knowledge before treating it as established.
7. If no reusable solution fits, record the gap instead of forcing a match.

### IMPLEMENT

Make the smallest coherent change that solves the problem. Reuse existing architecture and components where appropriate.

### RUN / INSPECT / CORRECT / VERIFY

Run the actual product whenever the environment permits. Exercise affected flows, inspect browser behavior and console/runtime output, check responsive states, correct regressions, and verify the original user outcome.

Use `validation/INDEX.md` to choose the appropriate evidence gates. A check is `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE`; never treat `BLOCKED` as `PASS`.

Record meaningful findings as evidence when they can support a future reusable decision.

## Reuse engine

Before inventing a solution, check the YON capability and pattern libraries.

A capability is a reusable product behavior such as asset management, rental management, geolocation, expiration handling, notifications, roles, workflows, documents, payments, or audit history.

A pattern is a reusable solution to a recurring product/interface problem.

Evidence is the support layer for these reusable decisions. It distinguishes what was observed or verified from what is inferred. Evidence does not automatically make a solution universal or `PROVEN`.

When a validated project solution appears broadly reusable, use `/yon-extract` to create a deliberate, privacy-checked extraction candidate. Extraction is separate from publication or promotion.

Prefer `proven` solutions. Treat `experimental` solutions as candidates that require validation.

## Private-project boundary

YON may be used inside private projects. Never publish or transfer private source code, secrets, credentials, customer data, proprietary prompts, identifying business rules, or private architecture into the public YON repository.

If a private project contains a broadly reusable solution, extract only the generalized capability or pattern and only publish it deliberately.

## Project instructions

Project-local `CLAUDE.md` and repository instructions remain authoritative for project-specific constraints. Do not overwrite them with generic YON assumptions.

## High-risk changes

Treat authentication, authorization, billing, destructive operations, database migrations, security controls, external integrations, and core business rules as high-risk. Understand existing behavior first and verify more strongly.

## Definition of done

Do not declare a task complete merely because code compiles. Confirm the affected user journey works in the running product and that important states, responsive behavior, accessibility, visual coherence, runtime errors, and relevant security boundaries have been considered.

## Supporting YON references

- Core rules: `YON.md`
- Product design: `skills/product-design/SKILL.md`
- UX: `skills/ux/SKILL.md`
- UI: `skills/ui/SKILL.md`
- SaaS: `skills/saas/SKILL.md`
- Onboarding: `skills/onboarding/SKILL.md`
- QA: `skills/qa/SKILL.md`
- Commands/workflows: `commands/`
- Reusable capabilities: `capabilities/INDEX.md`
- Reusable patterns: `patterns/INDEX.md`
- Evidence: `evidence/INDEX.md`
- Extraction: `skills/yon-extract/SKILL.md`
- Validation gates: `validation/INDEX.md`
