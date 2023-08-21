import random # Will need this!

# Constants for each player selection
ROCK     = 'rock'
PAPER    = 'paper'
SCISSORS = 'scissors'

def get_computer_rps():
    # Get random RPS selection, return string
    random_int = random.randint(1,3)
    if random_int == 1:
        return ROCK
    if random_int == 2:
        return PAPER
    return SCISSORS

def get_user_rps():
    # Get user RPS, ensure is valid, return string
    selection = ''
    while selection != ROCK and selection != PAPER and selection != SCISSORS:
        selection = input('Enter rock, paper, or scissors: ')
    return selection

def result_check(user, computer):
    # Two string parameters, determine who won or if there was a tie.
    if user == computer:
        print('TIE')
    elif (user == PAPER and computer == ROCK)    or  (user == ROCK and computer == SCISSORS) or  (user == SCISSORS and computer == PAPER): 
        print('USER WON')
    else:
        print('COMPUTER WON')

def main():
    # Get user input, Get random computer RPS, 
    # Print whether or not user won
    user_choice = get_user_rps()
    computer_choice = get_computer_rps()
    result_check(user_choice, computer_choice)

main()