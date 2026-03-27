---
title: Fall Festival 2026 - SharePoint Home Page Content (Internal Team)
purpose: Ready-to-paste content for internal SharePoint team site
audience: Fall Festival 2026 Committee & Casa Familiar Staff
approach: Hybrid (Modern Page web parts + Text content blocks)
tags: [sharepoint, content, fall-festival, internal, committee, copy-paste]
last_update: 2026-03-27
---

# SharePoint Home Page Content - Fall Festival 2026 (Internal)

> [!IMPORTANT]
> This is an **internal team site** for the Fall Festival 2026 committee. The content is written for staff and committee members, not the public. There is no external registration platform -- this is a free walk-in event.

---

## Section 1: Hero Banner

> **Web Part**: Hero (Full Width)
> **Layout**: One layer

**Title**: Fall Festival 2026 -- Committee Hub
**Subtitle**: San Ysidro Civic Center | 212 W Park Ave | Date TBD (October 2026)
**CTA Button Text**: View Task List
**CTA Button Link**: *(link to the SharePoint Tasks list once created)*
**Image**: Fall/autumn-themed branding or Casa Familiar logo with seasonal overlay

---

## Section 2: Team Dashboard -- Quick Links

> **Web Part**: Quick Links
> **Layout**: Tiles or Grid (large icons)

These are the primary internal resources for the committee:

| # | Link Title | Destination | Notes |
|---|------------|-------------|-------|
| 1 | Task List | SharePoint Tasks List | Main task tracker for the committee |
| 2 | Committee Roster | SharePoint Roster List | Members, roles, contact info |
| 3 | Budget Tracker | SharePoint Budget List | Expenses, vendors, approvals |
| 4 | Event Documents | SharePoint Document Library | Flyers, vendor contracts, permits, maps |
| 5 | Vendor Applications | TBD | Food vendor and booth applications (if applicable) |
| 6 | Open Task Board | Event Tasks List > Progress board view | Kanban-style drag-and-drop task management |

> [!NOTE]
> Unlike Abrazo, there is **no external registration platform** (no RunSignUp, no Eventbrite). Remove any registration-related Quick Links. If a platform is added later, update this section.

---

## Section 3: Event Tasks (List Web Parts)

> **Web Part**: List (native)
> **Source**: Event Tasks list (Work Progress Tracker template)
> Do NOT use static text here. The List web part updates automatically when committee members edit items.

### List Web Part Configuration on the Page

1. Add a **List** web part to the page
2. Select the **Event Tasks** list
3. Select the view **"Grouped by work item progress"** as default
4. Committee members can edit items directly from the Home Page by clicking on any item

> [!TIP]
> The **Progress board** view works better in full screen, not embedded. That is why Quick Link #6 above says "Open Task Board" pointing directly to the list with the Progress board view.

### (Optional) Second List Web Part

Add a second List web part below the primary one with the view **"Grouped by priority"** to provide a priority-first perspective for leadership.

---

## Section 4: Event Quick Reference (Text Web Part)

Copy and paste into a **Text** web part. This gives committee members fast access to event details when someone asks:

---

### Event Details -- Quick Reference

| Field | Detail |
|-------|--------|
| **Event** | Fall Festival 2026 |
| **Date** | TBD (October 2026 - estimated) |
| **Time** | TBD |
| **Location** | San Ysidro Civic Center |
| **Address** | 212 W Park Ave, San Diego, CA 92173 |
| **Phone** | (619) 428-1115 |
| **Admission** | FREE -- Walk-in, no registration required |
| **Expected Attendance** | TBD |

### Day-of Schedule

> TBD -- to be filled in once committee finalizes the timeline.

| Time | Activity |
|------|----------|
| TBD | Gates Open |
| TBD | Activities Begin |
| TBD | Event Closes |

---

## Section 5: Activities & Attractions (Text Web Part)

Copy and paste into a **Text** web part:

---

### Confirmed Activities

| Activity | Description | Status |
|----------|-------------|--------|
| **Pumpkin Patch** | Seasonal pumpkin selection area for families | Confirmed |
| **Food Vendors** | Food stands and/or trucks | Confirmed |
| **Kids Activities** | TBD (games, crafts, face painting) | Planning |
| **Live Entertainment** | TBD (music, DJ, performances) | Planning |
| **Community Booths** | TBD (local organizations, exhibitors) | Planning |

> [!NOTE]
> This section replaces the "Pricing Reference" section from Abrazo. Since Fall Festival is a free event, there is no ticket pricing. Vendor pricing (food, pumpkins, activity tickets) will be managed by individual vendors.

---

## Section 6: Committee Contacts & Roles (Text Web Part)

Copy and paste into a **Text** web part:

---

### Committee Contacts

| Role | Name | Email | Responsibility |
|------|------|-------|----------------|
| IT / SharePoint | Nefi | *(internal)* | Site setup, permissions, automation |
| Event Lead | TBD | TBD | Overall event coordination |
| Volunteer Coordinator | TBD | TBD | Volunteer recruitment & day-of coordination |
| Food/Vendor Coordinator | TBD | TBD | Vendor outreach, booth logistics |
| General Inquiries | Casa Familiar | info@casafamiliar.org | Public-facing email |

> [!NOTE]
> Update contacts once committee kickoff meeting is completed and leads are confirmed.

---

## Section 7: Important Documents (Document Library Web Part)

> **Web Part**: Document Library (native)
> **Purpose**: Surface the event documents folder directly on the home page

1. Add a **Document Library** web part
2. Point it to the "Fall Festival 2026" document library or folder
3. Suggested folder structure inside the library:

```
Fall-Festival-2026-Documents/
  Flyers-Marketing/
  Vendor-Contracts/
  Permits/
  Volunteer-Info/
  Meeting-Notes/
  Day-of-Logistics/
  Photos-Media/
```

---

## SharePoint Page Setup Checklist (Internal Team Site)

- [ ] **Step 1**: Create new Site Page titled "Fall Festival 2026 -- Committee Hub"
- [ ] **Step 2**: **[WEB PART]** Add Hero web part with fall-themed branding (Section 1)
- [ ] **Step 3**: **[WEB PART]** Add Quick Links with internal lists (Section 2)
- [ ] **Step 4**: **[WEB PART]** Add List web part > Event Tasks > view "Grouped by work item progress" (Section 3)
- [ ] **Step 4b**: **[WEB PART]** (Optional) Add second List web part > view "Grouped by priority" (Section 3)
- [ ] **Step 5**: **[TEXT]** Paste Event Quick Reference (Section 4)
- [ ] **Step 6**: **[TEXT]** Paste Activities & Attractions (Section 5)
- [ ] **Step 7**: **[TEXT]** Paste Committee Contacts & Roles (Section 6)
- [ ] **Step 8**: **[WEB PART]** Add Document Library web part (Section 7)
- [ ] **Step 9**: Upload event documents to the library
- [ ] **Step 10**: Publish page and set as Home Page
- [ ] **Step 11**: Verify all committee members have access via M365 Group
