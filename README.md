# Antigravity Google Sheets PM Suite

> **Transform any Google Sheet into an Executive Agile Sprint & Task Management Hub with a Single Prompt in Google Antigravity.**

Supported Platforms: **Windows**, **macOS**, **Linux**

---

## Highlights

* **Single-Prompt Agile Automation**: Ask Antigravity to create a full sprint board, task tracker with dropdowns, burndown charts, and executive KPI scorecards in any Google Sheet link.
* **Native MCP Integration**: Uses `google-sheets` MCP (`sheetcraft-mcp`) providing 34+ native Google Sheets capabilities: formulas, conditional formatting, cell merging, frozen rows, dropdown data validations, and embedded charts.
* **Zero-Installation Project Mode**: Open this folder in Antigravity on Windows, Mac, or Linux, and the tools are immediately active.
* **1-Click Platform Installers**: Includes `install_windows.bat` for Windows and `install_mac_linux.sh` for macOS/Linux.
* **Pre-Loaded Professional Skills**:
  * `sprint-management`: Sprint planning, backlog grooming, burndown tracking, and velocity analytics.
  * `task-tracker`: Kanban task schemas, priority flows, dropdown data validations, and assignee workload allocation.
  * `sheets-dashboard-architect`: Executive KPI scorecards, dynamic sparkline gauges, and embedded charts.

---

## Directory Structure

```text
antigravity-sheets-pm-suite/
├── .agents/
│   ├── mcp_config.json                 # Automatic Google Sheets MCP declaration
│   ├── rules/
│   │   └── AGENTS.md                   # Behavioral and design rules for Antigravity
│   └── skills/
│       ├── sprint-management/
│       │   └── SKILL.md                # Sprint planning & burndown instructions
│       ├── task-tracker/
│       │   └── SKILL.md                # Task board, dropdown & formatting instructions
│       └── sheets-dashboard-architect/
│           └── SKILL.md                # Executive dashboard & sparkline instructions
├── templates/
│   └── sprint_suite_blueprint.json     # Standard blueprint with sample data & schemas
├── scripts/
│   └── init_pm_suite.py               # Standalone Python CLI / programmatic builder
├── install_windows.bat                 # 1-Click Windows installer & config script
├── install_mac_linux.sh                # 1-Click macOS/Linux installer & config script
├── SETUP_GUIDE.md                      # Detailed OS-by-OS guide from install to edit
├── QUICKSTART.md                       # 2-minute quickstart cheat sheet
└── README.md                           # This file
```

---

## Quickstart (3 Steps)

### 1. Authenticate with Google
Run once in your terminal:
```bash
npx -y sheetcraft-mcp auth login
```
*(Signs in via Google OAuth and caches tokens locally)*

### 2. Open this Project in Antigravity
* **Antigravity Desktop**: Click **Open Folder** and select `antigravity-sheets-pm-suite`.
* **Antigravity CLI**:
  ```bash
  cd antigravity-sheets-pm-suite
  agy
  ```

### 3. Prompt Antigravity
Paste your prompt in the chat:
```text
Connect to my sheet: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
Build our Sprint 12 project management suite:
- Tab 1: "Executive Dashboard" with KPI cards for Total Tasks, Completion %, Delivered Points, and a SPARKLINE bar.
- Tab 2: "Task Tracker" with 10 engineering tasks, dropdown validations for Status and Priority, and soft color conditional formatting.
- Freeze row 1 on all tabs.
```

---

## Skills Reference

| Skill | Trigger / Scope | Primary Capabilities |
| :--- | :--- | :--- |
| **`sprint-management`** | Sprint Planning, Velocity, Burndown | Manages sprint cycles, capacity, committed vs delivered story points, and linear burndown schedules. |
| **`task-tracker`** | Tasks, Kanban, Workflows | Builds task rows, assigns team members, injects dropdown validations, and highlights blockers. |
| **`sheets-dashboard-architect`** | Dashboards, KPIs, Visuals | Builds executive scorecards, dynamic `=SPARKLINE(...)` visual progress bars, and embedded charts. |

---

## Operating Rules for Antigravity

This project enforces strict standards via `.agents/rules/AGENTS.md`:
1. **Never destructive**: Existing user tabs and raw data are never deleted.
2. **Dynamic formulas**: Metrics use `=COUNTIF(...)`, `=SUMIFS(...)`, and `=COUNTA(...)` so calculations stay live when users edit cells in Google Sheets.
3. **Executive aesthetics**: Uses dark navy headers (`#1F4E79`), white bold text, subtle gray gridlines, and soft pastel status fills.

---

## License & Contributing

Built for Google Antigravity & the Model Context Protocol ecosystem. Feel free to extend rules, add customized skills, or customize templates.
