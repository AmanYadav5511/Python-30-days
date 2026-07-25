def is_prime(n):
    if n < 0:
        return('negative number')
    elif n == 1:
        return('not a prime number')
    elif n % 2 == 0:
        return('it is a prime number')
    else:
        return('not a prime no')
    
print(is_prime(3))
