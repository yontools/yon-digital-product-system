# YON Digital Product System

Sistema abierto de metodología, skills, patrones, capacidades, evidencia, agentes, planificación, detección de entorno, orquestación y ejecución para diseñar, construir, mejorar y verificar productos digitales.

YON es un sistema operativo de product-engineering para trabajar con IA sobre productos reales. No es solamente una colección de prompts ni un UI kit.

## Flujo central

`OBSERVE → UNDERSTAND → DETECT → PROPOSE → IMPLEMENT → RUN → INSPECT → CORRECT → VERIFY`

## Uso con Claude Code

```bash
claude --plugin-dir /ruta/a/yon-digital-product-system
```

Después:

```text
/yon-digital-product-system:yon
```

Para la guía completa: `INSTALL-CLAUDE-CODE.md`.

## Skills principales

- `yon` — sistema maestro
- `yon-audit` — auditoría
- `yon-polish` — mejora segura
- `yon-build` — construcción
- `yon-environment` — detección del entorno
- `yon-tool-registry` — resolución de herramientas
- `yon-execute` — ejecución controlada
- `yon-execution-plan` — planificación por slices
- `yon-orchestrate` — selección y coordinación de herramientas
- `yon-business-graph` — contexto relacional
- `yon-event-engine` — eventos y reacciones
- `yon-policy` — límites de decisión
- `yon-agent-system` — agentes y autonomía acotada
- `yon-saas` — SaaS
- `yon-web` — sitios web
- `yon-landing` — landing pages
- `yon-onboarding` — onboarding
- `yon-visual` — inteligencia visual
- `yon-motion` — motion
- `yon-qa` — QA
- `yon-validate` — validación
- `yon-product-model` — modelo universal
- `yon-business-discovery` — descubrimiento del negocio
- `yon-capability-discovery` — descubrimiento de capacidades
- `yon-capability-resolver` — composición de capacidades
- `yon-blueprint` — Product Blueprint
- `yon-extract` — extracción de conocimiento
- `yon-learn` — promoción de conocimiento revisado

## Arquitectura de razonamiento

Para productos amplios o AI-native, YON puede componer:

`BUSINESS DISCOVERY → UNIVERSAL PRODUCT MODEL → BUSINESS GRAPH → EVENT ENGINE → POLICY → AGENT SYSTEM → CAPABILITIES → BLUEPRINT → EXECUTION`

No todas las capas son obligatorias. Cada una se usa solo cuando mejora una decisión real.

### Business Discovery

Entiende cómo opera realmente un negocio antes de decidir qué software necesita. Los Business Operating Archetypes son hipótesis de descubrimiento, no plantillas verticales.

### Universal Product Model

Modela conceptualmente `Party`, `Relationship`, `Role`, `Resource`, `Action`, `Event`, `State`, `Time/Temporal Rule`, `Workflow`, `Transaction`, `Communication`, `Document` y `Permission/Boundary`.

### Business Graph

Hace explícito el contexto de relaciones entre participantes, recursos, organizaciones, workflows y eventos cuando ese contexto mejora decisiones, routing, permisos, continuidad o agentes. No prescribe una base de datos de grafos.

### Event Engine

Distingue acciones/comandos de ocurrencias y permite razonar sobre reacciones, idempotencia, retries, causación, correlación y recuperación. No prescribe un broker o infraestructura concreta.

### Policy

Define condiciones de decisión y límites: `ALLOW`, `DENY`, `REQUIRE_APPROVAL`, `ESCALATE` o `BLOCKED`. Policy no reemplaza autorización ni ejecución.

### Agent System

Define agentes con identidad configurable, objetivo, contexto, herramientas, memoria, permisos, políticas, aprobación, escalamiento y autonomía acotada.

Niveles:

`1 Observer → 2 Assistant → 3 Operator → 4 Bounded Autonomous`

`MODEL CAPABILITY ≠ TOOL ACCESS ≠ AUTHORIZATION ≠ AUTONOMY`

## Flujo de construcción

`PROBLEMA → BUSINESS DISCOVERY → UNIVERSAL MODEL → GRAPH/EVENT/POLICY/AGENT CONTEXT → DISCOVERY → RESOLUTION → BLUEPRINT → EXECUTION PLAN → ENVIRONMENT → TOOL REGISTRY → ORCHESTRATION → EXECUTION → VERIFICACIÓN`

## Environment Detection

Estados de herramientas:

`UNKNOWN | SIGNALLED | AVAILABLE | UNAVAILABLE | UNAUTHORIZED | DEGRADED`

Precedencia:

`ACTUAL > AUTHORIZED > CONFIGURED > SIGNALLED > ASSUMED`

`DOCUMENTED ≠ AVAILABLE`

La detección es portable, de solo lectura y no imprime secretos ni variables de entorno completas.

## Tool & Execution Orchestration

`DECIDE → SELECT TOOL → AUTHORIZE → EXECUTE → OBSERVE → DECIDE NEXT → VERIFY`

Si una herramienta necesaria no existe, no está autorizada o no puede producir la evidencia requerida, YON usa una alternativa segura cuando sea equivalente o marca `BLOCKED`.

## Ejecución controlada

Plan:

`PLANNED → READY → IN_PROGRESS → VERIFYING → VERIFIED`

Ejecución:

`PLANNED → IN_PROGRESS → INSPECTING → CORRECTING → VERIFIED`

Orquestación:

`PLANNED → AUTHORIZED → EXECUTING → OBSERVING → DECIDING → COMPLETED`

`BLOCKED ≠ PASS`

## Capacidades reutilizables

Las capabilities representan soluciones de producto generalizables. Incluyen party & relationship management, asset management, rental management, geolocation/tracking, temporal states and expiration, notifications, customer management, roles and permissions, workflows, documents, payment tracking, audit history, business graph, event coordination, bounded agents y policy boundaries.

Una solución privada puede inspirar una capability pública solo después de generalizarla deliberadamente.

## Patrones, evidencia y aprendizaje

La evidencia conecta el trabajo real con conocimiento reutilizable. `yon-extract` crea candidatos generalizados y `yon-learn` promueve conocimiento revisado.

Estados de conocimiento:

`DISCOVERED → EXPERIMENTAL → PROVEN → DEPRECATED`

Estados de evidencia:

`UNVERIFIED | SUPPORTED | STRONG | CONTRADICTED`

## Validación continua

`scripts/validate_yon.py` valida la estructura y los contratos del sistema. GitHub Actions ejecuta el validador en push y pull request mediante `.github/workflows/validate.yml`.

La validación de producto usa gates proporcionales al riesgo: Structure, Product Journey, UX, UI, Accessibility, Runtime, Security y Regression.

## Privacidad

Este repositorio es público. No debe contener secretos, credenciales, datos privados de clientes, prompts privados, código propietario ni reglas de negocio identificables de proyectos privados.

## Estructura

```text
.claude-plugin/
discovery/
model/
environment/
orchestration/
events/
policy/
skills/
commands/
agents/
blueprints/
execution/
capabilities/
patterns/
evidence/
validation/
adapters/
scripts/
.github/workflows/validate.yml
```

## Estado

YON está en evolución. Sus capas de entorno, Tool Registry, orquestación, Business Graph, Event Engine, Policy y Agent System permiten trabajar sobre productos reales sin inventar herramientas, permisos, relaciones, eventos, decisiones o resultados.
