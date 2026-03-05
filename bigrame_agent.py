#!/usr/bin/env python3
# ================================
# BIGRAME AI SECURITY AGENT
# Legal Bug Bounty Assistant
# ================================

import os
import subprocess
import pickle
import time
from pathlib import Path

import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


# ================================
# CONFIG
# ================================

HOME = Path.home()

DATA_FOLDER = HOME / "ALL_DATA_BACKUP"
AGENT_DIR = HOME / "bigrame-agent"
MODEL_DIR = AGENT_DIR / "model"
REPORT_DIR = AGENT_DIR / "reports"

MODEL_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_FILE = MODEL_DIR / "ai_model.pkl"
VECT_FILE = MODEL_DIR / "vectorizer.pkl"


# ================================
# PDF TEXT EXTRACT
# ================================

def extract_text_from_pdf(file_path):

    text = ""

    try:
        reader = PyPDF2.PdfReader(str(file_path))

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        print("[ERROR] PDF Read Failed:", file_path.name)

    return text


# ================================
# TRAIN AI MODEL
# ================================

def train_ai():

    print("\n[INFO] Searching PDFs...")

    pdfs = list(DATA_FOLDER.glob("*.pdf"))

    if not pdfs:
        print("[WARNING] No PDFs Found!")
        return None, None


    print("[INFO]", len(pdfs), "PDFs Found")

    texts = []

    for pdf in pdfs:
        print("[READING]", pdf.name)
        text = extract_text_from_pdf(pdf)

        if text.strip():
            texts.append(text)


    if not texts:
        print("[ERROR] No valid text found")
        return None, None


    print("[INFO] Vectorizing data...")

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=15000
    )

    X = vectorizer.fit_transform(texts)

    y = [0] * len(texts)


    print("[INFO] Training AI...")

    model = MultinomialNB()
    model.fit(X, y)


    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)

    with open(VECT_FILE, "wb") as f:
        pickle.dump(vectorizer, f)


    print("[SUCCESS] AI Training Complete!")

    return model, vectorizer


# ================================
# LOAD AI
# ================================

def load_ai():

    if not MODEL_FILE.exists():
        return None, None


    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)

    with open(VECT_FILE, "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer


# ================================
# RUN RECON SCAN
# ================================

def run_recon(target):

    print("\n[INFO] Starting Recon on:", target)

    report_file = REPORT_DIR / f"{target}_report.txt"


    with open(report_file, "w") as report:

        report.write("BIGRAME AI REPORT\n")
        report.write("Target: " + target + "\n\n")


        # NMAP
        print("[SCAN] Nmap...")

        report.write("==== NMAP ====\n")

        nmap = subprocess.getoutput(f"nmap -sV {target}")

        report.write(nmap + "\n\n")


        # WAYBACK URLs (gau)
        print("[SCAN] Wayback URLs...")

        report.write("==== WAYBACK URLS ====\n")

        gau = subprocess.getoutput(f"gau {target}")

        report.write(gau + "\n\n")


        # HTTPX
        print("[SCAN] HTTPX...")

        report.write("==== HTTPX ====\n")

        httpx = subprocess.getoutput(f"echo {target} | httpx")

        report.write(httpx + "\n\n")


    print("[SUCCESS] Report Saved:", report_file.name)



# ================================
# LIVE WATCHER (AUTO TRAIN)
# ================================

def pdf_watcher():

    print("\n[WATCHER] Started...")

    known = set()

    while True:

        pdfs = set(DATA_FOLDER.glob("*.pdf"))

        new = pdfs - known

        if new:
            print("[NEW PDF FOUND] Training AI...")
            train_ai()
            known = pdfs

        time.sleep(30)



# ================================
# MENU
# ================================

def show_menu():

    print("""
===========================
 BIGRAME AI SECURITY AGENT
===========================

1. Train AI from PDFs
2. Run Recon Scan
3. Start PDF Watcher
4. Exit

===========================
""")


# ================================
# MAIN
# ================================

def main():

    print("\n[STARTING] BIGRAME AI AGENT\n")

    model, vectorizer = load_ai()

    if model:
        print("[INFO] AI Model Loaded")
    else:
        print("[INFO] No AI Model Found")


    while True:

        show_menu()

        choice = input("Enter Option: ").strip()


        # TRAIN
        if choice == "1":
            train_ai()


        # SCAN
        elif choice == "2":

            target = input("Enter Target Domain: ").strip()

            if target:
                run_recon(target)


        # WATCHER
        elif choice == "3":
            pdf_watcher()


        # EXIT
        elif choice == "4":
            print("Bye!")
            break


        else:
            print("Invalid Option!")



# ================================
# RUN
# ================================

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# ======================================
# BIGRAME AI AGENT NEXT LEVEL
# Auto Recon + AI Risk Detection + Alerts
# ======================================

import os
import subprocess
import pickle
import time
from pathlib import Path
import requests
import json

import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


HOME = Path.home()
DATA_FOLDER = HOME / "ALL_DATA_BACKUP"
AGENT_DIR = HOME / "bigrame-agent"
MODEL_DIR = AGENT_DIR / "model"
REPORT_DIR = AGENT_DIR / "reports"

MODEL_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

MODEL_FILE = MODEL_DIR / "ai_model.pkl"
VECT_FILE = MODEL_DIR / "vectorizer.pkl"

# ===========================
# TELEGRAM CONFIG
# ===========================
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("[TELEGRAM ERROR]", e)

# ===========================
# PDF AI TRAINER
# ===========================
def extract_text_from_pdf(file_path):
    text = ""
    try:
        reader = PyPDF2.PdfReader(str(file_path))
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except:
        pass
    return text

def train_ai():
    pdfs = list(DATA_FOLDER.glob("*.pdf"))
    if not pdfs:
        return None, None
    texts = [extract_text_from_pdf(pdf) for pdf in pdfs if extract_text_from_pdf(pdf).strip()]
    if not texts:
        return None, None
    vectorizer = TfidfVectorizer(stop_words="english", max_features=15000)
    X = vectorizer.fit_transform(texts)
    y = [0]*len(texts)
    model = MultinomialNB()
    model.fit(X, y)
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)
    with open(VECT_FILE, "wb") as f:
        pickle.dump(vectorizer, f)
    return model, vectorizer

def load_ai():
    if not MODEL_FILE.exists():
        return None, None
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)
    with open(VECT_FILE, "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

# ===========================
# AUTO SUBDOMAIN + SCAN
# ===========================
def find_subdomains(domain):
    print("[INFO] Finding subdomains for", domain)
    try:
        output = subprocess.getoutput(f"subfinder -d {domain} -silent")
        subdomains = output.splitlines()
        return subdomains
    except:
        return []

def run_recon(domain):
    subdomains = find_subdomains(domain)
    for sub in subdomains:
        report_file = REPORT_DIR / f"{sub}_report.txt"
        with open(report_file, "w") as f:
            f.write(f"Target: {sub}\n")
            nmap_res = subprocess.getoutput(f"nmap -sV {sub}")
            f.write("=== NMAP ===\n" + nmap_res + "\n")
            httpx_res = subprocess.getoutput(f"echo {sub} | httpx")
            f.write("=== HTTPX ===\n" + httpx_res + "\n")
        send_telegram(f"[BIGRAME AI] Recon complete for {sub}, report saved.")

# ===========================
# LIVE PDF WATCHER
# ===========================
def pdf_watcher():
    known = set()
    while True:
        pdfs = set(DATA_FOLDER.glob("*.pdf"))
        new = pdfs - known
        if new:
            train_ai()
            known = pdfs
        time.sleep(30)

# ===========================
# MENU
# ===========================
def menu():
    print("""
===========================
BIGRAME AI NEXT LEVEL
===========================

1. Train AI from PDFs
2. Run Recon Scan
3. Start PDF Watcher
4. Exit
===========================
""")

def main():
    model, vect = load_ai()
    while True:
        menu()
        choice = input("Enter Option: ").strip()
        if choice=="1":
            train_ai()
        elif choice=="2":
            domain = input("Enter domain: ").strip()
            if domain:
                run_recon(domain)
        elif choice=="3":
            pdf_watcher()
        elif choice=="4":
            break
        else:
            print("Invalid choice!")

if __name__=="__main__":
    main()
