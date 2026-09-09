# YON Digital Product System

Sistema abierto de metodología, skills, patrones, capacidades, evidencia y agentes para diseñar, construir, mejorar y verificar productos digitales.

## Qué es YON

YON es un sistema operativo de product-engineering para trabajar con IA sobre productos reales. No es solamente una colección de prompts ni un UI kit.

Su objetivo es que una IA pueda entender el producto antes de modificarlo, detectar oportunidades de mejora, reutilizar soluciones probadas, implementar de forma segura y verificar el resultado real.

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
- `yon-saas` — diseño y construcción de SaaS
- `yon-web` — sitios web
- `yon-landing` — landing pages
- `yon-onboarding` — onboarding
- `yon-visual` — inteligencia visual
- `yon-motion` — motion y microinteracciones
- `yon-qa` — verificación del producto real
- `yon-validate` — validación estructural y de producto
- `yon-product-model` — modelado conceptual universal del producto
- `yon-capability-discovery` — descubrimiento de capacidades, patrones y gaps
- `yon-capability-resolver` — composición mínima de capacidades reutilizables
- `yon-blueprint` — creación y refinamiento del Product Blueprint
- `yon-extract` — extracción deliberada de conocimiento generalizable desde evidencia
- `yon-learn` — promoción deliberada de conocimiento revisado hacia patterns/capabilities

Las skills especializadas de `product-design`, `ux`, `ui`, `saas`, `onboarding` y `qa` aportan conocimiento reutilizable adicional.

## Universal Product Model

YON incorpora una capa conceptual anterior a las capabilities: el **Universal Product Model**.

Su propósito es que YON pueda reconocer estructuras comunes entre productos de dominios muy diferentes sin imponer una arquitectura única. Usa primitivas como `Party`, `Relationship`, `Role`, `Resource`, `Action`, `Event`, `State`, `Time/Temporal Rule`, `Workflow`, `Transaction`, `Communication`, `Document` y `Permission/Boundary`.

El modelo **no es** un esquema de base de datos, ORM, framework, arquitectura automática ni API universal. No todos los productos necesitan todas las primitivas y una primitiva conceptual no implica que deba existir una capability reutilizable.

El flujo ampliado para productos suficientemente amplios es:

`PRODUCT → UNIVERSAL MODEL → DISCOVERY → RESOLUTION → BLUEPRINT → IMPLEMENTATION → VERIFICATION`

Referencia: `model/UNIVERSAL-PRODUCT-MODEL.md`.

## Descubrimiento, composición y Blueprint

YON separa **descubrir**, **resolver** y **definir el contrato de construcción**.

El flujo para productos amplios es:

`PROBLEMA → DISCOVERY → RESOLUTION → BLUEPRINT → IMPLEMENTACIÓN → VERIFICACIÓN`

`yon-capability-discovery` descompone el workflow real, busca conocimiento reutilizable, clasifica candidatos como `DIRECT`, `SUPPORTING`, `OPTIONAL`, `MISSING` o `PRODUCT-SPECIFIC`, y determina si un gap podría ser candidato a YON, debe permanecer específico del producto o necesita más evidencia.

`yon-capability-resolver` transforma ese descubrimiento en la composición mínima justificada y define límites, dependencias y orden de implementación.

`yon-blueprint` convierte el entendimiento y la resolución en un **Product Blueprint**: participantes, relaciones, jobs, workflows, entidades, lifecycle, capacidades, patrones, gaps, comportamiento específico, riesgos y gates de verificación.

El Blueprint es un contrato de decisión, no una arquitectura automática ni un esquema de base de datos. No autoriza a cambiar innecesariamente un producto que ya funciona.

Los Blueprints reutilizan `blueprints/BLUEPRINT-TEMPLATE.md` y nunca deben contener secretos, datos privados, código propietario ni reglas de negocio identificables.

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

model/
├── README.md
├── UNIVERSAL-PRODUCT-MODEL.md
└── PRODUCT-MODEL-TEMPLATE.md

skills/
├── yon/
├── yon-audit/
├── yon-polish/
├── yon-build/
├── yon-saas/
├── yon-web/
├── yon-landing/
├── yon-onboarding/
├── yon-visual/
├── yon-motion/
├── yon-qa/
├── yon-validate/
├── yon-product-model/
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
