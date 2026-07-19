#Collatz sequence (the actual ATBS chapter exercise, harder version): ask for a number. While it's not 1 — 
# if even, halve it; if odd, multiply by 3 and add 1.
# Print each step AND count how many steps it took to reach 1.

attempts = 0
print('enter a number.')
number = int(input())

while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    print(number)
    attempts += 1

print('Steps taken:' , attempts)