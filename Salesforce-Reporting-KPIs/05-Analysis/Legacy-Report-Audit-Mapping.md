---
title: Legacy Report Audit & Salesforce Mapping Analysis
project: Salesforce Reporting & KPIs
it_analyst: Nefi Lopez
date: 2026-03-16
tags: [analysis, reporting, legacy-data, salesforce, audit]
---

# Analysis: Legacy Report Audit & Salesforce Mapping

To ensure a successful transition to Salesforce, we must perform a detailed audit of the reports currently used by Gema (Social Services) and Mayra (FOC). These "Legacy Reports" (mostly Excels) represent the current source of truth for the organization.

## Objectives of the Audit
1. **Identify Data Gaps**: Ensure Cloud Care's custom intakes capture all data points required by existing reports.
2. **Standardize Metrics**: Align disparate Excel formulas with Salesforce's automated reporting logic.
3. **Eliminate Redundancy**: Pinpoint fields that are manually calculated but could be automated.

## Audit Framework for Social Services (Gema)
| Legacy Report Requirement | Source of Truth (Existing) | Salesforce Object/Field (Goal) | Automation Potential |
| :--- | :--- | :--- | :--- |
| **Immigration Case Status** | Manual Excel Sheet | `Case` Object / `Status` Field | High (Auto-update via Flow) |
| **Demographic Breakdown** | Intake Form (Paper) | `Contact` Object / Custom Fields | High (Via Salesforce Intake) |
| **Procedure Completion Rate** | Monthly Calculation (Excel) | Calculated Summary Report | Total (Real-time Dashboard) |

## Audit Framework for FOC (Mayra)
| Legacy Report Requirement | Source of Truth (Existing) | Salesforce Object/Field (Goal) | Automation Potential |
| :--- | :--- | :--- | :--- |
| **Financial Literacy Attendance** | Sign-in Sheets / Excel | `Campaign` or `Event` Object | Medium (Barcode/Check-in App) |
| **Client Credit Score Change** | Historical Comparison Excel | `Engagement` Object / Custom Metrics | High (Auto-calculate Delta) |
| **Grant Performance Reports** | Manual Compilation (Quarterly) | Salesforce "Bucketed" Reports | High (Automated Schedules) |

## Gap Analysis Methodology (The "Audit Visit")
When visiting Gema and Mayra, use the following "Audit Checklist":
1. **Request Raw Data**: Ask for the latest exported Excel file they used to report to management.
2. **Trace the Path**: Ask: "To get this number (KPI), which cell in which Excel does it come from?"
3. **Check Cloud Care Alignment**: Compare those cells with the new Salesforce Intake fields. 
   - *If the field exists in Excel but not in Salesforce, we have a "Gap" that Cloud Care needs to fix.*

## Recommendation for the IT Analyst
Do not try to migrate every single Excel column. Instead, focus on the **"Top 5 metrics"** that actually go into the executive reports. Use **Power Automate** as a temporary bridge to clean legacy CSVs before uploading them to Salesforce to ensure data integrity.

---
*This analysis serves as the foundation for US-05 (Historical Data Migration) and Epic 3.*
