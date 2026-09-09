---
name: yon-product-model
description: Model the universal product structure before capability resolution when participants, relationships, resources, workflows, lifecycle, time, transactions, communications, or boundaries materially affect product decisions.
disable-model-invocation: true
---

# YON Product Model

Use this skill when a product is broad enough that a lightweight conceptual model will improve discovery, resolution, blueprinting, or verification.

## Purpose

Move from product understanding to a stable conceptual vocabulary without imposing architecture:

`PRODUCT → UNIVERSAL MODEL → DISCOVERY → RESOLUTION → BLUEPRINT`

## Process

1. Understand the user outcome, participants, jobs, workflows, constraints, and existing behavior.
2. Identify only the universal primitives that materially clarify the product: Party, Relationship, Role, Resource, Action, Event, State, Time/Temporal Rule, Workflow, Transaction, Communication, Document, Permission/Boundary.
3. Separate identity, relationship, role, and authorization.
4. Identify lifecycle and temporal behavior when they affect outcomes.
5. Distinguish intentional Actions from recorded Events.
6. Keep specialized domain semantics product-specific unless evidence supports generalization.
7. Map relevant primitive combinations to existing YON capabilities and patterns.
8. Pass genuine gaps to capability discovery; do not invent a capability merely because a primitive has no mapping.
9. Use the model as input to Product Blueprint when the product is broad enough.
10. Define verification implications for important states, boundaries, workflows, and temporal rules.

## Rules

- The model is conceptual, not a schema.
- It is not an architecture generator or mandatory framework.
- Do not require every product to use every primitive.
- Do not create abstractions for nouns alone.
- Do not introduce graph/database infrastructure merely because relationships exist.
- Do not convert every repeated feature into a capability.
- Preserve working local architecture unless a justified product decision requires change.

## Output

For broad products, produce or update a lightweight Product Model using `model/PRODUCT-MODEL-TEMPLATE.md`, then provide:

1. product outcome;
2. relevant participants and relationships;
3. resources/entities;
4. meaningful actions;
5. events and state changes;
6. temporal rules;
7. workflows;
8. transactions, communications, and documents when relevant;
9. permission/tenancy boundaries;
10. capability/pattern mapping;
11. product-specific boundary;
12. risks and verification implications;
13. intentionally unmodeled concepts.

## Completion rule

The model is complete when it clarifies the important product relationships and behaviors, maps naturally into discovery/blueprint work, leaves specialized semantics local, and avoids unnecessary abstraction.
