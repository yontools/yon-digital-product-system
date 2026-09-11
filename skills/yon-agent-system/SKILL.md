---
name: yon-agent-system
description: Define bounded AI agent behavior in YON using configurable identity, goals, context, tools, permissions, autonomy levels, approvals, escalation, audit, and verification.
disable-model-invocation: true
---

# YON Agent System

## Position

`BUSINESS GRAPH → EVENT ENGINE → AGENT SYSTEM → ORCHESTRATION → EXECUTION → VERIFICATION`

## Use when

Use this skill when a product needs an AI agent that does more than answer questions: observe operational context, recommend actions, execute authorized work, react to events, or operate autonomously within defined boundaries.

Do not add an agent merely because AI is fashionable. First establish a meaningful user or operational outcome.

## Process

1. Define the outcome and operating context.
2. Identify the participant represented by the agent and its organization/context.
3. Define objective, exclusions, tools, permissions, memory, channels, and data scope.
4. Select the smallest autonomy level justified by the outcome.
5. Define approval thresholds, escalation rules, and stop conditions.
6. Resolve actual tool availability and authorization through YON's Environment, Tool Registry, and Orchestration layers.
7. Define relevant graph context and event triggers when applicable.
8. Implement or configure the agent.
9. Verify allowed, denied, approval, boundary, failure, and stop behavior.
10. Record evidence for reusable learning without exposing private implementation.

## Autonomy rule

Autonomy is bounded authority, not intelligence.

`MODEL CAPABILITY ≠ TOOL ACCESS ≠ AUTHORIZATION ≠ AUTONOMY`

A capable model with no authorized tool cannot act. An available tool does not grant permission. An autonomous level does not bypass policy.

## Required controls

Every operational agent must have, proportionally to risk:

- explicit identity/purpose;
- objective and exclusions;
- allowed context;
- tool scope;
- permission boundary;
- autonomy level;
- approval requirements;
- escalation/stop conditions;
- auditability;
- verification criteria.

## Failure rule

If a required authority, tool, policy, context, or verification condition is unknown or unavailable, mark the operation `BLOCKED` at the smallest boundary. Never convert an unknown into permission.

## Privacy

Never copy private prompts, secrets, customer data, credentials, private business rules, or proprietary architecture into public YON knowledge.

## Reference

Use `agents/AGENT-AUTONOMY.md` and `agents/AGENT-PROFILE-TEMPLATE.md` for the conceptual model and profile structure.
