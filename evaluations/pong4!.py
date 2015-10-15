# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel = [10, -5]
ball_pos = [WIDTH / 2, HEIGHT / 2]
direction = random.choice([LEFT, RIGHT])
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
acc = 5

# spawn with random-ness
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == False:
        ball_vel = [random.randrange(1,5), -random.randrange(1,5)]
    else:
        ball_vel = [-random.randrange(1,5), -random.randrange(1,5)]

# define event handlers
def new_game():
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0.0
    paddle2_vel = 0.0
    spawn_ball(random.choice([LEFT, RIGHT]))    

# draw handler    
def draw(canvas):
    global score1, score2 
    global ball_pos, ball_vel, PAD_WIDTH, bal_vel
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # print ball_pos   
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # colissions, reflections and scoring 
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:	
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]  
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:   
            direction = LEFT
            spawn_ball(direction)
            score2 += 1          
     
    if ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS:
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
        else:   
            direction = RIGHT
            spawn_ball(direction)
            score1 += 1                  
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel    
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")

    canvas.draw_text(str(score1), (235, 40), 36, 'White', 'monospace')
    canvas.draw_text(str(score2), (350, 40), 36, 'White', 'monospace')


# keydown handler

def keydown(key):
    global paddle1_vel, paddle2_vel, acc

    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc

# keyup handler    
def keyup(key):
    global paddle1_vel, paddle2_vel, acc

    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= acc

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Reset', new_game)

# start frame
new_game()
frame.start()
