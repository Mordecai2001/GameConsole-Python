# Blackjack Game Program
# ------------------IMPORTS------------------------------------
import random
# there's a dealer in Blackjack, you play against him
# ------------------CLASS DEFINITIONS--------------------------


class Card:
    # creates card objects
    def __init__(self, s, v):  # constructor function
        # stores the suit and value
        if (s == "spades"):
            self.suit = "\u2660"
            self.suit_num = 4  # encodes the value of the suit, not needed for Blackjack
        elif (s == "hearts"):
            self.suit = "\u2661"
            self.suit_num = 3
        elif (s == "diamonds"):
            self.suit = "\u2662"
            self.suit_num = 2
        elif (s == "clubs"):
            self.suit = "\u2663"
            self.suit_num = 1
        self.value = v  # saves the value
        self.x = v  # just for display purposes
        # SCORING SYSTEM
        # assigns Blackjack values
        if (self.value == 11 or self.value == 12 or self.value == 13):  # face cards are 10
            self.BJval = 10
            self.BJval_alt = 0
        elif (self.value == 1):  # the ace can be 1 or 11
            self.BJval = 1
            self.BJval_alt = 11
        else:  # the rest have the same value
            self.BJval = self.value
            self.BJval_alt = 0

    def display(self):  # displays the card object
        # change 1,11,12,13 to A,J,Q,K
        if (self.x == 1):
            self.x = "A"
        elif (self.x == 11):
            self.x = "J"
        elif (self.x == 12):
            self.x = "Q"
        elif (self.x == 13):
            self.x = "K"
        print("[", self.suit, self.x, "]", sep='')

    def display_down(self):
        # it displays the card with the face down
        print("[  ]")


class doubleDeck:
    # creates Deck objects
    def __init__(self):  # constructor function
        self.Deck = [None]*104
        for i in range(13):
            self.Deck[i] = Card("spades", i+1)
        for i in range(13):
            self.Deck[i+13] = Card("hearts", i+1)
        for i in range(13):
            self.Deck[i+26] = Card("diamonds", i+1)
        for i in range(13):
            self.Deck[i+39] = Card("clubs", i+1)
        for i in range(13):
            self.Deck[i+52] = Card("spades", i+1)
        for i in range(13):
            self.Deck[i+65] = Card("hearts", i+1)
        for i in range(13):
            self.Deck[i+78] = Card("diamonds", i+1)
        for i in range(13):
            self.Deck[i+91] = Card("clubs", i+1)
        self.top = 0  # initializes the starting point

    def shuffle(self):  # it shuffles the deck
        for i in range(100):
            idx1 = random.randint(0, 103)
            idx2 = random.randint(0, 103)
            temp = self.Deck[idx1]
            self.Deck[idx1] = self.Deck[idx2]
            self.Deck[idx2] = temp
        # reset the top back to zero
        self.top = 0

    def displayDeck(self):  # displays the Deck object
        print("===========================")
        for i in range(104):
            if (i == self.top):
                print("------------TOP------------")
            self.Deck[i].display()
        print("===========================")

    def dealCard(self):
        x = self.Deck[self.top]
        self.top = self.top+1
        return x  # returns a Card object


class Player():
    # creates Player objects
    def __init__(self, deck):
        # creates an array of cards
        # 14 is the maximum of cards with the minimum values, if added goes beyond 21
        self.card = [None]*14
        self.card[0] = deck.dealCard()
        self.card[1] = deck.dealCard()
        self.num_cards = 2

    def hit(self, deck):
        self.card[self.num_cards] = deck.dealCard()
        self.num_cards = self.num_cards+1

    def displayPlayerCards(self):
        for i in range(self.num_cards):
            self.card[i].display()

# -------FUNCTION DEFINITIONS-------------------------


def handValue(player):
    # this function calculates the value of a hand with best ace optimization
    # step1: findinf the number of aces
    k = 0  # assume there are none, k holds the number of aces
    for i in range(player.num_cards):
        if (player.card[i].value == 1):
            k = k+1
    sum_without_aces = 0
    for i in range(player.num_cards):
        if (player.card[i].value != 1):
            sum_without_aces = sum_without_aces+player.card[i].BJval
    sum = 0
    if (k == 0):
        sum = sum_without_aces
    elif (k > 0):
        if (sum_without_aces < 11-k):
            sum = sum_without_aces+10+k
        elif (sum_without_aces == 11-k):
            sum = 21
        else:
            sum = sum_without_aces+k
    return sum


def displayHands(player, dealer):
    # this function displays the hands
    print("-----------------")
    print("--DEALER--")
    dealer.displayPlayerCards()
    print("--USER--")
    player.displayPlayerCards()
    print("-----------------")


def displayHands_down(player, dealer):
    # this function displays the hands with one of the dealer's down
    print("-DEALER-")
    dealer.card[0].display()
    dealer.card[1].display_down()
    print("-USER-")
    player.displayPlayerCards()


def winMethod(player, dealer, wallet, bet):
    # this function when performed if the player has won
    displayHands(player, dealer)
    print("You won!")
    wallet = wallet+bet
    return wallet


def lossMethod(player, dealer, wallet, bet):
    # this function is performed when the player loses
    displayHands(player, dealer)
    print("You lost!")
    wallet = wallet-bet
    return wallet


def getChoice():
    # this function gets the choice from the user
    print("-----------------")
    print("Your available choices are:")
    print("1.Hit")
    print("2.Stand")
    print("-----------------")
    choice = int(input("Enter your choice:"))
    while (choice != 1 and choice != 2):
        choice = int(input("Enter your choice:"))
    return choice


def main():
    # cards=deckCreator()#creates the deck
    # shuffle(cards)#shuffles the deck
    Deck1 = doubleDeck()  # creates the deck by calling the constructor function
    Deck1.shuffle()
    wallet = 100  # initialize the wallet with $100
    while (True):
        if (Deck1.top > 52):  # shuffle an reset the deck
            Deck1.shuffle()
            Deck1.top = 0
        # create the dealer and the player
        dealer = Player(Deck1)
        p1 = Player(Deck1)
        # BETTING
        if (wallet == 0):
            print("You lost all your money")
            break
        print("-----You have: $", wallet, sep="")
        print("-------------------------------")
        bet = float(input("Enter your bet:"))
        while (bet <= 0 or bet > wallet):  # correct accounting
            bet = float(input("Enter a valid bet:"))
        # THE DEAL
        print("-----------------")
        displayHands_down(p1, dealer)
        # check if the user already won/lost(blackjacks/naturals)
        if (handValue(p1) == 21 and handValue(dealer) != 21):
            wallet = winMethod(p1, dealer, wallet, bet)
            continue
        elif (handValue(p1) == handValue(dealer) == 21):
            wallet = lossMethod(p1, dealer, wallet, bet)
            continue
        elif (handValue(p1) != 21 and handValue(dealer) == 21):
            wallet = lossMethod(p1, dealer, wallet, bet)
            continue
        # THE PLAY
        else:
            win_loss = False  # a flag that keeps track if the user won or lost
            print("-------------------------------")
            print("--USER TURN--")
            while (True):
                choice = getChoice()
                if (choice == 1):  # chose to hit
                    p1.hit(Deck1)
                elif (choice == 2):  # if the player chooses to stand we break
                    break
                # check win condition
                if (handValue(p1) > 21):
                    wallet = lossMethod(p1, dealer, wallet, bet)
                    win_loss = True
                    break
                elif (handValue(p1) == 21):
                    wallet = winMethod(p1, dealer, wallet, bet)
                    win_loss = True
                    break
                else:  # while it's under 21
                    displayHands_down(p1, dealer)
                    if (p1.num_cards == 5):
                        wallet = winMethod(p1, dealer, wallet, bet)
                        win_loss = True
                        break
            if (win_loss == False):  # here comes the dealer's turn
                print("-------------------------------")
                print("--DEALER TURN--")
                print("-----------------")
                print("-DEALER-")
                displayHands(p1, dealer)  # now, reveal the dealer's card
                # hit until it gest at least to 17
                while (handValue(dealer) < 17):
                    dealer.hit(Deck1)
                # if the dealer's score is lower than the player's it should hit
                while (handValue(p1) > handValue(dealer)):
                    dealer.hit(Deck1)
                if (handValue(dealer) > 21):
                    wallet = winMethod(p1, dealer, wallet, bet)
                else:
                    wallet = lossMethod(p1, dealer, wallet, bet)
