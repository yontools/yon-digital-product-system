# YON Digital Product System

Sistema abierto de metodología, skills, patrones, capacidades, evidencia, agentes, planificación, orquestación y ejecución para diseñar, construir, mejorar y verificar productos digitales.

## Qué es YON

YON es un sistema operativo de product-engineering para trabajar con IA sobre productos reales. No es solamente una colección de prompts ni un UI kit.

Su objetivo es que una IA pueda entender el producto antes de modificarlo, detectar oportunidades de mejora, reutilizar soluciones probadas, convertir decisiones en un plan controlado, seleccionar las herramientas adecuadas, implementar, inspeccionar el producto real, corregir y verificar el resultado.

## Flujo central

`OBSERVE → UNDERSTAND → DETECT → PROPOSE → IMPLEMENT → RUN → INSPECT → CORRECT → VERIFY`

## Uso con Claude Code

YON está empaquetado como plugin de Claude Code.

### Probar localmente

```bash
claude --plugin-dir /ruta/a/yon-digital-product-system
```

Después:

```text
/yon-digital-product-system:yon
```

También podés pedir directamente:

```text
Usá YON para auditar este SaaS y encontrá los problemas de mayor impacto.
```

Para ver la guía completa: `INSTALL-CLAUDE-CODE.md`.

## Skills principales

- `yon` — sistema maestro y ciclo completo
- `yon-audit` — auditoría sin modificar
- `yon-polish` — mejora segura de producto existente
- `yon-build` — construcción de un producto nuevo
- `yon-execute` — ejecución controlada de un Blueprint mediante slices, runtime inspection, corrección y verificación
- `yon-execution-plan` — convierte un Blueprint en slices ejecutables, dependencias, criterios de aceptación y checkpoints de verificación
- `yon-orchestrate` — selecciona y coordina la herramienta mínima necesaria para ejecutar una acción real con autorización, riesgo y evidencia
- `yon-saas` — diseño y construcción de SaaS
- `yon-web` — sitios web
- `yon-landing` — landing pages
- `yon-onboarding` — onboarding
- `yon-visual` — inteligencia visual
- `yon-motion` — motion y microinteracciones
- `yon-qa` — verificación del producto real
- `yon-validate` — validación estructural y de producto
- `yon-product-model` — modelado conceptual universal del producto
- `yon-business-discovery` — descubrimiento del modelo operativo del negocio mediante arquetipos de operación
- `yon-capability-discovery` — descubrimiento de capacidades, patrones y gaps
- `yon-capability-resolver` — composición mínima de capacidades reutilizables
- `yon-blueprint` — creación y refinamiento del Product Blueprint
- `yon-extract` — extracción deliberada de conocimiento generalizable desde evidencia
- `yon-learn` — promoción deliberada de conocimiento revisado hacia patterns/capabilities

Las skills especializadas de `product-design`, `ux`, `ui`, `saas`, `onboarding` y `qa` aportan conocimiento reutilizable adicional.

## Business Discovery

YON incorpora una capa de **Business Discovery** para entender cómo opera realmente un negocio antes de decidir qué software necesita.

La idea central es evitar plantillas rígidas del tipo "software para barbería", "software para clínica" o "software para lavadero". Una categoría empresarial no determina por sí sola sus workflows.

YON identifica **Business Operating Archetypes**: formas recurrentes de operar que pueden aparecer en múltiples industrias, como `Service Delivery`, `Appointment & Scheduling`, `Request → Order → Execution`, `Rental & Temporary Use`, `Asset & Field Operations`, `Commerce & Fulfillment`, `Case / Ticket / Work Management`, `Membership & Subscription`, `Marketplace & Matching`, `Approval & Authorization` o `Intake → Assessment → Decision → Follow-up`.

Un negocio puede combinar varios arquetipos. Cada arquetipo es una **hipótesis de descubrimiento**, no una lista automática de funcionalidades, arquitectura, esquema de base de datos ni paquete SaaS.

El flujo ampliado es:

`BUSINESS REQUEST → OBSERVE OPERATION → IDENTIFY ARCHETYPES → MODEL WORKFLOWS → DISCOVER CAPABILITIES → RESOLVE → BLUEPRINT`

Referencia: `discovery/BUSINESS-OPERATING-ARCHETYPES.md` y `discovery/BUSINESS-DISCOVERY-TEMPLATE.md`.

## Universal Product Model

YON incorpora una capa conceptual posterior al entendimiento del negocio y anterior a las capabilities: el **Universal Product Model**.

Su propósito es que YON pueda reconocer estructuras comunes entre productos de dominios muy diferentes sin imponer una arquitectura única. Usa primitivas como `Party`, `Relationship`, `Role`, `Resource`, `Action`, `Event`, `State`, `Time/Temporal Rule`, `Workflow`, `Transaction`, `Communication`, `Document` y `Permission/Boundary`.

El modelo **no es** un esquema de base de datos, ORM, framework, arquitectura automática ni API universal. No todos los productos necesitan todas las primitivas y una primitiva conceptual no implica que deba existir una capability reutilizable.

## Descubrimiento, composición, Blueprint y ejecución

YON separa **descubrir**, **resolver**, **definir el contrato de construcción**, **planificar**, **orquestar** y **ejecutar**.

El flujo para productos amplios es:

`PROBLEMA → BUSINESS DISCOVERY → UNIVERSAL MODEL → DISCOVERY → RESOLUTION → BLUEPRINT → EXECUTION PLAN → ORCHESTRATION → EXECUTION → VERIFICACIÓN`

`yon-business-discovery` entiende el modelo operativo del negocio y evita inferir requisitos desde la etiqueta del rubro.

`yon-capability-discovery` descompone el workflow real, busca conocimiento reutilizable, clasifica candidatos como `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING` o `PRODUCT-SPECIFIC`, y determina si un gap podría ser candidato a YON, debe permanecer específico del producto o necesita más evidencia.

`yon-capability-resolver` transforma ese descubrimiento en la composición mínima justificada y define límites, dependencias y orden de implementación.

`yon-blueprint` convierte el entendimiento y la resolución en un **Product Blueprint**: participantes, relaciones, jobs, workflows, entidades, lifecycle, capacidades, patrones, gaps, comportamiento específico, riesgos y gates de verificación.

`yon-execution-plan` transforma el Blueprint en un plan operativo: slices verticales, dependencias, criterios de aceptación observables, riesgos, checkpoints, regresiones y condiciones de bloqueo.

`yon-orchestrate` conecta cada slice con la herramienta concreta que pueda producir la evidencia necesaria: repositorio, terminal, browser, tests, GitHub, deployment/infrastructure, database o visual/media. La herramienta se elige por suficiencia de evidencia, no por disponibilidad o moda.

`yon-execute` utiliza ese plan y la capa de orquestación para implementar, ejecutar el producto real, inspeccionar, corregir y volver a verificar. Si una decisión crítica no está resuelta o una verificación de alto riesgo no puede realizarse, bloquea en lugar de inventar o declarar éxito.

El Blueprint, Execution Plan, Orchestration Layer y Execution Engine son contratos de decisión/orquestación, no una arquitectura automática ni un esquema de base de datos. No autorizan a cambiar innecesariamente un producto que ya funciona.

## Tool & Execution Orchestration

La capa `orchestration/` define el contrato entre la intención de YON y las herramientas reales del entorno.

Su principio es:

`DECIDE → SELECT TOOL → AUTHORIZE → EXECUTE → OBSERVE → DECIDE NEXT → VERIFY`

YON usa un **Tool Capability Registry** para separar la capacidad abstracta de su implementación concreta. Una capacidad no se considera disponible simplemente porque esté documentada: el entorno debe confirmar que el adaptador existe, está autorizado y puede producir evidencia.

Referencia: `orchestration/README.md`, `orchestration/TOOL-CAPABILITY-REGISTRY.md`, `orchestration/TOOL-CAPABILITY-MATRIX.md` y `orchestration/TOOL-ADAPTER-TEMPLATE.md`.

### Regla fundamental

`DOCUMENTED ≠ AVAILABLE`

Si una herramienta necesaria no existe, no está autorizada o no puede producir la evidencia requerida, YON debe usar una alternativa segura cuando sea equivalente o marcar `BLOCKED`.

El objetivo no es utilizar muchas herramientas. Es producir el máximo progreso justificable con el mínimo riesgo y la mínima complejidad.

## Ejecución controlada

El plan sigue:

`PLANNED → READY → IN_PROGRESS → VERIFYING → VERIFIED`

La ejecución sigue:

`PLANNED → IN_PROGRESS → INSPECTING → CORRECTING → VERIFIED`

o, cuando corresponde:

`IN_PROGRESS / VERIFYING → BLOCKED`

La orquestación añade:

`PLANNED → AUTHORIZED → EXECUTING → OBSERVING → DECIDING → COMPLETED`

`BLOCKED` nunca equivale a `VERIFIED` ni a `PASS`.

La ejecución prioriza slices verticales, valor observable, dependencias, riesgo y verificabilidad. No convierte cada mejora detectada en alcance obligatorio.

## Agentes

YON incluye especialistas para:

- product design
- UX review
- UI review
- QA review

Los agentes analizan sin editar cuando la tarea requiere una revisión especializada.

## Capacidades reutilizables

Las capabilities representan soluciones de producto generalizables que pueden combinarse al crear nuevos sistemas.

Ejemplos:

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

Una solución de un proyecto privado puede inspirar una capability pública, pero solo después de generalizarla deliberadamente.

## Patrones

Los patrones resuelven problemas recurrentes de producto e interfaz y documentan contexto, solución, variantes, trade-offs, accesibilidad, responsive y verificación.

## Evidencia, aprendizaje y evolución

La evidencia conecta el trabajo real con el conocimiento reutilizable. Puede registrar observaciones, feedback, experimentos, verificaciones de runtime, regresiones y resultados de producción.

La evidencia no convierte automáticamente una solución en `PROVEN`. YON distingue hechos observados de inferencias y exige revisión antes de promover conocimiento.

Cuando una solución parece reutilizable, `yon-extract` puede generar un candidato de pattern o capability. `yon-learn` puede promover un candidato revisado; extracción y publicación son pasos deliberadamente separados.

Estados de conocimiento: `DISCOVERED → EXPERIMENTAL → PROVEN → DEPRECATED`.

## Validación continua

YON incluye un validador estructural portable en `scripts/validate_yon.py`. Comprueba integridad básica del plugin, skills, commands, agents e índices/referencias locales.

GitHub Actions ejecuta ese validador en cada push y pull request mediante `.github/workflows/validate.yml`.

La validación de producto usa gates proporcionales al riesgo: Structure, Product Journey, UX, UI, Accessibility, Runtime, Security y Regression.

## Privacidad

Este repositorio es público. No debe contener secretos, credenciales, datos privados de clientes, prompts privados, código propietario ni reglas de negocio identificables de Yontools, Vantto u otros proyectos privados.

El conocimiento generalizable puede evolucionar en YON; el material privado permanece en el proyecto privado.

## Estructura

```text
.claude-plugin/
└── plugin.json

discovery/
├── README.md
├── BUSINESS-OPERATING-ARCHETYPES.md
└── BUSINESS-DISCOVERY-TEMPLATE.md

model/
├── README.md
├── UNIVERSAL-PRODUCT-MODEL.md
└── PRODUCT-MODEL-TEMPLATE.md

skills/
├── yon/
├── yon-audit/
├── yon-polish/
├── yon-build/
├── yon-execute/
├── yon-execution-plan/
├── yon-orchestrate/
├── yon-saas/
├── yon-web/
├── yon-landing/
├── yon-onboarding/
├── yon-visual/
├── yon-motion/
├── yon-qa/
├── yon-validate/
├── yon-product-model/
├── yon-business-discovery/
├── yon-capability-discovery/
├── yon-capability-resolver/
├── yon-blueprint/
├── yon-extract/
├── yon-learn/
├── product-design/
├── ux/
├── ui/
├── saas/
├── onboarding/
└── qa/

agents/
├── product-designer.md
├── ux-reviewer.md
├── ui-reviewer.md
└── qa-reviewer.md

blueprints/
├── README.md
└── BLUEPRINT-TEMPLATE.md

execution/
├── README.md
└── EXECUTION-PLAN-TEMPLATE.md

orchestration/
├── README.md
├── TOOL-CAPABILITY-REGISTRY.md
├── TOOL-CAPABILITY-MATRIX.md
└── TOOL-ADAPTER-TEMPLATE.md

capabilities/
patterns/
evidence/
validation/
commands/
adapters/
scripts/
└── validate_yon.py
.github/
└── workflows/
    └── validate.yml
```

## Estado

YON está en evolución. Las capacidades y patrones usan estados como `experimental`, `proven` y `deprecated` para diferenciar ideas de soluciones con evidencia.

La evidencia usa `UNVERIFIED`, `SUPPORTED`, `STRONG` y `CONTRADICTED` para expresar cuánto respalda una afirmación. Son sistemas distintos y no deben confundirse.
