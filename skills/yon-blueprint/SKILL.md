---
name: yon-blueprint
description: Create or refine a YON Product Blueprint from business discovery, product modeling, capability resolution, workflows, risks, and verification needs.
disable-model-invocation: true
---

# YON Product Blueprint

Create a concise, traceable decision contract between product understanding and implementation.

A Blueprint answers **what the product must accomplish, for whom, through which workflows, with which justified reusable behavior, and how the result will be verified**. It does not prescribe an automatic architecture, database schema, framework, or implementation style.

## Position in YON

For broad or workflow-heavy products:

`BUSINESS OPERATION → ARCHETYPES → PRODUCT MODEL → DISCOVERY → RESOLUTION → BLUEPRINT → IMPLEMENT → VERIFY`

When Business Discovery is not applicable, start from the strongest available product understanding. Do not invent archetypes merely to fill the Blueprint.

## Traceability contract

Preserve this chain wherever it materially helps decisions:

`BUSINESS OUTCOME → WORKFLOW → ARCHETYPE → PRODUCT PRIMITIVES → CAPABILITY / PATTERN → DECISION → VERIFICATION`

Every selected reusable capability should be explainable by a real behavior or workflow. Every important product decision should have an observable outcome or verification implication. Missing links are gaps to expose, not reasons to invent detail.

## Required analysis

1. Define the primary user/business outcome and measurable or observable success criteria.
2. Identify participants, organizations, roles, and meaningful relationships; keep identity, role, relationship, and authorization distinct.
3. Identify primary jobs and critical workflows, including triggers, handoffs, decisions, outcomes, and failure/recovery paths where relevant.
4. When the request describes a real-world operation, use Business Discovery and record detected archetypes with confidence and behavioral justification. Archetypes are context, not automatic requirements.
5. Use the Universal Product Model only where it materially clarifies parties, relationships, resources, actions, events, states, temporal rules, workflows, transactions, communications, documents, or boundaries. Do not over-model.
6. Use capability discovery and resolution before selecting reusable capabilities. Search by behavior/workflow, not by industry label.
7. Select recurring patterns only when they solve a demonstrated interaction problem.
8. Classify every capability match as `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING`, or `PRODUCT-SPECIFIC` and preserve maturity/evidence context.
9. For genuine `MISSING` behavior, choose only `YON-CANDIDATE`, `PRODUCT-SPECIFIC`, or `NEEDS-EVIDENCE`; never force a reusable match.
10. Separate reusable behavior from product-specific business rules and domain semantics.
11. Define the **minimal composition**: what is required, what supports it, what is deliberately excluded, and where ownership/boundaries sit.
12. Identify dependencies, assumptions, unresolved questions, and high-risk boundaries.
13. Define implementation order by dependency, user value, risk, and verification—not by feature-count or arbitrary module order.
14. Define proportional verification gates for the primary journey and relevant UX, UI, accessibility, runtime, security, and regression risks.

## Blueprint rules

- The Blueprint is a decision contract, not automatic architecture, schema, or code generation instructions.
- Do not turn an archetype into a feature list.
- Do not turn an optional capability into a hidden requirement.
- Do not add abstractions solely because they look reusable.
- Preserve existing working behavior unless the intended outcome or explicit decision requires change.
- Project-local instructions, constraints, data boundaries, and approved product decisions remain authoritative.
- High-risk areas require explicit evidence and stronger verification.
- If information is uncertain, label it as an assumption, unresolved question, low-confidence archetype, or `NEEDS-EVIDENCE` rather than presenting inference as fact.
- A Blueprint may intentionally be incomplete when the correct next step is discovery, validation, or a product-specific decision.
- Never place private source code, secrets, customer data, proprietary prompts, confidential architecture, or identifying business rules into reusable/public Blueprint knowledge.

## Output

Use `blueprints/BLUEPRINT-TEMPLATE.md` and produce:

- product outcome and success criteria;
- participants, roles, relationships, and boundaries;
- business archetypes and confidence when applicable;
- primary jobs and critical workflows;
- domain/product primitives and lifecycle/temporal rules;
- capability resolution with maturity/evidence and classification;
- pattern selection and rationale;
- minimal reusable composition and ownership boundaries;
- product-specific behavior;
- genuine gaps, assumptions, and unresolved questions;
- risk and verification matrix;
- dependency-aware implementation order;
- privacy check;
- post-implementation evidence hooks.

## Completion rule

A Blueprint is ready when the primary outcome and critical workflow are sufficiently understood to guide implementation without guessing; participants and relationships are explicit; archetype context is justified when used; reusable capabilities/patterns are traceable and classified; product-specific behavior is separated; gaps and uncertainty are honest; high-risk areas have verification gates; and implementation order is clear.
