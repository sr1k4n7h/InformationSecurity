__author__ = 'sr1k4n7h'

import socket

host = ''
port = 12347
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

p = 107
g = 73
b = 15
B = (g ** b) % p

s.sendall(bytes(B))
A = s.recv(1024)
s.close()
print 'Alice Secret Key : ', repr(A)

Bob_Shared_Secret = (int(A) ** b) % p
print("Bob privately calculated Shared Secret Key : " + str(Bob_Shared_Secret))

