# template for "Stopwatch: The Game"

import simplegui

# define global variables
time = 0
tries = 0
wins = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    '''Formats the time'''
    tenths = t % 10
    sec = (t - tenths) // 10 % 60	
    min = (t - sec) // 600   
    return str(min) + ":" + "%02d" % sec + "." + str(tenths)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    '''Starts timer. The game begins!'''
    timer.start()
    
def stop():
    '''Stops game'''
    global tries, wins
    if timer.is_running():
        timer.stop()
        tries = tries + 1
        if time % 10 == 0:
            wins = wins + 1
            
def reset():
    '''Resets timer and points'''
    global time, tries, wins
    tries = 0
    wins = 0
    time = 0
    if timer.is_running():
        timer.stop()
    

# define event handler for timer with 0.1 sec interval
def tick():
    '''Tick-Tack!'''
    global time
    time = time + 1
    

# define draw handler
def draw(canvas):
    '''Drawing'''
    canvas.draw_text(format(time),(55,115),56,"Yellow","monospace")
    canvas.draw_text(str(wins) + "/" + str(tries),(240,30),24,"Green","monospace")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

# register event handlers
timer = simplegui.create_timer(100,tick)
frame.set_draw_handler(draw)
frame.add_button("Start",start,200)
frame.add_button("Stop",stop,200)
frame.add_button("Reset",reset,200)

# start frame
frame.start()

# Please remember to review the grading rubric
