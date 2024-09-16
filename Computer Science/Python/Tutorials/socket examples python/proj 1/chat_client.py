#Chat client side
import socket

#Define constants
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#Create a client socket and connect to server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((DEST_IP, DEST_PORT))

#Send/ recieve messages
while True:
    #Recieve information from the server
    message = clientSocket.recv(BYTESIZE).decode(ENCODER)
    
    #Quit if the connected server wants to quit
    if message == "quit":
        clientSocket.send("quit".encode(ENCODER))
        print("\nEnding the chat...")
        break
    else:
        print(f"{message}")
        message = input("Message: ")
        clientSocket.send(message.encode(ENCODER))

#Close the client socket
clientSocket.close()