while True:
    print('who are you?')
    name = input()
    if name != 'Aman':
        continue
    print('Hello aman what is the password?')
    password = input()
    if password == 'yadav':
     print('Access granted')
     break
    else:
       print('Access denied')
       