---
title: Interview Guide: Gema (SS) and Mayra (FOC)
tags: [interview, discovery, kpis, automation, research, sprint-1]
---

# Interview Guide for Gema and Mayra Visits

As an IT Analyst seeking to understand KPIs for Salesforce and automation opportunities, this guide provides the structure for your research visits scheduled for Sprint 1.

## Meeting Objective (Your Pitch)
"The goal of my visit today is to understand the challenges you face building your reports. We want to see how the intakes built in Salesforce can make your life easier and reduce manual work through automation."

## Technical Tasks & Checklist

### 1. Workflow Mapping (Mermaid Documentation)
- [ ] Observe the full path from client arrival to data entry.
- [ ] Diagram the "As-Is" process (who touches the data, which system is used).
- [ ] Identify points where data leaves Salesforce and enters an Excel/Paper process.

### 2. Intake Audit (Salesforce vs. Legacy)
- [ ] Record a step-by-step entry of a new client into the Salesforce intake.
- [ ] Compare current Salesforce fields with legacy Excel columns.
- [ ] **Gap Analysis**: List specific fields required for management but missing in Salesforce.

### 3. Report & Formula Audit (Gema - Social Services)
- [ ] Collect 3+ samples of manual reports used for immigration or procedures.
- [ ] Identify friction points in generating these summaries.

### 4. Financial & Grant Audit (Mayra - FOC)
- [ ] Perform a full "Shadowing" session of one financial counseling intake.
- [ ] **Formula Documentation**: Copy and explain the logic of Excel formulas used for monthly reports.
- [ ] **Grant Compliance**: Identify exact fields required for Grant reporting (HUD, etc.).

## Key Questions for the Interview

### Current Reporting & Data Provenance
- **Data Sources**: Exactly where do you pull the data from? (e.g., Salesforce export, separate personal Excel, paper intake, email, or legacy database?)
- **Consolidation**: Do you have to merge data from multiple Excel files to create one report? If so, how do you do it? (e.g., Copy-paste, VLOOKUPs, or manual tallying?)
- **Manual Effort**: How much time per month do you spend just searching for, cleaning, and consolidating this data before the report is actually ready?

### Pain Points & Low-Code Opportunities
- What task do you consider most tedious or repetitive during your week?
- Do you enter the same client information into more than one system?

## Strategic Notes for Nefi
- **Identify Manual Bottlenecks**: If data is downloaded to be manually filtered, that is a prime candidate for a Python script or Power Automate flow.
- **Listen for Real KPIs**: Focus on the metrics the directors actually care about for their executive dashboards.
- **Maintain Agile-Lite focus**: Do not promise a full system fix today; focus on "Quick Wins" using existing Office 365 tools.

---
*Reference: Salesforce Backlog US-01 and US-02.*
