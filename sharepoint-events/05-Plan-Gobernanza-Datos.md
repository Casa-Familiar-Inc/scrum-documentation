# Plan de Gobernanza de Datos: Sitios de Eventos "Casa Familiar"

Este documento establece las reglas y políticas para asegurar que la información generada en cada sitio de evento se mantenga segura, organizada y cumpla con las políticas de retención de la organización.

---

## 1. Estructura y Arquitectura (Dónde vive la información)

El modelo de gobernanza se basa en una arquitectura **"Hub & Spoke"** (Centro y Ejes):

*   **El Centro (Hub Site):** `Casa Familiar Events`
    *   **Propósito:** Portal público para todos los empleados. Consolidación de información de todos los eventos.
    *   **Gobernanza:** Solo el equipo core de planeación (y TI) tiene permisos de edición. El resto de la organización solo tiene acceso de *Lectura*.
    *   **Datos alojados:** Políticas generales, plantillas maestras, columnas de sitio globales (`CF_TaskStatus`, etc.).

*   **Los Ejes (Event Sites):** `Event: [Nombre del Evento 202X]`
    *   **Propósito:** Espacio de trabajo colaborativo específico para *cada* evento.
    *   **Gobernanza:** Todos los miembros del comité del evento tienen permisos de edición.
    *   **Datos alojados:** Presupuestos específicos, listas de tareas del evento, contratos de proveedores, rosters.

---

## 2. Gestión de Permisos (Quién puede ver y editar)

La seguridad se maneja mediante Grupos de Microsoft 365 y niveles de permiso estándar de SharePoint. No se deben romper las herencias de permisos a nivel de carpeta o archivo individual a menos que sea estrictamente necesario (ej: Presupuestos).

| Rol en el Evento | Grupo de SharePoint | Nivel de Permiso | Cuándo usarlo |
| :--- | :--- | :--- | :--- |
| **Director / Líder de Proyecto** | Owners (Propietarios) | Full Control | Puede crear listas, cambiar configuraciones del sitio y gestionar accesos. Máximo 2-3 personas. |
| **Comité / Coordinadores / Volunteers Core** | Members (Miembros) | Edit | Pueden agregar, editar y borrar tareas, riesgos, documentos y elementos del presupuesto. |
| **Voluntarios Generales / Staff Externo** | Visitors (Visitantes) | Read | Solo pueden ver la información para estar enterados, pero no pueden modificar documentos ni listas. |

**Excepción Crítica (Lista de Presupuesto):**
La lista `Event Budget` y la carpeta de facturas/contratos deben configurarse para que solo el rol de *Owners* y el área de Finanzas puedan aprobar ("Payment Status: Paid").
*   **Acción:** Romper la herencia de permisos solo en esa lista si se requiere privacidad financiera absoluta.

---

## 3. Retención y Ciclo de Vida de los Datos (Cuánto tiempo se guarda)

Para cumplir con normativas legales y evitar la acumulación de "basura digital", se aplicarán políticas de retención y limpieza automatizada.

### 3.1 Política de Retención Legal (Microsoft Purview)
*   **Alcance:** Documentos críticos (Contratos de proveedores, Facturas firmadas, Pólizas de seguro, Evidencia de mitigación de riesgos).
*   **Regla:** Retención de **10 años** desde que se marca como "Final" o "Pagado". No pueden ser eliminados permanentemente ni por el usuario (ver [[04d-Detalle-Retention-Policies]]).

### 3.2 Ciclo de Vida del Sitio del Evento (Site Lifecycle Management)
Dado que se crean nuevos sitios cada año (ej: The Walk 2024, The Walk 2025), los sitios viejos deben "congelarse".

| Fase | Cuándo Ocurre | Acción de Gobernanza |
| :--- | :--- | :--- |
| **1. Activo** | Planeación y ejecución del evento | Accesos normales (Edición completa para miembros). |
| **2. Cierre (Read-Only)** | 30 días después del evento | TI o el Dueño del Sitio cambian el grupo de "Members" a "Visitors". El sitio se vuelve un "archivo histórico de solo lectura". Nadie puede modificar datos pasados. |
| **3. Archivado Profundo** | 3 años después del evento | Se desvincula del Menú del Hub (ya no es visible globalmente) pero sigue accesible vía búsqueda e indexación para auditorías. |

---

## 4. Estandarización de Metadatos (Cómo se etiqueta la información)

Para poder buscar reportes (ej: "Muéstrame todas las tareas 'Completadas' de todos los eventos del '2024'"), dependemos 100% del uso estricto de **Site Columns** aplicadas vía los **Site Scripts** (ver [[04h-Site-Script]]).

**Reglas de Ingreso de Datos:**
1.  **Cero Listas Personalizadas a nivel Raíz:** Todas las listas core (Tasks, Risks, Budget, Roster) *deben* crearse siempre y únicamente usando el template oficial "Casa Familiar - Full Event Setup".
2.  **No modificar tipos de campo Core:** Los campos inyectados por el template (`CF_TaskStatus`, `Expense Category`) no deben ser borrados ni renombrados por los dueños del sitio.
3.  **Uso de Metadatos Obligatorios:** Los campos definidos como `isRequired: true` en el template (Ej: *Due Date*, *Estimated Cost*) garantizan que no existan registros "huérfanos".

---

## 5. Auditoría y Revisiones

*   **Frecuencia:** Bimestral.
*   **Responsable:** Administrador de SharePoint / Project Manager Global.
*   **Acción:**
    1.  Revisar el *Site Usage Analytics* para identificar sitios "abandonados".
    2.  Verificar que los *Owners* de los sitios siguen siendo empleados activos de Casa Familiar (Identity Management).
    3.  Asegurar que ningún sitio de evento tenga habilitada la opción de compartir enlaces anónimos ("Anyone with the link") para proteger información personal del Roster o Financiera.

### 📂 Relacionado
*   [[04d-Detalle-Retention-Policies|Política técnica de Prevención de Datos (Purview)]]
*   [[04h-Site-Script|Documentación del Template Automatizado Principal]]
