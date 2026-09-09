# /yon-business-discovery

Use YON Business Discovery to understand the real operating model behind a business request before implementation.

## Instructions

1. Read `skills/yon-business-discovery/SKILL.md`.
2. Read `discovery/BUSINESS-OPERATING-ARCHETYPES.md`.
3. Read `discovery/BUSINESS-DISCOVERY-TEMPLATE.md`.
4. Start from business outcomes, participants, relationships, and real workflows.
5. Do not use the industry/category as a software template.
6. Identify only operating archetypes supported by observed signals.
7. Assign confidence to each archetype.
8. When useful, use the Universal Product Model to clarify participants, resources, actions, events, states, temporal rules, workflows, transactions, communications, documents, and boundaries.
9. Then run capability discovery by behavior and classify candidates as `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING`, or `PRODUCT-SPECIFIC`.
10. Keep domain-specific rules local unless evidence supports reuse.
11. Mark unresolved assumptions and questions explicitly.
12. Do not implement code as part of discovery.

## Output

Return:

- business outcome;
- participants and relationships;
- observed workflows;
- detected archetypes and confidence;
- resources, lifecycle, and temporal rules;
- candidate capabilities and patterns;
- genuine gaps and gap decisions;
- product-specific behavior;
- unresolved questions;
- recommended next action;
- verification implications;
- privacy check.

An archetype is a discovery hypothesis, not an automatic feature list, architecture, schema, or SaaS template.
