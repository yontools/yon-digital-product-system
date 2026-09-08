# Capability: Geolocation & Tracking

**Status:** `experimental`

## Problem
Products managing mobile or physical operations need location context to know where assets or field activities are and to act on that information.

## When to use
Use when location materially affects operational decisions, dispatch, safety, service delivery, asset visibility, or customer communication.

## Core behavior
Represent location as time-aware information rather than assuming a coordinate is always current. Show last known position, timestamp, confidence/accuracy when available, and relevant operational state. Connect location to the entity users are actually trying to manage.

## UX considerations
- Show last update time, not just a pin.
- Make stale location explicit.
- Use map views when geography helps decisions; otherwise prefer simpler summaries.
- Keep status and location understandable together.
- Provide accessible non-map alternatives for critical information.

## Data considerations
Consider coordinate precision, timestamp, source, accuracy, retention, privacy, and update frequency. Avoid collecting more location data than the product needs.

## Integration points
Assets, rentals, dispatch, routes, alerts, field operations, dashboards, and audit history.

## Edge cases and failures
- GPS unavailable
- stale position
- inaccurate position
- device offline
- duplicate updates
- privacy/consent restrictions

## Verification
- [ ] Current/last-known distinction is clear
- [ ] Timestamp is visible where relevant
- [ ] Stale/offline states are handled
- [ ] Critical location information has a non-map representation
- [ ] Privacy requirements are respected

## Evidence
Generalized operational tracking capability.

## Privacy check
No project-specific code, secrets, customer data, credentials, or proprietary business rules are included.
