import socket, threading, os
#import tkinter as tk

#Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024
NAME = "Client"
NAME_SEPARATOR = " ~ "


#window = tk.Tk()
#window.title(socket.gethostname())

#Create client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((DEST_IP, DEST_PORT))
clientSocket.send(f"{NAME} has connected".encode(ENCODER))

def config_message(text):
    return (NAME + NAME_SEPARATOR + text).encode(ENCODER)

def send_message():
    '''send a message to the server'''
    while True:
        clientSocket.send(config_message(input("")))

def print_message(message):
    os.system("cls")
    print(message.decode(ENCODER))

def recieve_message():
    '''recieve an incoming message'''
    while True:
        message = clientSocket.recv(BYTESIZE)
        if message:
            print_message(message)

recieveThread = threading.Thread(target=recieve_message)
sendThread = threading.Thread(target=send_message)

recieveThread.start()
sendThread.start()
sendThread.join()
print("Program ended")

