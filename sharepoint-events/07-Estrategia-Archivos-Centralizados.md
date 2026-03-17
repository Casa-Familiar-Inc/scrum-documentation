# Estrategia de Archivos Centralizados (Hub vs Event Sites)

El modelo de "Hub & Spoke" (Centro y Ejes) no solo aplica a las listas, sino también a la gestión de documentos. El error más común al planear eventos es tener 5 versiones diferentes del mismo "Formato de Check-in" regadas por todos los sitios.

Aquí tienes el plan recomendado para gobernar los archivos y mantener una "Única Fuente de Verdad" (Single Source of Truth).

---

## 1. El Hub Site: La Biblioteca Maestra (Plantillas y Políticas)

El sitio Hub (`Event Planning Improvements Project`) es el "Corporativo". Aquí no se guarda trabajo en progreso de ningún evento específico.

### Bibliotecas de Documentos Recomendadas en el Hub:
1.  **"Master Templates" (Plantillas Maestras):**
    *   **Qué guardar:** Logos oficiales, formatos vacíos de presupuestos (Excel), formatos de check-in de voluntarios, machotes de contratos.
    *   **Permisos (Crucial):** Solo el equipo central (Owners) tiene permiso de *Edición*. Todos los demás voluntarios tienen permiso de *Lectura* (solo pueden descargar o copiar).
2.  **"Global Policies & Manuals" (Políticas Globales):**
    *   **Qué guardar:** Manuales de respuesta a emergencias, guías de código de vestimenta, protocolos de seguridad.
    *   **Permisos:** Igual que arriba, 100% de Lectura para la mayoría.

### Beneficio:
Si en 2025 cambias el logo de la organización, solo actualizas el archivo en la carpeta "Master Templates" del Hub. Cuando los voluntarios de un evento vayan a buscar el logo, siempre descargarán la versión más nueva, sin que tengas que avisarles a todos.

---

## 2. Los Event Sites: Espacios de Trabajo (Working Documents)

Cada sitio de evento individual (Ej: `The Walk 2024`) viene por defecto con una biblioteca llamada **"Documents"** (Documentos). Ese es el espacio de trabajo activo.

### ¿Qué se guarda en el Sitio del Evento?
*   Contratos de proveedores **ya firmados** para *ese* evento.
*   Presentaciones de PowerPoint específicas para *esa* junta de comité.
*   El plano de mesas (Layout) del salón de *ese* año.

### Permisos:
*   Todos los miembros del comité del evento tienen permisos para **Editar, Borrar y Crear** la biblioteca de su sitio. Es su espacio de trabajo.

---

## 3. ¿Cómo Conectar Ambos Mundos? (Flujo de Trabajo del Usuario)

Para que los voluntarios no se frustren buscando la "Plantilla de Check-in", debes hacer que fluya de manera natural desde el Hub hacia el Sitio del Evento.

### La Función Mágica: "Colocar un Acceso Directo" (Add shortcut)
1. Ve a la biblioteca "Master Templates" de tu Hub Site.
2. Selecciona la carpeta de plantillas.
3. Copia el **enlace (URL)** de esa biblioteca.
4. En tu sitio de evento, puedes agregar ese enlace como un acceso directo (Quick Link) o en el menú izquierdo de navegación.

### Método "Copy to" (Recomendado para SharePoint Moderno)
La mejor manera de trabajar es enseñar a los voluntarios este flujo:
1. El voluntario entra al **Hub Site**.
2. Entra a la biblioteca **Master Templates**.
3. Selecciona el formato vacío (ej: `Formato-CheckIn-Vacio.xlsx`).
4. Haz clic en el botón superior que dice **"Copy to"** (Copiar a).
5. SharePoint le preguntará "¿A dónde lo quieres copiar?". El voluntario selecciona su sitio de evento activo (Ej: `The Walk 2024` -> `Documents`).
6. **Magia:** El documento vacío se copia al sitio del evento, donde el voluntario ya puede llenarlo con nombres sin afectar la plantilla maestra del Hub.

---

## 4. Mejora Continua: Actualizando Plantillas

¿Qué pasa si un voluntario del evento "The Walk 2024" mejora la plantilla del presupuesto agregando fórmulas increíbles?

*   Esa mejora se queda en su sitio de evento.
*   Te envía un correo diciendo: "Oye, mejoré el formato de presupuesto, ¿lo puedes hacer el oficial?".
*   Tú (como Owner del Hub) vas a tu computadora, descargas el formato mejorado, y **lo subes a la biblioteca "Master Templates" del Hub** reemplazando el viejo.
*   ¡Listo! El próximo evento (Ej: Gala 2024) ya usará el formato mejorado cuando le den "Copy to". 

### 📂 Relacionado
*   [[05-Plan-Gobernanza-Datos|Plan de control de versiones y permisos]]
*   [[06-Estrategia-Reutilizacion-Anual|Qué hacer con los documentos de eventos pasados]]
