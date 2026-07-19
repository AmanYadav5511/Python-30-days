#Print numbers 1 to 50, but skip multiples of 4 using continue.

for num in range(1, 51):
    if num % 4 == 0:
        continue
    print(num)