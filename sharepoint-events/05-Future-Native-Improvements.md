# Mejoras Adicionales de SharePoint (Nativas)

A continuación se presentan recomendaciones de mejora adicionales para los sitios de eventos de Casa Familiar, utilizando exclusivamente herramientas nativas de Microsoft 365 y SharePoint incluidas en el licenciamiento estándar para evitar generar costos extra.

## 1. Integración Nativa con Microsoft Teams
Dado que cada sitio de evento está asociado a un Grupo de M365 (y por lo tanto a un Team de Teams), podemos unificar aún más la experiencia del comité.

- **Pestaña de Tareas:** Incrusta directamente la vista de la lista *Event Tasks* (como pestaña de Sitio Web o Lista) dentro del canal General en Teams. Esto permite que el comité actualice su progreso sin necesidad de abrir el navegador web.
- **Canales por Área:** En lugar de enviar correos caóticos, crea canales en Teams para `#Logística`, `#Voluntariado`, `#Marketing` para centrar las conversaciones. Las carpetas en la Biblioteca de Documentos del sitio deben alinearse con la estructura de canales en Teams.

## 2. Vistas Visuales: Board View (Kanban)
En la lista de *Event Tasks*, configura una "Board View" (Vista de Tablero) basada en la columna `CF_TaskStatus`.
- **Beneficio:** Esta es una funcionalidad *Out-of-the-Box*. Permite al comité visualizar su carga de trabajo en columnas (Pending -> In Progress -> Completed) y arrastrar y soltar tarjetas.
- **Reemplazo de Power Apps:** Esta vista mejora la experiencia web y móvil de forma gratuita sin diseñar formularios complejos.

## 3. Seguimiento de Presupuesto (Expense Tracking)
Para el control financiero de eventos sin fines de lucro.
- **Lista Adicional (`Event Budget`):** Crea una lista con las siguientes columnas:
  - `Item Concept` (Texto)
  - `Estimated Amount` (Moneda)
  - `Actual Amount` (Moneda)
  - `Category` (Choice: Food, Rental, Marketing, etc.)
  - `CF_YearCycle` (Número)
  - Attachments habilitados (para subir cotizaciones y recibos).
- **Enlace de Facturas:** El Lead del comité puede autorizarlas, y se agrupan por `Category` para tener sub-totales automáticos nativos en la vista de lista.

## 4. Directorio y Recursos Compartidos en el Hub
Para evitar duplicar el esfuerzo de buscar proveedores año tras año entre diferentes comités:
- **Lista Maestra de Proveedores en el Hub:** `Casa Familiar Vendors`.
  - Columnas: Nombre, Contacto, Teléfono, Especialidad (Comida, Música, Seguridad), Calificación (1 a 5 estrellas por el Lead anterior).
- **Lookup Column:** En cada lista de `Event Tasks` e incluso en la lista de presupuesto (`Event Budget`), utiliza una columna de búsqueda (Lookup) referenciando la lista del Hub Site. Esta es una funcionalidad nativa y evita la redundancia de datos.

## 5. Cuadros de Mando Ejetutivos (Dashboards) y Reportes
Para la junta directiva de Casa Familiar que requiere una visión general sin entrar en el detalle de todos los sitios:
- **Página Principal del Hub (Vista de Roll-up):** Usa el Web Part de "Highlighted Content" o "News" en el `Casa Familiar Events Hub` para consultar una vista consolidada de todas las *Event Tasks* a través de los 5 sitios asociados que tengan estado `Blocked` y el `CF_YearCycle` actual. Esto resalta rápidamente si algún evento necesita apoyo de la alta gerencia, utilizando el motor de búsqueda interno de SharePoint de forma gratuita.
