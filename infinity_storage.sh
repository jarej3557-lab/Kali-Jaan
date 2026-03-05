#!/bin/bash
echo "🌌 KALI JAAN INFINITY-STORAGE IS ONLINE..."

# Local data folder
LOCAL_DIR=~/kali_jaan/local_data
mkdir -p $LOCAL_DIR

while true; do
  # Check if there is any data to move
  if [ "$(ls -A $LOCAL_DIR)" ]; then
    echo "🛸 Teleporting data to Cloud... (Unlimited Mode)"
    
    # Ye command data ko cloud pe bhejegi aur local se delete kar degi
    # Jisse local 47GB hamesha khali rahegi
    rclone move $LOCAL_DIR gdrive:KALI_JAAN_MASS_DATA --delete-empty-src-dirs --transfers 4 --checkers 8
    
    echo "✅ Local Space Recovered. Ready for more data!"
  fi
  # Har 5 second mein check karega
  sleep 5
done
