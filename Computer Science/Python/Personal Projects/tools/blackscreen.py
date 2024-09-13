import tkinter as tk

PIN = "16777216"

alpha = 1
lastToggleOn = True
locked = False

window = tk.Tk()
window.title("Blackscreen")
window.config(bg="black")
window.attributes("-fullscreen", True)

unlockEntry = tk.Entry(window, relief="flat", bg="black", fg="white")
unlockEntry.place(x=0, y=0)

def lock(eventCatch):
    global alpha
    alpha = 1
    update()
    locked = True
    window.attributes("-topmost", True)

def update():
    global alpha
    clampAlpha()
    window.attributes("-alpha", alpha)

def clampAlpha():
    global alpha
    if not locked:
        if alpha > 1:
            alpha = 1
        if alpha < 0.01:
            alpha = 0.01
    else:
        alpha = 1

def upAlpha(eventCatch):
    global alpha
    alpha += 0.01
    update()

def downAlpha(eventCatch):
    global alpha
    alpha -= 0.01
    update()

def toggleOff():
    global alpha
    alpha = 0
    update()

def toggleAlpha(eventCatch):
    global alpha, lastToggleOn
    if lastToggleOn:
        alpha = 0 if alpha == 1 else 1
        lastToggleOn = not lastToggleOn
    else:
        alpha = 1 if alpha >= 0 else 0
        lastToggleOn = not lastToggleOn
    update()

def checkPin(eventCatch):
    global PIN
    global unlockEntry
    global locked
    chars = unlockEntry.get()
    if chars == PIN:
        locked = False
        window.attributes("-topmost", False)
        window.iconify()
        
unlockEntry.bind("<KeyRelease>", checkPin)

window.bind("<Up>", upAlpha)
window.bind("<Down>", downAlpha)
window.bind("<t>", toggleAlpha)
window.bind("l", lock)

window.mainloop()
