# Rock-paper-scissors-lizard-Spock

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    """
    Converts name to a number
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return -1

def number_to_name(number):
    """
    Converts number to a name
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "wrong!"  

def rpsls(player_choice):
    """
    Let's play!
    """
    if name_to_number(player_choice) != -1:
        print "Player chooses " + player_choice
        player_number = name_to_number(player_choice)
        
        comp_number = random.randrange(0,5)
        comp_choice = number_to_name(comp_number)
        print "Computer chooses " + comp_choice
        
        if comp_number>=0 and comp_number<=4: #just in case...
            win_number = (comp_number - player_number) % 5
            if win_number == 1 or win_number == 2:
                print "Computer wins!"
            elif win_number == 3 or win_number == 4:
                print "Player wins!"
            else:
                print "Player and computer tie!"
        print ""
    else:
        print "Player makes wrong choice!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


