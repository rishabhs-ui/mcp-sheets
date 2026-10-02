# Complete Setup & Installation Guide: Antigravity Google Sheets PM Suite

This guide walks you through every step to go from a clean machine to editing and building full Google Sheets Agile dashboards, sprint boards, and task trackers using **Google Antigravity** on **Linux**, **Windows**, or **macOS**.

---

## Table of Contents
1. [Prerequisites](#1-prerequisites)
2. [Step 1: Install Google Antigravity](#step-1-install-google-antigravity)
   - [Windows Installation](#windows-installation)
   - [macOS Installation](#macos-installation)
   - [Linux Installation](#linux-installation)
3. [Step 2: Install Node.js & npx](#step-2-install-nodejs--npx)
4. [Step 3: Authenticate Google Sheets](#step-3-authenticate-google-sheets)
5. [Step 4: Configure the Google Sheets MCP](#step-4-configure-the-google-sheets-mcp)
6. [Step 5: Launch Antigravity & Open the Project](#step-5-launch-antigravity--open-the-project)
7. [From Install to Editing Google Sheets on a Single Prompt](#from-install-to-editing-google-sheets-on-a-single-prompt)
   - [Prompt 1: Full Sprint Board + Task Tracker + Dashboard](#prompt-1-full-sprint-board--task-tracker--dashboard)
   - [Prompt 2: Real-time Task Updates & Blocker Logging](#prompt-2-real-time-task-updates--blocker-logging)
   - [Prompt 3: Custom KPI Dashboard & Burndown Chart](#prompt-3-custom-kpi-dashboard--burndown-chart)
8. [Troubleshooting & FAQ](#troubleshooting--faq)

---

## 1. Prerequisites

Before starting, ensure you have:
* A Google Account (to view and edit Google Sheets).
* A web browser (for Google OAuth authorization).
* Terminal / Command Prompt access.

---

## Step 1: Install Google Antigravity

Antigravity comes in two surfaces: **Antigravity Desktop 2.0** (standalone visual application) and **Antigravity CLI (`agy`)** (terminal-based agent). You can use either or both.

### Windows Installation

#### Method A: Antigravity Desktop 2.0 (GUI)
1. Download the Antigravity Windows installer (`Antigravity-Setup.exe`) from the official release page or your organization's portal:
   ```text
   https://antigravity.google
   ```
2. Double-click `Antigravity-Setup.exe` and follow the setup wizard.
3. Launch **Antigravity** from your Windows Start Menu.

#### Method B: Antigravity CLI (`agy`) via Terminal
Open **PowerShell** or **Windows Terminal** (run as Administrator if installing globally):
```powershell
npm install -g @google/antigravity-cli
```
Verify installation:
```powershell
agy --version
```

---

### macOS Installation

#### Method A: Antigravity Desktop 2.0 (GUI)
1. Download `Antigravity.dmg` from:
   ```text
   https://antigravity.google
   ```
2. Open `Antigravity.dmg` and drag **Antigravity** into your `Applications` folder.
3. Open Antigravity from Spotlight or Applications.

#### Method B: Antigravity CLI via Homebrew / npm
Open Terminal:
```bash
# Using npm
npm install -g @google/antigravity-cli

# Or using Homebrew (if formula is added)
brew install antigravity
```
Verify installation:
```bash
agy --version
```

---

### Linux Installation (Ubuntu, Debian, Fedora, Arch)

#### Method A: Antigravity CLI (`agy`)
Open Terminal:
```bash
# Ubuntu / Debian
sudo apt update && sudo apt install -y curl nodejs npm
sudo npm install -g @google/antigravity-cli

# Fedora / RHEL
sudo dnf install -y nodejs npm
sudo npm install -g @google/antigravity-cli

# Arch Linux
sudo pacman -S nodejs npm
sudo npm install -g @google/antigravity-cli
```
Verify installation:
```bash
agy --version
```

#### Method B: Antigravity Desktop (AppImage / .deb)
1. Download `Antigravity.AppImage` or `Antigravity.deb`.
2. For AppImage:
   ```bash
   chmod +x Antigravity.AppImage
   ./Antigravity.AppImage
   ```
3. For `.deb`:
   ```bash
   sudo dpkg -i Antigravity.deb
   ```

---

## Step 2: Install Node.js & npx

The `google-sheets` MCP server runs via `sheetcraft-mcp` (using `npx`), which requires Node.js.

* **Windows**: Download the Node.js LTS MSI installer from [https://nodejs.org/](https://nodejs.org/) and run it. Check the box to "Automatically install necessary tools".
* **macOS**: `brew install node`
* **Linux**: `sudo apt install -y nodejs npm`

Verify in your terminal:
```bash
node -v
npx -v
```

---

## Step 3: Authenticate Google Sheets

Authentication takes less than 30 seconds using the built-in OAuth flow:

1. Open your terminal or Command Prompt.
2. Run the authentication command:
   ```bash
   npx -y sheetcraft-mcp auth login
   ```
3. A browser window will automatically open asking you to sign in with your Google account.
4. Select your account and grant Google Sheets access (`https://www.googleapis.com/auth/spreadsheets`).
5. Upon authorization, you will see:
   ```text
   Authentication successful! Tokens stored at ~/.config/sheetcraft-mcp/oauth-tokens.json
   ```

*(On Windows, tokens are stored at `%USERPROFILE%\.config\sheetcraft-mcp\oauth-tokens.json`)*.

---

## Step 4: Configure the Google Sheets MCP

You can configure the MCP either **Per-Project** (Zero-Installation) or **Globally**.

### Option A: Per-Project (Zero-Installation - Included in this repository!)
This project already contains `.agents/mcp_config.json`:
```json
{
  "mcpServers": {
    "google-sheets": {
      "command": "npx",
      "args": ["-y", "sheetcraft-mcp"],
      "env": {
        "SHEETS_TOOLSETS": "all"
      }
    }
  }
}
```
Whenever you open this project folder in Antigravity, the Google Sheets tools are **automatically discovered and activated**.

### Option B: 1-Click Automated Installer

* **On Windows**: Double-click `install_windows.bat`.
* **On macOS/Linux**: Run `./install_mac_linux.sh` in your terminal.

The script automatically registers `google-sheets` in Antigravity's global configuration (`~/.gemini/config/mcp_config.json`).

---

## Step 5: Launch Antigravity & Open the Project

### Using Antigravity Desktop:
1. Open the **Antigravity** desktop app.
2. Click **Open Folder / Project** in the left sidebar.
3. Select this repository folder (`antigravity-sheets-pm-suite`).
4. In the chat canvas, the agent is now equipped with all Google Sheets tools and Sprint skills!

### Using Antigravity CLI:
1. Open your terminal inside this project folder:
   ```bash
   cd antigravity-sheets-pm-suite
   agy
   ```
2. Antigravity will start with the project context loaded.

---

## From Install to Editing Google Sheets on a Single Prompt

Now, you can edit, format, build formulas, and generate complete dashboards in **any Google Sheet URL using a single plain English prompt**.

Here are real-world prompt examples:

### Prompt 1: Full Sprint Board + Task Tracker + Dashboard

Copy and paste this single prompt into Antigravity (replace with your Google Sheet URL):

```text
Connect to my Google Sheet: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
Set up a complete Agile Sprint 10 management suite for our engineering team:
1. An "Executive Dashboard" tab with 4 KPI cards (Total Tasks, Completion Rate %, Delivered Points, Blockers), a live SPARKLINE progress bar, and status breakdown.
2. A "Task Tracker" tab with 10 engineering tasks distributed across Alex, Maria, and Dev, with dropdown validations for Status (Done, In Progress, Review, Blocked) and Priority (P0, P1, P2, P3).
3. Apply conditional formatting so "Done" is green, "Blocked" is red, and "In Progress" is blue.
4. Freeze the header row on all tabs.
```

**What Antigravity does automatically:**
1. Resolves the spreadsheet ID and inspects sheet structure.
2. Calls `add_sheet` to create the required tabs.
3. Populates headers and sample tasks with formulas (`COUNTIF`, `SUMIFS`, `SPARKLINE`).
4. Injects dropdown data validations using `set_data_validation`.
5. Applies color fills using `conditional_format`.
6. Freezes row 1 using `freeze_rows_columns`.
7. Responds with the completed sheet URL and an executive summary.

---

### Prompt 2: Real-time Task Updates & Blocker Logging

```text
In my sheet: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
Update task TSK-103 to "Blocked" with note "Waiting on production AWS credentials from DevOps", and mark task TSK-101 as "Done". Check how this impacts our Sprint Completion % on the Executive Dashboard.
```

**What Antigravity does automatically:**
1. Searches the `Task Tracker` for `TSK-103` and `TSK-101`.
2. Updates cell values cleanly.
3. Reads the updated KPI metric from the `Executive Dashboard` and reports the new completion percentage back to you!

---

### Prompt 3: Custom KPI Dashboard & Burndown Chart

```text
In my sheet: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
Add a "Sprint Burndown" tab for a 10-day sprint starting Oct 5 with 50 committed story points. Include daily ideal vs actual remaining points and embed a native line chart visualizing the burndown trajectory.
```

---

## Troubleshooting & FAQ

#### Q: I get `OAuth token not found` or `Authentication failed`.
* **Fix**: Run `npx -y sheetcraft-mcp auth login` in your terminal. Ensure your default browser is signed into the Google account that has permission to access the target spreadsheet.

#### Q: On Windows, I get `'npx' is not recognized as an internal or external command`.
* **Fix**: Install Node.js LTS from [nodejs.org](https://nodejs.org/). Make sure you restart your terminal after installing.

#### Q: How do I share this with a colleague who doesn't code?
1. Send them this project folder (or ZIP).
2. Tell them to double-click `install_windows.bat`.
3. Open Antigravity and paste their Google Sheet link with instructions.

#### Q: Does this overwrite my existing sheets?
* **No**. The agent's rules (`AGENTS.md`) strictly mandate non-destructive operations: existing tabs are left untouched unless you explicitly instruct the agent to update them.
