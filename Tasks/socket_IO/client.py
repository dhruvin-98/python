import socket

c = socket.socket()
print("socket created")

c.connect(("localhost",9999))

name = input("Name : ")

c.send((name.encode()))
