# YON Product Composition Guide

## Purpose

Provide a domain-neutral way to decompose products into reusable behaviors without turning YON into a vertical-specific application.

## Core composition layers

When a new product is requested, inspect these layers before inventing modules:

1. **Parties** — people and organizations participating in the product.
2. **Relationships** — how parties relate to each other or to an organization/context.
3. **Roles & permissions** — what each participant is allowed to do.
4. **Resources** — things being managed, scheduled, assigned, delivered, rented, or tracked.
5. **Transactions** — commercial or operational exchanges such as payments, charges, reservations, or documents when required.
6. **Workflows** — stateful processes and handoffs.
7. **Time** — schedules, deadlines, expirations, availability, and temporal rules.
8. **Communication** — notifications, reminders, messages, and delivery channels.
9. **Traceability** — audit history and meaningful historical events.

These are decomposition dimensions, not a mandatory architecture and not nine mandatory capabilities.

## Relationship-first reasoning

Start with who participates and what outcome they are trying to achieve. Then determine:

`PARTIES → RELATIONSHIPS → ROLES → RESOURCES → WORKFLOWS → TIME → TRANSACTIONS → COMMUNICATION → TRACEABILITY`

Not every product uses every layer. Omit layers that are not justified by the actual workflow.

## Examples

### Service business

A service business may involve:

`Person/Organization → Customer relationship → Professional role → Service/resource → Appointment workflow → Availability/time → Payment → Reminder → History`

The domain-specific meaning of "service", "professional", or "appointment" remains product-level unless reusable evidence supports a capability.

### Rental business

A rental workflow may involve:

`Customer/Organization → Rental relationship → Operator role → Asset → Rental lifecycle → Expiration → Charge/payment → Deadline notification → Audit history`

The existing YON capabilities should be reused where their documented scope matches.

### Field operation

A field workflow may involve:

`Parties → Customer/operator relationship → Permissions → Asset → Location-aware workflow → Time/deadline → Notifications → Audit history`

## Decision rules

- Do not create a capability for every noun in the model.
- Create or reuse capabilities around repeatable product behavior and outcomes.
- Keep identity separate from contextual role.
- Keep relationship semantics explicit.
- Keep domain behavior owned by the capability that actually governs it.
- If a layer is required but no capability exists, report a gap rather than inventing a match.
- If a gap appears reusable across products, send it through `yon-extract`; do not publish automatically.

## Resolver guidance

The resolver should use this guide to ask:

- Who participates?
- What relationships exist?
- What can each participant do?
- What is being managed or exchanged?
- What changes state?
- What depends on time?
- What triggers communication?
- What must be auditable?
- Which of these behaviors already have YON coverage?
- Which remain product-specific?

The answers form the product's capability composition; they do not dictate its database schema, framework, or UI architecture.

## Privacy

This guide is intentionally domain-neutral. Never populate it with private project names, customer data, proprietary implementation details, secrets, or identifying business rules.
