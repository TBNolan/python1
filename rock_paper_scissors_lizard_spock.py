# Rock-paper-scissors-lizard-Spock template

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
    changes name (string) to number (int) corresponding to the choice
    """
    # delete the following pass statement and fill in your code below
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
        print "name_to_number received unexpected input"

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    """changes number (int) to name (string) of the choice """
    # delete the following pass statement and fill in your code below
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
        print "number_to_name received unexpected input"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    """
    takes input of player choice and generates random computer choice
    and calculates the winner
    """
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print ""

    # print out the message for the player's choice
    print "Player has chose", str(player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)

    # print out the message for computer's choice
    print "Computer has chose", str(comp_choice)    
    
    # compute difference of comp_number and player_number modulo five
    result = (comp_number - player_number) % 5

    # use if/elif/else to determine winner, print winner message
    if result <= 2 and result > 0:
        print str(comp_choice), "beats", str(player_choice), "Computer Wins!"
    elif result == 0:
        print "tie"
    else:
        print str(player_choice), "beats", str(comp_choice) + ".", "Player Wins!"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric