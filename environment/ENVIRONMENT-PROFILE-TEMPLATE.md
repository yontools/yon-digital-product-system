# YON Environment Profile

> Perfil local de referencia. Completar con evidencia observable; no inventar disponibilidad.

## 1. Identity

- Profile ID:
- Project root:
- Repository:
- Branch/ref:
- Detected at:
- Profile state: `DETECTED | PARTIAL | BLOCKED`

## 2. Local instructions

- Repository instructions:
- Agent/IDE instructions:
- Deployment/runtime instructions:
- Relevant constraints:

## 3. Stack signals

| Area | Signal | Evidence | Confidence |
|---|---|---|---|
| Runtime | | | |
| Language | | | |
| Framework | | | |
| Package manager | | | |
| Database | | | |
| Styling/UI | | | |
| Testing | | | |
| Browser automation | | | |
| Deployment | | | |

## 4. Project scripts

- dev:
- build:
- test:
- lint:
- typecheck:
- e2e:
- other relevant scripts:

## 5. Tool adapters

| Adapter | Class | Availability | Evidence | Risk | Authorization |
|---|---|---|---|---|---|
| | | `UNKNOWN/SIGNALLED/AVAILABLE/UNAVAILABLE/UNAUTHORIZED/DEGRADED` | | | |

## 6. Authority

Record only whether the environment provides enough authority for the next action. Never record secrets.

- repository read:
- repository write:
- local execution:
- browser execution:
- test execution:
- GitHub operations:
- deployment operations:
- database operations:
- external integrations:
- high-risk approval:

## 7. Evidence

For every important detection, record the source used: command result, file/config signal, package manifest, tool probe, or explicit authorization.

## 8. Blockers

- Missing tool:
- Missing permission:
- Missing input:
- Conflicting signals:
- Required verification unavailable:

## 9. Privacy

- No secrets copied:
- No customer data copied:
- No proprietary code copied:
- No private architecture/business rules copied:

## 10. Handoff to orchestration

The profile should answer:

1. What environment are we in?
2. Which tools are actually available?
3. Which tools are only signalled?
4. Which actions are authorized?
5. What remains unknown?
6. What is the smallest safe next detection or execution action?
