# YON Tool & Execution Orchestration

La capa de orquestación conecta las decisiones de YON con las herramientas reales disponibles en un entorno de desarrollo.

Su propósito no es imponer una infraestructura. Es definir **cómo YON decide qué herramienta usar, cuándo usarla, qué permiso requiere, qué resultado debe observar y cuándo debe detenerse**.

## Principio

`YON → DECIDE → SELECT TOOL → AUTHORIZE → EXECUTE → OBSERVE → DECIDE NEXT → VERIFY`

Una herramienta no sustituye el razonamiento de producto. Ejecuta una acción dentro de un contrato explícito.

## Clases de herramientas

- **Repository / filesystem** — inspección y modificación de archivos.
- **Terminal / runtime** — instalación, scripts, builds, servidores y comandos.
- **Browser / automation** — interacción con el producto ejecutándose y QA de journeys.
- **Tests** — unit, integration, end-to-end, accessibility y otros checks disponibles.
- **GitHub** — ramas, commits, PRs, issues y CI cuando estén autorizados.
- **Deployment / infrastructure** — Vercel, Supabase u otros proveedores cuando estén conectados y autorizados.
- **Visual / media** — generación o edición de imágenes, video y otros assets cuando aporten valor real.

Los nombres concretos de herramientas son adaptadores del entorno. YON no debe inventar que una herramienta está disponible.

## Contrato de una acción

Cada acción significativa debe poder expresar:

1. objetivo
2. herramienta seleccionada
3. motivo de selección
4. entrada / contexto mínimo
5. permiso requerido
6. resultado esperado
7. efectos secundarios
8. evidencia producida
9. condición de continuación
10. condición de parada o rollback

## Estados

### Orquestación

`PLANNED → AUTHORIZED → EXECUTING → OBSERVING → DECIDING → COMPLETED`

Cuando falta una condición crítica:

`PLANNED / AUTHORIZED / EXECUTING / OBSERVING → BLOCKED`

`BLOCKED` nunca significa éxito.

### Riesgo

- **LOW** — lectura, inspección, tests locales, QA no destructivo.
- **MEDIUM** — edición de código, instalaciones, generación de assets, commits o cambios reversibles.
- **HIGH** — producción, migraciones, billing, auth/authz, operaciones destructivas, seguridad, integraciones externas críticas o reglas centrales del negocio.

Las acciones HIGH requieren autorización y evidencia proporcional. Si no pueden verificarse, se bloquean.

## Política de selección

1. Usar la herramienta más pequeña que produzca evidencia suficiente.
2. Inspeccionar antes de mutar.
3. Preferir lectura estática si responde la pregunta; no abrir el navegador por costumbre.
4. Preferir runtime cuando el comportamiento real sea parte de la pregunta.
5. No ejecutar cambios destructivos para obtener información que pueda obtenerse de forma segura.
6. Reutilizar herramientas ya disponibles en el proyecto antes de introducir dependencias nuevas.
7. No desplegar, migrar ni tocar servicios externos solo para "probar" una hipótesis sin autorización.
8. Después de una mutación significativa, observar el resultado antes de decidir el siguiente paso.
9. No declarar una acción ejecutada si la herramienta no estuvo realmente disponible o no devolvió evidencia.
10. Si la herramienta necesaria no existe o no está autorizada, marcar `BLOCKED` y explicar la condición faltante.

## Límites

La orquestación debe respetar:

- límites de privacidad entre proyectos
- secretos y credenciales
- tenancy y autorización del producto
- instrucciones locales del repositorio
- cambios de alto riesgo
- alcance aprobado en Blueprint y Execution Plan
- evidencia disponible

YON puede generalizar aprendizajes, pero nunca copiar automáticamente código privado, datos de clientes, secretos, prompts privados, arquitectura propietaria o reglas de negocio identificables.

## Integración

El skill `yon-orchestrate` define el proceso de selección y ejecución de herramientas. `yon-execute` lo usa como capa operacional entre el plan y la implementación/inspección real.

Los adaptadores concretos pueden vivir fuera de esta capa. Este directorio define el contrato, no una arquitectura obligatoria.
