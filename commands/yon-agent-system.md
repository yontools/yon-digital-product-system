# /yon-agent-system

Define or review an operational AI agent using YON's bounded-autonomy model.

## Process

1. Read `skills/yon-agent-system/SKILL.md`.
2. Read `agents/AGENT-AUTONOMY.md` and the profile template.
3. Establish the user/business outcome and operating context.
4. Define identity, objective, exclusions, context, tools, permissions, memory, channels, autonomy, approvals, escalation, stop conditions, and audit.
5. Use Business Graph and Event Engine reasoning only when they materially improve the agent behavior.
6. Resolve tool availability and authority before proposing execution.
7. Define verification for allowed, denied, approval, boundary, failure, and stop behavior.
8. Keep private implementation details private.

## Rules

- Do not equate model capability with authority.
- Do not infer permission from tool availability.
- Do not silently raise autonomy level.
- Do not bypass tenant, privacy, security, or approval boundaries.
- Unknown required authority or capability is `BLOCKED`.
- High-risk actions require explicit policy and proportional verification.

## Output

Return an agent profile, autonomy level, context/tool boundary, approval and escalation rules, verification gates, unresolved blockers, and next implementation step.
