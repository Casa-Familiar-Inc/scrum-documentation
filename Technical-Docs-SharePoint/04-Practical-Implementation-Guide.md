# Master Implementation Guide: "Casa Familiar Events" System

This is the definitive guide for implementing and managing the event site ecosystem. The system is designed for the **SharePoint Modern Experience**.

---

## Automation Prerequisites (September 2024)
Before running any scripts (`.ps1`) or uploading JSON files, you have two options based on your preference:

### Option A: Official SharePoint Module (SPO)
*   **Use:** Ideal for registering the Site Script (JSON) "officially".
*   **Ease:** Does not require third-party application registration.
*   **Guide:** **[[04j-Official-SPO-Deployment|See steps with the official module here]]**.

### Option B: PnP PowerShell (Recommended for Experts)
*   **Use:** Necessary for creating folders, complex menus, and content automation.
*   **Power:** Much more flexible but requires Entra ID registration.
*   **Guide:** **[[04e-Detalle-Site-Scripts|See steps with PnP here]]**.

---

## Phase 1: Hub Configuration (The "Brain")
*This phase is performed manually once on the main site.*

1.  **Create the Hub Site:**
    *   Name: `Event Planning Improvements Project` (or your Hub name).
    *   Register it as a **Hub Site** in the SharePoint Admin Center.
2.  **Site Columns (The Metadata):**
    *   Define the 3 master columns in the Hub so all events speak the same language.
    *   **[[04a-Base-Columns-Detail|See exact column configuration here]]**
3.  **Compliance Policies:**
    *   Configure rules so contracts and minutes are not accidentally deleted.
    *   **[[04d-Detalle-Retention-Policies|See Retention configuration]]**
4.  **File Structure and Menu:**
    *   Configure the "Master Templates" libraries and the "MegaMenu" in English.
    *   **[[08-Hub-Site-English-Content|See Hub and Menu blueprint]]**
    *   **[[09-Event-Site-Folder-Structure|See operational structure for Event Sites]]**
    *   **Automation:** Use `create-hub-folders.ps1` for the Hub and `create-event-folders.ps1` for each new site.

---

## Phase 2: Site Automation (The "Blueprint")
*Use templates (Site Scripts) to create event sites in 2 minutes.*

1.  **The Master Mold (JSON):**
    *   Use the "Ultimate" version which already has all Tasks, Budget, Risks, and Roster fields configured.
    *   **[[04h-Site-Script|V5 Script Deployment Instructions]]**
2.  **Theme Registration (Branding):**
    *   Ensure the "Teal" theme is registered so sites look professional. (Instructions inside the Site Scripts guide above).

---

## Phase 3: Governance and Continuity (The "Control")
*How to maintain order over the years.*

1.  **Governance Plan:**
    *   Rules on who can edit what and when sites transition to "Read-Only" mode.
    *   **[[05-Data-Governance-Plan|Data Governance Plan]]**
2.  **Reuse Strategy:**
    *   Create a new site or clean the old one? (Hint: A new one is always better).
    *   **[[06-Annual-Reuse-Strategy|Annual Reuse Plan]]**
3.  **Centralized File Management:**
    *   How templates flow from the Hub to event sites.
    *   **[[07-Centralized-Files-Strategy|Document Strategy]]**

---

## Phase 4: Visualization and Formatting (The "Look")
*Make information easy to consume for volunteers.*

1.  **Color Formatting (JSON):**
    *   Codes so the "Blocked" status is automatically red and "Completed" is green.
    *   **[[04b-JSON-Formatting-Templates|See visual formatting codes]]**
2.  **Page Design:**
    *   How to arrange elements on the main page so the committee sees their tasks upon entry.
    *   **[[04f-Detalle-Visualizacion-Paginas|See page design guide]]**

---

## Phase 5: Future Improvements (Native Power)
For the future, consider using native tools to extend functionality:
*   **[[05-Future-Native-Improvements|See automation ideas with Power Automate]]**

---
