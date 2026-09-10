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
5. If the project or required tooling is unfamiliar, run the YON Environment Detection flow and build/refresh an Environment Profile.
6. If real tool execution is required, resolve the project-local Tool Registry with `yon-tool-registry` before selecting concrete adapters.
7. Inspect the existing implementation before proposing changes.
8. Load `skills/yon-orchestrate/SKILL.md` for tool-mediated execution.

Do not assume a project uses a particular framework, database, or deployment provider until the repository confirms it.

## Command mapping

- Audit an existing product → `commands/yon-audit.md`
- Polish an existing product → `commands/yon-polish.md`
- Build a new product → `commands/yon-build.md`
- Detect/refresh environment → `commands/yon-environment.md`
- Resolve project Tool Registry → `commands/yon-tool-registry.md`
- Execute an approved plan → `commands/yon-execute.md`
- Create an execution plan → `commands/yon-execution-plan.md`
- Orchestrate a real tool action → `commands/yon-orchestrate.md`
- SaaS-specific work → `commands/yon-saas.md`
- Website → `commands/yon-web.md`
- Landing page → `commands/yon-landing.md`
- Onboarding → `commands/yon-onboarding.md`
- Visual work → `commands/yon-visual.md`
- Motion → `commands/yon-motion.md`
- QA → `commands/yon-qa.md`

## Operating loop

`OBSERVE → UNDERSTAND → DETECT → PROPOSE → IMPLEMENT → RUN → INSPECT → CORRECT → VERIFY`

For environment-aware execution:

`DETECT PROJECT → DETECT STACK → DETECT TOOLS → DETECT AUTHORITY → BUILD PROFILE → RESOLVE TOOL REGISTRY`

For tool-mediated execution:

`DECIDE → SELECT TOOL → AUTHORIZE → EXECUTE → OBSERVE → DECIDE NEXT`

Do not stop after writing code when the environment allows execution and verification. Do not claim a tool action occurred without actual evidence.

## Environment + Tool Registry

Use the Environment Profile as evidence, then resolve it into a project-local Tool Registry.

The registry must distinguish:

- `AVAILABLE`
- `UNAVAILABLE`
- `UNAUTHORIZED`
- `DEGRADED`
- `UNKNOWN`

Use evidence precedence:

`ACTUAL > AUTHORIZED > CONFIGURED > SIGNALLED > ASSUMED`

`DOCUMENTED ≠ AVAILABLE`.

A package, configuration entry, script, or documentation reference may signal a capability but cannot prove that the concrete adapter is usable. Presence never implies authorization.

Before high-risk or externally mutating actions, refresh the relevant adapter state close to execution time.

Never expose secret values while detecting or resolving the environment. Do not install, deploy, migrate, delete or mutate production merely to prove that a capability exists.

## Tool selection

Use the smallest available adapter that can establish the required evidence:

- repository/filesystem for static inspection and edits
- terminal/runtime for scripts, builds, servers and commands
- browser/automation for real interactive behavior
- tests for repeatable acceptance evidence
- GitHub for repository/CI collaboration state
- deployment/infrastructure for hosted state or deployment operations
- visual/media for meaningful product assets

If the required capability is `UNKNOWN`, probe safely or remain `BLOCKED`. If an equivalent lower-risk adapter produces sufficient evidence, prefer it.

## Authorization and risk

- `LOW`: read-only inspection, local tests, non-destructive browser QA.
- `MEDIUM`: edits, dependency installation, generated assets, commits, reversible repository changes.
- `HIGH`: production deployment, migrations, billing, auth/authz, destructive operations, security-sensitive changes, critical external integrations, or core business rules.

HIGH-risk actions require explicit authorization and proportional verification. If the required permission or verification is unavailable, mark the action `BLOCKED`.

## Reuse principle

Prefer proven capabilities and patterns over reinventing solutions. When a project contains a reusable solution, identify the generalizable pattern separately from project-specific implementation details.

A private project's code, secrets, data, customer information, prompts, business rules, or proprietary architecture must never be copied into the public YON repository automatically.

## Change safety

- Preserve working behavior unless there is a clear reason to change it.
- Inspect before mutate.
- Prefer small, reversible changes.
- Treat auth, payments, permissions, data migrations, destructive operations, and production infrastructure as high-risk.
- Observe meaningful mutations before deciding the next action.
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

`BLOCKED` is never `PASS` or `VERIFIED`.

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
