---
title: Abrazo 2026 - SharePoint Site Implementation Plan
project: SharePoint Events Portal
event_date: 2026-05-02
status: In Progress
sprint: Sprint 1 (Mar 18 - Mar 31, 2026)
tags: [project-plan, abrazo, sharepoint, timeline, workflow, IT]
last_update: 2026-03-26
---

# Abrazo 2026 - SharePoint Site Implementation Plan

> [!NOTE]
> This plan covers **IT scope only** -- the SharePoint site creation, configuration, and deployment. Event coordination tasks (volunteers, sponsors, logistics) are managed by the event committee directly.

## Project Timeline

```mermaid
gantt
    title Abrazo 2026 - IT Implementation Timeline
    dateFormat YYYY-MM-DD
    axisFormat %b %d

    section Site Creation
    Audit Abrazo 2024 Structure         :done, audit, 2026-03-18, 3d
    Create Abrazo 2026 SP Site          :active, site, 2026-03-26, 2d
    Associate to Events Hub             :hub, 2026-03-27, 1d

    section Configuration
    Configure M365 Group & Permissions  :perms, 2026-03-28, 1d
    Provision Core Lists                :lists, 2026-03-28, 2d
    Customize List Views & Columns      :views, 2026-03-29, 1d

    section Content Deployment
    Build Home Page with Web Parts      :content, 2026-03-30, 2d
    Add RunSignUp CTA Link              :link, 2026-03-31, 1d
    Create Document Library Structure   :docs, 2026-03-31, 1d

    section Handoff
    Training Session with Committee     :training, 2026-04-01, 2d
```

---

## Task Breakdown

### Phase 1: Site Creation (Sprint 1)

| # | Task | Priority | Status | Due |
|---|------|----------|--------|-----|
| 1 | Audit Abrazo 2024 SharePoint structure and permissions | High | Done | Mar 20 |
| 2 | Create "Abrazo 2026" Communication Site in SharePoint | High | To Do | Mar 28 |
| 3 | Associate Abrazo 2026 site to the Events Hub | High | To Do | Mar 28 |

### Phase 2: Configuration (Sprint 1)

| # | Task | Priority | Status | Due |
|---|------|----------|--------|-----|
| 4 | Configure M365 Group and permissions for Committee Members | Medium | To Do | Mar 30 |
| 5 | Provision core lists (Event Tasks, Roster, Budget, Risks) using Work Progress Tracker template | High | To Do | Mar 31 |
| 6 | Customize Category column with event-specific choices (see [[03-Event-Tasks-List-Design.md]]) | Medium | To Do | Mar 31 |
| 7 | Add custom columns (Phase, Week) to Event Tasks list | Low | To Do | Mar 31 |

### Phase 3: Content Deployment (Sprint 1)

| # | Task | Priority | Status | Due |
|---|------|----------|--------|-----|
| 8 | Build Home Page using modern web parts (Hero, Quick Links, List, Document Library) | High | To Do | Mar 30 |
| 9 | Paste event content into Text web parts (see [[01-SharePoint-Home-Page-Content.md]]) | Medium | To Do | Mar 31 |
| 10 | Add RunSignUp Call to Action link on Home Page | Low | To Do | Mar 31 |
| 11 | Create Document Library folder structure (Flyers, Contracts, Volunteer-Info, etc.) | Medium | To Do | Mar 31 |
| 12 | Publish page and set as Home Page | Medium | To Do | Mar 31 |

### Phase 4: Handoff (Sprint 2)

| # | Task | Priority | Status | Due |
|---|------|----------|--------|-----|
| 13 | Conduct SharePoint training session for committee members | Medium | To Do | Apr 3 |
| 14 | Create legacy folders for past Abrazo events (2024, etc.) | Low | To Do | Apr 7 |

---

## Workflow: SharePoint Site Deployment

```mermaid
flowchart TD
    A[Start: Create Communication Site] --> B[Associate to Events Hub]
    B --> C[Configure M365 Group & Permissions]
    C --> D[Provision Core Lists]
    D --> E{Use Site Script?}
    E -->|Yes| F[Deploy via Site Script JSON]
    E -->|No| G[Create Lists Manually]
    F --> H[Customize List Columns & Views]
    G --> H
    H --> I[Build Home Page]
    I --> J[Add Hero Banner]
    J --> K[Add List Web Parts]
    K --> L[Add Text Web Parts with Content]
    L --> M[Add Quick Links & CTA]
    M --> N[Add Document Library Web Part]
    N --> O[Publish Page & Set as Home]
    O --> P[Handoff: Training Session]
```

---

## Key Dependencies

```mermaid
flowchart LR
    subgraph Blockers
        B1[Hub Site must be registered first - Epic 1]
    end

    subgraph IT Implementation
        A1[Create SP Site]
        A2[Configure Lists & Permissions]
        A3[Deploy Home Page Content]
        A4[Handoff to Committee]
    end

    B1 --> A1
    A1 --> A2
    A2 --> A3
    A3 --> A4
```

> [!WARNING]
> **Dependency**: If Epic 1 (Hub Site registration) is not completed first, the Abrazo 2026 site can still be created as a standalone Communication Site, but it will need to be manually re-associated to the Hub later.

---

## IT Milestones

| Date | Milestone |
|:----:|-----------|
| Mar 28 | SharePoint site created and associated to Hub |
| Mar 31 | Lists provisioned, permissions configured, Home Page live |
| Apr 3 | Committee training completed -- site handed off |

---

## JIRA Alignment

| JIRA ID | Story/Task | Sprint |
|---------|------------|--------|
| SP-US06 | Create Urgent Abrazo 2026 Site | Sprint 1 |

> [!NOTE]
> New sub-tasks may need to be created in JIRA for the Home Page setup and list configuration tasks (Tasks 4-12 above). Consider creating them under SP-US06.
