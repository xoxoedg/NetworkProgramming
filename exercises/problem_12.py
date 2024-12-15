from socket import *

server_port = 15000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print("The Server is running on port", server_port)


while True:
    try:
        connection_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        data = connection_socket.recv(4096)
        if not data:
            print("No data received. Closing connection.")
            continue

        # Decode and print the HTTP request
        print(f"Received:\n{data.decode('utf-8')}\n")

        # Send a basic HTTP response
        response = "HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nHello, World!"
        connection_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error in connection handling: {e}")
    finally:
        connection_socket.close()