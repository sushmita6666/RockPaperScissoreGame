import random

def play():
    user = input("What's your Choice?\n'r' or 'R' for rock, 'p' or 'P' for paper, 's' or 'S' for scissors\n")
    computer = random.choice(['r','p','s','R','P','S'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, opponent):
    if (player in 'rR' and opponent in 'sS') or (player in 'sS' and opponent in 'pP') or (player in 'pP' and opponent in 'rR'):
        return True

print(play())