# YON Digital Product System

Sistema abierto de metodología, skills, patrones, capacidades, evidencia, agentes, planificación, detección de entorno, orquestación y ejecución para diseñar, construir, mejorar y verificar productos digitales.

## Qué es YON

YON es un sistema operativo de product-engineering para trabajar con IA sobre productos reales. No es solamente una colección de prompts ni un UI kit.

Su objetivo es que una IA pueda entender el producto antes de modificarlo, detectar oportunidades de mejora, reutilizar soluciones probadas, convertir decisiones en un plan controlado, reconocer el entorno real, seleccionar herramientas adecuadas, implementar, inspeccionar el producto real, corregir y verificar el resultado.

## Flujo central

`OBSERVE → UNDERSTAND → DETECT → PROPOSE → IMPLEMENT → RUN → INSPECT → CORRECT → VERIFY`

## Uso con Claude Code

YON está empaquetado como plugin de Claude Code.

```bash
claude --plugin-dir /ruta/a/yon-digital-product-system
```

Después:

```text
/yon-digital-product-system:yon
```

También podés pedir:

```text
Usá YON para auditar este SaaS y encontrá los problemas de mayor impacto.
```

Para la guía completa: `INSTALL-CLAUDE-CODE.md`.

## Skills principales

- `yon` — sistema maestro y ciclo completo
- `yon-audit` — auditoría sin modificar
- `yon-polish` — mejora segura de producto existente
- `yon-build` — construcción de producto nuevo
- `yon-environment` — detección del proyecto, stack, herramientas y autoridad
- `yon-tool-registry` — resolución de herramientas disponibles y autorizadas
- `yon-execute` — ejecución controlada de un Blueprint mediante slices, runtime inspection, corrección y verificación
- `yon-execution-plan` — convierte un Blueprint en slices ejecutables, dependencias, criterios de aceptación y checkpoints
- `yon-orchestrate` — selecciona y coordina la herramienta mínima necesaria con autorización, riesgo y evidencia
- `yon-business-graph` — contexto de relaciones y conexiones significativas
- `yon-event-engine` — eventos, reacciones, idempotencia y coordinación
- `yon-policy` — límites de decisión, aprobación, denegación y bloqueo
- `yon-agent-system` — agentes con herramientas, contexto y autonomía acotada
- `yon-saas` — diseño y construcción de SaaS
- `yon-web` — sitios web
- `yon-landing` — landing pages
- `yon-onboarding` — onboarding
- `yon-visual` — inteligencia visual
- `yon-motion` — motion y microinteracciones
- `yon-qa` — verificación del producto real
- `yon-validate` — validación estructural y de producto
- `yon-product-model` — modelado conceptual universal del producto
- `yon-business-discovery` — descubrimiento del modelo operativo del negocio
- `yon-capability-discovery` — descubrimiento de capacidades, patrones y gaps
- `yon-capability-resolver` — composición mínima de capacidades reutilizables
- `yon-blueprint` — Product Blueprint
- `yon-extract` — extracción deliberada de conocimiento generalizable
- `yon-learn` — promoción deliberada de conocimiento revisado

Las skills especializadas de `product-design`, `ux`, `ui`, `saas`, `onboarding` y `qa` aportan conocimiento reutilizable adicional.

## Arquitectura de razonamiento

Para productos amplios o AI-native, YON puede componer capas distintas:

`BUSINESS DISCOVERY → UNIVERSAL PRODUCT MODEL → BUSINESS GRAPH → EVENT ENGINE → POLICY → AGENT SYSTEM → CAPABILITIES → BLUEPRINT → EXECUTION`

No todas son obligatorias. Cada capa se usa solo cuando mejora una decisión real.

### Business Discovery

Entiende cómo opera realmente un negocio antes de decidir qué software necesita. Usa Business Operating Archetypes como hipótesis de descubrimiento, no como plantillas verticales.

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

`yon-capability-discovery` descompone workflows y clasifica candidatos como `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING` o `PRODUCT-SPECIFIC`.

`yon-capability-resolver` transforma ese descubrimiento en la composición mínima justificada.

`yon-blueprint` convierte decisiones en un contrato de producto.

`yon-execution-plan` transforma el Blueprint en slices verticales, dependencias, criterios de aceptación, riesgos, checkpoints y bloqueos explícitos.

`yon-environment` reconoce el entorno real.

`yon-tool-registry` resuelve disponibilidad, autorización y degradación de herramientas.

`yon-orchestrate` selecciona la herramienta mínima capaz de producir la evidencia necesaria.

`yon-execute` implementa, ejecuta el producto real, inspecciona, corrige y vuelve a verificar.

## Distinciones fundamentales

`ACTION ≠ EVENT`

`RELATIONSHIP ≠ AUTHORIZATION`

`TOOL AVAILABILITY ≠ AUTHORITY`

`MODEL CAPABILITY ≠ AUTONOMY`

`POLICY DECISION ≠ EXECUTION`

`BLOCKED ≠ PASS`

## Environment Detection

La capa `environment/` detecta proyecto, stack, herramientas, autoridad y evidencia. Estados:

`UNKNOWN | SIGNALLED | AVAILABLE | UNAVAILABLE | UNAUTHORIZED | DEGRADED`

Precedencia:

`ACTUAL > AUTHORIZED > CONFIGURED > SIGNALLED > ASSUMED`

`DOCUMENTED ≠ AVAILABLE`

El detector es portable, de solo lectura y no imprime secretos ni variables de entorno completas.

## Tool & Execution Orchestration

Principio:

`DECIDE → SELECT TOOL → AUTHORIZE → EXECUTE → OBSERVE → DECIDE NEXT → VERIFY`

Si una herramienta necesaria no existe, no está autorizada o no puede producir la evidencia requerida, YON debe usar una alternativa segura cuando sea equivalente o marcar `BLOCKED`.

## Ejecución controlada

Plan:

`PLANNED → READY → IN_PROGRESS → VERIFYING → VERIFIED`

Ejecución:

`PLANNED → IN_PROGRESS → INSPECTING → CORRECTING → VERIFIED`

Orquestación:

`PLANNED → AUTHORIZED → EXECUTING → OBSERVING → DECIDING → COMPLETED`

## Capacidades reutilizables

Las capabilities representan soluciones de producto generalizables. Ejemplos: party & relationship management, asset management, rental management, geolocation/tracking, temporal states and expiration, notifications, customer management, roles and permissions, workflows, documents, payment tracking, audit history, business graph, event coordination, bounded agents y policy boundaries.

Una solución privada puede inspirar una capability pública solo después de generalizarla deliberadamente.

## Patrones, evidencia y aprendizaje

La evidencia conecta el trabajo real con conocimiento reutilizable. `yon-extract` crea candidatos generalizados y `yon-learn` promueve conocimiento revisado.

Estados de conocimiento:

`DISCOVERED → EXPERIMENTAL → PROVEN → DEPRECATED`

Estados de evidencia:

`UNVERIFIED | SUPPORTED | STRONG | CONTRADICTED`

## Validación continua

`scripts/validate_yon.py` valida la estructura del sistema y los contratos de environment, orchestration, graph/event/agent y policy. GitHub Actions ejecuta el validador en push y pull request mediante `.github/workflows/validate.yml`.

La validación de producto usa gates proporcionales al riesgo: Structure, Product Journey, UX, UI, Accessibility, Runtime, Security y Regression.

## Privacidad

Este repositorio es público. No debe contener secretos, credenciales, datos privados de clientes, prompts privados, código propietario ni reglas de negocio identificables de proyectos privados.

El conocimiento generalizable puede evolucionar en YON; el material privado permanece en el proyecto privado.

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
ag​ents/
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

YON está en evolución. La detección de entorno, el Tool Registry, la orquestación, el Business Graph, el Event Engine, Policy y el Agent System agregan capas para que YON pueda trabajar sobre productos reales sin inventar herramientas, permisos, relaciones, eventos, decisiones o resultados.
