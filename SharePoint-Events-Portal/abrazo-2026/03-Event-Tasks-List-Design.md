---
title: Abrazo 2026 - Event Tasks List Design
purpose: SharePoint List schema for Event Tasks based on Work Progress Tracker template
list_template: Work Progress Tracker (Microsoft)
tags: [sharepoint, list, event-tasks, schema, abrazo]
last_update: 2026-03-26
---
- [ ] 
# Event Tasks List Design - Abrazo 2026

## Base Template

Using the **Work Progress Tracker** template from SharePoint as starting point, customized for event management.

---

## Column Schema

### Columns Modified from Template

| Column Name          | Type                | Original (Template)                                  | Customized For Events                 | Required |
| -------------------- | ------------------- | ---------------------------------------------------- | ------------------------------------- | :------: |
| **Work Item**        | Single line of text | Generic work item                                    | Task title (keep as-is)               |   Yes    |
| **Description**      | Multi-line text     | Generic description                                  | Specific deliverable or action item   |   Yes    |
| **Category**         | Choice              | Planning, Research, Design, Engineering, Marketing   | **See custom categories below**       |   Yes    |
| **Progress**         | Choice              | Completed, Behind, In progress, Not started, Blocked | **See custom statuses below**         |   Yes    |
| **Priority**         | Choice              | Critical, High, Medium, Low                          | Keep as-is (works for events)         |   Yes    |
| **Start Date**       | Date                | Date                                                 | Keep as-is                            |    No    |
| **Due Date**         | Date                | Date                                                 | Keep as-is                            |   Yes    |
| **Assigned To**      | Person              | Person                                               | Keep as-is                            |   Yes    |
| **Notes**            | Multi-line text     | Free text                                            | Keep as-is (internal notes)           |    No    |
| **Key Stakeholders** | Person (multi)      | Person                                               | Keep as-is (who needs to be informed) |    No    |

### New Columns to Add

| Column Name | Type | Purpose | Options/Format |
|-------------|------|---------|----------------|
| **Phase** | Choice | Which project phase this task belongs to | Pre-Event, Day-Of, Post-Event |
| **Week** | Calculated or Choice | T-minus week for countdown tracking | T-8, T-7, T-6, T-5, T-4, T-3, T-2, T-1, T-0, T+1, T+2 |
| **Dependency** | Lookup | Links to another task this one depends on | Lookup to same list |

---

## Custom Category Choices

Replacing the generic template categories with event-specific ones:

| Category                   | Color Suggestion | What It Covers                                |
| -------------------------- | :--------------: | --------------------------------------------- |
| **IT / SharePoint**        |       Blue       | Site creation, permissions, lists, automation |
| **Logistics**              |      Orange      | Venue, packet pickup, day-of setup, signage   |
| **Outreach**               |      Green       | Sponsors, exhibitors, community promotion     |
| **Volunteers**             |      Purple      | Recruitment, assignments, training            |
| **Budget / Finance**       |       Red        | Expenses, vendor payments, approvals          |
| **Communications**         |       Teal       | Flyers, social media, email blasts            |
| **Committee Coordination** |      Yellow      | Meetings, training, handoffs                  |
| **Post-Event**             |       Gray       | Survey, data archive, retrospective           |

---

## Custom Progress Statuses

Keep the original template statuses -- they work well for event management:

| Progress | JSON Color | Meaning |
|----------|:---:|---------|
| **Not Started** | Light Gray `#F0F0F0` | Task in backlog, not yet started |
| **In Progress** | Blue `#0078D4` | Actively being worked on |
| **Behind** | Orange `#FF8C00` | Past due date or behind schedule |
| **Blocked** | Red `#D13438` | Cannot proceed, dependency or issue |
| **Completed** | Green `#107C10` | Done and verified |

---

## Pre-Populated Tasks (IT Scope Only)

> [!NOTE]
> These are only the IT setup tasks to be loaded when the list is created. The event committee will add their own tasks (Outreach, Volunteers, Logistics, etc.) after the handoff training.

### IT / SharePoint Tasks

| Work Item | Description | Category | Progress | Priority | Start Date | Due Date | Assigned To | Phase |
|-----------|-------------|----------|----------|----------|------------|----------|-------------|-------|
| Create Abrazo 2026 SP Site | Create Communication Site and associate to Events Hub | IT / SharePoint | Not Started | Critical | 03/26/2026 | 03/28/2026 | Nefi | Pre-Event |
| Configure Permissions | Set up M365 Group and assign permissions for committee members | IT / SharePoint | Not Started | High | 03/28/2026 | 03/30/2026 | Nefi | Pre-Event |
| Provision Core Lists | Create Event Tasks, Roster, Budget, and Risks lists | IT / SharePoint | Not Started | High | 03/30/2026 | 03/31/2026 | Nefi | Pre-Event |
| Customize List Columns | Add Phase, Week, and custom Category choices to Event Tasks list | IT / SharePoint | Not Started | Medium | 03/30/2026 | 03/31/2026 | Nefi | Pre-Event |
| Build Home Page | Configure SharePoint home page using web parts and event content | IT / SharePoint | Not Started | High | 03/28/2026 | 03/30/2026 | Nefi | Pre-Event |
| Add RunSignUp CTA Link | Add Call to Action web part linking to RunSignUp registration page | IT / SharePoint | Not Started | Low | 03/31/2026 | 03/31/2026 | Nefi | Pre-Event |
| Create Document Library | Set up folder structure for event documents (Flyers, Contracts, etc.) | IT / SharePoint | Not Started | Medium | 03/31/2026 | 03/31/2026 | Nefi | Pre-Event |
| SharePoint Training | Conduct training session with committee on how to use lists and the site | IT / SharePoint | Not Started | Medium | 04/01/2026 | 04/03/2026 | Nefi | Pre-Event |
| Create Legacy Folders | Create archive folders for past Abrazo events (2024, etc.) | IT / SharePoint | Not Started | Low | 04/03/2026 | 04/07/2026 | Nefi | Pre-Event |

---

## Views

The Work Progress Tracker template comes with 5 predefined views. Here is how to use each one and which custom views to add.

### Predefined Views (Already Included in Template)

| # | View Name | What it Does | Best Use on Home Page |
|---|-----------|-------------|----------------------|
| 1 | **All Items** | Shows all tasks unfiltered | Full list management, not ideal for home page (too much data) |
| 2 | **Grouped by priority** | Groups items by Critical > High > Medium > Low | Good for committee meetings -- see what matters most first |
| 3 | **Grouped by work item progress** | Groups by Not Started > In Progress > Behind > Blocked > Completed | Good overview of where everything stands. **Recommended for home page List web part** |
| 4 | **My work items** | Filters to only tasks assigned to the logged-in user [Me] | Great for individual committee members to see their own tasks |
| 5 | **Progress board** | Kanban-style board with columns by progress status | Best for drag-and-drop task management. Use for committee working sessions |

### Home Page View Recommendation

For the **List web part on the home page (Section 3)**, use these views:

| List Web Part | View to Select | Why |
|---------------|----------------|-----|
| **Primary** (top) | **Grouped by work item progress** | Committee sees everything organized by status at a glance |
| **Secondary** (optional, below) | **Grouped by priority** | Gives a priority-first perspective for leadership |

> [!TIP]
> The **Progress board** view is especially useful but works better when you navigate directly to the list (not embedded on the home page). Consider adding a Quick Link that says "Open Task Board" pointing directly to the list with the Progress board view.

### Custom Views to Add

These 2 views are not in the template and should be created for specific needs:

#### Custom View: "Upcoming Deadlines"

Use this view if you want a **focused, deadline-driven** view on the home page instead of the grouped views above.

| Setting | Value |
|---------|-------|
| **Filter** | Due Date >= [Today] AND Progress != "Completed" |
| **Sort** | Due Date (ascending) |
| **Columns** | Work Item, Due Date, Assigned To, Progress, Priority, Category |
| **Group by** | (none) |
| **Home page use** | Alternative primary view -- shows only what's coming up next, sorted by urgency |

#### Custom View: "Blocked Items"

| Setting | Value |
|---------|-------|
| **Filter** | Progress = "Blocked" |
| **Sort** | Priority (descending), Due Date (ascending) |
| **Columns** | Work Item, Due Date, Assigned To, Priority, Notes |
| **Home page use** | Optional second List web part -- makes blocked items always visible to leadership |

---

## JSON Column Formatting (Future - Epic 3)

> [!NOTE]
> When Epic 3 (UI Customization & Advanced Views) is reached, apply JSON formatting to the Progress column for visual status indicators. This is the code from the backlog:

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/column-formatting.schema.json",
  "elmType": "div",
  "style": {
    "padding": "4px 8px",
    "border-radius": "4px",
    "font-weight": "600",
    "text-align": "center",
    "background-color": "=if(@currentField == 'Completed', '#DFF6DD', if(@currentField == 'In Progress', '#DEF0FF', if(@currentField == 'Blocked', '#FDE7E9', if(@currentField == 'Behind', '#FFF4CE', '#F0F0F0'))))",
    "color": "=if(@currentField == 'Completed', '#107C10', if(@currentField == 'In Progress', '#0078D4', if(@currentField == 'Blocked', '#D13438', if(@currentField == 'Behind', '#FF8C00', '#666666'))))"
  },
  "txtContent": "@currentField"
}
```
