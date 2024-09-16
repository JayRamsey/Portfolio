#Chat server side
import socket

#Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#Create a server socket, bind it to an IP/Port, and listen
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST_IP, HOST_PORT))
serverSocket.listen()
print(HOST_IP, HOST_PORT)

#Accept any incoming connection
print("Server is running...\n")
clientSocket, clientAddress = serverSocket.accept()
clientSocket.send("You are connected to the server...\n".encode(ENCODER))

#Send/ recieve messages
while True:
    #recieve information from client
    message = clientSocket.recv(BYTESIZE).decode(ENCODER)
    if message == "quit":
        clientSocket.send("quit".encode(ENCODER))
        print("Ending the chat...")
        break
    else:
        print(f"{message}")
        message = input("Message: ")
        clientSocket.send(message.encode(ENCODER))

#Close the socket
serverSocket.close()