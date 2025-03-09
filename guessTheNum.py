#project: A game where the user guesses a random number between 1 and 10


import random

# Generate a random number
random_num = random.randint(1, 10)
print('I have picked a number between 1 to 10. Can you guess the number?')

# Now allow the user to guess the number
while True:
    guess = int(input('Enter your guess: '))
    if (guess == random_num):
        print('Congratulations! You guessed it!')
        break
    elif (guess < random_num):
        print('Too low! Try again!')
    else:
        print('Too high! Try again!')
        







