fruits = ['apple', 'banana', 'cherry']

fruits.remove('apple')
print(fruits)

del fruits[1]
print(fruits)

removed_item = fruits.pop(0)
print('removed item from list is ',removed_item)
print(fruits)

#pop returns a value and del and remove do not