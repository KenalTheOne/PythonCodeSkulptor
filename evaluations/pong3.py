# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
init_pos = [WIDTH / 2, HEIGHT / 2]
ball_pos = [0, 0]
ball_vel = [None, None]
pad_hit = 0
time = 0
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
score = [0, 0]
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if direction == "RIGHT":
        ball_vel = [random.randrange(120, 240) / 60.0, -random.randrange(60, 100) / 60.0]
    else:
        ball_vel = [-random.randrange(120, 240) / 60.0, -random.randrange(60, 100) / 60.0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score  # these are numbers
    global score1, score2  # these are ints
    score = [0, 0]
    spawn_ball("LEFT")

def tick():
    global time
    time = time + 1

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -5
    if key == simplegui.KEY_MAP["S"]:
        paddle1_vel = 5
    elif key == simplegui.KEY_MAP["W"]:
        paddle1_vel = -5
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["S"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["W"]:
        paddle1_vel = 0
    
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] +  ball_vel[0]
    ball_pos[1] = ball_pos[1] +  ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if abs(ball_pos[1] - paddle1_pos) <= HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score[1] += 1
            spawn_ball("RIGHT")
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if abs(ball_pos[1] - paddle2_pos) <= HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * 1.1
        else:
            score[0] += 1
            spawn_ball("LEFT")
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = paddle1_pos + paddle1_vel
    paddle2_pos = paddle2_pos + paddle2_vel
    
    if paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    
    if paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    
    if paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    
    if paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
        
    # draw paddles
    canvas.draw_polygon([(1, paddle1_pos - HALF_PAD_HEIGHT), (7, paddle1_pos - HALF_PAD_HEIGHT), (7, HALF_PAD_HEIGHT + paddle1_pos), (1, HALF_PAD_HEIGHT + paddle1_pos)], 1, 'White', 'White')
    
    canvas.draw_polygon([(593, paddle2_pos - HALF_PAD_HEIGHT), (599, paddle2_pos - HALF_PAD_HEIGHT), (599, HALF_PAD_HEIGHT + paddle2_pos), (593, HALF_PAD_HEIGHT + paddle2_pos)], 1, 'White', 'White')
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(("%d" % score[0]), [150, 50], 50, "White")
    canvas.draw_text(("%d" % score[1]), [450, 50], 50, "White")


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
but_restar = frame.add_button('Restart', new_game, 100)

# start frame
new_game()
frame.start()