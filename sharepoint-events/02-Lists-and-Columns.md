# Estructura de Listas y Contenido (Detalle Profundo)

Para mantener la estandarización y evitar diferencias entre los sitios de eventos, cada sub-sitio de evento contendrá las siguientes listas. Todas deben usar Content Types definidos en el Hub.

## 1. Lista: Event Tasks
Lista principal para el seguimiento de actividades.

| Column | Data Type | Description / Options | Advanced Configuration |
| :--- | :--- | :--- | :--- |
| **Title** | Text | Nombre de la tarea. | Requerido |
| **Description** | Multiple lines text | Detalles de la responsabilidad. | Rich Text habilitado |
| **Assigned To** | Person or Group | Persona asignada. | Restringido al M365 Group del sitio |
| **Status** | Choice | `Pending`, `In Progress`, `Blocked`, `Completed`, `Cancelled`. | Default: `Pending`. Formato Condicional (Rojo/Amarillo/Verde) |
| **Year (Cycle)** | Choice (o Number) | Año al que pertenece (ej: `2024`). | Indexado. Requerido. |
| **Start Date** | Date and Time | Cuándo debe comenzar la tarea. | Friendly Format |
| **Due Date** | Date and Time | Fecha límite o de finalización. | Validación: Mayor a Start Date |
| **Closing Notes** | Multiple lines text | Lecciones aprendidas. | - |
| **Lead Approval** | Yes/No | Check para tareas críticas. | Visible solo a Owners o vía validación de lista. |

*Análisis Profundo:* Indexar la columna `Year (Cycle)` es esencial cuando la lista supera los 5,000 elementos (eventos a largo plazo), asegurando que las Vistas activas no se rompan (límite de Threshold de SharePoint).

## 2. Lista: Committee Roster (Roles y Miembros)
Lista para registrar quién participó en qué rol en cada comité anual.

| Column | Data Type | Description / Options | Advanced Configuration |
| :--- | :--- | :--- | :--- |
| **Title (Name)** | Person or Group | Usuario de M365 perteneciente al comité. | Mostrar foto de perfil |
| **Committee Role**| Choice | `Lead`, `Member`. | - |
| **Area/Department**| Choice | `Logistics`, `Marketing`, `Volunteering`. | Permite crear vistas de directorio precisas |
| **Year** | Choice / Number | Año de participación (ej: `2024`). | - |

## 3. Lista: Risks & Issues (Registro de Riesgos)
Los eventos a menudo sufren contratiempos imprevistos no considerados tareas normales. Separar esto de 'Event Tasks' permite medir el nivel de salud del proyecto.

| Column | Data Type | Description / Options |
| :--- | :--- | :--- |
| **Risk/Issue** | Text | Ej: "Faltan permisos del Ayuntamiento" |
| **Impact** | Choice | `High`, `Medium`, `Low` |
| **Mitigation Plan**| Multiple lines | Qué se hará al respecto. |
| **Status** | Choice | `Open`, `Resolved` |
| **Year** | Choice / Number | Año |

## 4. Document Library: Event Documents
Estructura unificada que asegura la Retention Policy.

- *Folder:* `/2023/`
- *Folder:* `/2024/`
  - *Folder:* `/2024/Committee Minutes/`
  - *Folder:* `/2024/Contracts and Permits/`
  - *Folder:* `/2024/Invoices/`

*Análisis de Integridad:* Se sugiere obligar el Control de Versiones en esta biblioteca para evitar sobreescrituras accidentales de contratos, y aplicar *Retention Labels* nativos desde el Compliance Center para que "Contracts and Permits" no puedan borrarse por al menos 5 años (para auditoría fiscal de Non-Profit).
