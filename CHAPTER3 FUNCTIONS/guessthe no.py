import random
secret = random.randint(1, 20)
print('I am guessing a number between 1 - 20')

for guessestaken in range(1, 7):
    print('take a guess')
    guess = int(input())

    if guess < secret:
        print('Too low')
    elif guess > secret:
        print('Too high')
    else:
        break

if guess == secret:
    print('Correct, you won')

else:
    print('You lost, the number is ', str(secret))