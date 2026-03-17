# Estructura de Carpetas Operativas para Sitios de Eventos

Mientras que el Hub Site contiene las **Master Templates**, cada sitio de evento individual (ej: *The Walk 2024*) necesita una estructura operativa para almacenar sus archivos de trabajo específicos, contratos firmados y activos del día del evento.

La consistencia en todos los sitios de eventos es clave para facilitar los reportes y la rotación del personal.

---

## 1. Recomendaciones para la Biblioteca "Documents"
Cada sitio de evento creado con la plantilla "Casa Familiar - Full Event Setup" tendrá una biblioteca por defecto llamada **Documents**. Esta debe organizarse de la siguiente manera:

### Estructura Sugerida de Carpetas (Inglés):

*   `01 - Financials & Expenses`
    *   *Propósito:* Presupuesto llenado localmente, cotizaciones de vendors y facturas específicas.
    *   *Contenido:* `TheWalk2024-Final-Budget.xlsx`, `Catering-Invoice-001.pdf`.
*   `02 - Planning & Logistics`
    *   *Propósito:* Planes operativos, run-of-shows y planos del lugar.
    *   *Contenido:* `Event-Schedule-V3.docx`, `Venue-Layout-Map.png`.
*   `03 - Marketing & Social Media`
    *   *Propósito:* Flyers específicos para este año, fotos del evento y comunicados de prensa localizados.
    *   *Contenido:* `Social-Media-Photos/`, `TheWalk2024-Campaign-Flyer.pdf`.
*   `04 - Signed Contracts & Agreements`
    *   *Propósito:* Versiones finales y firmadas de documentos (Mover desde el template del Hub -> Llenar -> Firmar -> Almacenar aquí).
    *   *Contenido:* `Signed-Security-Contract.pdf`, `Talent-Waivers/`.
*   `05 - Volunteer & Staff Management`
    *   *Propósito:* Horarios de turnos, listas de contactos específicas para este equipo.
    *   *Contenido:* `Shift-Schedule-Final.xlsx`, `Staff-Instructions.pdf`.
*   `06 - Post-Event & Debrief`
    *   *Propósito:* Reportes resumidos, resultados de encuestas y lecciones aprendidas.
    *   *Contenido:* `Post-Event-Report.docx`, `Survey-Results-Summary.xlsx`.

---

## 2. Mejores Prácticas para Dueños de Sitios
1.  **No crees carpetas de primer nivel:** Mantente fiel a las 6 categorías estándar de arriba.
2.  **Convención de Nombres:** Prefija los archivos con el Nombre del Evento y Año (ej: `Gala2024-GuestList.xlsx`) para que, si alguna vez se mueven o comparten, el contexto permanezca.
3.  **Usa el Hub:** Si necesitas un formulario "en blanco", ve a la biblioteca `Master Templates` del Hub y usa la función **"Copy to"** para traerlo aquí.

---

## 3. Automatización (Creación Programática)
Dado que los Site Scripts de SharePoint aún no soportan de forma nativa la creación de estructuras de carpetas complejas, se recomienda que el **Dueño del Sitio** o **Administrador de TI** ejecute el script `create-event-folders.ps1` inmediatamente después de que se aprovisione un nuevo sitio de evento.

---
### Relacionado
*   [[08-Hub-Site-English-Content|Compara con la estructura de Master Templates del Hub Site]]
*   [[07-Estrategia-Archivos-Centralizados|Aprende cómo copiar archivos del Hub al Sitio de Evento]]
