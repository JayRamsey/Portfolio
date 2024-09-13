import random

class player:

    def __init__(self, name):
        self.name = name
        self.currentCard = None

def getDeck():
    cards = ["2","3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["hearts", "Diamonds", "Clubs", "Spades"]
    deck = []
    for suit in range(len(suits)):
        for card in range(len(cards)):
            deck.append(cards[card] + " of " + suits[suit])
    return deck

def shuffle():
    deck = getDeck()
    indexes = [i for i in range(len(deck))]
    newIndexes = []
    newDeck = []
    while len(newIndexes) < 52:
        newIndexes.append(indexes.pop(random.randint(0, len(indexes)-1)))

    for i in range(len(deck)):
        newDeck.append(deck[newIndexes[i]])
        
    return newDeck
    
def drawCards():
    card1 = shuffle()[0]
    card2 = shuffle()[1]
    
    return card1, card2

def getWinner(card1, card2):
    cardType1 = card1.split()[0]
    cardType2 = card2.split()[0]
    match cardType1:
        case "Jack":
            score1 = 11
        case "Queen":
            score1 = 12
        case "King":
            score1 = 13
        case "Ace":
            score1 = 14
        case _:
            score1 = int(cardType1)
    match cardType2:
        case "Jack":
            score2 = 11
        case "Queen":
            score2 = 12
        case "King":
            score2 = 13
        case "Ace":
            score2 = 14
        case _:
            score2 = int(cardType2)
    if score1 > score2:
        print("Player 1 won!\n")
    elif score1 != score2:
        print("Player 2 won!\n")
    if score1 == score2:
        print("It was a draw\n")
    print("Player 1 got a", card1, "and player 2 got a", card2)
    
def main():
    while True:
        player1 = player(input("Enter Player 1's name: "))
        player2 = player(input("Enter Player 2's name: "))
        input("Press enter to generate cards.\n")

        player1.currentCard, player2.currentCard = drawCards()
        getWinner(player1.currentCard, player2.currentCard)
main()
