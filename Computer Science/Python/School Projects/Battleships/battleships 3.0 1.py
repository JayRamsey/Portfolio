import tkinter as tk
import sys

#Defining the constants that will be used for creating the game
GRID_OUTSIDE_PADDING = 100
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GRID_SIZE = 300
GRID_SPACES = 10
SPACE_SIZE = int(GRID_SIZE / GRID_SPACES)

run = True
mouseX = 0
mouseY = 0
phase = 0

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
        for i in range(len(self.squares)):
            if not playerDisplay.squares[self.squares[i][0]][self.squares[i][1]] != "light blue":
                self,squares = self.lastSquares
                
    
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
        self.canvas.place(x=x, y=y)
        
        self.update()

    def tempShow(self, squares, colour):
        for square in range(len(squares)):
            fillColour = colour
            row = square[0]
            column = square[1]
            self.canvas.create_rectangle(self.spaceSize * column, self.spaceSize * row,
                                             self.spaceSize * (column + 1), self.spaceSize * (row + 1),
                                             fill=fillColour)
            
    def update(self):
        
        for row in range(GRID_SPACES):
            for column in range(GRID_SPACES):
                match self.squares[row][column]:
                    case "empty":
                        fillColour = self.baseColour
                    case "ship":
                        fillColour = "gray"
                    case "cursor":
                        fillColour = "white"
                    case _:
                        fillColour = self.squares[row][column]
                        
                self.canvas.create_rectangle(self.spaceSize * column, self.spaceSize * row,
                                             self.spaceSize * (column + 1), self.spaceSize * (row + 1),
                                             fill=fillColour)
    
        window.update()

def mouseMove(event):
    x = event.x
    y = event.y

    global mouseX
    mouseX = x

    global mouseY
    mouseY = y
    

def displayPiece(selectedIndex, topLeft, orientation):
    ship = ships[selectedIndex]
    for square in range(ship.length):
        if orientation == "h":
            playerDisplay.squares[topLeft[0]][topLeft[1] + square] = "black"
        elif orientation == "v":
            playerDisplay.squares[topLeft[0] + square][topLeft[1]] = "black"

def rotate():
    if ships[0].orientation == "h":
        ships[0].orientation = "v"
        return
    elif ships[0].orientation == "v":
        ships[0].orientation = "h"
        return

def main():
    while run:
        playerDisplay.update()
        column, row = (mouseY - playerDisplay.x)//playerGrid.spaceSize, (mouseX - playerDisplay.y)//playerDisplay.spaceSize
        print(row, column)
        playerDisplay.tempShow([[row, column]], "black")

        
        

window = tk.Tk()
window.title("Battleships")
window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

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


window.mainloop()

