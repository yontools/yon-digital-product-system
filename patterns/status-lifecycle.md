# Pattern: Status + Lifecycle

**Status:** `experimental`

## Problem
Users cannot act confidently when an entity's current state, next state, or timing is unclear.

## Context
Orders, rentals, assets, tickets, approvals, jobs, deliveries, subscriptions, operational records.

## Solution
Represent lifecycle state explicitly, make the current state legible, define valid transitions, and surface the next meaningful action or condition.

## When to use
- An entity changes state over time.
- Actions depend on state.
- Deadlines or transitions affect operations.

## When NOT to use
- The value is static and has no meaningful lifecycle.
- A status label would duplicate information without improving decisions.

## Variants
- Status chip + next action.
- Timeline.
- State machine visualization.
- Deadline-aware status with temporal state.

## Trade-offs
- More explicit state improves clarity but adds modeling and UI complexity.
- Do not create states merely to make a workflow look sophisticated.

## Accessibility
Never rely on color alone. Pair status color with text/icon semantics, accessible labels, and sufficient contrast.

## Responsive
Keep current state and next action visible on mobile. Move detailed history into a secondary surface when space is limited.

## Verification
Test every valid transition, invalid transition, stale data, concurrent updates, refresh, permission differences, and boundary times where relevant.

## Evidence
Generalized recurring product-design pattern; currently experimental in YON.

## Changelog
- 2026-09-09 — Initial version
