# YON Capabilities

Capabilities are reusable product capabilities extracted from real problems and validated implementations.

A capability is broader than a UI pattern. It describes a repeatable business/product behavior that can be composed into new systems.

## Examples

- Asset management
- Rental management
- Geolocation and tracking
- Temporal states and expiration
- Notification orchestration
- Customer management
- Roles and permissions
- Workflow management
- Document management
- Payment tracking
- Audit history
- Operational dashboards

## Lifecycle

`DISCOVERED → EXPERIMENTAL → PROVEN → DEPRECATED`

A capability should only be marked `proven` when it has evidence from real usage, testing, or repeated implementation.

## Privacy boundary

Capabilities must describe the generalized solution, not expose private project code, secrets, customer data, credentials, proprietary business rules, or identifying implementation details.

A private project can inspire a capability. Publishing the capability requires an explicit decision to extract and generalize it.

## Recommended capability structure

Each capability can document:

1. Problem
2. When to use it
3. Inputs and outputs
4. Core behavior
5. UX considerations
6. Data considerations
7. Integration points
8. Failure and edge cases
9. Verification criteria
10. Status and evidence
