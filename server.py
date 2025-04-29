import socket
import threading

HOST = 'localhost'
PORT = 5555

clients = []

def handle_client(conn):
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"[SERVER] Received: {data}")
        except:
            break
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[SERVER] Listening on {HOST}:{PORT}")
    
    while True:
        conn, addr = server.accept()
        print(f"[SERVER] Connected to {addr}")
        thread = threading.Thread(target=handle_client, args=(conn,))
        thread.start()

if __name__ == "__main__":
    main()
