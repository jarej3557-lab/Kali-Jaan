#!/bin/bash
echo "🛡️ KALI JAAN GHOST-MIRROR IS ACTIVE..."

# Local folder बनाना जहाँ आप काम करेंगे
mkdir -p ~/kali_jaan/local_data

# बैकग्राउंड में लूप चलाना जो हर 10 सेकंड में डेटा क्लाउड पर भेजेगा
while true; do
  # अगर फोल्डर खाली नहीं है, तो डेटा मूव करें
  if [ "$(ls -A ~/kali_jaan/local_data)" ]; then
    echo "📦 Moving data to G-Drive to save space..."
    rclone move ~/kali_jaan/local_data gdrive:KALI_JAAN_DATA --delete-empty-src-dirs
  fi
  sleep 10
done
