import socket

localAddress = ''
localPort = 8080
bufferSize = 1024
encodingFormat = 'utf-8'

msg = 'hey mr server'.encode(encodingFormat)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.sendto(msg, (localAddress, localPort))

msgFromServer = clientSocket.recvfrom(bufferSize)

print(msgFromServer[0].decode('utf-8'))
