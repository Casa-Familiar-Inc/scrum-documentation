# 11 - Cronograma de Implementación y Tareas

A continuación se presenta la estimación de esfuerzo y el calendario para la implementación del proyecto de Automatización de Eventos en SharePoint. El cronograma asume como fecha de inicio el **16 de marzo de 2026** y distribuye el trabajo para manejar la infraestructura correctamente y sin riesgos.

### Resumen de Esfuerzo
* **Esfuerzo Total Estimado:** ~20 horas de trabajo.
* **Duración del Bloque:** 5 días hábiles (aprox. 4 horas de dedicación diaria).

---

## Calendario Detallado

| ID | Resumen de la Tarea | Descripción y Entregables | Esfuerzo Estimado | Fecha Programada |
| :--- | :--- | :--- | :--- | :--- |
| **TASK-01** | Prerrequisitos de Entorno | Instalación de PowerShell 7 y registro de Aplicación en Entra ID para habilitar la automatización interactiva PnP. | 2 horas | **16-Mar-2026** |
| **TASK-02** | Metadata y Site Columns | Creación de columnas maestras (`CF_TaskStatus`, `CF_YearCycle`, etc.) a nivel Hub para que todos los sitios de eventos las hereden y se estandarice el reporte. | 3 horas | **16-Mar-2026** |
| **TASK-03** | Gobernanza de Datos | Configuración de labels y políticas de retención de 10 años en Microsoft Purview para la categoría de *Signed Contracts*. | 2 horas | **17-Mar-2026** |
| **TASK-04** | Despliegue de Site Designs | Registro de las plantillas JSON (`hub-site-template.json` y `event-site-template.json`) en el centro de administración de SharePoint (SPO Shell). | 2 horas | **17-Mar-2026** |
| **TASK-05** | Configuración de Hub Site | Ejecución del script `create-hub-folders.ps1` para generar el MegaMenu oficial y construir las jerarquías de la biblioteca de *Master Templates*. | 3 horas | **18-Mar-2026** |
| **TASK-06** | Automatización de Event Sites | Creación de sitio piloto (ej. Dia de Reyes) y ejecución del script `create-event-folders.ps1` para validación de la arquitectura de la Plantilla de Evento. | 2 horas | **18-Mar-2026** |
| **TASK-07** | Pulido Visual UI (Formatos) | Aplicar el formato condicional JSON (colores) a las columnas críticas como Status (Rojo/Verde) y vistas de Board/Kanban. | 3 horas | **19-Mar-2026** |
| **TASK-08** | Capacitación y Gobernanza | Entrega técnica y recorrido de la documentación y *Plan B manual* con los responsables del comité y administradores del portal. | 3 horas | **20-Mar-2026** |

---
> **Nota de Planeación:** Las tareas TASK-01 a TASK-04 son estrictamente técnicas (Back-end/Infraestructura), mientras que TASK-05 en adelante impactan lo visual y la forma en que los usuarios locales utilizarán SharePoint.
