import socket
import threading

# function to handle incoming messages from clients
def handle_client(conn, addr, clients):
    # add client to list of clients
    clients.append(conn)
    print(f"[NEW CONNECTION] {addr} connected. Total clients: {len(clients)}")

    # loop to receive messages from client
    while True:
        try:
            # receive message from client
            msg = conn.recv(1024).decode('utf-8')
            print(f"[{addr}] {msg}")

            # check if client has ended chat
            if msg.strip().lower() == 'bye':
                conn.send('Bye'.encode('utf-8'))
                conn.close()
                clients.remove(conn)
                print(f"[DISCONNECTED] {addr} disconnected. Total clients: {len(clients)}")
                break

            # send message to all clients except the sender
            for client in clients:
                if client != conn:
                    client.send(msg.encode('utf-8'))
        except:
            clients.remove(conn)
            conn.close()
            print(f"[DISCONNECTED] {addr} disconnected. Total clients: {len(clients)}")
            break

# main function to start the server
def main():
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # define the host and port to bind to
    host = 'localhost'
    port = 8000

    # bind the socket to the host and port
    server.bind((host, port))

    # listen for incoming connections
    server.listen()

    print(f"[LISTENING] Server is listening on {host}:{port}")

    clients = []

    # loop to accept incoming connections
    while True:
        # accept incoming connection
        conn, addr = server.accept()

        # create a new thread to handle the connection
        thread = threading.Thread(target=handle_client, args=(conn, addr, clients))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

# start the program
if __name__ == '__main__':
    main()
