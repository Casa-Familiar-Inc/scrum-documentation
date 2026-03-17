---
title: Product Backlog - Salesforce KPIs
tags: [jira, backlog, scrum, sprint, epic, user-story]
---

# Product Backlog for JIRA

This document contains Epics and User Stories formatted for JIRA migration, utilizing 2-week Sprints and Story Points.

## Epic 1: Discovery Phase & Requirements Gathering
**Description**: Understand current FOC and Social Services processes to map reporting needs and KPIs.
**Estimated Duration**: Sprint 1 (Mar 18, 2026 - Mar 31, 2026)

### US-01: Social Services Site Visit (Gema)
**As an** IT Analyst,
**I want to** conduct a technical visit to Gema at Social Services,
**In order to** understand custom intake design and reporting pain points.
- **Story Points**: 3
- **Acceptance Criteria**:
  - [ ] Documented "As-Is" workflow for immigration/procedures.
  - [ ] Collection of 3+ sample manual reports currently used.
  - [ ] List of fields missing in the current Cloud Care intake design.
- **Tasks**:
  1. Schedule interview with Gema.
  2. Interview Gema using the Technical Guide.
  3. Map the current manual process in Mermaid.
  4. Compare legacy Excel fields with new Salesforce fields.

### US-02: FOC Site Visit (Mayra)
**As an** IT Analyst,
**I want to** conduct a technical visit to Mayra at FOC,
**In order to** understand financial service workflows and data tracking needs.
- **Story Points**: 3
- **Acceptance Criteria**:
  - [ ] Documented "As-Is" workflow for financial counseling.
  - [ ] Identification of duplicate data entry points between Salesforce and spreadsheets.
  - [ ] List of success metrics (KPIs) currently tracked manually.
- **Tasks**:
  1. Schedule interview with Mayra.
  2. Perform "Shadowing" session of one intake process.
  3. Document all Excel formulas used for monthly reporting.
  4. Identify fields required for Grant reporting.

---

## Epic 2: KPI Definition & Data Architecture
**Description**: Translate visit findings into structured metrics for Salesforce.
**Estimated Duration**: Sprint 2 (Apr 01, 2026 - Apr 14, 2026)

### US-03: KPI Specification for Social Services & FOC
**As a** Scrum Master/Analyst,
**I want to** define formal KPI specifications,
**In order to** align Salesforce development with management goals.
- **Story Points**: 5
- **Acceptance Criteria**:
  - [ ] Approved list of 5 core KPIs for each department.
  - [ ] Detailed "Calculation Logic" (formulas) for each KPI documented.
  - [ ] Mapping of KPIs to specific Salesforce Objects/Fields for Cloud Care team.
- **Tasks**:
  1. Draft the "KPI Definition Document".
  2. Present KPIs to center admins for validation.
  3. Technical review with Cloud Care consultants.
  4. Create technical mapping for Salesforce developer.

### US-04: Low-Code Automation Assessment
**As an** IT Analyst,
**I want to** analyze automation opportunities using Power Automate or Scripts,
**In order to** eliminate manual data cleaning tasks.
- **Story Points**: 8
- **Acceptance Criteria**:
  - [ ] Feasibility study for automated data exports from Cloud Care intakes.
  - [ ] Prototype of one automation (e.g., CSV auto-format script).
  - [ ] Documented cost/benefit analysis for the proposed tools.
- **Tasks**:
  1. Research Cloud Care API availability.
  2. Test Power Automate Salesforce connector.
  3. Build a "Proof of Concept" (POC) script for data cleaning.

---

## Epic 3: Data Consolidation & Integrity
**Description**: Ensure historical data is migrated and new data is high-quality.
**Estimated Duration**: Sprint 3 (Apr 15, 2026 - Apr 28, 2026)

### US-05: Historical Data Migration Strategy
**As a** Data Analyst,
**I want to** map and migrate historical Excel data to Salesforce,
**In order to** enable year-over-year reporting.
- **Story Points**: 13
- **Acceptance Criteria**:
  - [ ] Data mapping document (Source Excel -> Target Salesforce Object).
  - [ ] Successful trial migration of 100+ records in the Sandbox environment.
  - [ ] Sign-off from Admin (Gema/Mayra) on data accuracy after trial.
- **Tasks**:
  1. Consolidate last 12 months of Excel reports.
  2. Perform data deduplication and cleansing.
  3. Create Data Loader mapping files.
  4. Execute dry-run in Sandbox.

### US-06: Data Validation Rules Implementation
**As an** IT Analyst,
**I want to** implement Salesforce validation rules on intakes,
**In order to** prevent "dirty data" from affecting reports.
- **Story Points**: 3
- **Acceptance Criteria**:
  - [ ] Mandatory fields identified for all critical reporting paths.
  - [ ] 3+ validation rules implemented to ensure correct data formats.
- **Tasks**:
  1. Review data entry errors from past records.
  2. Create "Required Field" list per department.
  3. Build and test validation rules in Salesforce.

---

## Epic 4: Executive Visibility & Dashboards
**Description**: Build the visualization layer for the Boss and IT Management.
**Estimated Duration**: Sprint 4 (Apr 29, 2026 - May 12, 2026)

### US-07: Executive Dashboard Design
**As an** IT Analyst,
**I want to** design the "Casa Familiar Impact Dashboard",
**In order to** show real-time progress to IT Leadership.
- **Story Points**: 8
- **Acceptance Criteria**:
  - [ ] Dashboard contains at least 3 charts: (1) Total Intakes by Center, (2) Case Status Funnel, (3) KPI Achievement %.
  - [ ] Visual design follows organizational brand colors.
  - [ ] Dashboard is accessible via Mobile Salesforce App.
- **Tasks**:
  1. Create "Report Folder" structure in Salesforce.
  2. Build custom summary reports.
  3. Assemble Dashboard components.
  4. Test Mobile User Experience (UX).

### US-08: Automatic Status Report Template
**As an** IT Analyst,
**I want to** standardize the Monthly Status Report,
**In order to** provide consistent updates to my Boss.
- **Story Points**: 2
- **Acceptance Criteria**:
  - [ ] Standardized Markdown template linked to Agile tasks.
  - [ ] One-click export or update process documented.
  - [ ] Inclusive of a "Risks/Blockers" section for executive attention.
- **Tasks**:
  1. Refine the Markdown template for Obsidian.
  2. Create a "Report Update" workflow guide.
  3. Present the first version to the IT Director for feedback.
