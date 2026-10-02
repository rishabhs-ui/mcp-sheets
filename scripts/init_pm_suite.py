#!/usr/bin/env python3
"""
Agile Sprint & Task Management Suite Initializer for Google Sheets
Can be invoked directly via CLI or called programmatically by Antigravity tools.
"""

import os
import sys
import json
import requests
import argparse

BLUEPRINT_PATH = os.path.join(os.path.dirname(__file__), "..", "templates", "sprint_suite_blueprint.json")

def get_token():
    # 1. Check environment variable
    if os.environ.get("GOOGLE_SHEETS_ACCESS_TOKEN"):
        return os.environ.get("GOOGLE_SHEETS_ACCESS_TOKEN")
    
    # 2. Check standard sheetcraft-mcp tokens
    home = os.path.expanduser("~")
    token_path = os.path.join(home, ".config", "sheetcraft-mcp", "oauth-tokens.json")
    if os.path.exists(token_path):
        try:
            with open(token_path) as f:
                data = json.load(f)
                return data.get("access_token")
        except Exception as e:
            print(f"Warning: Failed to read {token_path}: {e}")
            
    print("Error: No Google Sheets OAuth token found.")
    print("Run: npx -y sheetcraft-mcp auth login")
    print("Or set: export GOOGLE_SHEETS_ACCESS_TOKEN='<your-token>'")
    sys.exit(1)

def build_sheets_suite(spreadsheet_id, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    with open(BLUEPRINT_PATH) as f:
        blueprint = json.load(f)
        
    print(f"Connecting to Google Sheet: {spreadsheet_id}...")
    meta_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}"
    resp = requests.get(meta_url, headers=headers)
    if resp.status_code != 200:
        print(f"Error accessing spreadsheet: {resp.status_code} {resp.text}")
        sys.exit(1)
        
    sheet_meta = resp.json()
    existing_sheets = {s['properties']['title']: s['properties']['sheetId'] for s in sheet_meta.get('sheets', [])}
    print(f"Found existing sheets: {list(existing_sheets.keys())}")
    
    # Create missing sheets
    reqs = []
    for sheet_def in blueprint['sheets']:
        stitle = sheet_def['title']
        if stitle not in existing_sheets:
            print(f"Adding new sheet: '{stitle}'")
            reqs.append({
                "addSheet": {
                    "properties": {
                        "title": stitle,
                        "gridProperties": sheet_def.get("grid_properties", {"rowCount": 100, "columnCount": 20})
                    }
                }
            })
            
    if reqs:
        batch_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}:batchUpdate"
        bresp = requests.post(batch_url, headers=headers, json={"requests": reqs})
        if bresp.status_code == 200:
            for reply in bresp.json().get('replies', []):
                added_props = reply.get('addSheet', {}).get('properties', {})
                existing_sheets[added_props.get('title')] = added_props.get('sheetId')
                
    # Populate Task Tracker
    tt_def = next(s for s in blueprint['sheets'] if s['title'] == 'Task Tracker')
    values_data = [tt_def['headers']] + tt_def['sample_rows']
    update_vals_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/'Task Tracker'!A1?valueInputOption=USER_ENTERED"
    requests.put(update_vals_url, headers=headers, json={"range": "'Task Tracker'!A1", "values": values_data})
    print("Populated 'Task Tracker' with headers and sample tasks.")

    # Populate Executive Dashboard
    ed_def = next(s for s in blueprint['sheets'] if s['title'] == 'Executive Dashboard')
    dash_rows = [
        ["AGILE SPRINT & TASK MANAGEMENT: EXECUTIVE DASHBOARD", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "TOTAL SPRINT TASKS", "", "", "SPRINT COMPLETION", "", "", "DELIVERED POINTS", "", "", "ACTIVE BLOCKERS", ""],
        ["", "=COUNTA('Task Tracker'!A2:A)", "", "", "=IFERROR(COUNTIF('Task Tracker'!F2:F, \"Done\")/COUNTA('Task Tracker'!A2:A), 0)", "", "", "=SUMIFS('Task Tracker'!G2:G, 'Task Tracker'!F2:F, \"Done\")", "", "", "=COUNTIF('Task Tracker'!F2:F, \"Blocked\")", ""],
        ["", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "SPRINT PROGRESS GAUGE", "", "", "", "", "", "", "", "", "", ""],
        ["", "=SPARKLINE(IFERROR(COUNTIF('Task Tracker'!F2:F, \"Done\")/COUNTA('Task Tracker'!A2:A), 0), {\"charttype\", \"bar\"; \"color1\", \"#10B981\"; \"max\", 1})", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "STATUS BREAKDOWN", "TASKS", "STORY POINTS", "% OF TOTAL", "", "PRIORITY BREAKDOWN", "TASKS", "", "", "", ""],
        ["", "Done", "=COUNTIF('Task Tracker'!F:F, \"Done\")", "=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, \"Done\")", "=IFERROR(C10/SUM(C$10:C$15), 0)", "", "P0 - Blocker", "=COUNTIF('Task Tracker'!E:E, \"P0 - Blocker\")", "", "", "", ""],
        ["", "In Progress", "=COUNTIF('Task Tracker'!F:F, \"In Progress\")", "=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, \"In Progress\")", "=IFERROR(C11/SUM(C$10:C$15), 0)", "", "P1 - High", "=COUNTIF('Task Tracker'!E:E, \"P1 - High\")", "", "", "", ""],
        ["", "Code Review", "=COUNTIF('Task Tracker'!F:F, \"Code Review\")", "=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, \"Code Review\")", "=IFERROR(C12/SUM(C$10:C$15), 0)", "", "P2 - Medium", "=COUNTIF('Task Tracker'!E:E, \"P2 - Medium\")", "", "", "", ""],
        ["", "QA", "=COUNTIF('Task Tracker'!F:F, \"QA\")", "=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, \"QA\")", "=IFERROR(C13/SUM(C$10:C$15), 0)", "", "P3 - Low", "=COUNTIF('Task Tracker'!E:E, \"P3 - Low\")", "", "", "", ""],
        ["", "Backlog", "=COUNTIF('Task Tracker'!F:F, \"Backlog\")", "=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, \"Backlog\")", "=IFERROR(C14/SUM(C$10:C$15), 0)", "", "", "", "", "", "", ""],
        ["", "Blocked", "=COUNTIF('Task Tracker'!F:F, \"Blocked\")", "=SUMIFS('Task Tracker'!G:G, 'Task Tracker'!F:F, \"Blocked\")", "=IFERROR(C15/SUM(C$10:C$15), 0)", "", "", "", "", "", "", ""]
    ]
    dash_url = f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/'Executive Dashboard'!A1?valueInputOption=USER_ENTERED"
    requests.put(dash_url, headers=headers, json={"range": "'Executive Dashboard'!A1", "values": dash_rows})
    print("Populated 'Executive Dashboard' with KPI scorecards, sparklines, and status matrices.")

    print("\n[SUCCESS] Project Management & Sprint Suite built successfully in Google Sheets!")
    print(f"Spreadsheet URL: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")

def main():
    parser = argparse.ArgumentParser(description="Initialize Google Sheets Sprint & Project Suite")
    parser.add_argument("spreadsheet_id", help="Google Sheet ID or Full URL")
    args = parser.parse_args()

    sid = args.spreadsheet_id
    if "/d/" in sid:
        sid = sid.split("/d/")[1].split("/")[0]

    token = get_token()
    build_sheets_suite(sid, token)

if __name__ == "__main__":
    main()
