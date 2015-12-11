__author__ = 'sr1k4n7h'

import socket

host = ''
port = 12347
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

p = 107
g = 73
a = 6
A = (g ** a) % p

conn, addr = s.accept()
B = conn.recv(1024)
print("Bob Secret Key :" + repr(B))
conn.sendall(bytes(A))

Alice_Shared_Secret = (int(B) ** a) % p
print("Alice privately calculated Shared Secret Key : " + str(Alice_Shared_Secret))
conn.close()
