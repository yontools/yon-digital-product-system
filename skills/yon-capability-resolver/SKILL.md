---
name: yon-capability-resolver
description: Map product requirements to reusable YON capabilities and patterns without importing private implementation details.
disable-model-invocation: true
---

# YON Capability Resolver

Use this skill when planning or extending a digital product and deciding which reusable YON capabilities should be considered.

## Objective

Translate a product need into a small, explicit capability composition before implementation.

The resolver must answer:

1. What user/business problem is being solved?
2. Which YON capabilities are directly relevant?
3. Which capabilities are optional or only hypotheses?
4. What important capability is missing?
5. What evidence supports each recommendation?
6. What must remain product-specific rather than becoming a shared capability?

## Resolution process

### 1. Understand the product

Inspect the request, target users, workflows, constraints, existing code, and current architecture. Do not assume a capability merely because a product belongs to a familiar category.

### 2. Search YON knowledge

Inspect:

- `capabilities/README.md`
- `capabilities/CAPABILITY-MAP.md`
- individual files in `capabilities/`
- relevant files in `patterns/`
- project-local documentation and code when available

### 3. Classify matches

For every candidate capability, classify it as:

- **DIRECT** — clearly required by the described workflow.
- **SUPPORTING** — useful to enable another capability.
- **OPTIONAL** — plausible but not yet justified.
- **MISSING** — required behavior with no reusable YON capability yet.
- **PRODUCT-SPECIFIC** — should stay in the product and should not be generalized automatically.

### 4. Check composition

Capabilities can compose, but YON must not force a predefined architecture. Validate dependencies, ownership of data, lifecycle interactions, permissions, notifications, and failure states.

### 5. Produce a resolution

Return a concise matrix:

| Capability | Classification | Why | Evidence | Next action |
|---|---|---|---|---|

Then provide:

- recommended composition
- unresolved questions
- missing capabilities
- implementation order
- verification plan
- privacy boundary

## Rules

- Reuse before reinventing.
- Do not copy private project code or proprietary details into YON.
- Do not treat capability-map combinations as automatic architecture decisions.
- Prefer the smallest capability set that solves the real problem.
- A missing capability is a useful result; do not invent a fake match.
- If evidence is weak, mark the capability as experimental or optional.
- Keep business rules that are unique to one company/product inside that product.

## Example

A rental product may resolve to:

`Asset Management + Rental Management + Temporal States & Expiration`

and optionally add `Notifications` when deadline communication is a real requirement.

The resolver should still inspect the actual workflow before recommending implementation.
