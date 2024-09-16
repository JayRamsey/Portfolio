import threading, socket
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
menu = ttk.Frame(window)
menu.pack(padx=20, pady=20)

MY_IP = socket.gethostbyname(socket.gethostname())
PORT = 12345
ENCODING = "utf-8"
clientSocket = None
BYTESIZE = 1024

def sendToHost(message):
    message = message.encode(ENCODING)
    clientSocket.send(message)

def join():
    if aliasEntry.get() != "":
        global clientSocket
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global HOST_ADDRESS
        HOST_ADDRESS = (hostIPEntry.get(), PORT)
        try:
            clientSocket.connect(HOST_ADDRESS)
        except:
            messagebox.showerror("IP not found", "The specified IP address is not a host.")
            return
    else:
        messagebox.showerror("Invalid alias", "You must specify your name.")
        return

    


def host():
    if aliasEntry.get() != "":
        global clientSocket
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global HOST_ADDRESS
        HOST_ADDRESS = (socket.gethostbyname(socket.gethostname()), PORT)
        
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind(HOST_ADDRESS)
        serverSocket.listen()
        
        clientSockets = []
        
    else:
        messagebox.showerror("Invalid alias", "You must specify your name.")
        return


    def broadcastMessage(message):
        for clientSocket in clientSockets:
            clientSocket.send(message.encode(ENCODING))
    
    
    def connectionLoop():
        while True:
            clientSocket, clientAddr = serverSocket.accept()
            clientSockets.append(clientSocket)
        
    def recieveLoop():
        while True:
            for clientSocket in clientSockets:
                message = clientSocket.recv(BYTESIZE)
                broadcastMessage(message)
                

ttk.Label(menu, text="Alias:").pack()
aliasEntry = ttk.Entry(menu)
aliasEntry.pack()

ttk.Label(menu, text="Room IP address:").pack()
hostIPEntry = ttk.Entry(menu)
hostIPEntry.pack()

joinButton = ttk.Button(menu, text="Join Room", command=join)
joinButton.pack(pady=25, side="left")

hostButton = ttk.Button(menu, text="Host")
hostButton.pack(pady=25, side="left")



window.mainloop()