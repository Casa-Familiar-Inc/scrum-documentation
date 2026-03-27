# Centralized File Strategy (Hub vs Event Sites)

The "Hub & Spoke" model applies not only to lists but also to document management. The most common error in planning events is having 5 different versions of the same "Check-in Format" scattered across all sites.

Here is the recommended plan to govern files and maintain a **"Single Source of Truth"**.

---

## 1. The Hub Site: The Master Library (Templates and Policies)

The Hub site (`Event Planning Improvements Project`) is the "Corporate" site. No work-in-progress for any specific event is stored here.

### Recommended Document Libraries in the Hub:
1.  **"Master Templates":**
    *   **What to store:** Official logos, blank budget formats (Excel), volunteer check-in formats, contract templates.
    *   **Permissions (Crucial):** Only the central team (Owners) has *Edit* permission. All other volunteers have *Read* permission (they can only download or copy).
2.  **"Global Policies & Manuals":**
    *   **What to store:** Emergency response manuals, dress code guides, security protocols.
    *   **Permissions:** Same as above, 100% Read-only for most.

### Benefit:
If you change the organization logo in 2025, you only update the file in the "Master Templates" folder of the Hub. When event volunteers look for the logo, they will always download the newest version without you having to notify everyone.

---

## 2. Event Sites: Workspaces (Working Documents)

Each individual event site (e.g., `The Walk 2024`) comes by default with a library called **"Documents"**. That is the active workspace.

### What is stored in the Event Site?
*   Vendor contracts **already signed** for *that* event.
*   PowerPoint presentations specific to *that* committee meeting.
*   The floor plan (Layout) for *that* year's venue.

### Permissions:
*   All event committee members have permissions to **Edit, Delete, and Create** in their site's library. It is their workspace.

---

## 3. How to Connect Both Worlds? (User Workflow)

To prevent volunteers from getting frustrated looking for the "Check-in Template", you must make it flow naturally from the Hub to the Event Site.

### The Magic Function: "Add Shortcut"
1. Go to the "Master Templates" library in your Hub Site.
2. Select the templates folder.
3. Copy the **link (URL)** of that library.
4. In your event site, you can add that link as a Quick Link or in the left navigation menu.

### "Copy to" Method (Recommended for Modern SharePoint)
The best way to work is to teach volunteers this flow:
1. The volunteer enters the **Hub Site**.
2. Enters the **Master Templates** library.
3. Selects the blank format (e.g., `Blank-CheckIn-Format.xlsx`).
4. Clicks the top button that says **"Copy to"**.
5. SharePoint will ask "Where do you want to copy it?". The volunteer selects their active event site (e.g., `The Walk 2024` -> `Documents`).
6. **Magic:** The blank document is copied to the event site, where the volunteer can now fill it with names without affecting the Hub's master template.

---

## 4. Continuous Improvement: Updating Templates

What if a volunteer for the "The Walk 2024" event improves the budget template by adding amazing formulas?

*   That improvement stays on their event site.
*   They send you an email saying: "Hey, I improved the budget format, can you make it official?".
*   You (as the Hub Owner) download the improved format and **upload it to the Hub's "Master Templates" library**, replacing the old one.
*   Done! The next event (e.g., Gala 2024) will already use the improved format when they click "Copy to".

---
*Generated for Casa Familiar IT Documentation.*
