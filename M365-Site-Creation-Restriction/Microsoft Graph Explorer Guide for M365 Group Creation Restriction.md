# Microsoft Graph Explorer: Guide for M365 Group Creation Restriction

> [!INFO] Official Casa Familiar Configuration Values
> The specific IDs needed for the setup have been pre-filled in the JSON code blocks below. You do not need to hunt for IDs manually. Simply copy and paste the values exactly as shown.
> 
> - **Security Group ID** (`SharepointSiteCreators`): `4744bdd7-cf8e-40fe-b955-3759b0d39bd9`
> - **Template ID** (`Group.Unified`): `62375ab9-6b52-47ed-826b-58e47e0e304b`
> - **Configuration ID** (Active M365 Tenant Rule): `90faf456-6ace-401a-a44e-8954f0d54945`

> [!NOTE]
> **Fast Track: Adding Exceptions to an Already Blocked System**
> If your Office 365 tenant **already has** a general restriction blocking everyone from creating sites, you can skip directly to **Step 6: Update an Existing Configuration (The Correct Method)**. The configuration ID and group exception ID have already been baked into the code for you.

This guide provides a highly detailed, non-technical walkthrough to restrict Microsoft 365 Group creation (which also blocks Teams and SharePoint site creation) using the Microsoft Graph Explorer.

## Step 1: Access and Login to Graph Explorer

Navigate to the following website:
[https://developer.microsoft.com/en-us/graph/graph-explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)

![[Pasted image 20260323095217.png]]
*Image: The main landing page of the Microsoft Graph Explorer.*

Click on the **"Sign In"** button on the left side menu to authenticate with your administrator account.

![[Pasted image 20260323095244.png]]
*Image: The Sign In button located on the top left corner.*

After successfully logging in, your profile picture and account name will appear on the left, and the workspace will be ready to execute commands:

![[Pasted image 20260323095312.png]]
*Image: The Graph Explorer interface after a successful login, showing your account details on the left pane.*

---

## Step 2: Get the Security Group ID (Optional)

In our case, the ID is already calculated (see Top Info).
If you need to verify it manually, in the Graph Explorer address bar at the top, execute the following `GET` query:

```text
GET https://graph.microsoft.com/v1.0/groups?$filter=displayName eq 'SharepointSiteCreators'
```

Locate the `"id"` field in the response at the bottom.
**Our ID is correctly confirmed as:** `4744bdd7-cf8e-40fe-b955-3759b0d39bd9`

![[Pasted image 20260324134757.png]]

---

## Step 3: Get the Correct Setup Template (Optional)

In our case, the Blueprint Template ID is already known.
If validating manually, call this endpoint in the address bar:
```text
GET https://graph.microsoft.com/v1.0/groupSettingTemplates
```

![[Pasted image 20260323105159.png]]

Locate the block named **exactly** `"Group.Unified"`.
**Our Template ID is correctly confirmed as:** `62375ab9-6b52-47ed-826b-58e47e0e304b`

---

## Step 4: Check if a Rule is Already Applied

Check if the organization already has a configuration created from that template.
Execute this in Graph Explorer:
```text
GET https://graph.microsoft.com/v1.0/groupSettings
```

If your screen returns an empty `"value": []`, proceed to **Step 5**.
If it returns a configuration for `Group.Unified`, verify that its `id` matches our predefined **Configuration ID**: `90faf456-6ace-401a-a44e-8954f0d54945`. Then proceed directly to **Step 6**.

![[Pasted image 20260323110912.png]]

---

## Step 5: Create a New Configuration

If no previous configuration exists, change the method dropdown to **POST** and execute:
```text
POST https://graph.microsoft.com/v1.0/groupSettings
```

In the "Request body" tab, paste the following JSON EXACTLY AS SHOWN (it already contains our official IDs, no editing required):

```json
{
  "templateId": "62375ab9-6b52-47ed-826b-58e47e0e304b",
  "values": [
    { "name": "EnableGroupCreation", "value": "false" },
    { "name": "GroupCreationAllowedGroupId", "value": "4744bdd7-cf8e-40fe-b955-3759b0d39bd9" }
  ]
}
```

![[Pasted image 20260323111303.png]]
*Image: Executing the POST request with the JSON payload in the request body.*

![[Pasted image 20260323111244.png]]
*Image: The successful response after creating the new configuration.*

---

## Step 6: Update an Existing Configuration (The Correct Method)

> [!IMPORTANT]
> **Why Update (PATCH) instead of making a new one?** 
> Microsoft only allows **ONE** saved rule for group creation in the entire tenant. The safest practice is to take the existing rule and "**inject**" the exception into it. 

Follow these EXACT steps to add the Leadership Group as an exception to our existing configuration:

### 1. Change the Method to PATCH
At the top left of the Graph Explorer address bar, select **`PATCH`** from the method dropdown list.

### 2. Type the Exact URL Address
In the address bar, paste the following exact path (which includes our official Casa Familiar Configuration ID pre-filled for you):

```text
https://graph.microsoft.com/v1.0/groupSettings/90faf456-6ace-401a-a44e-8954f0d54945
```

### 3. Prepare the "Request Body"
Below the address bar, find the tab labeled **"Request body"**. Click on it, clear everything inside, and **paste the exact code below**. 

This tells Microsoft: "Block everyone (false), EXCEPT our SharepointSiteCreators group":

```json
{
  "values": [
    { "name": "EnableGroupCreation", "value": "false" },
    { "name": "GroupCreationAllowedGroupId", "value": "4744bdd7-cf8e-40fe-b955-3759b0d39bd9" }
  ]
}
```

### 4. Execute the Command
Press the large blue button **"Run query"**. 

If successful, the bottom screen will show **`No Content - 204`**. Congratulations, the rule has been applied!

---

## Step 7: Verification Process

To ensure everything took effect, run:

```text
GET https://graph.microsoft.com/v1.0/groupSettings
```

Check the response values to confirm the block is active:
- `EnableGroupCreation = false`
- `GroupCreationAllowedGroupId = 4744bdd7-cf8e-40fe-b955-3759b0d39bd9`

---

## Step 8: How to Revert the Restriction

If you ever need to lift the ban and allow **all** users to create groups/sites freely again:

1. Change the method to **PATCH** and use this exact URL:
```text
https://graph.microsoft.com/v1.0/groupSettings/90faf456-6ace-401a-a44e-8954f0d54945
```
2. In the Request Body, send this payload to toggle creation back to `true`:
```json
{
  "values": [
    { "name": "EnableGroupCreation", "value": "true" }
  ]
}
```
3. Click **Run Query**. 

---

## Step 9: Field Test Verification

To confirm the block works for regular users, perform these tests with a non-admin account:

### Test 1: Microsoft Teams
- Log into [teams.microsoft.com](https://teams.microsoft.com).
- Navigate to the "Teams" tab. The "+ Join or create a team" button should not allow creating new teams.

### Test 2: SharePoint Online
- Log into SharePoint. The "+ Create site" button should be hidden or disabled.

### Test 3: Outlook Web
- Log into [outlook.office.com](https://outlook.office.com). The option to create a "New group" should not appear.

### Test 4: Administrator Check
- Log into the [M365 Admin Center](https://admin.microsoft.com) with an Admin account.
- IT administrators can still provision groups securely from here.



