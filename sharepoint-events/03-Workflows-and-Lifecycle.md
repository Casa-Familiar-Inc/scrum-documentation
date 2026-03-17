# Flujos de Trabajo y Ciclo de Vida del Evento (Extendido)

A continuación se presentan los diagramas de ciclo de vida con un enfoque profundo en el manejo de excepciones y el archivado robusto.

## 1. Ciclo de Vida de Tareas (Event Task)
Gestiona las asignaciones y los posibles cuellos de botella (bloqueos y escalaciones).

```mermaid
stateDiagram-v2
    [*] --> Pending : Creación Manual/Automática
    Pending --> InProgress : La persona asignada inicia el trabajo
    InProgress --> Blocked : Existe un Problema/Dependencia
    Blocked --> InProgress : Bloqueo resuelto
    Blocked --> Escalated : Si no se resuelve en 48h (Automático)
    Escalated --> InProgress : Intervención del Lead
    InProgress --> Completed : Trabajo finalizado
    Pending --> Cancelled : Tarea descartada (Con justificación)
    Completed --> [*]
    Cancelled --> [*]
```

## 2. Proceso de Rollover Anual (Rotación de Comité y Archivados)
Dado que los comités cambian cada año, el rollover no puede simplemente asignar tareas a las mismas personas. El ciclo se centra en "limpiar responsabilidades" y despejar el tablero para el nuevo comité.

```mermaid
sequenceDiagram
    participant AD as M365 Admin (Entra ID)
    participant Lead as Comité Lead Entrante/Saliente
    participant SP as SharePoint (Listas)
    participant PA as Power Automate

    Lead->>SP: Finaliza el evento (Tareas en estado Completed/Cancelled)
    Note over SP: Las tareas históricas permanecen "congeladas" bajo la columna [Year]
    Lead->>AD: Elimina a los miembros del comité viejo del M365 Group
    Lead->>AD: Agrega a los miembros del comité nuevo al M365 Group
    Lead->>SP: Actualiza la lista "Committee Roster" con nuevos miembros y el New Year
    Lead->>PA: Ejecuta el flujo "Prepare Next Year" (Botón de Flujo)
    PA->>SP: Extrae las "Master Tasks" (ej: "Get City Hall Permit", "Table Rentals")
    PA->>SP: Genera nuevas tareas asignando [Year] = Next Year (Status = Pending)
    Note over PA: CRÍTICO: La columna 'Assigned To' en las nuevas tareas se deja VACÍA.
    SP-->>Lead: El tablero está limpio. El nuevo Lead puede comenzar a asignar tareas al nuevo comité.
```

## 3. Flujo de Notificaciones y Acuerdo de Nivel de Servicio (SLA)
Para evitar la saturación de correos electrónicos, el flujo incorpora verificaciones de tiempo (Recurrencia Diaria) en Power Automate en lugar de notificaciones instantáneas para todo.

```mermaid
flowchart TD
    A["Trigger: Recurrencia Diaria (8:00 AM)"] --> B["Obtener tareas 'In Progress' o 'Pending'"]
    B --> C{"¿Vence en < 3 días?"}
    C -- "Sí" --> E["Añadir al Resumen Diario"]
    C -- "No" --> D{"¿Está Bloqueada?"}
    D -- "Sí" --> E
    D -- "No" --> F["Siguiente tarea"]
    E --> F
    F --> G{"¿Quedan más tareas?"}
    G -- "Sí" --> C
    G -- "No" --> H{"¿Resumen vacío?"}
    H -- "No" --> I["Enviar mensaje en Teams (Canal Comité)"]
    H -- "Sí" --> J["Fin del Flujo"]
    I --> J
```
*Análisis Operativo:* Un Resumen Diario es infinitamente mejor para la *Gobernanza* que disparar un correo por cada elemento de lista creado. Ayuda a mantener la tranquilidad del comité y aumenta la probabilidad de que las alertas sean leídas y atendidas.
