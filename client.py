#Pseudocode for client side programming
import socket

# Client
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5000))
    print("Connected to server, start sending messages (type 'exit' to quit)")
    while True:
        message = input("> ")
        client.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            break
        data = client.recv(1024)
        print(f"Received: {data.decode('utf-8')}")
    client.close()

start_client()
