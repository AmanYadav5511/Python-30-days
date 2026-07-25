def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
       result = 3 * number + 1
       print(result)
       return result
    
try:
     number = int(input('enter a number '))
     count = 0
     while number != 1:
        number = collatz(number)
        count += 1
     print('steps taken = ' + str(count))
except ValueError:
    print('please follow the commands, it has aksed for a number')
 