from pickle import TRUE
import random
import sys

def play():
    playAgain = True
    while playAgain == True:
        try:
            # Allow user input to choose between rock paper or scissors same with the computer
            print("Here are the option: \nOption 1) 'r' for rock \nOption 2)'p' for paper \nOption 3)'s' for scissors")
            user = input("What's your choice?: ")
            computer = random.choice(['r', 'p', 's'])

            # Data sanitisation
            if(len(user) == 1 and user == "r" or user == "R" or user == "p" or user == "P" or user == "s" or user == "S"):
                # If user and computer chose the same, outcome = draw
                if user == computer:
                    print('It\'s a tie')
                    break 
                # Check to see whose the winner
                elif isWin(user, computer) == True:
                    print('You won!')
                    break 
                else:
                    print('You lost!')
                    break 
            else:
                raise Exception
        except:
            print("Please enter either 'r', 'p' or 's' \n")
    
    # Check to see if the user would like to play again 
    exit = input("\nWould you like to play game? Y/N: ")
    # Data sanitisation
    if(len(exit) == 1 and exit == "Y" or exit == "y" or exit == "N" or exit == "n"):
        if exit == "Y" or exit == "y":
            print(play())
        # Closing game since player do not wish to play again
        else:
            sys.exit("Quitting game")
            


# Create an helper function to decide who wins
# We know that rock beats scissors, scissors beat paper and paper beat rock
def isWin(player, opponent):
    #return true if player wins (opponent = computer in this scenario)
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

# Has to be print because of the return string ~ else you wouldnt be able to see it
print(play())
