#Skip and stop (mirrors Q4 + Q5 combined)
#Print numbers 1 to 100, but: skip multiples of 7 with continue, and the moment you reach a number bigger than 60, print "Stopping here" and break.

for num in range(1, 101):
    if num % 7 == 0:
        continue
    print(num)
    if num > 60:
        print('Stopping here')
        break