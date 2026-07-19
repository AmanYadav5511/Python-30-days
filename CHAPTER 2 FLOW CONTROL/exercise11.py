#Print this pattern using nested loops:

#*
#**
#***
#****
#*****

for row in range(1, 6, 1):          # outer loop: rows 1,2,3,4,5
    for star in range(row):      # inner loop: runs 'row' times
        print('*', end='')       # print one star, stay on same line
    print()       