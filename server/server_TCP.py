import socket

HOST = "0.0.0.0"
PORT = 5100

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server pornit pe portul {PORT}")
print("Aștept client...")

conn, addr = server.accept()
print(f"Client conectat: {addr}")

while True:
    data = conn.recv(1024)

    if not data:
        print("Client deconectat.")
        break

    mesaj = data.decode()
    print("Client:", mesaj)

    if mesaj.lower() == "exit":
        break

    raspuns = input("Server: ")
    conn.send(raspuns.encode())

conn.close()
server.close()