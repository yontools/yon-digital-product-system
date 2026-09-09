---
name: yon-capability-resolver
description: Resolve product requirements into the smallest evidence-aware composition of reusable YON capabilities and patterns without importing private implementation details.
disable-model-invocation: true
---

# YON Capability Resolver

Use this skill after or together with `yon-capability-discovery` when planning or extending a digital product and deciding which reusable YON capabilities should be used in implementation.

## Objective

Translate a real product need into the smallest justified capability composition before implementation.

The resolver answers:

1. What user/business problem must be solved?
2. Which reusable capabilities directly cover required behavior?
3. Which supporting capabilities are needed for composition?
4. Which candidates are optional hypotheses?
5. What required behavior is genuinely missing?
6. What evidence supports each recommendation?
7. What must remain product-specific?
8. In what order should the capabilities be implemented and verified?

## Relationship with Business Discovery

When the product comes from a real-world business operation, `yon-business-discovery` may first identify Business Operating Archetypes. Those archetypes provide **behavioral context**, not automatic capability requirements.

Use:

`BUSINESS OPERATION → ARCHETYPES → WORKFLOWS → CAPABILITY DISCOVERY → RESOLUTION`

A resolver must still verify the actual workflow before turning an archetype into a capability recommendation. For example, `Appointment & Scheduling` does not automatically require a generic calendar, and `Commerce & Fulfillment` does not automatically require inventory.

## Relationship with Discovery

`yon-capability-discovery` searches broadly for reusable knowledge and identifies genuine gaps.

This resolver turns that discovery into an implementation-oriented composition.

Use the sequence:

`PROBLEM → DISCOVERY → RESOLUTION → COMPOSITION → IMPLEMENTATION → VERIFICATION`

If discovery has not been performed and the problem spans several reusable behaviors, perform discovery first rather than guessing.

## Resolution process

### 1. Understand the product

Inspect the request, users, roles, jobs, workflows, constraints, existing behavior, relevant code, and project instructions. Do not assume a capability merely because the product belongs to a familiar category.

### 2. Use business context when available

If a Business Discovery result exists, inspect its detected archetypes, confidence, evidence, workflows, resources, and unresolved questions.

Treat:

- HIGH confidence as strong contextual evidence;
- MEDIUM confidence as useful but confirmable context;
- LOW confidence as a hypothesis that must not silently become a requirement.

If no Business Discovery exists, do not invent archetypes simply to fill the process.

### 3. Decompose required behavior

Identify the minimum behaviors needed for the requested outcome: entities and relationships, lifecycle/state changes, time rules, ownership, permissions, communications, transactions/documents when relevant, operational handoffs, and critical states.

Use `capabilities/COMPOSITION-GUIDE.md` as a domain-neutral checklist for these dimensions. It is a reasoning aid, not a mandatory architecture.

### 4. Search YON knowledge

Inspect:

- `capabilities/INDEX.md`
- `capabilities/CAPABILITY-MAP.md`
- `capabilities/COMPOSITION-GUIDE.md`
- individual capability files
- `patterns/INDEX.md`
- relevant pattern files
- `evidence/INDEX.md` and relevant evidence when available

Search by behavior and workflow, not only product category.

### 5. Classify matches

For every relevant candidate, assign exactly one classification:

- **DIRECT** — clearly required and substantially covered by an existing reusable capability.
- **SUPPORTING** — enables a direct capability or important workflow.
- **OPTIONAL** — plausible but not currently justified.
- **MISSING** — required reusable behavior with no adequate YON capability.
- **PRODUCT-SPECIFIC** — important to this product but should remain local.

Never use a DIRECT match merely because names sound similar.

### 6. Evaluate evidence and maturity

For each reusable recommendation, state the available evidence and lifecycle maturity. Prefer `PROVEN` when documented scope matches. Treat `EXPERIMENTAL` as a hypothesis requiring validation when material. Do not promote maturity during resolution.

Evidence status and capability lifecycle are separate dimensions:

- evidence: `UNVERIFIED`, `SUPPORTED`, `STRONG`, `CONTRADICTED`;
- lifecycle: `DISCOVERED`, `EXPERIMENTAL`, `PROVEN`, `DEPRECATED`.

Do not confuse either system with the classification above.

### 7. Validate composition

Before recommending a composition, check interactions between:

- entity relationships and data ownership;
- tenancy and isolation;
- lifecycle/state transitions;
- permissions and authorization;
- notifications and timing;
- auditability;
- failure and recovery;
- operator workflows;
- responsive/accessibility requirements.

The capability map is a discovery aid, never an automatic architecture decision.

### 8. Resolve gaps honestly

A `MISSING` capability is valid output. Do not invent a match.

For each genuine gap, decide whether it is:

- `YON-CANDIDATE` — likely reusable across multiple products;
- `PRODUCT-SPECIFIC` — should remain local;
- `NEEDS-EVIDENCE` — potentially reusable but insufficiently supported.

A gap does not become a public capability automatically. Use `yon-extract` for deliberate extraction and `yon-learn` for reviewed promotion.

### 9. Produce the resolution matrix

Return:

| Need / behavior | Archetype context | Candidate | Classification | Maturity | Evidence | Coverage | Gap decision | Next action |
|---|---|---|---|---|---|---|---|---|

Then provide:

- problem/workflow summary;
- relevant archetypes and confidence;
- direct capabilities;
- supporting capabilities;
- optional capabilities;
- missing capabilities;
- product-specific requirements;
- recommended minimal composition;
- dependencies/interactions;
- implementation order;
- verification plan;
- unresolved questions;
- privacy boundary.

## Composition rules

1. Prefer the smallest composition that fully covers the required outcome.
2. Add a capability only when its behavior is justified by the workflow.
3. Treat archetype matches as context, never proof.
4. Do not duplicate semantics across capabilities.
5. Keep domain-specific business rules in the product unless evidence supports broader reuse.
6. If two capabilities overlap, explain the boundary and choose one owner for the behavior.
7. If a dependency is uncertain, mark it unresolved instead of silently adding it.
8. Optional capabilities must not become hidden requirements.

## Rules

- Reuse before reinventing.
- Search before creating.
- Do not force a capability match.
- Do not copy private code, secrets, customer data, proprietary prompts, confidential architecture, or identifying business rules into YON.
- Do not treat capability-map combinations as automatic architecture.
- Do not upgrade lifecycle maturity during resolution.
- Do not publish or promote reusable knowledge from this skill.
- Preserve existing working behavior unless the requested outcome requires change.

## Example

A rental workflow might resolve to:

`Asset Management + Rental Management + Temporal States & Expiration`

with `Notification Orchestration` as supporting when deadline communication is required.

The resolver must still inspect the actual workflow, ownership, permissions, timing rules, and failure states before treating that composition as justified.

## Completion rule

A resolution is complete when the real workflow is understood, relevant business archetypes are treated as contextual evidence rather than requirements, candidates are classified, evidence and maturity are visible, composition boundaries are explicit, gaps are honest, product-specific requirements are separated, and the next implementation and verification steps are clear.
