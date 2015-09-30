import simplegui

x = 5

def key_down(key):
    global x
    if key == simplegui.KEY_MAP["space"]:
        x *= 2
    
    
def key_up(key):
    global x
    if key == simplegui.KEY_MAP["space"]:
        x -= 3
        print x

frame = simplegui.create_frame("Test",1,1)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.start()
