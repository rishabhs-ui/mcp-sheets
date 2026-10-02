---
name: task-tracker
description: Real-time Task Management, Kanban-style workflows, Dropdown Data Validations, and Assignee Workload allocation in Google Sheets via MCP.
---

# Task Tracker Skill

This skill defines rules and procedures for building and operating responsive, interactive task management boards in Google Sheets.

---

## Capabilities

1. **Task Board Generation**: Build structured task lists with IDs, descriptions, epics, priorities, assignees, dates, and blockers.
2. **Data Validation Dropdowns**: Inject native Google Sheets dropdown menus into Status and Priority columns.
3. **Automated Status Highlighting**: Apply multi-rule conditional formatting (Done, In Progress, Blocked, Review).
4. **Assignee Capacity & Workload Rollup**: Calculate real-time task count and story points per developer.

---

## Standard Schema (`Task Tracker`)

| Col | Header | Format / Validation | Description |
| :--- | :--- | :--- | :--- |
| **A** | `Task ID` | Plain text (`TSK-101`) | Unique task identifier |
| **B** | `Title / Summary` | Plain text | Short actionable task description |
| **C** | `Epic / Feature` | Plain text | Functional category (e.g. `Auth`, `Billing`) |
| **D** | `Assignee` | Plain text | Responsible team member |
| **E** | `Priority` | Dropdown: `P0 - Blocker`, `P1 - High`, `P2 - Medium`, `P3 - Low` | Urgency tier |
| **F** | `Status` | Dropdown: `Backlog`, `In Progress`, `Code Review`, `QA`, `Done`, `Blocked` | Current workflow state |
| **G** | `Story Points` | Number (1, 2, 3, 5, 8, 13) | Effort estimate |
| **H** | `Hours Spent` | Number | Logged engineering time |
| **I** | `Due Date` | Date (`YYYY-MM-DD`) | Target delivery date |
| **J** | `Blocker Notes` | Plain text | Dependency or impediment detail |

---

## Data Validation Injection (`set_data_validation`)

When creating the table, invoke `set_data_validation` on column ranges:

1. **Status Dropdown (Column F: Rows 2 to 500)**:
   - Type: `ONE_OF_LIST`
   - Values: `["Backlog", "In Progress", "Code Review", "QA", "Done", "Blocked"]`
   - Show dropdown arrow: `true`

2. **Priority Dropdown (Column E: Rows 2 to 500)**:
   - Type: `ONE_OF_LIST`
   - Values: `["P0 - Blocker", "P1 - High", "P2 - Medium", "P3 - Low"]`
   - Show dropdown arrow: `true`

---

## Assignee Workload Summary Block

Include a workload summary table on the right side (e.g., Columns L to P):
- **Assignee Name**
- **Assigned Tasks**: `=COUNTIF(D2:D, L2)`
- **Total Points**: `=SUMIFS(G2:G, D2:D, L2)`
- **Done Points**: `=SUMIFS(G2:G, D2:D, L2, F2:F, "Done")`
- **Workload Sparkline**: `=SPARKLINE(N2, {"charttype", "bar"; "color1", "#4285F4"; "max", 20})`

---

## Single-Prompt Workflows

### Prompt Example:
> *"Add a Task Tracker tab to my sheet: <URL> with dropdowns for Status and Priority, assign 8 frontend tasks to Alex and Maria, and highlight blockers in red."*

### Agent Action Steps:
1. `resolve_target` on the spreadsheet URL.
2. `add_sheet` with title `"Task Tracker"`.
3. Set column headers with navy fill and bold white text.
4. Populate tasks with formulas and initial values.
5. Call `set_data_validation` for columns E and F.
6. Apply `conditional_format` for `Blocked` (soft red) and `Done` (soft green).
7. Call `freeze_rows_columns` to freeze Row 1.
