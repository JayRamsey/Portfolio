import tkinter as tk
import keyboard
import time
import pyautogui as pag

window = tk.Tk()
window.title("Auto-Typer")
SCREEN_WIDTH, SCREEN_HEIGHT = pag.size()

def press(key):
    keyboard.press(key)

def click(x, y):
    pag.click(x=x, y=x)

def typeString(startDelay=0, string="", delay=0.01, loops=1):
    shiftSymbols = '!"£$%^&*()<>?@:{}_'
    print("typing:", string)
    window.iconify()
    time.sleep(0.1 + startDelay)
    for i in range (loops):
        time.sleep(0.1)
        isInCommand = False
        for i in range(len(string)-1):
            char = string[i]
            print(char)
            if char == "<":
                print("checking for matching angle bracket")
                tempString = string[i:]
                try:
                    tempString = tempString[1:tempString.index(">")]
                    isInCommand = True
                except:
                    continue
                print("using command:", tempString)
                for key in tempString.split("+"):
                    press(key)
                for key in tempString.split("+"):
                    keyboard.release(key)
            if char == ">" and isInCommand:
                print("Command excecuted")
                isInCommand = False
            if isInCommand == False:
                if char.isupper() or char in shiftSymbols:
                    keyboard.press("shift")
                if char.islower() and char not in shiftSymbols:
                    keyboard.release("shift")
                if char not in "<>":
                    press(char)
                    time.sleep(delay)
                    
                    
        time.sleep(0.1)
        
    keyboard.release("shift")
    keyboard.release("ctrl")
    keyboard.release("alt")
    keyboard.release("shift")
    
    window.deiconify()

topFrame = tk.Frame(window)
topFrame.pack(side="top")

tk.Label(topFrame, text="Text to type").pack()
textEntry = tk.Text(topFrame, height=6)
textEntry.pack(padx=20, pady=5)


timeFrame = tk.Frame(window)
timeFrame.pack(side="left", padx=5, pady=20, expand=True, fill="x")

loopFrame = tk.Frame(window)
timeFrame.pack(side="left", padx=5, pady=20, expand=True, fill="x")

tk.Label(timeFrame, text="Start delay").pack(expand=True, fill="x")
startDelay = tk.Scale(timeFrame, from_=2, to=15, resolution=0.2, orient="horizontal")
startDelay.pack(padx=20, pady=5, expand=True, fill="x")

tk.Label(timeFrame, text="key press delay").pack(expand=True, fill="x")
keyDelay = tk.Scale(timeFrame, from_=0.02, to=1, resolution=0.01, orient="horizontal")
keyDelay.pack(padx=20, pady=5, expand=True, fill="x")

tk.Label(timeFrame, text="Number of times to loop").pack(expand=True, fill="x")
loopScale = tk.Scale(timeFrame, from_=1, to=1000, resolution=1, orient="horizontal")
loopScale.pack(padx=20, pady=5, expand=True, fill="x")



run = tk.Button(topFrame, text="Run auto-typer", command=lambda: typeString(startDelay.get(), textEntry.get("1.0", "end"), keyDelay.get(), loopScale.get()))
run.pack(padx=5, pady=5, side="bottom")

geometry = window.geometry()

# Parse the geometry string to extract positionX and positionY
window.mainloop()

