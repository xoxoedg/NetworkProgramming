from socket import *
import logging

from tech.logger import Logger

logger = Logger(__name__).get_logger()

server_port = 34000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("0.0.0.0", server_port))
serverSocket.listen(1)

while True:

    logger.info('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    ip, port = addr

    logger.info("Accepting request from address: " + ip)
    try:
        message = connectionSocket.recv(1024).decode()
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.sendall(outputdata.encode())
        connectionSocket.close()
    except IOError as e:
        logging.error("Error while sending data" + e.message)
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.close()
    
serverSocket.close()
sys.exit()