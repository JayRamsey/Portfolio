import datetime #import the datetime module which is used to get the current date / time

def getFileData():
    try:
        with open("vbDinerSaveData.txt", "r") as textFile: #loop through the save data file and store it in a list
            lines = [line for line in textFile]
        return lines
    except:
        print("Error! File Not Found")
        
def saveFileData(dataRefs):
    try:
        with open("vbDinerSaveData.txt", "w") as textFile: #write the list onto the file
            for i in range(len(dataRefs)):
                line = dataRefs[i]
                textFile.write(line)
        print("information succesfully saved\n")
    except FileNotFoundError:
        print("Error! File Not Found")
    except IOError as error:
        print(f"An unexpected error occured: {error}")
        
#define various variables which are used through the program
defaultDampingLeft = 1
defaultDampingRight = 2
topBar = ["ORDER TIME", "NUMBER OF GUESTS", "ORDERS", "WAITER", "DATE"]
sideBar = ["TABLE NUMBER", "1", "2", "3", "4", "5"]
dataRefs = getFileData()

def charCheck(string):
    illegalCharsStr = ' /%\*#$"!@<>~/{}[]-_=+^&¬`()?' #all the "illegal" characters
    allowed = True
    for i in range(len(string)):
        if string[i] in illegalCharsStr: #loops through the parameter string and checks if it contains any of the illegal characters
            allowed = False
    if not allowed:
        print("Some characters you entered were not allowed\n")
    return allowed
    
def longest(data, topBar, sideBar):
    #loops through all the arrays/ lists used in the table and gets the length of the longest string contained
    longest = 0
    for row in range(len(data)):
        for column in range(len(data[0])):
            dataSingle = str(data[row][column]) #loops through the table data
            if int(len(dataSingle)) > longest:
                longest = len(dataSingle)
                
    for column in range(len(topBar)):
        dataSingle = str(topBar[column-1]) #loops through the top bar of the table
        if int(len(dataSingle)) > longest:
            longest = len(dataSingle)
            
    for row in range(len(sideBar)):
        dataSingle = str(sideBar[row]) #loops through the side bar of the table
        if int(len(dataSingle)) > longest:
            longest = len(dataSingle)
            
    return longest

def addWhitespace(longest, dataSingle):
    whitespace = ""
    for i in range(longest + defaultDampingRight - len(dataSingle)): #pads out items with spaces to make sure the table columns line up
        whitespace += " "
    whitespace += "│"
    return whitespace

def drawHorizontalBorder(rowStr, j, tableHeight):
    tableWidth = len(rowStr)
    borderRow = ""
        
    for i in range(tableWidth):
        #the middle columns from top to bottom
        if 1 < i + 1 < tableWidth and 1 <= j + 1 <= tableHeight or j == -1:
            '''depending on the iteration of the loop and the corresponding character
            in the previous row it adds the corresponding character for the box'''#########
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

def table():
    data = getDataFromRefs()
    draw(data, topBar, sideBar) #initiates the table

def draw(data, topBar, sideBar):
    print("\n")
    data[0] = topBar
    tableHeight = len(data)
    longestItem = longest(data, topBar, sideBar) #calls "longest" and gets the longest item
    leftWhitespace = ""
    for i in range(defaultDampingLeft):
        leftWhitespace += " "
    for row in range(len(data)):
        sideData = str(sideBar[row])
        rowStr = ("│" + leftWhitespace + sideData + str(addWhitespace(longestItem, sideData))) 
        for column in range(len(data[0])):
            dataSingle = str(data[row][column-1])
            whitespace = addWhitespace(longestItem, dataSingle) #adds the correct amount of whitespace for the given string
            rowStr += " " + dataSingle + whitespace #concatenates all of the rows information into one string
            
        drawHorizontalBorder(rowStr, row, tableHeight)
        print(rowStr) #outputs the row

    drawHorizontalBorder(rowStr, -1, tableHeight)
    print("\n\n")

def tableCheck(table):
    if dataRefs[table - 1] == "null\n": #check if the tale is free or not
        return True
    else:
        return False
    
def seatGuestsAndOrder():
    #define all the starting variables
    monthList = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC"]
    guestNum = 0
    orders = []
    tableSatAt = "null"
    waiterInitials = ""

    #get the table to seat at, validating and checking if the table is free
    while True:
        tableSatAt = input("Enter table to seat guests at: ")
        if tableSatAt.isdigit():
            try:
                tableSatAt = int(tableSatAt)
            except ValueError:
                tableSatAt = 0
            if 0 < tableSatAt < 6:
                if tableCheck(tableSatAt):
                    #table number is valid
                    break
                else:
                    print("Table is not free\n")
            else:
                print("Table does not exist\n")
        else:
            print("Please enter a valid value\n")

    #get the number of guests and validate
    while True:
        guestNum = input("Enter number of guests: ")
        if guestNum.isdigit():
            guestNum = int(guestNum)
            if 0 < guestNum < 6:
                break
            else:
                print("Please enter a valid number of guests\n")
        else:
            print("Please enter a number\n")


    print("‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗\n")
    print("Order types are:\n   1. Standard (£8)\n   2. premium (£12)\n   3. Deluxe (£15)\n")
    for i in range(guestNum): #loop for each guest and get the order for each one
        while True:
            print("Enter order type for guest number", str(i+1) + ": ")
            order = input("")
            match order:
                case "1":
                    orders.append("stan")
                    break
                case "2":
                    orders.append("prem")
                    break
                case "3":
                    orders.append("delu")
                    break
                case _:
                    print("Please enter a valid value\n")
    while True:
        waiterInitials = input("Enter waiter initials: ") #get the waiters initials and validate
        if len(waiterInitials) != 2:
               print("Initials need to be 2 letter long\n")
        if charCheck(waiterInitials) == True and len(waiterInitials) == 2:
            break

    orderString = ""
    for i in range(guestNum):
        orderString += orders[i] #put all the orders together in the correct format
        if i < guestNum - 1:
            orderString += "-"
    orderString += " "

    print("‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗\n")
    
    now = datetime.datetime.now() #use the datetime module to get the month and day
    time = now.strftime("%H:%M:%S")
    day = str(now.day)
    month = monthList[now.month - 1]

    orderRef = orderString + str(tableSatAt) + str(guestNum) + day + month + waiterInitials.upper() + " " + time + "\n" #concatenate all the information into the same string
    dataRefs[tableSatAt - 1] = orderRef
    saveFileData(dataRefs)

    print("\n")

#turns each booking reference into readable data for the table
def getDataFromRefs():
    monthList = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC"]
    guests = []
    date = []
    waiter = []
    data = []
    times = []
    dataTemp = []
    for i in range(len(dataRefs)):
        dataTemp.append(dataRefs[i].split()) #seperates the orders from the ref
    for i in range(len(dataTemp)):
        if len(dataTemp[i]) == 1:#reads the number of guests from the reference
            guests.append("0")
        else:
            guests.append(dataTemp[i][1][1])
            
    for i in range(len(dataTemp)):
        month = ""
        if len(dataTemp[i]) == 1: 
            date.append("N/A")
        else:
            #reads the date off of the order reference
            month = str(monthList.index(dataTemp[i][1][4:7]))   
            if len(month) == 1:
                month = "0" + month
            date.append(dataTemp[i][1][2:4] + "/" + month)
        if len(date[i]) == 4:
            date[i] = "0" + date[i]
    for i in range(len(dataTemp)):
        if len(dataTemp[i]) == 1:
            times.append("N/A")
        else:
            #reads the time off of saved data
            times.append(dataTemp[i][2])
            
    for i in range(len(dataTemp)):#gets the waiters initials
        if len(dataTemp[i]) == 1:
            waiter.append("None")
        else:
            waiter.append(dataTemp[i][1][7:10])
    data.append([])
    for i in range(len(dataTemp)):
        data.append([times[i], guests[i], dataTemp[i][0], waiter[i], date[i]])#creates an array from the data grabbed off the references
    return(data)
            
def getReceipt():
    endFunct = False
    while True:
        hasGotAnswer = False
        #ask which table you want to get the receipt for
        tableToCharge = input("Enter table to get receipt for: ")
        if tableToCharge.isdigit():
            tableToCharge = int(tableToCharge)
            if 0 < tableToCharge < 6:
                if not tableCheck(tableToCharge):
                    while True:
                        #two step verification
                        inputString = "Are you sure you want to charge table " + str(tableToCharge) + "? (Y or N): "
                        yOrN = input(inputString)
                        if yOrN.lower() == "y" or yOrN.lower() == "n":
                            hasGotAnswer = True
                            break
                        else:
                            print("Please enter a valid response\n")
                else:
                    print("Requested table is empty\n")
            else:
                print("Please enter a valid table number")
        else:
            print("Please enter a number")
        if hasGotAnswer:
            yOrN = yOrN.lower()
            if yOrN == "y":
                #exits the loop
                break
            else:
                #exits the loop and leaves the function
                endFunct = True
                break
    if endFunct:
        return 0
    #define the lists to store the info in
    priceList = []
    totalNoDiscount = 0
    totalDiscount = 0
    tableInfo = getDataFromRefs()[tableToCharge]
    orders = tableInfo[2].split("-")
    tip = 0
    discountList = []
    now = datetime.datetime.now()
    weekday = now.weekday()
    currentTime = now.strftime("%H:%M:%S")
    for i in range(int(tableInfo[1])):
        #reads off the reference and adds to the price
        match orders[i]:
            case "stan":
                priceList.append(8)
                totalNoDiscount += 8
            case "prem":
                priceList.append(12)
                totalNoDiscount += 12
            case "delu":
                priceList.append(15)
                totalNoDiscount += 15
            case _:
                print("Something went wrong, please check if the save data is corrupt")
    while weekday == 1 or weekday == 3 or weekday == 6:
        hasCard = input("Do the customers have a 'Sick' card? (Y or N): ") #checks if the day is compatible with a sick card discount and asks if they have one
        hasCard = hasCard.lower()
        if hasCard == "y" or hasCard == "n":
            break
        else:
            print("Please enter a valid value\n")
    if weekday != 1 and weekday != 3 and weekday != 6:
        hasCard = "n"
    if hasCard == "y":
        for i in range(len(orders)):
            match priceList[i]: #if the user has a sick card create the discount multipliers
                case 8:
                    discountList.append(0.9)
                case 12:
                    discountList.append(0.85)
                case 15:
                    discountList.append(0.8)
    else:
        for i in range(len(orders)):
            
            discountList.append(1)

    while True:
        #gets the tip and validates it
        tip = input("Enter tip amount: ")
        dotCount = 0
        for i in range(len(tip)):
            if tip[i] == ".":
                dotCount += 1
        if dotCount < 2:
            if tip.replace(".", "").isnumeric(): #checks if the value can be converted into a float
                if not("-" in tip):
                    tip = float(tip)
                    break
                else:
                    print("Please enter a positive number\n")
            else:
                print("Please enter a valid value\n")
        else:
            print("Please do not enter more than 1 decimal point, what are you trying to do? break the program?")
            
    print("\n\n――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――\n")
    print("      Visual Basic Diner Receipt\n") #prints out the receipt
    print("  ", currentTime, " ", tableInfo[4])
    print("\nTable", tableToCharge, "\n\n")
    print("Price Breakdown:\n")

    actualPriceList = []
    
    for i in range(len(priceList)):
        match priceList[i]:
            case 8:
                mealType = "Standard meal package"
            case 12:
                mealType = "Premium meal package"
            case 15:
                mealType = "Deluxe meal package"

        actualPriceList.append(priceList[i] * discountList[i]) #works out the actual price using the discount
        rowStr = "    " + mealType + " ...... £" + str(priceList[i]) + " x " + str(discountList[i]) + "(Sick card discount)" + " = £" + str(actualPriceList[i]) #makes a string that explains prices to the customer
        totalDiscount += actualPriceList[i]
        print(rowStr) 

    print("\n    Tip ... £" + str(tip))
    totalDiscount += tip
    totalNoDiscount += tip
    print("\nTotal ...... £", round(totalDiscount, 2))
    if hasCard == "y":
        print("Money saved with Sick card: £" +  str(round(totalNoDiscount - totalDiscount, 2)))
    print("\n――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――\n\n")

    dataRefs[tableToCharge - 1] = "null\n"
    saveFileData(dataRefs)
    
def checkOption(option):
    option = int(option)
    match option: #call a function based on the already validated user input
        case 1:
            table()
        case 2:
            seatGuestsAndOrder()
        case 3:
            getReceipt()
        case 4:
            quit()
        case _:
            print("input invalid\n")
            
def main():
    while True:
        print("‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗\n")
        print("~ Menu ~ ")
        print("1. Display all diner information \n2. Seat Guests \n3. Get receipt for a table\n4. quit")
        print("‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗‗\n")
        option = input("Please enter option: ")
        if option == "1" or option == "2" or option == "3" or option == "4" or option == "4":#runs "checkOption" if option is equal to one of the option values
            checkOption(option)
        else:
            print("Please enter a valid option\n")
            
main()