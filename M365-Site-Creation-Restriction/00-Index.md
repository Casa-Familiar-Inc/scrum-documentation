# M365 Site and Group Creation Restriction

This documentation repository details the process for centralizing the creation of Microsoft 365 resources (SharePoint Sites, Teams, Planner Plans) exclusively for IT administrators.

## Current Configuration Status
- **SharePoint**: Site creation blocked for end users (via Web Interface).
- **M365 Groups**: Total group creation block (via Graph API / PowerShell).

## Available Guides

1. **[[01-Graph-Explorer-Guide|Graph Explorer Guide]]**: Manual method using Microsoft's API explorer. Ideal for quick configurations without scripts. Includes:
    - Total vs. restricted block.
    - **Reversal** process.
    - Verification walkthrough.

2. **[[02-PowerShell-Method|PowerShell Method]]**: Automation using the Microsoft Graph module. Ideal for IT administrators. Includes:
    - Configuration scripts.
    - Reversion scripts.
    - Technical verification.

---

## Governance Strategy
To keep the tenant clean of "Shadow IT", the following has been defined:
1. No standard user can create sites or groups autonomously.
2. Administrators must create resources from the corresponding Admin Centers.
3. It is recommended to establish a request flow (e.g., Microsoft Forms) for users to request new resources.

---
*Documentation generated for Casa Familiar - IT Analyst.*
