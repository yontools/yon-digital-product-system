# YON Product Model

Use the Universal Product Model when a product has enough participants, relationships, resources, workflows, lifecycle, temporal rules, transactions, communications, documents, or authorization boundaries that a conceptual model will improve decisions.

## Instructions

1. Read `model/README.md` and `model/UNIVERSAL-PRODUCT-MODEL.md`.
2. Understand the actual product outcome and workflow first.
3. Use `model/PRODUCT-MODEL-TEMPLATE.md` when a written model is useful.
4. Model only primitives that materially clarify the product.
5. Keep identity, relationships, roles, and permissions separate.
6. Map relevant combinations to YON capabilities and patterns.
7. Hand unresolved reusable behavior to `yon-capability-discovery`.
8. For broad products, use the model as an input to `yon-blueprint`.
9. Keep domain-specific semantics local.
10. Define verification implications for important states, boundaries, workflows, and temporal rules.

Do not turn the model into a database schema or architecture prescription. Do not introduce abstractions merely because a concept can be generalized.

## Output

Return:

- product outcome;
- participants / relationships / roles;
- resources / entities;
- actions;
- events / states;
- temporal rules;
- workflows;
- transactions / communications / documents when relevant;
- permissions / tenancy boundaries;
- capability and pattern mapping;
- product-specific boundary;
- risks and verification;
- intentionally unmodeled concepts;
- next action.
