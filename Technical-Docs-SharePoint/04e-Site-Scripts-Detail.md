# Site Script Deployment Guide (v3+)

This guide explains how to register and apply Site Scripts (`event-site-template.json` and `hub-site-template.json`) using the latest PnP PowerShell standards (post-September 2024).

## 1. Prerequisites (PowerShell 7)

Microsoft updated security policies in September 2024. You must now register your own application in your tenant to allow interactive logins.

### 1.1 Register the PnP App in Entra ID
Run this command once per tenant:
```powershell
Register-PnPEntraIDAppForInteractiveLogin
```
- A browser window will open. Log in with your administrator account.
- Grant consent for the organization.
- **IMPORTANT**: An Application (Client) ID will appear in your PowerShell terminal. Copy and save it.

---

## 2. Connect to SharePoint

Once registered, connect using your new Client ID:
```powershell
$SiteURL = "https://your-tenant.sharepoint.com/sites/YourSite"
$ClientID = "YOUR-CLIENT-ID-HERE"

Connect-PnPOnline -Url $SiteURL -Interactive -ClientId $ClientID
```

---

## 3. Register the Site Script

To add your JSON as a template in SharePoint:

```powershell
# Read the JSON file
$json = Get-Content -Path ".\event-site-template.json" -Raw

# Add the Site Script to SharePoint
Add-PnPSiteScript -Title "Casa Familiar - Event Site Template" -Content $json -Description "Standardized lists for event planning"
```
Take note of the ID returned by this command.

---

## 4. Create the Site Design (Site Template)

Now, link that script to a "Site Design" so it appears in the web interface:

```powershell
Add-PnPSiteDesign -Title "Event Planning Site" -SiteScriptIds "THE-ID-FROM-STEP-3" -WebTemplate "64"
```
Note: "64" is the ID for a Team Site.

---

## 5. Visual Application (Web Interface)

Once registered via PowerShell, you can apply it visually:
1. Go to your new SharePoint site.
2. Click **Settings** (Gear icon) -> **Apply a site template**.
3. Go to the **From your organization** tab.
4. Select "Event Planning Site" and click **Use template**.

---
> [!TIP]
> Use `Get-PnPSiteScript` and `Get-PnPSiteDesign` to list already registered templates.

---
*Generated for Casa Familiar IT Documentation.*
