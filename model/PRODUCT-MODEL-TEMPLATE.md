# Product Model Template

Use this lightweight model for products where understanding participants, relationships, resources, workflows, and boundaries materially improves implementation decisions.

## Product outcome

- Primary outcome:
- Who benefits:
- What must become easier, faster, safer, clearer, or more reliable:

## Participants

| Party | Relationship / context | Role | Important boundary |
|---|---|---|---|
| | | | |

## Resources / entities

| Resource / entity | Why it matters | Lifecycle? | Product-specific semantics |
|---|---|---|---|
| | | | |

## Primary actions

| Actor | Action | Target | Expected result |
|---|---|---|---|
| | | | |

## Events and state changes

| Event | Trigger | State change | Consequence |
|---|---|---|---|
| | | | |

## Temporal rules

| Rule | Applies to | Boundary | Consequence |
|---|---|---|---|
| | | | |

## Workflows

### Workflow: [name]

1. Start condition:
2. Participants:
3. Actions:
4. States:
5. Decisions:
6. Handoffs:
7. Failure / recovery:
8. Completion condition:

## Transactions

- Relevant transaction(s):
- Parties involved:
- Commitment / exchange:
- Important states:
- Payment involved? Yes / No / Unknown

## Communications

| Trigger | Audience | Purpose | Channel / delivery constraint |
|---|---|---|---|
| | | | |

## Documents

| Document | Purpose | Produced / received | Required? |
|---|---|---|---|
| | | | |

## Capability discovery

| Need / behavior | Candidate | Classification | Coverage | Evidence | Gap decision | Next action |
|---|---|---|---|---|---|---|
| | | | | | | |

Use exactly one classification: `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING`, `PRODUCT-SPECIFIC`.

## Product-specific boundary

List concepts that should remain local because they are domain-specific, proprietary, regulatory, or not sufficiently generalizable.

## Risks and verification

- High-risk areas:
- Critical journey to exercise:
- Authorization boundaries:
- Temporal edge cases:
- Failure/recovery paths:
- Regression checks:

## Modeling restraint

Record anything intentionally **not** modeled and why. Avoid introducing abstractions that do not improve a product decision.
