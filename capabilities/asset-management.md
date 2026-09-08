# Capability: Asset Management

**Status:** `experimental`

## Problem
Businesses need to know what operational assets exist, where they are, what state they are in, who is responsible for them, and what happened to them over time.

## When to use
Use when a product manages physical or digital assets with an identifiable lifecycle. Examples include equipment, vehicles, containers, devices, licenses, or other trackable resources.

## Core behavior
An asset should have a stable identity, current state, relevant attributes, ownership/responsibility context, and history. The product should make the next useful action obvious from the asset's current context.

## UX considerations
- Show current status prominently.
- Keep frequent actions close to the asset.
- Provide history without hiding the current state.
- Distinguish unavailable, inactive, archived, and operational states.
- Avoid forcing users to navigate through unrelated screens for common asset actions.

## Data considerations
Model stable asset identity separately from changing events/state history. Avoid destructive overwrites when history is operationally important.

## Integration points
May connect with geolocation, rentals, work orders, notifications, maintenance, documents, billing, and permissions.

## Edge cases and failures
- duplicate identifiers
- unknown location
- missing state
- asset temporarily unavailable
- archived asset referenced by historical records
- concurrent updates

## Verification
- [ ] Asset can be created and identified
- [ ] Current state is visible
- [ ] State changes are reflected correctly
- [ ] History remains coherent
- [ ] Missing/unknown data has an explicit state
- [ ] Permissions are respected

## Evidence
Generalized capability suitable for repeated SaaS workflows. It is intentionally not tied to any private implementation.

## Privacy check
No project-specific code, secrets, customer data, credentials, or proprietary business rules are included.
