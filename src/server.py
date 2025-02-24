import logging
from socket import *
from typing import Tuple, TextIO

from src.tech.logger import Logger

logger: Logger = Logger(__name__)

server_port: int = 34000
serverSocket: socket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("0.0.0.0", server_port))
serverSocket.listen(1)

while True:

    logger.logger.info("Waiting for connection...")
    connectionSocket: socket
    addr: Tuple[str, int]
    connectionSocket, addr = serverSocket.accept()
    ip: str
    port: int
    ip, port = addr

    logger.logger.info("Accepting request from address: " + ip)
    try:
        message: str = connectionSocket.recv(1024).decode()

        filename: str = message.split()[1]
        f: TextIO = open(filename[1:])
        outputdata: str = f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.sendall(outputdata.encode())
        connectionSocket.close()
    except IOError as e:
        logging.error("Error while sending data" + str(e))
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.close()

serverSocket.close()
exit(0)
