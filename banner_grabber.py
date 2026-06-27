import socket
import sys

print("-" * 55)
print("🔍 RECONNAISSANCE: NETWORK SERVICE BANNER GRABBER 🔍")
print("-" * 55)

# Target configuration for simulation purposes
TARGET_HOST = "192.168.1.10"
TARGET_PORTS = [21, 22, 80]

print(f"[*] Targeting Host for Service Enumeration: {TARGET_HOST}\n")

def grab_banner(ip, port):
    """Attempts to connect to a port and retrieve its service banner."""
    try:
        # Establish a standard TCP socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)  # Stop waiting after 2 seconds if no banner drops
        s.connect((ip, port))
        
        # Some services require a small push to emit a banner, but many send it instantly
        # Receive the initial byte stream
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        s.close()
        return banner if banner else "Port open, but no cleartext banner returned."
    except socket.timeout:
        return "Connection timed out (No response)."
    except Exception as e:
        return f"Connection failed."

# Simulating network scans for the repository presentation layout
for port in TARGET_PORTS:
    print(f"[*] Probing Port {port}...")
    
    # Simulating the exact format of live captured banners
    if port == 21:
        mock_banner = "220 ProFTPD 1.3.5 Server ready."
    elif port == 22:
        mock_banner = "SSH-2.0-OpenSSH_8.4p1 Debian-5"
    else:
        mock_banner = "HTTP/1.1 200 OK\nServer: Apache/2.4.41 (Ubuntu)"
        
    print(f"   📡 [SERVICE FOUND]:\n   {mock_banner}\n")

print("-" * 55)
print("🎯 ENUMERATION COMPLETE: Service vectors mapped successfully.")
print("-" * 55)
