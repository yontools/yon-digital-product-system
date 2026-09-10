# YON Product Blueprints

Product Blueprints are structured planning artifacts produced before implementation when a product is broad enough to benefit from explicit modeling.

A Blueprint is a **decision contract** between product understanding and implementation. It is not an automatic architecture, database schema, framework prescription, or permission to redesign working behavior.

## Purpose

A Blueprint makes the intended product decision explicit before code expands:

- primary outcome and success criteria;
- business operating context and archetypes when applicable;
- participants, roles, relationships, and boundaries;
- users, jobs, and critical workflows;
- entities/resources and lifecycle;
- temporal rules and important states;
- capabilities and patterns selected from YON;
- minimal composition and ownership boundaries;
- genuine gaps and uncertainty;
- product-specific behavior;
- tenancy, authorization, and high-risk boundaries;
- implementation order;
- verification gates;
- decisions and post-implementation evidence hooks.

## Traceability

When useful, preserve:

`BUSINESS OUTCOME → WORKFLOW → ARCHETYPE → PRODUCT PRIMITIVES → CAPABILITY / PATTERN → DECISION → VERIFICATION`

The chain is a reasoning aid, not a requirement to populate every field. If evidence is missing, record the gap instead of inventing a connection.

## Lifecycle

`REQUEST → BUSINESS DISCOVERY → PRODUCT MODEL → DISCOVERY → RESOLUTION → BLUEPRINT → EXECUTION → VERIFICATION`

For products without a meaningful business-operation context, Business Discovery may be skipped. For narrow/simple work, a full Blueprint may also be unnecessary.

After implementation, meaningful findings can flow into evidence and deliberate extraction/learning.

## Rules

1. Build from the real user/business outcome and workflow, not from a generic industry template.
2. When applicable, use the smallest combination of Business Operating Archetypes supported by behavioral evidence; archetypes are hypotheses, not automatic requirements.
3. Reuse YON knowledge before inventing new abstractions.
4. Keep identity, role, relationship, domain behavior, and authorization conceptually separate.
5. Use the Universal Product Model only where it materially clarifies the product; do not over-model.
6. Search and resolve capabilities by behavior/workflow, not by industry label.
7. Record `MISSING` honestly instead of forcing a capability match.
8. Keep product-specific business rules local unless deliberate evidence supports reuse.
9. Patterns require a real interaction problem; do not add them as decoration.
10. High-risk decisions require stronger verification.
11. Existing working behavior should not be redesigned unnecessarily.
12. Never include private source code, secrets, customer data, proprietary prompts, confidential architecture, or identifying business rules in reusable/public Blueprint knowledge.

## Execution

An approved Blueprint can be passed to `yon-execute`.

Execution follows:

`PLAN → IMPLEMENT → RUN → INSPECT → CORRECT → VERIFY`

Use vertical slices where possible. Each slice should have an expected behavior and verification evidence. Execution may stop as `BLOCKED` when a critical product decision, authorization/access condition, infrastructure dependency, or high-risk verification requirement is unresolved.

The Blueprint does not grant permission to invent missing decisions or expand scope.

## Output

Use `BLUEPRINT-TEMPLATE.md` for a consistent structure. The Blueprint should be concise enough to guide implementation while explicit enough to expose assumptions, boundaries, trade-offs, unresolved questions, and verification needs.
