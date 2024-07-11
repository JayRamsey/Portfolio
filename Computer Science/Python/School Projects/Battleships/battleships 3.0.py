import tkinter as tk
from tkinter import messagebox
import random
import winsound

#Defining the constants that will be used for creating the game
GRID_OUTSIDE_PADDING = 100
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GRID_SIZE = 300
GRID_SPACES = 10
SPACE_SIZE = int(GRID_SIZE / GRID_SPACES)
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#other values
run = True
mouseX = 0
mouseY = 0
phase = 0



#basic window settings
window = tk.Tk()
window.title("Battleships")
window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
window.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)

window.configure(bg="black")


def QUIT():
    window.destroy()
    quit

class ship:
    def __init__(self, length, name): #constructor for class ship
        self.orientation = "h"
        self.length = length
        self.name = name
        
    
#create a list containing all ships for enemy and player
ships = [ship(5, "Carrier"),
         ship(4, "Battleship"),
         ship(3, "Submarine"),
         ship(2, "Destroyer")]

enemyShips = [ship(5, "Carrier"),
              ship(4, "Battleship"),
              ship(3, "Submarine"),
              ship(2, "Destroyer")]

playerHealth = 0
enemyHealth = 0 #self explanatory

class grid: #the main grid class
    def __init__(self, x, y, size, passedShips):
        self.x = x
        self.y = y
        self.size = size
        self.baseColour = "light blue"
        self.spaceSize = int(size / GRID_SPACES)
        self.squares = [["empty" for i in range(GRID_SPACES)] for j in range(GRID_SPACES)]
        self.canvas = tk.Canvas(window, width=size, height=size, bg="black")
        self.rects = []
        self.canvas.place(x=x, y=y)
        self.ships = passedShips
        
        self.update(True)

    def tempShow(self, squares, colour):
        #temporarily displays something on the grid
        for square in squares:
            fillColour = colour
            row = square[0]
            column = square[1]
            self.canvas.create_rectangle(self.spaceSize * column, self.spaceSize * row,
                                             self.spaceSize * (column + 1), self.spaceSize * (row + 1),
                                             fill=fillColour,
                                             tag="square")
            
            window.update()
    

    #loops through the grids squares and displays each one
    def update(self, hidePieces):
        self.canvas.delete("square")
        for row in range(GRID_SPACES):
            for column in range(GRID_SPACES):
                match self.squares[row][column]:
                    #checks what the square is, and sets the fillColour accordingly.
                    case "empty":
                        fillColour = self.baseColour
                    case "ship":
                        if hidePieces:
                            fillColour = self.baseColour
                        else:
                            fillColour = "gray"
                    case "hit":
                        fillColour = "red"
                    case "miss":
                        fillColour = "white"
                    case _:
                        fillColour = self.squares[row][column]
                
                #draws the square
                self.canvas.create_rectangle(self.spaceSize * column, self.spaceSize * row,
                                             self.spaceSize * (column + 1), self.spaceSize * (row + 1),
                                             fill=fillColour,
                                             tag="square")
        window.update() #self explanatory
    
    #tries to place a ship on a passed through square
    def place(self, row, column):
        if len(self.ships) > 0:
            ship = self.ships[0]
            canPlace = True
            if 0 <= row < GRID_SPACES  and 0 <= column < GRID_SPACES:
                for square in range(ship.length):
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
            else:
                canPlace = False
            #if the squares in the select places are empty, then set the values to signify that there are ship segments there
            if canPlace:
                for square in range(ship.length):
                    if ship.orientation == "h":
                        self.squares[row][column + square] = "ship"
                    if ship.orientation == "v":
                        self.squares[row + square][column] = "ship"
                del self.ships[0]

    #resets the grid
    def resetSquares(self):
        self.squares = [["empty" for i in range(GRID_SPACES)] for j in range(GRID_SPACES)]
    
    #the function bound to a mouse click on the canvas in the placing stage of the game
    def clickPlace(self, mouse):
        column, row = (mouse.x - self.x)//self.spaceSize + 3, (mouse.y - self.y)//self.spaceSize + 3
        self.place(row, column)

def changeCoord(row):
    return LETTERS[GRID_SPACES - 1 - row]

#captures mouse movement
def mouseMove(event):
    x = event.x
    y = event.y
    global mouseX
    mouseX = x
    global mouseY
    mouseY = y


def resetShips(): #self explanatory
    playerDisplay.ships = [ship(5, "Carrier"),
                        ship(4, "Battleship"),
                        ship(3, "Submarine"),
                        ship(2, "Destroyer")]

    enemyDisplay.ships = [ship(5, "Carrier"),
                        ship(4, "Battleship"),
                        ship(3, "Submarine"),
                        ship(2, "Destroyer")]

 #self explanatory- bound to rotate button
def rotate():
    if len(ships) > 0:
        if ships[0].orientation == "h":
            ships[0].orientation = "v"
            return
        elif ships[0].orientation == "v":
            ships[0].orientation = "h"
            return

successfulAttack = False

#the procedure that is called when the player clicks on the enemy grid, after the placing phase
def playerAttack(mouse):
    column, row = (mouseX - enemyDisplay.x)//enemyDisplay.spaceSize + 20, (mouseY - enemyDisplay.y)//enemyDisplay.spaceSize + 3
    try:
        square = enemyDisplay.squares[row][column]
        letter = changeCoord(row)
        match square: #self explanatory
            case "hit":
                return
            case "ship":
                enemyDisplay.squares[row][column] = "hit" #self explanatory
                global enemyHealth
                enemyHealth -= 1
                global successfulAttack
                successfulAttack = True
                return
            case "empty":
                enemyDisplay.squares[row][column] = "miss" #self explanatory
                successfulAttack = True
                return
            case "miss": #self explanatory
                pass
                
    except:
        global succesfulAttack
        succesfulAttack = False #tells the game wether or not a successful attack has occurred
        return
    
def game():
    
    #resetting health values so when game restarts they are as they should be
    global playerHealth
    global enemyHealth
    playerHealth = 0
    playerHealth = 0
    for i in range(len(playerDisplay.ships)):
        enemyHealth += enemyDisplay.ships[i].length
        playerHealth += playerDisplay.ships[i].length
    
    #randomly tries to place enemy ships until there are none left to place
    while len(enemyDisplay.ships) > 0:
        ranOrien = random.choice(["h", "v"])
        ranRow = random.randint(0, GRID_SPACES)
        ranColumn = random.randint(0, GRID_SPACES)

        enemyDisplay.ships[0].orientation = ranOrien
        try:
            enemyDisplay.place(ranRow, ranColumn)
        except:
            pass
    
    resetShips()

    playerDisplay.canvas.bind("<Button-1>", playerDisplay.clickPlace) #binds the clickPlace procedure to a click on the player canvas
    bannerText = "Choose your ship locations:"
    bannerWidth = 43
    info = tk.Label(window,
                      text=bannerText,
                      font=("Helvetica", 12),
                      width=bannerWidth,
                      justify="left",
                      height = 8,
                      bg="black",
                      fg="white",
                      anchor="nw",
                      highlightbackground="white",
                      highlightthickness=2)

    info.place(x=playerDisplay.x, y=WINDOW_HEIGHT - 180) #self explanatory

    while run:
        window.update()
        lastSquareHover = [0, 0]
        #placing user ships
        rotateButton.place(x=playerDisplay.x + playerDisplay.size + 5, y=playerDisplay.y)
        while len(playerDisplay.ships) > 0:
            column, row = (mouseX - playerDisplay.x)//playerDisplay.spaceSize + 3, (mouseY - playerDisplay.y)//playerDisplay.spaceSize + 3 #turns the mouse position into column and rows
            if lastSquareHover != [row, column]:
                playerDisplay.update(False)
                lastSquareHover = [row, column]
            try:
                for square in range(playerDisplay.ships[0].length):
                    if playerDisplay.ships[0].orientation == "h":
                        try:
                            playerDisplay.tempShow([[row, column + square]], "white") #shows a preview of where it will place a ship
                        except:
                            pass
                    if playerDisplay.ships[0].orientation == "v":
                        try:
                            playerDisplay.tempShow([[row + square, column]], "white") #shows a preview of where it will place a ship.
                        except:
                            pass
            except:
                playerDisplay.update(False)
        #user finished placing ships.

        rotateButton.destroy() #self explanatory
        enemyDisplay.canvas.bind("<Button-1>", playerAttack) #self explanatory
        
        squaresNotAttackedEnemy = [[i, j] for i in range(GRID_SPACES) for j in range(GRID_SPACES)]

        playerDisplay.update(False) #self explanatory

        info["text"] = "Click on the squares to strategically destroy the\nenemy's ships!"
        info.update()

        #attack loop
        while enemyHealth > 0 and playerHealth > 0:
            global successfulAttack
            successfulAttack = False
            while successfulAttack == False:
                column, row = (mouseX - enemyDisplay.x)//enemyDisplay.spaceSize + 20, (mouseY - enemyDisplay.y)//enemyDisplay.spaceSize + 3 #gets hovered column and row.
                if lastSquareHover != [row, column]:
                    enemyDisplay.update(True)
                    lastSquareHover = [row, column]
                try:
                    enemyDisplay.tempShow([[row, column]], "red") #shows the current cursor position on the grid.
                except:
                    pass
                if successfulAttack == True:
                    break
            enemyDisplay.update(True) #the value of "True" passed through means that ships will be hidden.
            
            attackCoors = random.choice(squaresNotAttackedEnemy) #chooses a random square that has not been attacked to attack.
            del squaresNotAttackedEnemy[squaresNotAttackedEnemy.index(attackCoors)]
            attackRow = attackCoors[0]
            attackColumn = attackCoors[1]
            
            letter = changeCoord(attackRow)
            
            match playerDisplay.squares[attackRow][attackColumn]:
                 #checks to see of the enemy hit or missed a player ship
                case "ship":
                    playerDisplay.squares[attackRow][attackColumn] = "hit"
                    winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
                    playerHealth -= 1
                case "empty":
                    playerDisplay.squares[attackRow][attackColumn] = "miss"
            playerDisplay.update(False)
        
        #checks to see who won, and displays relevant message
        if enemyHealth <= 0:
            response = messagebox.askyesno(title="You won!", message="Congratulations you defeated all the enemy ships! Would you like to restart? (No to quit)")
        if playerHealth <= 0:
            winsound.PlaySound("lose.wav", winsound.SND_ASYNC)
            response = messagebox.askyesno(title="You lost!", message=f"The enemy sunk all your ships, you still had {enemyHealth} squares to find! Would you like to restart? (No to quit)")
        
        #returns the value that the player gave back of wether to restart of not.
        if response:
            return True
        else:
            return False
            

playerDisplay = grid(GRID_OUTSIDE_PADDING, #creates an instance of the grid class for the player grid.
                     GRID_OUTSIDE_PADDING,
                     GRID_SIZE, ships)

enemyDisplay = grid(WINDOW_WIDTH - GRID_OUTSIDE_PADDING - GRID_SIZE, #creates an instance of the grid class for the enemy grid.
                    GRID_OUTSIDE_PADDING,
                    GRID_SIZE, enemyShips)

#create and place a quit button.
quitButton= tk.Button(window, text="QUIT", command=QUIT, fg="white", bg="black", width=10, height=3)
quitButton.place(x=WINDOW_WIDTH - 100, y=20)

rotateButton = tk.Button(window, text="Rotate", command=rotate)
window.bind("<Motion>", mouseMove)

restart = True
while restart:
    #if the player wishes not to restart it keeps calling the game
    playerDisplay.resetSquares()
    playerDisplay.update(True)
    enemyDisplay.resetSquares()
    enemyDisplay.update(False)
    restart = game()
    resetShips()

QUIT() #if not restarting, quit the game.

#sorry about the global variables the way I had done most of the program and the amount I have done it meant it was way to hard to undo, i'll adopt a different style in next projects so I don't use any!