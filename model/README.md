# Universal Product Model

The Universal Product Model is YON's conceptual layer for understanding a product before deciding which reusable capabilities or product-specific behaviors are needed.

It provides a small vocabulary for describing who participates, what exists, what can happen, how things change, and under which boundaries those changes are allowed.

## Purpose

YON should be able to recognize common product structures across domains without assuming that every product is built from the same database schema, framework, architecture, or business model.

The model therefore sits **before capability composition**:

`PRODUCT → UNIVERSAL MODEL → DISCOVERY → RESOLUTION → BLUEPRINT → IMPLEMENTATION → VERIFICATION`

## Important boundary

The Universal Product Model is:

- a conceptual vocabulary;
- a reasoning aid for product discovery and blueprints;
- a way to detect relationships between reusable behaviors.

It is **not**:

- a database schema;
- an ORM model;
- an architecture generator;
- a mandatory framework;
- a universal API contract;
- a requirement that every product implement every primitive.

A primitive can be useful for understanding a product without becoming a reusable capability or a persisted entity.

## Core primitives

YON currently uses these primitives as the default vocabulary:

| Primitive | What it represents |
|---|---|
| Party | A person or organization participating in the product context. |
| Relationship | A meaningful connection between parties or between a party and a resource/context. |
| Role | A contextual responsibility or position held by a party. |
| Resource | A thing the product manages, references, allocates, or acts upon. |
| Action | Something a participant or system can intentionally do. |
| Event | Something that happened and may trigger state changes, workflows, notifications, or history. |
| State | A meaningful condition in a lifecycle. |
| Time / Temporal Rule | A time boundary, duration, schedule, recurrence, or expiration condition. |
| Workflow | A coordinated sequence of actions, states, decisions, and handoffs that produces an outcome. |
| Transaction | A meaningful exchange or commitment, such as a payment, booking, sale, rental, or other domain transaction. |
| Communication | A message or interaction used to inform, request, confirm, remind, or coordinate. |
| Document | Structured or unstructured information with a business/product purpose. |
| Permission / Boundary | Rules defining who may see, change, execute, or access something within a context. |

## Modeling rules

1. Start with the real user outcome and workflow.
2. Use primitives to clarify the product; do not model for modeling's sake.
3. Keep identity, relationship, role, and permission conceptually separate.
4. Treat lifecycle and time as first-class when they affect user outcomes.
5. Distinguish an event from an action: an action is something intended; an event records something that occurred.
6. Do not assume every resource is a physical asset or that every transaction is financial.
7. Do not force a universal primitive into the product when the concept does not materially help.
8. A universal concept does not automatically justify a reusable capability.
9. Domain semantics remain product-specific until repeated evidence supports generalization.
10. Preserve local architecture and working behavior unless a justified product decision requires change.

## Relationship to capabilities

The model describes **what kind of thing or interaction exists**. Capabilities describe **reusable product behavior around it**.

Examples:

- `Party + Relationship + Role` can inform Party & Relationship Management.
- `Resource + State + Action` can inform Asset Management or another domain capability.
- `State + Time Rule + Event` can inform Temporal States & Expiration.
- `Event + Communication` can inform Notification Orchestration.
- `Action + Workflow + Permission` can inform Workflow Engine and Roles & Permissions.
- `Transaction + Document + Event` may inform payment, billing, booking, or domain-specific capabilities when evidence supports them.

These are mappings, not automatic architecture decisions.

## Product-specific boundary

A product may introduce concepts that do not belong in the universal model. Examples include specialized domain terminology, unique regulatory rules, proprietary processes, or business-specific semantics.

YON should keep those local unless deliberate extraction demonstrates that the concept is genuinely reusable.

## Use in YON

The Universal Product Model should be consulted when:

- a product contains several participant types or relationships;
- the same person or organization can have different contextual roles;
- resources have meaningful lifecycle states;
- workflows span multiple actions or handoffs;
- timing, expiration, recurrence, or scheduling affects outcomes;
- events trigger other product behavior;
- permissions or tenancy boundaries materially affect workflows;
- capability discovery needs a stable conceptual vocabulary.

For a small change, do not create a full model unnecessarily.

## Canonical reference

See `model/UNIVERSAL-PRODUCT-MODEL.md` for the detailed reference and `model/PRODUCT-MODEL-TEMPLATE.md` for a lightweight modeling template.
