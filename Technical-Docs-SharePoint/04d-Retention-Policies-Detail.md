# Technical Detail: Retention Policies (Microsoft Purview)

### 1. What is a Retention Policy?
It is a compliance rule that lives above SharePoint in the **Microsoft Purview (Compliance Center)**. It ensures that important information is not lost, whether by human error or intentional deletion.

In your project, **contracts and budgets** are critical. A retention policy guarantees that even if someone tries to delete a file, SharePoint will keep a hidden copy for the duration you define.

---

### 2. Configuration in Microsoft Purview

To configure this, an administrator must go to: **Microsoft 365 Admin Center** -> **Compliance** (or Purview) -> **Data Lifecycle Management** -> **Microsoft 365** -> **Retention Policies**.

#### Recommended Configuration for Casa Familiar:
*   **Name:** `Retention Policy - Event Contracts (5 Years)`
*   **Description:** `Mandatory retention for event contract and finance documents.`
*   **Type:** **Static** (To apply to specific sites).
*   **Locations:** Select **SharePoint sites**. You can choose to apply it to all sites or only those belonging to the Event Hub.
*   **Retention Settings:**
    *   **Retain items for a specific period:** `5 years`.
    *   **Start the retention period based on:** `When items were created`.
    *   **At the end of the retention period:** `Do nothing` (or delete automatically for total cleanup).

---

### 3. How does it work in practice?
If a user tries to delete a contract under this policy:

1.  The file appears to disappear from the document library.
2.  However, SharePoint automatically moves it to a hidden library called the **"Preservation Hold Library"**.
3.  Only administrators with special permissions can view or recover those files from that hidden library during the 5-year policy duration.

---

### 4. Difference between "Retention Policy" and "Retention Label"
*   **Policy:** Applied to the **entire site** or library. It is automatic, and the user doesn't have to do anything. *(Recommended for Phase 1).*
*   **Label:** The user manually chooses which files to mark (e.g., marking only the "Contract.pdf" file). More flexible but requires users to remember to apply the label.

---
*Generated for Casa Familiar IT Documentation.*
