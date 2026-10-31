import socket 

s= socket.socket()

s.bind(("localhost", 9999))

s.listen(3)
print("Listning...")

while True:

    conn , addr = s.accept()
    print("Accepting connection from ",addr)
    conn.send("Thank you for connecting".encode())

    data = conn.recv(1024).decode()
    if not data:
        break

    print("Mesage revieved from client ")

    conn.close()








