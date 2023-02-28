# Getting IP address using python

import socket
hostname = socket.gethostname()
IPAddre = socket.gethostbyname(hostname)
print(IPAddre)