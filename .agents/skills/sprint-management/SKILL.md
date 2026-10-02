---
name: sprint-management
description: Automated Agile Sprint Planning, Sprint Backlog Setup, Burndown Tracker, and Velocity Analytics inside Google Sheets via MCP.
---

# Sprint Management Skill

This skill provides step-by-step procedures for initializing, planning, and managing Agile sprints in Google Sheets using the `google-sheets` MCP server.

---

## Capabilities

1. **Sprint Initialization**: Setup a new sprint cycle with duration, start/end dates, team capacity, and committed story points.
2. **Sprint Backlog Architecture**: Structure user stories, story points (Fibonacci), acceptance criteria, and sprint goals.
3. **Burndown & Burnup Tracking**: Create daily burndown schedules tracking remaining story points vs ideal burndown trajectory.
4. **Velocity Analysis**: Track sprint-over-sprint completion velocity (committed vs delivered story points).

---

## Standard Sheet Layout: `Sprint Overview`

When building or updating a `Sprint Overview` sheet:

### 1. Sprint Meta Header (Rows 1–5)
- **Cell A1:F1** (Merged): Sprint Title (e.g., `Sprint 24: Core Platform & Payment Gateway Integration`)
- **Key Metrics Table (Row 3–5)**:
  - `Sprint Status`: Active / Planning / Completed
  - `Sprint Start Date`: e.g., `2026-10-05`
  - `Sprint End Date`: e.g., `2026-10-16` (2 Weeks / 10 Working Days)
  - `Team Capacity (SP)`: Total available story points
  - `Committed (SP)`: `=SUM('Task Tracker'!G2:G)`
  - `Completed (SP)`: `=SUMIFS('Task Tracker'!G2:G, 'Task Tracker'!F2:F, "Done")`
  - `Sprint Health`: `=IF(G4>=0.8*E4, "🟢 On Track", IF(G4>=0.5*E4, "🟡 At Risk", "🔴 Delayed"))`

### 2. Burndown Schedule Table (Columns H to M)
Columns:
- `Day #` (Day 1, Day 2, ..., Day 10)
- `Date` (Working days excluding weekends)
- `Ideal Remaining (SP)`: Linear reduction formula `=Capacity - (Capacity/10 * (Day - 1))`
- `Actual Remaining (SP)`: Actual remaining points at the end of each day
- `Variance`: `=Actual - Ideal`

### 3. Native Burndown Line Chart
Call `create_chart` with:
- `chartType: LINE`
- Domain: `Date` column
- Series 1: `Ideal Remaining` (Dashed gray line)
- Series 2: `Actual Remaining` (Solid blue line)

---

## Standard Single-Prompt Workflows

### Prompt Example:
> *"Create Sprint 14 for our mobile app team starting next Monday for 2 weeks in sheet <URL>. Team capacity is 65 story points. Commit 12 user stories across Authentication and Checkout epics."*

### Agent Action Steps:
1. `resolve_target` with the provided spreadsheet URL.
2. `add_sheet` with title `"Sprint 14 Overview"`.
3. `batch_update_values` writing the metadata table and burndown columns.
4. Populate `"Task Tracker"` with 12 distributed user stories tagged with Epics and Story Points.
5. Create a burndown line chart linked to the burndown table.
6. Apply professional navy & white styling via `format_cells`.
