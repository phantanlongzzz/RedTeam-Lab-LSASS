@echo off
setlocal EnableExtensions

cd /d "E:\IT_Workspace\Ethical Hacking\web\Plan\benign_payload"

:: ================================================================
:: RED TEAM LAB BUILD SCRIPT
:: ================================================================

:: Mặc định toàn bộ CMD là chữ đỏ
color 0C
cls

echo.
echo ================================================================
echo.
echo              RRRR   EEEEE  DDDD
echo              R   R  E      D   D
echo              RRRR   EEEE   D   D
echo              R R    E      D   D
echo              R  RR  EEEEE  DDDD
echo.
echo              TTTTT  EEEEE   AAAAA  M   M
echo                T    E       A   A  MM MM
echo                T    EEEE    AAAAA  M M M
echo                T    E       A   A  M   M
echo                T    EEEEE   A   A  M   M
echo.
echo ================================================================
echo.
echo              !!! RED TEAM LAB BUILD !!!
echo              !!! PAYLOAD BUILD SYSTEM !!!
echo.
echo ================================================================
echo.

powershell -NoProfile -Command "Write-Host '[!] BUILDING RED TEAM LAB PAYLOAD...' -ForegroundColor Red"

echo.
echo [1/2] Building payload...
echo.

python -m PyInstaller --onefile --name RedTeamLabPayload payload.py

if errorlevel 1 (
    echo.
    powershell -NoProfile -Command "Write-Host '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' -ForegroundColor Red"
    powershell -NoProfile -Command "Write-Host '           !!! BUILD FAILED !!!' -ForegroundColor Red"
    powershell -NoProfile -Command "Write-Host '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' -ForegroundColor Red"
    echo.
    powershell -NoProfile -Command "Write-Host 'PyInstaller returned an error.' -ForegroundColor Red"
    echo.
    pause
    exit /b 1
)

echo.
powershell -NoProfile -Command "Write-Host '[+] BUILD SUCCESS' -ForegroundColor Green"
echo.

echo [2/2] Copying EXE to web downloads...
echo.

copy /Y "dist\RedTeamLabPayload.exe" "..\..\downloads\RedTeamLabPayload.exe"

if errorlevel 1 (
    echo.
    powershell -NoProfile -Command "Write-Host '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' -ForegroundColor Red"
    powershell -NoProfile -Command "Write-Host '           !!! COPY FAILED !!!' -ForegroundColor Red"
    powershell -NoProfile -Command "Write-Host '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' -ForegroundColor Red"
    echo.
    powershell -NoProfile -Command "Write-Host 'Could not copy the EXE to the downloads folder.' -ForegroundColor Red"
    echo.
    pause
    exit /b 1
)

echo.
powershell -NoProfile -Command "Write-Host '[+] COPY SUCCESS' -ForegroundColor Green"

echo.
powershell -NoProfile -Command "Write-Host '================================================================' -ForegroundColor Green"
powershell -NoProfile -Command "Write-Host '             !!! BUILD COMPLETE !!!' -ForegroundColor Green"
powershell -NoProfile -Command "Write-Host '================================================================' -ForegroundColor Green"
echo.

pause
exit /b 0
