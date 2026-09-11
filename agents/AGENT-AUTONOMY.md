# YON Agent Autonomy

## 1. Purpose

YON agents are software participants that can observe context, reason about goals, use authorized tools, communicate, and take bounded actions.

Agent autonomy is a **control model**, not a model-quality rating. A more capable model does not automatically receive more authority.

`MODEL CAPABILITY ≠ TOOL ACCESS ≠ AUTHORIZATION ≠ AUTONOMY`

## 2. Agent profile

A meaningful agent definition should establish:

- identity/name configurable by the product or organization;
- objective and success criteria;
- operating context;
- available tools/capabilities;
- permissions and boundaries;
- memory/context allowed to use;
- channels through which it may communicate;
- autonomy level;
- approval thresholds;
- escalation rules;
- stop conditions;
- audit/observability requirements.

See `AGENT-PROFILE-TEMPLATE.md`.

## 3. Autonomy levels

### Level 1 — Observer

Analyzes information and produces observations or recommendations.

It does not execute consequential actions.

### Level 2 — Assistant

Proposes actions and can prepare work, but consequential actions require human approval.

### Level 3 — Operator

Executes explicitly authorized actions within defined tools, permissions, scope, and limits.

### Level 4 — Bounded Autonomous

Acts without per-action approval inside a clearly defined policy boundary. It must escalate or stop when the action exceeds that boundary or uncertainty becomes material.

Autonomy level must never override authorization, security policy, tenant isolation, or explicit high-risk approval requirements.

## 4. Agent decision loop

`OBSERVE → CONTEXTUALIZE → ASSESS → DECIDE → AUTHORIZE → ACT → OBSERVE RESULT → VERIFY → CONTINUE / ESCALATE / STOP`

The Business Graph can provide relationship context. The Event Engine can provide triggers and evidence of occurrences. Neither grants authority by itself.

## 5. Tool authority

An agent can only use tools that are:

- available;
- authorized for the current context;
- within the agent's granted scope;
- appropriate for the action;
- consistent with YON orchestration risk rules.

`AVAILABLE` does not mean `AUTHORIZED`.

An unavailable, unauthorized, degraded, or unknown required tool creates a blocker rather than permission to improvise.

## 6. Approval gates

Human approval should remain explicit for high-impact actions unless a product has deliberately defined and verified a bounded policy that permits the action.

High-risk examples include:

- financial commitments or transfers;
- destructive operations;
- security-sensitive changes;
- authorization changes;
- production migrations;
- irreversible customer-impacting actions;
- changes to core business rules.

Approval must identify what will happen, affected scope, important consequences, and the authority being granted.

## 7. Memory and context

Agents should receive the smallest context necessary to perform the task.

Context may come from product records, graph relationships, events, documents, conversation, or approved external systems.

Do not provide secrets, unrelated tenant data, private implementation details, or unnecessary personal information merely because an agent can technically access it.

## 8. Escalation and uncertainty

Agents should distinguish:

- known facts;
- supported evidence;
- inference;
- uncertainty;
- missing information.

Material uncertainty should trigger clarification, escalation, or safe non-action rather than fabricated certainty.

## 9. Stop conditions

An agent must stop or escalate when:

- required authorization is absent;
- a tool is unavailable or unsafe;
- scope is exceeded;
- policy is ambiguous;
- a destructive consequence is unexpected;
- required evidence is missing;
- an external system behaves unexpectedly;
- repeated retries indicate a systemic failure;
- tenant or privacy boundaries become uncertain.

## 10. Auditability

Consequential agent actions should be traceable to:

`AGENT → AUTHORITY → TOOL → ACTION → EVENT / RESULT`

Where applicable, preserve correlation and causation identifiers so an operator can understand why an action happened.

## 11. Agent and workflow boundaries

An agent should not silently invent a workflow.

The product defines meaningful business workflows and policies. The agent can operate within those boundaries, select among permitted actions, or propose a product-specific decision when explicitly allowed.

## 12. Verification

Verify autonomy at the level of behavior:

- permitted action succeeds;
- denied action is blocked;
- approval gates are enforced;
- tool boundaries are respected;
- context is tenant-safe;
- uncertainty causes safe escalation;
- important actions are auditable;
- retries do not create unsafe duplicate effects;
- stop conditions actually stop execution.

Validation outcomes remain `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE`.

## 13. Privacy

Public YON documentation must never contain private agent prompts, customer data, secrets, credentials, proprietary business rules, or private tool configurations.
