# 04j - Guía de Despliegue Oficial de SharePoint Online (SPO)

Si prefieres usar el **Microsoft SharePoint Online Management Shell Oficial** en lugar de PnP, utiliza esta guía. Este método es la forma "tradicional" y NO requiere registrar una aplicación en Entra ID.

## 1. Prerrequisitos
Asegúrate de tener instalado el módulo oficial:
```powershell
Install-Module -Name Microsoft.Online.SharePoint.PowerShell -Force
```

## 2. Conectar a tu Centro de Administración
Reemplaza `netorg4878279` con el nombre real de tu tenant:
```powershell
Connect-SPOService -Url https://netorg4878279-admin.sharepoint.com
```

## 3. Registrar el Site Script (JSON)
Ejecuta estos comandos para subir tu `event-site-template.json`:

```powershell
# 1. Leer el contenido del JSON
$json = Get-Content -Path ".\event-site-template.json" -Raw

# 2. Agregar el script a tu tenant
$script = Add-SPOSiteScript -Title "Casa Familiar - Official Event Site" -Content $json

# 3. Crear el Site Design (Plantilla)
# Usa WebTemplate "64" para Team Sites
Add-SPOSiteDesign -Title "Official Event Setup" -WebTemplate "64" -SiteScripts $script.Id
```

## 4. ¿Por qué usar PnP para Carpetas?
Aunque el módulo oficial de SPO (arriba) es perfecto para registrar scripts, **no puede** crear fácilmente carpetas dentro de las bibliotecas de documentos ni gestionar MegaMenus.

- **Para el JSON:** Usa el módulo Oficial de SPO (esta guía).
- **Para Carpetas/Menús:** Usa PnP PowerShell (ya que sus cmdlets están diseñados específicamente para la automatización de contenido).

---
> [!TIP]
> Usa `Get-SPOSiteScript` y `Get-SPOSiteDesign` para gestionar tus plantillas oficiales a través del módulo de SPO.
