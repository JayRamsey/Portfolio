import random
import turtle

gridSize = 50

grid = [[1 for i in range(gridSize)] for j in range(gridSize)]
grid[1][1] = 0

def isFull():
    isFull = True
    for column in range(gridSize):
        for row in range(gridSize):
            if grid[row][column] == 0:
                for yOffset in range(-2, 3):
                    if yOffset == 2 or yOffset == -2:
                        for xOffset in range(-2, 3):
                            if xOffset == -2 or xOffset == 2:
                                if  gridSize > row + yOffset >= 0 and gridSize > column + xOffset >= 0:
                                    if grid[row + yOffset][column + xOffset] == 1:
                                        isFull = False
                                    
    return isFull

def getBranchPos():
    for column in range(gridSize):
        for row in range(gridSize):
            if grid[row][column] == 0:
                for yOffset in range(-2, 3):
                    if yOffset == 2 or yOffset == -2:
                        for xOffset in range(-2, 3):
                            if xOffset == -2 or xOffset == 2:
                                if gridSize > row + yOffset >= 0 and gridSize > column + xOffset >= 0:
                                    if grid[row + yOffset][column + xOffset] == 1:
                                        return row, column

def chooseDirection(pos):
    possibleMoves = []
    if 0 <= pos[0] - 2 < gridSize and 0 <= pos[1] - 2 < gridSize:
        if grid[pos[0] - 2][pos[1] - 2] == :
            possibleMoves.append([-2, -2])
    if 0 <= pos[0] - 2 < gridSize:
        
    
    
    return move
            

def main():
    while not isFull():
        print(isFull())
        currentPos = getBranchPos()
        direction = chooseDirection(currentPos)
        
        
main()









        