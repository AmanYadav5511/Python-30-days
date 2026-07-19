def sum_digits(number):
    total = 0
    while number > 0:
        total = total + number % 10 
        number = number // 10
    return total

print(sum_digits(1234))
