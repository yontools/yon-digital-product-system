# YON Environment Detection Rules

## Objective

Detect enough of the current environment to choose a safe and effective tool. Detection is evidence gathering, not architecture generation.

## Project detection

Inspect, when present:

- repository root markers (`.git`, package manifests, common workspace files)
- local instruction files such as `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md` and project-specific instructions
- package manifests and lockfiles
- runtime/config files
- scripts and test configuration
- deployment configuration

Do not require a particular file layout.

## Stack detection

Use direct signals first:

- `package.json` scripts/dependencies
- lockfiles
- Python project metadata
- framework configuration files
- test configuration
- deployment configuration

A dependency or config file is a **signal**, not proof that the corresponding service is reachable or usable.

## Tool detection

A tool may be classified `AVAILABLE` only after an observable availability check appropriate to that adapter, such as an executable lookup or a safe read-only capability check.

Examples:

- `git` executable found → Git tool signal can become `AVAILABLE` for local Git inspection.
- `node`/package manager found → runtime tool can become `AVAILABLE` for that runtime.
- Playwright dependency/config found → browser automation is `SIGNALLED`; it becomes `AVAILABLE` only when the required execution path is confirmed.
- Vercel/Supabase config → deployment/database capability is `SIGNALLED`; it does not prove authentication, project access or authorization.

Never infer authorization from installation alone.

## Authority detection

Separate these questions:

1. Can the tool be executed?
2. Can it read the target?
3. Can it mutate the target?
4. Is the requested action authorized?
5. Can the result be verified?

If a required answer is unknown, keep the action `BLOCKED` or perform the smallest safe read-only detection step.

## Confidence

Use:

- `HIGH` — directly observed from the environment.
- `MEDIUM` — strong repository/config signal.
- `LOW` — indirect or incomplete signal.

Never convert a LOW signal into tool availability.

## Conflict resolution

When signals disagree:

`actual availability > local instructions/config > manifest/scripts > generic assumptions`

Preserve the conflict in the profile instead of silently resolving it.

## Safety

Detection must be non-destructive by default. It must not:

- print secrets or credential values
- modify dependencies
- migrate databases
- deploy
- delete data
- alter production state
- copy private project material into public YON

## Output

A useful profile ends with a concrete decision:

`READY FOR ACTION`, `NEEDS SAFE DETECTION`, or `BLOCKED`

and identifies the evidence and missing condition behind that decision.
