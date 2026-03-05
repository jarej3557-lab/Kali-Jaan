import os, sys, telebot, subprocess, shutil, time

BOT_TOKEN = "8771709842:AAGfrocNi8TkDxi8wMIKgv_srxrtp23D0z0"
bot = telebot.TeleBot(BOT_TOKEN)
FILENAME = "/home/kali/gdrive/kalijaan.py"

@bot.message_handler(commands=['update'])
def handle_update(message):
    # यह सिर्फ तभी चलेगा जब आप /update लिखकर कोड भेजेंगे
    new_code = message.text.replace('/update', '').strip()
    if not new_code:
        bot.reply_to(message, "शशि भाई, कोड तो लिखिये!")
        return
    
    with open("test_code.py", "w") as f:
        f.write(new_code)
    
    check = subprocess.run([sys.executable, "-m", "py_compile", "test_code.py"], capture_output=True)
    if check.returncode == 0:
        with open(FILENAME, "w") as f: f.write(new_code)
        bot.reply_to(message, "✅ सिस्टम अपडेट हो गया! रीस्टार्ट हो रहा हूँ...")
        os.execv(sys.executable, ['python3'] + sys.argv)
    else:
        bot.reply_to(message, f"❌ कोड में गड़बड़ है:\n{check.stderr.decode()}")

@bot.message_handler(func=lambda m: True)
def chat_logic(message):
    # यहाँ आप जो भी पूछेंगे, उसका जवाब मिलेगा
    msg = message.text.lower()
    if "hacking" in msg:
        bot.reply_to(message, "🛡️ शशि भाई, हम Penetration Testing (Network, Web, OSINT) कर सकते हैं। आप कौन सा टूल चलाना चाहते हैं?")
    else:
        bot.reply_to(message, "🦁 काली जान एक्टिव है। आदेश दीजिये!")

if name == "main":
    while True:
        try: bot.infinity_polling()
        except: time.sleep(5)