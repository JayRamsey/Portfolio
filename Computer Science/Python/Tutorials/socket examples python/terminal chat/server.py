import socket, threading

#Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#Create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST_IP, HOST_PORT))
serverSocket.listen()

clientSocketList = []

messages = []

def addMessage(message):
    messages.append(message)

def broadcast_message(message):
    for clientSocket in clientSocketList:
        clientSocket.send(message)

def recieve_message():
    '''Recieve an incoming message from a specific client'''
    while True:
        for clientSocket in clientSocketList:
            message = clientSocket.recv(BYTESIZE)
            # if message:
            print(message.decode(ENCODER))
            addMessage(message)
            broadcast_message(messages)
            
def connect_client():
    '''Connect an incoming client to the server'''
    while True:
        clientSocket, clientAddr = serverSocket.accept()
        clientSocketList.append(clientSocket)
        

connectThread = threading.Thread(target=connect_client)
recieveThread = threading.Thread(target=recieve_message)

connectThread.start()
recieveThread.start()

recieveThread.join()



