#Ask the user for a number n, then 
#print whether it's prime. Use a for loop with break. Test: 2, 7, 15, 1.

print('Enter a number.')
n = int(input())

if n < 2:                      # 1, 0, negatives are not prime by definition
    print(n, 'is not prime')
else:
    is_prime = True            # assume prime until proven guilty

    for i in range(2, n):      # try divisors 2, 3, 4, ... n-1
        if n % i == 0:         # divides evenly? found a divisor
            is_prime = False   # flip the flag
            break              # no point checking further

    if is_prime:               # loop finished, ask the flag
        print(n, 'is prime')
    else:
        print(n, 'is not prime')