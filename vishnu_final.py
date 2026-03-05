import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Kiwix port 8080 par chal raha hai
KIWIX_URL = "http://localhost:8080" 

@app.route('/')
def dashboard():
    return render_template_string("""
    <html>
    <head>
        <title>VISHNU SUPREME : GLOBAL DATA AGENT</title>
        <style>
            body { background: #000; color: #0f0; font-family: 'Courier New'; margin: 0; overflow: hidden; }
            .header { height: 60px; background: #050505; border-bottom: 2px solid #0f0; padding: 10px; text-align: center; }
            .content { height: calc(100vh - 80px); width: 100%; border: none; }
            iframe { width: 100%; height: 100%; border: none; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1 style="margin:0;">[ VISHNU AGENT : GLOBAL DATA ]</h1>
            <p style="margin:0;">Status: Offline Knowledge Base Active</p>
        </div>
        <div class="content">
            <iframe src="{{ url }}"></iframe>
        </div>
    </body>
    </html>
    """, url=KIWIX_URL)

if __name__ == "__main__":
    # Dashboard ko port 5000 par chalayenge
    app.run(host='0.0.0.0', port=5000)

