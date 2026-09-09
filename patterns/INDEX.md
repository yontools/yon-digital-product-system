# YON Pattern Index

Machine-oriented discovery index for reusable product patterns.

## Selection

Classify matches as `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING`, or `PRODUCT-SPECIFIC`. Pattern status indicates evidence strength; it does not force selection.

| Pattern | File | Status | Typical signals |
|---|---|---|---|
| Progressive Disclosure | `progressive-disclosure.md` | experimental | complexity, settings, advanced options |
| Empty / First-Use State | `empty-first-use-state.md` | experimental | empty lists, new accounts, first action |
| Action Feedback | `action-feedback.md` | experimental | save, submit, mutation, async action |
| Status + Lifecycle | `status-lifecycle.md` | experimental | states, workflows, pending, active, expired |
| Confirmation for Risky Actions | `risky-action-confirmation.md` | experimental | delete, revoke, cancel, irreversible action |
| Responsive Data Density | `responsive-data-density.md` | experimental | tables, dashboards, mobile operations |

## Rules

1. Prefer the smallest pattern set that solves the user problem.
2. Combine patterns only when their responsibilities are distinct.
3. If no pattern fits, report `MISSING` rather than forcing one.
4. Keep domain-specific rules in the product, not in a generic pattern.
5. Validate experimental patterns before treating them as proven.

## Privacy

This index contains generalized knowledge only. Do not add private implementation details or customer data.
