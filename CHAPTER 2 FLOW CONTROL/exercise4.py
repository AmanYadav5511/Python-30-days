#Use a while loop to keep asking the user for a password until 
# they type "scorpio". After 3 wrong attempts, print "Locked out" and break.

attempts = 0

while True:

    print('Enter the password')
    password = input()

    attempts += 1

    if password == 'scorpio':
       print('access granted')
       break

    elif attempts == 3:
        print('locked out')
        break