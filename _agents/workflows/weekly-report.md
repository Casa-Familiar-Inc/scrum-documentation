---
description: How to fill out the IT Weekly Activity Report
---

# IT Weekly Activity Report — Workflow Rule

## Report Location

All weekly reports are saved in: `c:\Dev\Scrum\weekly-reports\`
Filename format: `YYYY-MM-DD-Weekly-Activity-Report.md`
The date in the filename corresponds to the **last day of the week covered**.

---

## Status Column Rule

The **Status** column is a **short description of what is currently happening**, not a fixed label.
Write it as a brief active phrase that describes the actual state of the task this week.

Never use generic labels like `In Progress`, `Ongoing`, or `Attended`.

| Example Task                          | Correct Status                          |
| :------------------------------------ | :-------------------------------------- |
| SharePoint Events Portal: Site Config | Configuring fields and lists            |
| SharePoint Events Portal: JSON Template | Building and validating JSON template |
| Salesforce: User Support              | Monitoring user; no new issues to date  |
| Gladys: TimeOff Calendar Permissions  | Waiting for user confirmation           |
| CFIT ticket cancelled by user         | Closed — no action required             |
| Meeting Rooms: approvals received     | Approval messages received              |

> Meetings and syncs (e.g., Salesforce Weekly Meeting) are **not tasks** and should not appear in the "Currently Working On" table. They belong in the **Completed This Week** table as one-time events.

---

## Section Rules

### "Currently Working On / New Tasks"

- Only list tasks that are **actively in flight** this week (status: `In Progress` or `Waiting`).
- The **Status** column reflects what is happening **right now**, not historical state.
- The **Next Steps** column reflects what will be done **next**, not what was done.
- Remove a task from this table as soon as it is completed or closed.

### "Completed This Week"

- Move tasks here when they are fully done or officially closed.
- Include one-time activities like meetings if they are noteworthy.
- For closed tickets (e.g., user cancelled), include the reason in the Outcome column.

### "Ongoing Activities and Projects"

- Use this section for **narrative context** on tasks still in progress.
- Write in full sentences. This section is read by IT Director Benjamin Gonzalez.
- Do not duplicate every row from "Currently Working On." Focus on meaningful updates or context.

### "Pending / Blocked"

- Use checkbox format: `- [ ] **Task Name**: Brief description of what is blocked or next.`
- List only tasks where something external is needed before work can continue.
- Remove an item when the blocker is resolved, even if the task is still in progress.

### "Notes & Observations"

- Use `> [!NOTE]` callouts for each item.
- One note per notable task or topic.
- Keep notes factual and concise. This section provides context for leadership review.

---

## Weekly Checklist

When filling out or updating the weekly report, go through the following steps:

1. Update `week_covered` and `date` in the frontmatter and the header section.
2. Review each task in "Currently Working On":
   - Is it still actively being worked on? → Keep as `In Progress`.
   - Is it blocked on someone else? → Change to `Waiting`.
   - Is it done or closed? → Remove from this table and add to "Completed This Week".
3. Add any new tasks started this week to "Currently Working On".
4. Add completed or closed items to the "Completed This Week" table with a clear Outcome.
5. Update the "Ongoing Activities and Projects" narrative section.
6. Update "Pending / Blocked" — remove resolved items, add new blockers.
7. Update or add Notes in the "Notes & Observations" section for each significant task.
8. All content must be written in **English**.

---

## Example Status Transitions

```
Task starts this week         → Add to "Currently Working On" as In Progress
Task blocked on user response → Change status to Waiting
Task completed                → Move to "Completed This Week", remove from active table
Ticket cancelled by user      → Move to "Completed This Week" with Closed outcome, add Note
Meeting attended              → Add directly to "Completed This Week" (not in active table)
```
