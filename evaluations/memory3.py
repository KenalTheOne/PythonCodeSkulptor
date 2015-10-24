# implementation of card game - Memory
# http://www.codeskulptor.org/#user40_F48x5pNRxX_0.py

import simplegui
import random

BUFFER = 10
NUM_CARDS = 16
CARD_SIZE = (50, 100)
CARD_INIT_POS = (BUFFER, BUFFER)
FRAME_SIZE = ( (NUM_CARDS * CARD_SIZE[0]) + (2 * BUFFER),
               (CARD_SIZE[1] + (2 * BUFFER)) )

cards = []
exposed = []
turns = 0
checked_cards = []

def get_label_text():
    return "Turns = " + str(turns)

def generate_exposed():
    '''Generates a list of 16 False values

        :returns list of False values
    '''
    return [False for num in range(0, 16)]

def generate_list():
    '''Generates a shuffled list of integers in the range of [0, 8)

        :returns shuffled list
    '''
    new_list = [num for num in range(0, 8)]
    random.shuffle(new_list)
    return new_list

def merge_lists(a, b):
    '''Merges two lists into a single list

        :param a list a
        :param b list b

        :returns merged version of list b into list a
    '''
    return [item for pair in zip(a, b) for item in pair]

def new_game():
    '''Resets all game logic'''
    global cards, exposed, turns, checked_cards
    turns = 0
    label.set_text(get_label_text())
    cards = merge_lists(generate_list(), generate_list())
    checked_cards = []
    exposed = generate_exposed()

def clicked_card(pos):
    '''Returns the index of the card that was clicked

        :param pos position of the mouse click

        :returns the index of the card that was clicked or None if the click was out of bounds
    '''
    if (    pos[1] >= CARD_INIT_POS[1] # Y axis
        and pos[1] <= CARD_INIT_POS[1] + CARD_SIZE[1]):
        if (     pos[0] >= CARD_INIT_POS[0] # X axis
             and pos[0] <= (CARD_INIT_POS[0] + (NUM_CARDS * CARD_SIZE[0])) ):
            return (pos[0] - BUFFER) // CARD_SIZE[0]

    return None

def mouseclick(pos):
    '''Exposes and unexposed card value, keeps track of turns, and flips cards back over if a match
       hasn't been found.
       NOTE - the state logic from class has been replaced with a simple, single list to track checked cards

       :param pos position of the mouse click
    '''
    global label, exposed, turns

    clicked_card_index = clicked_card(pos)

    if (clicked_card_index is not None) and (not exposed[clicked_card_index]):
        exposed[clicked_card_index] = True
        checked_cards.append(clicked_card_index)
        if (len(checked_cards) == 2):
            turns += 1
        if (len(checked_cards) == 3):
            if (cards[checked_cards[0]] != cards[checked_cards[1]]):
                exposed[checked_cards[0]] = False
                exposed[checked_cards[1]] = False
            checked_cards.pop(0)
            checked_cards.pop(0)

    label.set_text(get_label_text())

def draw(canvas):
    for i, card in enumerate(cards):
        new_card_pos = ( (CARD_INIT_POS[0] + (i * CARD_SIZE[0]) ), CARD_INIT_POS[1] )
        new_text_pos = ( new_card_pos[0], new_card_pos[1] + CARD_SIZE[1] )
        if exposed[i]:
            canvas.draw_text(str(card), new_text_pos, CARD_SIZE[1], 'Yellow')
        else:
            canvas.draw_polygon([ [new_card_pos[0], new_card_pos[1]]
                                , [new_card_pos[0] + CARD_SIZE[0], new_card_pos[1]]
                                , [new_card_pos[0] + CARD_SIZE[0], new_card_pos[1] + CARD_SIZE[1]]
                                , [new_card_pos[0], new_card_pos[1] + CARD_SIZE[1]]
                                ], 1, 'Yellow', 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", FRAME_SIZE[0], FRAME_SIZE[1])
frame.add_button("Reset the Game", new_game)
label = frame.add_label(get_label_text())

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

