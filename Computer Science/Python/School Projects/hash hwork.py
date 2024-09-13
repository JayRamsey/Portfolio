def folding(number):
    numStr = ""
    for i in range(0, len(number) - 1, 2):
        numStr += str(int(number[i]) + int(number[i + 1]))
    if len(number) <= 2:
        return int(number) % 23
    else:
        return int(folding(numStr))
        
def midSquare(number):
    numStr = str(number)
    middleStart = (len(numStr) // 2) - 1
    number = pow(int(numStr[middleStart] + numStr[middleStart + 1]), 2)
    return number % 23
    


while True:
    while True:
        option = input("Would you like to use a folding algorithm (FOLD) or a mid-square algorithm (MID): ").upper()
        if option == "FOLD" or option == "MID":
            break
    while True:
        number = input("Enter a number to hash: ")
        if number.isdigit():
            break

    if option == "FOLD":
        value = folding(number)
    else:
        value = midSquare(number)

    print("The hashed value is:", value)
