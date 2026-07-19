def collatz(number):
    
        if number % 2 == 0:
            result = number //2
            print(result)
            return result
        else:
            result = number * 3 + 1
        print(result)
        return result

try:       
    number = int(input('enter a number '))  
    while number != 1:
       number = collatz(number)
except ValueError:
    print('Nigga: You must enter a integer,')