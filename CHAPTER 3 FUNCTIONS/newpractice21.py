def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    print('Enter your choice please: ')
    choice = input()
    
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input('enter first no: '))
            num2 = float(input('enter second no: '))
        except ValueError:
            print('invalid input')
            continue

        if choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))

        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))

        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))

        elif choice == '4':
            try:
              print(num1, '/', num2, '=', divide(num1, num2))
            except ZeroDivisionError:
                print('invalid operation , 0 can not be divided')
