allGuests = { 'Alice': {'apples': 7, 'pretzels': 12},
'Carol':{'ham sandwiches': 3, 'apple': 2},
 'Bob':{'cups': 3, 'apple pies': 2}}

def totalBrought(guests,item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item , 0)
    return numBrought
    
print('total items brought were = ')
print(' - Apples.    '+ str(totalBrought(allGuests, 'apples')))
print(' - PRETZELS.    '+ str(totalBrought(allGuests, 'pretzels')))
print(' - Ham sandwich.    '+ str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Cups.    '+ str(totalBrought(allGuests, 'cups')))
print(' - Apple pies.    '+ str(totalBrought(allGuests, 'apple pies')))