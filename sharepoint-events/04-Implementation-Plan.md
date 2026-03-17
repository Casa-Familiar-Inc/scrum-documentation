# Plan de Implementación del Sitio (Extendido)

Este plan cubre todo desde la configuración inicial hasta el plan de gobernanza y adopción de usuarios (Change Management).

> [!NOTE] 
> **¿Requiere Desarrollo?**
> El grueso de esta arquitectura es **Configuración Out-of-the-Box (OOTB)** (haciendo clic en la interfaz de SharePoint).
> NO se requiere programación tradicional (como React o C#). 
> Sin embargo, incluye ligeras cargas de **Low-Code/Scripting** (marcadas con la etiqueta [LOW-CODE]) en dos áreas: 
> 1. Power Automate: Para conectar flujos lógicos (arrastrar y soltar bloques condicionales).
> 2. JSON/PnP PowerShell: Para automatizar la creación de sitios en lugar de hacerlo de forma manual e iterativa.

## Fase 1: Arquitectura de Hub y Gobernanza (Data Governance)
- [ ] **1.1. Crear Hub Site:** Crear un Communication Site ("Casa Familiar Events") y registrarlo. [CONFIGURATION]
- [ ] **1.2. Site Columns (Nivel Hub):** Crear tipos de datos CF_TaskStatus, CF_YearCycle, CF_CommitteeRole. [CONFIGURATION]
- [ ] **1.3. Content Types (Nivel Hub):** Agrupar Site Columns en Event Task CT y Roster CT, y publicarlos (Content Type Publisher). [CONFIGURATION]
- [ ] **1.4. Retention Policies (Compliance Center):** Aplicar políticas de auditoría a las bibliotecas de documentos (vida útil obligatoria de 5 años para contratos). [CONFIGURATION]

## Fase 2: Automatización del Despliegue de Sitios (Desarrollo Ligero)
- [ ] **2.1. Plantilla (Site Script & Site Design):** [LOW-CODE] Desarrollar scripts JSON y PnP PowerShell que instalen automáticamente las listas (Event Tasks, Risks, Committee Roster, Event Budget) sobre los grupos de M365 creados.
- [ ] **2.2. Aprovisionamiento:** [LOW-CODE] Ejecutar el Site Design en los 5 sitios base (Fall Festival, Haunted House...). Esto elimina errores tipográficos al escribir columnas manualmente.

## Fase 3: Configuración de Interfaz y Vistas Nativas
- [ ] **3.1. Formato de Vistas (List Formatting):** [LOW-CODE] Aplicar JSON Formatters (código JSON nativo de SharePoint) para colorear toda la fila de verde si está Completed o de rojo grueso si está Blocked.
- [ ] **3.2. Vistas Indexadas:** Crear un índice a nivel de plataforma para la columna CF_YearCycle para prevenir el colapso del sitio a largo plazo (List Threshold de 5,000 elementos). [CONFIGURATION]
- [ ] **3.3. Hub Central Dashboard:** Configurar Highlighted Content Webparts en el Hub central para mostrar "Tareas Bloqueadas Recientes". [CONFIGURATION]

## Fase 4: Flujos Operativos y Notificaciones (Plumbing / Flow)
- [ ] **4.1. Resumen Diario de Vencimientos:** [LOW-CODE] Programar el "Daily Digest" en Power Automate para verificar tareas vencidas.
- [ ] **4.2. Flujo de Rollover Automático:** [LOW-CODE] Crear el flujo maestro que clona tareas críticas del ciclo anterior y prepara al nuevo comité.

## Fase 5: Estrategia de Adopción (Change Management)
- [ ] **5.1. Piloto Técnico (UAT):** Probar los flujos con usuarios ficticios en 1 sitio o con el equipo técnico.
- [ ] **5.2. Playbook / Manual del Comité:** Crear una WIKI o página dentro del Hub Site llamada "Cómo gestionar mi evento" (capacitación asíncrona para la rotación constante de voluntarios).
- [ ] **5.3. Limitación de Daños (Permisos):** Validar que los permisos para el Committee Roster no permitan borrar la lista completa. (Cambiar nivel Contributor -> Nivel de permiso personalizado sin capacidad de borrar listas/elementos).
- [ ] **5.4. Go-Live y Soporte Temprano:** Incorporar a los comités reales del año actual e iniciar el soporte de hypercare por 2 a 3 semanas.
