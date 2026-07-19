#FizzBuzz: print 1 to 30. Multiples of 3 → "Fizz", 
#multiples of 5 → "Buzz", both → "FizzBuzz". Classic interview question, do it clean

for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:
        print(num,'FizzBuzz')

    elif num % 3 == 0:
        print(num,'Fizz')

    elif num % 5 == 0:
        print(num,'Buzz')

    else:
        print(num)