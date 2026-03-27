# Technical Detail: Page Visualization (Web Parts)

### 1. The Difference between List and Page
*   **The List:** The data "repository". This is where you enter tasks, choose the year, and see colors (e.g., `https://your-site/Lists/EventTasks`).
*   **The Page:** The site's "face". This is what users see when they enter (Home). This is where you **display** the list elegantly.

---

### 2. How to Add Your Master Columns to a List
If you already have a list created and want to start using your master columns (Status, Year, Role), follow this path to avoid recreating them:

1.  Enter the list in SharePoint.
2.  Click the gear icon (**Settings**) -> **List settings**.
3.  Scroll down to the **Columns** section and click **Add from existing site columns**.
4.  In "Select columns from", choose your group `_Casa Familiar`.
5.  Select the column, click **Add >**, and then **OK**.

---

### 3. How to Display Your List on the Home Page
To ensure the committee sees their tasks when entering the site:
1. Go to the **Home** page and click **Edit** (top right corner).
2. Click the plus (**+**) circle to add a new web part.
3. Search for and select the **List** web part.
4. Select the task list (e.g., Event Tasks).
5. Click **Republish** to save changes.

---

### 4. Customizing the View on the Page
Once the list is on the page, you can:
*   **Filter:** Configure the component to only show "Blocked" tasks.
*   **Hide columns:** To prevent the page from looking cluttered, you can hide the "ID" or "Created By" columns and keep only the essentials.

### 5. Visual Summary
*   **Where does the column live?** In the List.
*   **Where is the Dashboard seen?** On the Page (using the List Web Part).

---
*Generated for Casa Familiar IT Documentation.*
