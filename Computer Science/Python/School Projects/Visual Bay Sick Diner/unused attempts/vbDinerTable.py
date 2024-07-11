

def getFileData():
    with open("vbDinerSaveData.txt", "r") as textFile:
        lines = [line.split(",") for line in textFile]
        
    return lines

def longest(data, topBar, sideBar):
    longest = 0
    
    for row in range(len(data)):
        for column in range(len(data[0])):
            dataSingle = str(data[row][column])
            if int(len(dataSingle)) > longest:
                longest = len(dataSingle)
                
    for column in range(len(topBar)):
        dataSingle = str(topBar[column])
        if int(len(dataSingle)) > longest:
            longest = len(dataSingle)
            
    for row in range(len(sideBar)):
        dataSingle = str(sideBar[row])
        if int(len(dataSingle)) > longest:
            longest = len(dataSingle)
            
    return longest

def addWhitespace(longest, dataSingle):
    whitespace = ""
    for i in range(longest + defaultDampingRight - len(dataSingle)):
        whitespace += " "
    whitespace += "│"
    return whitespace

def drawHorizontalBorder(rowStr, j, tableHeight):
    tableWidth = len(rowStr)
    borderRow = ""
        
    for i in range(tableWidth):
        #the middle columns from top to bottom
        if 1 < i + 1 < tableWidth and 1 <= j + 1 <= tableHeight or j == -1:
            if rowStr[i] == "│":
                if j == 0:
                    borderRow += "┬"
                elif j != -1:
                    borderRow += "┼"
                elif i != 0 and i + 1 != tableWidth: 
                    borderRow += "┴"
            else:
                borderRow += "─"

        #the left side
        if i == 0:
            if j == 0:
                borderRow += "┌"
            if j == -1:
                borderRow += "└"
            if 1 < j + 1 <= tableHeight:
                borderRow += "├"

        #the right side
        if i + 1 == tableWidth:
            if j == 0:
                borderRow += "┐"
            if j == -1:
                borderRow += "┘"
            if 1 < j + 1 <= tableHeight:
                borderRow += "┤"
        
    print(borderRow)

def draw(data, topBar, sideBar):
    print("\n")
    data.insert(0, topBar)
    tableHeight = len(data)
    longestItem = longest(data, topBar, sideBar)
    leftWhitespace = ""
    for i in range(defaultDampingLeft):
        leftWhitespace += " "
    for row in range(len(data)):
        sideData = str(sideBar[row])
        rowStr = ("│" + leftWhitespace + sideData + str(addWhitespace(longestItem, sideData)))
        for column in range(len(data[0])):
            dataSingle = str(data[row][column])
            whitespace = addWhitespace(longestItem, dataSingle)
            rowStr += " " + dataSingle + whitespace
            
        drawHorizontalBorder(rowStr, row, tableHeight)
        print(rowStr)

    drawHorizontalBorder(rowStr, -1, tableHeight)
    print("\n\n")


topBar = ["column 1", "column 2", "column 3", "column 4", "column 5"]
sideBar = ["", "row 1", "row 2", "row 3", "row 4", "row 5"]
data = getFileData()

defaultDampingLeft = 1
defaultDampingRight = 2

draw(data, topBar, sideBar)

while True:
    i = 1
