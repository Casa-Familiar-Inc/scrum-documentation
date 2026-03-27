# Restricting Microsoft 365 Group Creation with Graph Explorer

## Validation Status

> Document corrected to use endpoints based on [`groupSettingTemplates`](https://graph.microsoft.com/v1.0/groupSettingTemplates) and not on [`directorySettingTemplates`](https://graph.microsoft.com/v1.0/directorySettingTemplates) paths, which are considered legacy or unverified in this guide.

## Objective

Document a way to restrict who can create Microsoft 365 groups, with an indirect impact on the creation of associated resources such as Teams and group-connected sites.

## Context

- Site creation from SharePoint is already disabled.
- Even so, Microsoft 365 group creation can still enable the creation of related resources.
- This guide focuses on **total block** (no one creates groups) or restricted (only administrators) using Graph Explorer.

---

## Validated Base Source

The endpoint taken as a valid reference for this documentation is:

```text
https://graph.microsoft.com/v1.0/groupSettingTemplates
```

## Prerequisites

1. Account with sufficient administrative permissions in Microsoft 365 / Entra ID.
2. Access to [`https://admin.microsoft.com`](https://admin.microsoft.com).
3. Access to [`https://developer.microsoft.com/graph/graph-explorer`](https://developer.microsoft.com/graph/graph-explorer).
4. A security group representing the users authorized to create groups (optional for total block).

---

## Step 1: Create the Authorized Security Group (Optional)

1. Go to [`https://admin.microsoft.com`](https://admin.microsoft.com).
2. Create a **Security** type group.
3. Use a recognizable name, for example: `M365 Group Creators`.
4. Add authorized accounts as members.

---

## Step 2: Get the Security Group ID (Optional)

In Graph Explorer, execute:

```text
GET https://graph.microsoft.com/v1.0/groups?$filter=displayName eq 'M365 Group Creators'
```

Example response:
```json
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#groups",
  "value": [
    {
      "id": "11111111-2222-3333-4444-555555555555",
      "displayName": "M365 Group Creators",
      "groupTypes": [],
      "mailEnabled": false,
      "securityEnabled": true
    }
  ]
}
```

Save the `id` value of the security group.

---

## Step 3: Get the Correct Template

In Graph Explorer, execute:

```text
GET https://graph.microsoft.com/v1.0/groupSettingTemplates
```

Example response (filtered for clarity):
```json
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#groupSettingTemplates",
  "value": [
    {
      "id": "62375ab9-6b52-4edc-8c87-4a3502a30d4b",
      "displayName": "Group.Unified",
      "description": "Template for a Unified Group settings object.",
      "values": [
        { "name": "EnableGroupCreation", "defaultValue": "true" },
        { "name": "GroupCreationAllowedGroupId", "defaultValue": "" }
      ]
    }
  ]
}
```

Look for the template corresponding to unified groups / Microsoft 365 Groups and save its `id`.

> Note: The exact visible name may vary depending on the tenant's response. Validate directly in the response before continuing.

---

## Step 4: Check if a Configuration is Already Applied

In Graph Explorer, execute:

```text
GET https://graph.microsoft.com/v1.0/groupSettings
```

Example response when no configuration exists:
```json
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#groupSettings",
  "value": []
}
```

Example response when a configuration exists:
```json
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#groupSettings",
  "value": [
    {
      "id": "88888888-9999-aaaa-bbbb-ccccddddeeee",
      "displayName": "Group.Unified",
      "templateId": "62375ab9-6b52-4edc-8c87-4a3502a30d4b",
      "values": [
        { "name": "EnableGroupCreation", "value": "false" }
      ]
    }
  ]
}
```

Expected result:

- If no relevant configuration exists, a new one is created.
- If a configuration based on the chosen template already exists, that instance is updated.

---

## Step 5: Create the Configuration

If no previous configuration exists, execute:

```text
POST https://graph.microsoft.com/v1.0/groupSettings
```

```json
{
  "templateId": "GROUPSETTINGTEMPLATE_ID",
  "values": [
    { "name": "EnableGroupCreation", "value": "false" }
  ]
}
```

> [!TIP]
> **Allowing a Specific Group**
> If you want to allow a specific security group to create sites (e.g., the group from Step 2), **do not change** `EnableGroupCreation` to `true` or replace `false` with the group ID. Instead, keep it `false` to block everyone else, and add a second property object for `GroupCreationAllowedGroupId` with the group's ID:
> 
> ```json
> {
>   "templateId": "GROUPSETTINGTEMPLATE_ID",
>   "values": [
>     { "name": "EnableGroupCreation", "value": "false" },
>     { "name": "GroupCreationAllowedGroupId", "value": "GROUP_ID" }
>   ]
> }
> ```

---

## Step 6: Update Existing Configuration (Best Approach)

> [!IMPORTANT]
> **Why Update?** Microsoft Graph only allows **one** configuration instance per template in the entire tenant. If a block is already in place, you cannot create a new one (it will throw a conflict error). You should **not** delete and recreate it either, as it causes temporary security vulnerabilities (factory defaults). The safest and only supported approach is to **PATCH (Update)** the existing configuration "hot".

If a configuration already exists, identify its `id` and execute a PATCH request. **Make sure to send both properties** so the general block remains active while adding the allowed group:

```text
PATCH https://graph.microsoft.com/v1.0/groupSettings/CONFIGURATION_ID
```

```json
{
  "values": [
    { "name": "EnableGroupCreation", "value": "false" },
    { "name": "GroupCreationAllowedGroupId", "value": "GROUP_ID" }
  ]
}
```

---

## Step 7: Verification

Run again:

```text
GET https://graph.microsoft.com/v1.0/groupSettings
```

Confirm that these values exist:

- `EnableGroupCreation = false`
- `GroupCreationAllowedGroupId` (empty for total block)

---

## Step 8: How to Reverse the Restriction (Reversal)

If you need to allow **all** users to create groups/sites again:

1. Get the `id` of the current configuration from `GET https://graph.microsoft.com/v1.0/groupSettings`.
2. Execute a **PATCH** to that URL:
   `PATCH https://graph.microsoft.com/v1.0/groupSettings/CONFIGURATION_ID`
3. Use the following Body:
```json
{
  "values": [
    { "name": "EnableGroupCreation", "value": "true" }
  ]
}
```
4. Optionally, you can delete the configuration entirely (revert to factory defaults) using:
   `DELETE https://graph.microsoft.com/v1.0/groupSettings/CONFIGURATION_ID`

---

## Step 9: Verification Walkthrough (Field Tests)

To confirm the block works:

### Test 1: Microsoft Teams
- Log in to [teams.microsoft.com](https://teams.microsoft.com) with a **standard** user account.
- Go to "Teams" -> "Join or create a team".
- **Expected result**: The "Create a team" button should have disappeared.

### Test 2: SharePoint
- Log in to the organization's SharePoint home page.
- **Expected result**: The "+ Create site" button should not be visible.

### Test 3: Outlook Web
- Log in to [outlook.office.com](https://outlook.office.com).
- Search for the "Groups" section in the left menu.
- **Expected result**: The "New group" option should be disabled or not appear.

### Test 4: Administrator Verification
- Log in to the [M365 Admin Center](https://admin.microsoft.com).
- Go to Teams & groups -> Active teams & groups.
- **Expected result**: The administrator **CAN** create groups from here.
