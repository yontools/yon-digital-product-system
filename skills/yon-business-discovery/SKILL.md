---
name: yon-business-discovery
description: Discover a business operating model from real workflows using reusable operating archetypes, then connect those behaviors to YON capabilities, patterns, gaps, and product-specific requirements.
disable-model-invocation: true
---

# YON Business Discovery

Use this skill when YON needs to understand what a business actually does before designing or building its software.

## Core principle

Start from **operation**, not industry label.

A business category such as barber shop, clinic, car wash, logistics company, school, rental company, or restaurant is not a product specification. The same operating behavior can exist across many categories, and one business can contain several different behaviors.

## Sequence

`BUSINESS REQUEST → OBSERVE OPERATION → IDENTIFY ARCHETYPES → MODEL WORKFLOWS → DISCOVER CAPABILITIES → RESOLVE → BLUEPRINT`

## Process

### 1. Understand the business outcome

Identify:

- who receives value;
- what the business delivers;
- how work enters the operation;
- what must happen for value to be delivered;
- how money, commitments, documents, or permissions matter when relevant;
- what success means operationally.

### 2. Observe workflows

Ask about the real operation rather than inventing a standard software flow:

- What triggers work?
- Who acts next?
- What information or resource is needed?
- What decisions occur?
- What gets assigned, scheduled, reserved, moved, delivered, approved, or completed?
- What can fail, expire, be cancelled, delayed, reopened, or escalated?
- What happens repeatedly?

### 3. Identify operating archetypes

Read `discovery/BUSINESS-OPERATING-ARCHETYPES.md`.

Select only archetypes supported by observed signals. A business may use multiple archetypes. Give each a confidence of HIGH, MEDIUM, or LOW.

Do not convert an archetype into an automatic feature list.

### 4. Model the operation

When useful, connect the archetypes to the Universal Product Model:

- participants and relationships;
- roles;
- resources;
- actions;
- events;
- states;
- temporal rules;
- workflows;
- transactions;
- communications;
- documents;
- permissions/boundaries.

Use the Universal Product Model only where it improves clarity. Do not over-model.

### 5. Discover reusable capabilities

After the operating model is understood, use `yon-capability-discovery` to search capabilities, patterns, evidence, and genuine gaps.

Search by behavior. For example:

- "service that must be booked" → scheduling;
- "equipment used until a deadline" → temporary use + temporal expiration;
- "field team moves assets between sites" → asset + field operations;
- "customer request needs review before execution" → request/order workflow + approval.

These are discovery examples, not automatic mappings.

### 6. Separate reusable from product-specific

Reusable behavior should map to YON capabilities/patterns when justified.

Keep domain-specific rules local when they are unique, insufficiently evidenced, or tightly coupled to the business.

If an important reusable behavior has no adequate capability, mark it `MISSING` and determine whether it is `YON-CANDIDATE`, `PRODUCT-SPECIFIC`, or `NEEDS-EVIDENCE`.

### 7. Produce a discovery result

Use `discovery/BUSINESS-DISCOVERY-TEMPLATE.md` and report:

1. business outcome;
2. participants/relationships;
3. workflows;
4. detected archetypes + confidence;
5. resources/lifecycle/time;
6. candidate capabilities/patterns;
7. gaps;
8. product-specific behavior;
9. unresolved questions;
10. recommended next step;
11. verification implications;
12. privacy check.

## Archetype rules

- An archetype is a behavioral hypothesis.
- Archetypes are not vertical templates.
- Archetypes are not architecture.
- Archetypes are not schemas.
- Archetypes are not automatic requirements.
- Prefer the smallest combination that explains the operation.
- Do not create a new archetype just because an industry has a new name.
- New archetypes require evidence and review.

## Privacy

Never transfer private source code, credentials, customer data, proprietary prompts, confidential architecture, identifying business rules, or other private implementation details into public YON knowledge.

## Completion rule

Business Discovery is complete when the real operation is understood enough to explain its primary workflows, relevant operating archetypes are supported by evidence, reusable capabilities can be searched intelligently, product-specific behavior is explicit, and the next product-design/build decision is justified.
