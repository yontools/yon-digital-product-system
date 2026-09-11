---
name: yon-policy
description: Define and verify explicit policy and decision boundaries for product actions, workflows, automations, and AI agents without confusing authorization, workflow, tool availability, or autonomy.
disable-model-invocation: true
---

# YON Policy

## Position

`CONTEXT → POLICY → DECISION → AUTHORIZED ACTION → EVENT / RESULT`

## Use when

Use this skill when behavior depends on explicit allow/deny rules, approval thresholds, limits, tenant boundaries, business conditions, or uncertainty handling.

Do not introduce a policy layer for a simple action whose behavior is already unambiguous.

## Process

1. Define the outcome and consequential action.
2. Identify actor, organization/context, resource, workflow/state, and relevant relationships.
3. Identify applicable permissions and business constraints.
4. Define conditions and required evidence.
5. Define explicit decision outcomes.
6. Define approval, escalation, failure, and stop behavior.
7. Resolve tool availability and authority separately from policy.
8. Verify allow, deny, approval, boundary, and unknown paths.
9. Record evidence and keep private decision logic private.

## Critical distinction

`AUTHENTICATION ≠ ROLE ≠ PERMISSION ≠ POLICY ≠ TOOL AVAILABILITY ≠ AUTONOMY`

A policy may decide that an action is allowed, but execution still requires the actor and tool to be authorized and available.

## Unknowns

If required context, authority, evidence, or policy is unknown, use `BLOCKED` rather than assuming permission.

## High-risk behavior

Financial commitments, destructive actions, authorization changes, production changes, security-sensitive operations, irreversible customer impact, and core business-rule changes require explicit policy and proportional verification.

## Output

Produce or update a policy contract using `policy/POLICY-CONTRACT-TEMPLATE.md`, including applicability, conditions, decision, approval/escalation, failure behavior, audit/evidence, and verification.
