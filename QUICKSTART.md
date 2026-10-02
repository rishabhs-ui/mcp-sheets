# ⚡ Quickstart Cheat Sheet: Antigravity Google Sheets PM Suite

Get from zero to editing Google Sheets with Antigravity in **2 minutes**.

---

## 1. Fast Setup

### On Windows
1. Double-click `install_windows.bat`.
2. Follow the browser prompt to log into your Google Account.
3. Open this folder in Antigravity.

### On macOS / Linux
```bash
./install_mac_linux.sh
```

---

## 2. Test Commands / Prompts

Open Antigravity and copy-paste any of these single prompts:

### Example A: Build Entire Sprint & Task Suite
```text
In my sheet: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
Build a Sprint 10 PM hub:
1. Executive Dashboard tab with 4 KPI scorecards, a live SPARKLINE progress bar, and status breakdown.
2. Task Tracker tab with 8 tasks across Auth and Billing epics, dropdowns for Status & Priority, and soft green/red conditional formatting.
```

### Example B: Add & Assign New Tasks
```text
In my sheet: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
Add 3 new P1 tasks for Maria Chen in Task Tracker:
- "Design Stripe Webhook Retry Logic" (5 SP)
- "Audit JWT Token Expiry Edge Cases" (3 SP)
- "Write E2E Cypress Checkout Tests" (5 SP)
```

### Example C: Mark Blocker & Alert Team
```text
In my sheet: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
Mark task TSK-103 as "Blocked" with note "Awaiting staging Redis credentials from DevOps". Update the dashboard and tell me the current blocker count.
```

### Example D: Daily Standup Summary
```text
Read the current state of my sheet: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
Give me an executive daily standup summary:
- How many tasks are Done vs In Progress vs Blocked?
- Who has the highest story point load?
- Are we on track for our sprint deadline?
```

---

## 3. Key Files in this Project

* **`.agents/rules/AGENTS.md`**: Directs the agent to format sheets with executive navy styling, proper formulas, and non-destructive updates.
* **`.agents/skills/sprint-management/SKILL.md`**: Sprint planning & burndown tracker procedures.
* **`.agents/skills/task-tracker/SKILL.md`**: Kanban workflows, priority levels, and dropdown injection.
* **`.agents/skills/sheets-dashboard-architect/SKILL.md`**: Executive KPI cards and dynamic formula construction.
* **`templates/sprint_suite_blueprint.json`**: Pre-configured JSON data blueprint.
