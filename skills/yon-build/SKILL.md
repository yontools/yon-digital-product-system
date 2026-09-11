---
name: yon-build
description: Build a new SaaS, website, landing page, dashboard, or digital product with YON from requirements through Blueprint, environment detection, execution planning, implementation, and verification.
disable-model-invocation: true
---

# YON Build

YON Build turns an understood product request into a verified implementation. For broad or multi-workflow products, a Product Blueprint is the contract between product understanding and implementation, and an Execution Plan is the operational handoff into implementation.

## Build sequence

`UNDERSTAND → BUSINESS DISCOVERY → PRODUCT MODEL → GRAPH/EVENT/POLICY/AGENT CONTEXT → DISCOVER → RESOLVE → BLUEPRINT → EXECUTION PLAN → ENVIRONMENT → EXECUTE → VERIFY`

### 1. Understand

Identify the goal, users, participants, roles, relationships, primary jobs, critical workflows, constraints, success criteria, existing behavior, and project-local instructions.

### 2. Business Discovery

When the request describes a real-world business operation, use `yon-business-discovery` before treating the business category as a product specification. Identify the smallest combination of Business Operating Archetypes supported by the actual workflow. Archetypes are hypotheses, not templates, feature lists, schemas, or architecture.

### 3. Product Model

For broad products, use the Universal Product Model when it materially clarifies participants, relationships, resources, actions, events, states, temporal rules, workflows, transactions, communications, documents, or boundaries. Do not over-model.

### 4. Graph / Event / Policy / Agent Context

For products with significant relationship-driven coordination, event reactions, explicit decision boundaries, or AI-operated workflows, use the relevant YON layers:

- **Business Graph** for relationship and context reasoning;
- **Event Engine** for meaningful occurrences and reactions;
- **Policy** for explicit decision, approval, denial, and boundary conditions;
- **Agent System** for bounded AI decision and action behavior.

Use only the layers justified by the product. They are conceptual and do not prescribe infrastructure.

### 5. Discover

Use `yon-capability-discovery` when the request spans multiple reusable behaviors or when the product model is unfamiliar. Search capabilities, patterns, and evidence. Classify matches and identify genuine gaps.

### 6. Resolve

Use `yon-capability-resolver` to select the minimum justified capability composition. Do not force matches or silently turn optional capabilities into requirements.

### 7. Blueprint

For broad products, create or update a Product Blueprint using `blueprints/BLUEPRINT-TEMPLATE.md`. The Blueprint should make participants, relationships, workflows, entities, lifecycle, capability composition, patterns, gaps, product-specific behavior, risks, implementation order, and verification gates explicit. When relevant, include graph context, event reactions, policy/approval boundaries, agent boundaries, and autonomy rules.

A Blueprint is a decision contract, not an automatic architecture or database schema. It must not override project-local constraints or justify unnecessary changes to working behavior.

### 8. Execution Plan

When the Blueprint contains multiple meaningful implementation steps, create an Execution Plan using `yon-execution-plan` and `execution/EXECUTION-PLAN-TEMPLATE.md`.

The plan converts approved decisions into dependency-aware vertical slices with observable acceptance criteria, risk classification, verification checkpoints, regression surfaces, explicit exclusions, and stop conditions.

Do not use technical file lists as a substitute for a user-value execution plan. Every meaningful slice must trace back to an outcome, workflow, and Blueprint decision.

### 9. Environment

Before concrete tool selection or execution in an unfamiliar/partially known project, use `yon-environment` to create or refresh an Environment Profile. Detect project/stack signals, verify actual tool availability when needed, separate availability from authorization, and record blockers/evidence without secrets.

`DOCUMENTED ≠ AVAILABLE`. A configured provider or dependency is only a signal until the required capability is safely verified.

### 10. Execute

Use `yon-execute` to run the ready slices. Use `yon-orchestrate` as the operational layer for concrete tool selection. Implement the smallest useful slice, run the real product, inspect the result, correct failures, and verify the slice before progressing when practical.

Do not silently invent unresolved product decisions. Pause at missing authorization/access, unresolved critical product behavior, or unverifiable high-risk boundaries and report the block.

### 11. Run / Inspect / Correct

Run the real product as early as practical. Exercise critical workflows, inspect browser/runtime behavior, console/network failures, responsive states, accessibility behavior, and relevant data/security boundaries. For event, policy, or agent behavior, inspect triggers, decisions, side effects, permissions, duplicate handling, approval gates, uncertainty handling, and stop conditions.

Correct the smallest responsible cause and re-run the affected journey.

### 12. Verify

Use `validation/INDEX.md` to select proportional gates. Verify the original user outcome end-to-end. Record meaningful findings as evidence when they can support future reusable knowledge.

## High-risk changes

Authentication, authorization, billing, destructive operations, migrations, security controls, external integrations, tenancy/isolation, agent actions with consequential side effects, policy changes affecting access or money, and core business rules require stronger understanding and verification. Execution may be blocked when required evidence or authorization is unavailable.

## Completion

A build is complete only when the affected user journey works in the running product, all required execution-plan slices are verified or explicitly blocked, important states are handled, responsive/accessibility concerns have been considered, relevant runtime/security boundaries are verified, policy decisions are explicit where applicable, agent/event behavior is bounded where applicable, no hidden high-risk failure remains, and the implementation remains consistent with the approved product intent.
