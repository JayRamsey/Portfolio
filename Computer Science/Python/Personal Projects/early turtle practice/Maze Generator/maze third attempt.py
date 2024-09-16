import turtle
import random

mazeSize = 100
gridSize = mazeSize - 1
topLeft = mazeSize /-2
turtle.clear()

turtleMulti = 5
turtle.color("white")
turtle.speed(0)
turtleWidth = turtleMulti * 0.85
turtle.width(turtleWidth)

turtle.penup()
turtle.goto(topLeft * turtleMulti, -topLeft * turtleMulti)
turtle.pendown()

wn = turtle.Screen()
wn.bgcolor("black")

grid = [[None for i in range(mazeSize)] for j in range(mazeSize)]
grid[0][0] = "start"
grid[gridSize][gridSize] = "end"

def isFull():
    for i in range(mazeSize):
        for j in range(mazeSize):
            if grid[i][j] is None:
                return False
    return True

def getChoices(row, column):
    choices = []
    if grid[row][column - 1] is None or grid[row][column - 1] == "end":
        if column != 0:
            choices.append("l")
    if column != gridSize:
        if grid[row][column + 1] is None or grid[row][column + 1] == "end":
            choices.append("r")
    if grid[row - 1][column] is None or grid[row - 1][column] == "end":
        if row != 0:
            choices.append("u")
    if row != gridSize:
        if grid[row + 1][column] is None or grid[row + 1][column] == "end":
            choices.append("d")
    return choices
    
def findEmpty():
    for row in range(mazeSize):
        for column in range(mazeSize):
            if grid[row][column] is not None and grid[row][column] != "end":
                if len(getChoices(row, column)) > 0:
                    return row, column

def draw(row, column):
    moves = 0
    turtle.penup()
    turtle.goto((topLeft + column) * turtleMulti, (topLeft + row) * -turtleMulti)
    turtle.pendown()
    
    choices = getChoices(row, column)
    if len(choices) > 0:
        choice = choices[random.randint(0, len(choices) - 1)]
        match choice:
            case "l":
                column -= 1
            case "r":
                column += 1
            case "u":
                row -= 1
            case "d":
                row += 1
        turtle.goto((topLeft + column) * turtleMulti, (topLeft + row) * -turtleMulti)
        moves += 1
        
        if grid[row][column] == None:
            grid[row][column] = "1" 
            grid[gridSize][gridSize] = "end"
        print(grid)

    else:
        row, column = findEmpty()
        draw(row, column)

    if not isFull():
        draw(row, column)
    

draw(0, 0)
turtle.done()
while True:
    input()    
