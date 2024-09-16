import random

winCount = 0


while True:
    sequence = []
    for i in range(10):
        sequence.append(random.randint(1, 13))
    print("Starting number:", sequence[0])
    for i in range(len(sequence) - 1):
        hORl = ""
        while hORl != "H" and hORl != "L":
            hORl = input("Higher(H) or Lower(L)? ")
        if hORl == "H" and sequence[i+1] > sequence[i]:
            winCount += 1
        if hORl == "L" and sequence[i+1] < sequence[i]:
            winCount += 1
        print("Next number: ", sequence)
    if winCount == 10:
        print("You won!\n")
    else:
        print("You lost!\n")
