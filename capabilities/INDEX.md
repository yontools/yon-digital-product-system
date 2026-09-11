# YON Capability Index

Machine-oriented index of reusable product capabilities.

## How YON uses this index

Use this index to discover candidate capabilities before designing or implementing product behavior. The index is a discovery aid, not an architecture generator.

Classifications produced by Discovery/Resolver:

- `DIRECT` — clearly required.
- `SUPPORTING` — enables another required behavior.
- `OPTIONAL` — plausible but not yet justified.
- `MISSING` — required behavior with no suitable capability.
- `PRODUCT-SPECIFIC` — should remain local to the product.

## Capabilities

| Name | File | Status | Domains |
|---|---|---|---|
| Party & Relationship Management | `party-relationship-management.md` | experimental | identity, relationships, organizations, participants, memberships |
| Asset Management | `asset-management.md` | experimental | assets, operations |
| Audit History | `audit-history.md` | experimental | operations, compliance, debugging, security |
| Business Graph & Relationship Context | conceptual layer | experimental | relationships, context, routing, agents |
| Event-driven Coordination | conceptual layer | experimental | events, workflows, reactions, automation |
| Geolocation & Tracking | `geolocation-tracking.md` | experimental | location, tracking, field operations |
| Notification Orchestration | `notification-orchestration.md` | experimental | notifications, operations, communication |
| Rental Management | `rental-management.md` | experimental | rentals, resources, operations |
| Roles & Permissions | `roles-permissions.md` | experimental | security, authorization, teams, SaaS |
| Temporal States & Expiration | `temporal-states-expiration.md` | experimental | time, lifecycle, deadlines |
| Workflow Engine | `workflow-engine.md` | experimental | workflows, operations, lifecycle |
| Agentic Operations & Bounded Autonomy | conceptual layer | experimental | AI agents, automation, tools, approvals |

## Discovery rules

1. Start with the user's actual problem and workflow.
2. Search by domain, behavior, and lifecycle—not only by capability name.
3. Prefer `proven` capabilities when available.
4. Treat `experimental` capabilities as candidates requiring validation.
5. If no capability fits without distortion, report `MISSING` rather than forcing a match.
6. Never use this index to import private project implementation details.

## Relationship principle

Participants are reusable across contexts; roles and relationships are contextual. Authorization remains a separate concern. Domain capabilities should reference participants rather than duplicate participant semantics.

## Graph, events, and agents

These three concepts are related but must remain distinct:

- **Business Graph** provides relationship context.
- **Event Engine** records meaningful occurrences and coordinates reactions.
- **Agent System** provides bounded decision and action behavior.

None of them independently grants authorization or dictates technical architecture.

## Privacy

Only generalized, reusable product knowledge belongs here. Private source code, secrets, credentials, customer data, proprietary prompts, and identifying business rules remain in their source project.
