import random

while True:
    number = random.randint(20, 30)
    print(number, "is the start number\n")
    while True:
        if number > 0:
            playerGo = True
            number -= int(input("How many would you like to remove?: "))
            print("The number is now", number, "\n")
        else:
            break
        if number > 0:
            playerGo = False
            compNumber = random.randint(1, 3)
            number -= compNumber
            print("The computer chose", compNumber)
            print("The number is now", number, "\n")
        else:
            break
    if playerGo:
        print("You lost...")
    else:
        print("You won!")
    input("\n\nPress enter to play again.")
