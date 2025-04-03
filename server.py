#This is a pseudocode for implementing server side socket and threading
import socket
import threading

# Server
def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"Received from {client_address}: {message}")
            # Broadcast the message to all connected clients
            for c in clients:
                if c != client_socket:
                    try:
                        c.send(data)
                    except:
                        clients.remove(c)
        except:
            break
    print(f"Connection with {client_address} closed")
    clients.remove(client_socket)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000))
    server.listen(5)
    print("Server started, waiting for connections...")
    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

clients = []
start_server()
