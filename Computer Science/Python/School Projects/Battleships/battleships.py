import tkinter as tk
import sys

screen = tk.Tk()

squareSize = 20
cellSpaceNS = 0
cellSpaceEW = 4
gridHorizontalPadding = squareSize * cellSpaceEW
gridVerticalPadding = squareSize * cellSpaceNS

pressedSquare = -1, -1

class playerDisplay:
    def __init__(self, row, column, colour):
        self.square = tk.Label(screen, bg=colour)

class gridButton:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.button = tk.Button(screen,
                                width=squareSize,
                                height=squareSize,
                                bg="light blue",
                                command=self.press)
        
        '''_, _, gridWidth, gridHeight = screen.grid_bbox(column, row)
        low = min(gridWidth, gridHeight)
        high = max(gridWidth, gridHeight)'''
        self.button.grid(row=row, column=column, padx=(0), pady=(0))
        
    def press(self):
        pressedSquare = self.row, self.column

class square:
    def __init__(self, partOf):
        self.row = None
        self.column = None
        self.parent = partOf

class ship:
    def __init__(self, name, length):
        self.segments = [square(name) for i in range(length)]
        self.name = name
        self.length = length
        self.health = length
        self.rotation = 0


def QUIT():
    screen.destroy()
    sys.exit()

pieces = [ship("Carrier", 5),
          ship("Battleship", 4),
          ship("cruiser", 3),
          ship("submarine", 3),
          ship("destroyer", 2)]

def checkSquare(row, column, gridSize, grid):
    if row >= 0 and row < gridSize and column >= 0 and column < gridSize and grid[row][column] == None:
        return True
    else:
        return False
        

def choosePlacements(gridSize, grid):
    screen.mainloop()
    print("please choose")
    while len(pieces) > 0:
        selectedPiece = pieces[0]
        while True:
            if pressedSquare != (-1, -1):
                break
        if selectedPiece.rotation == 0: #0 correlates to a horizontal rotation
            canPlace = True
            for i in range(selectedPiece.length):
                if not checkSquare(pressedSquare[0], pressedSquare[1] + i, gridSize, grid):
                    canPlace = False
            if canPlace:
                for i in range(selectedPiece):
                    grid[pressedSquare[0]][pressedSquare[1] + i]
        if selectedPiece.rotation == 1: #1 correlates to a vertical rotation
            canPlace = True
            for i in range(selectedPiece.length):
                if not checkSquare(pressedSquare[0] + i, pressedSquare[1], gridSize, grid):
                    canPlace = False
            if canPlace:
                for i in range(selectedPiece):
                    grid[pressedSquare[0]][pressedSquare[1] + i]
        
        

def rotate():
    if pieces[0].rotation == 1:
        pieces[0].rotation = 0
        return
    elif pieces[0].rotation == 0:
        pieces[0].rotation = 1
    
    
def gameMain():
    for row in range(gridSize):
        buttonGrid.append([])
        screen.rowconfigure(row, weight=1, uniform="")
        for column in range(gridSize):
            buttonGrid[row].append(gridButton(row, column))
            screen.columnconfigure(column, weight=1, uniform="")
    
def main():
    while True:
        gridSize = input("Enter grid size: ")
        try:
            gridSize = int(gridSize)
            break
        except:
            print("Please enter an integer.")
    
    playerGrid = [[None for i in range(gridSize)] for j in range(gridSize)]
    buttonGrid = []

    windowWidth = squareSize * gridSize + 2 * gridHorizontalPadding
    windowHeight = 40 * gridSize + 2 * gridVerticalPadding
    
    screen.maxsize(windowWidth, windowHeight)
    screen.minsize(windowWidth, windowHeight)
    
    quitButton = tk.Button(screen, text="QUIT", command=QUIT).grid(row=gridSize, column=gridSize-2, columnspan=2, sticky="we")
    rotateButton = tk.Button(screen, text="Rotate", command=rotate)
    startButton = tk.Button(screen, text="START", command=gameMain).grid(row = gridSize, column=gridSize//2, sticky="nesw", columnspan=gridSize%2, rowspan=2)
    
    screen.mainloop()
    
    playerGrid = choosePlacements(gridSize, playerGrid)

main()