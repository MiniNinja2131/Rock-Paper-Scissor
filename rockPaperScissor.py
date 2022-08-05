import random

def play():
    # Allow user input to choose between rock paper or scissors same with the computer
    print("Here are the option: \nOption 1) 'r' for rock \nOption 2)'p' for paper \nOption 3)'s' for scissors")
    user = input("What's your choice?: ")
    computer = random.choice(['r', 'p', 's'])

    # If user and computer chose the same, outcome = draw
    if user == computer:
        return 'It\'s a tie'

    if isWin(user, computer) == True:
        return 'You won!'
    return 'You lost!'

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
