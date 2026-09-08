# YON Digital Product System

Sistema abierto de metodología, skills, patrones, capacidades y agentes para diseñar, construir, mejorar y verificar productos digitales.

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

Las skills especializadas de `product-design`, `ux`, `ui`, `saas`, `onboarding` y `qa` aportan conocimiento reutilizable adicional.

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

## Privacidad

Este repositorio es público. No debe contener secretos, credenciales, datos privados de clientes, prompts privados, código propietario ni reglas de negocio identificables de Yontools, Vantto u otros proyectos privados.

El conocimiento generalizable puede evolucionar en YON; el material privado permanece en el proyecto privado.

## Estructura

```text
.claude-plugin/
└── plugin.json

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

capabilities/
patterns/
commands/
adapters/
```

## Estado

YON está en evolución. Las capacidades y patrones usan estados como `experimental`, `proven` y `deprecated` para diferenciar ideas de soluciones con evidencia.
