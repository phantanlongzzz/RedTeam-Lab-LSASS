@echo off
setlocal

cd /d "%~dp0"

echo ============================================
echo        RED TEAM LAB - WINDOWS BUILD
echo ============================================

python --version
if errorlevel 1 (
    echo [!] Python was not found.
    exit /b 1
)

python -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo [!] PyInstaller is not installed.
    echo     python -m pip install pyinstaller
    exit /b 1
)

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

if not exist downloads mkdir downloads

python -m PyInstaller ^
    --onefile ^
    --name RedTeamLabPayload ^
    payload.py

if errorlevel 1 (
    echo [!] Build failed.
    exit /b 1
)

copy /Y "dist\RedTeamLabPayload.exe" "downloads\RedTeamLabPayload.exe"

if errorlevel 1 (
    echo [!] Copy failed.
    exit /b 1
)

echo.
echo [+] Windows build complete:
echo     %~dp0downloads\RedTeamLabPayload.exe

endlocal