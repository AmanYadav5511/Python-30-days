fruits = ['mango','banana','kiwi']
print('enter fruit name = ')
name = input()
if name in fruits:
    print('Found it at position ', fruits.index(name))
else:
    print('Not found')