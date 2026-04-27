import socket
import signal
import sys

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

conn = None

def shutdown(signum, frame):
    print("\n[SERVER] Se oprește...")

    try:
        if conn:
            conn.close()
            print("[SERVER] Conexiune client închisă")
    except:
        pass

    try:
        server.close()
        print("[SERVER] Socket server închis")
    except:
        pass

    sys.exit(0)

# capture Ctrl+C
signal.signal(signal.SIGINT, shutdown)

print(f"Server pornit pe portul {PORT}")
print("Aștept client...")

try:
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

except Exception as e:
    print(f"Eroare: {e}")

finally:
    shutdown(None, None)