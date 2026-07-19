#A year is a leap year if divisible by 4, except century years must 
# be divisible by 400. Write code that prints whether year is a 
# leap year. Test: 2024 (yes), 1900 (no), 2000 (yes).

print('Enter the year to check if its a leap year or not.')

year = int(input())

if year % 400 == 0:
    print('yes')

if year % 100 == 0:
    print('no')

elif year % 4 == 0:
    print('yes')

else:
    print('no')