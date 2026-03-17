---
title: Product Backlog - SharePoint Events Portal
tags: [backlog, sharepoint, automation, epic, user-story, ac]
---

# Product Backlog - SharePoint Events Portal

This backlog breaks down the technical and operational requirements for the Casa Familiar Events system.

## Epic 1: Hub Architecture & Data Governance
**Description**: Set up the central infrastructure to ensure all event sites share the same data definitions.
**Estimated Duration**: Sprint 1 (Mar 18, 2026 - Mar 31, 2026)

### US-01: Hub Site & Global Column Setup
**As an** IT Analyst,
**I want to** configure a Hub Site and create centralized Site Columns,
**In order to** standardize the definition of "Status", "Year Cycle", and "Priority" across all events.
- **Complexity**: Medium
- **Acceptance Criteria**:
  - [ ] Hub Site "Casa Familiar Events" is registered.
  - [ ] Global Site Columns (CF_TaskStatus, CF_YearCycle) are created at the Hub level.
  - [ ] Content Types are published to the Content Type Hub.
- **Tasks**:
  1. Create M365 Communication Site for the Hub.
  2. Register site as a Hub in SharePoint Admin Center.
  3. Create Site Columns with standardized choice options.
  4. Create "Event Task" Content Type.

---

## Epic 2: Automated Site Deployment (Low-Code)
**Description**: Automate the creation of event sites to eliminate manual setup errors.
**Estimated Duration**: Sprint 3 (Apr 15, 2026 - Apr 28, 2026)

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
**Estimated Duration**: Sprint 4 (Apr 29, 2026 - May 12, 2026)

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
**Estimated Duration**: Sprint 5 (May 13, 2026 - May 26, 2026)

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
**Estimated Duration**: Sprint 6 (May 27, 2026 - Jun 09, 2026)

### US-05: Secure Offboarding Configuration
**As an** IT Administrator,
**I want to** restrict list deletion permissions,
**In order to** prevent accidental data loss by volunteers.
- **Complexity**: Low
- **Acceptance Criteria**:
  - [ ] "Contribute without Delete" permission level created.
  - [ ] Applied to all "Committee Member" groups.
