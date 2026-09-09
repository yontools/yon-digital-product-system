# /yon-capability-resolver

## Purpose
Resolve a product requirement into the smallest evidence-aware composition of reusable YON capabilities and patterns after discovery.

## Instructions

1. Understand the product problem, users, roles, jobs, critical workflows, constraints, and existing behavior.
2. If the problem spans multiple reusable behaviors and discovery has not been performed, use `/yon-capability-discovery` first.
3. Inspect `capabilities/INDEX.md`, `capabilities/CAPABILITY-MAP.md`, individual capabilities, `patterns/INDEX.md`, relevant patterns, and evidence when available.
4. Search by behavior and workflow, not merely by product category.
5. Classify candidates as `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING`, or `PRODUCT-SPECIFIC`.
6. Check interactions between lifecycle, permissions, notifications, data ownership, tenancy, auditability, failure/recovery, and operator workflows.
7. Evaluate both capability lifecycle (`DISCOVERED`, `EXPERIMENTAL`, `PROVEN`, `DEPRECATED`) and evidence status (`UNVERIFIED`, `SUPPORTED`, `STRONG`, `CONTRADICTED`) without confusing either with classification.
8. Do not force a capability match. A genuine `MISSING` result is preferable to a fake match.
9. For each genuine gap, classify it as `YON-CANDIDATE`, `PRODUCT-SPECIFIC`, or `NEEDS-EVIDENCE`.
10. Prefer the smallest composition that fully covers the actual outcome.
11. Keep proprietary implementation details in the target project and never publish knowledge automatically.

## Output

Return:

- problem/workflow summary;
- capability resolution matrix with need, candidate, classification, maturity, evidence, coverage, gap decision, and next action;
- direct capabilities;
- supporting capabilities;
- optional capabilities;
- missing capabilities;
- product-specific requirements;
- recommended minimal composition;
- dependencies and interaction boundaries;
- unresolved questions;
- implementation order;
- verification plan;
- privacy boundary.

## Completion rule

A resolution is complete when the actual workflow is understood, reusable candidates are classified, evidence and maturity are visible, composition boundaries are explicit, genuine gaps are honest, product-specific requirements are separated, and the next implementation and verification steps are clear.
