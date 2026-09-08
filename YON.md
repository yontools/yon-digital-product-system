# YON — Core Operating System

## Identity

YON is a product-development methodology and instruction layer for AI-assisted creation and improvement of digital products.

It is not a UI kit and it is not a collection of prompts. It is a decision system.

## Mission

Help an AI and a human team build products that are useful, understandable, efficient, resilient and polished.

## Non-negotiable principles

1. Understand the product and its users before changing it.
2. Preserve working behavior unless there is a reason to change it.
3. Optimize for user outcomes, not feature count.
4. Reduce unnecessary steps, decisions and cognitive load.
5. Prefer contextual actions over hidden or distant actions.
6. Treat loading, empty, success, error, permission and edge states as first-class UX.
7. Design mobile and responsive behavior intentionally.
8. Accessibility is part of product quality, not a final pass.
9. Use visual assets when they improve communication; avoid generic decoration.
10. Validate the real running product, not only source code.
11. Never expose private project code, credentials, customer data or secrets into this public system.
12. Never make a change only because a framework, trend or pattern says it is fashionable.

## Operating loop

### 1. OBSERVE
Inspect the repository, product structure, existing UI, routes, data flows, assets, dependencies and available tooling.

### 2. UNDERSTAND
Identify users, roles, primary jobs, business rules, constraints, critical workflows and success criteria.

### 3. DETECT
Find friction, ambiguity, unnecessary steps, inconsistency, missing states, accessibility problems, visual weaknesses, performance risks, automation opportunities and product gaps.

### 4. PROPOSE
Prioritize findings by impact, confidence and effort. Explain why a change is worthwhile before implementing risky changes.

### 5. IMPLEMENT
Make the smallest coherent set of changes that produces the desired improvement. Reuse existing architecture and components when appropriate.

### 6. RUN
Start the real application and exercise the affected flows.

### 7. INSPECT
Review browser behavior, visual hierarchy, responsive states, console errors and critical interactions.

### 8. CORRECT
Fix regressions and incomplete states. Do not stop at the first successful build.

### 9. VERIFY
Confirm the original goal was achieved and existing important behavior still works.

## Decision framework

For every proposed change ask:

- What user problem does this solve?
- What evidence supports the change?
- What existing behavior could it affect?
- Can it be simpler?
- Can it happen closer to the moment of need?
- Can the system do the work automatically?
- What happens on mobile?
- What happens when data is missing or wrong?
- How will we verify the result?

## Change safety

### Low-risk
Copy refinement, spacing, obvious accessibility fixes, visual consistency, non-breaking states and isolated UI improvements.

### Medium-risk
Navigation changes, workflow changes, data presentation changes, component refactors and changes affecting multiple routes.

### High-risk
Authentication, authorization, billing, destructive actions, database migrations, security controls, external integrations and changes to core business rules.

High-risk changes require explicit understanding of the existing behavior and stronger verification.

## Completion standard

A task is not complete because the code compiles.

A task is complete when:

- the intended user outcome is improved;
- affected flows work in the running product;
- important states are handled;
- responsive behavior is acceptable;
- accessibility has been considered;
- no obvious console/runtime regression remains;
- the change is coherent with the existing product.
