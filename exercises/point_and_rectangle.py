import simplegui

point = [10, 20]
vel = [3, 0.7]

def tick():
    point[0] += vel[0]
    point[1] += vel[1]

def draw(canvas):
    canvas.draw_polygon([[50, 50],[180, 50],[180, 140],[50, 140]],1,"Red")
    canvas.draw_circle(point,2,1,"Green")
    
frame = simplegui.create_frame("Test",200,200)
timer = simplegui.create_timer(100,tick)
frame.set_draw_handler(draw)

frame.start()
timer.start()