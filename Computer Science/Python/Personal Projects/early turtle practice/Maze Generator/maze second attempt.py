import random
import turtle
import time


maze = turtle.Turtle()
maze.speed(0)
maze.width(10)
maze.color("white")

turtleMultiplier = 20
gridSize = 30
topLeft = ((gridSize / -2) - 1) * turtleMultiplier
maze.penup()
maze.goto(topLeft, -topLeft)
maze.pendown()

wn = turtle.Screen()
wn.bgcolor("black")



time.sleep(1)


'''maze.forward((gridSize + 2) * turtleMultiplier)
maze.right(90)
maze.forward((gridSize + 1) * turtleMultiplier)
maze.right(90)
maze.forward((gridSize + 1) * turtleMultiplier)
maze.right(90)
maze.forward((gridSize + 1) * turtleMultiplier)
maze.right(90)'''



maze.penup()
turtle.setheading(0)
turtle.forward(turtleMultiplier)
turtle.pendown()

time.sleep(1)

grid = [[[[None, None, None],
          [None, 0, None],
          [None, None, None]] for i in range(gridSize)] for i in range(gridSize)]

'''for row in range(gridSize):
    for column in range(gridSize):
        if row == 0:
            for i in range(3):
                grid[row][column][0][i] = "wall"
        if row == gridSize - 1:
            for i in range(3):
                grid[row][column][2][i] = "wall"
        if column == 0:
            for i in range(3):
                grid[row][column][i][0] = "wall"
        if column == gridSize - 1:
            for i in range(3):
                grid[row][column][i][2] = "wall"'''

grid[0][0][1][1] = 1

def hasOptions(currentXPos, currentYPos):
    options = 0
    if currentXPos > 0 and grid[currentYPos][currentXPos - 1][1][1] == 0 and 0 < currentYPos < gridSize - 1:
        options += 1
    if currentXPos < gridSize - 1 and grid[currentYPos][currentXPos + 1][1][1] == 0:
        options += 1
    if currentYPos > 1 and grid[currentYPos - 1][currentXPos][1][1] == 0 and 0 < currentXPos < gridSize - 1:
        options += 1
    if currentYPos < gridSize - 1 and grid[currentYPos + 1][currentXPos][1][1] == 0:
        options += 1
    
    if options > 0:
        return True
    else:
        return False
    
    

def isSquare(x, y):
    if grid[y][x][1][1] != 1:
        return False
    else:
        return True

def isNotFull():
    countSquares = 0
    for y in range(gridSize):
        for x in range(gridSize):
            if isSquare(x, y):
                countSquares += 1
    amountNeeded = gridSize ** 2
    
    if countSquares < amountNeeded:
        return True
    else:
        return False

def findEmpty():
    squares = []
    for x in range(0, gridSize):
        for y in range(0, gridSize):
            if grid[y][x][1][1] == 1 and hasOptions(x, y):
                squares.append([x, y])
        return squares[random.randint(0, len(squares))]
        
def main():
    currentXPos = 0
    currentYPos = 0
    while isNotFull:
        maze.pendown()
        optionsList = []
        if 0 < currentXPos and grid[currentYPos][currentXPos - 1][1][1] == 0:
            optionsList.append("left")
        if currentXPos < gridSize - 1 and grid[currentYPos][currentXPos + 1][1][1] == 0:
            optionsList.append("right")
        if 0 < currentYPos and grid[currentYPos - 1][currentXPos][1][1] == 0:
            optionsList.append("up")
        if currentYPos < gridSize - 1 and grid[currentYPos + 1][currentXPos][1][1] == 0:
            optionsList.append("down")
        
        if len(optionsList) > 0:
            try:
                n = random.randint(0, len(optionsList) - 1)
            except:
                n = 0
            chosen = optionsList[n]
        else:
            nextPathStart = findEmpty()
            maze.penup()
            currentXPos = nextPathStart[0]
            currentYPos = nextPathStart[1]
            maze.goto(topLeft + (currentXPos * turtleMultiplier), - topLeft + (-currentYPos * turtleMultiplier))
            maze.pendown()
        
        
        match chosen:
            case "left":
                if currentXPos > 0:
                    grid[currentYPos][currentXPos][1][1] = 1
                    grid[currentYPos][currentXPos][1][0] = "l"
                    grid[currentYPos][currentXPos - 1][1][1] = 1
                    grid[currentYPos][currentXPos - 1][1][2] = "l"
                    currentXPos -= 1
            case "right":
                if currentXPos < gridSize - 1:
                    grid[currentYPos][currentXPos][1][1] = 1
                    grid[currentYPos][currentXPos][1][2] = "l"
                    grid[currentYPos][currentXPos + 1][1][1] = 1
                    grid[currentYPos][currentXPos + 1][1][0] = "l"
                    currentXPos += 1
            case "up":
                if currentYPos > 1:
                    grid[currentYPos][currentXPos][1][1] = 1
                    grid[currentYPos][currentXPos][0][1] = "l"
                    grid[currentYPos - 1][currentXPos][1][1] = 1
                    grid[currentYPos - 1][currentXPos][2][1] = "l"
                    currentYPos -= 1
            case "down":
                if currentYPos < gridSize - 1:    
                    grid[currentYPos][currentXPos][1][1] = 1
                    grid[currentYPos][currentXPos][2][1] = "l"
                    grid[currentYPos + 1][currentXPos][1][1] = 1
                    grid[currentYPos + 1][currentXPos][0][1] = "l"
                    currentYPos += 1

        print(currentXPos, currentYPos)
        maze.goto(topLeft + (currentXPos * turtleMultiplier), -topLeft + (-currentYPos * turtleMultiplier))
    
main()

turtle.done