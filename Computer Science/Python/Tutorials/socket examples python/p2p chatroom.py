import threading
import socket
import os

def clearConsole():
    try:
        os.system("cls")
    except:
        try:
            os.system("clear")
        except:
            try:
                print("\033c", end="")
            except:
                print("For some reason the console could not be cleared")

while True:
    print("1. Host\n2. Join")
    instanceType = input("Option number: ")
    if instanceType == "1" or instanceType == "2":
        break
    else:
        clearConsole()
    clearConsole()


print("Enter you alias:")
alias = input("")
clearConsole()

MY_COMP_NAME = socket.gethostname()
MY_IP = socket.gethostbyname(MY_COMP_NAME)
PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 2048

def outputInfo():
    print(f"Hostname: {MY_COMP_NAME}")
    print(f"My IP: {MY_IP}")

outputInfo()

class client:
    def __init__(self):
        self.ip = MY_IP
        self.port = PORT
        self.messages = []
    
    
    def recieveMessages(self):
        
        
        while True:
            pass
    
    
    def connect(self):
