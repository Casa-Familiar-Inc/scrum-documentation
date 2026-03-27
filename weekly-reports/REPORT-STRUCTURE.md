# IT Weekly Activity Report — Structure Guide

## File Naming Convention

```
YYYY-MM-DD-Weekly-Activity-Report.md
```

Example: `2026-03-18-Weekly-Activity-Report.md`

---

## Report Sections

### 1. YAML Frontmatter (between `---`)

Required fields:

| Field          | Description                      | Example                     |
| :------------- | :------------------------------- | :-------------------------- |
| `title`        | Fixed report title               | `IT Weekly Activity Report` |
| `it_analyst`   | IT analyst name                  | `Nefi Lopez`                |
| `it_director`  | IT director name                 | `Benjamin Gonzalez`         |
| `week_covered` | Date range of the week           | `03/11/26 - 03/18/26`      |
| `tags`         | Tags for organization            | `[weekly-report, it-operations, sprint-1]` |

### 2. Header (H1 + metadata)

Replicate the frontmatter data in readable format:

```
**Name**: Nefi Lopez / Benjamin Gonzalez
**Title**: IT Analyst / IT Director
**Department**: IT
**Week Covered**: MM/DD/YY - MM/DD/YY
**Date**: MM/DD/YY
```

### 3. Currently Working On / New Tasks

**Format**: Table with 5 columns

| Column        | Description                                      |
| :------------ | :----------------------------------------------- |
| `Task`        | Task name in **bold**                            |
| `Status`      | Current status (short descriptive phrase)        |
| `Next Steps`  | What needs to be done next                       |
| `Lead`        | Who is executing (typically `Nefi`)              |
| `Stakeholder` | Involved department (`IT`, `HR`, `FOC`, etc.)    |

### 4. Completed This Week

**Format**: Table with 4 columns

| Column        | Description                                      |
| :------------ | :----------------------------------------------- |
| `Task`        | Completed task name in **bold**                  |
| `Outcome`     | Result or description of the deliverable         |
| `Lead`        | Who executed it                                  |
| `Stakeholder` | Benefiting department                            |

### 5. Ongoing Activities and Projects

**Format**: Bullet list (`-`)

Each item contains the project/process name in **bold** followed by a brief description of the current state.

```markdown
- **Project X**: Current status and next steps.
- **Project Y**: Continues in phase of ...
```

### 6. Pending / Blocked

**Format**: Checkbox list (`- [ ]`)

Each item describes what is pending or blocked.

```markdown
- [ ] **Task A**: Reason it is pending.
- [ ] **Task B**: Blocked waiting for approval from ...
```

### 7. Notes & Observations

**Format**: Obsidian callouts with `> [!NOTE]`

Each note groups relevant information for the week. The callout title goes after the tag.

```markdown
> [!NOTE] Topic Title
> Note content. Can be multiline by continuing with `>` on each line.
```

Also supports `[!WARNING]`, `[!IMPORTANT]`, `[!CAUTION]`, `[!TIP]`.

---

## Exporting to Word via Obsidian

1. Open the `.md` file in Obsidian
2. Right-click the file in the file explorer
3. Select **Export to PDF** or use the **Pandoc** plugin for Word export
4. Alternatively, use `Ctrl+P` (Command Palette) → search for **"Export"** or **"Pandoc: Export as docx"**

### Recommended Obsidian Plugins for Word Export

- **Pandoc Plugin** — Converts `.md` to `.docx` directly
- **Enhanced Export** — Additional export format options

---

## Weekly Workflow

1. Copy the template `weekly-report-template.md`
2. Rename to `YYYY-MM-DD-Weekly-Activity-Report.md`
3. Update frontmatter and metadata (dates, names)
4. Fill in each section with the week's information
5. Export to Word via Obsidian
