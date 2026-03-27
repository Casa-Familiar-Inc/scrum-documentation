---
title: Fall Festival 2026 - SharePoint Site Implementation Plan
project: SharePoint Events Portal
event_date: TBD (October 2026 - estimated)
status: In Progress
sprint: Sprint 1 (Mar 18 - Mar 31, 2026)
tags: [project-plan, fall-festival, sharepoint, timeline, workflow, IT]
last_update: 2026-03-27
---

# Fall Festival 2026 - SharePoint Site Implementation Plan

> [!NOTE]
> This plan covers **IT scope only** -- the SharePoint site creation, configuration, and deployment. Event coordination tasks (vendors, volunteers, activities, logistics) are managed by the event committee directly.

> [!IMPORTANT]
> This is a **shell deployment** -- the SharePoint site structure is being set up now (Sprint 1) in anticipation of the event. Content details (schedule, activities, contacts) will be populated as the committee is assembled and planning progresses.

## Project Timeline

```mermaid
gantt
    title Fall Festival 2026 - IT Implementation Timeline
    dateFormat YYYY-MM-DD
    axisFormat %b %d

    section Site Creation
    Create Fall Festival 2026 SP Site       :active, site, 2026-03-27, 2d
    Associate to Events Hub                 :hub, 2026-03-28, 1d

    section Configuration
    Configure M365 Group & Permissions      :perms, 2026-03-28, 1d
    Provision Core Lists                    :lists, 2026-03-28, 2d
    Customize List Views & Columns          :views, 2026-03-29, 1d

    section Content Deployment
    Build Home Page with Web Parts          :content, 2026-03-29, 2d
    Create Document Library Structure       :docs, 2026-03-30, 1d

    section Handoff
    Handoff to Committee (when assembled)   :training, 2026-04-01, 5d
```

---

## Task Breakdown

### Phase 1: Site Creation (Sprint 1)

| # | Task | Priority | Status | Due |
|---|------|----------|--------|-----|
| 1 | Create "Fall Festival 2026" Communication Site in SharePoint | High | To Do | Mar 28 |
| 2 | Associate Fall Festival 2026 site to the Events Hub | High | To Do | Mar 28 |

### Phase 2: Configuration (Sprint 1)

| # | Task | Priority | Status | Due |
|---|------|----------|--------|-----|
| 3 | Configure M365 Group and permissions for Committee Members | Medium | To Do | Mar 30 |
| 4 | Provision core lists (Event Tasks, Roster, Budget, Risks) using Work Progress Tracker template | High | To Do | Mar 31 |
| 5 | Customize Category column with event-specific choices (see [[03-Event-Tasks-List-Design.md]]) | Medium | To Do | Mar 31 |
| 6 | Add custom columns (Phase, Week) to Event Tasks list | Low | To Do | Mar 31 |

### Phase 3: Content Deployment (Sprint 1)

| # | Task | Priority | Status | Due |
|---|------|----------|--------|-----|
| 7 | Build Home Page using modern web parts (Hero, Quick Links, List, Document Library) | High | To Do | Mar 30 |
| 8 | Paste event content into Text web parts (see [[01-SharePoint-Home-Page-Content.md]]) | Medium | To Do | Mar 31 |
| 9 | Create Document Library folder structure (Flyers, Vendor-Contracts, Permits, Volunteer-Info, etc.) | Medium | To Do | Mar 31 |
| 10 | Publish page and set as Home Page | Medium | To Do | Mar 31 |

### Phase 4: Handoff (Sprint 2+)

| # | Task | Priority | Status | Due |
|---|------|----------|--------|-----|
| 11 | Conduct SharePoint training session for committee members (when assembled) | Medium | To Do | TBD |

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
    I --> J[Add Hero Banner - Fall Theme]
    J --> K[Add List Web Parts]
    K --> L[Add Text Web Parts - TBD Content]
    L --> M[Add Quick Links - Internal Only]
    M --> N[Add Document Library Web Part]
    N --> O[Publish Page & Set as Home]
    O --> P[Handoff: Training Session - When Committee Ready]
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
        A3[Deploy Home Page Shell]
        A4[Handoff to Committee - TBD]
    end

    B1 --> A1
    A1 --> A2
    A2 --> A3
    A3 --> A4
```

> [!WARNING]
> **Dependency**: If Epic 1 (Hub Site registration) is not completed first, the Fall Festival 2026 site can still be created as a standalone Communication Site, but it will need to be manually re-associated to the Hub later.

---

## Key Differences from Abrazo 2026

| Area | Abrazo 2026 | Fall Festival 2026 |
|------|------------|-------------------|
| External registration | RunSignUp CTA link required | None -- free walk-in event |
| Pricing sections | 5K/10K pricing tables on home page | No pricing -- free admission |
| Course map | RunSignUp course map link | Not applicable |
| Content readiness | Full content ready at deployment | Shell only -- content TBD |
| Committee | Assembled, contacts known | Not yet assembled |

---

## IT Milestones

| Date | Milestone |
|:----:|-----------| 
| Mar 28 | SharePoint site created and associated to Hub |
| Mar 31 | Lists provisioned, permissions configured, Home Page shell live |
| TBD | Committee training completed -- site handed off |

---

## JIRA Alignment

| JIRA ID | Story/Task | Sprint |
|---------|------------|--------|
| TBD | Create Fall Festival 2026 Shell Site | Sprint 1 |

> [!NOTE]
> A new user story needs to be created in JIRA for the Fall Festival site deployment. Recommend creating under the SharePoint Events Portal project, similar to SP-US06 for Abrazo.
