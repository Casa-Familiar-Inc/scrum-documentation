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

---

## Epic 4: Zero Trust UAT Environment Setup
**Description**: Provision and secure the UAT QuickBooks Non-Profit server using Tailscale for shared vendor access and strict firewall rules ensuring AppFolio API only connectivity.
**Estimated Duration**: Sprint 2 (Apr 01, 2026 - Apr 14, 2026)
**Story Points**: 13

### US-05: Configure Tailscale Zero Trust Access
**As an** IT Analyst,
**I want to** configure Tailscale on the UAT server and invite the vendor,
**In order to** provide secure, isolated RDP access without opening firewall ports.
- **Story Points**: 5
- **Priority**: High
- **Acceptance Criteria**:
  - [ ] Tailscale free version is installed and registered to Casa Familiar.
  - [ ] Vendor's email is invited explicitly to the UAT machine node.
  - [ ] Vendor can successfully RDP into the shared local account over the Tailscale IP.
  - [ ] Key expiry is disabled to prevent sudden disconnections during testing.
- **Tasks**:
  1. Set up the Tailscale admin account and install the client on the VM.
  2. Create a standard local Windows user `UAT-Vendor` for RDP.
  3. Invite the vendor via Tailscale sharing and test connectivity using a personal hotspot.

### US-06: Restrict Outbound Internet Traffic
**As an** IT Analyst,
**I want to** block general internet browsing while allowing outbound connections to the AppFolio Reports API,
**In order to** comply with security policies and prevent unauthorized data exfiltration.
- **Story Points**: 5
- **Priority**: High
- **Acceptance Criteria**:
  - [ ] Web browsers (Edge/Chrome) cannot load general sites (e.g., Google, Outlook).
  - [ ] PowerShell or Postman can successfully reach the AppFolio Reports API endpoint.
  - [ ] Tailscale daemon can communicate with its coordination servers.
- **Tasks**:
  1. Identify AppFolio API IP addresses/FQDNs required.
  2. Configure Simplewall default-deny rules and whitelist critical executables.
  3. Verify Tailscale connectivity is unaffected by the outbound block.

### US-07: Deploy QuickBooks Desktop Non-Profit
**As an** IT Analyst,
**I want to** install QuickBooks Desktop Non-Profit and connect it to the AppFolio API,
**In order to** prepare the application layer for vendor data validation.
- **Story Points**: 3
- **Priority**: Medium
- **Acceptance Criteria**:
  - [ ] QuickBooks Desktop Non-Profit is installed and licensed/trial-activated.
  - [ ] Low-code batch script is added to startup to initialize Tailscale and QB automatically.
- **Tasks**:
  1. Install QuickBooks using Casa Familiar provided media.
  2. Place the startup `.bat` script in the shared user's Startup folder.
  3. Perform a test run logged in as the `UAT-Vendor` account.
