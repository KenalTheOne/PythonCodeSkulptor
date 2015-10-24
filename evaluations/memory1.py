# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    global cardlist,exposed
    global state
    global pos1,pos2,reset,turns
    turns = 0
    state = 0
    cardlist=[]
    
    label.set_text("Turns = " + str(turns))
    
    cardlist = range(8)
    cardlist.extend(range(8))
#    print cardlist
    random.shuffle(cardlist)    
#    print cardlist	
    exposed=[False for i in range(17)]
#    print exposed 
    
# define event handlers
def mouseclick(pos):

    # add game state logic here
    global state
    global pos1,pos2,cardlist,reset,turns
    
    print pos[0] / 50    
     
    pos = pos[0] / 50
    if state == 0:
    #init state    
        state = 1
        pos1 = pos
        exposed[pos1] = True
    elif state == 1:
        if not exposed[pos]:
            state = 2
            pos2 = pos
            exposed[pos2] = True
            turns += 1
    elif state == 2:
        if not exposed[pos]:
            if cardlist[pos1] != cardlist[pos2]:
                exposed[pos1] = False
                exposed[pos2] = False
            else:
                pass
            pos1 = pos
            exposed[pos1] = True
            state = 1
            
    label.set_text("Turns = " + str(turns))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cardlist,exposed
    k = 0;
    position = 50/2

    for i in cardlist:
      canvas.draw_text(str(i), (k*50+50/3, 80), 60, 'Red')
      k +=1		    
 
    for i in range(17):
      if exposed[i] == False:
        canvas.draw_line((50*i,50), (50*(i+1), 50), 100, 'Green')
#################################################################################3

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