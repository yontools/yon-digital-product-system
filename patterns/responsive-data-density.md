# Pattern: Responsive Data Density

**Status:** `experimental`

## Problem
Desktop tables often become unreadable or operationally painful on narrow screens.

## Context
Admin panels, operational dashboards, lists with many fields, mobile-first field work.

## Solution
Preserve task-critical information while adapting representation to available space. Do not simply shrink a desktop table until it becomes unusable.

## When to use
- Users inspect or act on records across device sizes.
- A table contains more information than a narrow viewport can safely display.

## When NOT to use
- Every column is genuinely required for simultaneous comparison and the product can reasonably require a larger viewport.

## Variants
- Priority columns + expandable details.
- Responsive card/list representation.
- Horizontal scroll with preserved column semantics.
- Detail drawer/page for secondary fields.

## Trade-offs
- Reformatting can improve mobile usability but may change scanning patterns.
- Hiding columns can remove context; make secondary information discoverable.

## Accessibility
Preserve table/list semantics where appropriate, maintain logical focus order, provide accessible names for disclosure controls, and do not require hover.

## Responsive
Define explicit behavior for mobile, tablet, and desktop rather than relying on accidental CSS overflow.

## Verification
Test real data, long labels, localization, zoom, keyboard navigation, touch targets, and the primary operational task on narrow and wide viewports.

## Evidence
Generalized recurring product-design pattern; currently experimental in YON.

## Changelog
- 2026-09-09 — Initial version
