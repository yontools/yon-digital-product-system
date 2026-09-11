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

## Business Discovery

YON incorpora una capa de **Business Discovery** para entender cómo opera realmente un negocio antes de decidir qué software necesita.

Evita plantillas rígidas del tipo "software para barbería", "software para clínica" o "software para lavadero". Una categoría empresarial no determina por sí sola sus workflows.

YON identifica **Business Operating Archetypes**: formas recurrentes de operar que pueden aparecer en múltiples industrias, como `Service Delivery`, `Appointment & Scheduling`, `Request → Order → Execution`, `Rental & Temporary Use`, `Asset & Field Operations`, `Commerce & Fulfillment`, `Case / Ticket / Work Management`, `Membership & Subscription`, `Marketplace & Matching`, `Approval & Authorization` o `Intake → Assessment → Decision → Follow-up`.

Cada arquetipo es una hipótesis de descubrimiento, no una lista automática de funcionalidades, arquitectura, esquema de base de datos ni paquete SaaS.

## Universal Product Model

El **Universal Product Model** es una capa conceptual posterior al entendimiento del negocio y anterior a las capabilities. Usa primitivas como `Party`, `Relationship`, `Role`, `Resource`, `Action`, `Event`, `State`, `Time/Temporal Rule`, `Workflow`, `Transaction`, `Communication`, `Document` y `Permission/Boundary`.

No es un esquema de base de datos, ORM, framework, arquitectura automática ni API universal.

## Contexto relacional, eventos, políticas y agentes

Para productos amplios o AI-native, YON puede componer cuatro capas distintas:

`UNIVERSAL PRODUCT MODEL → BUSINESS GRAPH → EVENT ENGINE → POLICY / AGENT SYSTEM`

- **Business Graph** — entiende relaciones significativas entre participantes, recursos, contextos y workflows.
- **Event Engine** — registra ocurrencias significativas y coordina reacciones.
- **Policy** — define condiciones de decisión, aprobación, denegación, escalamiento o bloqueo.
- **Agent System** — permite que agentes observen, razonen y actúen dentro de límites explícitos.

Estas capas no son arquitectura obligatoria. Se usan solo cuando mejoran el resultado del producto.

Distinciones fundamentales:

`ACTION ≠ EVENT`

`RELATIONSHIP ≠ AUTHORIZATION`

`TOOL AVAILABILITY ≠ AUTHORITY`

`MODEL CAPABILITY ≠ AUTONOMY`

`POLICY DECISION ≠ EXECUTION`

La autonomía de agentes se expresa como:

`1 Observer → 2 Assistant → 3 Operator → 4 Bounded Autonomous`

Mayor capacidad del modelo no implica mayor autoridad.

## Descubrimiento, composición, Blueprint y ejecución

YON separa **descubrir**, **resolver**, **definir el contrato de construcción**, **planificar**, **orquestar** y **ejecutar**.

El flujo para productos amplios es:

`PROBLEMA → BUSINESS DISCOVERY → UNIVERSAL MODEL → GRAPH/EVENT/POLICY/AGENT CONTEXT → DISCOVERY → RESOLUTION → BLUEPRINT → EXECUTION PLAN → ENVIRONMENT → ORCHESTRATION → EXECUTION → VERIFICACIÓN`

`yon-business-discovery` entiende el modelo operativo del negocio.

`yon-capability-discovery` descompone workflows y clasifica candidatos como `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING` o `PRODUCT-SPECIFIC`.

`yon-capability-resolver` transforma ese descubrimiento en la composición mínima justificada.

`yon-blueprint` convierte el entendimiento y la resolución en un **Product Blueprint**.

`yon-execution-plan` transforma el Blueprint en slices verticales, dependencias, criterios de aceptación, riesgos, checkpoints y bloqueos explícitos.

`yon-environment` reconoce el entorno real antes de que YON dependa de una herramienta concreta.

`yon-tool-registry` resuelve el estado de los adapters a partir de evidencia del entorno.

`yon-orchestrate` conecta cada slice con la herramienta concreta que pueda producir la evidencia necesaria.

`yon-execute` implementa, ejecuta el producto real, inspecciona, corrige y vuelve a verificar.

## Environment Detection

La capa `environment/` permite que YON responda antes de actuar:

1. ¿Dónde estoy trabajando?
2. ¿Qué stack y señales existen?
3. ¿Qué herramientas están realmente disponibles?
4. ¿Cuáles están solamente señaladas por configuración?
5. ¿Qué autoridad existe para la acción?
6. ¿Qué evidencia respalda cada conclusión?
7. ¿Qué sigue bloqueado o desconocido?

Estados de disponibilidad:

`UNKNOWN | SIGNALLED | AVAILABLE | UNAVAILABLE | UNAUTHORIZED | DEGRADED`

Regla de precedencia:

`ACTUAL > AUTHORIZED > CONFIGURED > SIGNALLED > ASSUMED`

Regla fundamental:

`DOCUMENTED ≠ AVAILABLE`

El detector `scripts/detect_environment.py` es portable y de solo lectura. No imprime secretos ni variables de entorno completas. La detección tampoco instala, despliega, migra ni modifica producción.

## Tool & Execution Orchestration

La capa `orchestration/` define el contrato entre la intención de YON y las herramientas reales.

Principio:

`DECIDE → SELECT TOOL → AUTHORIZE → EXECUTE → OBSERVE → DECIDE NEXT → VERIFY`

YON usa un **Tool Capability Registry** para separar la capacidad abstracta de su implementación concreta. La disponibilidad debe confirmarse en el entorno; no se infiere desde documentación o configuración.

Si una herramienta necesaria no existe, no está autorizada o no puede producir la evidencia requerida, YON debe usar una alternativa segura cuando sea equivalente o marcar `BLOCKED`.

## Ejecución controlada

Plan:

`PLANNED → READY → IN_PROGRESS → VERIFYING → VERIFIED`

Ejecución:

`PLANNED → IN_PROGRESS → INSPECTING → CORRECTING → VERIFIED`

Orquestación:

`PLANNED → AUTHORIZED → EXECUTING → OBSERVING → DECIDING → COMPLETED`

`BLOCKED` nunca equivale a `VERIFIED` ni a `PASS`.

## Capacidades reutilizables

Las capabilities representan soluciones de producto generalizables. Ejemplos:

- party & relationship management
- asset management
- rental management
- geolocation/tracking
- temporal states and expiration
- notifications
- customer management
- roles and permissions
- workflows
- documents
- payment tracking
- audit history
- business graph / relationship context
- event-driven coordination
- agentic operations & bounded autonomy
- policy & decision boundaries

Una solución de un proyecto privado puede inspirar una capability pública, pero solo después de generalizarla deliberadamente.

## Patrones, evidencia y aprendizaje

Los patrones resuelven problemas recurrentes de producto e interfaz.

La evidencia conecta el trabajo real con el conocimiento reutilizable: observaciones, feedback, experimentos, runtime verification, regresiones y resultados de producción.

La evidencia no convierte automáticamente una solución en `PROVEN`. `yon-extract` crea candidatos generalizados y `yon-learn` promueve conocimiento revisado.

Estados de conocimiento:

`DISCOVERED → EXPERIMENTAL → PROVEN → DEPRECATED`

Estados de evidencia:

`UNVERIFIED | SUPPORTED | STRONG | CONTRADICTED`

## Validación continua

`scripts/validate_yon.py` valida la estructura del sistema, incluyendo plugin, skills, commands, agents, environment, orchestration, graph/event/agent y policy contracts.

GitHub Actions ejecuta el validador en push y pull request mediante `.github/workflows/validate.yml`.

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

YON está en evolución. Las capabilities y patterns usan estados de madurez para diferenciar ideas de soluciones con evidencia. La detección de entorno, el Tool Registry, la orquestación, el Business Graph, el Event Engine, Policy y el Agent System agregan capas operacionales y de razonamiento para que YON pueda trabajar sobre productos reales sin inventar herramientas, permisos, relaciones, eventos, decisiones o resultados.
