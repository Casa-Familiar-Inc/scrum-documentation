# Arquitectura General de SharePoint

## Resumen
La solución está estructurada utilizando un **Hub Site** principal para "Casa Familiar Events", al cual se asocian **sitios secundarios (Team Sites)** para cada evento específico.

## Estructura de Sitios
- **Hub Site:** `Casa Familiar Events Hub`
  - Sitios Asociados (Eventos):
    - `Fall Festival`
    - `Haunted House`
    - `Día de Muertos`
    - `Thanksgiving`
    - `Día de Reyes`

## Gestión de Comités y Permisos (Estrategia para Alta Rotación)
Dado que la rotación constante de los miembros del comité año tras año es una realidad, la gestión de identidad es la pieza central de esta arquitectura.
- Cada sitio de evento tendrá un **Microsoft 365 Group** único y persistente.
- **Onboarding/Offboarding Centralizado:** La rotación anual se gestiona **exclusivamente** agregando o eliminando miembros del grupo M365 a través de Entra ID o el Admin Center.
  - *Ventaja clave:* Al dejar un comité, el voluntario pierde instantáneamente el acceso a correos, calendarios y archivos logísticos confidenciales para el próximo año.
  - *Riesgo mitigado:* No se crean "grupos huérfanos" (ej: "Comité 2023", "Comité 2024"). Es un solo grupo que muta sus miembros.
- **Roles y Gobernanza:**
  - **Site Owners (Leads):** 2 personas. Tienen control total sobre las listas, flujos y permisos de su sub-sitio. Son responsables de "Cerrar" el año.
  - **Site Members (Comité):** ~8 personas. Pueden agregar, editar y completar tareas en las listas de su evento. No pueden borrar elementos ni borrar Vistas (se debe configurar el nivel de permiso *Contribute* sin *Delete* para proteger la auditoría).
  - **Site Visitors:** Empleados o voluntarios que solo necesitan ver el progreso (Solo lectura).
  - **External Sharing:** Debe estar bloqueado o restringido para asegurar que las minutas, bases de datos o contratos permanezcan accesibles solo para el personal interno.

## Unificación y Mantenibilidad (Enfoque de Desarrollo)
Para lograr la mantenibilidad requerida por un perfil técnico (Developer) y unificar los sitios:
1. **Configuración del Hub Site:** La navegación principal, el branding y los permisos globales (si aplica) se gestionan desde el Hub.
2. **Site Templates / Site Scripts (JSON):** 
   - Crear un esquema de sitio base usando JSON/PowerShell que contenga todas las listas requeridas. Al aplicar esta plantilla a cualquier evento nuevo o existente, las listas estándar se generarán o actualizarán automáticamente.
   - *Consideración profunda:* Esto permite que en el futuro, si se agrega un nuevo evento (ej: "Posada Navideña"), lanzar el portal tome 5 minutos y respete exactamente las mismas columnas.
3. **Site Columns y Content Types:** Definirlos a nivel de Hub y publicarlos en los sitios secundarios (Content Type Hub) para que todas las listas de eventos compartan exactamente los mismos nombres internos e IDs de esquema (ej: `Task Status`, `Event Year`). Esto es crucial para el cruce de datos (Roll-up) y consolidaciones en PowerBI.
