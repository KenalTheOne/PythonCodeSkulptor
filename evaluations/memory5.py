# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards, exposed, turns, state
    turns = state = 0
    cards = range(8) + range(8)
    random.shuffle(cards)
    exposed = [False for i in range(16)]
    label.set_text('Turns = ' + str(turns))

      
# define event handlers
def mouseclick(pos):
    global cards, clicked_card, exposed, turns, label, state, card1, card2
    # add game state logic here
    clicked_card = pos[0] // 50
    if not exposed[clicked_card]:
        if state == 0:
            state = 1
            card1 = clicked_card
            exposed[clicked_card] = True
        elif state == 1:
            state = 2
            card2 = clicked_card
            exposed[clicked_card] = True
            turns +=1
            label.set_text('Turns = ' + str(turns))
        else:
            state = 1
            exposed[card1] = exposed[card2] = (cards[card1] == cards[card2])
            exposed[clicked_card] = True
            card1 = clicked_card

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    pos = 10
    n = 0
    for num in cards:
        if exposed[n]:
            canvas.draw_text(str(num), [pos, 65], 60, "White")
        else:
            x = n * 50
            canvas.draw_polygon([(x, 0), (x, 100), (x+50, 100), (x+50, 0)], 1, 'Green', 'Green')
            canvas.draw_line([n * 50, 0], [n * 50, 100], 3, "Black")
        pos += 50
        n += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric