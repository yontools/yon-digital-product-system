# /yon-capability-discovery

## Purpose
Discover reusable YON capabilities and patterns from a real product problem, identify genuine gaps, and separate reusable knowledge from product-specific requirements before implementation.

## Instructions

1. Inspect the actual product problem, users, roles, workflows, constraints, and relevant existing behavior.
2. Decompose the workflow into actors, relationships, entities, lifecycle, time rules, communications, permissions, ownership, documents/payments when relevant, handoffs, and critical states.
3. Search `capabilities/INDEX.md`, `capabilities/CAPABILITY-MAP.md`, individual capabilities, `patterns/INDEX.md`, relevant patterns, and evidence when available.
4. Search by behavior and workflow, not merely by product category or nouns.
5. Classify each candidate as exactly one of `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING`, or `PRODUCT-SPECIFIC`.
6. Do not force a match. A `MISSING` result is preferable to a fake capability match.
7. For each genuine missing behavior, decide whether it is a `YON-CANDIDATE`, `PRODUCT-SPECIFIC`, or `NEEDS-EVIDENCE`.
8. Check composition interactions involving ownership, lifecycle, permissions, notifications, auditability, failure/recovery, and operator workflows.
9. Treat the capability map as a discovery aid, not an automatic architecture.
10. Do not create, publish, or promote reusable knowledge automatically.
11. Preserve the privacy boundary: never copy private code, secrets, customer data, proprietary prompts, confidential architecture, or identifying business rules into YON.

## Output

Return:

- problem/workflow summary;
- discovery matrix with need, candidate, classification, coverage, evidence, gap decision, and next action;
- direct capabilities;
- supporting capabilities;
- optional capabilities;
- missing capabilities;
- product-specific requirements;
- recommended composition;
- implementation order;
- verification plan;
- unresolved questions;
- privacy boundary.

## Completion rule

Discovery is complete when the workflow has been decomposed, reusable knowledge has been searched, candidates are explicitly classified, genuine gaps are identified without invention, product-specific boundaries are clear, and the next implementation step is justified.
