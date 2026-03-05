#!/bin/bash
echo "🚀 शशि भाई, मेगा-इंस्टॉलेशन शुरू हो रहा है..."

# 1. जरूरी सिस्टम टूल्स इंस्टॉल करना
sudo apt update && sudo apt install -y python3 python3-pip git curl wget unzip

# 2. फोल्डर्स को चेक करना और परमिशन देना
folders=("AI_AGENT" "SUPREME_TOOL" "kali_jaan" "GDRIVE_BEAST" "beast-tool" "google_drive")

for folder in "${folders[@]}"; do
    if [ -d "$folder" ]; then
        echo "⚙️  $folder को सेटअप कर रहा हूँ..."
        chmod -R +x "$folder"
        # अगर अंदर कोई requirements.txt है तो उसे इंस्टॉल करना
        if [ -f "$folder/requirements.txt" ]; then
            pip3 install -r "$folder/requirements.txt" --break-system-packages
        fi
    else
        echo "⚠️  $folder नहीं मिला, इसे स्किप कर रहा हूँ।"
    fi
done

# 3. .deb फाइल को इंस्टॉल करना
if [ -f "beast-tool.deb" ]; then
    echo "📦 beast-tool.deb को इंस्टॉल कर रहा हूँ..."
    sudo dpkg -i beast-tool.deb || sudo apt --fix-broken install -y
fi

# 4. 'Go' लैंग्वेज के टूल्स को पाथ में जोड़ना
if [ -d "go/bin" ]; then
    export PATH=$PATH:$(pwd)/go/bin
    echo "✅ Go binaries पाथ में जोड़ दी गई हैं।"
fi

echo "🏁 शशि भाई, सारे टूल्स तैयार हैं! अब आप 'Master Commander' चला सकते हैं।"
