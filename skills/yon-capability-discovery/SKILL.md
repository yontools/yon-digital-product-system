---
name: yon-capability-discovery
description: Discover reusable YON capabilities and patterns from a real product problem, identify genuine gaps, and separate reusable knowledge from product-specific requirements.
disable-model-invocation: true
---

# YON Capability Discovery

Use this skill before implementation when the product problem may be solved by composing reusable YON capabilities.

## Objective

Move from a real product problem to an evidence-aware capability map:

`PROBLEM → EXISTING CAPABILITIES → EXISTING PATTERNS → GAPS → COMPOSITION → IMPLEMENTATION`

Discovery is broader than resolution. Resolution chooses the best current composition; discovery searches for what may exist, what is missing, and what should remain product-specific.

## Process

### 1. Understand the actual problem

Inspect the request, users, roles, jobs, workflows, constraints, existing behavior, and relevant project documentation/code when available.

Start from behaviors and outcomes, not the product category. A "barbershop", "clinic", or "laundry" is not itself a capability.

### 2. Decompose the workflow

Identify:

- actors and relationships;
- primary jobs and outcomes;
- entities/assets involved;
- lifecycle/state transitions;
- time or expiration rules;
- communications and notifications;
- permissions and ownership;
- payments or documents when relevant;
- operational handoffs;
- critical success, failure, empty, loading, and edge states.

### 3. Discover reusable knowledge

Inspect, in order:

1. `capabilities/INDEX.md`
2. `capabilities/CAPABILITY-MAP.md`
3. relevant capability files
4. `patterns/INDEX.md`
5. relevant pattern files
6. `evidence/INDEX.md` and linked evidence when available

Search by behavior, not only by nouns. For example, "deadline-driven rental" may reveal temporal expiration and notifications even when the requested product is called something else.

### 4. Classify every candidate

Use exactly one classification per candidate:

- **DIRECT** — required by the actual workflow and substantially covered by an existing reusable capability.
- **SUPPORTING** — enables a direct capability or important workflow without being the primary outcome.
- **OPTIONAL** — plausible and useful, but not justified by current requirements.
- **MISSING** — the workflow requires reusable behavior for which YON has no adequate capability.
- **PRODUCT-SPECIFIC** — important to the product but intentionally should remain local because it is unique, domain-specific, or not sufficiently generalizable.

Do not label a capability DIRECT merely because it is adjacent to the domain.

### 5. Detect genuine gaps

A gap is genuine only when:

1. the behavior is required or strongly implied by the workflow;
2. existing YON capabilities do not adequately cover it;
3. composing existing capabilities would not solve it without inventing substantial new semantics.

For each MISSING item, decide:

- `YON-CANDIDATE` — likely reusable across multiple products and worth an extraction candidate;
- `PRODUCT-SPECIFIC` — should stay local;
- `NEEDS-EVIDENCE` — potentially reusable, but insufficient evidence exists.

Discovery never publishes a new capability automatically.

### 6. Check composition

For the proposed set, inspect interactions between:

- data ownership;
- relationships and tenancy;
- lifecycle/state transitions;
- permissions;
- notifications;
- audit history;
- failure and recovery paths;
- responsive/operator workflows.

The capability map is a discovery aid, not an automatic architecture.

### 7. Produce the discovery matrix

Return:

| Need / behavior | Candidate | Classification | Coverage | Evidence | Gap decision | Next action |
|---|---|---|---|---|---|---|

Then provide:

1. problem and workflow summary;
2. direct capabilities;
3. supporting capabilities;
4. optional capabilities;
5. missing capabilities;
6. product-specific requirements;
7. recommended composition;
8. implementation order;
9. verification plan;
10. unresolved questions;
11. privacy boundary.

## Evidence rules

- Prefer knowledge with stronger evidence.
- `EXPERIMENTAL` knowledge is usable as a hypothesis and should be validated when material to the product.
- `PROVEN` knowledge can be preferred when its documented scope matches the problem.
- Absence of evidence is not evidence that a capability does not work; distinguish `MISSING` from `NEEDS-EVIDENCE`.
- Do not upgrade lifecycle maturity during discovery.

## Privacy boundary

Never copy private project code, credentials, customer data, proprietary prompts, confidential architecture, identifying business rules, or other private implementation details into YON.

A private implementation may be used as context for discovery, but only generalized, reviewable knowledge can become a YON extraction candidate.

## Non-goals

Discovery does not:

- implement code;
- create or publish capabilities automatically;
- force a standard architecture;
- turn every repeated feature into a capability;
- replace product-specific domain modeling;
- treat a category label as proof of a capability match.

## Completion rule

Discovery is complete when the real workflow has been decomposed, reusable capabilities and patterns have been searched, every relevant candidate is classified, genuine gaps are explicit, product-specific boundaries are clear, and the next implementation step is justified.
