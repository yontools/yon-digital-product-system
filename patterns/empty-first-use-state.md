# Pattern: Empty / First-Use State

**Status:** `experimental`

## Problem
An empty screen often tells the user what data is missing but not what to do next.

## Context
New accounts, empty lists, dashboards before setup, newly created workspaces.

## Solution
Make the empty state explain the current condition, show the value of the feature, and provide one clear next action when an action exists.

## When to use
- The user has not created the first resource.
- A workflow is waiting for initial configuration.
- An empty result is meaningful and actionable.

## When NOT to use
- The empty state is intentionally informational with no useful next action.
- Search/filter results are empty; use the appropriate no-results variant instead.

## Variants
- First-use onboarding state.
- Empty collection with primary CTA.
- Empty dashboard with setup checklist.
- No-results state for search/filter.

## Trade-offs
- Rich guidance can help activation but should not become a tutorial wall.
- The CTA must match the user's immediate job, not the product's internal structure.

## Accessibility
Use a clear heading and descriptive text. Ensure the primary action has an accessible name and visible focus. Do not communicate meaning by illustration alone.

## Responsive
Keep the message and primary action readable and reachable on narrow screens. Avoid oversized empty illustrations that push the useful action below the fold.

## Verification
Start from a clean state and verify that a new user can identify the next useful action without external instructions.

## Evidence
Generalized recurring product-design pattern; currently experimental in YON.

## Changelog
- 2026-09-09 — Initial version
