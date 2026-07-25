def power(base, exp):
    result = 1
    for i in range(exp):
        result = result * base
    print(f"{base} raised to power of {exp} is {result}")

power(3,3)