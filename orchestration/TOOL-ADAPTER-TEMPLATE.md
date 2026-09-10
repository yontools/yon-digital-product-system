# YON Tool Adapter Template

Use this template when connecting a concrete development tool to YON.

## Identity

- Adapter ID:
- Tool class: `REPOSITORY | TERMINAL | BROWSER | TEST | GITHUB | DEPLOYMENT | DATABASE | VISUAL | MEDIA`
- Version:
- Environment:

## Purpose

What product question or action does this adapter support?

## Contract

### Inputs

- Required:
- Optional:
- Preconditions:

### Outputs

- Primary result:
- Evidence returned:
- Error/failure information:

## Authority

- Read access:
- Write access:
- Project scope:
- External systems:
- Required authorization:

## Risk

`LOW | MEDIUM | HIGH`

Explain why.

## Side effects

List every known side effect, including indirect effects such as generated files, remote mutations, deployments, messages, or data changes.

## Rollback / stop condition

Describe how to undo the action when possible. If rollback is impossible, state the stop condition and required confirmation before execution.

## Availability

`UNKNOWN | AVAILABLE | UNAVAILABLE | UNAUTHORIZED | DEGRADED`

Availability must be established by the environment; documentation alone is insufficient.

## Evidence

Define what proves that the adapter actually ran and what it produced.

## Failure semantics

- Tool unavailable → `BLOCKED` unless an equivalent safe capability exists.
- Permission denied → `BLOCKED` unless authority can be legitimately obtained.
- Ambiguous result → do not declare success; gather targeted evidence.
- Partial mutation → report exactly what changed and inspect before continuing.

## Privacy

The adapter must not expose secrets, credentials, customer data, proprietary code, private prompts, or confidential business rules to public YON knowledge.
