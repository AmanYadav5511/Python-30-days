import random

secret = random.randint(1, 50)
for attempt in range(1, 8):
    print('Take a guess')
    guess = int(input())

    if guess < secret:
      print('too low')

    elif guess > secret:
       print('Too high')

    elif guess == secret:
       print('Correct you won')
       break

else:
   print('you lost, the secret was', secret)