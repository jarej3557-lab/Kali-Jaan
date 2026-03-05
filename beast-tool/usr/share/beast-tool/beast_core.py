import sys
import socket

def scan(target):
    print(f"--- Scanning Target: {target} ---")
    # Basic Port Scan (Example: 80, 443)
    ports = [80, 443, 21, 22]
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        s.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: beast <target_url_or_ip>")
    else:
        target = sys.argv[1]
        scan(target)
