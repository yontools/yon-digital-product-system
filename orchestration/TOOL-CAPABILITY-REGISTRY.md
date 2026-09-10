# YON Tool Capability Registry

The registry describes **what an environment can actually do**, independently from the model that decides what to do.

It is an operational catalog, not a dependency list and not an architecture prescription.

## Registry rule

A capability is considered available only when the environment can demonstrate that the corresponding adapter/tool exists, is authorized for the target project, and can return observable evidence.

`DOCUMENTED ≠ AVAILABLE`

## Capability classes

| Class | Typical capability | Preferred evidence |
|---|---|---|
| REPOSITORY | inspect/edit files, search code, inspect history | file/tree/diff evidence |
| TERMINAL | run scripts, tests, builds, package commands | command output |
| BROWSER | open app, interact, inspect runtime UI | screenshots/logs/journey result |
| TEST | unit/integration/e2e/a11y checks | test report |
| GITHUB | branches, commits, PRs, issues, CI | GitHub object/status |
| DEPLOYMENT | preview/deploy/rollback/status | provider deployment evidence |
| DATABASE | inspect/query/migrate data | query/migration result |
| VISUAL | generate/edit/analyze visual assets | generated/inspected asset |
| MEDIA | generate/analyze video or other media | media artifact/result |

## Selection matrix

| Need | First choice | Escalate when |
|---|---|---|
| Understand code structure | REPOSITORY | runtime behavior is ambiguous |
| Validate a script/build | TERMINAL | environment dependency is missing |
| Verify actual UI behavior | BROWSER | browser adapter unavailable |
| Prove a regression | TEST | test coverage is insufficient; use targeted runtime evidence |
| Inspect collaboration/CI | GITHUB | action requires permissions not granted |
| Verify production state | DEPLOYMENT | preview/local evidence is insufficient |
| Understand persisted data | DATABASE | query access is unavailable |
| Improve a visual asset | VISUAL | visual generation would not materially improve outcome |
| Add meaningful motion/video | MEDIA | static treatment is sufficient |

## Tool selection algorithm

1. Define the question the action must answer.
2. Identify the smallest capability that can produce sufficient evidence.
3. Confirm the adapter exists.
4. Confirm project authorization and scope.
5. Assess risk and required approval.
6. Execute one meaningful action.
7. Observe its output.
8. Decide whether evidence is sufficient or another capability is required.
9. Stop when the question is answered or the next required capability is unavailable.

Do not call several tools merely because they are available.

## Capability record

Each concrete adapter should expose, at minimum:

- `id`
- `class`
- `purpose`
- `read_or_write`
- `risk`
- `requires_authorization`
- `project_scope`
- `input_contract`
- `output_evidence`
- `side_effects`
- `rollback_or_stop`
- `availability_status`

Recommended availability values:

`UNKNOWN | AVAILABLE | UNAVAILABLE | UNAUTHORIZED | DEGRADED`

## Example registry

```yaml
- id: terminal.local
  class: TERMINAL
  purpose: run repository scripts and tests
  read_or_write: write-capable
  risk: MEDIUM
  requires_authorization: project-local
  availability_status: UNKNOWN
  evidence: command-output

- id: browser.playwright
  class: BROWSER
  purpose: inspect and exercise the running product
  read_or_write: interactive
  risk: LOW
  requires_authorization: project-local
  availability_status: UNKNOWN
  evidence: journey-result-and-runtime-observation

- id: github.repository
  class: GITHUB
  purpose: inspect repository state and authorized collaboration operations
  read_or_write: read/write-capable
  risk: MEDIUM
  requires_authorization: repository
  availability_status: UNKNOWN
  evidence: git-object-or-api-result
```

The examples are abstract adapter identifiers. YON must not claim they exist until the environment confirms them.

## Risk and authority

### LOW

Read-only inspection, non-destructive browser QA, local validation and other reversible observation.

### MEDIUM

Code edits, dependency installation, generated assets, branch/commit operations and other reversible mutations.

### HIGH

Production changes, destructive actions, database migrations, billing, authentication/authorization, tenancy boundaries, security controls and critical external integrations.

HIGH-risk actions require explicit authorization appropriate to the environment and evidence proportional to the consequence.

## Tool chaining

A chain is valid only when each step has a reason based on the previous result:

`QUESTION → TOOL A → EVIDENCE A → DECISION → TOOL B → EVIDENCE B → ... → VERIFY`

If Tool A resolves the question, do not execute Tool B.

If Tool A fails because the adapter is unavailable, mark the action `BLOCKED` unless a safe alternative can produce equivalent evidence.

## Privacy and boundaries

The registry must never contain:

- secrets or credentials
- customer data
- private prompts
- proprietary code
- confidential business rules
- hidden infrastructure details from private projects

A capability may be generalized publicly only at the level needed to describe its reusable behavior and contract.
