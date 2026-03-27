---
title: Product Backlog - IT Governance & Security
last_update: 2026-03-17
tags: [backlog, security, governance, sharepoint, teams]
---

# Product Backlog - IT Governance & Security

Este backlog centraliza las tareas de auditoría, seguridad y control de acceso del tenant de Casa Familiar.

## Epic 1: Tenant Security & Group Governance
**Description**: Restrict unauthorized creation of groups and audit administrator permissions.
**Sprint**: Sprint 1 (Mar 18, 2026 - Mar 31, 2026)

### US-01: Tenant-Wide Group & Site Creation Restriction
**As an** IT Analyst,
**I want to** restrict the ability to create M365 Groups, SharePoint Sites, and Teams,
**In order to** prevent "Shadow IT" and maintain a clean, organized tenant.
- **Complexity**: High (Critical)
- **Story Points**: 8
- **Acceptance Criteria**:
  - [ ] Entra ID Settings updated to restrict group creation to a specific security group.
  - [ ] SharePoint Online Admin settings updated to disable self-service site creation for users.
  - [ ] Documentation of the new "Provisioning Process" created.
- **Tasks**:
  1. Audit current "M365 Group" ownership.
  2. Configure Entra ID Group Creation Policy.
  3. Run PowerShell script to disable self-service site creation.

### US-02: User Access Audit: Karla Torres
**As an** IT Analyst,
**I want to** review Karla Torres' specific permissions in SharePoint and Teams,
**In order to** confirm if her current role allows for group creation and adjust if necessary.
- **Complexity**: Low
- **Story Points**: 2
- **Acceptance Criteria**:
  - [ ] Report of Karla Torres' site collections and group roles generated.
  - [ ] Permissions adjusted to align with IT security policy.
- **Tasks**:
  1. Run "User Permissions" report in SharePoint Admin Center.
  2. Audit Teams ownership and membership for Karla Torres.
  3. Document and apply necessary modifications.
