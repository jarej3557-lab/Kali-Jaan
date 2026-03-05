#!/bin/bash
echo "🌍 KALI JAAN GLOBAL CLOUD DOMINATION STARTING..."

# दुनिया के मशहूर क्लाउड फोल्डर्स बनाना
CLOUDS=("gdrive" "mega" "dropbox" "onedrive" "box" "yandex" "pcloud" "amazon" "azure" "s3")

for cloud in "${CLOUDS[@]}"; do
    mkdir -p ~/kali_jaan/world_storage/$cloud
    echo "📁 Created slot for: $cloud"
done

# Ghost Mirror को ग्लोबल बनाना (किसी भी फोल्डर में डेटा डालो, वो क्लाउड पर जाएगा)
while true; do
  for cloud in "${CLOUDS[@]}"; do
    if [ "$(ls -A ~/kali_jaan/world_storage/$cloud)" ]; then
       echo "🚀 Pushing data to $cloud..."
       rclone move ~/kali_jaan/world_storage/$cloud $cloud:KALI_JAAN_ARCHIVE --delete-empty-src-dirs &
    fi
  done
  sleep 15
done
