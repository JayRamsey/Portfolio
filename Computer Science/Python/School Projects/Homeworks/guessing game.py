NumberToGuess = 0
while NumberToGuess < 1:
    NumberToGuess = int(input("Player one enter a number: "))

Guess = 0
GuessCount = 0

while Guess != NumberToGuess and GuessCount < 3:
    Guess = int(input("Player two have a guess: "))
    GuessCount += 1
if Guess == NumberToGuess:
    print("Player two wins")
else:
    print("Player one wins")
