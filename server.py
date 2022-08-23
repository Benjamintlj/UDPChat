
import socket

localAddress = ''
localPort = 8080
bufferSize = 1024
encodingFormat = 'utf-8'

msg = 'I got your message!'.encode(encodingFormat)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((localAddress, localPort))

while True:
    receivedMessage, receivedAddress = serverSocket.recvfrom(bufferSize)

    print(receivedMessage.decode(encodingFormat))

    serverSocket.sendto(msg, receivedAddress)

