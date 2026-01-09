import socket
import random
import os

os.system("cls") #Use "cls" on Windows and "clear" on Linux
print("//~~ Client Side ~~//")

host, port = ("127.0.0.1", 1337)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

#Sending the request SYN
m = str(random.randint(1000, 2000))
sock.sendall(b"[1] SYN/seq=" + m.encode())

#Recieving the request SYN-ACK
synack = sock.recv(1024).decode()
print(synack)

#Sending the request ACK
n = synack.split("seq=")[1].split(" ")[0]
n = str(int(n) + 1)
sock.sendall(b"[3] ACK/seq=" + n.encode())

#Connection established!
print("\n" + "=" * 40)
print("✅ CONNECTION ESTABLISHED!")
print("=" * 40)
print("\nThree-way handshake complete.")
print("Client is now connected to the server.")