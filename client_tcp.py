import socket

SERVER_IP = "100.69.220.50"
PORT = 5100

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

print("Connected to server!")

while True:
    msg = input("You: ")

    if msg.lower() == "exit":
        break

    client.send(msg.encode())

    data = client.recv(1024).decode()
    print("Server:", data)

client.close()