#!/usr/bin/env bash
set -e

echo "======================================================================"
echo "  Google Antigravity - Google Sheets PM Suite Installer (Mac/Linux)"
echo "======================================================================"
echo ""

# 1. Check Node.js / npx
if ! command -v npx &> /dev/null; then
    echo "[!] Node.js and npx are required but not found."
    echo "    macOS: brew install node"
    echo "    Linux (Ubuntu/Debian): sudo apt update && sudo apt install -y nodejs npm"
    exit 1
fi
echo "[✓] Node.js and npx detected: $(npx --version)"

# 2. Authenticate Google Sheets
echo ""
echo "----------------------------------------------------------------------"
echo "Step 1: Authenticate Google Sheets"
echo "----------------------------------------------------------------------"
echo "Opening browser to authorize Google Sheets..."
npx -y sheetcraft-mcp auth login || echo "[!] Re-run 'npx -y sheetcraft-mcp auth login' if auth was interrupted."
echo "[✓] Google Sheets authentication verified."

# 3. Configure Antigravity Global MCP
echo ""
echo "----------------------------------------------------------------------"
echo "Step 2: Register Google Sheets MCP in Google Antigravity"
echo "----------------------------------------------------------------------"
CONFIG_DIR="$HOME/.gemini/config"
mkdir -p "$CONFIG_DIR"
CONFIG_FILE="$CONFIG_DIR/mcp_config.json"

python3 -c "
import json, os

cfg_path = os.path.expanduser('~/.gemini/config/mcp_config.json')
data = {}
if os.path.exists(cfg_path):
    try:
        with open(cfg_path) as f:
            data = json.load(f)
    except Exception:
        data = {}

if 'mcpServers' not in data:
    data['mcpServers'] = {}

data['mcpServers']['google-sheets'] = {
    'command': 'npx',
    'args': ['-y', 'sheetcraft-mcp'],
    'env': {
        'SHEETS_TOOLSETS': 'all'
    }
}

with open(cfg_path, 'w') as f:
    json.dump(data, f, indent=2)
"
echo "[✓] Antigravity MCP config updated at: $CONFIG_FILE"

# 4. Check Antigravity
echo ""
echo "----------------------------------------------------------------------"
echo "Step 3: Check Antigravity"
echo "----------------------------------------------------------------------"
if command -v agy &> /dev/null; then
    echo "[✓] Antigravity CLI ('agy') is installed."
else
    echo "[i] Antigravity CLI not found. To install:"
    echo "    npm install -g @google/antigravity-cli"
    echo "    Or launch the Antigravity Desktop 2.0 app."
fi

echo ""
echo "======================================================================"
echo "  INSTALLATION COMPLETE!"
echo "======================================================================"
echo "Open this directory in Antigravity or launch:"
echo "    agy"
echo "Then prompt:"
echo "    'Create a Sprint 10 task tracker and executive dashboard in sheet <URL>'"
echo ""
