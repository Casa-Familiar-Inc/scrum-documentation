# Detalle Técnico: Ultimate Site Script (V5 - Final)

Esta es la versión **lista para producción** de tu automatización de gestión de eventos. Cada lista está completamente equipada, los enlaces de navegación están preconfigurados y el branding se aplica automáticamente.

---

### 1. Qué Incluye

| List | Columns | Smart View |
| :--- | :--- | :--- |
| **Event Tasks** | Status, Year, Due Date, Start Date, Assigned To, Priority, Category, % Complete, Notes | "My Pending Tasks", "Blocked Tasks" |
| **Risks** | Status, Risk Category, Probability, Impact Level, Mitigation Plan, Risk Owner, Review Date | "Active Risks" |
| **Committee Roster** | Role, Year, Phone, Email, Availability, Emergency Contact, Special Skills | — |
| **Event Budget** | Expense Category, Vendor, Estimated Cost, Actual Cost, Payment Status, Approved By, Invoice Date, Receipt Notes | "Pending Payments" |

**Plus:** Tema Teal + Navegación MegaMenu + Enlaces en el menú izquierdo.

---

### 2. Post-Despliegue: Convertir Campos de Texto a Choice

Después de aplicar el script, mejora manualmente estos campos para un mejor control de datos:

| List | Field | Recommended Choices |
| :--- | :--- | :--- |
| Event Tasks | Priority | High, Medium, Low |
| Event Tasks | Category | Venue, Catering, Entertainment, Marketing, Logistics |
| Risks | Probability | Low, Medium, High |
| Risks | Impact Level | Low, Medium, High, Critical |
| Event Budget | Payment Status | Pending, Approved, Paid, Cancelled |
| Event Budget | Expense Category | Venue Rental, Food & Beverage, Decorations, Permits, Insurance, Marketing |
| Committee Roster | Availability | Full-Time, Part-Time, Event Day Only |

**Cómo:** List Settings → clic en el nombre de la columna → cambiar Type a Choice → agregar opciones → OK.

---

### 3. Cómo Desplegar (Estrategia de Script Dual)

Dado que ahora tienes una arquitectura con un Hub central y múltiples Sitios de Eventos conectados, tienes **dos scripts JSON diferentes**.

#### A. Desplegando el Hub Site Script (`hub-site-template.json`)
Este script solo debe ejecutarse **una vez** en tu portal principal. Fuerza el tema Teal y establece el layout a MegaMenu con cabecera compacta.

**Importante:** Antes de ejecutar estos comandos, asegúrate de haber seguido la **[[04e-Detalle-Site-Scripts|Nueva Guía de Autenticación]]** para registrar tu Client ID.

```powershell
# Conectar usando PnP (Moderno)
Connect-PnPOnline -Url https://netorg4878279.sharepoint.com/sites/TuHub -Interactive -ClientId "TU-ID"

$hubContent = Get-Content ".\hub-site-template.json" -Raw
$hubResult = Add-PnPSiteScript -Title "Casa Familiar - Hub Branding" -Content $hubContent
Add-PnPSiteDesign -Title "Apply Hub Branding" -SiteScriptIds $hubResult.Id -WebTemplate "68"
```
*Aplica esta plantilla "Apply Hub Branding" solo a tu Hub Site principal.*

---

#### B. Desplegando el Event Sites Script (`event-site-template.json`)
Este es el motor principal. Crea las 4 listas, se une al Hub automáticamente y configura el Menú Izquierdo. Lo aplicarás a *cada* nuevo sitio de evento que crees (ej: The Walk 2025).

**Si estás actualizando el script existente (V5):**
```powershell
$newContent = Get-Content ".\event-site-template.json" -Raw
Set-PnPSiteScript -Identity "3b6c1a53-25d0-4cb0-bb48-ad0d0f6522e4" -Content $newContent
```

**Si estás creando una plantilla nueva para Sitios de Eventos:**
```powershell
$content = Get-Content ".\event-site-template.json" -Raw
$result = Add-PnPSiteScript -Title "Casa Familiar V5 - Event Site" -Content $content
Add-PnPSiteDesign -Title "Casa Familiar - Full Event Setup" -SiteScriptIds $result.Id -WebTemplate "64"
```
*Nota: Usamos WebTemplate "64" para Team Sites modernos.*

#### Después de Subir (Ambas Opciones):
1. Ve a tu sitio de SharePoint.
2. Haz clic en el engrane -> **Apply a site template** -> **From your organization**.
3. Selecciona **"Casa Familiar - Full Event Setup"**.
4. ¡Listo! Se aplicarán las 4 listas, vistas, enlaces de navegación y el branding.

> **Importante:** Si las listas ya existen de una ejecución previa, el script omitirá su creación pero no agregará nuevas columnas. Para probar un despliegue limpio, aplícalo en un sitio nuevo o borra las listas existentes primero.

---

### 4. Opcional: Registrar el Tema Teal Primero
Si recibes un error de tema, registra el tema Teal antes de aplicar:

```powershell
$themepalette = @{
  "themePrimary" = "#008080"; "themeLighterAlt" = "#f0fafa"
  "themeLighter" = "#c5eded"; "themeLight" = "#98dede"
  "themeTertiary" = "#4dbdbd"; "themeSecondary" = "#1a9e9e"
  "themeDarkAlt" = "#007373"; "themeDark" = "#006161"
  "themeDarker" = "#004848"; "neutralLighterAlt" = "#faf9f8"
  "neutralLighter" = "#f3f2f1"; "neutralLight" = "#edebe9"
  "neutralQuaternaryAlt" = "#e1dfdd"; "neutralQuaternary" = "#d0d0d0"
  "neutralTertiaryAlt" = "#c8c6c4"; "neutralTertiary" = "#a19f9d"
  "neutralSecondary" = "#605e5c"; "neutralPrimaryAlt" = "#3b3a39"
  "neutralPrimary" = "#323130"; "neutralDark" = "#201f1e"
  "black" = "#000000"; "white" = "#ffffff"
}
Add-SPOTheme -Name "Teal" -Palette $themepalette -IsInverted $false
```

---
### Relacionado
*   [[04b-JSON-Formatting-Templates|Aplicar formato de colores después del despliegue]]
*   [[04f-Detalle-Visualizacion-Paginas|Agregar listas a tu página de inicio]]
*   [[04-Guia-Implementacion-Practica|Volver a la Guía Práctica]]
