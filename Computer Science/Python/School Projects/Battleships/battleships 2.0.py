import tkinter as tk
import sys

GAME_NAME = "Battleships"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
OBJECT_SIZE = 40
GRID_SIZE = 10

bgColour = "light blue"

class pickButton:
    def __init__(self, row, column):
        self.button= tk.Button(window, command=self.command, bg="light blue", width=OBJECT_SIZE, height=OBJECT_SIZE)
        self.row = row
        self.column = column
        self.button.grid(row=self.row, column=self.column, padx=1, pady=1)
        
    def command(self):
        pass

class square:
    def __init__(self, row, column):
        self.row = None
        self.column = None
        
        canvas.create_rectangle(column * OBJECT_SIZE - OBJECT_SIZE / 2,
                                row * OBJECT_SIZE - OBJECT_SIZE / 2,
                                column * OBJECT_SIZE + OBJECT_SIZE / 2,
                                row * OBJECT_SIZE + OBJECT_SIZE / 2,
                                fill="black")
        
class ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.health = length
        self.rotation = 0

pieces = [ship("Carrier", 5),
          ship("Battleship", 4),
          ship("cruiser", 3),
          ship("submarine", 3),
          ship("destroyer", 2)]


def QUIT():
    window.destroy()
    sys.exit()
    
def playerTurn():
    pass

def computerTurn():
    pass

def pickPlaces():
    rotateButton = tk.Button(window, text="Rotate")
    rotateButton.grid(row=GRID_SIZE, column=0)
    buttons = []
    for row in range(GRID_SIZE):
        buttons.append([])
        for column in range(GRID_SIZE):
            buttons[row].append(pickButton(row, column))
    
    while len(pieces) > 0:
        window.update()

window = tk.Tk()
window.title(GAME_NAME)
window.resizable(False, False)

canvas = tk.Canvas(window, bg=bgColour, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

for i in range(GRID_SIZE * 2):
    window.rowconfigure(i, weight=1)
    window.columnconfigure(i, weight = 1)
    

start = tk.Button(window, command=pickPlaces, text="START")
start.place(x=WINDOW_WIDTH / 2, y=WINDOW_HEIGHT / 2)

window.mainloop()
