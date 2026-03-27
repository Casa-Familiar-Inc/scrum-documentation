# Data Governance Plan: "Casa Familiar" Event Sites

This document establishes the rules and policies to ensure that the information generated at each event site remains secure, organized, and complies with the organization's retention policies.

---

## 1. Structure and Architecture (Where the Info Lives)

The governance model is based on a **"Hub & Spoke"** architecture:

*   **The Hub Site:** `Casa Familiar Events`
    *   **Purpose:** Public portal for all employees. Consolidation of information from all events.
    *   **Governance:** Only the core planning team (and IT) has editing permissions. The rest of the organization has *Read* access only.
    *   **Hosted Data:** General policies, master templates, global site columns (`CF_TaskStatus`, etc.).

*   **The Event Sites (Spokes):** `Event: [Event Name 202X]`
    *   **Purpose:** Collaborative workspace specific to *each* event.
    *   **Governance:** All event committee members have editing permissions.
    *   **Hosted Data:** Specific budgets, event task lists, vendor contracts, rosters.

---

## 2. Permission Management (Who Can View and Edit)

Security is managed using Microsoft 365 Groups and standard SharePoint permission levels. Permission inheritance should not be broken at the folder or individual file level unless strictly necessary (e.g., Budgets).

| Event Role | SharePoint Group | Permission Level | When to Use |
| :--- | :--- | :--- | :--- |
| **Director / Project Lead** | Owners | Full Control | Can create lists, change site settings, and manage access. Max 2-3 people. |
| **Committee / Coordinators / Core Volunteers** | Members | Edit | Can add, edit, and delete tasks, risks, documents, and budget items. |
| **General Volunteers / External Staff** | Visitors | Read | Can only view information to stay informed but cannot modify documents or lists. |

**Critical Exception (Budget List):**
The `Event Budget` list and the invoices/contracts folder should be configured so only the *Owners* role and the Finance area can approve ("Payment Status: Paid").
*   **Action:** Break permission inheritance only on that list if absolute financial privacy is required.

---

## 3. Data Retention and Lifecycle (How Long Info Is Kept)

To comply with legal regulations and avoid "digital clutter" accumulation, retention policies and automated cleanup will be applied.

### 3.1 Legal Retention Policy (Microsoft Purview)
*   **Scope:** Critical documents (Vendor contracts, Signed invoices, Insurance policies, Risk mitigation evidence).
*   **Rule:** **10-year** retention from the time they are marked "Final" or "Paid". They cannot be permanently deleted, even by the user (see [[04d-Detalle-Retention-Policies]]).

### 3.2 Event Site Lifecycle Management
Since new sites are created each year (e.g., The Walk 2024, The Walk 2025), old sites must be "frozen".

| Phase | When It Occurs | Governance Action |
| :--- | :--- | :--- |
| **1. Active** | Event planning and execution | Normal access (Full editing for members). |
| **2. Closing (Read-Only)** | 30 days after the event | IT or the Site Owner changes the "Members" group to "Visitors". The site becomes a "read-only historical archive". No past data can be modified. |
| **3. Deep Archive** | 3 years after the event | Decoupled from the Hub Menu (no longer globally visible) but still accessible via search and indexing for audits. |

---

## 4. Metadata Standardization (How Info Is Labeled)

To be able to search reports (e.g., "Show me all 'Completed' tasks for all '2024' events"), we depend 100% on the strict use of **Site Columns** applied via **Site Scripts** (see [[04h-Site-Script]]).

**Data Entry Rules:**
1.  **Zero Root-Level Custom Lists:** All core lists (Tasks, Risks, Budget, Roster) *must* always and only be created using the official "Casa Familiar - Full Event Setup" template.
2.  **No Modifying Core Field Types:** Fields injected by the template (`CF_TaskStatus`, `Expense Category`) must not be deleted or renamed by site owners.
3.  **Use of Mandatory Metadata:** Fields defined as `isRequired: true` in the template (e.g., *Due Date*, *Estimated Cost*) guarantee that no "orphan" records exist.

---

## 5. Auditing and Reviews

*   **Frequency:** Every two months.
*   **Responsible:** SharePoint Administrator / Global Project Manager.
*   **Action:**
    1.  Review *Site Usage Analytics* to identify "abandoned" sites.
    2.  Verify that site *Owners* are still active Casa Familiar employees (Identity Management).
    3.  Ensure no event site has anonymous link sharing ("Anyone with the link") enabled to protect Roster or Financial personal information.

---
*Generated for Casa Familiar IT Documentation.*
