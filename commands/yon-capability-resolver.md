# /yon-capability-resolver

## Purpose
Resolve a product requirement into the smallest useful composition of reusable YON capabilities and patterns before implementation.

## Instructions

1. Understand the product problem, users, roles, critical workflows, constraints, and existing behavior.
2. Inspect `capabilities/INDEX.md`, `capabilities/CAPABILITY-MAP.md`, individual capabilities, and relevant patterns.
3. Classify candidate capabilities as `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING`, or `PRODUCT-SPECIFIC`.
4. Check interactions between lifecycle, permissions, notifications, data ownership, and failure states.
5. Prefer proven capabilities; mark weak evidence as experimental.
6. Do not force a capability match when the product needs something different.
7. Keep proprietary implementation details in the target project.

## Output

Return:

- problem summary;
- capability resolution matrix;
- recommended composition;
- missing capabilities;
- unresolved questions;
- implementation order;
- verification plan;
- privacy boundary.

## Completion rule

A resolution is complete when the recommended capability set is justified by the actual workflow and the next implementation step is clear.
