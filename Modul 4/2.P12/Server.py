from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recvfrom(2048)
	print (message)