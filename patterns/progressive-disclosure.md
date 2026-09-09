# Pattern: Progressive Disclosure

**Status:** `experimental`

## Problem
Too much information or too many controls overwhelm users and slow primary tasks.

## Context
Complex SaaS, settings, forms, dashboards, configuration-heavy workflows.

## Solution
Expose the information and actions needed for the current decision first. Reveal secondary or advanced detail only when it becomes relevant.

## When to use
- A screen has competing primary and secondary actions.
- Advanced configuration is uncommon but important.
- Expert controls would distract first-time users.

## When NOT to use
- Users need simultaneous visibility to compare critical information.
- Hiding information would reduce trust or make a decision harder.

## Variants
- Collapsible advanced section.
- Step-based flow.
- Detail drawer or contextual panel.
- Summary first, full detail on demand.

## Trade-offs
- Less visible information can improve focus but increase discovery cost.
- Requires clear affordances and predictable disclosure.

## Accessibility
Use semantic controls, keyboard-operable disclosure, visible focus, accurate expanded/collapsed state, and meaningful labels. Do not hide critical information from assistive technology.

## Responsive
On narrow screens, prioritize the primary task and move secondary detail into drawers, accordions, or subsequent views without making critical actions inaccessible.

## Verification
Test first-time and experienced users, keyboard navigation, screen-reader semantics, and whether the primary task requires fewer cognitive steps.

## Evidence
Generalized recurring product-design pattern; currently experimental in YON.

## Changelog
- 2026-09-09 — Initial version
