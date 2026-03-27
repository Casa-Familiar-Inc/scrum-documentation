---
title: Product Backlog - SharePoint Events Portal
last_update: 2026-03-17
tags: [backlog, sharepoint, automation, epic, user-story, ac]
---

# Product Backlog - SharePoint Events Portal

This backlog breaks down the technical and operational requirements for the Casa Familiar Events system.

## Epic 1: Hub Architecture & Data Governance
**Description**: Set up the central infrastructure to ensure all event sites share the same data definitions.
**Sprint**: Sprint 1 (Mar 18, 2026 - Mar 31, 2026)
**JIRA Epic**: EPIC 1: HUB ARCHITECTURE

### US-01: Hub Site & Global Column Setup
**As an** IT Analyst,
**I want to** configure a Hub Site and create centralized Site Columns,
**In order to** standardize the definition of "Status", "Year Cycle", and "Priority" across all events.
- **Complexity**: Medium
- **Story Points**: 5
- **Sprint**: Sprint 1
- **JIRA IDs**: CF-41 (US), CF-42, CF-43, CF-44, CF-45 (Tasks)
- **Acceptance Criteria**:
  - [ ] Hub Site "Casa Familiar Events" is registered.
  - [ ] Global Site Columns (CF_TaskStatus, CF_YearCycle) are created at the Hub level.
  - [ ] Content Types are published to the Content Type Hub.
- **Tasks**:
  1. `CF-42` Create M365 Communication Site for the Hub.
  2. `CF-43` Register site as a Hub in SharePoint Admin Center.
  3. `CF-44` Create Site Columns with standardized choice options.
  4. `CF-45` Create "Event Task" Content Type.

---

## Epic 2: Automated Site Deployment (Low-Code)
**Description**: Automate the creation of event sites to eliminate manual setup errors.
**Sprint**: Sprint 2-3 (Apr 1 - Apr 28, 2026)

### US-02: Site Script & Site Design Development
**As an** IT Analyst,
**I want to** develop JSON-based Site Scripts,
**In order to** install standard lists (Tasks, Roster, Budget) automatically on new sites.
- **Complexity**: High
- **Acceptance Criteria**:
  - [ ] JSON Site Script defines the 4 core lists (Tasks, Risks, Roster, Budget).
  - [ ] Site Design is available in the "From your organization" tab during site creation.
  - [ ] Deployment to 5 initial sites (Fall Festival, etc.) takes less than 5 minutes each.
- **Tasks**:
  1. Export list schemas to JSON.
  2. Write the Site Script manifest.
  3. Register Site Design via PnP PowerShell.
  4. Test deployment on a sandbox site.

---

## Epic 3: UI Customization & Advanced Views
**Description**: Use JSON formatting to make the interface intuitive for volunteers.
**Sprint**: Sprint 4 (Apr 29, 2026 - May 12, 2026)

### US-03: Advanced List Formatting
**As a** Committee Member,
**I want to** see tasks color-coded based on their status,
**In order to** immediately identify blocked items.
- **Complexity**: Medium
- **Acceptance Criteria**:
  - [ ] "Status" column uses JSON formatting (Green for Completed, Red for Blocked).
  - [ ] Entire row formatting applied to the Task List for high visibility.
- **Tasks**:
  1. Develop JSON formatting code for status columns.
  2. Apply conditional formatting to the "Blocked" state.
  3. Configure "High Priority" view on each list.

---

## Epic 4: Operational Flows & Rollover
**Description**: Automate notifications and the transition between event years.
**Sprint**: Sprint 5 (May 13, 2026 - May 26, 2026)

### US-04: Daily Expiry Notifications
**As an** Event Lead,
**I want to** receive a daily summary of overdue tasks via Power Automate,
**In order to** keep my committee accountable.
- **Complexity**: Medium
- **Acceptance Criteria**:
  - [ ] Power Automate flow runs daily.
  - [ ] Email digest sent to leads containing only overdue or blocked tasks.

---

## Epic 5: Governance & Adoption
**Description**: Ensure security and provide training materials for high-turnover committees.
**Sprint**: Sprint 6 (May 27, 2026 - Jun 09, 2026)

### US-05: Secure Offboarding Configuration
**As an** IT Administrator,
**I want to** restrict list deletion permissions,
**In order to** prevent accidental data loss by volunteers.
- **Complexity**: Low
- **Acceptance Criteria**:
  - [ ] "Contribute without Delete" permission level created.
  - [ ] Applied to all "Committee Member" groups.

---

## Epic 6: Event Site Deployments & Historical Consolidation
**Description**: Setup of event SharePoint sites (Abrazo 2026, Fall Festival 2026) and archival of past knowledge.
**Sprint**: Sprint 1 (Mar 18, 2026 - Mar 31, 2026)
**JIRA Epic**: EPIC 6: EVENT SITES

### US-06: Review Abrazo 2024 & Create Urgent Abrazo 2026
**As an** IT Analyst,
**I want to** audit the structure of Abrazo 2024 and deploy the new 2026 site,
**In order to** provide the event committee with a functional workspace for the current year.
- **Complexity**: High (Urgent)
- **Story Points**: 8
- **Sprint**: Sprint 1
- **JIRA IDs**: SP-US06
- **Acceptance Criteria**:
  - [x] Structure of Abrazo 2024 list/folders analyzed.
  - [ ] Site "Abrazo 2026" created using the new Hub standard.
  - [ ] Home Page deployed with event content (Hero, Schedule, Pricing, Quick Links).
  - [ ] RunSignUp registration embedded or linked on Home Page.
  - [ ] Core lists (Tasks, Roster, Budget) provisioned.
  - [ ] M365 Group & permissions configured for Committee Members.
- **Tasks**:
  1. `CF-T01` Audit Abrazo 2024 permissions and structure. **(Done)**
  2. `CF-T02` Create "Abrazo 2026" communication site.
  3. `CF-T03` Associate 2026 site to the Events Hub.
  4. `CF-T04` Build Home Page using modern web parts + content from `abrazo-2026/01-SharePoint-Home-Page-Content.md`.
  5. `CF-T05` Embed RunSignUp registration widget/link on Home Page.
  6. `CF-T06` Configure M365 Group and set permissions.
  7. `CF-T07` Provision core lists (Tasks, Roster, Budget) -- via Site Script or manual.
- **Reference Docs**:
  - Event Overview: [[abrazo-2026/00-Event-Overview.md]]
  - SharePoint Content: [[abrazo-2026/01-SharePoint-Home-Page-Content.md]]
  - Project Plan: [[abrazo-2026/02-Abrazo-2026-Project-Plan.md]]

---

### US-09: Create Fall Festival 2026 Shell Site
**As an** IT Analyst,
**I want to** deploy a SharePoint Communication Site shell for the Fall Festival 2026,
**In order to** have the infrastructure ready before the committee is assembled, enabling a faster handoff when planning begins.
- **Complexity**: Medium
- **Story Points**: 5
- **Sprint**: Sprint 1
- **JIRA IDs**: TBD
- **Acceptance Criteria**:
  - [ ] Site "Fall Festival 2026" created as Communication Site.
  - [ ] Site associated to the Events Hub.
  - [ ] Core lists (Tasks, Roster, Budget, Risks) provisioned using Work Progress Tracker template.
  - [ ] Home Page shell deployed with web parts and placeholder content.
  - [ ] Document Library folder structure created (Flyers, Vendor-Contracts, Permits, etc.).
  - [ ] M365 Group created for future committee members.
- **Tasks**:
  1. `CF-T08` Create "Fall Festival 2026" Communication Site.
  2. `CF-T09` Associate site to the Events Hub.
  3. `CF-T10` Provision core lists (same schema as Abrazo).
  4. `CF-T11` Build Home Page shell using web parts + content from `fall-festival-2026/01-SharePoint-Home-Page-Content.md`.
  5. `CF-T12` Create Document Library folder structure.
  6. `CF-T13` Configure M365 Group and set initial permissions.
- **Event Details (known)**:
  - **Location**: San Ysidro Civic Center, 212 W Park Ave, San Diego, CA 92173
  - **Admission**: Free, walk-in only
  - **Activities**: Pumpkin patch, food vendors, community activities
  - **Date**: TBD (October 2026 estimated)
  - **Committee**: Not yet assembled
- **Reference Docs**:
  - Event Overview: [[fall-festival-2026/00-Event-Overview.md]]
  - SharePoint Content: [[fall-festival-2026/01-SharePoint-Home-Page-Content.md]]
  - Project Plan: [[fall-festival-2026/02-Fall-Festival-Project-Plan.md]]
  - Task List Design: [[fall-festival-2026/03-Event-Tasks-List-Design.md]]

---

### US-07: Committee Leads Discovery & Outreach
**As an** IT Analyst,
**I want to** identify previous event leads and request historical data,
**In order to** centralize organizational knowledge in SharePoint.
- **Complexity**: Medium
- **Story Points**: 5
- **Acceptance Criteria**:
  - [ ] List of leads from past Abrazo events identified (via Karla Torres).
  - [ ] Standardized email sent to leads requesting event documentation.
  - [ ] Historical folders created for each past event identified.
- **Tasks**:
  1. Sync with Karla Torres/Ricardo to identify past leads.
  2. Draft and send outreach email to leads.
  3. Consolidate received documents into legacy event sites.

### US-08: Events Committee Training & Sync
**As a** Scrum Master,
**I want to** hold a kickoff meeting with the Events Committee,
**In order to** align expectations, present progress, and train them on the new lists.
- **Complexity**: Medium
- **Story Points**: 3
- **Acceptance Criteria**:
  - [ ] 30-min meeting held with the full committee.
  - [ ] "Progress Report" presented.
  - [ ] Training on "Task Lists" and "JSON Formatting" basics provided.
- **Tasks**:
  1. Schedule meeting with the committee.
  2. Prepare report and training materials.
  3. Log feedback and expectations in Obsidian.

