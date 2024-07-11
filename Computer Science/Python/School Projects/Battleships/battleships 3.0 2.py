import tkinter as tk
import sys
import time

#Defining the constants that will be used for creating the game
GRID_OUTSIDE_PADDING = 100
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GRID_SIZE = 300
GRID_SPACES = 10
SPACE_SIZE = int(GRID_SIZE / GRID_SPACES)
SHIP_LENGTHS = [5, 4, 3, 2]


run = True
mouseX = 0
mouseY = 0
phase = 0

playerHealth = 0
enemyHealth = 0
for i in range(len(SHIP_LENGTHS)):
    enemyHealth += SHIP_LENGTHS[i]
    playerHealth += SHIP_LENGTHS[i]

def QUIT():
    window.destroy()
    sys.exit()

class ship:
    def __init__(self, length, name):
        self.orientation = "h"
        self.length = length
        self.name = name
        squares = [(None, None) for i in range(length)]
        self.lastSquares = squares
        
    def checkCollisions(self):
        pass
                
    
#create a list containing all ships
ships = [ship(5, "Carrier"),
         ship(4, "Battleship"),
         ship(3, "Submarine"),
         ship(2, "Destroyer")]
        
class grid:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.baseColour = "light blue"
        self.spaceSize = int(size / GRID_SPACES)
        self.squares = [["empty" for i in range(GRID_SPACES)] for j in range(GRID_SPACES)]
        self.canvas = tk.Canvas(window, width=size, height=size, bg="black")
        self.rects = []
        self.canvas.place(x=x, y=y)
        
        self.update()

    def tempShow(self, squares, colour):
        for square in squares:
            fillColour = colour
            row = square[0]
            column = square[1]
            self.canvas.create_rectangle(self.spaceSize * column, self.spaceSize * row,
                                             self.spaceSize * (column + 1), self.spaceSize * (row + 1),
                                             fill=fillColour,
                                             tag="square")
            
            window.update()
            
    def update(self):
        self.canvas.delete("square")
        for row in range(GRID_SPACES):
            for column in range(GRID_SPACES):
                match self.squares[row][column]:
                    case "empty":
                        fillColour = self.baseColour
                    case "ship":
                        fillColour = "gray"
                    case _:
                        fillColour = self.squares[row][column]
                        
                self.canvas.create_rectangle(self.spaceSize * column, self.spaceSize * row,
                                             self.spaceSize * (column + 1), self.spaceSize * (row + 1),
                                             fill=fillColour,
                                             tag="square")
        window.update()
    
    def place(self, mouse):
        if len(ships) > 0:
            ship = ships[0]
            column, row = (mouse.x - self.x)//self.spaceSize + 3, (mouse.y - self.y)//self.spaceSize + 3
            canPlace = True
            for square in range(ships[0].length):
                if ship.orientation == "h":
                    try:
                        if self.squares[row][column + square] != "empty":
                           canPlace = False 
                    except:
                        return
                if ship.orientation == "v":
                    try:
                        if self.squares[row + square][column] != "empty":
                           canPlace = False
                    except:
                        return
            if canPlace:
                for square in range(ships[0].length):
                    if ship.orientation == "h":
                        self.squares[row][column + square] = "ship"
                    if ship.orientation == "v":
                        self.squares[row + square][column] = "ship"
                del ships[0]
        
def mouseMove(event):
    x = event.x
    y = event.y
    global mouseX
    mouseX = x
    global mouseY
    mouseY = y

def rotate():
    if len(ships) > 0:
        if ships[0].orientation == "h":
            ships[0].orientation = "v"
            return
        elif ships[0].orientation == "v":
            ships[0].orientation = "h"
            return

def main():
    playerDisplay.canvas.bind("<Button-1>", playerDisplay.place)
    bannerText = "Choose your ship locations:"
    bannerWidth = 43
    banner = tk.Label(window,
                      text=bannerText,
                      font=("Helvetica", 12),
                      width=bannerWidth,
                      height = 8,
                      bg="black",
                      fg="white",
                      anchor="nw",
                      highlightbackground="white",
                      highlightthickness=2)
    
    banner.place(x=playerDisplay.x, y=WINDOW_HEIGHT - 180)
    while run:
        window.update()
        lastSquareHover = [0, 0]
        
        while len(ships) > 0:
            column, row = (mouseX - playerDisplay.x)//playerDisplay.spaceSize + 3, (mouseY - playerDisplay.y)//playerDisplay.spaceSize + 3
            if lastSquareHover != [row, column]:
                playerDisplay.update()
                lastSquareHover = [row, column]
            try:
                for square in range(ships[0].length):
                    if ships[0].orientation == "h":
                        try:
                            '''tempColour = "green"
                            if playerDisplay.squares[row][column + square] != "empty":
                                tempColour = "red"'''
                            playerDisplay.tempShow([[row, column + square]], "white")
                            
                        except:
                            pass
                    if ships[0].orientation == "v":
                        try:
                            '''tempColour = "green"
                            if playerDisplay.squares[row + square][column] != "empty":
                                tempColour = "red"'''
                            playerDisplay.tempShow([[row + square, column]], "white")
                            
                        except:
                            pass
            except:
                playerDisplay.update()
        rotateButton.destroy()
        while True:
            column, row = (mouseX - enemyDisplay.x)//enemyDisplay.spaceSize - 3, (mouseY - enemyDisplay.y)//enemyDisplay.spaceSize - 3
            if lastSquareHover != [row, column]:
                enemyDisplay.update()
                lastSquareHover = [row, column]
            try:
                enemyDisplay.tempShow([[row, column]], "red")
            except:
                pass

window = tk.Tk()
window.title("Battleships")
window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

window.configure(bg="black")

playerDisplay = grid(GRID_OUTSIDE_PADDING,
                     GRID_OUTSIDE_PADDING,
                     GRID_SIZE)

enemyDisplay = grid(WINDOW_WIDTH - GRID_OUTSIDE_PADDING - GRID_SIZE,
                    GRID_OUTSIDE_PADDING,
                    GRID_SIZE)

quitButton= tk.Button(window, text="QUIT", command=QUIT, fg="white", bg="black", width=10, height=3)
quitButton.place(x=WINDOW_WIDTH - 100, y=20)

rotateButton = tk.Button(window, text="Rotate", command=rotate)
rotateButton.pack()
window.bind("<Motion>", mouseMove)

main()

window.mainloop()
