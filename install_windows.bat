@echo off
setlocal enabledelayedexpansion

echo ======================================================================
echo   Google Antigravity - Google Sheets PM Suite Installer (Windows)
echo ======================================================================
echo.

:: 1. Check for Node.js / npx
where npx >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Node.js and npx were not detected on your system.
    echo     Please install Node.js (LTS version) from: https://nodejs.org/
    echo     After installing Node.js, run this script again.
    pause
    exit /b 1
)
echo [✓] Node.js and npx detected.

:: 2. Google Sheets Authentication
echo.
echo ----------------------------------------------------------------------
echo Step 1: Authenticate Google Sheets with your Google Account
echo ----------------------------------------------------------------------
echo Running Google OAuth authentication...
echo A browser window will open. Sign in and grant Sheets access.
echo.
call npx -y sheetcraft-mcp auth login
if %errorlevel% neq 0 (
    echo [!] Google authentication was not completed.
    echo     You can re-run: npx -y sheetcraft-mcp auth login
) else (
    echo [✓] Google Sheets authenticated successfully!
)

:: 3. Configure Antigravity Global MCP
echo.
echo ----------------------------------------------------------------------
echo Step 2: Register Google Sheets MCP in Google Antigravity
echo ----------------------------------------------------------------------
set "CONFIG_DIR=%USERPROFILE%\.gemini\config"
if not exist "%CONFIG_DIR%" mkdir "%CONFIG_DIR%"
set "CONFIG_FILE=%CONFIG_DIR%\mcp_config.json"

powershell -NoProfile -Command ^
  "$cfgPath = '%CONFIG_FILE%';" ^
  "$json = if (Test-Path $cfgPath) { Get-Content $cfgPath -Raw | ConvertFrom-Json } else { [pscustomobject]@{} };" ^
  "if (-not $json.mcpServers) { $json | Add-Member -MemberType NoteProperty -Name 'mcpServers' -Value ([pscustomobject]@{}) };" ^
  "$sheetsConfig = [pscustomobject]@{ command = 'npx'; args = @('-y', 'sheetcraft-mcp'); env = [pscustomobject]@{ SHEETS_TOOLSETS = 'all' } };" ^
  "$json.mcpServers | Add-Member -MemberType NoteProperty -Name 'google-sheets' -Value $sheetsConfig -Force;" ^
  "$json | ConvertTo-Json -Depth 10 | Set-Content $cfgPath -Encoding UTF8"

echo [✓] Antigravity MCP config updated at: %CONFIG_FILE%

:: 4. Verify Antigravity Installation
echo.
echo ----------------------------------------------------------------------
echo Step 3: Verify Antigravity
echo ----------------------------------------------------------------------
where agy >nul 2>nul
if %errorlevel% equ 0 (
    echo [✓] Antigravity CLI ('agy') is installed and ready.
) else (
    echo [i] Antigravity CLI not found in PATH.
    echo     If using Antigravity Desktop 2.0, open the Antigravity application.
    echo     To install the Antigravity CLI, run:
    echo     npm install -g @google/antigravity-cli (or download from https://antigravity.google)
)

echo.
echo ======================================================================
echo   INSTALLATION COMPLETE!
echo ======================================================================
echo You are ready to manage Google Sheets with a single prompt in Antigravity!
echo.
echo Next Steps:
echo 1. Open this folder in Antigravity.
echo 2. Type your prompt in Antigravity, for example:
echo    "Create a Sprint 10 task tracker and executive dashboard in sheet <URL>"
echo.
pause
