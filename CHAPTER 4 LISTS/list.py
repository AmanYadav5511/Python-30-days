catnames = []
while True:
    print('Enter the name of cat ' + str(len(catnames) + 1))
    name= input()
    if name == '':
     break
    
    catnames = catnames + [name]
print('The cat names are ' + name)
for name in catnames:
     print(' ' + name)
