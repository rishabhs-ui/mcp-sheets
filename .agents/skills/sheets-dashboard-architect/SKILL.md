---
name: sheets-dashboard-architect
description: Executive KPI Dashboard design, KPI scorecards, dynamic formulas, sparklines, and embedded charts inside Google Sheets via MCP.
---

# Sheets Dashboard Architect Skill

This skill defines instructions for building executive-ready project dashboards in Google Sheets with KPI scorecards, progress bars, and embedded charts.

---

## Layout Architecture

An executive dashboard sheet (`Executive Dashboard`) must be structured into clear visual zones:

```text
+-------------------------------------------------------------------------------+
|  ROW 1-2: DASHBOARD BANNER & SPRINT OBJECTIVE                                |
+-------------------------------------------------------------------------------+
|  ROW 4-7: KPI SCORECARD METRIC CARDS (Total, Completed, Velocity, Blocked)    |
+-------------------------------------------------------------------------------+
|  ROW 9-11: OVERALL SPRINT PROGRESS BAR (SPARKLINE GAUGE)                     |
+-------------------------------------------------------------------------------+
|  ROW 13-25:                                  |  ROW 13-25:                    |
|  STATUS BREAKDOWN TABLE + DONUT/PIE CHART    |  EPIC PROGRESS TABLE + CHART   |
+-------------------------------------------------------------------------------+
|  ROW 27-40: RECENT SPRINT VELOCITY & BURNDOWN TREND (LINE CHART)             |
+-------------------------------------------------------------------------------+
```

---

## 1. Executive KPI Cards (Row 4 to 7)

Build 4 side-by-side KPI cards:

| Card | Label | Formula / Value | Formatting |
| :--- | :--- | :--- | :--- |
| **Card 1** | `Total Tasks` | `=COUNTA('Task Tracker'!A2:A)` | 20pt Bold Navy (`#1F4E79`) |
| **Card 2** | `Sprint Completion` | `=IFERROR(COUNTIF('Task Tracker'!F2:F, "Done")/COUNTA('Task Tracker'!A2:A), 0)` | 20pt Bold Green (`#166534`), Format: `0.0%` |
| **Card 3** | `Delivered Story Points` | `=SUMIFS('Task Tracker'!G2:G, 'Task Tracker'!F2:F, "Done")` | 20pt Bold Blue (`#1E40AF`) |
| **Card 4** | `Active Blockers` | `=COUNTIF('Task Tracker'!F2:F, "Blocked")` | 20pt Bold Red (`#991B1B`) |

---

## 2. Dynamic Progress Sparkline (Row 9)

Add a visual progress gauge:
```sheets
=SPARKLINE(
  IFERROR(COUNTIF('Task Tracker'!F2:F, "Done")/COUNTA('Task Tracker'!A2:A), 0),
  {"charttype", "bar"; "color1", "#10B981"; "max", 1}
)
```

---

## 3. Status Breakdown Aggregation Table (Row 13–20)

| Status | Task Count Formula | Story Points Formula | % of Total |
| :--- | :--- | :--- | :--- |
| `Done` | `=COUNTIF('Task Tracker'!F:F, "Done")` | `=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, "Done")` | `=C14/SUM(C$14:C$19)` |
| `In Progress` | `=COUNTIF('Task Tracker'!F:F, "In Progress")` | `=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, "In Progress")` | `=C15/SUM(C$14:C$19)` |
| `Code Review` | `=COUNTIF('Task Tracker'!F:F, "Code Review")` | `=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, "Code Review")` | `=C16/SUM(C$14:C$19)` |
| `QA` | `=COUNTIF('Task Tracker'!F:F, "QA")` | `=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, "QA")` | `=C17/SUM(C$14:C$19)` |
| `Backlog` | `=COUNTIF('Task Tracker'!F:F, "Backlog")` | `=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, "Backlog")` | `=C18/SUM(C$14:C$19)` |
| `Blocked` | `=COUNTIF('Task Tracker'!F:F, "Blocked")` | `=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, "Blocked")` | `=C19/SUM(C$14:C$19)` |

---

## 4. Embedded Charts via MCP

Call `create_chart`:
1. **Status Distribution**:
   - `chartType: COLUMN` or `PIE`
   - Domain: Column B (Status Name)
   - Series: Column C (Task Count)
2. **Sprint Velocity Trend**:
   - `chartType: LINE`
   - Shows historical story points delivered over last 5 sprints.

---

## Single-Prompt Execution

### Prompt Example:
> *"Create an executive dashboard in tab 'Executive Dashboard' summarizing the tasks from 'Task Tracker' with 4 KPI cards, a sparkline bar, and a status breakdown."*

### Agent Action Steps:
1. Ensure tab `'Executive Dashboard'` exists via `add_sheet`.
2. Format KPI card headers and metric cells using `format_cells`.
3. Inject the dynamic formulas referencing `'Task Tracker'`.
4. Insert the `=SPARKLINE(...)` formula.
5. Create status breakdown summary table.
6. Invoke `create_chart` to embed the status visualization.
