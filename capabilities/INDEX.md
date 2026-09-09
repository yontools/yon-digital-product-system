# YON Capability Index

Machine-oriented index of reusable product capabilities.

## How YON uses this index

Use this index to discover candidate capabilities before designing or implementing product behavior. The index is a discovery aid, not an architecture generator.

Classifications produced by the Capability Resolver:

- `DIRECT` — clearly required.
- `SUPPORTING` — enables another required behavior.
- `OPTIONAL` — plausible but not yet justified.
- `MISSING` — required behavior with no suitable capability.
- `PRODUCT-SPECIFIC` — should remain local to the product.

## Capabilities

| Name | File | Status | Domains |
|---|---|---|---|
| Party & Relationship Management | `party-relationship-management.md` | experimental | identity, relationships, organizations, roles, customers |
| Asset Management | `asset-management.md` | experimental | assets, operations |
| Audit History | `audit-history.md` | experimental | operations, compliance, debugging, security |
| Geolocation & Tracking | `geolocation-tracking.md` | experimental | location, tracking, field operations |
| Notification Orchestration | `notification-orchestration.md` | experimental | notifications, operations, communication |
| Rental Management | `rental-management.md` | experimental | rentals, resources, operations |
| Roles & Permissions | `roles-permissions.md` | experimental | security, authorization, teams, SaaS |
| Temporal States & Expiration | `temporal-states-expiration.md` | experimental | time, lifecycle, deadlines |
| Workflow Engine | `workflow-engine.md` | experimental | workflows, operations, lifecycle |

## Discovery rules

1. Start with the user's actual problem and workflow.
2. Search by domain, behavior, and lifecycle—not only by capability name.
3. Prefer `proven` capabilities when available.
4. Treat `experimental` capabilities as candidates requiring validation.
5. If no capability fits without distortion, report `MISSING` rather than forcing a match.
6. Never use this index to import private project implementation details.

## Privacy

Only generalized, reusable product knowledge belongs here. Private source code, secrets, credentials, customer data, proprietary prompts, and identifying business rules remain in their source project.
