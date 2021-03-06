# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

min = 0
max = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global min, max, attempts, secret
   
    secret = random.randrange(min, max)
    attempts = math.trunc(math.ceil(math.log(max - min + 1, 2)))
    
    print
    print "New game. Range is from " + str(min) + " to " + str(max)
    print "Number of remaining guesses is " + str(attempts)    

# define event handlers for control panel
def range100():
    # button that changes the range to [min,100) and starts a new game  
    global max
    max = 100
    new_game()
    

def range1000():
    # button that changes the range to [min,1000) and starts a new game     
    global max
    max = 1000
    new_game()

    
def input_guess(guess):
    # main game logic goes here	
    global secret, attempts
    
    attempts = attempts - 1
    
    print
    print "Guess was " + guess
    print "Number of remaining guesess is " + str(attempts)

    try:
        if attempts == 0 and int(guess) != secret:
            print "You are ran out of guesses. The number was " + str(secret)
            new_game()
        elif int(guess) < secret:
            print "Higher!"
        elif int(guess) > secret:
            print "Lower!"           
        else:
            print "Correct!"
            new_game()
    except ValueError:
        print "Invalid number!"
    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
btn100 = frame.add_button("Range is [" + str(min) + ",100)",range100,200)
btn1000 = frame.add_button("Range is [" + str(min) + ",1000)",range1000,200)
inp = frame.add_input("Enter a guess",input_guess,195)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
