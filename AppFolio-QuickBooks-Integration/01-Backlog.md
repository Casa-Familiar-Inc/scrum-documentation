---
title: Product Backlog - AppFolio to QuickBooks
tags: [backlog, quickbooks, uat, pm]
---

# Product Backlog - AppFolio to QuickBooks

## Epic 1: UAT Server Infrastructure & Maintenance
**Description**: Ensure Dancing Numbers has a stable, isolated environment to perform their test migrations.
**Estimated Duration**: Sprint 1 (Mar 18, 2026 - Mar 31, 2026)

### US-01: Finalize UAT Server Setup for Vendor
**As an** IT PM,
**I want to** finish provisioning the restricted UAT server via Tailscale,
**In order to** hand it over to Dancing Numbers as soon as environment readiness is required.
- **Priority**: High (Functional dependency for vendor)
- **Acceptance Criteria**:
  - [ ] Server is isolated from the main internal network.
  - [ ] Tailscale is installed and configured for vendor access.
  - [ ] QuickBooks Desktop demo is installed and loaded with base lists.
- **Tasks**:
  1. Verify Tailscale connectivity with a test account.
  2. Confirm QuickBooks database lists (no transactions) are accessible.
  3. Send credentials and connection guide to Dancing Numbers.

### US-02: QuickBooks Trial Rollback (Monthly Maintenance)
**As an** IT PM,
**I want to** establish a repeatable process to rollback the VM snapshot,
**In order to** bypass the 30-day QuickBooks trial limit without losing the vendor's IP setup.
- **Acceptance Criteria**:
  - [ ] Snapshot rollback process is documented.
  - [ ] Rollback and re-installation take less than 30 minutes.
- **Tasks**:
  1. Take "Golden Image" snapshot of the clean VM.
  2. Create calendar reminder for day 28 of the trial.
  3. Document the steps to reinstall the QB Demo after a rollback.

---

## Epic 2: Stakeholder Management & Unblocking
**Description**: Resolve internal bottlenecks so the vendor can continue their work.
**Estimated Duration**: Sprint 1 (Mar 18, 2026 - Mar 31, 2026)

### US-03: Obtain Accounting Data Validation
**As the** Project Coordinator,
**I want to** get official sign-off on the accounting data accuracy from the internal stakeholder,
**In order to** authorize Dancing Numbers to proceed to the next phase.
- **Acceptance Criteria**:
  - [ ] Written confirmation (Email/Teams) from the stakeholder approving the data.
  - [ ] Vendor confirms they have what they need to proceed.
- **Tasks**:
  1. Execute "Unresponsive Stakeholder" communication plan (See 05-Analysis).
  2. Schedule a 15-minute forced sync-up call.
  3. Escalate to IT Director/Boss if no response in 48 hours.

---

## Epic 3: Vendor Coordination
**Description**: Keep the vendor aligned, track milestones, and manage meetings.
**Estimated Duration**: Ongoing (Starts Sprint 1: Mar 18, 2026 - Mar 31, 2026)

### US-04: Weekly Sync with Dancing Numbers
**As the** Project Coordinator,
**I want to** hold a brief weekly stand-up with the vendor,
**In order to** track progress and log any new blockers.
- **Acceptance Criteria**:
  - [ ] Weekly meeting invites sent.
  - [ ] Brief meeting minutes recorded in Obsidian.
