import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} to high (H), too low (L), or is correctly(C)?').lower()
        if feedback ==  'h':
            high = guess - 1
        elif feedback == 'l':
              low = guess + 1
    print(f'Yay! The Computer guessed your number, {guess}, correctly!')

computer_guess(500)