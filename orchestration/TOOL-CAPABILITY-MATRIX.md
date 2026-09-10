# YON Tool Capability Matrix

This matrix defines the **decision boundary** between YON's intent and concrete adapters.

| Product need | Evidence required | Capability class | Default risk | Escalation |
|---|---|---|---|---|
| Understand repository | files, routes, dependencies, instructions | REPOSITORY | LOW | TERMINAL |
| Change implementation | diff + affected behavior | REPOSITORY | MEDIUM | TEST / BROWSER |
| Run build or script | command result | TERMINAL | LOW/MEDIUM | targeted diagnosis |
| Verify user journey | runtime interaction | BROWSER | LOW | TEST |
| Verify regression | reproducible check | TEST | LOW/MEDIUM | BROWSER |
| Inspect CI | workflow/check result | GITHUB | LOW | TERMINAL or GitHub logs |
| Create branch/PR | GitHub object | GITHUB | MEDIUM | review |
| Deploy preview | provider result | DEPLOYMENT | MEDIUM | runtime verification |
| Change production | deployment + runtime evidence | DEPLOYMENT | HIGH | explicit authorization |
| Query application data | bounded query result | DATABASE | MEDIUM | runtime/product evidence |
| Change schema/data | migration + integrity evidence | DATABASE | HIGH | rollback/backup plan |
| Create custom visual | generated/inspected asset | VISUAL | LOW/MEDIUM | UI verification |
| Add meaningful video | media artifact + product relevance | MEDIA | LOW/MEDIUM | performance/accessibility |

## Minimum evidence by mutation

### Read-only

The tool result itself is normally sufficient, provided it answers the question and the source is authoritative.

### Code mutation

Require at least:

1. resulting diff;
2. relevant build/test result;
3. runtime evidence when behavior is user-visible.

### External mutation

Require:

1. authorization;
2. exact target/scope;
3. provider result;
4. post-mutation inspection;
5. rollback or recovery path when applicable.

### High-risk mutation

Require all of the above plus explicit high-risk verification. If any critical evidence cannot be obtained, the final result is `BLOCKED`, not `PASS`.

## Fallback policy

A fallback is valid only when it answers the **same question with equivalent evidence** and does not increase risk unnecessarily.

Example:

`BROWSER unavailable → static source inspection` is valid only for questions that do not require runtime behavior.

It is not valid to claim a runtime journey passed based solely on source inspection.

## No-tool rule

YON should sometimes choose **no tool**:

- the required evidence is already available;
- the requested change is not justified;
- the next action is blocked by an unresolved product decision;
- executing a tool would create risk without increasing useful evidence.

The goal is not maximum tool usage. The goal is maximum justified progress.
