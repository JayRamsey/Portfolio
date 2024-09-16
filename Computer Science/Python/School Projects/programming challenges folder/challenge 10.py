import random

def draw():
    print("You drew with the computer.\n")
def win():
    print("You won!\n")
def lose():
    print("You lost :(\n")
while True:
    response = ""
    while response.lower() != "rock" and response.lower() != "paper" and response.lower() != "scissors":
        response = input("Enter rock, paper or scissors\n")
    randomCase = random.randint(1, 3)
    match randomCase:
        case 1:
            compResponse = "rock"
        case 2:
            compResponse = "paper"
        case 3:
            compResponse = "scissors"
    if compResponse == "rock":
        if response == "paper":
            win()
        elif response == "scissors":
            lose()
        elif response == "rock":
            draw()
    elif compResponse == "paper":
        if response == "paper":
            draw()
        elif response == "scissors":
            win()
        elif response == "rock":
            lose()
    elif compResponse == "scissors":
        if response == "paper":
            lose()
        elif response == "scissors":
            draw()
        elif response == "rock":
            win()

