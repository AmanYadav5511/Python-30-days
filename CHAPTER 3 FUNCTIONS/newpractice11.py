def apply_discount(price, percent):
    result = price * percent/100
    print(result)
    return price - result

print(apply_discount(800, 10))