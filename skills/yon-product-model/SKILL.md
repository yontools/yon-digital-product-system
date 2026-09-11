---
name: yon-product-model
description: Model the universal product structure before capability resolution when participants, relationships, resources, workflows, lifecycle, time, transactions, communications, or boundaries materially affect product decisions.
disable-model-invocation: true
---

# YON Product Model

Use this skill when a product is broad enough that a lightweight conceptual model will improve discovery, resolution, blueprinting, or verification.

## Purpose

Move from product understanding to a stable conceptual vocabulary without imposing architecture:

`PRODUCT → UNIVERSAL MODEL → BUSINESS GRAPH CONTEXT → DISCOVERY → RESOLUTION → BLUEPRINT`

## Process

1. Understand the user outcome, participants, jobs, workflows, constraints, and existing behavior.
2. Identify only the universal primitives that materially clarify the product: Party, Relationship, Role, Resource, Action, Event, State, Time/Temporal Rule, Workflow, Transaction, Communication, Document, Permission/Boundary.
3. Separate identity, relationship, role, and authorization.
4. Identify lifecycle and temporal behavior when they affect outcomes.
5. Distinguish intentional Actions from recorded Events.
6. When relationships materially affect routing, responsibility, access, automation, or agent decisions, use the Business Graph as contextual reasoning—not as a database prescription.
7. Keep specialized domain semantics product-specific unless evidence supports generalization.
8. Map relevant primitive combinations to existing YON capabilities and patterns.
9. Pass genuine gaps to capability discovery; do not invent a capability merely because a primitive has no mapping.
10. Use the model as input to Product Blueprint when the product is broad enough.
11. Define verification implications for important states, boundaries, workflows, temporal rules, graph relationships, and event reactions.

## Rules

- The model is conceptual, not a schema.
- It is not an architecture generator or mandatory framework.
- Do not require every product to use every primitive.
- Do not create abstractions for nouns alone.
- Do not introduce graph/database infrastructure merely because relationships exist.
- Do not create an event system merely because events sound sophisticated.
- Do not convert every repeated feature into a capability.
- Preserve working local architecture unless a justified product decision requires change.

## Graph, events, and agents

For AI-native or highly coordinated products, keep these layers distinct:

- Business Graph: relationship and context reasoning.
- Event Engine: meaningful occurrences and reactions.
- Agent System: bounded decision and action behavior.
- Orchestration: actual tool selection, authority, execution, and observation.

An event does not grant permission. A relationship does not automatically grant authorization. An agent autonomy level does not bypass policy.

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
10. graph context when materially useful;
11. capability/pattern mapping;
12. product-specific boundary;
13. risks and verification implications;
14. intentionally unmodeled concepts.

## Completion rule

The model is complete when it clarifies the important product relationships and behaviors, maps naturally into discovery/blueprint work, leaves specialized semantics local, and avoids unnecessary abstraction.
