allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches' : 3, 'apples':2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def TotalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought are : ')
print('Apples         ' + str(TotalBrought(allGuests, 'apples')))
print('Cups         ' + str(TotalBrought(allGuests, 'cups')))
print('Cakes        ' + str(TotalBrought(allGuests, 'cakes')))
print('Ham sandwiches        ' + str(TotalBrought(allGuests, 'ham sandwiches ')))
print('Apple pies        ' + str(TotalBrought(allGuests, 'apple pies')))