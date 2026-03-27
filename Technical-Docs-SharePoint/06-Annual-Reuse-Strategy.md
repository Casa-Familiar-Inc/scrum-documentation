# Annual Site Reuse Strategy

When an event repeats every year (e.g., *The Walk 2024*, *The Walk 2025*), the question arises: **Do I reuse the same SharePoint site and delete the old content, or create a new one?**

In Modern SharePoint, Microsoft's recommendation is almost always to **create a new site**. Here we explain why and how to manage both strategies.

---

## Strategy 1: "New Year, New Site" (Recommended)

Instead of deleting old tasks, you create a fresh site using the **Site Script** we've already automated.

*   **Example:** You have `casafamiliar.sharepoint.com/sites/TheWalk2024`. Next year you create `.../sites/TheWalk2025`.

### Advantages
1.  **Perfect Audit Trail:** You have an intact historical archive of what happened in 2024 (who did what, how much it cost, what failed).
2.  **Zero Deletion Risk:** There is no danger of someone accidentally deleting a 2024 contract believing it was "clutter" to clean the list.
3.  **Legal Compliance (Purview):** 10-year retention policies work perfectly because the old site is simply archived (see [[05-Data-Governance-Plan]]).
4.  **Speed:** Thanks to your Site Script ([[04h-Site-Script]]), creating the 2025 site and its lists takes less than 2 minutes.

### Disadvantages
*   Generates more sites in your administration console (which is normal and expected in Microsoft 365).

### Workflow (Step-by-Step):
1.  **Event Closing (November 2024):** Change permissions of the `TheWalk2024` site to "Read-Only". Nothing is touched.
2.  **New Cycle Start (January 2025):** Create the `TheWalk2025` site.
3.  **Apply Template:** Run the "Casa Familiar - Full Event Setup" template on the new site.
4.  **Link to Hub:** The script already automatically connects it to the main hub.
5.  **Copy Templates:** Manually move only the "blank" template documents (e.g., check-in format) from the 2024 site to the 2025 site.

---

## Strategy 2: "Site Recycling" (Not Recommended)

You use exactly the same site (`casafamiliar.sharepoint.com/sites/TheWalk`) year after year, cleaning the lists.

### Advantages
*   The URL never changes. Volunteers always keep the same link in their favorites.
*   You don't have to move or copy base documents from year to year.

### Disadvantages (High Risks)
1.  **Loss of History:** To start with clean lists, someone must delete last year's tasks. Operational history is lost.
2.  **Legal Conflict:** If you configure the 10-year Retention policy, **Microsoft 365 will prevent you from deleting items** to recycle them. The system will throw an error when attempting to "clean up" for the new year.
3.  **View Saturation:** If you choose *not* to delete but only change the `CF_YearCycle` column (e.g., filter the view to only show "2025"), after 3 years your Task list will be huge, very slow to load, and search will be a mess.

---

## Verdict for Casa Familiar

Since you have implemented **Automated Site Scripts** and need **Contract Retention Policies**, the only viable and safe long-term strategy is **Strategy 1 (New Year, New Site)**.

**Solution to the "Eternal Link" problem:**
To prevent users from getting confused with new URLs every year, best practice is:
On your **main Hub Site**, place a giant button that says "Go to Current The Walk Event". As an administrator, you only update that button each year to point to the new site (from 2024 to 2025). The end user only needs to remember the Hub Site path.

---
*Generated for Casa Familiar IT Documentation.*
