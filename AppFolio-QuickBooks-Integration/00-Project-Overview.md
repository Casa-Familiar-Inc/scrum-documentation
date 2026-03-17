---
title: AppFolio to QuickBooks Integration
status: In Progress
it_analyst: Nefi Lopez (PM/Coordinator)
vendor: Dancing Numbers (India)
accounting_method: Accrual
tags: [integration, quickbooks, appfolio, uat, vendor-management]
date_created: 2026-03-16
---

# AppFolio to QuickBooks Integration

## Organizational Context
Casa Familiar is migrating financial data from AppFolio to QuickBooks Desktop using an Accrual Accounting method. We have hired an external vendor in India, **Dancing Numbers**, who has a proven and robust solution for this mapping. 

## My Role (IT Analyst / Project Manager)
My primary role here is **NOT** software development. It is Project Management (PM) and Infrastructure Coordination:
1. Provide the vendor with a technical environment to test their solution (UAT Server).
2. Facilitate communication between the vendor and our internal Accounting/Finance stakeholders.
3. Ensure the project keeps moving and blockages are resolved.

## Technical Architecture (UAT)
- **Environment**: Isolated UAT VM restricted from Casa Familiar's main network.
- **Access**: Internet access enabled, secured via **Tailscale**.
- **Software**: QuickBooks Desktop (Demo version, 30-day trial).
- **Data**: Database loaded with operational lists (Accounts, Vendors, etc.), but NO live transactions yet.
- **Maintenance**: VM Snapshotting enabled. Every 30 days, the VM state is rolled back to reset the QuickBooks trial license, requiring a quick re-installation.

## Current Major Blocker
- **Issue**: Dancing Numbers requires Casa Familiar's internal stakeholder to verify the mapped accounting data is accurate before they proceed.
- **Status**: The internal stakeholder is unresponsive (no Teams, no Email) for over a week. The project cannot advance to the next development phase without this validation.
