#Guessing game: use random.randint(1, 20) to pick a secret number. Give the user 5 attempts. 
# After each guess print "too high" or "too low". If they win, print how many attempts it took. 


import random

secret = random.randint(1, 20)


for attempt in range(1, 6):
    print('Take a guess (1-20):')
    guess = int(input())

    if guess < secret:
        print('Too low')
    elif guess > secret:
        print('Too high')
    elif guess == secret:
        print('Correct! You got it in', attempt, 'guesses')
        break

else:
    print('You lost! The number was', secret)