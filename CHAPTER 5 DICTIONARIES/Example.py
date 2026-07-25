birthdays = {'Alice': 'dec 12', 'Aman': 'Dec 1', 'Arun': 'April 5'}

while True:
    print('Enter a name (blank to quit)')
    name = input()

    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('No birthday found for name = '+ name)
        print('when is their birthday?')
        bday=input()
        birthdays[name]=bday
        print('Database updated')