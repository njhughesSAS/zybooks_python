# TODO: Import the random module
import random

def number_guess(num):
    # TODO: Get a random number between 1-100
    guess = random.randint(1, 100)
    # TODO: Read numbers and compare to random number
    if num == guess:
        print('{} is correct!'.format(guess))
    elif num < guess:
        print('{} is too low. Random number was {}.'.format(num, guess))
    elif num > guess:
        print('{} is too high. Random number was {}.'.format(num, guess))
        
if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    # Convert the string tokens into integers
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        number_guess(num)
