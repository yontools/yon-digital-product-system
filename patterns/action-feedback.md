# Pattern: Action Feedback

**Status:** `experimental`

## Problem
Users need to know whether an action was accepted, is processing, succeeded, failed, or requires attention.

## Context
Forms, saves, uploads, background jobs, mutations, integrations, destructive actions.

## Solution
Reflect the action lifecycle in the interface. Give immediate acknowledgement, show progress when meaningful, confirm success, and provide recovery-oriented errors.

## When to use
- An action changes data or triggers work.
- Completion is not instantaneous.
- Failure can leave the user uncertain about what happened.

## When NOT to use
- A purely local interaction is self-evident and instantaneous.
- Extra feedback would create noise without reducing uncertainty.

## Variants
- Inline status.
- Button pending state.
- Toast for lightweight confirmation.
- Persistent activity/status for long-running work.

## Trade-offs
- Too little feedback creates uncertainty; too much creates noise.
- Transient feedback should not be the only place critical information appears.

## Accessibility
Announce important status changes appropriately, preserve focus, provide non-color indicators, and ensure loading states do not trap keyboard or screen-reader users.

## Responsive
Feedback should remain close to the triggering action on small screens and must not be hidden behind hover-only interactions.

## Verification
Test slow networks, duplicate clicks, failures, retries, refresh during processing, and successful completion. Verify that the user can distinguish all meaningful states.

## Evidence
Generalized recurring product-design pattern; currently experimental in YON.

## Changelog
- 2026-09-09 — Initial version
