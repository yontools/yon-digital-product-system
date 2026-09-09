---
name: yon-blueprint
description: Create or refine a YON Product Blueprint from an understood product request, capability resolution, workflows, relationships, risks, and verification needs.
disable-model-invocation: true
---

# YON Product Blueprint

Create a concise decision contract between product understanding and implementation.

## Sequence

`UNDERSTAND → DISCOVER → RESOLVE → BLUEPRINT → IMPLEMENT → VERIFY`

## Required analysis

1. Define the user outcome and success criteria.
2. Identify participants, organizations, roles, and meaningful relationships.
3. Identify primary jobs and critical workflows.
4. Model core entities/resources and ownership/tenancy boundaries.
5. Model lifecycle, temporal rules, and important states.
6. Use capability discovery and resolution before selecting reusable capabilities.
7. Select recurring patterns only when they fit the actual problem.
8. Separate reusable behavior from product-specific business rules.
9. Record genuine gaps and decide `YON-CANDIDATE`, `PRODUCT-SPECIFIC`, or `NEEDS-EVIDENCE`.
10. Identify high-risk areas and proportional verification gates.
11. Define implementation order and unresolved questions.

## Blueprint rules

- A Blueprint is not an automatic architecture or database schema.
- Do not force a capability match.
- Do not turn optional capabilities into hidden requirements.
- Keep identity, role, relationship, domain behavior, and authorization conceptually distinct.
- Preserve working behavior unless the intended outcome requires change.
- Project-local instructions and constraints remain authoritative.
- Never place private source code, secrets, customer data, proprietary prompts, confidential architecture, or identifying business rules into reusable/public Blueprint knowledge.

## Output

Use `blueprints/BLUEPRINT-TEMPLATE.md` and produce:

- product outcome;
- participants and relationships;
- jobs and critical workflows;
- domain model;
- capability resolution matrix;
- pattern selection;
- minimal composition;
- product-specific behavior;
- gaps, assumptions, unresolved questions;
- risk and verification matrix;
- implementation order;
- privacy check.

A Blueprint is ready when another implementation step can proceed without guessing the intended product model or silently inventing reusable abstractions.
