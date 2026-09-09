# YON Business Discovery

The Business Discovery layer helps YON understand what a business actually does before deciding what software it needs.

It works from **operating behavior**, not vertical labels.

A request such as "build a system for a car wash" is therefore not treated as a car-wash template. YON investigates the real operation and may discover service delivery, scheduling, intake, payments, notifications, customer relationships, staff assignment, inventory, recurring visits, or other behaviors.

## Core idea

`BUSINESS REQUEST → OBSERVE OPERATION → IDENTIFY ARCHETYPES → MODEL WORKFLOWS → DISCOVER CAPABILITIES → RESOLVE COMPOSITION`

A **Business Operating Archetype** is a reusable discovery hypothesis describing a recurring way a business operates.

It is **not**:

- a vertical template;
- an automatic feature list;
- an architecture;
- a database schema;
- a fixed SaaS package;
- proof that a capability is required.

## Why this layer exists

The Universal Product Model describes common product primitives. Capabilities describe reusable product behaviors. Business Discovery sits between the real-world business and those reusable building blocks.

It answers questions such as:

- What is the business actually trying to accomplish?
- Who participates and how do they relate?
- What starts the work?
- What resource, service, case, order, or commitment moves through the operation?
- What decisions and handoffs occur?
- What has to happen next, and by when?
- Which operating archetypes are actually present?
- Which YON capabilities support those behaviors?
- What remains product-specific?

## Initial archetype library

See `BUSINESS-OPERATING-ARCHETYPES.md` for the initial compact library:

- Service Delivery
- Appointment & Scheduling
- Request → Order → Execution
- Reservation & Allocation
- Rental & Temporary Use
- Asset & Field Operations
- Recurring Service & Renewal
- Commerce & Fulfillment
- Case / Ticket / Work Management
- Membership & Subscription
- Marketplace & Matching
- Approval & Authorization
- Intake → Assessment → Decision → Follow-up
- Document & Compliance Lifecycle
- Event / Session Operations

The list is intentionally small. New archetypes require evidence and should not be created merely because a vertical has a different name.

## Discovery rules

1. Start with the business outcome and actual workflow.
2. Treat the business category as a clue, never as the model.
3. Identify one or more operating archetypes only when their behavioral signals are present.
4. An operation may combine multiple archetypes.
5. One archetype may map to multiple capabilities.
6. One capability may support multiple archetypes.
7. Keep domain-specific rules local unless there is evidence they generalize.
8. Record uncertainty instead of inventing requirements.
9. Validate important assumptions with the real workflow and users.
10. Never expose private project details while extracting reusable knowledge.

## Output

A discovery should produce:

1. business outcome;
2. participants and relationships;
3. observed workflows;
4. detected archetypes with confidence;
5. relevant resources and lifecycle;
6. time/temporal rules;
7. candidate capabilities and patterns;
8. gaps;
9. product-specific behavior;
10. unresolved questions;
11. recommended next step.

Use `BUSINESS-DISCOVERY-TEMPLATE.md` for a structured result.
