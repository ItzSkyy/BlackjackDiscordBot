import random as rand
import discord as disc
from discord.ext import commands

game_points = {
    'Ace': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

card_draw = {
    1: 'Ace',       #1, 11
    2: '2',         #2
    3: '3',         #3
    4: '4',         #4
    5: '5',         #5
    6: '6',         #6
    7: '7',         #7
    8: '8',         #8
    9: '9',         #9
    10: '10',       #10
    11: 'Jack',     #10
    12: 'Queen',    #10
    13: 'King'      #10
}

def draw_card():
    global cards
    global points
    random_index = rand.randint(1, 13)
    counter = 0
    for i in cards.values():
        counter += 1
        if counter == random_index:
            return [i, points[i]]
          
class Dealer:
    def __init__(self):
        self.score = 0
        self.cards = []
        self.turnOver = False
        self.aceCount = 0
        self.ace1Count = 0

    def hits(self): 
        card, score = draw_card()
        lastcard = len(self.cards)
        self.cards.append(card) 
        if self.cards[lastcard - 1] == "Ace":
          self.aceCount += 1
        self.score += score
        if "Ace" in self.cards and self.score > 21 and self.aceCount != self.ace1Count:
          self.score -= 10
          self.ace1Count += 1

    def showStartCards(self):
        print(f"Dealer card: {self.cards[1]}")
        
    def showStartCardsR(self):
        return(f"Dealer card: {self.cards[1]}")

    def showCards(self):
        tempcards = self.cards
        tempstring = ", ".join(tempcards)
        print(f"Dealer cards: {tempstring}")

    def showCardsR(self):
        tempcards = self.cards
        tempstring = ", ".join(tempcards)
        return(f"Dealer cards: {tempstring}")

    def showStartScore(self):
        print(f"Dealer score: {points[self.cards[1]]}")

    def showScore(self):
        print(f"Dealer score: {self.score}")

    def showStartScoreR(self):
        return(f"Dealer score: {points[self.cards[1]]}")

    def showScoreR(self):
        return(f"Dealer score: {self.score}")

 
class Player:
    def __init__(self):
        self.score = 0
        self.cards = []
        self.turnOver = False
        self.aceCount = 0
        self.ace1Count = 0
        self.name = ""
        self.bet = 0

    def setName(self, name):
        self.name = name

    def hits(self):
        card, score = draw_card()
        lastcard = len(self.cards)
        self.cards.append(card)
        if self.cards[lastcard - 1] == "Ace":
          self.aceCount += 1
        self.score += score
        if "Ace" in self.cards and self.score > 21 and self.aceCount != self.ace1Count:
          self.score -= 10
          self.ace1Count += 1 

    def stands(self):
        self.turnOver = True

    def showCards(self):
        tempcards = self.cards
        tempstring = ", ".join(tempcards)
        print(f"Player cards: {tempstring}")

    def showScore(self):
        print(f"Player score: {self.score}")

    def showCardsR(self):
        tempcards = self.cards
        tempstring = ", ".join(tempcards)
        return(f"Player cards: {tempstring}")

    def showScoreR(self):
        return(f"Player score: {self.score}")


class Game(Player, Dealer):
    def __init__(self, Player, Dealer):
        self.player = Player
        self.dealer = Dealer
        self.playerWinFlag = False
        self.dealerWinFlag = False
        self.tieFlag = False
        self.playerChoice = ""
      
    def makeInput(self):
        while self.playerChoice != "s" and self.playerChoice != "h" and p.turnOver == False:

            if self.checkBust():
                self.playerWinFlag = False
                p.turnOver = True
                self.stands()
                return 
            else:
                self.playerChoice = str(input("Hit or Stand? Choose. (H/S)"))
                self.playerChoice = self.playerChoice.lower()

            if self.playerChoice == "s":
                p.turnOver = True
                return
            elif self.playerChoice == "h":
                Player.hits(p)
                Player.showCards(p)
                Player.showScore(p)
                self.playerChoice = ""
                return

    def runGame(self):
        while (self.playerWinFlag != True
               and self.dealerWinFlag != True) and self.tieFlag != True:
            if p.turnOver == False:
                p.hits()            # Player gains a card.
                d.hits()            # Dealer gains a card.
                p.hits()            # Player gains a card.
                d.hits()            # Dealer gains a card.
                d.showStartCards()  # Displays dealer 2nd card.
                d.showStartScore()  # Displays dealer 2nd card score.
                p.showCards()       # Displays all of the player cards (in an array currently).
                p.showScore()       # Displays total player score.
                p.turnOver = False

            while p.turnOver == False:
                self.makeInput()
                self.checkStatus(d, p)
                            
            self.dealerTurn(d, p)
            self.checkStatus(d, p)

        if self.playerWinFlag == True:
            print(f"Player wins! \nPlayer Score: {p.score} \nDealer Score: {d.score}")
        
        elif self.dealerWinFlag == True:
            print(f"Dealer wins! \nDealer Score: {d.score} \nPlayer Score: {p.score}")
        
        else:
            print(f"Tie! \nPlayer Score: {p.score} \nDealer Score: {d.score}")

    def checkBust(self):
        if p.score > 21:
            self.dealerWinFlag = True
            self.playerWinFlag = False
            return True
        else:
            return False

    def checkStatus(self, dealer, player):
        if dealer.score == player.score:
            self.tieFlag = True
            return

        if p.turnOver == True and d.turnOver == True:
            if d.score > p.score or p.score > 21:
                self.dealerWinFlag = True
                return
            else:
                self.playerWinFlag = True
                return

    def dealerTurn(self, dealer, player):
        while dealer.turnOver == False:
            if dealer.score < 17 and player.score > dealer.score and player.score < 22:
                dealer.hits()
                if dealer.score > 21:
                    self.playerWinFlag = True
                    return
            else:
                dealer.turnOver = True
                return
games = []

p = Player()
d = Dealer()
g = Game(p, d)