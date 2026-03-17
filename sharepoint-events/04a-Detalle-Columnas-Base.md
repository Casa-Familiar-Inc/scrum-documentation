# Detalle Técnico: Columnas de Sitio (Modern SharePoint)

> [!NOTE]
> En la interfaz moderna (**Modern Experience**), algunas configuraciones avanzadas aún requieren acceder al panel de *Site Settings* tradicional, pero la aplicación de estas columnas a las listas es 100% moderna.

### 1. ¿Qué son las "Site Columns"?
**No son listas.** Imagínalas como los "encabezados" o "categorías" que utilizarás más adelante dentro de tus listas.

*   **Una Lista** es como una hoja de Excel (ej: "Lista de Tareas").
*   **Una Site Column** es la definición del campo (ej: "Estado") que vive al nivel del sitio para que puedas usarlo en muchas hojas de Excel diferentes sin tener que volver a crearlo.

En SharePoint, una **Site Column** es una definición de columna reutilizable. A diferencia de una columna de lista estándar, si cambias la configuración de una Site Column (ej: agregas una nueva opción de estado), el cambio puede propagarse automáticamente a todas las listas que la utilizan.

### 2. Configuración de las 3 Columnas Maestras (Paso a Paso)

> [!IMPORTANT]
> **Ubicación:** Ve siempre a tu **HUB SITE** primero.
> Haz clic en el icono del engrane (**Settings** -> **Site information** -> **View all site settings** -> **Site columns** -> **Create**.

---

#### A. Columna: `CF_TaskStatus`
*   **Nombre de columna:** `CF_TaskStatus`
*   **Tipo:** `Choice (menú para elegir)`
*   **Grupo:** `New group` -> `_Casa Familiar`
*   **Descripción:** `Estandarizar el progreso de las tareas.`
*   **Requerir que esta columna contenga información:** `Sí` (Importante: cada tarea debe tener un estado).
*   **Forzar valores únicos:** `No`
    ```text
    1. Pending
    2. In Progress
    3. Blocked
    4. Completed
    ```
*   **Permitir opciones 'Fill-in':** `No` (Crítico: permitir estados personalizados rompe la automatización de tareas).
*   **Mostrar opciones usando:** `Drop-Down Menu`
*   **Valor por defecto:** `1. Pending`

---

#### B. Columna: `CF_YearCycle`
*   **Nombre de columna:** `CF_YearCycle`
*   **Tipo:** `Choice (menú para elegir)`
*   **Grupo:** `Existing group` -> `_Casa Familiar`
*   **Descripción:** `Ciclo anual del evento (ej: 2025).`
*   **Requerir que esta columna contenga información:** `Sí` (Importante para el seguimiento histórico).
*   **Opciones:**
    ```text
    2024
    2025
    2026
    2027
    ```
*   **Permitir opciones 'Fill-in':** `Sí` (Importante: permite agregar años futuros sin editar la configuración).
*   **Mostrar opciones usando:** `Drop-Down Menu`
*   **Valor por defecto:** `Choice` -> (Dejar vacío o seleccionar el año actual).

---

#### C. Columna: `CF_CommitteeRole`
*   **Nombre de columna:** `CF_CommitteeRole`
*   **Tipo:** `Choice (menú para elegir)`
*   **Grupo:** `Existing group` -> `_Casa Familiar`
*   **Descripción:** `Rol dentro del comité del evento.`
*   **Requerir que esta columna contenga información:** `No` (Opcional, ya que algunas tareas podrían no estar asignadas a un rol específico aún).
*   **Opciones:**
    ```text
    Event Lead
    Logistics
    Finance / Treasury
    Volunteer Management
    Communication / Marketing
    ```
*   **Permitir opciones 'Fill-in':** `Sí` (Útil si surge un nuevo rol en el comité durante el año).
*   **Mostrar opciones usando:** `Drop-Down Menu`
*   **Valor por defecto:** (Dejar vacío).

### 3. Ventajas de este Enfoque
1.  **Mantenimiento Centralizado:** Si el comité decide agregar un estado llamado "En Revisión", solo lo agregas en un lugar.
2.  **Reportes Consolidados:** Al usar exactamente el mismo nombre de columna y opciones.
3.  **Visualización Pro:** Puedes aplicar [[04b-JSON-Formatting-Templates|Formatos JSON avanzados]] para que las listas sean fáciles de leer.

---

### Recursos Adicionales
*   [[04b-JSON-Formatting-Templates|Manual de Códigos JSON para Formato de Columnas]]
