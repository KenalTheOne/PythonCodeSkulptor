# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck, exposed, state, counter
    first_cards = [0,1,2,3,4,5,6,7]
    second_cards = [0,1,2,3,4,5,6,7]
    deck = first_cards + second_cards
    random.shuffle(deck)
    exposed = []
    for x in range(0,16):
        exposed.append(False)
    state = 0
    counter = 0
    label.set_text("Turns =" + str(counter))
    
# define event handlers
def mouseclick(pos):
    global deck, state, exposed, card1_index, card2_index, counter
    y = pos[0] // 50
    if state == 0:
        
        if exposed[y]:
            pass
        else:
            exposed[y] = True
            card1_index = y
            state = 1
            
            
    elif state == 1:
        if exposed[y]:
            pass
        else:
            exposed[y] = True
            card2_index = y
            state = 2
            counter = counter + 1
            label.set_text("Turns =" + str(counter))
          
            
            if deck[card1_index] == deck[card2_index]:
                exposed[card1_index] = True
                exposed[card2_index] = True
                state = 0
                
    elif state == 2:
        if exposed[y]:
            pass
        elif deck[card1_index] != deck[card2_index]:
            exposed[card1_index] = False
            exposed[card2_index] = False
            exposed[y] = True
            card1_index = y
            state = 1
            
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed
    i = [0, 100]
    
    for x in range(len(deck)):
        if exposed[x]:
            canvas.draw_text(str(deck[x]), i, 45, 'Red')
            i[0] = i[0] + 50
        else:
            canvas.draw_polygon([i,[i[0], i[1] - 100],[i[0] + 45, i[1] - 100],[i[0] + 45, i[1]]],5,'green','green')
            i[0] = i[0] + 50
            
    

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns =")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric