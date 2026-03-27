---
title: Abrazo 2026 - SharePoint Home Page Content (Internal Team)
purpose: Ready-to-paste content for internal SharePoint team site
audience: Abrazo 2026 Committee & Casa Familiar Staff
approach: Hybrid (Modern Page web parts + Text content blocks)
tags: [sharepoint, content, abrazo, internal, committee, copy-paste]
last_update: 2026-03-26
---

# SharePoint Home Page Content - Abrazo 2026 (Internal)

> [!IMPORTANT]
> This is an **internal team site** for the Abrazo 2026 committee. The content is written for staff and committee members, not the public. The public-facing registration page is RunSignUp.

---

## Section 1: Hero Banner

> **Web Part**: Hero (Full Width)
> **Layout**: One layer

**Title**: Abrazo 2026 -- Committee Hub
**Subtitle**: 5K Walk & 10K Run | Saturday, May 2, 2026 | Las Americas Premium Outlets
**CTA Button Text**: View Task List
**CTA Button Link**: *(link to the SharePoint Tasks list once created)*
**Image**: Event flyer or Casa Familiar branding

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
| 4 | Event Documents | SharePoint Document Library | Flyers, contracts, permits, maps |
| 5 | RunSignUp Dashboard | https://runsignup.com/Race/CA/SanYsidro/CasaFamiliar5k | Public registration page (reference) |
| 6 | Course Map | https://runsignup.com/Race/CasaFamiliar5k/Page/course | Route details |
| 7 | Volunteer Sign-ups | https://runsignup.com/Race/CasaFamiliar5k/Page/Volunteer | External volunteer form |

---

## Section 3: Event Tasks (List Web Parts)

> **Web Part**: List (native)
> **Source**: Event Tasks list (Work Progress Tracker template)
> Do NOT use static text here. The List web part updates automatically when committee members edit items.

### Predefined Template Views

The Work Progress Tracker template already includes these 5 views ready to use:

| # | View | What it Does | Home Page Use |
|---|------|-------------|---------------|
| 1 | **All Items** | All items unfiltered | General management, not ideal for home page |
| 2 | **Grouped by priority** | Groups by Critical > High > Medium > Low | Good for committee meetings |
| 3 | **Grouped by work item progress** | Groups by Not Started > In Progress > Behind > Blocked > Completed | **Recommended as primary home page view** |
| 4 | **My work items** | Filters to only tasks assigned to the logged-in user [Me] | For individual committee members to see their own tasks |
| 5 | **Progress board** | Kanban-style board with columns by status | For collaborative work sessions (drag-and-drop) |

### List Web Part Configuration on the Page

1. Add a **List** web part to the page
2. Select the **Event Tasks** list
3. Select the view **"Grouped by work item progress"** as default
4. Committee members can edit items directly from the Home Page by clicking on any item

> [!TIP]
> **Progress board** works better in full screen, not embedded. Add a Quick Link in Section 2 called **"Open Task Board"** pointing directly to the list with the Progress board view.

### (Optional) Second List Web Part

Add a second List web part below the primary one with the view **"Grouped by priority"** to provide a priority-first perspective for leadership.

### (Optional) Additional Custom Views

If you need more specific views, create these in the list (see details in [[03-Event-Tasks-List-Design.md]]):

| Custom View | Filter | Use |
|-------------|--------|-----|
| **Upcoming Deadlines** | Due Date >= [Today] AND Progress != "Completed" | Focused view on what is coming up next |
| **Blocked Items** | Progress = "Blocked" | Keep blocked items always visible |

---

## Section 4: Event Quick Reference (Text Web Part)

Copy and paste into a **Text** web part. This gives committee members fast access to event details when someone asks:

---

### Event Details -- Quick Reference

| Field | Detail |
|-------|--------|
| **Event** | Abrazo 5K Walk & 10K Run 2026 |
| **Theme** | "Get Up, Stand Up" (Rasta / Bob Marley) |
| **Date** | Saturday, May 2, 2026 |
| **Time** | 6:30 AM - 11:00 AM |
| **Location** | Las Americas Premium Outlets |
| **Address** | 4061 Camino De La Plaza #490, San Ysidro, CA 92173 |
| **Registration URL** | https://runsignup.com/Race/CA/SanYsidro/CasaFamiliar5k |
| **Short Link** | bit.ly/abrazo26 |
| **Expected Attendance** | 300+ participants |

### Day-of Schedule

| Time | Activity |
|------|----------|
| 6:30 AM | Registration Opens |
| 7:00 AM | Welcome Ceremony |
| 7:30 AM | 10K Run Start |
| 7:35 AM | 5K Walk Start |
| 8:45 AM - 11:00 AM | Awards, Raffles & Celebration |

---

## Section 5: Pricing Reference (Text Web Part)

Copy and paste into a **Text** web part. Useful when committee members need to answer pricing questions:

---

### Pricing Quick Reference

#### 5K Walk

| Who | Price | Includes |
|-----|:---:|------|
| General Registrant | $50 | T-Shirts, Bibs, Medals + Food & Drink Bracelet (2 burritos + 2 drinks) |
| Casa Program Participant | $20 | T-Shirts, Bibs, Medals *(Food & Drink Bracelet NOT included)* |

#### 10K Run

| Who | Price | Includes |
|-----|:---:|------|
| General Registrant | $65 | T-Shirts, Bibs, Medals + Food & Drink Bracelet (2 burritos + 2 drinks) |
| Casa Program Participant | $20 | T-Shirts, Bibs, Medals *(Food & Drink Bracelet NOT included)* |

#### Additional Purchases

| Item | Price |
|------|:---:|
| Food & Drink Bracelet (2 burritos + 2 drinks) | $25 |

### Common Questions from Participants

| Question | Answer |
|----------|--------|
| Kids pricing? | Free for 12 & under. T-shirts, food, beverages NOT included. Recommend buying Food & Drink Bracelet. |
| Cash payments? | Yes. Direct to Rec 2 Reception (268 W Park Ave, San Ysidro, CA 92173). Exact change only. |
| Beer Garden? | Yes, returning this year. Access included with Food & Drink Bracelet. |
| Dress code? | Rasta theme encouraged -- socks, headbands, wristbands, anything. |

---

## Section 6: Committee Contacts & Roles (Text Web Part)

Copy and paste into a **Text** web part:

---

### Committee Contacts

| Role | Name | Email | Responsibility |
|------|------|-------|----------------|
| IT / SharePoint | Nefi | *(internal)* | Site setup, permissions, automation |
| Volunteer Coordinator | Sergio | sergiog@casafamiliar.org | Volunteer recruitment & day-of coordination |
| Sponsorship & Exhibitors | Ricardo | ricardog@casafamiliar.org | Sponsor outreach, exhibitor logistics |
| General Inquiries | Casa Familiar | info@casafamiliar.org | Public-facing email for participants |
| Event Lead | *(TBD)* | *(TBD)* | Overall event coordination |

> [!NOTE]
> Update the Event Lead once committee kickoff meeting is completed and leads are confirmed.

---

## Section 7: RunSignUp Registration Link

> **Web Part**: Call to Action or Text
> RunSignUp blocks iframe embedding (X-Frame-Options). Use a direct link instead.

1. Add a **Call to Action** or **Text** web part with a prominent link
2. Configure:

| Field | Value |
|-------|-------|
| **Heading** | RunSignUp Registration Page (External) |
| **Description** | Public registration page for participants. Use this link to check registration numbers and share with participants. |
| **Button Text** | Open RunSignUp |
| **Button Link** | https://runsignup.com/Race/CA/SanYsidro/CasaFamiliar5k |

> [!NOTE]
> This link is already included in Quick Links (Section 2). This section is optional if you want to give more visibility to the registration link.

---

## Section 8: Important Documents (Document Library Web Part)

> **Web Part**: Document Library (native)
> **Purpose**: Surface the event documents folder directly on the home page

1. Add a **Document Library** web part
2. Point it to the "Abrazo 2026" document library or folder
3. Suggested folder structure inside the library:

```
Abrazo-2026-Documents/
  Flyers-Marketing/
  Contracts-Permits/
  Sponsor-Materials/
  Volunteer-Info/
  Meeting-Notes/
  Day-of-Logistics/
```

---

## SharePoint Page Setup Checklist (Internal Team Site)

- [ ] **Step 1**: Create new Site Page titled "Abrazo 2026 -- Committee Hub"
- [ ] **Step 2**: **[WEB PART]** Add Hero web part (Section 1)
- [ ] **Step 3**: **[WEB PART]** Add Quick Links with internal lists + RunSignUp + "Open Task Board" link (Section 2)
- [ ] **Step 4**: **[WEB PART]** Add List web part > Event Tasks > view "Grouped by work item progress" (Section 3)
- [ ] **Step 4b**: **[WEB PART]** (Optional) Add second List web part > view "Grouped by priority" (Section 3)
- [ ] **Step 5**: **[TEXT]** Paste Event Quick Reference (Section 4) -- use two-column layout
- [ ] **Step 6**: **[TEXT]** Paste Pricing tables + FAQ (Section 5)
- [ ] **Step 7**: **[TEXT]** Paste Committee Contacts & Roles (Section 6)
- [ ] **Step 8**: **[WEB PART]** Add Call to Action link for RunSignUp (Section 7, optional)
- [ ] **Step 9**: **[WEB PART]** Add Document Library web part (Section 8)
- [ ] **Step 10**: Upload event documents to the library
- [ ] **Step 11**: Publish page and set as Home Page
- [ ] **Step 12**: Verify all committee members have access via M365 Group
