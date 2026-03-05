import os, socket, requests
from flask import Flask, render_template_string, request, session, redirect, send_from_directory
from datetime import datetime

app = Flask(__name__)
app.secret_key = "VISHNU_KEY_2026"

# --- CONFIGURATION (Bhai, yahan aapki details set hain) ---
USER_PASS = "admin123" 
DATA_DIR = os.path.join(os.getcwd(), "world_data")

# --- APKI PRIVATE DETAILS ---
TELEGRAM_TOKEN = "8602662385:AAFfB14VY3kN3QscMqDc0IcqvVAz8nH0jBc" 
CHAT_ID = "8435650166" 

os.makedirs(DATA_DIR, exist_ok=True)

# --- TELEGRAM NOTIFICATION LOGIC ---
def send_to_bot(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID, 
            "text": message, 
            "parse_mode": "HTML"
        }
        requests.post(url, data=payload, timeout=5)
    except: pass

# --- DASHBOARD DESIGN ---
HTML_TEMPLATE = """
<html>
<head><title>VISHNU SUPREME V3</title>
<style>
    body{background:#000;color:#0f0;font-family:monospace;padding:20px;}
    .box{border:1px solid #0f0;padding:15px;margin:10px;border-radius:10px;background:rgba(0,255,0,0.05);}
    .btn{color:black; background:yellow; padding:8px 15px; text-decoration:none; font-weight:bold; border-radius:5px; display:inline-block;}
    .status{color: cyan; font-weight:bold;}
</style>
</head>
<body>
    <h1>[ VISHNU SUPREME : CLOUD ACTIVE ]</h1>
    <p>System Status: <span class="status">● ONLINE</span></p>
    
    <div class="box">
        <h3>📂 GDrive Data Vault:</h3>
        <ul>
            {% for f in files %} 
            <li>{{ f }} <a href="/download/{{ f }}" style="color:cyan;">[Download to School PC]</a></li> 
            {% endfor %}
        </ul>
    </div>

    <div class="box">
        <h3>🧠 OpenAI Public Intelligence:</h3>
        <p>Fetch research data from OpenAI archives directly to your phone.</p>
        <a href="/grab_openai" class="btn">FETCH AI ARCHIVE</a>
    </div>

    <div class="box">
        <h3>📝 Remote Note to GDrive:</h3>
        <form action="/manual_save" method="post">
            <input type="text" name="content" placeholder="Type anything..." style="width:70%;background:#111;color:#0f0;border:1px solid #0f0;padding:5px;">
            <button type="submit" class="btn" style="padding:5px;">SAVE</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('password') == USER_PASS:
            session['logged_in'] = True
            send_to_bot(f"<b>⚠️ LOGIN ALERT</b>\nDashboard accessed from School/External PC!")
            return redirect('/')
        return "Access Denied."
    return '<body style="background:#000;color:#0f0;text-align:center;padding-top:100px;"><form method="post"><h1>ENTER MASTER KEY</h1><input type="password" name="password" style="background:#000;color:#0f0;border:1px solid #0f0;"><br><br><button type="submit">UNLOCK SYSTEM</button></form></body>'

@app.route('/')
def dashboard():
    if not session.get('logged_in'): return redirect('/login')
    files = os.listdir(DATA_DIR)
    return render_template_string(HTML_TEMPLATE, files=files)

@app.route('/grab_openai')
def grab_openai():
    if not session.get('logged_in'): return redirect('/login')
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        # Fetching from Wikipedia's OpenAI page as a public source
        r = requests.get("https://en.wikipedia.org/wiki/OpenAI", headers=headers, timeout=10)
        filename = f"openai_intel_{datetime.now().strftime('%H%M%S')}.txt"
        with open(os.path.join(DATA_DIR, filename), "w", encoding='utf-8') as f:
            f.write(r.text[:5000])
        
        send_to_bot(f"✅ <b>Data Harvested!</b>\nFile: {filename}\nSource: OpenAI Public Archive")
        return redirect('/')
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/manual_save', methods=['POST'])
def manual_save():
    content = request.form.get('content')
    filename = f"school_note_{datetime.now().strftime('%H%M%S')}.txt"
    with open(os.path.join(DATA_DIR, filename), "w") as f:
        f.write(content)
    send_to_bot(f"📥 <b>New Data from School:</b>\n{content}")
    return redirect('/')

@app.route('/download/<filename>')
def download_file(filename):
    if not session.get('logged_in'): return redirect('/login')
    return send_from_directory(DATA_DIR, filename)

if __name__ == "__main__":
    # Starting notification
    send_to_bot("🚀 <b>VISHNU SUPREME ONLINE</b>\nAgent is ready for deployment. Cloud Link established.")
    app.run(host='0.0.0.0', port=5000)

