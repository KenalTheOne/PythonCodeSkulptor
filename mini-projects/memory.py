# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards, exposed, turns, state, idx1, idx2
    cards = range(0,8) + range(0,8)
    random.shuffle(cards)
    exposed = [False for x in range(0,16)]
    turns = 0
    state = 0
    idx1 = -1
    idx2 = -1
    label.set_text("Turns = 0")
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global turns, state, idx1, idx2
    for x in range(0,16):
        if pos[0] >= x * 50 and pos[0] < (x * 50 + 50):
            if not exposed[x]:
                exposed[x] = True
                if state == 1:
                    idx2 = x
                    state = 2
                else:
                    if cards[idx1] != cards[idx2]:
                        exposed[idx1] = False
                        exposed[idx2] = False
                    idx1 = x
                    state = 1
                    turns += 1
                    label.set_text("Turns = " + str(turns)) 
                               
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for x in range(0,16):
        if exposed[x]:
            canvas.draw_polygon([(x*50,0),(x*50+50,0),(x*50+50,100),(x*50,100)],1,"White","Black")
            canvas.draw_text(str(cards[x]),(7+x*50,72),72,"White","monospace")
        else:
            canvas.draw_polygon([(x*50,0),(x*50+50,0),(x*50+50,100),(x*50,100)],4,"Black","Orange")

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