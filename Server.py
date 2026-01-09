import socket
import random
import os

os.system("cls") #Use "cls" on Windows and "clear" on Linux
print("//~~ Server Side ~~//")

host, port = ("127.0.0.1", 1337)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

(client, (host, port)) = sock.accept()

#Recieving the request SYN
syn = client.recv(1024).decode()
print(syn)

#sending request SYN-ACK
m = syn.split("seq=")[1]
m = str(int(m) + 1)
n = str(random.randint(100, 2000))

client.sendall(b"[2] SYN/seq=" + n.encode() + b" ACK/seq=" + m.encode())

#Receive the request ACK
ack = client.recv(1024).decode()
print(ack)

#Connection established!
print("\n" + "=" *40)
print("✅CONNECTION ESTABLISHED!")
print("=" * 40)
print("/nThree-way handshake complete.")
print("Server is now connected to the client.")