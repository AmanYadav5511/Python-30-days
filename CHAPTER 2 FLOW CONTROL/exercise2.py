#Take three numbers a, b, c and print the largest — using only if/elif/else, no max().

print('enter a, b, c.')
a = int(input())
b = int(input())
c = int(input())

if (a > b) and (a > c):
    print(' "a" is larger ')

elif (b > a) and (b > c):
    print(' "b" is larger ')

elif (c > a) and (c > b):
    print(' "c" is larger ')