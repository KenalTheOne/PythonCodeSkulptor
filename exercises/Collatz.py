import simplegui

# global state


# helper functions

def init(start):
    global result
    result = start
    print "Input is", result
    
def get_next(current):
    if current % 2 == 0:
        current = current / 2
    else:
        current = current * 3 + 1
    return current

# timer callback

def update():
    global result
    result = get_next(result)
    print str(result)
    # Stop iterating after max_iterations
    if result == 1:
        timer.stop() 
        
# register event handlers

timer = simplegui.create_timer(1, update)

# start program
init(23)
timer.start()