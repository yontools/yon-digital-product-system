# YON Policy & Decision Boundaries

## Purpose

Policies define the conditions and boundaries under which a product, workflow, automation, or agent may act.

Policy is the missing control layer between **context** and **action**:

`CONTEXT → POLICY / DECISION → AUTHORIZED ACTION → EVENT / RESULT`

This layer is conceptual. It does not prescribe a rules engine, programming language, policy server, or authorization technology.

## What policy answers

A policy can establish:

- who or what may act;
- in which organization/context;
- on which resource;
- under which conditions;
- which actions are allowed, denied, or require approval;
- what limits apply;
- what evidence is required;
- what happens when information is missing or uncertain.

## Policy is not

- authentication;
- a role definition;
- a workflow itself;
- an agent autonomy level;
- a tool registry;
- an event;
- a database schema.

These concerns interact, but must remain distinguishable.

## Decision outcomes

Use explicit outcomes:

- `ALLOW` — action may proceed within stated scope;
- `DENY` — action must not proceed;
- `REQUIRE_APPROVAL` — action needs an identified approval boundary;
- `BLOCKED` — required context, authority, policy, or evidence is unavailable/unknown;
- `NOT_APPLICABLE` — policy does not govern the action.

Never treat `BLOCKED` as `ALLOW` or silently fall back to assumption.

## Policy evaluation

A proportional evaluation can be expressed as:

`ACTOR + CONTEXT + RESOURCE + ACTION + EVIDENCE → POLICY → DECISION`

The decision should be traceable when the action is consequential.

## Policy precedence

When multiple boundaries apply, prefer the most restrictive applicable boundary unless the product has explicitly defined a different precedence rule.

At minimum consider:

1. security and tenant boundary;
2. explicit authorization;
3. product/business policy;
4. workflow state;
5. approval requirement;
6. agent autonomy boundary;
7. tool capability and availability.

Availability is not authority.

## Agents

An agent must evaluate applicable policy before consequential actions. Autonomy level changes how often approval may be required; it does not remove authorization or security boundaries.

## Events

Events may trigger policy evaluation, but an event is evidence of an occurrence, not permission to act.

## Business Graph

Graph relationships may provide context such as ownership, responsibility, membership, or customer relationship. They do not independently grant authorization.

## Verification

Verify at least the relevant allow, deny, approval, boundary, uncertainty, and failure paths for consequential behavior.

## Privacy

Public YON policy examples must remain generic. Never publish private rules, secrets, customer data, credentials, proprietary decision logic, or private implementation details.
