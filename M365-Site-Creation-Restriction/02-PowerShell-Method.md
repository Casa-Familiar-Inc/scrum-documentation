# PowerShell Method for M365 Group Creation Restriction

## Validation Status

> This guide was corrected to remove unverified references to `DirectorySetting` and align it with the `groupSettingTemplates` / `groupSettings` resource family.

## Important Note

It is not assumed here that fully equivalent high-level cmdlets exist for all tenants using the old `Get-MgDirectorySettingTemplate` flow. As a safer operational reference, this document uses direct Microsoft Graph calls from PowerShell.

---

## Requirements

- [`Microsoft.Graph`](https://www.powershellgallery.com/packages/Microsoft.Graph) module installed.
- Sufficient administrative permissions.
- A security group already created to authorize group creation (optional).

---

## Connection

```powershell
Connect-MgGraph -Scopes "Group.ReadWrite.All","Directory.ReadWrite.All"
```

> **Scopes Explanation**:
> - `Group.ReadWrite.All`: Required to read and write group settings (`groupSettings`)
> - `Directory.ReadWrite.All`: Required to read group setting templates (`groupSettingTemplates`)

---

## Step 1: Get the Authorized Group (Optional)

```powershell
$GroupName = "M365 Group Creators"
$AllowedGroup = Get-MgGroup -Filter "displayName eq '$GroupName'"

if (-not $AllowedGroup) {
    throw "Security group '$GroupName' not found."
}

$AllowedGroupId = $AllowedGroup.Id
$AllowedGroupId
```

---

## Step 2: Get the Correct Template

```powershell
$templatesResponse = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/groupSettingTemplates"
$template = $templatesResponse.value | Where-Object {
    $_.displayName -match "Unified|Microsoft 365|Group"
} | Select-Object -First 1

if (-not $template) {
    throw "No compatible template found in groupSettingTemplates."
}

$template.id
```

---

## Step 3: Check Existing Configurations

```powershell
$settingsResponse = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/groupSettings"
$settingsResponse.value
```

> **Example response when no configuration exists**:
> ```json
> {
>   "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#groupSettings",
>   "value": []
> }
> ```
>
> **Example response when a configuration exists**:
> ```json
> {
>   "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#groupSettings",
>   "value": [
>     {
>       "id": "88888888-9999-aaaa-bbbb-ccccddddeeee",
>       "displayName": "Group.Unified",
>       "templateId": "62375ab9-6b52-4edc-8c87-4a3502a30d4b",
>       "values": [
>         { "name": "EnableGroupCreation", "value": "false" }
>       ]
>     }
>   ]
> }
> ```

---

## Step 4: Create the Configuration

If no applicable configuration exists (total block):

```powershell
$body = @{
    templateId  = $template.id
    values      = @(
        @{ name = "EnableGroupCreation"; value = "false" }
    )
} | ConvertTo-Json -Depth 5

Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/groupSettings" -Body $body -ContentType "application/json"
```

> [!TIP]
> **Allowing a Specific Group**
> If you want to allow a specific security group to create sites (e.g., the group from Step 1), **do not change** `EnableGroupCreation` to `true` or replace `false` with the group ID. Instead, keep it `false` to block everyone else, and add a second property for `GroupCreationAllowedGroupId` with the `$AllowedGroupId` variable:
> 
> ```powershell
> $body = @{
>     templateId  = $template.id
>     values      = @(
>         @{ name = "EnableGroupCreation"; value = "false" },
>         @{ name = "GroupCreationAllowedGroupId"; value = $AllowedGroupId }
>     )
> } | ConvertTo-Json -Depth 5
> ```

---

## Step 5: Update Existing Configuration (Best Approach)

> [!IMPORTANT]
> **Why Update?** Entra ID only allows **one** configuration instance per template for the entire tenant. You cannot run another `POST` if a block exists (conflict error). Deleting and recreating is also discouraged as it leaves a temporary window where anyone can create sites. The official, secure approach is to use `PATCH` to update the existing configuration "hot".

If a configuration already exists, first identify its `id` and send the updated values array maintaining the general block `false` alongside your group ID.

```powershell
$settingId = "CONFIGURATION_ID"

$body = @{
    values = @(
        @{ name = "EnableGroupCreation"; value = "false" },
        @{ name = "GroupCreationAllowedGroupId"; value = $AllowedGroupId } # Add this line to allow a specific group, use "" to block all
    )
} | ConvertTo-Json -Depth 5

Invoke-MgGraphRequest -Method PATCH -Uri "https://graph.microsoft.com/v1.0/groupSettings/$settingId" -Body $body -ContentType "application/json"
```

---

## Verify Configuration

```powershell
Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/groupSettings"
```

Confirm in the response:

- `EnableGroupCreation = false`
- `GroupCreationAllowedGroupId` (empty for total block)

---

## Reverse Change (Reversal)

Reversal must be done on the already created configuration, usually by updating the values or deleting the instance.

Example updating values:

```powershell
$settingId = "CONFIGURATION_ID"

$body = @{
    values = @(
        @{ name = "EnableGroupCreation"; value = "true" }
    )
} | ConvertTo-Json -Depth 5

Invoke-MgGraphRequest -Method PATCH -Uri "https://graph.microsoft.com/v1.0/groupSettings/$settingId" -Body $body -ContentType "application/json"

# Alternative: Delete the custom configuration (reverts to factory defaults)
# Invoke-MgGraphRequest -Method DELETE -Uri "https://graph.microsoft.com/v1.0/groupSettings/$settingId"
```

---

## Verification Walkthrough

1. **Teams**: Standard user should not see "Create team" button.
2. **SharePoint**: "+ Create site" button hidden for users.
3. **Outlook**: Groups section does not allow creation.
4. **Admin**: Must be able to create from the M365 Admin Center.
