# Technical Detail: Content Types (List Templates)

### 1. What is a "Content Type"?
If **Site Columns** are the ingredients, the **Content Type** is the "recipe". It is a template that groups several columns so you can apply them to a list in one go.

---

### 2. Instructions for Creating the Content Type

For both, go to: **Settings** (Gear) -> **Site information** -> **View all site settings** -> **Site content types** -> **Create content type**.

#### A. Content Type: `Event Task CT` (For Tasks)
Fill in the fields exactly like this:

*   **Name:** `Event Task CT`
*   **Description:** `Master template for Casa Familiar event tasks.`
*   **Category:** Select **"New category"** and type `_Casa Familiar` (so it appears alongside your columns).
*   **Parent content type:**
    *   **Parent category:** `List Content Types`
    *   **Content type:** `Item` (the cleanest base for building custom lists).

---

#### B. Content Type: `Roster CT` (For the Committee)
Fill in the fields exactly like this:

*   **Name:** `Roster CT`
*   **Description:** `Master template for the committee list and roles.`
*   **Category:** Select **"Existing category"** -> `_Casa Familiar`.
*   **Parent content type:**
    *   **Parent category:** `List Content Types`
    *   **Content type:** `Item`.

---

### 3. The Final Step: Adding Your Columns
Once you click **Create**, SharePoint will take you to the new Content Type screen. Do the following to finish the "recipe":

1.  Click **Add site column** (or *Add from existing site columns*).
2.  Search for your group `_Casa Familiar`.
3.  Add the corresponding columns:
    *   For `Event Task CT`: Add `CF_TaskStatus` and `CF_YearCycle`.
    *   For `Roster CT`: Add `CF_CommitteeRole` and `CF_YearCycle`.

---
*Generated for Casa Familiar IT Documentation.*
