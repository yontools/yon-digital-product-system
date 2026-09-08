---
name: notification-orchestration
description: Coordinate user and operational notifications across events, channels, timing, preferences, and delivery states.
status: experimental
domains: notifications, operations, communication
---

# Notification Orchestration

## Problem
Important events can be missed when communication depends on manual follow-up or when each feature implements its own notification logic.

## When to use it
Use when a product needs reliable communication triggered by business or system events, especially deadlines, status changes, assignments, approvals, or failures.

## Inputs
- Event or state transition
- Recipient(s)
- Channel(s)
- Timing rules
- User preferences
- Message/template data

## Outputs
- Notification intent
- Delivery attempt/state
- Read or acknowledgement state when applicable
- Failure information suitable for retry or operator action

## Core behavior
Separate event detection from message delivery. Support channel preferences, deduplication, scheduling, retries, and observable delivery states where the product requires them.

## UX considerations
Notifications should be actionable, understandable, appropriately urgent, and avoid duplicate or noisy messages. Critical operational alerts should expose the underlying object and the action required.

## Data considerations
Model event identity, recipient, channel, delivery status, timestamps, retry information, and relevant references. Avoid storing unnecessary sensitive message content.

## Integration points
Email, messaging platforms, push notifications, SMS providers, in-app notifications, workflow engines, scheduled jobs.

## Edge cases
- Duplicate events
- Expired notification
- Invalid recipient/channel
- Provider outage
- Retry exhaustion
- Conflicting user preferences
- Time-zone-sensitive delivery

## Verification
Verify event-to-notification mapping, deduplication, retry behavior, preference handling, failure visibility, and time-sensitive delivery.

## Evidence
Experimental until validated through repeated real-world implementations or tests.

## Privacy check
Do not publish credentials, provider configuration secrets, customer data, private message content, or proprietary notification rules.
