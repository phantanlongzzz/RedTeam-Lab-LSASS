#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "============================================"
echo "       RED TEAM LAB - LINUX BUILD"
echo "============================================"

python3 --version

if ! python3 -m PyInstaller --version >/dev/null 2>&1; then
    echo "[!] PyInstaller is not installed."
    echo "    python3 -m pip install pyinstaller"
    exit 1
fi

rm -rf build dist
mkdir -p downloads

python3 -m PyInstaller \
    --onefile \
    --name RedTeamLabPayload \
    payload.py

cp -f dist/RedTeamLabPayload downloads/RedTeamLabPayload

echo
echo "[+] Linux build complete:"
echo "    $SCRIPT_DIR/downloads/RedTeamLabPayload"