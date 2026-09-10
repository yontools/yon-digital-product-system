# YON Environment Detection

La capa de **Environment Detection** permite que YON entienda el entorno real antes de seleccionar herramientas o ejecutar cambios.

No intenta adivinar. Construye un perfil observable del proyecto y distingue entre señales del repositorio y disponibilidad real de herramientas.

## Flujo

`DETECT PROJECT → DETECT STACK → DETECT TOOLS → DETECT AUTHORITY → BUILD PROFILE → FEED REGISTRY`

## Qué detecta

- raíz del proyecto y repositorio Git
- instrucciones locales relevantes
- manifests y lockfiles
- runtime y package manager signals
- framework/library signals cuando existen
- scripts de desarrollo, build, test y lint
- señales de browser/E2E y testing
- señales de database, deployment e integraciones
- herramientas realmente encontrables en PATH
- posibles estados de disponibilidad del adaptador
- blockers y evidencia de cada detección

## Jerarquía de confianza

1. disponibilidad real comprobada en el entorno
2. configuración/instrucciones locales
3. manifests, lockfiles y scripts
4. señales indirectas del proyecto
5. suposiciones genéricas — nunca suficientes para declarar una herramienta disponible

`DOCUMENTED ≠ AVAILABLE`.

## Estados de herramienta

- `UNKNOWN` — todavía no se comprobó.
- `SIGNALLED` — el proyecto contiene señales compatibles, pero no se comprobó disponibilidad.
- `AVAILABLE` — la herramienta fue detectada de forma verificable.
- `UNAVAILABLE` — se buscó y no está disponible.
- `UNAUTHORIZED` — existe, pero no se cuenta con autorización para la acción requerida.
- `DEGRADED` — está disponible, pero una dependencia o capacidad necesaria no funciona.

## Privacidad

El detector nunca imprime valores de secretos, tokens, cookies, credenciales ni variables de entorno completas. Detectar que existe una configuración no equivale a revelar su contenido.

El perfil es contexto operacional local. No debe copiarse automáticamente al repositorio público YON cuando contiene información privada del proyecto.

## Uso

El skill `yon-environment` define cuándo crear o refrescar el perfil. El script `scripts/detect_environment.py` ofrece una detección portable basada en Python estándar. El resultado alimenta a `yon-orchestrate` y al Tool Capability Registry.

La detección no modifica el proyecto por defecto.
