import socket

SERVER_IP = "100.69.220.50"
PORT = 5100

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP client ready!")

while True:
	msg = input("You: ")

	if msg.lower() == "exit":
		break

	client.sendto(msg.encode(), (SERVER_IP, PORT))

	data, addr = client.recvfrom(1024)
	print("Server:", data.decode())

client.close()
