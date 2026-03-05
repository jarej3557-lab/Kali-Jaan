#!/bin/bash
echo "⚡ KALI JAAN GLOBAL BEAST MODE ACTIVATING..."

# Duniya bhar ke 40+ providers ki list
PROVIDERS=("gdrive" "mega" "onedrive" "dropbox" "box" "pcloud" "yandex" "amazon" "s3" "b2" "webdav" "ftp" "sftp" "azure" "googlecloud" "wasabi" "hubic" "koofr" "jottacloud" "opendrive" "uptobox")

mkdir -p ~/kali_jaan/world_storage

for p in "${PROVIDERS[@]}"; do
    mkdir -p ~/kali_jaan/world_storage/$p
    echo "🔗 Slot Ready for: $p"
done

# 'Ghost Mirror' ka Advanced Version jo har slot ko monitor karega
while true; do
  for p in "${PROVIDERS[@]}"; do
    if [ "$(ls -A ~/kali_jaan/world_storage/$p)" ]; then
       echo "🌪️ Sucking data into $p..."
       rclone move ~/kali_jaan/world_storage/$p $p:KALI_JAAN_WORLD_DATA --delete-empty-src-dirs --transfers 10 --checkers 20 &
    fi
  done
  sleep 10
done
