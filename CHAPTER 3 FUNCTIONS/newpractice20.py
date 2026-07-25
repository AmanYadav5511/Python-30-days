def sum_digits(n):
    total_addition = 0
    leftout = abs(n)

    while leftout > 0:
        last_digit = leftout % 10
        total_addition += last_digit
        leftout //= 10
    print(total_addition)
    return total_addition

sum_digits(1234)
