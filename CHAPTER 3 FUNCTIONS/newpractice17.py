def safe_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Error: invalid argument')

print(safe_divide(10,2))
print(safe_divide(8,2))
print(safe_divide(0,0))
print(safe_divide(1,2))