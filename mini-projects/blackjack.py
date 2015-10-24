# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 100

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

#other globals
PLAYER_LOC = (100, 400)
DEALER_LOC = (100, 100)
OUTCOME_LOC = (20, 300)
TITLE_LOC = (125, 50)
SCORE_LOC = (400, 590)
BET_LOC = (50, 590)

bet = 10

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        result = ""
        for card in self.cards:  
            result += str(card) + " " 
        return result

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        has_ace = False
        hand_value = 0
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                has_ace = True
        if not has_ace:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
   
    def draw(self, canvas, pos):
        for index in range(len(self.cards)):
            self.cards[index].draw(canvas,[pos[0] + index * CARD_SIZE[0],pos[1]])  
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        result = ""
        for card in self.cards:  
            result += str(card) + " " 
        return result  

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, hand_of_player, hand_of_dealer, score, bet
    
    if in_play:
        outcome = "You lose. Hit or stand?"
        score -= bet
    else:
        outcome = "Hit or Stand?"
        
    betinfo.set_text("")
    bet = int(betinput.get_text())    

    deck = Deck()
    deck.shuffle()
    
    hand_of_player = Hand()
    hand_of_dealer = Hand()
    for i in range(2):
        hand_of_player.add_card(deck.deal_card())
        hand_of_dealer.add_card(deck.deal_card())
        
    #print "Player's hand: " + str(hand_of_player)
    #print "Dealer's hand: " + str(hand_of_dealer)

    in_play = True

def hit():
    global in_play, hand_of_player, outcome, score, deck
 
    # if the hand is in play, hit the player
    if in_play:
        hand_of_player.add_card(deck.deal_card())
   
    # if busted, assign a message to outcome, update in_play and score
    if hand_of_player.get_value() > 21:
        in_play = False
        score -= bet
        outcome = "You have busted. New deal?"
        #print outcome
       
def stand():
    global in_play, hand_of_player, hand_of_dealer, outcome, score, deck
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while hand_of_dealer.get_value() < 17:
            hand_of_dealer.add_card(deck.deal_card())
        if hand_of_dealer.get_value() > 21:
            score += bet
            outcome = "Dealer has busted. New deal?"
        elif hand_of_player.get_value() > hand_of_dealer.get_value():
            score += bet
            outcome = "You win! New deal?"
        else:
            score -= bet
            outcome = "Dealer wins. New deal?"
        in_play = False
    #print outcome

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global in_play, outcome, score, bet
    hand_of_player.draw(canvas,PLAYER_LOC)
    hand_of_dealer.draw(canvas,DEALER_LOC)
    if in_play:
        canvas.draw_image(card_back, 
                          CARD_CENTER, CARD_SIZE,
                          (DEALER_LOC[0] + CARD_CENTER[0], DEALER_LOC[1] + CARD_CENTER[1]), CARD_SIZE
                         )
    canvas.draw_text(outcome,((600 - (len(outcome) * 20)) / 2,OUTCOME_LOC[1]),36,"White","monospace")
    canvas.draw_text("BLACKJACK",TITLE_LOC,72,"Yellow","monospace")
    canvas.draw_text("Score: $" + str(score), SCORE_LOC, 24, "White", "monospace")
    canvas.draw_text("Bet is $" + str(bet), BET_LOC, 24, "White", "monospace")
    
    canvas.draw_text("Your hand:",(100,395),24,"White","monospace")
    canvas.draw_text("Dealer's hand:",(100,95),24,"White","monospace")

# input bet handler
def set_bet(bet_text):
    global bet
    curbet = bet 
    try:   
        newbet = int(bet_text)
        if newbet < 1 or newbet > 100:
            betinput.set_text(str(curbet))
            newbet = curbet
        if curbet != newbet:
            betinfo.set_text("Bet will be changed in next deal")        
    except ValueError:
        betinput.set_text(str(curbet))
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

betinput = frame.add_input("Bet (from $1 to $100): ", set_bet, 200)
betinfo = frame.add_label("",250)

# get things rolling
betinput.set_text(str(bet))
deal()
frame.start()


# remember to review the gradic rubric