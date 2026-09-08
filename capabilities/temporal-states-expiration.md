# Capability: Temporal States & Expiration

**Status:** `experimental`

## Problem
Operational systems often depend on time. Users need to know not only what state something is in, but when that state changes and what action is required before or after a deadline.

## When to use
Use when an entity has a meaningful start, deadline, grace period, expiration, SLA, or time-based transition.

## Core behavior
Derive deterministic states from timestamps and business-defined thresholds. Surface the current state, remaining time when useful, and the next required action. Time-based transitions should be consistent across UI, notifications, and backend logic.

## UX considerations
- Never rely on color alone to communicate urgency.
- Show human-readable timing where it helps decisions.
- Make imminent deadlines visible without creating noise.
- Explain what happens when a deadline passes.

## Data considerations
Define timezone, clock source, precision, and boundary conditions. Prefer server-authoritative time for business-critical transitions.

## Integration points
Rentals, bookings, subscriptions, SLAs, tasks, notifications, billing, workflows, and dashboards.

## Edge cases and failures
- clock/timezone differences
- exactly-at-deadline behavior
- missing timestamps
- paused lifecycle
- extended deadline
- notification delivery failure

## Verification
- [ ] State transitions are deterministic
- [ ] Boundary times are tested
- [ ] Timezone behavior is explicit
- [ ] UI communicates urgency accessibly
- [ ] Notifications match the underlying state

## Evidence
Generalized time-driven workflow capability.

## Privacy check
No project-specific code, secrets, customer data, credentials, or proprietary business rules are included.
