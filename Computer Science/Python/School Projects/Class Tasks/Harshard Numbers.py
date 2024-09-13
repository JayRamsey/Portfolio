n = input("Enter number Harshard number in sequence: ")
HNumbers = []
currentNum = 1
while len(HNumbers) < int(n):
    currentNumDigits = str(currentNum)
    total = 0
    for i in range(len(currentNumDigits)):
        total += int(currentNumDigits[i])
    if currentNum % total == 0:
        HNumbers += str(currentNum)
    print(total)
    currentNum += 1
print(HNumbers[n], "is a Harshard number.]")

