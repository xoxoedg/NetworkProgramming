# import socket module
from socket import *
import sys
from sys import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
serverSocket.bind(('', 12000))
serverSocket.listen(1)
print("The server is ready to accept connection")
while True:

    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        http_header = b"HTTP/1.1 200 OK\r\n\r\n"
        print(message)
        connectionSocket.send(http_header)

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            print(outputdata[i])
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n")
        connectionSocket.close()

    sys.exit()  #
