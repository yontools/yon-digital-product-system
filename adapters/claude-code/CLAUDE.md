# YON Digital Product System — Claude Code Adapter

This file is the Claude Code entry point for projects that use YON.

## Mission

Apply YON as a product-engineering operating system: understand the product, inspect the existing implementation, identify the highest-value improvements, implement safely, run the product, inspect the result, correct issues, and verify the outcome.

## Loading order

Before changing a project:

1. Read `YON.md` from the YON repository or installed copy.
2. Read the relevant skill under `skills/`.
3. Read the relevant command under `commands/`.
4. Inspect the target project's own instructions (`CLAUDE.md`, `AGENTS.md`, README, package scripts, and relevant docs).
5. Inspect the existing implementation before proposing changes.

Do not assume a project uses a particular framework, database, or deployment provider until the repository confirms it.

## Command mapping

- Audit an existing product → `commands/yon-audit.md`
- Polish an existing product → `commands/yon-polish.md`
- Build a new product → `commands/yon-build.md`
- SaaS-specific work → `commands/yon-saas.md`
- Website → `commands/yon-web.md`
- Landing page → `commands/yon-landing.md`
- Onboarding → `commands/yon-onboarding.md`
- Visual work → `commands/yon-visual.md`
- Motion → `commands/yon-motion.md`
- QA → `commands/yon-qa.md`

## Operating loop

`OBSERVE → UNDERSTAND → DETECT → PROPOSE → IMPLEMENT → RUN → INSPECT → CORRECT → VERIFY`

Do not stop after writing code when the environment allows execution and verification.

## Reuse principle

Prefer proven capabilities and patterns over reinventing solutions. When a project contains a reusable solution, identify the generalizable pattern separately from project-specific implementation details.

A private project's code, secrets, data, customer information, prompts, business rules, or proprietary architecture must never be copied into the public YON repository automatically.

## Change safety

- Preserve working behavior unless there is a clear reason to change it.
- Prefer small, reversible changes.
- Treat auth, payments, permissions, data migrations, destructive operations, and production infrastructure as high-risk.
- Verify high-risk changes explicitly before considering them complete.

## Definition of done

A task is not complete merely because the code compiles. When applicable, verify:

- intended user flow
- responsive behavior
- loading, empty, error, and success states
- accessibility basics
- visual consistency
- console/runtime errors
- affected integrations
- tests and build

## Private project boundary

YON is a methodology and capability library. It may be used inside private projects, but private project material remains private unless an owner explicitly chooses to extract and publish a generalized pattern.

## Pattern extraction

When a solution proves useful across projects, document it as a generalized capability or pattern containing:

- problem
- context
- solution
- constraints
- verification/evidence
- reusable implementation guidance
- status: `experimental`, `proven`, or `deprecated`

Never publish project-specific secrets, customer data, credentials, proprietary code, or identifying business logic as part of a pattern.
