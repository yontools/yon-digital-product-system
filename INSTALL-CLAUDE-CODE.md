# Instalar YON en Claude Code

YON está empaquetado como un plugin de Claude Code para poder reutilizar el sistema en distintos proyectos y mantenerlo versionado.

## Opción recomendada: probar directamente desde Git

Cloná este repositorio en una ubicación local y, desde el directorio del proyecto donde quieras trabajar, ejecutá:

```bash
claude --plugin-dir /ruta/a/yon-digital-product-system
```

Después verificá que el plugin aparezca en `/help` y probá el skill maestro:

```text
/yon-digital-product-system:yon
```

También podés simplemente describir una tarea de producto. La skill `yon` está diseñada para activarse cuando la tarea implique diseñar, construir, auditar, pulir o verificar un producto digital.

## Uso cotidiano

Ejemplos:

```text
Usá YON para auditar este SaaS y encontrá los problemas de mayor impacto.
```

```text
Usá YON para construir esta funcionalidad de punta a punta y verificá que funcione en el navegador.
```

```text
Usá YON para pulir esta pantalla sin romper la funcionalidad existente.
```

Para una acción explícita también podés invocar los skills/comandos específicos que estén instalados.

## Desarrollo del plugin

Mientras desarrollás YON, podés recargar cambios dentro de una sesión con:

```text
/reload-plugins
```

La forma recomendada por Claude Code para probar un plugin local es `--plugin-dir`.

## Qué hace YON

YON aplica el ciclo:

`OBSERVE → UNDERSTAND → DETECT → PROPOSE → IMPLEMENT → RUN → INSPECT → CORRECT → VERIFY`

No se limita a generar código. Primero inspecciona el producto y su contexto, identifica oportunidades, implementa cambios coherentes y verifica el resultado real.

## Privacidad

El repositorio público de YON contiene metodología, skills, patrones y capacidades generalizadas. No debe recibir automáticamente código, secretos, datos de clientes, credenciales, prompts privados ni reglas propietarias de proyectos privados como Yontools o Vantto.

## Instalación personal sin plugin

Claude Code también permite skills personales en:

```text
~/.claude/skills/<skill-name>/SKILL.md
```

Esta modalidad es útil para una copia personal o una experimentación rápida. Para distribución y evolución de YON, el plugin es la forma principal.

## Versionado

El plugin tiene una versión explícita en `.claude-plugin/plugin.json`. Cuando hagamos cambios compatibles, incrementaremos la versión según el alcance del cambio.
