# YON Product Blueprints

Product Blueprints are structured planning artifacts produced before implementation when a product is broad enough to benefit from explicit modeling.

A Blueprint is not an automatic architecture or database schema. It is a decision contract between product understanding and implementation.

## Purpose

A Blueprint makes the intended product model explicit before code expands:

- participants and relationships;
- users, roles, and jobs;
- entities and resources;
- workflows and lifecycle states;
- time-sensitive behavior;
- capabilities and patterns selected from YON;
- genuine gaps;
- product-specific behavior;
- tenancy, permissions, and high-risk boundaries;
- implementation order;
- verification gates.

## Lifecycle

`REQUEST → DISCOVERY → RESOLUTION → BLUEPRINT → IMPLEMENTATION → VERIFICATION`

After implementation, meaningful findings can flow into evidence and deliberate extraction/learning.

## Rules

1. Build from the real user outcome and workflow, not from a generic industry template.
2. Reuse YON knowledge before inventing new abstractions.
3. Keep identity, role, relationship, domain behavior, and authorization conceptually separate.
4. Record `MISSING` honestly instead of forcing a capability match.
5. Keep product-specific business rules local unless deliberate evidence supports reuse.
6. Do not treat the Blueprint as permission to redesign working behavior unnecessarily.
7. High-risk decisions require stronger verification.
8. Never include private source code, secrets, customer data, proprietary prompts, confidential architecture, or identifying business rules in reusable/public Blueprint knowledge.

## Output

Use `BLUEPRINT-TEMPLATE.md` for a consistent structure. The Blueprint should be concise enough to guide implementation while explicit enough to expose assumptions and unresolved questions.
