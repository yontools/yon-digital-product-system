# YON Event Engine

## Purpose

The Event Engine defines how YON reasons about meaningful occurrences and their consequences.

An **event records that something happened**. It is distinct from an action or command, which expresses intent to change something.

The Event Engine is a product reasoning and coordination layer. It does not require a particular message broker, queue, database, or event-driven infrastructure.

## Core flow

`ACTION / EXTERNAL SIGNAL → EVENT → CONTEXT → POLICY / WORKFLOW → REACTION → NEW EVENT`

A reaction may be a state transition, notification, task, workflow step, integration, audit record, or agent decision.

## Event contract

A meaningful event should provide enough context to be safely interpreted:

- stable event identifier;
- event type;
- schema/version;
- occurred-at timestamp;
- source/context;
- actor when known;
- subject/resource;
- organization/tenant boundary;
- correlation identifier when a business flow spans events;
- causation identifier when one event resulted from another;
- relevant facts or state-change information;
- idempotency identity where duplicate delivery is possible;
- sensitivity classification when data handling requires it;
- provenance/evidence when event origin matters.

See `EVENT-CONTRACT-TEMPLATE.md`.

## Commands versus events

Do not blur intent and occurrence.

- **Command/action:** "send reminder" or "approve order".
- **Event:** "reminder sent" or "order approved".

A command can fail without producing its corresponding success event. An event should represent an occurrence that the system can treat as factual within its stated evidence boundary.

## Event reactions

YON should define reactions from meaningful business conditions, not from every database mutation.

Example:

`rental_expired → identify responsible party → create collection task → permitted notification → audit outcome`

Each reaction must respect permissions, tenant boundaries, idempotency, failure handling, and approval requirements.

## Reliability principles

When events are used operationally:

- expect duplicate delivery unless exactly-once behavior is genuinely established;
- make consumers idempotent where repetition is possible;
- define retry behavior for recoverable failures;
- isolate poison/unprocessable events instead of silently dropping them;
- define ordering only where business behavior actually depends on order;
- preserve correlation and causation for diagnosis;
- make important side effects observable;
- never claim an event occurred merely because an action was requested.

## Event and audit history

An event can support audit history, but the concepts are not identical.

Audit answers **who changed what, when, and under which authority**.

Events answer **what meaningful occurrence happened** and provide context for reactions.

A product may need one, both, or neither.

## Event and temporal rules

Time-based rules may produce events:

`deadline reached → expiration event → workflow reaction`

The engine should avoid continuously polling when a more appropriate scheduling mechanism exists, but YON does not prescribe the implementation.

## Event and agents

Agents may consume events as triggers or context, but an event does not itself grant permission to act.

Agent actions remain bounded by tool availability, authorization, policy, autonomy level, approval gates, and stop conditions.

## Verification

At proportional risk levels verify:

1. correct event is emitted for the intended occurrence;
2. duplicate delivery does not create unsafe duplicate effects;
3. required context and tenant boundaries are preserved;
4. reactions occur only when their conditions are met;
5. failures retry or stop according to defined policy;
6. important side effects are observable;
7. event history supports the intended operational diagnosis.

Validation outcomes remain `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE`.

## Privacy

Events can contain sensitive business information. Public YON documentation must use generic examples and never expose private customer data, secrets, credentials, proprietary event payloads, or private architecture.
