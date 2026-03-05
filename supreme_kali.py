import os
import sys
import subprocess
import platform
import socket
from flask import Flask, render_template_string
from datetime import datetime

# --- AUTOMATIC DEPENDENCY INSTALLER ---
def install_dependencies():
    print("[*] Checking Dependencies...")
    required = ['flask', 'requests']
    for lib in required:
        try:
            __import__(lib)
        except ImportError:
            print(f"[!] Installing {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Execute installation before starting
install_dependencies()

app = Flask(__name__)

# --- CORE SECURITY LOGIC ---

def get_details():
    return {
        "ip": socket.gethostbyname(socket.gethostname()),
        "os": platform.system(),
        "release": platform.release(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# --- BROWSER DASHBOARD (EXTANDABLE) ---

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Supreme AI Command Center</title>
    <style>
        body { background-color: #050505; color: #00ff00; font-family: 'Courier New', monospace; margin: 0; padding: 20px; }
        .header { border-bottom: 2px solid #ff0000; padding-bottom: 10px; margin-bottom: 20px; text-align: center; }
        .container { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
        .card { border: 1px solid #00ff00; padding: 15px; background: #0a0a0a; box-shadow: 0 0 10px #00ff0033; }
        .btn { background: #ff0000; color: white; border: none; padding: 10px 20px; cursor: pointer; font-weight: bold; width: 100%; margin-top: 10px; }
        .btn:hover { background: #cc0000; }
        .status-on { color: #00ff00; font-weight: bold; }
    </style>
</head>
<body>
    <div class="header">
        <h1>VISHNU SUPREME AI: V2.0</h1>
        <p>Global Security & Research Dashboard</p>
    </div>

    <div class="container">
        <div class="card">
            <h3>[+] System Intelligence</h3>
            <p>Local IP: {{ data.ip }}</p>
            <p>Kernel: {{ data.os }} {{ data.release }}</p>
            <p>Server Time: {{ data.time }}</p>
        </div>

        <div class="card">
            <h3>[+] Media Access</h3>
            <p>Status: <span class="status-on">READY</span></p>
            <button class="btn" onclick="alert('Initializing Voice Listener...')">START MIC MONITOR</button>
            <button class="btn" onclick="alert('Scanning for Media Files...')">BROWSE PHOTOS</button>
        </div>

        <div class="card" style="grid-column: span 2;">
            <h3>[+] World-Wide Modules</h3>
            <div style="display: flex; gap: 10px;">
                <button class="btn" style="background: #333;">Network Recon</button>
                <button class="btn" style="background: #333;">Vulnerability Scan</button>
                <button class="btn" style="background: #333;">Payload Gen</button>
            </div>
            <p style="font-size: 12px; margin-top: 10px; color: #888;">Note: Add your custom Python logic in the 'modules' directory.</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, data=get_details())

# --- LAUNCHER ---
if __name__ == "__main__":
    # Flask ko '0.0.0.0' par chalane se ye network ke kisi bhi device se open hoga
    print("\n" + "="*50)
    print("   SUPREME AI LOADED SUCCESSFULLY")
    print("="*50)    app.run(host='0.0.0.0', port=5000)
