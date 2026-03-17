# 04e - Guía de Despliegue de Site Scripts (v3+)

Esta guía explica cómo registrar y aplicar los Site Scripts (`event-site-template.json` y `hub-site-template.json`) utilizando los estándares más recientes de PnP PowerShell (Posteriores a Septiembre 2024).

## 1. Prerrequisitos (PowerShell 7)

Microsoft actualizó las políticas de seguridad en Septiembre 2024. Ahora debes registrar tu propia aplicación en tu tenant para permitir los inicios de sesión interactivos.

### 1.1 Registrar la App de PnP en Entra ID
Ejecuta este comando una sola vez por tenant:
```powershell
Register-PnPEntraIDAppForInteractiveLogin
```
- Se abrirá una ventana del navegador. Inicia sesión con tu cuenta de administrador.
- Concede el consentimiento para la organización.
- IMPORTANTE: En tu terminal de PowerShell, aparecerá un Application (Client) ID. Cópialo y guárdalo.

## 2. Conectar a SharePoint

Una vez registrado, conéctate usando tu nuevo Client ID:
```powershell
$SiteURL = "https://netorg4878279.sharepoint.com/sites/TuSitio"
$ClientID = "TU-CLIENT-ID-AQUI"

Connect-PnPOnline -Url $SiteURL -Interactive -ClientId $ClientID
```

## 3. Registrar el Site Script

Para agregar tu JSON como una plantilla en SharePoint:

```powershell
# Leer el archivo JSON
$json = Get-Content -Path ".\event-site-template.json" -Raw

# Agregar el Site Script a SharePoint
Add-PnPSiteScript -Title "Casa Familiar - Event Site Template" -Content $json -Description "Listas estandarizadas para planeación de eventos"
```
Toma nota del ID devuelto por este comando.

## 4. Crear el Site Design (Plantilla de Sitio)

Ahora, vincula ese script a un "Site Design" para que aparezca en la interfaz web:

```powershell
Add-PnPSiteDesign -Title "Event Planning Site" -SiteScriptIds "EL-ID-DEL-PASO-3" -WebTemplate "64"
```
Nota: "64" es el ID para un Team Site.

## 5. Aplicación Visual (Interfaz Web)

Una vez registrado vía PowerShell, puedes aplicarlo visualmente:
1. Ve a tu nuevo sitio de SharePoint.
2. Haz clic en Settings (Icono del engrane) -> Apply a site template.
3. Ve a la pestaña From your organization.
4. Selecciona "Event Planning Site" y haz clic en Use template.

---
> [!TIP]
> Usa `Get-PnPSiteScript` y `Get-PnPSiteDesign` para listar las plantillas ya registradas.
