# Configuración Centralizada del Hub Site (Guía de Contenido)

Para mantener la consistencia con tu "Ultimate English Site Script" (V5), el Hub Site central (`Event Planning Improvements Project`) debe estar estructurado y nombrado completamente en Inglés para los elementos del sistema, aunque las descripciones estén en Español.

Aquí tienes el blueprint exacto de qué crear en el Hub Site, incluyendo nombres de bibliotecas, estructuras de carpetas y plantillas esenciales.

---

## 1. Bibliotecas de Documentos a Crear
No uses la biblioteca por defecto "Documents" para todo. Segrega tus archivos creando estas bibliotecas específicas en el Hub Site (Icono Engrane -> Add an App -> Document Library).

### Library A: `Master Templates`
**Propósito:** Hogar de todos los archivos en blanco y reutilizables.
**Permisos:** Owners (Edit), Members/Visitors (Read-Only).

**Estructura Completa de Carpetas dentro de `Master Templates`:**

*   `01 - Finance & Budget`
    *   `Event-Budget-Blank-Template.xlsx`
    *   `Vendor-Invoice-Cover-Sheet.docx`
    *   `Reimbursement-Request-Form.pdf`
    *   `Sponsorship-Pitch-Deck.pptx`
    *   `Sponsorship-Pricing-Tiers.pdf`
    *   `Tax-Exemption-Certificate.pdf`

*   `02 - Operations & Logistics`
    *   `Volunteer-Check-In-Sheet.xlsx`
    *   `Event-Run-of-Show-Template.docx`
    *   `Venue-Inspection-Checklist.pdf`
    *   `Equipment-Inventory-Tracker.xlsx`
    *   `Catering-Menu-Template.docx`
    *   `Event-Debrief-Meeting-Agenda.docx`

*   `03 - Marketing & Branding`
    *   `Casa-Familiar-Official-Logos.zip`
    *   `Press-Release-Template.docx`
    *   `Social-Media-Graphics-Base.pptx`
    *   `Typography-and-Brand-Colors.pdf`
    *   `Email-Newsletter-Template.docx`
    *   `Event-Flyer-Template.dotx`

*   `04 - Legal & Contracts`
    *   `Standard-Vendor-Agreement.docx`
    *   `Liability-Waiver-Form.pdf`
    *   `Photo-Release-Consent-Form.pdf`
    *   `Talent-Performer-Agreement.docx`
    *   `Non-Disclosure-Agreement-NDA.pdf`

*   `05 - Risk & Safety Management`
    *   `Risk-Assessment-Matrix-Blank.xlsx`
    *   `Incident-Report-Form.pdf`
    *   `Emergency-Contact-List-Template.xlsx`

*   `06 - Committee & Volunteers`
    *   `Committee-Meeting-Minutes-Template.docx`
    *   `Volunteer-Role-Descriptions.pdf`
    *   `Certificate-of-Appreciation-Template.pptx`


### Library B: `Global Policies & Procedures`
**Propósito:** Reglas y manuales oficiales que no cambian de evento en evento.
**Permisos:** Owners (Edit), Members/Visitors (Read-Only).

**Contenido Recomendado (Sin carpetas, mantener plano para facilitar búsquedas):**
*   `Emergency-Response-Protocol.pdf`
*   `Volunteer-Code-of-Conduct.pdf`
*   `Expense-Approval-Policy.pdf`
*   `Media-Interaction-Guidelines.pdf`
*   `Vendor-Onboarding-Process.pdf`
*   `Data-Privacy-and-Photo-Policy.pdf`
*   `Event-Cancellation-Policy.pdf`

---

## 2. Navegación del Hub Site (MegaMenu)
El Hub utiliza el layout de MegaMenu para mostrar un directorio completo de recursos.

**Estructura Extendida del Menú (Inglés para los Enlaces):**
*   **Home** *(Link al Hub Home Page)*
*   **Active Events** *(Dropdown)*
    *   *The Walk 2024*
    *   *Annual Gala 2024*
    *   *Community Festival 2024*
*   **Master Templates** *(Dropdown - Link a la Library A)*
    *   *Finance & Budget*
    *   *Operations & Logistics*
    *   *Marketing & Branding*
    *   *Legal & Contracts*
    *   *Risk & Safety*
    *   *Committee & Volunteers*
*   **Global Policies** *(Dropdown - Link a la Library B)*
    *   *Emergency Protocols*
    *   *Volunteer Code of Conduct*
    *   *Vendor Onboarding Process*
*   **Quick Links** *(Dropdown)*
    *   *Submit Expense Reimbursement*
    *   *IT Support Request*
    *   *Marketing Brand Portal*
*   **Past Events Archive** *(Dropdown)*
    *   *The Walk 2023*
    *   *Annual Gala 2023*

---

## 3. Diseño de la Página Principal del Hub (Web Parts)
La Home page del Hub Site no debe mostrar tareas (eso pertenece a los sitios de eventos). Debe actuar como un panel para toda la organización.

**Web Parts Recomendados (De arriba a abajo):**
1.  **Hero Web Part:**
    *   *Título:* "Welcome to Casa Familiar Event Planning"
    *   *Botón de Llamado a la Acción:* "Go to Current Event: The Walk 2024" (Se actualiza anualmente).
2.  **Quick Links Web Part (Layout de Iconos):**
    *   Link 1: Download Official Logos
    *   Link 2: View Emergency Protocols
    *   Link 3: Submit Reimbursement
3.  **News Web Part:**
    *   Úsalo para publicar anuncios organizacionales (ej: "New Catering Vendor Approved", "Gala Date Moved").
4.  **Events Web Part:**
    *   Consolida fechas de calendario de todos los Event Sites conectados para mostrar una línea de tiempo unificada.

---

## 4. Recordatorio del Flujo de Trabajo
**Siempre entrena al personal con esta regla:**
*"Nunca edites un archivo directamente en la biblioteca `Master Templates`. Abre la carpeta, selecciona el archivo, haz clic en **Copy to** en el menú superior, y envíalo a la biblioteca de documentos de tu sitio de evento específico antes de llenarlo."*

---
### Relacionado
*   [[07-Estrategia-Archivos-Centralizados|Por qué centralizamos archivos (Estrategia)]]
*   [[04h-Site-Script|La plantilla usada para los Sitios de Eventos]]
