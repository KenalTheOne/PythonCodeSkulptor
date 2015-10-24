# implementation of card game - Memory

import simplegui
import random
NUM_GRID = 16
pos_cards = {}
num_arr = {}
pos_num = []
count = 0

# helper function to initialize globals
def new_game():
    global num_arr, state, pos_cards, pos_num
    state = 0
    pos_cards = {}
    num_arr = {}
    pos_num = []
    for i in (0, 1):
        numbers = range(0,NUM_GRID/2)
        random.shuffle(numbers)
        for number in numbers:
            num_arr[len(num_arr)] = number

# define event handlers
def mouseclick(pos):
    global state, count
    # add game state logic here
    for idx, pos_card in pos_cards.items():
        if pos_card[0][0]<= pos[0] <= pos_card[1][0] and pos[1] <= pos_card[3][1]:
            is_exist = False
            for pos in pos_num:
                if pos_card == pos[2]:
                    is_exist = True
            if not is_exist:
                count +=1
                label.set_text("Turns = "+ str(count))
                pos_num.append([num_arr[idx],[pos_card[1][0] -35, 65], pos_card])
                if state == 0:
                    state = 1
                elif state == 1:
                    if pos_num[len(pos_num)-1][0] == pos_num[len(pos_num)-2][0]:
                        state = 0
                        count -= 2
                        if count == 0:
                            new_game()
                    else:
                        state = 2
                else:
                    state = 1
                    pos_num.pop(len(pos_num)-2)
                    pos_num.pop(len(pos_num)-2)
            
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global pos_cards
    for x in range(NUM_GRID):
        pos_card = [[x * 50, 0], [x * 50 + 50, 0], [x * 50 + 50, 100],[x * 50, 100]]
        pos_cards[x] = list(pos_card)
        
    for idx, pos_card in pos_cards.items():
        canvas.draw_polygon(pos_card, 1, 'black', 'Green')
        
    for num in num_arr:
        for pos in pos_num:
            if num == pos[0] :
                canvas.draw_text(str(num_arr[num]), pos[1], 40, 'White')
        
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