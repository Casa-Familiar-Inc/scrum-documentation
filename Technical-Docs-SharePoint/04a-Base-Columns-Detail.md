# Technical Detail: Site Columns (Modern SharePoint)

> [!NOTE]
> In the **Modern Experience**, some advanced configurations still require accessing the traditional *Site Settings* panel, but the application of these columns to lists is 100% modern.

### 1. What are "Site Columns"?
**They are not lists.** Think of them as the "headers" or "categories" that you will use later within your lists.

*   **A List** is like an Excel sheet (e.g., "Task List").
*   **A Site Column** is the field definition (e.g., "Status") that lives at the site level so you can use it in many different Excel sheets without having to recreate it.

In SharePoint, a **Site Column** is a reusable column definition. Unlike a standard list column, if you change a Site Column's settings (e.g., you add a new status option), the change can automatically propagate to all lists that use it.

### 2. Configuration of the 3 Master Columns (Step-by-Step)

> [!IMPORTANT]
> **Location:** Always go to your **HUB SITE** first.
> Click the gear icon (**Settings**) -> **Site information** -> **View all site settings** -> **Site columns** -> **Create**.

---

#### A. Column: `CF_TaskStatus`
*   **Column Name:** `CF_TaskStatus`
*   **Type:** `Choice`
*   **Group:** `New group` -> `_Casa Familiar`
*   **Description:** `Standardize task progress.`
*   **Require that this column contains information:** `Yes` (Important: every task must have a status).
*   **Enforce unique values:** `No`
    ```text
    1. Pending
    2. In Progress
    3. Blocked
    4. Completed
    ```
*   **Allow 'Fill-in' choices:** `No` (Critical: allowing custom statuses breaks task automation).
*   **Display choices using:** `Drop-Down Menu`
*   **Default value:** `1. Pending`

---

#### B. Column: `CF_YearCycle`
*   **Column Name:** `CF_YearCycle`
*   **Type:** `Choice`
*   **Group:** `Existing group` -> `_Casa Familiar`
*   **Description:** `Annual event cycle (e.g., 2025).`
*   **Require that this column contains information:** `Yes` (Important for historical tracking).
*   **Choices:**
    ```text
    2024
    2025
    2026
    2027
    ```
*   **Allow 'Fill-in' choices:** `Yes` (Important: allows adding future years without editing settings).
*   **Display choices using:** `Drop-Down Menu`
*   **Default value:** `Choice` -> (Leave empty or select the current year).

---

#### C. Column: `CF_CommitteeRole`
*   **Column Name:** `CF_CommitteeRole`
*   **Type:** `Choice`
*   **Group:** `Existing group` -> `_Casa Familiar`
*   **Description:** `Role within the event committee.`
*   **Require that this column contains information:** `No` (Optional, as some tasks might not be assigned to a specific role yet).
*   **Choices:**
    ```text
    Event Lead
    Logistics
    Finance / Treasury
    Volunteer Management
    Communication / Marketing
    ```
*   **Allow 'Fill-in' choices:** `Yes` (Useful if a new committee role arises during the year).
*   **Display choices using:** `Drop-Down Menu`
*   **Default value:** (Leave empty).

### 3. Advantages of this Approach
1.  **Centralized Maintenance:** If the committee decides to add a status called "Under Review", you only add it in one place.
2.  **Consolidated Reports:** By using exactly the same column name and options.
3.  **Pro Visualization:** You can apply [[04b-JSON-Formatting-Templates|Advanced JSON Formatting]] to make lists easy to read.

---

### Additional Resources
*   [[04b-JSON-Formatting-Templates|JSON Column Formatting Code Manual]]
