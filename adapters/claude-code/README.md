# Claude Code adapter

This directory defines how YON can be loaded into an AI coding workflow such as Claude Code.

## Intended behavior

The adapter should make YON's operating rules available without copying private application code or credentials into the public repository.

A project using the adapter should:

1. load the YON core rules;
2. discover the relevant command/skill for the task;
3. inspect the target repository before making changes;
4. use project-local rules as additional constraints;
5. run and verify affected flows;
6. report what was changed and verified.

## Important boundary

YON is a public methodology. The adapter must never assume that project code, secrets, customer data or private business knowledge should be contributed back to this repository.

Project-specific instructions always remain local to the project.
