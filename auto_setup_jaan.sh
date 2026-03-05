#!/bin/bash
echo "🔥 KALI JAAN STORAGE TUNING (V101)..."

# 1. Purane mounts ko saaf karna
fusermount -u ~/kali_jaan/drive1 2>/dev/null
pkill -9 rclone 2>/dev/null

# 2. Folder check karna
mkdir -p ~/kali_jaan/drive1

# 3. Mounting with specialized flags for Stability
rclone mount gdrive: ~/kali_jaan/drive1 \
    --vfs-cache-mode writes \
    --allow-other \
    --daemon

sleep 2
if mountpoint -q ~/kali_jaan/drive1; then
    echo "✅ SHASHI BHAI, G-DRIVE AB CONNECT HAI!"
    df -h ~/kali_jaan/drive1
else
    echo "❌ ERROR: Mount nahi ho paya. Ek baar 'sudo apt install fuse3' check karein."
fi
