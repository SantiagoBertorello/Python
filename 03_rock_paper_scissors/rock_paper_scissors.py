import random

def play():
    user =  input("What\'s your choice?'r' for rock, 'p' for paper, or 's' for scissors\n")
    computer =  random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie. Again,'

        
    
    if is_win(user, computer):
        return(f"You won! computer choice {computer}")
    
    return(f'You lost computer choice {computer}')

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    
print(play())
