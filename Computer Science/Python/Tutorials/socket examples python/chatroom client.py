import tkinter as tk
import threading, socket


window = tk.Tk()
window.title("Chatroom")
window.geometry("800x450")

def attemptConnect():
    pass

def joinPressed():
    



mainMenuFrame = tk.Frame(window)

tk.Label(mainMenuFrame, text="Alias:").pack()
nameEntry = tk.Entry(mainMenuFrame)
nameEntry.pack()

tk.Label(mainMenuFrame, text="Room IP:").pack()
roomEntry = tk.Entry(mainMenuFrame)
roomEntry.pack()

joinButton = tk.Button(mainMenuFrame, text="Join Room", command=joinPressed)


mainMenuFrame.pack()






window.mainloop()