# Capability: Rental Management

**Status:** `experimental`

## Problem
A rental business needs to manage agreements between customers and resources across a lifecycle: requested, assigned, active, due, overdue, returned, cancelled, or closed.

## When to use
Use when a product manages temporary possession or use of an asset, resource, space, or service with a start/end period.

## Core behavior
Represent the rental as a lifecycle with dates, parties, assigned resource, current status, and history. The system should calculate or surface upcoming deadlines and make the next operational action obvious.

## UX considerations
- Show remaining time and due state clearly.
- Make extension, return, cancellation, or escalation contextual.
- Distinguish scheduled, active, overdue, and completed rentals.
- Surface exceptions rather than requiring users to discover them manually.

## Data considerations
Keep rental records distinct from assets and customers. Store lifecycle events when auditability matters. Define timezone behavior explicitly.

## Integration points
Asset management, expiration, notifications, geolocation, contracts, billing, documents, and workflows.

## Edge cases and failures
- missing end date
- timezone boundary
- extension overlapping another reservation
- asset becomes unavailable during rental
- cancellation after activation
- late return

## Verification
- [ ] Rental lifecycle is coherent
- [ ] Dates and timezone are handled consistently
- [ ] Due/overdue state is deterministic
- [ ] Related asset/customer context is visible
- [ ] Extensions and completion preserve history

## Evidence
Generalized capability for temporary-use business processes; intentionally independent of any private project.

## Privacy check
No project-specific code, secrets, customer data, credentials, or proprietary business rules are included.
