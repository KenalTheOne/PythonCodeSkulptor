#!/usr/bin/env python
# Implementation of classic arcade game Pong

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

# initialize globals - pos and vel encode vertical info for paddles
    # CONSTANTS
X = 0
Y = 1
LEFT = False
RIGHT = True

    # DIMENSIONS
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

    # Variables
paddle1_pos = HEIGHT // 2
paddle2_pos = HEIGHT // 2
paddle1_vel = 0.0
paddle2_vel = 0.0
count1 = 0			# paddle 1 velocity factor
count2 = 0
score1 = 0
score2 = 0
out_left = False
out_right = False
ball_pos = [WIDTH //2, HEIGHT // 2]
ball_vel = [0, 0]
is_paused = False

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global count1, out_left, out_right, score1, score2
    ball_pos = [WIDTH //2, HEIGHT // 2]
    # lets hesitate before the ball launches
    """ Actually this doesn't work on CodeSkulptor so let's disable it here
    ball_vel = [0, 0]
    count1 = 0
    timer1.start()
    while count1 < 12 :
        continue
    timer1.stop()
    count1 = 0
    """

    if out_left :
        score2 += 1
        out_left = False
    elif out_right :
        score1 += 1
        out_right = False
        
    ball_vel = [ random.randrange(120,240), -random.randrange(0,180) ]
    if direction :
        pass
    else :
        ball_vel[X] = - ball_vel[X]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global  pos, vel        # these are lists (pairs) of floats

    score1 = score2 = 0
    spawn_ball( random.randrange(0,2) )

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
    global out_left, out_right

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    if ball_pos[Y] < BALL_RADIUS or ball_pos[Y] > HEIGHT-BALL_RADIUS :
        ball_vel[Y] = -ball_vel[Y]
    if ball_pos[X] < BALL_RADIUS :
        spawn_ball( RIGHT )
    if ball_pos[X] > WIDTH - BALL_RADIUS :
        spawn_ball( LEFT )

    ball_pos[X] += ball_vel[X] / 60.0
    ball_pos[Y] += ball_vel[Y] / 60.0

    # draw ball
    canvas.draw_circle( ball_pos, BALL_RADIUS, 1, "Red", "White")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_vel < 0.0 and paddle1_pos <= HALF_PAD_HEIGHT :
        paddle1_vel = 0.0
    if paddle1_vel > 0.0 and paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT :
        paddle1_vel = 0.0

    if paddle2_vel < 0.0 and paddle2_pos <= HALF_PAD_HEIGHT :
        paddle2_vel = 0.0
    if paddle2_vel > 0.0 and paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT :
        paddle2_vel = 0.0

    paddle1_pos += paddle1_vel / 60.0
    paddle2_pos += paddle2_vel / 60.0

    # draw paddles
    lf = PAD_WIDTH // 2 - 1
    canvas.draw_line((lf, paddle1_pos-HALF_PAD_HEIGHT),
        (lf, paddle1_pos+HALF_PAD_HEIGHT), PAD_WIDTH, 'Red')
    rt = WIDTH - PAD_WIDTH // 2
    canvas.draw_line((rt, paddle2_pos-HALF_PAD_HEIGHT),
        (rt, paddle2_pos+HALF_PAD_HEIGHT), PAD_WIDTH, 'Blue')

    # determine whether paddle and ball collide
    top = paddle1_pos - HALF_PAD_HEIGHT
    bot = paddle1_pos + HALF_PAD_HEIGHT
    if ball_pos[X] <= PAD_WIDTH + BALL_RADIUS :
        if ball_pos[Y] > top and ball_pos[Y] < bot :
            ball_vel[X] = 1.1 * abs( ball_vel[X] )
            ball_vel[Y] *= 1.1
        else :
            out_left = True

    top = paddle2_pos - HALF_PAD_HEIGHT
    bot = paddle2_pos + HALF_PAD_HEIGHT
    if ball_pos[X] >= WIDTH - PAD_WIDTH - BALL_RADIUS :
        if ball_pos[Y] > top and ball_pos[Y] < bot :
            ball_vel[X] = -1.1 * abs( ball_vel[X] )
            ball_vel[Y] += 1.1
        else :
            out_right = True

    # draw scores
    canvas.draw_text(str(score1), ( WIDTH//2-64, 32), 32, 'Gray')
    canvas.draw_text(str(score2), (WIDTH//2+40, 32), 32, 'Gray')
    
def keydown(key):
    global paddle1_vel, paddle2_vel

    acc = 240
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
        timer2.start()
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
        timer2.start()
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
        timer1.start()
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
        timer1.start()


def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["up"]:
        timer2.stop()
        paddle2_vel = 0
    if key==simplegui.KEY_MAP["down"]:
        timer2.stop()
        paddle2_vel = 0
    if key==simplegui.KEY_MAP["w"]:
        timer1.stop()
        paddle1_vel = 0
    if key==simplegui.KEY_MAP["s"]:
        timer1.stop()
        paddle1_vel = 0

def timer1_handler():
    global count1
    count1 += 1

def timer2_handler():
    global count2
    count2 += 1

def reset_button_handler() :
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Reset', reset_button_handler )
timer1 = simplegui.create_timer(20, timer1_handler)
timer2 = simplegui.create_timer(20, timer2_handler)


# start frame
new_game()
frame.start()

