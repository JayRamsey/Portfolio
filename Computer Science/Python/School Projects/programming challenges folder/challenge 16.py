import random

while True:
    input("Press enter to start.")
    n = random.randint(1, 100)
    guessNumber = 0
    while True:
        guess = 0
        while -1 < guess < 101:
            guess = int(input("Enter a guess: "))
        guessNumber += 1
        if guess > n:
            print("Too high! Try again.")
        if guess < n:
            print("Too low! Try again.")
        if guess == n:
            print("Correct! You guessed the number in", guessNumber, "Guesses")
